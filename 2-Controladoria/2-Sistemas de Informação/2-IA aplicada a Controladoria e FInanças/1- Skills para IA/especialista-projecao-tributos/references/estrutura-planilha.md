# Referência: Estrutura Padrão da Planilha de Projeção

## Organização das Abas (ordem obrigatória)

| Nº | Nome da Aba | Cor da Guia | Protegida? |
|---|---|---|---|
| 1 | `Premissas` | Azul escuro | Não (editável) |
| 2 | `Histórico` | Cinza | Sim (read-only) |
| 3 | `Projeção_Base` | Amarelo | Não |
| 4 | `Projeção_Otimista` | Verde | Não |
| 5 | `Projeção_Pessimista` | Vermelho | Não |
| 6 | `Consolidado` | Azul claro | Não |
| 7 | `Budget_vs_Real` | Laranja | Não (se aplicável) |
| 8 | `Alertas` | Vermelho escuro | Não |
| 9 | `Backtest` | Cinza escuro | Não |
| 10 | `Checks` | Verde escuro | Não |

(`Premissas_Fiscais` e `Impostos_Projetados` ficam depois de `Premissas` e de `Projeção_Pessimista`, respectivamente, quando houver projeção de tributos.)

---

## Aba: Premissas

Estrutura mínima. **Os valores abaixo são EXEMPLOS de formato, não premissas reais:** cada linha deve receber o valor e a fonte definidos pelo usuário.

| Linha | Coluna A (descrição) | Coluna B (valor) | Coluna C (fonte/nota) |
|---|---|---|---|
| 3 | Taxa de Crescimento Receita (a.m.) | [exemplo: 2,5%] | Premissa do gestor (informe a justificativa) |
| 4 | Inflação anual de referência | [exemplo: informe] | Índice e fonte escolhidos pelo usuário, com data |
| 5 | Inflação mensal | =((1+B4)^(1/12))-1 | Calculado |
| 6 | Cenário otimista: variação de volume | [premissa] | Justificativa |
| 7 | Cenário otimista: variação de preço | [premissa] | Justificativa |
| 8 | Cenário pessimista: variação de volume | [premissa] | Justificativa |
| 9 | Cenário pessimista: variação de preço | [premissa] | Justificativa |
| 10 | Horizonte de Projeção (meses) | 12 | Definido pelo usuário |
| 11 | Peso da média móvel: mês mais recente | [exemplo: 50%] | Ponto de partida; teste no backtest |
| 12 | Peso da média móvel: penúltimo mês | [exemplo: 30%] | Ponto de partida; teste no backtest |
| 13 | Peso da média móvel: antepenúltimo | [exemplo: 20%] | Ponto de partida; teste no backtest |
| 14 | % CMV / Receita | [calculado do histórico] | Critério declarado (ponderado ou simples) |
| 15 | % Comissões / Receita | [calculado do histórico] | Critério declarado |
| 20 | Gatilho de crescimento anômalo | [exemplo: 30%] | Heurística ajustável |
| 21 | Gatilho de desvio vs budget | [exemplo: 15%] | Heurística ajustável |

Os cenários variam **drivers** (volume, preço, custo), não um fator único sobre o resultado.

---

## Aba: Histórico

**Regras absolutas:**
- Nenhuma fórmula que dependa de premissas
- Apenas dados reais, importados ou colados
- Colunas de período no formato `MMM/AA` (Jan/24, Fev/24, ...)
- Linha 1: cabeçalho de período
- Linha 2: código da linha financeira (ex: REC_BRUTA, CMV, EBITDA)
- Linha 3 em diante: valores

**Formatação:**
- Fundo branco para dados históricos
- Fonte: Calibri 11
- Números: formato moeda sem símbolo `#.##0` ou `#.##0,0`

---

## Abas: Projeção_Base / Otimista / Pessimista

**Formatação das células:**
- Fundo cinza claro (#F2F2F2) para todas as células de projeção (diferencia do histórico)
- Primeira coluna de projeção com borda esquerda dupla (separador visual do histórico)
- Linha de EBITDA e Margem EBITDA em negrito

**Comentário de célula obrigatório (primeira célula de cada linha projetada):**
```
Método: [nome do método]
Período base: [meses usados]
Referência: Premissas!$B$3
```

**Estrutura de colunas:**

| Col | Conteúdo |
|---|---|
| A | Código da linha |
| B | Descrição da linha |
| C | Tipo (Receita / CMV / Fixo / Variável / EBITDA) |
| D em diante | Períodos projetados (Jan/26, Fev/26...) |

---

## Aba: Consolidado

Visão lado a lado dos 3 cenários para cada período:

| Linha | Base | Otimista | Pessimista | Δ Otim/Base | Δ Pess/Base |
|---|---|---|---|---|---|
| Receita Bruta | R$ | R$ | R$ | % | % |
| Receita Líquida | R$ | R$ | R$ | % | % |
| CMV | R$ | R$ | R$ | % | % |
| Margem Bruta | R$ | R$ | R$ | % | % |
| Despesas Fixas | R$ | R$ | R$ | % | % |
| EBITDA | R$ | R$ | R$ | % | % |
| Margem EBITDA | % | % | % | pp | pp |

---

## Aba: Budget_vs_Real (quando aplicável)

| Coluna | Conteúdo |
|---|---|
| A | Código da linha |
| B | Descrição |
| C | Realizado acumulado |
| D | Budget acumulado |
| E | Desvio R$ (C−D) |
| F | Desvio % ((C/D)−1) |
| G | Status (ícone: ✅ ≤5% / ⚠️ 5–15% / 🔴 >15%) |

---

## Aba: Alertas

Gerada automaticamente com fórmulas. Colunas:

| A: Linha | B: Período | C: Tipo de Alerta | D: Valor Atual | E: Valor de Referência | F: Desvio |
|---|---|---|---|---|---|
| Receita Bruta | Mar/26 | Crescimento anômalo | R$ 1.350.000 | R$ 950.000 | +42% |

---

## Convenções de Formatação Geral

### Números financeiros (R$):
```
Formato: #.##0  (sem casas decimais)
Negativo: (vermelho) -#.##0
```

### Percentuais:
```
Formato: 0,0%  (uma casa decimal)
```

### Períodos:
```
Formato de célula: MMM/AA
Exemplo: Jan/26, Fev/26
```

### Código de cores:
| Elemento | Cor |
|---|---|
| Histórico — fundo | Branco |
| Projeção — fundo | Cinza claro #F2F2F2 |
| Cabeçalho | Azul escuro #1F3864, texto branco |
| EBITDA / Totais | Azul médio #2E75B6, texto branco |
| Alertas críticos | Vermelho #FF0000 |
| Alertas atenção | Laranja #FF9900 |
| OK | Verde #00B050 |
