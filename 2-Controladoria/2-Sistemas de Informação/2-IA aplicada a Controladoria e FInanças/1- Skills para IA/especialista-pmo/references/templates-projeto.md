# Templates de Projeto — PMO Controladoria

## 1. PROJECT CHARTER (Ficha do Projeto)

```
═══════════════════════════════════════════════════════
FICHA DO PROJETO
═══════════════════════════════════════════════════════
Nome do Projeto   : [Nome descritivo e objetivo]
Código / ID       : PROJ-[ANO]-[NNN]
Data de Criação   : ___/___/______
Versão            : 1.0

OBJETIVO (SMART)
─────────────────
[O quê] + [Por quê] + [Para quem] + [Até quando] + [Como medir]

ESCOPO
─────────────────
INCLUI:
  □ [entregável 1]
  □ [entregável 2]

NÃO INCLUI (Out of Scope):
  □ [item excluído 1]
  □ [item excluído 2]

STAKEHOLDERS
─────────────────
Patrocinador      : [nome] — [cargo]
Gestor do Projeto : [nome] — [cargo]
Equipe Principal  : [nomes e papéis]
Impactados        : [áreas / BUs afetadas]

PREMISSAS
─────────────────
□ [premissa 1 — o que precisa ser verdade para o projeto funcionar]
□ [premissa 2]

RESTRIÇÕES
─────────────────
□ Prazo máximo   : ___/___/______
□ Orçamento máx. : R$ ___________
□ Restrições de recursos: [ex: equipe disponível apenas 20h/semana]

CRITÉRIOS DE SUCESSO
─────────────────────
□ [métrica 1: o que mediremos e qual o valor-alvo]
□ [métrica 2]
□ [métrica 3]

RISCOS INICIAIS
────────────────
□ [risco 1] — Prob: A/M/B — Impacto: A/M/B
□ [risco 2]

APROVAÇÕES
───────────
Patrocinador: _________________________ Data: ___/___/______
Gestor:       _________________________ Data: ___/___/______
═══════════════════════════════════════════════════════
```

---

## 2. RACI — MATRIZ DE RESPONSABILIDADES

```
R = Responsável (executa)
A = Aprovador (assina / valida formalmente)
C = Consultado (opina antes da decisão)
I = Informado (recebe a informação depois)

┌─────────────────────────────┬──────────┬──────────┬──────────┬──────────┬──────────┐
│ Entregável / Decisão        │ [Papel1] │ [Papel2] │ [Papel3] │ [Papel4] │ [Papel5] │
├─────────────────────────────┼──────────┼──────────┼──────────┼──────────┼──────────┤
│ Kick-off                    │    A     │    R     │    I     │    I     │    C     │
│ Diagnóstico Preliminar      │    A     │    R     │    C     │    I     │    I     │
│ Plano de Projeto            │    A     │    R     │    C     │    C     │    I     │
│ [Entregável 4]              │          │          │          │          │          │
│ [Entregável 5]              │          │          │          │          │          │
│ Apresentação Final          │    A     │    R     │    C     │    I     │    I     │
│ Aceite Formal               │    A     │    I     │    I     │    I     │    I     │
└─────────────────────────────┴──────────┴──────────┴──────────┴──────────┴──────────┘
```

---

## 3. PLANO DE COMUNICAÇÃO

| Comunicação | Audiência | Frequência | Canal | Responsável | Formato |
|---|---|---|---|---|---|
| Reunião Operacional | Equipe do projeto | Semanal | Teams / Presencial | Gestor do Projeto | Pauta + Ata |
| Reunião de Progresso | CFO + Controller | Quinzenal | Presencial | Gestor do Projeto | Status Report |
| Comitê Executivo | CFO + Diretoria | Mensal | Presencial | Patrocinador | Dashboard + PPTX |
| E-mail de Status | Stakeholders | Semanal | E-mail | Gestor do Projeto | Template padrão |
| Relatório Final | Board | Pontual | Presencial + PDF | Consultoria | PPTX + PDF |

---

## 4. REGISTRO DE RISCOS

| # | Risco | Categoria | Prob | Impacto | Score | Resposta | Mitigação | Responsável | Status |
|---|---|---|---|---|---|---|---|---|---|
| R01 | | Técnico | | | | Mitigar | | | Aberto |
| R02 | | Recursos | | | | Aceitar | | | Aberto |
| R03 | | Cronograma | | | | Contingenciar | | | Aberto |

**Prob/Impacto:** A = Alto (3), M = Médio (2), B = Baixo (1)
**Score:** A×A=🔴 9, A×M=🔴 6, M×M=🟡 4, A×B=🟡 3, M×B=🟢 2, B×B=🟢 1

---

## 5. REGISTRO DE DECISÕES (Decision Log)

| # | Data | Decisão Tomada | Alternativas Consideradas | Decisor | Impacto no Projeto |
|---|---|---|---|---|---|
| D01 | | | | | |
| D02 | | | | | |

---

## 6. CHANGE REQUEST (Solicitação de Mudança)

```
SOLICITAÇÃO DE MUDANÇA — CHANGE REQUEST
─────────────────────────────────────────
CR #    : CR-[NNN]
Projeto : [nome do projeto]
Data    : ___/___/______
Solicitante: [nome]

DESCRIÇÃO DA MUDANÇA SOLICITADA:
[Descrever claramente o que precisa mudar]

JUSTIFICATIVA:
[Por que essa mudança é necessária?]

IMPACTO PREVISTO:
□ Escopo:     [aumenta / reduz / não afeta]
□ Prazo:      [atraso de ___ dias / não afeta]
□ Orçamento:  [aumento de R$ ___ / não afeta]
□ Qualidade:  [melhora / piora / não afeta]
□ Recursos:   [adiciona ___ horas / não afeta]

DECISÃO:
□ APROVADO   □ REJEITADO   □ PENDENTE

Aprovado por: _____________________  Data: ___/___/______
─────────────────────────────────────────
```

---

## 7. ATA DE REUNIÃO (PADRÃO PMO)

```
ATA DE REUNIÃO
─────────────────────────────────────────
Projeto   : [nome]
Reunião   : [tipo: operacional / comitê / kick-off / encerramento]
Data      : ___/___/______  Horário: ___h às ___h
Local     : [local ou link]
Facilitador: [nome]

PARTICIPANTES:
□ [Nome] — [Cargo/Papel]
□ [Nome] — [Cargo/Papel]
Ausentes justificados: [nomes]

PAUTA:
1. [item 1]
2. [item 2]
3. [item 3]

DISCUSSÕES E DECISÕES:
1. [item] → Decisão: [decisão tomada]
2. [item] → Decisão: [decisão tomada]

PRÓXIMOS PASSOS / AÇÕES:
┌────────────────────────────────┬──────────────────┬──────────────┐
│ Ação                           │ Responsável      │ Prazo        │
├────────────────────────────────┼──────────────────┼──────────────┤
│                                │                  │              │
│                                │                  │              │
└────────────────────────────────┴──────────────────┴──────────────┘

PRÓXIMA REUNIÃO: ___/___/______ às ___h
Ata enviada por: ______________ em ___/___/______
─────────────────────────────────────────
```
