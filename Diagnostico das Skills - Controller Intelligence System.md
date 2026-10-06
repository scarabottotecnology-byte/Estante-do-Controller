# Diagnóstico das Skills — Controller Intelligence System

Data: 06/10/2026. Etapa 1 do agente Controller Skill Architect: **diagnóstico, sem modificar nenhuma skill**.

## Como esta análise foi feita (e seus limites)

- Li o frontmatter, a estrutura de títulos, o tamanho de cada seção e os arquivos de referência das 19 skills da pasta `2-Controladoria/.../1- Skills para IA`.
- Medi sinais objetivos por skill: menções a premissas, validação, rastreabilidade, normas (CPC/NBC/IFRS), WACC/CAPM, COSO, reforma tributária, ABC e cenários.
- Li por inteiro as seções-chave das skills centrais (Jefferson, Crimson, índice de doutrinadores). Nas demais li o esqueleto, não cada linha.
- **Não executei as skills com dados reais.** Os níveis abaixo medem o que o texto da skill permite que ela faça, não o resultado comprovado. Só `fpa-estruturador` tem casos de teste (`test_cases.json`).
- Cruzei com o acervo da Estante: 174 documentos catalogados, incluindo 47 pronunciamentos CPC, leis, apostilas, teses e artigos.

---

## 1. Inventário das skills

| # | Skill | Objetivo | Categoria | Função | Nível | Potencial |
|---|---|---|---|---|:-:|:-:|
| 1 | skill-controller-jefferson-scarabotto | Orquestrador geral com 34 "especialistas" | Controladoria, Tecnologia, IA | Roteador | 2 | 4 |
| 2 | skill-controller-estrategico (Inteligência Crimson) | Fechamento: DRE, orçado × realizado × forecast, DFC direto, balanço gerencial, prévia executiva | Controladoria, FP&A | Executora | 3 | 4 |
| 3 | agente-financeiro | CFO estratégico com 10 especialistas internos e saída padronizada | Finanças, FP&A, Estratégia | Consultiva | 3 | 5 |
| 4 | mestre-modelagem-financeira | Pipeline A/B até DRE+DFC+BP integrados, sensibilidade e valuation simplificado | Finanças, FP&A | Orquestradora | 3 | 4 |
| 5 | mestre-projecao-financeira | Projeção em 9 fases, 3 cenários, enquadramento tributário e alerta de reforma | FP&A, Tributário | Executora | 3 | 4 |
| 6 | fpa-estruturador | Padroniza base financeira em colunas fixas, com matriz de centros de custo | Dados, FP&A | Executora | 2 | 3 |
| 7 | mago-financeiro | Concilia e classifica lançamentos (plano de contas e centro de custo) | Contabilidade, Dados | Executora | 2 | 3 |
| 8 | super-auditor-contabil | Varredura de não conformidades, scoring e checklist de liberação | Auditoria | Executora/auditora | 3 | 5 |
| 9 | especialista-custos | Custos em 9 etapas: custeio, rateio, indicadores, simulações | Custos, Pricing | Executora | 3 | 4 |
| 10 | especialista-fopag | Folha, encargos, provisões, CTMO, rescisões, budget de pessoal | Custos, Contabilidade | Executora | 3 | 4 |
| 11 | especialista-faturamento | Conciliação de NFs, receita por canal, recebíveis, aging | Contabilidade, FP&A | Executora | 2 | 4 |
| 12 | relatorio-financeiro-executivo | Relatório HTML/PPTX/XLSX/DOCX de alto padrão visual | Controladoria | Entregável | 2 | 3 |
| 13 | engenheiro-dados-financeiros | ETL em 7 fases, SQL, Python, dashboards HTML | Dados, Tecnologia | Executora | 3 | 4 |
| 14 | especialista-apis-publicas | Escolhe e integra APIs públicas | Dados, Tecnologia | Consulta | 1 | 2 |
| 15 | dev-specialist | Regras de desenvolvimento (React, Supabase) com preservação do sistema | Tecnologia | Executora | 3 | 3 |
| 16 | diretor-comercial-marketing | Precificação, pesquisa de mercado, funil comercial | Pricing, Estratégia | Consultiva | 3 | 3 |
| 17 | pmo-controladoria | Projetos, processos, RACI, ADKAR, integração Asana/ClickUp | Estratégia, Governança | Consultiva | 3 | 4 |
| 18 | professor-controladoria | Ensina controladoria em 3 camadas ancorado em doutrinadores | Controladoria, IA | Didática | 3 | 4 |
| 19 | business-strategist-master | Ideia → Business Plan em 2 fases com gate de aprovação | Estratégia, Finanças | Consultiva | 4 | 5 |

