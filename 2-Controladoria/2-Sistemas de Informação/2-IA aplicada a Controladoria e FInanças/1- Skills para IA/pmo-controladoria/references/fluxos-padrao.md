# Fluxos Padrão — Controladoria e FP&A

## 1. CICLO DE FP&A (Anual)

```
[INÍCIO DO EXERCÍCIO]
      ↓
(Definição de Premissas Macroeconômicas)
  IPCA, CDI, câmbio, crescimento de setor
      ↓
(Workshop de Budget com Gestores de BU)
  ⚠️ Risco: gestores inflam receita e deflam custo
      ↓
{Aprovação do Budget pela Diretoria?}
  → NÃO → Revisão com ajustes → loop
  → SIM ↓
(Distribuição do Budget por Centro de Custo)
  [DOC: Forecast_Orçamento_Aprovado.xlsx]
      ↓
=== CICLO MENSAL ===
(Coleta do Realizado — D+1 a D+3)
  Fontes: SAP, OMIE, Master, Medicator
      ↓
(Conciliação e Tratamento de Dados)
  ⚠️ Ponto crítico: qualidade dos dados na fonte
  [DOC: Base_Realizado_MES_AAAA.xlsx]
      ↓
(Análise de Variação Orçado vs Realizado)
  Por BU, por centro de custo, por gestor
      ↓
(Elaboração do Relatório Gerencial)
  [DOC: DRE_Gerencial + Dashboard Power BI]
      ↓
{Variações > 10%?}
  → SIM → Nota explicativa obrigatória
  → NÃO ↓
(Revisão do Forecast — Mês Atual)
  Realizado YTD + Budget restante + ajustes
      ↓
(Apresentação ao CFO / Controller) — D+5
      ↓
{Aprovação CFO?}
  → NÃO → Ajustes e reapresentação
  → SIM ↓
(Distribuição do Relatório Final) — D+7
  [Stakeholders: CFO, Diretoria, Gestores]
      ↓
[FIM DO CICLO MENSAL — aguardar próximo mês]
```

---

## 2. FECHAMENTO CONTÁBIL (D+1 a D+5)

| Dia | Atividade | Responsável | Sistema | Entregável |
|---|---|---|---|---|
| D+1 | Exportação de lançamentos | Controller | SAP / OMIE | Base bruta de lançamentos |
| D+1 | Conciliação bancária | Financeiro | OMIE + Bancos | Extrato reconciliado |
| D+2 | Tratamento e normalização dos dados | FP&A | Excel / Python | Base tratada por CC |
| D+2 | Alocação por centro de custo | Controller | SAP / Notion | Planilha de rateio |
| D+3 | Fechamento de OPEX por BU | FP&A | Excel | DRE preliminar |
| D+3 | Validação de CMV e estoques | Controller + Produção | SAP / Master | CMV validado |
| D+4 | Consolidação da DRE por BU | FP&A | Forecast_2026.xlsx | DRE Consolidada |
| D+4 | Análise de variação vs Budget | FP&A | Excel + Power BI | Relatório de variação |
| D+5 | Revisão CFO + ajustes finais | CFO + Controller | — | Relatório aprovado |
| D+5 | Distribuição para gestores | Controller | E-mail + Teams | Relatório final |

**⚠️ Alertas críticos no fechamento:**
- Lançamentos sem centro de custo = erro de rateio
- CAPEX lançado como OPEX = distorção de margem
- Competência ≠ caixa = distorção de fluxo
- Lançamentos duplicados ou estornos não conciliados

---

## 3. APROVAÇÃO DE CAPEX

```
[SOLICITAÇÃO DE CAPEX]
  Quem: Gestor da área
  Como: Formulário em Notion/Forms com: descrição, valor, BU, CC, justificativa, prazo
      ↓
(Análise Técnica — Controller)
  Verificar: orçamento disponível, código de CC correto, classificação ativo/gasto
      ↓
{Valor > R$ 50k?}
  → SIM → Requer aprovação da Diretoria
  → NÃO ↓
{Valor > R$ 10k?}
  → SIM → Requer aprovação do CFO
  → NÃO → Aprovação do Controller é suficiente
      ↓
(Aprovação registrada no sistema)
  [DOC: Formulário de CAPEX aprovado com assinatura]
      ↓
(Lançamento no SAP com código de projeto CAPEX)
      ↓
(Acompanhamento mensal no relatório de CAPEX)
  Comparativo: orçado x realizado x forecast
      ↓
[ATIVO ATIVADO E DEPRECIAÇÃO INICIADA]
```

---

## 4. GESTÃO DE CENTROS DE CUSTO

### Ciclo de Controle Mensal
```
[ABERTURA DO MÊS]
      ↓
(Comunicação dos limites orçamentários por CC)
  Enviado pelo Controller para cada gestor
      ↓
=== DURANTE O MÊS ===
(Gestor solicita via Notion/Forms toda despesa relevante)
  Com: valor, fornecedor, CC, competência, aprovador
      ↓
{Despesa dentro do orçamento?}
  → SIM → Aprovação automática pelo Controller
  → NÃO → Aprovação escalonada (CFO ou Diretoria)
      ↓
(Lançamento no sistema)
      ↓
=== FECHAMENTO ===
(Extração dos lançamentos do mês por CC)
      ↓
(Análise de desvios por centro e por gestor)
      ↓
(Relatório de Centros de Custo — D+5)
  ⚠️ Alertas automáticos para desvios > 15%
      ↓
[PRÓXIMO MÊS]
```

---

## 5. PIPELINE DE DADOS PARA BI (Power BI)

```
[FONTES DE DADOS]
  SAP (OPEX, CAPEX, contabilidade)
  OMIE (contas a pagar/receber, caixa)
  Master (produção, CMV farmácia)
  Medicator (manipulação, estoque)
  Notion/Forms (centros de custo, aprovações)
      ↓
(Extração — D+1)
  Formato: Excel / CSV por sistema
  ⚠️ Padronizar: header, encoding, datas, valores negativos
      ↓
(Tratamento — FPA Estruturador)
  Normalizar BU, CC, mês competência, grupo de contas
  Modelo 17 colunas padrão
      ↓
(Carga no Power BI)
  Dataset principal: BD-Controladoria
  Atualização: automática D+2 (via gateway) ou manual
      ↓
(Dashboards disponíveis)
  - PAINEL GERAL (receita, margem, EBITDA por mês)
  - PAINEL OPERACIONAL (por BU, por canal)
  - NÃO OPERACIONAL (ativos patrimoniais)
  - ANÁLISE DE VARIAÇÃO (orçado x realizado)
      ↓
[DISTRIBUIÇÃO — D+5]
  Acesso: CFO, Controller, Gestores de BU
```
