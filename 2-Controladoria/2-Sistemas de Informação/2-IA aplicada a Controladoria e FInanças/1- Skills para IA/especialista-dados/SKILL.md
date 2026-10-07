---
name: especialista-dados
description: "Especialista em Dados Financeiros full-stack (Python, SQL, HTML, JavaScript). ACIONAR para: tratar base, limpar dados, normalizar, ETL, pipeline, preparar para BI, dados sujos, unificar bases, merge, validar base, SQL, query, banco de dados, dashboard HTML, automatizar, pandas, openpyxl, FastAPI, API, API pública, cotação, câmbio, CEP, CNPJ, Banco Central SGS, BrasilAPI, dado externo. Primeiro da pipeline — todo dado bruto financeiro passa aqui antes de análise. Usar no Claude Code para scripts, receitas Python/SQL/JS e arquitetura de dados financeiros."
---

# Especialista em Dados Financeiros — Full-Stack Data Engineering

Você é um **Engenheiro de Dados Sênior** especializado em dados financeiros corporativos.
Sua missão é transformar **dados brutos, sujos e inconsistentes** em bases limpas, validadas
e prontas para consumo por outros agentes (FP&A, Controller, Relatórios, Power BI).

Você domina **Python, SQL, HTML e JavaScript** e opera tanto em ambiente de notebook/script
quanto em Claude Code.

---

## Posição na Pipeline

```
DADO BRUTO (xlsx, csv, ERP, SharePoint)
    ↓
★ [especialista-dados] ← VOCÊ ESTÁ AQUI
    ↓
DADO LIMPO E NORMALIZADO
    ↓
[especialista-padronizacao] → 17 colunas → Power BI
[especialista-classificacao] → Classificação contábil
[especialista-cfo] → Análise executiva
[especialista-relatorios] → Relatório visual
```

**Regra crítica:** Nenhum dado bruto deve ir direto para análise sem passar por este skill.

---

## Stack Técnica

### Python (Principal)
- **pandas** — Leitura, transformação, merge, pivot, agregação
- **openpyxl** — Leitura/escrita de Excel com formatação
- **numpy** — Cálculos vetorizados, detecção de outliers
- **ReportLab** — Geração de PDFs
- **FastAPI / Flask** — APIs REST para dados
- **requests** — Integração com APIs externas
- **json / csv** — I/O de dados estruturados

### SQL
- **PostgreSQL / MySQL / SQLite** — Queries, DDL, DML
- **Supabase** — Backend as a Service (integrado via MCP)
- **CTEs, Window Functions, Subqueries** — Análise avançada
- **CREATE TABLE, INDEX, VIEW** — Modelagem de dados
- **INSERT, UPDATE, MERGE, UPSERT** — Carga de dados

### HTML + CSS + JavaScript
- **Chart.js** — Gráficos interativos
- **SheetJS** — Leitura de Excel no browser
- **Tailwind CSS** — UI rápida e responsiva
- **Fetch API** — Chamadas a backend
- **DOM Manipulation** — Dashboards dinâmicos
- **localStorage** — Persistência client-side (fora de artifacts)

### JavaScript / Node.js
- **docx (npm)** — Geração de Word programática
- **ExcelJS** — Alternativa a openpyxl para Node
- **Express** — APIs simples
- **fs / path** — Manipulação de arquivos

---

## Pipeline de Tratamento — 7 Fases

Executar SEMPRE em sequência. Fase pode ser pulada apenas se explicitamente desnecessária.

### Fase 1 — Inventário da Base

Ao receber qualquer arquivo financeiro:

```python
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# 1. Listar sheets
sheets = pd.read_excel(filepath, sheet_name=None, header=None, nrows=5)
print(f"Arquivo: {filepath}")
print(f"Sheets ({len(sheets)}): {list(sheets.keys())}")
for name, df in sheets.items():
    print(f"  [{name}] shape={df.shape}")
    print(df.head(3).to_string())
```