### Por que cada nota

- **1 — Jefferson (nível 2):** a skill tem regras boas (nunca inventar números, separar dado confirmado, inferência, hipótese e recomendação, "quando perguntar", validação final). Mas os 34 "especialistas" têm entre 160 e 450 caracteres cada: são listas de responsabilidades, sem método. Por exemplo, "Gestão de Riscos" tem 163 caracteres. Ela duplica, em versão rasa, skills que já existem em profundidade.
- **2 — Crimson (nível 3):** tem fluxo completo (objetivo, diagnóstico da base, regime, classificação, DRE, orçado × realizado, drivers, DFC, balanço, auditoria, prévia executiva, qualidade do fechamento) e regra de no máximo 3 perguntas. Sobrepõe `mestre-modelagem` e `agente-financeiro`.
- **3 — agente-financeiro (nível 3):** estrutura de saída obrigatória (visão executiva, análise, riscos, oportunidades, plano, PMO) e bloco "dados necessários". Falta validação explícita (0 menções) e base técnica de normas.
- **4 e 5 — modelagem e projeção (nível 3):** são as mais metodológicas. `mestre-projecao` tem 10 menções a premissas, 14 a cenários e 12 à reforma tributária. `mestre-modelagem` tem mapa de integridade entre demonstrativos.
- **8 — super-auditor (nível 3):** scoring, relatório de não conformidades em .xlsx e checklist de liberação. Audita lançamentos e relatórios, não faz auditoria interna baseada em riscos.
- **9 — custos (nível 3):** 9 etapas e três arquivos de referência (métodos de custeio, rateio, fórmulas). ABC é citado, mas sem método de TDABC, custo padrão e variações.
- **10 — fopag (nível 3):** profundo no domínio (encargos, provisões, rescisões), mas com **zero menções a validação** e dependente de regras que mudam.
- **19 — business-strategist (nível 4):** única com gate de aprovação explícito e regra de rastreabilidade ("nunca misture fato com hipótese"), com 16 menções a premissas.
- **14 — APIs públicas (nível 1):** 50 linhas, útil como consulta, sem workflow.

---

## 2. Diagnóstico por critério (A–L), visão consolidada

| Critério | Pontos fortes | Pontos fracos |
|---|---|---|
| A. Papel | Quase todas têm papel claro | Jefferson e Crimson se sobrepõem como "controller geral" |
| B. Escopo | Bom nas especializadas | Poucas dizem o que **não** fazem |
| C. Conhecimento | Custos, fopag, projeção tributária | Normas (CPC/NBC/IFRS) quase ausentes; WACC só em `mestre-modelagem`; COSO em nenhuma |
| D. Raciocínio | Projeção, estratégia, agente-financeiro | Os 34 especialistas do Jefferson não têm método |
| E. Processo | Fluxos numerados na maioria | Poucos pontos de parada obrigatórios |
| F. Dados incompletos | Crimson (≤ 3 perguntas), agente-financeiro (dados necessários) | Faturamento e relatório assumem dados prontos |
| G. Validação | Auditor, dev, Jefferson (15 menções) | fopag, relatório, agente-financeiro e professor: 0 |
| H. Governança | Jefferson, mago, estratégico | Rastreabilidade de fonte irregular |
| I. Output | Estrutura de saída obrigatória em vários | Entregáveis de decisão (memorando, recomendação com alternativas) são raros |
| J. Exceções | Auditor (red flags) | Mudanças legais e casos fora do padrão quase não tratados |
| K. Decisão | agente-financeiro, business-strategist | Skills operacionais param na análise |
| L. Execução | PMO, faturamento (scripts) | Poucas fecham em plano de ação com dono e prazo |

### Achados transversais

