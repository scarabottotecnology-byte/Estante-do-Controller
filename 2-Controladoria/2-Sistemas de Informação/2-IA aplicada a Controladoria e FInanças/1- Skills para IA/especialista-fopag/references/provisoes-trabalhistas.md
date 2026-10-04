# Provisões Trabalhistas — Metodologia e Cálculos

## 1. CONCEITO E IMPORTÂNCIA

Provisões trabalhistas são **obrigações estimadas** que a empresa acumula mensalmente por regime de competência, mesmo antes do efetivo pagamento. Sem provisões corretas, o DRE subestima custos e o Balanço Patrimonial omite passivos reais.

**Principais provisões trabalhistas:**
1. Provisão de Férias
2. Provisão de 13º Salário (Gratificação Natalina)
3. FGTS sobre Provisões
4. INSS Patronal sobre Provisões
5. Provisão de Rescisão (opcional — por expectativa de turnover)

---

## 2. PROVISÃO DE FÉRIAS

### Base legal
- CLT, arts. 129–145
- Período aquisitivo: 12 meses de trabalho
- Período concessivo: 12 meses após o aquisitivo
- Adicional constitucional: 1/3 do salário de férias (CF/88, art. 7°, XVII)

### Cálculo mensal da provisão

```
Provisão bruta de férias = Salário bruto × (1 + 1/3) / 12
                        = Salário bruto × 1,3333 / 12
                        = Salário bruto × 0,11111

Onde:
  1,3333 = 1 (salário de férias) + 0,3333 (1/3 constitucional)
  ÷ 12   = competência mensal
```

**Exemplo:**
```
Salário bruto:               R$ 3.000,00
Provisão bruta férias:       R$ 3.000 × 1,3333 / 12 = R$ 333,33
```

### Encargos patronais sobre a provisão de férias

Os encargos incidem sobre a **provisão bruta** de férias (salário + 1/3):

```
Encargos sobre prov. férias = Provisão bruta × (INSS% + FGTS% + RAT/FAP% + Terceiros%)
```

**Exemplo (Lucro Real, comércio, RAT 1%):**
```
Provisão bruta férias:           R$ 333,33
INSS patronal (20%):             R$ 66,67
FGTS (8%):                       R$ 26,67
RAT/FAP (1,5%):                  R$ 5,00
Terceiros (3,1%):                R$ 10,33
Total encargos prov. férias:     R$ 108,67
Total provisão férias (tudo):    R$ 442,00
```

> ⚠️ **INSS não incide sobre o terço constitucional de férias** quando pago na época própria (STJ — Súmula 328). Mas como provisão contábil, é prudente provisionar integralmente para cobrir o eventual pagamento em dobro (atraso).

### Quando a provisão aumenta vs. decresce
- **Aumenta:** a cada mês de trabalho acumulado sem gozo
- **Decresce:** quando o colaborador entra em gozo (a provisão acumulada é baixada)
- **Abono pecuniário:** até 1/3 das férias pode ser convertido em dinheiro; provisionar junto

---

## 3. PROVISÃO DE 13º SALÁRIO

### Base legal
- Lei 4.090/1962 e Lei 4.749/1965
- Direito proporcional: 1/12 por mês (ou fração ≥ 15 dias) trabalhado no ano
- Pagamento: primeira parcela (novembro) e segunda parcela (20 de dezembro)

### Cálculo mensal da provisão

```
Provisão bruta 13° = Salário bruto / 12

Competência: cada mês trabalhado = 1/12 do salário bruto anual
```

**Exemplo:**
```
Salário bruto:            R$ 3.000,00
Provisão bruta 13°:       R$ 3.000 / 12 = R$ 250,00
```

### Encargos patronais sobre a provisão de 13º

```
Encargos sobre prov. 13° = Provisão bruta 13° × (INSS% + FGTS% + RAT/FAP% + Terceiros%)
```

> ⚠️ O INSS **incide sobre o 13°** (diferente das férias com terço). Alíquota patronal integral (20% no Lucro Real).

**Exemplo (Lucro Real, comércio, RAT 1%):**
```
Provisão bruta 13°:            R$ 250,00
INSS patronal (20%):           R$ 50,00
FGTS (8%):                     R$ 20,00
RAT/FAP (1,5%):                R$ 3,75
Terceiros (3,1%):              R$ 7,75
Total encargos prov. 13°:      R$ 81,50
Total provisão 13° (tudo):     R$ 331,50
```

