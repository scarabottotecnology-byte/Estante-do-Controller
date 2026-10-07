# Playbooks por tema — quando não há skill dedicada

Use estes playbooks para os temas da Estante que **não** têm skill própria. Cada um traz: quando usar, perguntas que mudam a resposta, método, checagens, fontes da Estante (veja `mapa-da-estante.md`) e entregável.

**Regras comuns:**
- Separe `DADO`, `PREMISSA`, `CÁLCULO` e `HIPÓTESE`.
- Cite a fonte da Estante com o caminho do arquivo. Se não houver fonte, diga e use `lacunas-da-estante.md`.
- Não afirme alíquota, prazo ou limite legal de memória. Marque `VERIFICAR VIGÊNCIA`.
- Se um tema tiver skill especializada, **acione a skill** em vez de usar o playbook.

---

## Índice rápido

1. Qual CPC para qual pergunta
2. Valuation (fluxo de caixa descontado e múltiplos)
3. Custo de capital e estrutura de capital
4. Orçamento de capital (VPL, TIR, payback)
5. Fluxo de caixa e capital de giro
6. Controles internos e gestão de riscos
7. Auditoria interna baseada em riscos
8. Perícia contábil e apuração de haveres
9. Tributação e reforma tributária
10. Performance: KPIs, BSC, ROIC e EVA
11. M&A e due diligence financeira
12. Análise de demonstrações e balanços
13. Contabilidade societária e demonstrações obrigatórias
14. Segurança da informação e LGPD
15. Pesquisa e metodologia
16. Liderança, gestão de pessoas e carreira do Controller
17. Ensino e plano de estudos

---

## 1. Qual CPC para qual pergunta

Os PDFs estão em `10-Normas/2-CPC/`. A tabela usa os títulos dos arquivos da Estante. Para itens específicos, abra o PDF (os itens já conferidos para auditoria estão em `super-auditor-contabil/references/normas-contabeis.md` e para custos em `especialista-custos/references/normas-e-fontes-custos.md`).

| Pergunta | CPC (arquivo da Estante) |
|---|---|
| Estrutura conceitual, qualidade da informação | CPC 00 |
| Como apresentar balanço, DRE e notas; materialidade; compensação | CPC 26 (e CPC 51 para apresentação e divulgação) |
| Fluxo de caixa | CPC 03 |
| Políticas, estimativas e correção de erro | CPC 23 |
| Evento após o fim do período | CPC 24 |
| Provisões, passivos e ativos contingentes | CPC 25 |
| Receita de contrato com cliente | CPC 47 |
| Instrumentos financeiros, perdas de crédito, hedge | CPC 48 (apresentação: CPC 39; evidenciação: CPC 40) |
| Imobilizado, intangível, propriedade para investimento | CPC 27, CPC 04, CPC 28 |
| Redução ao valor recuperável | CPC 01 |
| Estoques | CPC 16 |
| Arrendamentos | CPC 06 |
| Tributos sobre o lucro (imposto diferido) | CPC 32 |
| Benefícios a empregados | CPC 33 (planos de aposentadoria: CPC 49) |
| Combinação de negócios | CPC 15 |
| Demonstrações consolidadas e separadas; coligadas; negócios em conjunto | CPC 36, CPC 35, CPC 18, CPC 19, CPC 45 |
| Valor justo | CPC 46 |
| Ajuste a valor presente | CPC 12 |
| Câmbio e conversão | CPC 02 |
| Subvenções governamentais | CPC 07 |
| Custos de empréstimos | CPC 20 |
| Partes relacionadas | CPC 05 |
| Informações por segmento; resultado por ação; demonstração intermediária | CPC 22, CPC 41, CPC 21 |
| DVA | CPC 09 |
| Pequenas e médias empresas | CPC PME |
| Adoção inicial | CPC 37 e CPC 43 |
| Setor público | MCASP 2025 (`10-Normas/6-Outros Reguladores`) |
| Todas as normas do CFC (NBC TG) em um arquivo | `10-Normas/1-CFC/NBC TG - Normas Completas (2018)` |

**Cuidado:** os pronunciamentos têm revisões. Confirme a versão vigente antes de afirmar um requisito em laudo ou parecer.

---

## 2. Valuation (fluxo de caixa descontado e múltiplos)

**Quando:** avaliar empresa, projeto, unidade ou participação.

**Perguntas que mudam a resposta:** propósito (compra, venda, laudo, gestão); data-base; horizonte; moeda; dados disponíveis; existência de projeções.