1. **Três "controllers gerais" concorrentes:** Jefferson, Crimson e agente-financeiro.
2. **Conhecimento de cliente dentro de skills genéricas:** matrizes e quirks do Grupo Oficial Farma em `fpa-estruturador`, `engenheiro-dados`, `faturamento`, `mestre-modelagem` e `pmo`. Isso limita o reuso e expõe dados de cliente quando o repositório é compartilhado.
3. **Validação desigual** (veja a tabela acima).
4. **Lacuna de normas:** a Estante tem 47 pronunciamentos CPC, a Lei 6.404, a Lei 12.973, a EC 132 e a LC 214, mas as skills quase não os usam.
5. **Custo de contexto:** `diretor-comercial-marketing` tem 67 KB e 2.391 linhas, `skill-controller-jefferson` tem 1.382 linhas. Arquivos assim consomem contexto em toda ativação.
6. **Testes:** apenas uma skill (`fpa-estruturador`) tem casos de teste.

---

## 3. Mapa de lacunas

| Lacuna | Onde aparece | Gravidade |
|---|---|---|
| Normas contábeis (CPC/IFRS) como fonte | Todas as skills contábeis | Crítica |
| Valuation, custo de capital, ROIC/EVA | Só `mestre-modelagem` (superficial) | Crítica |
| Auditoria interna baseada em riscos, COSO, controles internos | `super-auditor` (parcial), `jefferson` (163 caracteres) | Crítica |
| Custo padrão, TDABC, gestão estratégica de custos | `especialista-custos` | Alta |
| Reforma tributária (IBS/CBS) além de um alerta | `mestre-projecao` | Alta |
| Orçamento e forecast com método (rolling, beyond budgeting) | `mestre-projecao`, `agente-financeiro` | Alta |
| Fluxo de caixa e capital de giro | Sem skill dedicada | Média |
| KPIs/BSC com método | `agente-financeiro` (KPIs) | Média |
| Testes e critérios de aceite por skill | 18 de 19 sem teste | Alta |
| Data quality como disciplina | `engenheiro-dados` (fase 5) | Média |

---

## 4. Matriz skill × conhecimento × Estante

| Skill | Lacuna | Fonte na Estante | Conhecimento a incorporar | Prioridade |
|---|---|---|---|---|
| super-auditor-contabil | Normas e auditoria baseada em risco | CPC 00, 23, 25, 26; Plano Anual de Auditoria Baseado em Riscos; Compliance Descomplicado; Manual de Gestão de Integridade, Riscos e Controles Internos (MP); apostila de Auditoria Contábil; Lei 6.404, Lei 12.973 | Regras de teste por conta com base no CPC; critério de materialidade; matriz de risco; evidência exigida por tipo de teste | **Crítica** |
| especialista-custos | TDABC, custo padrão, estratégia de custos | Contabilidade de Custos (apostilas e Claretiano); Custeio ABC; dissertação sobre gestão estratégica de custos; guias do Sebrae de preço e planejamento | Regras de escolha de método (quando ABC, quando variável); decomposição de margem por produto, canal e unidade; critérios de rateio e seu viés | **Crítica** |
| mestre-modelagem-financeira | Valuation e custo de capital | CPC 03, 26, 46; Avaliação de Empresas e Projetos (FGV); VPL e TIR; artigos brasileiros de custo de capital; slides de Risco e Retorno; notas de ROC/ROIC e EVA | Rotina de WACC com premissas rastreáveis; teste de coerência de fluxo de caixa; sensibilidade com intervalos | **Alta** |
| mestre-projecao-financeira | Orçamento, rolling forecast, tributos | 9 documentos de Budget; caso de rolling forecast; Analysis of Budget Performance; CPC 32; LC 214; EC 132; guia de contabilização CBS/IBS | Critério de escolha entre orçamento anual, rolling e beyond budgeting; checagem de enquadramento tributário; tratamento da transição | **Alta** |
| agente-financeiro | Validação e base técnica | Controladoria Estratégica Decisória; Guia de Indicadores; BSC; Alavancas de Controle de Simons | Mapa de causa e efeito dos KPIs; critérios de alerta; passos de validação antes da recomendação | **Alta** |
| skill-controller-jefferson | Substituir stubs por roteamento | Todas as skills especializadas | Tabela "pergunta → skill → entregável"; regras de escalonamento | **Crítica** |
| especialista-faturamento | Reconhecimento de receita e perdas | CPC 47, CPC 48, CPC 25 | Regras de corte de competência e PCLD; testes de reconciliação de receita | Média |
| especialista-fopag | Provisões e benefícios | CPC 25, CPC 33, CPC 32 | Provisão de férias, 13º e contingências sob CPC; validação de memória de cálculo | Média |
| professor-controladoria | Ancoragem em fontes | Livros da lista de leitura e documentos da Estante | Citação por documento da Estante, em vez de memória do modelo | Média |
| fpa-estruturador e mago-financeiro | Consolidação e matriz do cliente | Plano de contas e matrizes de centro de custo | Um modo único com a matriz carregada de arquivo do cliente | Média |
| relatorio-financeiro-executivo | Validação antes da entrega | Controladoria Estratégica Decisória; Guia de Indicadores | Checagem cruzada de totais e unidades; separar fato de interpretação | Média |
| engenheiro-dados-financeiros | Data quality formal | Segurança da Informação e LGPD (2 guias) | Dimensões de qualidade (completude, unicidade, consistência, validade); regras de LGPD em dados | Baixa |
| business-strategist-master | Valuation e M&A | Fusões e Aquisições; Avaliação de Empresas | Critérios de decisão no gate; escolha de método de avaliação | Baixa |
| pmo-controladoria | Governança e risco de projeto | Manual de Integridade, Riscos e Controles Internos | Registro de riscos alinhado a COSO | Baixa |
| diretor-comercial-marketing | Pricing com custo | Guias de preço do Sebrae; skill de custos | Piso de preço pela margem de contribuição | Baixa |