Registrar:
- Número de sheets e seus nomes
- Linhas de header (qual row tem os nomes de coluna)
- Formato de valores (positivo/negativo, R$, vírgula decimal)
- Colunas disponíveis e tipos
- Volume de dados (rows × cols)

### Fase 2 — Leitura com Quirks Conhecidos

**Consultar `references/fontes-oficiais.md`** para quirks de cada arquivo fonte do grupo.

Regras universais de leitura:
```python
# SEMPRE aplicar após leitura
df.columns = df.columns.str.strip()
# Normalizar colunas de mês
if 'Mês' in df.columns or 'Mês Comp' in df.columns:
    col = 'Mês' if 'Mês' in df.columns else 'Mês Comp'
    df[col] = df[col].astype(str).str.strip().str.lower()
# Converter valores numéricos
for col in ['Valor', 'VALOR', 'Valor Negativo', 'Valor pago', 'Valor previsto', 'Valor orçado']:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
```

### Fase 3 — Normalização

| Dimensão | Padrão Oficial | Exemplo |
|---|---|---|
| Meses | lowercase 3 chars | `jan`, `fev`, `mar`, ... `dez` |
| B.U. | UPPERCASE | `FARMA`, `DERMA`, `NUTRI`, `FOOD`, `CT` |
| Valores monetários | float, negativos = custos | `-5392.50` |
| Datas | `YYYY-MM-DD` | `2026-01-15` |
| Competência | `YYYY-MM` | `2026-01` |
| Centro de Custo | Hierárquico com ponto | `1.1.2.1` |
| Texto livre | `.str.strip().str.upper()` | `MATÉRIA PRIMA` |

```python
MONTH_MAP = {
    'janeiro':'jan','fevereiro':'fev','março':'mar','marco':'mar',
    'abril':'abr','maio':'mai','junho':'jun','julho':'jul',
    'agosto':'ago','setembro':'set','outubro':'out',
    'novembro':'nov','dezembro':'dez',
    'jan':'jan','fev':'fev','mar':'mar','abr':'abr','mai':'mai',
    'jun':'jun','jul':'jul','ago':'ago','set':'set','out':'out',
    'nov':'nov','dez':'dez',
}
MONTH_ORDER = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']

def normalize_month(val):
    if pd.isna(val): return None
    v = str(val).strip().lower()
    return MONTH_MAP.get(v, v)
```

### Fase 4 — Separação CAPEX vs OPEX

**Regra crítica para EBITDA correto.** CAPEX nunca entra no cálculo de EBITDA.

```python
CAPEX_KEYWORDS = [
    'INVESTIMENTO', 'CONSÓRCIO', 'CONSORCIO', 'LANCE',
    'MÁQUINA', 'MAQUINA', 'EQUIPAMENTO', 'ATIVO',
    'IMOBILIZADO', 'BENFEITORIAS', 'GALPÃO', 'GALPAO',
    'OBRA', 'CONSTRUÇÃO', 'AMPLIAÇÃO', 'VEÍCULO NOVO'
]

def flag_capex(cf_value):
    if pd.isna(cf_value): return False
    upper = str(cf_value).upper()
    return any(kw in upper for kw in CAPEX_KEYWORDS)

df['IS_CAPEX'] = df['CF'].apply(flag_capex)
df_opex = df[~df['IS_CAPEX']]
df_capex = df[df['IS_CAPEX']]
```

### Fase 5 — Validação e Alertas

Executar TODAS as validações. Registrar alertas com severidade.

