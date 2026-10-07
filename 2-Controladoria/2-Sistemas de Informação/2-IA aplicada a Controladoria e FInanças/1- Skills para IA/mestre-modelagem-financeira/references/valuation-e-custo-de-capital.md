# Valuation e custo de capital — método, checagens e fontes

Uso: Etapa 4.6 do `mestre-modelagem-financeira`. É um guia de **método**. Os números dos exemplos são **fictícios e didáticos**; não são dados de mercado.

Valuation completo, laudo ou avaliação para transação exigem profissional habilitado e análise específica. Aqui o resultado é sempre uma **faixa** com premissas e sensibilidade.

---

## 1. Passo a passo do DCF simplificado

1. **Objeto e propósito:** o que se avalia (empresa, unidade, projeto), para quê e em que data-base.
2. **Normalizar o histórico:** itens não recorrentes, partes relacionadas, políticas contábeis (por exemplo, arrendamentos sob o CPC 06).
3. **Projetar** receita, margem, CAPEX e capital de giro (use `mestre-projecao-financeira`; aqui você integra).
4. **Fluxo livre da firma (FCFF):**
   `FCFF = EBIT × (1 − t) + D&A − CAPEX − Δ Necessidade de Capital de Giro`
5. **Taxa de desconto (k):** WACC calculado ou TMA informada (seção 2).
6. **Valor terminal:** `VT = FCFF_n × (1 + g) / (k − g)`, descontado ao presente: `VT / (1 + k)^n`.
7. **Valor da firma (EV):** soma dos valores presentes dos fluxos mais o valor terminal descontado.
8. **Ponte para o patrimônio:** `Equity = EV − dívida líquida − outros itens semelhantes à dívida` (arrendamentos, contingências prováveis, minoritários) `+` ativos não operacionais.
9. **Sensibilidade:** tabela de duas entradas (k × g) e destaque da participação do valor terminal.
10. **Conclusão em faixa**, com as premissas críticas e o que mudaria a conclusão.

## 2. Taxa de desconto

**WACC** = `E/(E+D) × Ke + D/(E+D) × Kd × (1 − t)`

| Insumo | Como obter | Cuidado |
|---|---|---|
| Ke (custo do capital próprio) | Modelo de precificação de ativos: `taxa livre de risco + beta × prêmio de risco`, ou critério declarado | Moeda e prazo da taxa livre de risco coerentes com o fluxo; beta alavancado para a estrutura-alvo; ajustes para empresa fechada (liquidez, tamanho) são **premissas** |
| Kd (custo da dívida) | Taxa efetiva de captação recente ou de mercado | Antes e depois do efeito fiscal; verificar vigência da dedutibilidade |
| Pesos E e D | Estrutura-alvo de capital, a valores de mercado quando possível | Não misture estrutura atual com estrutura-alvo sem dizer |
| t (alíquota) | Alíquota aplicável | `VERIFICAR VIGÊNCIA` |

**TMA (taxa mínima de atratividade)** é uma exigência do investidor ou da empresa, informada pelo usuário. **Não é WACC.** Se o usuário fornecer a TMA, use-a e rotule como tal; se for útil, mostre também o WACC calculado para comparar.

**Exemplo didático (valores fictícios):** taxa livre de risco 10%, beta 1,1, prêmio de risco 6% → Ke = 10% + 1,1 × 6% = 16,6%. Kd antes do imposto 14%, alíquota 34% → Kd = 9,24%. Pesos 60% e 40% → WACC = 0,6 × 16,6% + 0,4 × 9,24% = 13,656%.

## 3. Exemplo numérico de DCF (fictício)

- FCFF: ano 1 = 100; ano 2 = 110; ano 3 = 120.
- k = 12%; g = 3%; dívida líquida = 300.
- VP dos fluxos: 89,29 + 87,69 + 85,41 = **262,39**.
- Valor terminal no ano 3: 120 × 1,03 / (0,12 − 0,03) = **1.373,33**; descontado: 1.373,33 / 1,12³ = **977,51**.
- EV = 262,39 + 977,51 = **1.239,90**. Participação do valor terminal: **78,8%**.
- Equity = 1.239,90 − 300 = **939,90**.

**Sensibilidade (EV):**

| k \ g | 2% | 3% | 4% |
|---|---|---|---|
| 11% | n/c | 1.396,8 | n/c |
| 12% | 1.133,6 | 1.239,9 | 1.372,8 |
| 13% | n/c | 1.114,4 | n/c |

(n/c = não calculado neste exemplo.) Uma variação de um ponto percentual em k ou em g muda o valor de forma relevante, e o valor terminal domina o resultado: a conclusão deve ser dada em faixa.

## 4. Múltiplos

- `EV = métrica × múltiplo`; `Equity = EV − dívida líquida e itens semelhantes`.
- Defina a **métrica** (EBITDA reportado, ajustado, de 12 meses) e o **EV** do comparável da mesma forma que a empresa avaliada.
- Selecione comparáveis com critério explícito (atividade, porte, crescimento, geografia) e registre por que foram incluídos ou excluídos.
- Mostre mediana e dispersão, não só a média.
- **Sem fonte, sem múltiplo.** Não use faixa "setorial" de memória.

## 5. Checagens obrigatórias

- [ ] Fluxo e taxa na mesma base (nominal ou real; antes ou depois da dívida).
- [ ] g menor que k e compatível com o crescimento da economia na moeda do fluxo.
- [ ] Investimento coerente com o crescimento projetado (crescer exige CAPEX e capital de giro).
- [ ] Valor terminal descontado e sua participação informada.
- [ ] Ponte EV → Equity inclui arrendamentos e outros itens semelhantes à dívida na mesma definição de EBITDA e de dívida.
- [ ] Data-base e critério de desconto declarados.
- [ ] Sensibilidade apresentada e resultado em faixa.
- [ ] Premissas rotuladas; `VERIFICAR VIGÊNCIA` em alíquotas.

## 6. Fontes da Estante

- `4-Finanças Corporativas/1-Valuation`: Avaliação de Empresas e Projetos (FGV); metodologias de avaliação; VPL e TIR; Finanças Corporativas e Valor (manual).
- `4-Finanças Corporativas/2-WACC`: slides de Risco e Retorno.
- `4-Finanças Corporativas/4-Estrutura de Capital`.
- `6-Performance/3-ROIC` e `4-EVA`: notas de Damodaran.
- `11-Pesquisa & Referencia/1-Artigos`: artigos brasileiros de custo de capital.
- `10-Normas/2-CPC`: CPC 46 (valor justo), CPC 06 (arrendamentos), CPC 03 (DFC).
- Cursos nos favoritos: Damodaran (Corporate Finance e Valuation). Livros na lista de leitura: Damodaran (*Investment Valuation*), Copeland (*Valuation*), Rosenbaum e Pearl.
- **Lacuna:** não há ainda texto-base de Damodaran nem Copeland na pasta; veja `lacunas-da-estante.md` no Controller Master.
