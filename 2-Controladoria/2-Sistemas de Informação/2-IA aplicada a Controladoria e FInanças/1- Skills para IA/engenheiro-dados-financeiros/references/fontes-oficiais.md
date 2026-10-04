# Fontes Oficiais — Guia de Leitura de Arquivos do Grupo Oficial Farma

Este documento contém todas as especificidades de leitura dos arquivos financeiros
utilizados pelo grupo. Consultar ANTES de ler qualquer arquivo.

---

## Índice
1. [Forecast_2026_V1.xlsx](#1-forecast_2026_v1xlsx)
2. [BICustos_por_centro__V3__DRE_Caixa.xlsx](#2-bicustos_por_centro__v3__dre_caixaxlsx)
3. [C_Custos_V8_Atualizado.xlsx](#3-c_custos_v8_atualizadoxlsx)
4. [Regras Transversais](#4-regras-transversais)
5. [Mapeamento de Colunas de Valor](#5-mapeamento-de-colunas-de-valor)
6. [Matriz Gestor → Grupo de CCs](#6-matriz-gestor--grupo-de-ccs)

---

## 1. Forecast_2026_V1.xlsx

### Sheet: BUDGET
- **header_row:** `header=2` (linha 3 do Excel, index 2 no pandas)
- **Coluna de valor:** `VALOR`
- **Coluna de mês:** `MÊS DE PAGAMENTO`
- **Formato de mês:** UPPERCASE (`JAN`, `FEV`, `MAR`...) — normalizar para lowercase
- **Colunas-chave:**
  - `B.U.` — Business Unit
  - `GRUPO` — Linha do P&L (RECEITA BRUTA, CMV, OPEX GERAL, OPEX PESSOAL, CAPEX, etc.)
  - `P.C. SINTÉTICO` — Plano de Contas sintético
  - `CC REDUZIDO` — Grupo de centro de custo
  - `CC - SINTÉTICO` — Centro de custo sintético
  - `CENTRO DE CUSTOS` — Centro de custo analítico (mais detalhado)
- **Quirks:**
  - Valores de budget são negativos para custos
  - Existe linha com CC REDUZIDO = `0` que são lançamentos sem classificação
  - `MÊS DE PAGAMENTO` pode conter espaços extras

```python
df_budget = pd.read_excel('Forecast_2026_V1.xlsx', sheet_name='BUDGET', header=2)
df_budget.columns = df_budget.columns.str.strip()
df_budget['VALOR'] = pd.to_numeric(df_budget['VALOR'], errors='coerce')
df_budget['MES_NORM'] = df_budget['MÊS DE PAGAMENTO'].str.upper().str.strip().map(MONTH_MAP_UPPER)
```

### Sheet: REALIZADO
- **header_row:** `header=0` (primeira linha)
- **Coluna de valor:** `Valor Negativo` (custos como valores negativos)
- **Coluna de mês:** `Mês`
- **Formato de mês:** Mixed case, inconsistente (`jan`, `JAN`, `Jan`, `fev`) — SEMPRE normalizar
- **Colunas-chave:**
  - `B.U.` — pode ter variações de case (`Farma`, `FARMA`, `farma`)
  - `GRUPO` — Linha do P&L
  - `CF` — Conta financeira / Plano de contas
  - `CCA` — Centro de custo analítico (formato `1.1.2.1 Estoque - Advanced`)
  - `CCS` — Centro de custo sintético (formato `1.1 Advanced`)
  - `Fornecedor` — Nome do fornecedor
- **Quirks:**
  - `B.U.` tem duplicação de case: `Farma` e `FARMA` são o mesmo
  - `Mês` tem inconsistências: `jan`, `JAN`, `Jan` — SEMPRE `.str.lower().str.strip()`
  - Março 2026 historicamente truncado (FOPAG zerado, SG&A incompleto)
  - Coluna `Valor Negativo` é a que contém os valores — NÃO usar `Valor`

```python
df_real = pd.read_excel('Forecast_2026_V1.xlsx', sheet_name='REALIZADO', header=0)
df_real.columns = df_real.columns.str.strip()
df_real['Valor Negativo'] = pd.to_numeric(df_real['Valor Negativo'], errors='coerce')
df_real['MES_NORM'] = df_real['Mês'].str.lower().str.strip()
df_real['BU_NORM'] = df_real['B.U.'].str.upper().str.strip()
```

### Sheet: Base_Receber27
- **header_row:** `header=0`
- **Coluna de valor pago:** `Valor pago`
- **Coluna de valor previsto:** `Valor previsto`
- **Coluna de mês:** `Caixa`
- **Formato de mês:** lowercase (`jan`, `fev`)
- **Colunas-chave:**
  - `BU` — Business Unit (sem ponto: `BU`, não `B.U.`)
  - `Canais de Venda.Canal de venda` — Canal comercial
- **Quirks:**
  - Campo de canal tem nome composto com ponto: `Canais de Venda.Canal de venda`
  - Esta sheet contém RECEITAS (regime caixa), não custos
  - Usar `Valor pago` para receita efetiva e `Valor previsto` para forecast de receita

```python
df_rec = pd.read_excel('Forecast_2026_V1.xlsx', sheet_name='Base_Receber27', header=0)
df_rec['Valor pago'] = pd.to_numeric(df_rec['Valor pago'], errors='coerce')
df_rec['Valor previsto'] = pd.to_numeric(df_rec['Valor previsto'], errors='coerce')
```

---

## 2. BICustos_por_centro__V3__DRE_Caixa.xlsx

### Sheet: BD-Controladoria
- **header_row:** `header=1` ⚠️ (NÃO é 0 — linha 2 do Excel)
- **Coluna de valor:** `Valor`
- **Coluna de mês:** `Mês Comp` (competência)
- **Formato de mês:** lowercase 3 chars (`jan`, `fev`...) — normalmente já ok
- **Colunas-chave:**
  - `Subgrupo` — Código do centro sintético (ex: `1.1 Advanced`)
  - `Centro de Custos` — CC analítico completo
  - `Unidade de negócios` — BU
  - `CF` — Conta financeira (Plano de Contas)
  - `Fornecedor` — Nome do fornecedor
- **Quirks:**
  - **header=1 é OBRIGATÓRIO** — sem isso, colunas ficam deslocadas
  - Contém dados de 2025 inteiro (12 meses fechados)
  - `Subgrupo` usa o prefixo numérico: `1.1`, `3.2`, `4.3.3` etc.
  - Alguns meses podem aparecer como `nan` para lançamentos de ajuste

```python
df_bd = pd.read_excel('BICustos_por_centro__V3__DRE_Caixa.xlsx',
                       sheet_name='BD-Controladoria', header=1)
df_bd.columns = df_bd.columns.str.strip()
df_bd['Valor'] = pd.to_numeric(df_bd['Valor'], errors='coerce')
```

### Sheet: BD-DRE_CONTROLADORIA
- **header_row:** `header=0`
- **Coluna de valor:** `Valor pago`
- **Contém:** Visão DRE com plano de contas
- **Colunas-chave:** `Plano de contas`, `CF`, `Mês Comp`

### Sheet: Budget 2025
- **header_row:** `header=0`
- **Coluna de valor:** `Valor orçado`
- **Colunas-chave:** `Unidade de negócios`, `Conta Contabil`, `Competencia`

### Sheet: Projeção
- **header_row:** `header=2` ⚠️
- **Estrutura:** Wide format — colunas = meses (`Jan`, `Fev`,..., `Dez`, `2025`, `2026`)
- **Linha index:** `Centros de Custos` (ex: `1.1 Advanced`, `Total`, `Faturamento realizado`)
- **Quirks:**
  - Não é tabela tabular normal — é uma matriz de projeção
  - Linha `Faturamento realizado` contém receita 2025 por mês
  - Linha `Total` contém custo total projetado por mês
  - Colunas `2025` e `2026` são totais anuais

```python
df_proj = pd.read_excel('BICustos_por_centro__V3__DRE_Caixa.xlsx',
                         sheet_name='Projeção', header=2)
```

### Sheet: Competencia
- Sheet auxiliar com dados de referência de competência
- Consultar se necessário para validação de períodos

---

## 3. C_Custos_V8_Atualizado.xlsx

- **Conteúdo:** Matriz completa de centros de custo do grupo
- **Estrutura:** Cada CC com colunas de atributos (Grupo, Sintético, Reduzido, BU, Gestor, Status)
- **Uso:** Referência para validação de CCs em outras bases
- **Quirks:**
  - Alguns CCs estão marcados como `INATIVAR` — não devem receber lançamentos
  - CCs agrupadores `Não aceita lançamentos` — usar filho mais específico
  - A V8 é a versão mais atual — versões anteriores podem ter CCs desatualizados

---

## 4. Regras Transversais

### SharePoint
- Arquivos em `oficialfarmacombr.sharepoint.com` **NÃO podem ser acessados diretamente**
- Devem ser baixados manualmente e re-uploadados ou exportados como CSV

### Meses Fechados 2026 (atualizar conforme progresso)
```python
MESES_FECHADOS_2026 = ['jan', 'fev']  # Atualizar mensalmente
# Março 2026: PARCIAL — dados truncados, FOPAG zerado
```

### EBITDA — Regra de Segmentação
```
EBITDA deve ser calculado EXCLUSIVAMENTE de BUs operacionais:
  ✅ FARMA, DERMA, NUTRI
  ❌ Haras, Ship, Patrimonial, Incorporadora (Não Operacionais)
  ❌ FOOD, CT (Novos Negócios em fase pre-revenue)

Não Operacionais e Novos Negócios devem estar em CCs do Grupo 5.
Se aparecerem misturados em G1-G4, alertar como ERRO DE CLASSIFICAÇÃO.
```

### Valores: Convenção de Sinal
```
Receitas  → POSITIVO (+16.355.920)
Custos    → NEGATIVO (-5.391.765)
Despesas  → NEGATIVO (-4.191.581)
CAPEX     → NEGATIVO (-6.223.013)
Deduções  → NEGATIVO (-567.204)
Impostos  → NEGATIVO (-453.071)
```

---

## 5. Mapeamento de Colunas de Valor

| Arquivo | Sheet | Coluna de Valor | Sinal |
|---|---|---|---|
| Forecast_2026_V1 | BUDGET | `VALOR` | Negativo = custo |
| Forecast_2026_V1 | REALIZADO | `Valor Negativo` | Negativo = custo |
| Forecast_2026_V1 | Base_Receber27 | `Valor pago` | Positivo = receita |
| BICustos_V3 | BD-Controladoria | `Valor` | Positivo = custo* |
| BICustos_V3 | BD-DRE | `Valor pago` | Misto |
| BICustos_V3 | Budget 2025 | `Valor orçado` | Positivo = custo |

*Nota: BD-Controladoria pode ter valores positivos para custos (depende do lançamento).
Verificar a convenção a cada leitura.

---

## 6. Matriz Gestor → Grupo de CCs

| Gestor | Grupos de CC | Áreas |
|---|---|---|
| **Lucas Caetano** | G1 Fábricas + G3 Facilities/Logística | 1.1, 1.2, 1.4, 3.1, 3.2, 3.3 |
| **Ana Lucia** | G2 Lojas (exceto Derma) | 2.x (exceto 2.1.2.1, 2.2.2.1, etc. que são Elaine) |
| **Elaine** | 1.3 Derma + Recepções Derma em Lojas + 4.9.3 | 1.3, 2.x.2.1 (Derma), 4.9.3 |
| **Ingrid Silveira** | G4 Adm/Financeiro/RH | 4.2.3.x |
| **Welby** | E-commerce + Comercial + Marketing | 4.3.3, 4.4.3, 4.5.3 |
| **Leandro** | TI | 4.8.3 |
| **Stefany** | Presidência | 4.1.3 |
| **Alessandro** | Projetos & Novos Negócios | 6.x |
| **Marcus** | Patrimonial / Não Operacional | 5.x |
| **Pamela** | Ginger (BU separada) | CCs específicos Ginger |

### Filtro rápido por gestor (Python)
```python
GESTOR_CC_MAP = {
    'Lucas Caetano':   lambda cc: cc.startswith(('1.1','1.2','1.4','3.')),
    'Ana Lucia':       lambda cc: cc.startswith('2.') and not cc.startswith(('2.1.2.1','2.2.2.1','2.3.2.1','2.4.2.1','2.5.2.1','2.6')),
    'Elaine':          lambda cc: cc.startswith(('1.3','2.6','4.9.3')) or cc in ['2.1.2.1','2.2.2.1','2.3.2.1','2.4.2.1','2.5.2.1'],
    'Ingrid Silveira': lambda cc: cc.startswith('4.2.3'),
    'Welby':           lambda cc: cc.startswith(('4.3.3','4.4.3','4.5.3')),
    'Leandro':         lambda cc: cc.startswith('4.8.3'),
    'Stefany':         lambda cc: cc.startswith('4.1.3'),
    'Alessandro':      lambda cc: cc.startswith('6.'),
    'Marcus':          lambda cc: cc.startswith('5.'),
}

def filter_by_gestor(df, gestor, cc_col='cc_sintetico'):
    func = GESTOR_CC_MAP.get(gestor)
    if func is None:
        raise ValueError(f"Gestor '{gestor}' não encontrado na matriz")
    return df[df[cc_col].apply(func)]
```

---

## Checklist de Leitura — Usar antes de cada arquivo

- [ ] Verificar `header_row` correto para a sheet
- [ ] Aplicar `.str.strip()` em TODAS as colunas de texto
- [ ] Converter colunas de valor para numérico com `errors='coerce'`
- [ ] Normalizar meses para lowercase 3 chars
- [ ] Normalizar B.U. para UPPERCASE
- [ ] Verificar convenção de sinal (positivo vs negativo)
- [ ] Checar se Março está completo (FOPAG, SG&A)
- [ ] Separar CAPEX de OPEX se necessário para EBITDA
- [ ] Rodar validação de duplicatas e outliers
- [ ] Confirmar meses fechados vs abertos
