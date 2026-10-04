# KPIs de FOPAG e Gestão de Pessoal — Biblioteca com Benchmarks

## 1. INDICADORES DE CUSTO DE PESSOAL

### 1.1 FOPAG% sobre Receita Bruta
```
FOPAG% Receita = FOPAG Total (salários + enc. + prov. + benef.) / Receita Bruta × 100
```

| Setor | Faixa saudável | Alerta | Crítico |
|-------|---------------|--------|---------|
| Varejo farmacêutico | 6–12% | 12–16% | > 16% |
| Varejo geral | 8–14% | 14–18% | > 18% |
| Logística e distribuição | 12–18% | 18–24% | > 24% |
| Serviços (escritório) | 25–40% | 40–50% | > 50% |
| Indústria de confecção | 15–25% | 25–35% | > 35% |
| Restaurante / alimentação | 28–35% | 35–42% | > 42% |

### 1.2 Custo Médio por Colaborador
```
Custo médio colaborador = FOPAG Total / Headcount médio do período
```

### 1.3 Multiplicador Salarial (fator de carga)
```
Multiplicador = CTMO / Salário Bruto base

Benchmarks Brasil:
  Lucro Real (INSS 20%)           → 1,80× a 2,20×
  Lucro Presumido (INSS 20%)      → 1,75× a 2,10×
  Simples (Anexo I/II — CPP no DAS) → 1,35× a 1,60×
  Simples (Anexo IV — INSS fora)  → 1,70× a 2,00×
```

### 1.4 Receita por Colaborador
```
Receita por colaborador = Receita Líquida / Headcount médio
```

| Setor | Faixa típica |
|-------|-------------|
| Farmácia de rede | R$ 150–300k/ano/funcionário |
| Varejo alimentar | R$ 200–400k/ano/funcionário |
| Logística | R$ 300–600k/ano/funcionário |
| Serviços contábeis | R$ 80–150k/ano/funcionário |

### 1.5 Produtividade de Pessoal
```
Produtividade = Receita Líquida / FOPAG Total

→ Quanto de receita cada R$ de folha gera
→ Benchmark varejo: R$ 6–10 de receita por R$ 1 de folha
```

---

## 2. INDICADORES DE TURNOVER

### 2.1 Taxa de Turnover Global
```
Turnover% = (Admissões + Demissões) / 2 / Headcount médio × 100
```

### 2.2 Turnover de Saída (Involuntário)
```
Turnover saída% = Demissões sem justa causa / Headcount médio × 100
```

### 2.3 Turnover Voluntário
```
Turnover voluntário% = Pedidos de demissão / Headcount médio × 100
```

| Setor | Turnover anual saudável | Alerta |
|-------|------------------------|--------|
| Varejo farmacêutico | 20–40% | > 50% |
| Logística / armazém | 30–60% | > 80% |
| Administrativo | 10–20% | > 30% |
| Call center / atendimento | 50–80% | > 100% |
| Confecção/têxtil | 20–40% | > 60% |

### 2.4 Custo Total do Turnover
```
Custo de turnover = (Custo de rescisão médio
                  + Custo de recrutamento e seleção
                  + Custo de treinamento/integração
                  + Perda de produtividade estimada) × Número de desligamentos no período

Estimativa rápida: 1,5× a 2,5× o salário bruto mensal por colaborador desligado
```

---

## 3. INDICADORES DE ABSENTEÍSMO

### 3.1 Taxa de Absenteísmo
```
Absenteísmo% = (Horas ausentes no período / Horas contratadas no período) × 100

Horas ausentes = Faltas não justificadas + Atestados médicos + Licenças + Atrasos
               (excluir: férias, feriados, folgas programadas)
```

| Nível | Taxa de absenteísmo | Status |
|-------|---------------------|--------|
| Ótimo | < 1,5% | 🟢 |
| Aceitável | 1,5–3,0% | 🟡 |
| Atenção | 3,0–5,0% | 🟠 |
| Crítico | > 5,0% | 🔴 |

### 3.2 Custo do Absenteísmo
```
Custo absenteísmo = CTMO diário médio × Total de dias perdidos no período

CTMO diário = CTMO mensal / 22 dias úteis (aproximação)
```

### 3.3 Frequência de Acidentes de Trabalho
```
Taxa de frequência = (Acidentes com afastamento / Horas trabalhadas) × 1.000.000
```

