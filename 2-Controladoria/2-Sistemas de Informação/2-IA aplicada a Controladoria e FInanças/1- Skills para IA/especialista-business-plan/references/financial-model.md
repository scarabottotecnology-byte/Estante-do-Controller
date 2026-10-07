# Modelo financeiro e análise de viabilidade

Índice: 1. Viabilidade em quatro dimensões · 2. Fórmulas · 3. Cenários · 4. Análise de retorno ("vale a pena?") · 5. Sensibilidade · 6. Projeções · 7. Cuidados

## 1. Viabilidade em quatro dimensões

Avalie sempre as quatro, mesmo que rapidamente. A ideia pode passar em uma e morrer em outra.

**Comercial**: existe cliente? existe dor? existe disposição a pagar (evidência, não opinião)? quem é o público-alvo? como adquirir clientes e a que custo?

**Operacional**: como o produto/serviço é entregue? que recursos e processos são necessários? o que pode ser automatizado? onde está o gargalo de capacidade?

**Financeira**: investimento inicial, custos fixos, custos variáveis, receita potencial, margem bruta e operacional, ponto de equilíbrio, capital de giro, payback, ROI, fluxo de caixa.

**Estratégica**: diferenciação, barreiras de entrada, dependência de fornecedores e plataformas, poder de negociação, risco competitivo, potencial de escala.

## 2. Fórmulas

```
Receita                    = Clientes × Ticket médio (× frequência, se recorrente)
Margem bruta               = Receita − Custos variáveis
Margem bruta %             = Margem bruta / Receita
Resultado operacional      = Receita − Custos variáveis − Custos fixos
Margem operacional %       = Resultado operacional / Receita
Margem de contribuição %   = (Receita − Custos variáveis) / Receita
Ponto de equilíbrio (R$)   = Custos fixos / Margem de contribuição %
Ponto de equilíbrio (un.)  = Custos fixos / (Preço unitário − Custo variável unitário)
CAC                        = Investimento comercial e marketing / Novos clientes
LTV                        = Receita média por cliente × margem × período de retenção
LTV/CAC                    = LTV / CAC
Payback do investimento    = Investimento inicial / Geração de caixa (mensal ou anual)
Payback do CAC (meses)     = CAC / (Receita mensal por cliente × margem)
ROI                        = Retorno líquido / Investimento
Burn rate                  = Saída líquida de caixa mensal
Runway                     = Caixa disponível / Burn rate
```

Notas de uso:
- No LTV, use margem (não receita bruta) e um período de retenção realista; para assinatura, retenção = 1 / churn mensal.
- Inclua impostos sobre receita nos custos variáveis. Em negócios no Brasil, o regime tributário (Simples, Presumido, Real) muda a margem de forma relevante; se for decisivo para a tese, sinalize como premissa crítica e, havendo skill de projeção tributária disponível, acione-a em vez de chutar alíquotas.
- Sempre inclua capital de giro (prazo de recebimento, estoque, prazo de pagamento). Muitos negócios "lucrativos" quebram por caixa.

## 3. Cenários

Quando os dados forem insuficientes, **não invente um número único**. Construa três cenários com premissas explícitas, em tabela:

| Premissa | Conservador | Base | Agressivo |
|---|---|---|---|
| Clientes/mês | | | |
| Ticket médio | | | |
| Conversão / CAC | | | |
| Churn / retenção | | | |
| Margem bruta | | | |
| Investimento inicial | | | |

Todos os valores são `PREMISSA DE TRABALHO` até o usuário confirmar ou uma fonte sustentar. Indique qual cenário você considera mais provável e por quê. Deixe claro que o cenário conservador deve ser o que o negócio precisa suportar para justificar o investimento.

## 4. Análise de retorno ("vale a pena?")

Quando perguntarem se uma ideia vale a pena, nunca responda só sim ou não. Estruture:

- **Capital necessário**: quanto, aproximadamente, para começar (investimento + capital de giro + colchão até o break-even).
- **Tempo até a primeira receita**: quanto para validar e faturar.
- **Tempo até o break-even**.
- **Payback**: prazo para recuperar o investimento.
- **Potencial de margem**: onde está a criação de valor.
- **Potencial de escala**: como cresce.
- **Principais riscos**: o que pode destruir a tese econômica.
- **Principais premissas**: as variáveis que precisam ser verdadeiras para o modelo funcionar.

Feche com um veredito condicional e honesto ("funciona se X e Y; morre se Z"), apontando qual teste barato resolve a incerteza dominante.

## 5. Análise de sensibilidade

Identifique as variáveis que mais movem o resultado (ticket, volume de clientes, conversão, CAC, churn, margem, custo, investimento, capital de giro) e mostre o efeito de variações (por exemplo, ±10% e ±20%) sobre receita, EBITDA, caixa, payback e ROI. O objetivo não é a tabela em si, e sim dizer ao usuário **quais 2 ou 3 premissas decidem o jogo** e merecem ser validadas primeiro.

## 6. Projeções

Com dados suficientes (ou premissas aprovadas), projete 12, 24 e 36 meses (60 quando fizer sentido), em três cenários:

Receita · custos variáveis · custos fixos · despesas comerciais e marketing · administrativo · tecnologia · impostos · margem de contribuição · EBITDA · lucro · fluxo de caixa · CAPEX · capital de giro · investimento · retorno acumulado.

Para planilha, gere um .xlsx com premissas em uma aba separada e as demais abas referenciando-as por fórmula (o usuário deve conseguir alterar uma premissa e ver o resultado mudar).

## 7. Cuidados

- Benchmarks (por exemplo, "LTV/CAC saudável é 3x") são heurísticas populares, não fatos universais. Se citá-los, rotule como regra prática e não como dado de mercado.
- Não use taxas de conversão, churn, CAC ou margens "típicas de mercado" sem fonte; peça ao usuário, pesquise ou trate como premissa explícita.
- Se o modelo só fecha com premissas agressivas, diga isso com todas as letras.
