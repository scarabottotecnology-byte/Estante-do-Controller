# Verbas Rescisórias — Tabela Completa e Simulador

## 1. TABELA GERAL DE VERBAS POR MODALIDADE DE DEMISSÃO

| Verba | Sem Justa Causa | Com Justa Causa | Pedido de Demissão | Acordo (§6° CLT) | Término de Contrato |
|-------|:---:|:---:|:---:|:---:|:---:|
| Saldo de salário | ✅ | ✅ | ✅ | ✅ | ✅ |
| Aviso prévio trabalhado pelo empregado | ✅ | ❌ | ✅ | — | — |
| Aviso prévio indenizado (empresa paga) | ✅ | ❌ | ❌ | ½ indenizado | — |
| Férias vencidas + 1/3 constitucional | ✅ | ✅ | ✅ | ✅ | ✅ |
| Férias proporcionais + 1/3 | ✅ | ❌ | ✅ | ✅ | ✅ |
| 13° salário proporcional | ✅ | ❌ | ✅ | ✅ | ✅ |
| Multa do FGTS (40%) | ✅ | ❌ | ❌ | 20% | ❌ |
| Contribuição social 10% FGTS | ✅ | ❌ | ❌ | ❌ | ❌ |
| FGTS do mês e aviso prévio | ✅ | ❌ | ❌ | ✅ | ✅ |
| Liberação do FGTS para saque | ✅ | ❌ | ❌ | ✅ (50%) | — |
| Seguro-desemprego | ✅ | ❌ | ❌ | ❌ | — |

---

## 2. AVISO PRÉVIO PROPORCIONAL (Lei 12.506/2011)

```
Aviso prévio = 30 dias (base)
             + 3 dias por ano completo de serviço (máximo até 60 dias adicionais)
             = Máximo: 90 dias

Fórmula:
  AP = 30 + (3 × anos completos trabalhados)
  Limite máximo = 90 dias
```

| Anos de serviço | Aviso prévio |
|----------------|-------------|
| Menos de 1 ano | 30 dias |
| 1 ano | 33 dias |
| 2 anos | 36 dias |
| 5 anos | 45 dias |
| 10 anos | 60 dias |
| 20 anos | 90 dias (teto) |

---

## 3. FÓRMULAS DE CÁLCULO — VERBA A VERBA

### 3.1 Saldo de Salário
```
Saldo = Salário bruto / 30 × Dias trabalhados no mês
      + Horas extras pendentes
      + Adicionais pendentes
```

### 3.2 Aviso Prévio Indenizado
```
AP indenizado = (Salário bruto / 30) × Dias de aviso prévio calculado
              + 1/3 constitucional de férias sobre o AP (se houver direito)
```

> O aviso prévio indenizado integra a remuneração para fins de FGTS e 13°.

### 3.3 Férias Vencidas (período aquisitivo completado)
```
Férias vencidas = Salário bruto × 1,3333
                (1 salário + 1/3 constitucional)
```

> Se há abono pecuniário de 1/3 já solicitado, recalcular proporcionalmente.

### 3.4 Férias Proporcionais
```
Férias proporcionais = (Salário bruto / 12) × Meses completos do período aquisitivo em curso
                     × 1,3333 (com o terço constitucional)
```

| Meses trabalhados no período | Avos de férias |
|------------------------------|---------------|
| 1 a 14 dias | 0 avos |
| 15 dias a 1 mês | 1/12 |
| 1 mês completo | 1/12 |
| 2 meses | 2/12 |
| … | … |
| 12 meses | 12/12 (= direito pleno) |

### 3.5 13° Proporcional
```
13° proporcional = Salário bruto / 12 × Meses completos trabalhados no ano
                 (Fração ≥ 15 dias conta como mês completo)
```

### 3.6 Multa do FGTS
```
Multa FGTS = Saldo do FGTS × 40% (demissão sem justa causa)
           ou
           Saldo do FGTS × 20% (acordo § 6° CLT)

Saldo FGTS = Depósitos realizados + Correção + Rendimentos - Saques anteriores
```

> A multa é paga pelo **empregador diretamente ao trabalhador**, fora do sistema FGTS.

### 3.7 Contribuição Social sobre FGTS (Lei 110/2001)
```
Contribuição social = Saldo do FGTS × 10%
(paga pelo empregador ao governo — não vai para o trabalhador)
```

