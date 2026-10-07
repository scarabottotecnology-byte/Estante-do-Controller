# Referência: Fórmulas Excel para Projeção Financeira

> Os limiares citados aqui (R², coeficiente de variação, pesos) são **heurísticas**. **Valide por backtest** (veja `metodos-de-projecao.md`). Proteja divisões com `IFERROR` ou `IF` para evitar `#DIV/0!`.

## FORECAST.LINEAR — Tendência Linear

```excel
=FORECAST.LINEAR(x, y_conhecidos, x_conhecidos)
```

**Uso prático:**
- `x` = número do período futuro (ex: 13 para o 13º mês)
- `y_conhecidos` = valores históricos da linha (ex: B2:M2)
- `x_conhecidos` = sequência de períodos históricos (ex: {1,2,3,...,12})

**Exemplo — projetar Jan/26 com base em 12 meses históricos:**
```excel
=FORECAST.LINEAR(13, Histórico!B5:M5, {1,2,3,4,5,6,7,8,9,10,11,12})
```

**Quando usar:** tendência linear clara e dados sem sazonalidade relevante. Como ponto de partida (heurística), R² alto; confirme com backtest.

---

## TREND — Regressão Múltipla

```excel
=TREND(y_conhecidos, x_conhecidos, x_novo, [constante])
```

**Exemplo — projetar 3 meses futuros de uma vez:**
```excel
=TREND(Histórico!B5:M5, {1,2,3,4,5,6,7,8,9,10,11,12}, {13,14,15}, TRUE)
```
> Nota: Fórmula matricial — confirmar com Ctrl+Shift+Enter no Excel legado; no Excel 365 funciona normalmente.

**Quando usar:** Mesmo que FORECAST.LINEAR, mas quando se quer projetar múltiplos períodos de uma vez.

---

## Índice Sazonal × Tendência

### Passo 1 — Índice sazonal de cada mês
Para cada mês, calcule a razão entre o valor do mês e a **média do respectivo ano**, e tire a média dessas razões entre os anos:
```excel
=AVERAGE(B5/AVERAGE($B5:$M5), N5/AVERAGE($N5:$Y5))
```
*(exemplo para o mês de janeiro com 2 anos de histórico: colunas B a M no ano 1 e N a Y no ano 2)*

Confira que a **soma dos 12 índices é 12** (ou a média é 1). Se não for, normalize dividindo cada índice pela média dos índices.

> **Erro comum:** dividir a média dos janeiros pela média de **apenas um** ano mistura tendência com sazonalidade e distorce o índice.

### Passo 2 — Projetar com tendência dessazonalizada
1. Dessazonalize o histórico: valor do mês ÷ índice do mês.
2. Ajuste a tendência sobre a série dessazonalizada (`FORECAST.LINEAR` ou `TREND`).
3. Ressazonalize: tendência projetada × índice do mês projetado.

```excel
=FORECAST.LINEAR(25, SérieDessazonalizada, Períodos) * IndiceMes
```
*(Aplicar o índice sobre uma tendência ajustada nos dados brutos conta a sazonalidade duas vezes.)*

**Quando usar:** sazonalidade evidente e histórico com pelo menos dois ciclos completos (por exemplo, 24 meses).

---

## Média Móvel Ponderada (pesos padrão: 50/30/20)

```excel
=(L5*0,5 + K5*0,3 + J5*0,2) * (1 + Premissas!$B$3)
```
*(Últimos 3 meses × pesos, corrigido pela taxa de crescimento da aba Premissas)*

**Quando usar:** Dados estáveis, sem tendência clara, poucos pontos históricos.

---

## % Fixo sobre Receita (custos variáveis)

### Calcular % histórico:
```excel
=SUM(B6:M6)/SUM(B5:M5)
```
*(Custo total ÷ receita total dos 12 meses: média ponderada pela receita. A média simples dos percentuais mensais, `=AVERAGE(B6:M6/B5:M5)`, exige fórmula matricial no Excel antigo e pesa igual meses grandes e pequenos. Escolha e declare o critério.)*

### Aplicar sobre receita projetada:
```excel
=Projeção_Base!B5 * Premissas!$C$10
```
*(Receita projetada × % custo médio armazenado em Premissas)*

**Quando usar:** CMV, comissões, fretes, impostos sobre receita — qualquer custo com % histórica estável.

---

## Flat + Reajuste por Inflação (custos fixos)

```excel
=Histórico!$M10 * (1 + Premissas!$B$5)
```
*(Último valor real × (1 + índice do período). Confirme se o índice em Premissas é mensal ou anual.)*

**Para reajuste acumulado em projeções longas:**
```excel
=Histórico!$M10 * (1 + Premissas!$B$5)^(n/12)
```
*(n = número de meses no futuro)*

**Quando usar:** Aluguel, folha administrativa, contratos reajustados por índice, depreciação.

---

## CORREL e RSQ — Validar qualidade da tendência

```excel
=RSQ(Histórico!B5:M5, {1,2,3,4,5,6,7,8,9,10,11,12})
```
- Retorna R² (0 a 1)
- R² alto indica boa aderência da reta ao **passado**, mas não garante boa previsão. Use como triagem (por exemplo, R² abaixo de 0,70 sugere testar média móvel ou pedir premissa manual) e **confirme por backtest**

---

## Alertas automáticos (aba Alertas)

### Alerta de crescimento anômalo:
```excel
=IFERROR(IF(ABS(C5/B5-1)>Premissas!$B$20, "⚠️ CRESCIMENTO ANÔMALO: "&TEXT(C5/B5-1,"0%"), "OK"), "n/d")
```

### Alerta de desvio vs budget:
```excel
=IFERROR(IF(ABS(Projeção_Base!B5/Budget!B5-1)>Premissas!$B$21,
   "⚠️ DESVIO "&TEXT(Projeção_Base!B5/Budget!B5-1,"0%")&" vs Budget",
   "✓"), "n/d")
```
*(Os gatilhos ficam em `Premissas!B20` e `B21`; os valores iniciais, como 30% e 15%, são heurísticas ajustáveis.)*

### Desvio absoluto e %:
```excel
=Projeção_Base!B5 - Budget!B5          → Desvio R$
=(Projeção_Base!B5/Budget!B5)-1        → Desvio %
```