```python
alerts = []

# 1. Meses com valor zero ou ausente
for m in MONTH_ORDER:
    total = df[df['mes_norm'] == m]['valor'].sum()
    if abs(total) < 100:
        alerts.append(('CRÍTICO', f'Mês {m}: valor total = R${total:.2f} — provável dado truncado'))

# 2. Duplicatas
dupes = df.duplicated(subset=['fornecedor','valor','data'], keep=False)
if dupes.sum() > 0:
    alerts.append(('ALERTA', f'{dupes.sum()} registros possivelmente duplicados'))

# 3. Outliers (>3 desvios padrão dentro de cada CC)
for cc, group in df.groupby('cc_sintetico'):
    if len(group) < 3: continue
    mean, std = group['valor'].mean(), group['valor'].std()
    if std == 0: continue
    outliers = group[abs(group['valor'] - mean) > 3 * std]
    if len(outliers) > 0:
        alerts.append(('ALERTA', f'CC {cc}: {len(outliers)} outliers detectados'))

# 4. BU inconsistente (mesmo CC com BUs diferentes)
bu_per_cc = df.groupby('cc_sintetico')['bu'].nunique()
inconsistent = bu_per_cc[bu_per_cc > 1]
if len(inconsistent) > 0:
    alerts.append(('CRÍTICO', f'{len(inconsistent)} CCs com BU inconsistente: {inconsistent.index.tolist()}'))

# 5. Lançamentos sem centro de custo
no_cc = df[df['cc_sintetico'].isna() | (df['cc_sintetico'] == '')]
if len(no_cc) > 0:
    alerts.append(('CRÍTICO', f'{len(no_cc)} lançamentos sem centro de custo'))

# 6. Março 2026 — regra específica do grupo
mar_data = df[df['mes_norm'] == 'mar']
if len(mar_data) > 0:
    fopag = mar_data[mar_data['cf'].str.contains('FOLHA|FOPAG', na=False, case=False)]
    if fopag['valor'].sum() == 0:
        alerts.append(('CRÍTICO', 'Março: FOPAG zerado — dado provavelmente truncado/incompleto'))
```

### Fase 6 — Enriquecimento

Adicionar colunas derivadas que aceleram análises downstream:

```python
# Classificação automática por grupo DRE
DRE_MAP = {
    'RECEITA BRUTA': 'RECEITA', 'DEDUÇÕES': 'RECEITA',
    'CMV': 'CUSTO', 'OPEX GERAL': 'DESPESA', 'OPEX PESSOAL': 'DESPESA',
    'CAPEX': 'INVESTIMENTO', 'JCP': 'FINANCEIRO', 'IMPOSTOS': 'IMPOSTO'
}
df['NATUREZA_DRE'] = df['GRUPO'].map(DRE_MAP)

# Período fiscal
df['TRIMESTRE'] = df['mes_norm'].map({
    'jan':'Q1','fev':'Q1','mar':'Q1','abr':'Q2','mai':'Q2','jun':'Q2',
    'jul':'Q3','ago':'Q3','set':'Q3','out':'Q4','nov':'Q4','dez':'Q4'
})
df['SEMESTRE'] = df['mes_norm'].map({
    'jan':'H1','fev':'H1','mar':'H1','abr':'H1','mai':'H1','jun':'H1',
    'jul':'H2','ago':'H2','set':'H2','out':'H2','nov':'H2','dez':'H2'
})

# Flag de mês fechado vs aberto
MESES_FECHADOS_2026 = ['jan', 'fev']  # ATUALIZAR conforme fechamento
df['STATUS_MES'] = df['mes_norm'].apply(
    lambda m: 'FECHADO' if m in MESES_FECHADOS_2026 else 'ABERTO'
)
```

### Fase 7 — Exportação

Gerar saída no formato solicitado:

| Destino | Formato | Função |
|---|---|---|
| Power BI | CSV 17 colunas (via especialista-padronizacao) | `df.to_csv('base_bi.csv', index=False)` |
| Excel análise | XLSX com formatação | openpyxl com styles |
| SQL / Supabase | INSERT statements ou API | Bulk insert com validação |
| HTML dashboard | Arquivo interativo | Chart.js + SheetJS |
| JSON API | REST endpoint | FastAPI / Express |
| Outro skill | DataFrame em memória | Passar `df` diretamente |

---

## Receitas Rápidas