**Método:**
1. Defina o objeto e o propósito.
2. Normalize o histórico (itens não recorrentes, partes relacionadas).
3. Projete receita, margem, investimento e capital de giro por drivers, com cenários.
4. Calcule o fluxo livre (da firma ou do acionista) de forma coerente com a taxa.
5. Estime a taxa de desconto (veja o playbook 3) e o valor residual com critério explícito.
6. Some o valor presente, ajuste para dívida líquida e outros itens, e obtenha o valor do patrimônio.
7. Teste com múltiplos de mercado (comparáveis) e explique as diferenças.
8. Faça sensibilidade da taxa e do crescimento na perpetuidade.

**Checagens:** taxa e fluxo na mesma base (nominal ou real; antes ou depois da dívida); valor residual não pode ser a maior parte do valor sem justificativa; crescimento perpétuo coerente com a economia; consistência entre investimento e crescimento.

**Fontes da Estante:** `4-Finanças Corporativas/1-Valuation` (Avaliação de Empresas e Projetos da FGV; metodologias de avaliação; VPL e TIR; manual de Finanças Corporativas e Valor); `4-Finanças Corporativas/2-WACC`; `6-Performance/3-ROIC` e `4-EVA` (notas de Damodaran). Cursos nos favoritos: Damodaran (Corporate Finance e Valuation).

**Entregável:** memorando de valor com faixa, premissas críticas, sensibilidade e limites.

---

## 3. Custo de capital e estrutura de capital

**Método:** custo do capital próprio (modelo de precificação de ativos ou outro critério declarado); custo da dívida após impostos; pesos de mercado ou meta; WACC; para empresas fechadas, discutir ajustes de liquidez e tamanho como premissas.

**Checagens:** beta e taxa livre de risco na mesma moeda e horizonte; estrutura-alvo versus atual; efeito fiscal da dívida (verifique a vigência da regra de dedução); trade-off entre alavancagem e risco.

**Fontes:** artigos brasileiros de custo de capital em `11-Pesquisa & Referencia/1-Artigos`; `4-Estrutura de Capital` (3 documentos); slides de Risco e Retorno em `2-WACC`.

**Entregável:** tabela de WACC com cada insumo, fonte e data, mais sensibilidade.

---

## 4. Orçamento de capital (VPL, TIR, payback)

**Método:** fluxo incremental; VPL à taxa de custo de capital; TIR com checagem de fluxos não convencionais (pode haver mais de uma TIR); payback simples e descontado como medidas de risco, não de valor; análise de cenários; opções reais quando houver flexibilidade.

**Checagens:** capital de giro incluído; custos perdidos fora; efeitos fiscais; projetos mutuamente exclusivos de vida diferente exigem padronização; racionamento de capital.

**Fontes:** `4-Valuation` (Vantagens e desvantagens do VPL e da TIR); artigo de práticas de orçamento de capital em `1-Artigos`.

**Entregável:** quadro de decisão com VPL, TIR, payback, risco e recomendação.

---

## 5. Fluxo de caixa e capital de giro

**Método:** fluxo direto para gestão de caixa e indireto para conciliar com o resultado; necessidade de capital de giro (NCG) e ciclo financeiro (prazos de recebimento, estoque e pagamento); projeção semanal e mensal; reserva mínima; covenants e linhas disponíveis.

**Checagens:** conversão resultado para caixa; sazonalidade; concentração de clientes; recebíveis vencidos; impostos e dividendos; fechamento do saldo com extrato.

**Fontes:** `4-Fluxo de Caixa` (e-book do curso); `5-Capital de Giro` (E-book Gestão Financeira; guia do Sebrae); CPC 03; teses de DFC em `3-Dissertações`.

**Entregável:** projeção de caixa em 13 semanas ou 12 meses, com gatilhos de alerta.

---

## 6. Controles internos e gestão de riscos

**Método:** identificar processos críticos e riscos; avaliar probabilidade e impacto; mapear controles existentes (preventivos, detectivos); definir risco residual; priorizar respostas (evitar, reduzir, transferir, aceitar); responsável, prazo e indicador; monitorar.

**Checagens:** segregação de funções; controles sobre dados e sistemas; evidência de operação do controle; riscos de fraude e de conformidade; apetite a risco definido.

**Fontes:** `7-Auditoria/3-Controles Internos` (Manual de Integridade, Riscos e Controles Internos da Gestão, do MP); `2-Auditoria Interna` (Plano Anual de Auditoria Baseado em Riscos; Compliance Descomplicado); alavancas de controle de Simons em `2-Controladoria/3-Controles Gerenciais` e `4-Management Control`. Cursos de riscos da Enap nos favoritos. **Lacuna:** a subpasta `4-Riscos` está vazia.