---

## 5. Skills redundantes e consolidações

Sem consolidar apenas para reduzir quantidade. As sugestões abaixo têm justificativa funcional.

| Redundância | Recomendação |
|---|---|
| Jefferson × Crimson × agente-financeiro (três controllers gerais) | **Jefferson vira o roteador único** ("Controller Master"). Remova os 34 stubs e aponte para a skill especializada. Crimson permanece como skill de **fechamento** e a agente-financeiro como **conselheira CFO**. |
| fpa-estruturador + mago-financeiro | Uma skill de **padronização e classificação** com dois modos. A matriz de centros de custo sai do texto da skill e vira arquivo de contexto do cliente. |
| especialista-apis-publicas → engenheiro-dados-financeiros | Incorporar como arquivo de referência de fontes externas. |
| Pricing no diretor-comercial × custos | Manter ambos, mas o preço-piso vem de `especialista-custos`. |
| Conhecimento do Grupo Oficial Farma em 5 skills | Criar **um** arquivo `contexto-oficial-farma` carregado só quando o cliente for esse. Mantém as skills genéricas. |
| dev-specialist | Não consolidar. Fica fora da arquitetura do controller, no eixo Tecnologia. |

---

## 6. Novas skills com justificativa funcional

| Nova skill | Justificativa | Fontes da Estante | Prioridade |
|---|---|---|---|
| **Normas Contábeis (CPC/IFRS)** | Hoje nenhuma skill consulta os 47 pronunciamentos. Seria a camada de conhecimento das demais. | CPC 00 a 48, Lei 6.404, Lei 11.638, Lei 12.973 | P1 |
| **Valuation e Alocação de Capital** | `mestre-modelagem` só faz valuation simplificado. Faltam WACC, DCF, VPL/TIR, ROIC e EVA com método. | Valuation (4 docs), WACC, ROIC, EVA | P1 |
| **Controles Internos e Riscos** | Hoje o auditor cobre lançamentos, não COSO nem auditoria baseada em risco. Alinha ao seu interesse de carreira. | Plano Anual de Auditoria, Compliance, Manual MP | P1 |
| **Tributário e Reforma Tributária** | Hoje é uma seção dentro de `mestre-projecao`. A reforma muda a transição até 2033. | EC 132, LC 214, 10 documentos de tributação | P1 |
| **Caixa e Capital de Giro (Treasury)** | Sem skill dedicada. Fluxo de caixa e capital de giro são rotina de controladoria. | Fluxo de Caixa, E-book Gestão Financeira | P2 |
| **Performance (KPIs e BSC)** | KPIs aparecem só como bloco em outras skills. | Guia de Indicadores, BSC, Simons | P2 |

Não sugeri "CFO Advisory", "Decision Intelligence" ou "Business Intelligence" como skills novas: já estão cobertas por `agente-financeiro`, `business-strategist-master` e `engenheiro-dados`. Criar outras seria categoria artificial.

---

## 7. Ranking de prioridade