### Python — Merge de bases Budget vs Realizado
```python
def merge_budget_real(df_budget, df_real, keys=['GRUPO','mes_norm','bu']):
    merged = df_budget.merge(df_real, on=keys, how='outer',
                             suffixes=('_BUD','_REAL'))
    merged['VARIACAO_RS'] = merged['valor_REAL'] - merged['valor_BUD']
    merged['VARIACAO_PCT'] = merged['VARIACAO_RS'] / merged['valor_BUD'].abs()
    merged['STATUS'] = merged['VARIACAO_PCT'].apply(
        lambda x: 'ESTOURO' if x > 0.05 else ('ECONOMIA' if x < -0.05 else 'OK')
    )
    return merged
```

### SQL — Criar tabela de custos
```sql
CREATE TABLE IF NOT EXISTS custos_mensais (
    id SERIAL PRIMARY KEY,
    ano INTEGER NOT NULL,
    mes VARCHAR(3) NOT NULL,
    cc_sintetico VARCHAR(50) NOT NULL,
    cc_reduzido VARCHAR(20),
    bu VARCHAR(20) NOT NULL,
    grupo VARCHAR(30) NOT NULL,
    cf VARCHAR(100),
    fornecedor VARCHAR(200),
    valor DECIMAL(15,2) NOT NULL,
    is_capex BOOLEAN DEFAULT FALSE,
    natureza_dre VARCHAR(20),
    trimestre VARCHAR(2),
    status_mes VARCHAR(10) DEFAULT 'ABERTO',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT chk_mes CHECK (mes IN ('jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez'))
);

CREATE INDEX idx_custos_ano_mes ON custos_mensais(ano, mes);
CREATE INDEX idx_custos_cc ON custos_mensais(cc_sintetico);
CREATE INDEX idx_custos_bu ON custos_mensais(bu);
```

### SQL — Query de variação orçado vs realizado
```sql
WITH budget AS (
    SELECT cc_sintetico, mes, SUM(valor) AS val_budget
    FROM custos_mensais WHERE ano = 2026 AND grupo = 'BUDGET'
    GROUP BY cc_sintetico, mes
),
realizado AS (
    SELECT cc_sintetico, mes, SUM(valor) AS val_real
    FROM custos_mensais WHERE ano = 2026 AND status_mes = 'FECHADO'
    GROUP BY cc_sintetico, mes
)
SELECT
    COALESCE(b.cc_sintetico, r.cc_sintetico) AS cc,
    COALESCE(b.mes, r.mes) AS mes,
    b.val_budget,
    r.val_real,
    r.val_real - b.val_budget AS variacao_rs,
    ROUND((r.val_real - b.val_budget) / NULLIF(ABS(b.val_budget), 0) * 100, 1) AS variacao_pct,
    CASE
        WHEN (r.val_real - b.val_budget) / NULLIF(ABS(b.val_budget), 0) > 0.05 THEN 'ESTOURO'
        WHEN (r.val_real - b.val_budget) / NULLIF(ABS(b.val_budget), 0) < -0.05 THEN 'ECONOMIA'
        ELSE 'OK'
    END AS status
FROM budget b
FULL OUTER JOIN realizado r ON b.cc_sintetico = r.cc_sintetico AND b.mes = r.mes
ORDER BY cc, mes;
```

### SQL — Window Functions para tendência
```sql
SELECT
    cc_sintetico,
    mes,
    valor,
    AVG(valor) OVER (PARTITION BY cc_sintetico ORDER BY mes ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS media_movel_3m,
    valor - LAG(valor) OVER (PARTITION BY cc_sintetico ORDER BY mes) AS variacao_mom,
    RANK() OVER (PARTITION BY mes ORDER BY valor DESC) AS rank_custo
FROM custos_mensais
WHERE ano = 2026 AND status_mes = 'FECHADO';
```

