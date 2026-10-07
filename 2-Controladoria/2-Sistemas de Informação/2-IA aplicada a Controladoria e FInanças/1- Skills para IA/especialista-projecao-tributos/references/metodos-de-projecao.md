# Métodos de projeção — escolha, validação e exemplos

Uso: Fases 3 e 4 do `especialista-projecao-tributos`. Os números dos exemplos são **fictícios**. Os limiares (R², coeficiente de variação, pesos) são **heurísticas de trabalho**, não normas: use-os como ponto de partida e **valide por backtest**.

---

## 1. Princípio

Escolha o método **pelos dados e por teste**, não por regra fixa. O método que melhor explica o passado não é necessariamente o que melhor prevê o futuro. Por isso, toda projeção relevante passa por **backtest** (seção 3) e é comparada com um método ingênuo.

## 2. Catálogo de métodos

| Situação dos dados | Método candidato | Observação |
|---|---|---|
| Tendência clara e estável | Regressão linear (`FORECAST.LINEAR`, `TREND`) | Verifique o ajuste (R²) e os resíduos; não extrapole muito além do histórico |
| Sazonalidade evidente | Índice sazonal × tendência | Exige pelo menos dois ciclos completos (por exemplo, 24 meses) |
| Dados estáveis, sem tendência | Média móvel (simples ou ponderada) | Pesos como 50/30/20 são ponto de partida; teste outros |
| Custo variável | % sobre a receita projetada | Use a mediana ou a média de período estável e verifique mudanças de mix |
| Custo fixo | Valor atual + reajuste (índice informado) | Declare o índice e a data de reajuste |
| Poucos dados (menos de 6 períodos) | Crescimento definido pelo usuário, rotulado como premissa | Não ajuste curva com tão pouca informação |
| Evento conhecido (novo produto, perda de cliente, reajuste de contrato) | Ajuste manual por driver | Registre evento, data e efeito |
| Receita com drivers claros | Volume × preço (ou clientes × ticket) | Preferível a projetar só o total |

**Projetar por drivers** costuma ser melhor que extrapolar o resultado: receita = volume × preço; margem bruta = receita − CMV; EBITDA = margem bruta − Opex.

## 3. Backtest (obrigatório para as linhas relevantes)

1. Separe os últimos 3 a 6 períodos como **teste** (ou use janela móvel).
2. Projete esses períodos usando só os dados anteriores.
3. Meça o erro: `APE = |real − projetado| / real` por período; **MAPE** = média dos APE; **viés** = soma de (projetado − real) / soma do real (positivo indica superestimação).
4. Compare com o método ingênuo (repetir o último valor ou o mesmo período do ano anterior). Se o método escolhido não supera o ingênuo, simplifique.
5. Registre o erro na aba de premissas e informe ao usuário.

**Exemplo:** real = 100, 110, 120, 130; projetado = 98, 115, 118, 140.
- APE = 2,0%; 4,5%; 1,7%; 7,7% → **MAPE ≈ 3,98%**.
- Viés = (−2 + 5 − 2 + 10) / 460 = **+2,4%** (superestima).

## 4. Exemplos de cálculo

**Média móvel ponderada (50/30/20):** últimos meses 100, 110, 120 (o mais recente é 120) → 0,5 × 120 + 0,3 × 110 + 0,2 × 100 = **113**.

**Regressão linear:** y = 100, 110, 120, 130 nos períodos 1 a 4 → próximo período (5) = **140**.

**Índice sazonal (trimestres):**
- Ano 1: 100, 120, 140, 140 (média 125). Ano 2: 110, 132, 154, 154 (média 137,5).
- Índice do trimestre = média dos (valor / média do ano): Q1 = (0,80 + 0,80)/2 = **0,80**; Q2 = **0,96**; Q3 = **1,12**; Q4 = **1,12**. A soma dos índices é 4,0.
- Projeção do ano 3 com média anual de 151,25 (+10% sobre 137,5): Q1 = 121; Q2 = 145,2; Q3 = 169,4; Q4 = 169,4; **total 605** (= 550 × 1,10).

## 5. Cenários (Fase 4)

- **Cenários são variações de drivers**, não multiplicadores arbitrários do resultado. Evite aplicar "×1,15" e "×0,85" a todas as linhas, porque isso trata custos fixos como se variassem com a receita.
- Se o usuário não definir as amplitudes, use valores **provisórios** e **rotule como premissa a confirmar**; peça a justificativa (histórico, contrato, mercado).
- Cada cenário deve manter a **coerência interna**: volume maior implica custo variável e capital de giro maiores; CAPEX sustenta a capacidade.

**Exemplo por drivers:**
- Base: volume 10.000 e preço R$ 100 → receita **R$ 1.000.000**.
- Otimista: volume +5% e preço +2% → 10.500 × 102 = **R$ 1.071.000**.
- Pessimista: volume −8% e preço 0% → 9.200 × 100 = **R$ 920.000**.

Probabilidades só entram se houver base para elas.

## 6. Tipos de orçamento (qual usar)

| Tipo | Quando faz sentido | Cuidado |
|---|---|---|
| Orçamento anual estático | Ambiente estável, controle de gastos | Fica obsoleto durante o ano |
| Forecast (revisões periódicas) | Acompanhar o ano com informação nova | Mantenha o orçado original como referência |
| Rolling forecast | Horizonte móvel (por exemplo, 12 meses à frente) para ambiente incerto | Exige processo e disciplina de atualização |
| Base zero | Revisão profunda de custos, realinhamento estratégico | Demorado; peça justificativa de cada gasto |
| Participativo | Engajar gestores nas metas | Risco de folga (sandbagging); calibre |

Fontes na Estante: `5-FP&A/1-Budget` (livros e textos de orçamento empresarial, planejamento orçamentário e análise de desempenho do orçamento), `3-Rolling Forecast` (estudo de caso) e `2-Forecast`. Resumo conceitual na base de conhecimento do `especialista-cfo` (tipos de orçamento e base zero).

## 7. Alertas (limiares são heurísticas)

Os valores abaixo são **gatilhos de investigação**, ajustáveis ao negócio: crescimento de linha acima de 30% mês a mês sem justificativa; desvio acumulado contra o orçamento acima de 15%; margem projetada abaixo do mínimo histórico; menos de 12 meses de histórico para projetar sazonalidade; carga tributária projetada diferente da histórica em mais de 2 pontos percentuais; RBT12 projetada se aproximando do limite de faixa do Simples (por exemplo, a menos de 10% do limite).

## 8. Integração com os demonstrativos

Esta skill projeta a **DRE** (receita, custos, despesas, EBITDA e tributos). Para **caixa e balanço**, entregue as premissas (capital de giro, CAPEX, financiamento) e acione `especialista-modelagem`, que integra DRE, DFC e BP, fecha o balanço e roda a sensibilidade.