| Prioridade | Skill | Nível | Potencial | Ganho esperado | Complexidade |
|---|---|:-:|:-:|---|---|
| **P0** | skill-controller-jefferson | 2 | 4 | Roteamento confiável e menos contexto gasto | Média |
| **P0** | super-auditor-contabil | 3 | 5 | Testes ancorados em CPC e em risco | Média |
| **P0** | especialista-custos | 3 | 4 | Método de decisão sobre custeio, ABC e margem | Média |
| **P1** | agente-financeiro | 3 | 5 | Validação e recomendação com alternativas | Média |
| **P1** | mestre-modelagem-financeira | 3 | 4 | WACC e valuation com premissas rastreáveis | Alta |
| **P1** | mestre-projecao-financeira | 3 | 4 | Reforma tributária e orçamento com método | Alta |
| **P1** | Normas Contábeis (nova) | — | 4 | Camada de conhecimento reutilizável | Média |
| **P1** | Controles Internos e Riscos (nova) | — | 4 | Alinha com carreira e preenche a lacuna de risco | Média |
| **P2** | fpa-estruturador + mago-financeiro | 2 | 3 | Reuso e menos manutenção | Baixa |
| **P2** | especialista-faturamento | 2 | 4 | Receita sob CPC 47 e PCLD | Média |
| **P2** | especialista-fopag | 3 | 4 | Validação e provisões sob CPC | Média |
| **P2** | professor-controladoria | 3 | 4 | Citação das fontes da Estante | Baixa |
| **P2** | Valuation e Alocação de Capital (nova) | — | 4 | Método dedicado | Alta |
| **P3** | relatorio-financeiro-executivo, engenheiro-dados, pmo, business-strategist | 2–4 | 3–5 | Ajustes finos | Baixa |
| **P3** | diretor-comercial, apis-publicas, dev-specialist | 1–3 | 2–3 | Reduzir tamanho, consolidar | Baixa |

---

## 8. Arquitetura futura (baseada nas skills reais)

```
CONTROLLER MASTER  (skill-controller-jefferson, só roteia)
│
├── CONTROLADORIA E FECHAMENTO
│     skill-controller-estrategico · relatorio-financeiro-executivo · especialista-faturamento
├── FP&A E PROJEÇÃO
│     mestre-projecao-financeira · mestre-modelagem-financeira · [Valuation e Alocação de Capital]
├── CUSTOS, PESSOAL E PRICING
│     especialista-custos · especialista-fopag · diretor-comercial-marketing (pricing)
├── AUDITORIA E GOVERNANÇA
│     super-auditor-contabil · [Controles Internos e Riscos] · [Normas Contábeis]
├── TRIBUTÁRIO
│     [Tributário e Reforma Tributária]
├── DADOS E AUTOMAÇÃO
│     fpa-estruturador + mago-financeiro (padronização) · engenheiro-dados-financeiros · especialista-apis-publicas · dev-specialist
├── ESTRATÉGIA E CONSELHO
│     agente-financeiro (CFO) · business-strategist-master · pmo-controladoria
└── ENSINO E CONHECIMENTO
      professor-controladoria  ←  Estante do Controller (fonte comum)
```

Itens entre colchetes são novos. O fluxo de dados existente permanece: `fpa-estruturador` → `mago-financeiro` → `super-auditor` → modelagem → relatório executivo.

---

## 9. Roadmap de evolução

| Fase | Foco | Entregas |
|---|---|---|
| **1. Fundamentos críticos** | Roteador e base normativa | Enxugar o Jefferson em roteador; criar a skill Normas Contábeis (CPC); separar `contexto-oficial-farma`; criar casos de teste para as skills P0 |
| **2. Especialização técnica** | Aprofundar P0 e P1 | Evoluir super-auditor, custos e modelagem com conhecimento da Estante; criar Controles Internos e Riscos |
| **3. Integração entre disciplinas** | Custo, preço, orçamento e tributo conversam | Preço-piso vindo de custos; projeção ligada a CPC 32 e à transição tributária; consolidar fpa-estruturador + mago |
| **4. Automação e inteligência** | Menos retrabalho | Testes automáticos por skill; rotinas de validação; ligar a Estante ao catálogo para citação com fonte |
| **5. Advisory / CFO** | Decisão e comunicação | Memorando de decisão com alternativas; agente-financeiro com validação completa; Valuation e Alocação de Capital |