---

## 4. INCIDÊNCIA DE INSS E IRRF SOBRE VERBAS RESCISÓRIAS

| Verba | Incide INSS? | Incide IRRF? |
|-------|:---:|:---:|
| Saldo de salário | ✅ | ✅ |
| Aviso prévio indenizado | ✅ | ✅ |
| Aviso prévio trabalhado | ✅ | ✅ |
| Férias vencidas | ✅ | ✅ |
| 1/3 constitucional s/ férias vencidas | ❌ (isento INSS — Súmula STJ 328) | ✅ |
| Férias proporcionais | ❌ (isento — OJ 195 SDI-1 TST) | ✅ |
| 1/3 s/ férias proporcionais | ❌ | ❌ (isento IRRF) |
| 13° proporcional | ✅ | ✅ |
| Multa FGTS 40% | ❌ | ❌ |
| Contribuição social 10% FGTS | ❌ | ❌ |
| Indenização por tempo (estabilidade) | ❌ | ❌ |

---

## 5. SIMULADOR DE RESCISÃO — TEMPLATE DE CÁLCULO

```
DADOS DO COLABORADOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Nome:                    _______________
Data admissão:           ___/___/_____
Data demissão:           ___/___/_____
Tipo de rescisão:        _______________
Salário bruto:           R$ ___________
Meses no período aq. em curso: ___ meses

CÁLCULO DAS VERBAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Saldo de salário:            R$ _______
(= Salário / 30 × dias trabalhados no mês)

Aviso prévio indenizado:     R$ _______
(= Salário / 30 × dias de AP)

Férias vencidas + 1/3:       R$ _______
(= Salário × 1,3333)

Férias proporcionais + 1/3:  R$ _______
(= Salário / 12 × avos × 1,3333)

13° proporcional:            R$ _______
(= Salário / 12 × meses no ano)

Multa FGTS (40%):            R$ _______
(= Saldo FGTS × 40%)

Contribuição social (10%):   R$ _______
(pago ao governo)

BRUTO RESCISÓRIO:            R$ _______

DESCONTOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INSS empregado:              R$ _______
IRRF:                        R$ _______
Outros descontos:            R$ _______
TOTAL DESCONTOS:             R$ _______

LÍQUIDO A PAGAR:             R$ _______

CUSTO TOTAL PARA A EMPRESA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Verbas brutas:               R$ _______
(+) Multa FGTS 40%:          R$ _______
(+) Contrib. social 10%:     R$ _______
(+) FGTS sobre verbas:       R$ _______
CUSTO TOTAL EMPRESA:         R$ _______
```

---

## 6. PRAZO DE PAGAMENTO (Homologação)

| Tipo de rescisão | Prazo para pagamento |
|-----------------|---------------------|
| Com aviso prévio trabalhado | 1° dia útil após o último dia |
| Com aviso prévio indenizado | 10° dia corrido após notificação |
| Sem aviso prévio (demissão imediata) | 10° dia corrido após demissão |

> ⚠️ Multa por atraso: artigo 477, § 8° CLT — salário mínimo por colaborador, aplicada pelo Auditor Fiscal.

---

## 7. CASOS ESPECIAIS

### Estabilidade provisória
Gestante, acidentado, dirigente sindical, membro CIPA e outros têm **estabilidade provisória**. A demissão sem justa causa gera direito à **indenização substitutiva** (salários do período estabilitário).

### Rescisão em contrato por tempo determinado
- Se empresa rescinde antes do prazo: indenização de 50% sobre os salários restantes
- Se empregado pede demissão: não recebe nada por essa quebra, mas perde aviso proporcional

### Transferência para outra empresa do grupo
- Se há mudança de CNPJ empregador sem rescisão formal → verificar continuidade do contrato
- Se há rescisão e nova admissão → calcular verbas normalmente, com risco de reconhecimento de unicidade

### Acordo § 6° CLT (Lei 13.467/2017 — Reforma Trabalhista)
- Apenas para rescisão acordada entre empresa e empregado
- Multa FGTS = 20% (em vez de 40%)
- Aviso prévio indenizado pela empresa = 50%
- Empregado saca 80% do saldo FGTS
- **Não** tem direito ao seguro-desemprego