---

## 4. QUADRO RESUMO — PROVISÃO MENSAL POR COLABORADOR

Calcule o total de provisões mensais a lançar no DRE:

| Item | Fórmula | R$ Exemplo |
|------|---------|-----------|
| Salário bruto | — | 3.000,00 |
| **Provisão bruta férias** | Sal × 1,3333 / 12 | 333,33 |
| INSS s/ prov. férias (20%) | 333,33 × 20% | 66,67 |
| FGTS s/ prov. férias (8%) | 333,33 × 8% | 26,67 |
| RAT/FAP s/ prov. férias (1,5%) | 333,33 × 1,5% | 5,00 |
| Terceiros s/ prov. férias (3,1%) | 333,33 × 3,1% | 10,33 |
| **Subtotal provisão férias** | | **441,99** |
| **Provisão bruta 13°** | Sal / 12 | 250,00 |
| INSS s/ prov. 13° (20%) | 250,00 × 20% | 50,00 |
| FGTS s/ prov. 13° (8%) | 250,00 × 8% | 20,00 |
| RAT/FAP s/ prov. 13° (1,5%) | 250,00 × 1,5% | 3,75 |
| Terceiros s/ prov. 13° (3,1%) | 250,00 × 3,1% | 7,75 |
| **Subtotal provisão 13°** | | **331,50** |
| **TOTAL PROVISÕES MENSAIS** | | **773,49** |
| **CTMO com provisões** | 3.000 + enc. + prov. | **~4.980,00** |

---

## 5. CONTABILIZAÇÃO DAS PROVISÕES

### Lançamento contábil mensal (provisão)
```
D — Despesa de provisão de férias (resultado)         R$ 441,99
C — Provisão para férias a pagar (passivo circulante) R$ 441,99

D — Despesa de provisão de 13° salário (resultado)    R$ 331,50
C — Provisão para 13° salário a pagar (PC)            R$ 331,50
```

### Lançamento na baixa (pagamento de férias)
```
D — Provisão para férias a pagar (PC)    → baixa do acumulado
D — Variação (se houver reajuste salarial)
C — Banco / Caixa
```

---

## 6. PASSIVO TRABALHISTA ACUMULADO

O passivo trabalhista é o saldo total das provisões acumuladas não pagas. Deve ser informado no Balanço Patrimonial no grupo **Passivo Circulante**.

### Composição do passivo trabalhista
```
Saldo de provisão de férias (por colaborador × tempo de casa)
+ Encargos sobre provisão de férias (INSS + FGTS + RAT + Terceiros)
+ Saldo de provisão de 13° (meses acumulados no ano)
+ Encargos sobre provisão de 13°
+ Provisão de rescisão estimada (opcional)
= Passivo trabalhista total
```

### Alerta: Provisão defasada
Se o colaborador recebeu reajuste salarial, a provisão acumulada pode estar **subavaliada**. Recalcular com o novo salário e lançar o ajuste.

```
Ajuste de provisão = (Novo salário - Salário anterior) × Meses acumulados × 1,3333 / 12
                   × (1 + Total de encargos%)
```

---

## 7. PROVISÃO DE RESCISÃO (ESTIMATIVA POR TURNOVER)

Para empresas com turnover histórico relevante, é prudente provisionar o custo estimado de rescisões futuras.

### Metodologia
```
Taxa de turnover histórica = Demissões nos últimos 12 meses / Headcount médio

Custo médio de rescisão por colaborador = (Média de verbas rescisórias dos últimos 12 meses)

Provisão mensal rescisão = Headcount atual × Taxa de turnover / 12 × Custo médio de rescisão
```

> Esta provisão é **gerencial** (não obrigatória pela legislação), mas aumenta a qualidade preditiva do DRE e do balanço.

---

## 8. INDICADORES DE CONTROLE DAS PROVISÕES

```
Grau de cobertura das provisões = Provisão acumulada / Passivo trabalhista real estimado
→ Saudável: ≥ 95%

Impacto das provisões sobre EBITDA = Total provisões / EBITDA operacional × 100
→ Benchmarking: 5–15% em empresas de serviço; 3–8% em varejo

Dias de férias vencidas médio = Funcionários com férias vencidas / Headcount total × 100
→ Alerta: > 20% do quadro com férias vencidas representa risco legal e passivo elevado
```