**Skills relacionadas:** `super-auditor-contabil` (testes sobre base), `pmo-controladoria` (registro de riscos de projeto).

**Entregável:** matriz de riscos e controles, plano de resposta.

---

## 7. Auditoria interna baseada em riscos

**Método:** universo de auditoria; avaliação de risco por entidade e processo; plano anual priorizado; programa de trabalho por auditoria; testes (indagação, observação, inspeção, reexecução, análise de dados); achados com condição, critério, causa e efeito; recomendações; acompanhamento.

**Checagens:** independência; evidência suficiente; materialidade; falso positivo; comunicação com o auditado antes do relatório.

**Fontes:** Plano Anual de Auditoria Baseado em Riscos e Compliance Descomplicado (`7-Auditoria/2-Auditoria Interna`); apostila de auditoria contábil (`1-Auditoria Independente`).

**Skill:** `super-auditor-contabil` para executar testes na base.

**Entregável:** plano anual, programa de auditoria e relatório.

---

## 8. Perícia contábil e apuração de haveres

**Método:** nomeação e escopo; quesitos; diligências e documentos; metodologia (balanço de determinação, fluxo de caixa descontado, valor patrimonial a preços de mercado, conforme o contrato e a decisão); laudo com fundamentação; resposta a quesitos e a assistentes técnicos.

**Checagens:** data-base; critério definido no contrato ou na decisão; tratamento de intangíveis e contingências; coerência com as normas técnicas de perícia.

**Fontes:** `8-Pericias/1-Perícia Contábil` (Auditoria e Perícia Contábil; manuais do CRCRS e do CRC-BA); `3-Apuração de Haveres` (estudo de caso da UFSC). **Lacunas:** laudos-modelo, quesitos, jurisprudência.

**Limite:** o plano de provas e conclusões periciais exigem profissional habilitado e responsabilidade técnica. A skill apoia a estrutura e a análise.

**Entregável:** estrutura de laudo, plano de trabalho pericial, memória de cálculo.

---

## 9. Tributação e reforma tributária

**Método:** identificar regime (Simples, Lucro Presumido, Lucro Real), atividade, estados e municípios; mapear tributos por operação; checar créditos e retenções; separar planejamento (legal) de elisão abusiva; documentar a base legal.

**Reforma do consumo (fatos verificados na Estante):**
- A EC 132/2023 e a LC 214/2025 instituem IBS, CBS e Imposto Seletivo.
- O guia do CRCSP descreve transição entre 2026 e 2032 e vigência integral do novo modelo a partir de 2033.
- A EC 132 prevê a extinção do ICMS e do ISS a partir de 2033 (arts. 128 e 129).
- A LC 214 traz regras de transição para a CBS e o IBS (o texto cita, por exemplo, os arts. 353 a 369; confira a redação na norma).
- Conferir sempre a redação vigente, regulamentos e alterações posteriores.

**Checagens:** vigência; jurisdição; efeito em preço, margem, contrato e sistema; tratamento contábil (guia do CRCSP).

**Fontes da Estante:** `9-Tributario/1-Tributação` (CF, CTN, RIR, Leis 9.430, 12.973, 10.637, 10.833, LCs 116, 87, 123); `2-Planejamento Tributário`; `3-Reforma Tributária`; working papers em `11-Pesquisa & Referencia/4-Working Papers`.

**Skills relacionadas:** `mestre-projecao-financeira` (enquadramento e alerta), `especialista-fopag` (encargos).

**Alertas:** não apresente planejamento tributário como certeza jurídica; recomende validação por profissional habilitado. Alíquotas e prazos: `VERIFICAR VIGÊNCIA`.

**Entregável:** mapa de tributos por operação, cenário de transição, lista de pontos a validar.

---

## 10. Performance: KPIs, BSC, ROIC e EVA

**Método:** partir da estratégia; escolher poucos indicadores por perspectiva; definir fórmula, fonte, frequência, meta e responsável; ligar indicadores por causa e efeito (mapa estratégico); calcular ROIC e comparar com o custo de capital; EVA como resultado após o custo do capital investido.

**Checagens:** indicador sem dono não entra; meta com base histórica ou de mercado; efeito colateral perverso; indicadores de resultado e de direcionador.

**Fontes:** `6-Performance` (Guia Referencial de Indicadores; BSC Módulo 3; ROIC; EVA e CFROI). Livros: Kaplan e Norton, Stewart (lista de leitura).

**Skill relacionada:** `agente-financeiro` (KPIs obrigatórios).

