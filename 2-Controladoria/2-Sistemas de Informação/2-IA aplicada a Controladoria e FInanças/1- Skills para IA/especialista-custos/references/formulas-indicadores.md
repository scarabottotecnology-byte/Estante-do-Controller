# Fórmulas e Indicadores — Biblioteca Completa

## CUSTOS UNITÁRIOS

```
Custo Primário = Matéria-Prima + Mão de Obra Direta
Custo de Transformação = Mão de Obra Direta + CIF
Custo de Produção = MP + MOD + CIF
Custo do Produto Acabado = Custo de Produção / Quantidade Produzida
CPV (Custo dos Produtos Vendidos) = Estoque Inicial + Custo de Produção do período - Estoque Final
  (equivale a Custo Unitário × Quantidade Vendida quando o critério de estoque é aplicado de forma consistente)
Custo Total do Período = CPV + Despesas Operacionais
CIF fixo absorvido = CIF fixo / Capacidade Normal × Produção Real   (CPC 16, item 13)
Custo da ociosidade (resultado do período) = CIF fixo - CIF fixo absorvido
```

## MARGEM DE CONTRIBUIÇÃO

```
MC Unitária = Preço de Venda - Custos Variáveis Unitários - Despesas Variáveis Unitárias
MC Total = MC Unitária × Quantidade Vendida
MC% = MC Unitária / Preço de Venda × 100

MC por Canal = Receita Canal - (Custos Variáveis + Despesas Variáveis alocadas ao canal)
MC por Cliente = Receita Cliente - Custos diretos do cliente
```

## MARGENS

```
Margem Bruta = Receita Líquida - CPV
Margem Bruta% = Margem Bruta / Receita Líquida × 100

Margem Operacional = EBIT / Receita Líquida × 100
EBITDA = EBIT + Depreciação + Amortização
Margem EBITDA% = EBITDA / Receita Líquida × 100

Lucro Líquido = EBIT - Resultado Financeiro - IR/CSLL
Margem Líquida% = Lucro Líquido / Receita Líquida × 100
```

## PONTO DE EQUILÍBRIO

```
PE Contábil (unidades) = Custos Fixos Totais / MC Unitária
PE Contábil (R$) = Custos Fixos Totais / MC%

PE Financeiro = (Custos Fixos Totais - Depreciação) / MC%
PE Econômico = (Custos Fixos Totais + Custo de Oportunidade) / MC%

PE com produto misto = Custos Fixos / MC% ponderada
  MC% ponderada = Σ(MC%_produto × participação_produto_no_mix)
```

## MARK-UP E PRECIFICAÇÃO

```
Mark-up Multiplicador = 1 / Mark-up Divisor
Mark-up Divisor = 1 - (% Impostos sobre venda + % Despesas variáveis + % Margem desejada)

Preço de Venda Mínimo = Custo Variável / Mark-up Divisor
Preço de Venda Ideal = Custo Pleno / Mark-up Divisor

Preço Mínimo de Negociação = Custo Variável (contribuição marginal = zero)
Preço de Contribuição = Qualquer valor > Custo Variável (contribui para fixos)
```

## ALAVANCAGEM OPERACIONAL

```
Grau de Alavancagem Operacional (GAO) = MC Total / EBIT
  → Indica: para cada 1% de aumento na receita, o EBIT cresce X%

Alavancagem Financeira = EBIT / Lucro Antes do IR
Alavancagem Combinada = GAO × Alavancagem Financeira
```

## ABSORÇÃO DE FIXOS

```
Taxa de Absorção por Hora-MOD = CIF Total / Total de Horas-MOD
Taxa de Absorção por Hora-Máquina = CIF Total / Total de Horas-Máquina
Taxa de Absorção por Custo-MOD = CIF Total / Custo Total de MOD

CIF Absorvido = Taxa × Base de Rateio consumida pelo produto
CIF Sub/Sobreabsorvido = CIF Real - CIF Absorvido
```

## CUSTEIO PADRÃO — VARIÂNCIAS

```
Variância de Preço de MP = (Preço Real - Preço Padrão) × Quantidade Real
Variância de Quantidade de MP = (Qtd Real - Qtd Padrão) × Preço Padrão
Variância Total de MP = Variância de Preço + Variância de Quantidade

Variância de Taxa de MOD = (Taxa Real - Taxa Padrão) × Horas Reais
Variância de Eficiência de MOD = (Horas Reais - Horas Padrão) × Taxa Padrão

Variância de Volume de CIF = (Cap. Normal - Cap. Real) × Taxa Padrão de CIF Fixo
  (positiva = subabsorção, desfavorável)

Conferência: Variância de Preço + Variância de Quantidade = Custo Real - Custo Padrão para a produção real
```

## RENTABILIDADE

```
ROI = Lucro Líquido / Investimento Total × 100
ROIC = NOPAT / Capital Investido × 100
  NOPAT = EBIT × (1 - Alíquota IR)

Payback Simples = Investimento / Fluxo de Caixa Anual
Payback Descontado = calcula o período em que o VPL acumulado = 0

VPL = Σ [FCt / (1+k)^t] - Investimento Inicial
TIR = taxa que torna o VPL = 0
```

## CAPACIDADE E OCIOSIDADE

```
Taxa de Ocupação = Capacidade Utilizada / Capacidade Instalada × 100
Capacidade Ociosa% = 1 - Taxa de Ocupação

Custo da Capacidade Ociosa = CIF Fixo × Capacidade Ociosa%
Perda por Ociosidade (R$) = Custo da Capacidade Ociosa (impacto no resultado)

Custo Real com Ociosidade = Custo Padrão / Taxa de Ocupação
  → Se ocupação = 70%, custo unitário real é 43% maior que o padrão a 100%
```

## INDICADORES DE EFICIÊNCIA

```
Produtividade = Output (unidades) / Input (horas, R$, pessoas)
Eficiência de MOD = Horas Padrão / Horas Reais × 100
Rendimento de MP = Quantidade Produzida / Quantidade Consumida de MP × 100
Perda% = (MP Consumida - MP Incorporada ao Produto) / MP Consumida × 100
```
