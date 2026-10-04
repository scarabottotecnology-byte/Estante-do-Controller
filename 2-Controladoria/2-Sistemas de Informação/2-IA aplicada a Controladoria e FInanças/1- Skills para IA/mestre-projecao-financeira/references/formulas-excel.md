# Referência: Fórmulas Excel para Projeção Financeira

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

**Quando usar:** Tendência linear clara, R² > 0,85, dados sem sazonalidade relevante.

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

### Passo 1 — Calcular o índice sazonal histórico
```excel
=AVERAGE(B5,N5,Z5)/AVERAGE(Histórico!$B5:$M5)
```
*(Média de todos os Janeiros ÷ Média geral = Índice de Janeiro)*

### Passo 2 — Aplicar índice sobre a tendência projetada
```excel
=FORECAST.LINEAR(13, Histórico!$B5:$M5, {1,...,12}) * IndiceJaneiro
```

**Quando usar:** Sazonalidade evidente (coef. de variação > 15%), histórico com pelo menos 24 meses.

---

## Média Móvel Ponderada (pesos padrão: 50/30/20)

```excel
=(L5*0,5 + K5*0,3 + J5*0,2) * (1 + Premissas!$B$3)
```
*(Últimos 3 meses × pesos, corrigido pela taxa de crescimento da aba Premissas)*

**Quando usar:** Dados estáveis, sem tendência clara, poucos pontos históricos.

---

## % Fixo sobre Receita (custos variáveis)

### Calcular % médio histórico:
```excel
=AVERAGE(B6:M6/B5:M5)
```
*(Linha de custo ÷ Receita, média dos 12 meses)*

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
*(Último valor real × (1 + IPCA))*

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
- R² > 0,85 → uso de regressão linear justificado
- R² < 0,70 → preferir média móvel ou solicitar premissa manual

---

## Alertas automáticos (aba Alertas)

### Alerta de crescimento anômalo:
```excel
=IF(ABS(C5/B5-1)>0.3, "⚠️ CRESCIMENTO ANÔMALO: "&TEXT(C5/B5-1,"0%"), "OK")
```

### Alerta de desvio vs budget:
```excel
=IF(ABS(Projeção_Base!B5/Budget!B5-1)>0.15, 
   "⚠️ DESVIO "&TEXT(Projeção_Base!B5/Budget!B5-1,"0%")&" vs Budget",
   "✓")
```

### Desvio absoluto e %:
```excel
=Projeção_Base!B5 - Budget!B5          → Desvio R$
=(Projeção_Base!B5/Budget!B5)-1        → Desvio %
```