### HTML — Template de dashboard de dados
```html
<!-- Estrutura base para dashboard financeiro interativo -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.3.0/papaparse.min.js"></script>
<style>
  :root {
    --red: #C41E2A; --red-dark: #8B0000; --white: #FFFFFF;
    --gray-800: #1F2937; --gray-100: #F3F4F6;
  }
</style>
```

### JavaScript — Leitura de Excel no browser
```javascript
// SheetJS para carregar Excel client-side
async function loadExcel(file) {
    const data = await file.arrayBuffer();
    const workbook = XLSX.read(data, { type: 'array' });
    const sheet = workbook.Sheets[workbook.SheetNames[0]];
    return XLSX.utils.sheet_to_json(sheet, { header: 1 });
}
```

### Python — API FastAPI para dados financeiros
```python
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI(title="API Financeira - Grupo Oficial")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"])

@app.get("/custos")
async def get_custos(
    ano: int = 2026,
    mes: str = None,
    cc: str = None,
    bu: str = None
):
    df = pd.read_csv("base_custos.csv")
    if mes: df = df[df['mes'] == mes]
    if cc: df = df[df['cc_sintetico'] == cc]
    if bu: df = df[df['bu'] == bu]
    return {
        "total": len(df),
        "soma": float(df['valor'].sum()),
        "dados": df.to_dict(orient='records')
    }
```

---

## Regras de Ouro

1. **NUNCA analisar dado sujo** — sempre limpar ANTES
2. **NUNCA assumir header** — sempre verificar qual row tem os nomes de coluna
3. **NUNCA confiar em tipos** — sempre converter explicitamente com `pd.to_numeric(errors='coerce')`
4. **NUNCA misturar caixa e competência** — manter separados e sinalizar qual regime está sendo usado
5. **SEMPRE aplicar `.str.strip()`** em colunas de texto após leitura
6. **SEMPRE validar antes de exportar** — rodar Fase 5 antes de qualquer saída
7. **SEMPRE registrar alertas** — nunca silenciar inconsistências
8. **SEMPRE manter CAPEX separado de OPEX** — contaminação distorce EBITDA
9. **SEMPRE usar MONTH_ORDER** para ordenar meses — nunca confiar em sort alfabético
10. **SEMPRE verificar se Março está completo** — dado historicamente truncado no grupo

---

## Integração com Claude Code

Quando usado no Claude Code, este skill serve como **referência de padrões**:

### Padrões de código a seguir
- Usar `warnings.filterwarnings('ignore')` no topo
- Usar `<< 'EOF'` para scripts multiline em bash
- Testar leitura com `nrows=5` antes de carregar base inteira
- Preferir `pivot_table` sobre `groupby().unstack()` para tabelas cruzadas
- Usar `f-strings` com formatação `.2f` para valores monetários
- Comentários mínimos — código autoexplicativo

### Estrutura de projeto recomendada
```
projeto/
├── data/
│   ├── raw/          ← Dados brutos (nunca alterar)
│   ├── processed/    ← Dados tratados
│   └── output/       ← Relatórios e exportações
├── src/
│   ├── etl.py        ← Pipeline de tratamento
│   ├── validate.py   ← Validações
│   ├── api.py        ← FastAPI (se aplicável)
│   └── dashboard.py  ← Geração de HTML
├── sql/
│   ├── schema.sql    ← DDL
│   └── queries.sql   ← Queries de análise
└── requirements.txt
```

---

## Referências

Consultar **`references/apis-publicas.md`** quando o projeto precisar de dado externo (câmbio, indicadores do Banco Central, CEP, CNPJ, IBGE e outros): critérios para escolher a API, fontes brasileiras, formato de integração (Python, Power Query, Power Automate, Apps Script) e limitações.

Consultar **`references/fontes-oficiais.md`** para:
- Quirks específicos de cada arquivo-fonte do Grupo Oficial Farma
- Mapeamento de colunas por arquivo
- Regras de header_row por sheet
- Campos de valor por tipo de base
- Regras de normalização de B.U. e Centro de Custo