A Fase 2 conversa com o seu plano de estudos: Gestão de Riscos (Enap), COSO e Valuation (Damodaran) alimentam diretamente as skills de Controles Internos e Valuation.

---

## 10. Plano de melhoria das skills P0

### skill-controller-jefferson-scarabotto (P0)

- **Skill atual:** roteador com 34 especialistas descritos em poucas linhas, 1.382 linhas no total.
- **Lacunas:** especialistas sem método; duplicam skills existentes; sem tabela de roteamento verificável.
- **Fontes:** as próprias skills especializadas e a seção "quando perguntar".
- **Novas regras:** (1) ao reconhecer um tema, chamar a skill especializada pelo nome; (2) só responder direto quando nenhuma skill cobrir o tema; (3) sempre separar dado, inferência, hipótese e recomendação (já existe); (4) pedir no máximo 3 informações por rodada (alinhado à Crimson).
- **Novo workflow:** input → classificar tema → escolher skill ou combinação → executar → validar contra a lista de qualidade → entregar com fontes.
- **Novos outputs:** resposta com "skill usada, premissas, riscos, próximos passos".
- **Nível esperado:** 4 (como roteador e governança).

### super-auditor-contabil (P0)

- **Skill atual:** varredura de não conformidades (numérica, classificação, fiscal, equação contábil, competência, consistência) com scoring e checklist de liberação.
- **Lacunas:** sem base normativa; sem materialidade; sem teste por risco; sem plano de evidências.
- **Fontes:** CPC 00, 23, 25, 26; Plano Anual de Auditoria Baseado em Riscos; Compliance Descomplicado; Manual MP de Riscos e Controles; apostila de Auditoria Contábil; Leis 6.404 e 12.973.
- **Novos conhecimentos → regras:** testes por conta ancorados em CPC (por exemplo, provisões sob CPC 25 e apresentação sob CPC 26); materialidade definida antes da varredura; evidência mínima por tipo de achado.
- **Novo workflow:** input → classificação → materialidade → varredura → scoring → validação → recomendação → plano de correção com dono e prazo.
- **Novos outputs:** relatório de achados com referência à norma, matriz de risco, plano de remediação.
- **Nível esperado:** 4.

### especialista-custos (P0)

- **Skill atual:** 9 etapas e três arquivos de referência (métodos, rateio, fórmulas).
- **Lacunas:** quando usar cada método; TDABC; custo padrão e variações; visão estratégica de custos; elo com preço.
- **Fontes:** Contabilidade de Custos (apostilas e Claretiano); Custeio ABC; dissertação de gestão estratégica de custos; guias do Sebrae de preço e planejamento.
- **Novos conhecimentos → regras:** transformar "margem de contribuição" em comportamento: decompor receita, custos variáveis e margem por produto, canal e unidade sempre que os dados permitirem; escolher o critério de rateio menos distorcivo e registrar a limitação; calcular o preço-piso a partir da margem de contribuição.
- **Novo workflow:** diagnóstico → método → cálculo → ranking de rentabilidade → simulação → recomendação → plano.
- **Novos outputs:** painel de rentabilidade por produto e canal, memória de rateio, simulação de preço-piso.
- **Nível esperado:** 4.

### Skills P1 (resumo)

- **agente-financeiro:** acrescentar etapa de validação (consistência dos dados, unidade, período, reconciliação) antes de recomendar; apresentar no mínimo duas alternativas e o impacto de cada. Nível 3 → 4.
- **mestre-modelagem-financeira:** rotina de WACC com premissas rastreáveis e sensibilidade com intervalos; CPC 03 e 26 como regra de integridade. Nível 3 → 4.
- **mestre-projecao-financeira:** critério para escolher orçamento anual, rolling ou beyond budgeting; checagem do enquadramento tributário com CPC 32 e o calendário da transição (EC 132, LC 214). Nível 3 → 4.

---

## Próximo passo sugerido

Escolher por qual P0 começar a evolução. Recomendo **`super-auditor-contabil`**: ele usa o que a Estante já tem de mais completo (CPC, auditoria e controles) e alimenta a skill de Controles Internos e Riscos, que combina com o seu plano de estudos.

Nada foi alterado nas skills. A etapa de evolução só começa depois da sua aprovação deste diagnóstico.