**Entregável:** painel de indicadores com definições e metas.

---

## 11. M&A e due diligence financeira

**Método:** tese; escopo; análise de qualidade do resultado (normalização do EBITDA); capital de giro normalizado; dívida líquida e itens semelhantes à dívida; contingências; contratos e clientes; projeção; valuation; estrutura (preço, ajustes, earn-out); integração.

**Fontes:** `4-Finanças Corporativas/6-M&A` (Fusões e Aquisições de Empresas); CPC 15 e CPC 36; `Kuwabara` em `1-Contabilidade/2-Contabilidade Societaria`.

**Skills relacionadas:** `mestre-modelagem-financeira`, `super-auditor-contabil`, `business-strategist-master`.

**Entregável:** relatório de achados de due diligence, ponte de valor (preço, ajustes).

---

## 12. Análise de demonstrações e balanços

**Método:** padronizar demonstrações; análise horizontal e vertical; indicadores de liquidez, estrutura de capital, rentabilidade e atividade; decomposição da rentabilidade (margem, giro, alavancagem); fluxo de caixa; qualidade do lucro; comparação com pares e histórico.

**Checagens:** período e unidade; itens não recorrentes; efeitos de práticas contábeis diferentes.

**Fontes:** `1-Contabilidade/5-Analise das demonstrações` (Princípios de Análise de Balanço); `4-Demonstrações Financeiras` (DELPA, DMPL, DVA, DFC, DRA); CPC 26.

**Entregável:** relatório de diagnóstico econômico-financeiro.

---

## 13. Contabilidade societária e demonstrações obrigatórias

**Método:** identificar o tipo de entidade e o conjunto de normas (Lei das S.A., CPC completo ou CPC PME); levantar demonstrações obrigatórias, notas e divulgações; operações societárias (incorporação, fusão, cisão) e seus efeitos.

**Fontes:** `1-Contabilidade/2-Contabilidade Societaria` (Lei 6.404/1976; Lei 11.638/2007; livro didático de contabilidade societária; Kuwabara); CPC 26, CPC PME; `10-Normas/1-CFC`.

**Entregável:** lista de demonstrações e divulgações aplicáveis, tratamento de uma operação societária.

---

## 14. Segurança da informação e LGPD

**Método:** mapa de dados pessoais; base legal por tratamento; direitos do titular; medidas técnicas e administrativas; incidentes; contratos com operadores; registro das operações; governança.

**Fontes:** `2-Controladoria/2-Sistemas de Informação/1-Segurança de Dados` (Segurança da Informação: Gestão e Governança com conformidade à LGPD; Guia Orientativo da ANPD). **Lacuna:** o texto da Lei 13.709/2018 não está na pasta.

**Limite:** orientação geral; para parecer jurídico, consulte advogado.

**Entregável:** inventário de dados, matriz de riscos e plano de adequação.

---

## 15. Pesquisa e metodologia

**Método:** pergunta de pesquisa; revisão de literatura; hipóteses; delineamento; amostra; coleta; análise; limitações; ética. Para artigos, teses e dissertações, ler problema, método, resultado e limitação.

**Fontes:** `11-Pesquisa & Referencia` (artigos, teses, dissertações, working papers, e `5-Metodologia`).

**Entregável:** protocolo de pesquisa, fichamento, resumo crítico.

---

## 16. Liderança, gestão de pessoas e carreira do Controller

**Método:** diagnóstico do contexto da equipe; clareza de papéis e metas; feedback contínuo; delegação; reuniões e ritos; desenvolvimento e sucessão; comunicação com a diretoria; gestão de conflitos; carreira (competências técnicas, de liderança e de negócio).

**Fontes:** `12-Liderança e Gestão` (Liderança e Gestão de Equipes; Competências de liderança; Gestão de Equipes em Trabalho Remoto; Gestão por Competências). Cursos nos favoritos e leituras da lista (Grove, Lencioni, entre outros). **Lacunas:** inteligência emocional e carreira.

**Entregável:** plano de desenvolvimento, roteiro de conversa, rotina de gestão.

---

## 17. Ensino e plano de estudos

**Método:** diagnosticar o nível; ensinar em camadas (conceito, método, aplicação); usar a Estante como fonte; criar exercícios com gabarito; ligar o estudo ao checklist de hard skills.

**Skill relacionada:** `professor-controladoria` (didática e doutrinadores).

**Ferramentas:** checklist de 51 hard skills no artefato; favoritos de cursos; plano de 12 semanas no ClickUp.

**Entregável:** aula, resumo, lista de exercícios ou plano semanal.