---

## 4. INDICADORES DE HEADCOUNT

### 4.1 Headcount por Centro de Custo
```
Tabela de headcount = Número de colaboradores ativos por CC no último dia do mês
(snapshot date)
```

### 4.2 Headcount Médio
```
Headcount médio = (Headcount início do mês + Headcount fim do mês) / 2
```

### 4.3 Tempo Médio de Casa
```
Tempo médio de casa = Soma do tempo de serviço de todos os colaboradores / Headcount
→ Indicador de maturidade e estabilidade do quadro
→ Alerta se < 12 meses (equipe muito nova, alto turnover estrutural)
```

### 4.4 Horas Extras — Indicadores
```
HE% sobre jornada = Horas extras pagas / Horas totais trabalhadas × 100

→ Saudável: < 5%
→ Atenção: 5–10%
→ Crítico: > 10% (indica subdimensionamento do quadro ou pico sazonal não planejado)

Custo HE = Horas extras × (Custo hora normal × 150%) para 50%
                         ou (Custo hora normal × 200%) para 100%
```

---

## 5. INDICADORES DE BENEFÍCIOS

### 5.1 Custo de Benefícios por Colaborador
```
Custo mensal benefícios = (VT + VR/VA + Plano saúde + Odonto + Seguro vida + outros)
                        / Headcount médio
```

### 5.2 Benefícios% sobre FOPAG
```
Benefícios% = Total benefícios / FOPAG bruto × 100

→ Varejo: 8–15% do bruto
→ Serviços: 12–20% do bruto
```

---

## 6. DASHBOARD EXECUTIVO DE FOPAG

Estrutura recomendada para relatório mensal ao C-Level:

```
┌─────────────────────────────────────────────────────────────────┐
│  PAINEL FOPAG — [MÊS/ANO]                                       │
├─────────────┬──────────────┬──────────────┬─────────────────────┤
│ FOPAG Total │ Budget        │ Variância     │ Status              │
│ R$ XXX.XXX  │ R$ XXX.XXX   │ +/-  R$ XXX  │ 🟢/🟡/🔴           │
├─────────────┴──────────────┴──────────────┴─────────────────────┤
│ Headcount atual: XXX    |  Turnover mês: X,X%  |  Absen.: X,X%  │
├──────────────────────────────────────────────────────────────────┤
│ FOPAG por Centro de Custo    │ R$       │ % Total │ vs Budget    │
│ ─── Operacional / Loja       │ XXX.XXX  │  XX%    │ 🟢 -X%      │
│ ─── Logística                │ XXX.XXX  │  XX%    │ 🟡 +X%      │
│ ─── Administrativo           │ XXX.XXX  │  XX%    │ 🟢 -X%      │
│ ─── Comercial                │ XXX.XXX  │  XX%    │ 🔴 +X%      │
├──────────────────────────────────────────────────────────────────┤
│ Provisões do mês             │ R$ XXX.XXX  (incluídas no total)  │
│ Passivo trabalhista acum.    │ R$ XXX.XXX                        │
├──────────────────────────────────────────────────────────────────┤
│ ALERTAS:                                                          │
│ ⚠ X colaboradores com férias vencidas a regularizar             │
│ ⚠ Horas extras acima do orçado em [CC]: +X%                     │
│ ⚠ Turnover em [área] acima do benchmark                         │
└──────────────────────────────────────────────────────────────────┘
```

---

## 7. CHECKLIST MENSAL DO FECHAMENTO DE FOPAG

- [ ] Folha processada e conferida (brutos, descontos, líquidos)
- [ ] SEFIP/GFIP gerada e transmitida
- [ ] DARF IRRF gerado (dia 20 do mês seguinte)
- [ ] GPS/INSS gerada
- [ ] FGTS depositado (dia 7 do mês seguinte)
- [ ] Provisões de férias calculadas e lançadas no ERP
- [ ] Provisões de 13° calculadas e lançadas no ERP
- [ ] Budget vs Realizado conferido e variâncias explicadas
- [ ] Headcount conferido (admissões e demissões do mês)
- [ ] eSocial: eventos enviados (S-1200, S-1210, S-2299 se rescisões)
- [ ] Rescisões calculadas e homologadas dentro do prazo
- [ ] CAGED enviado (até dia 7 do mês seguinte)
