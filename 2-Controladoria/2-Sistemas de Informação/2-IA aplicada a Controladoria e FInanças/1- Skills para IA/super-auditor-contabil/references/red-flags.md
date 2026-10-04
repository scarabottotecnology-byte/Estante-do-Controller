# 🚨 RED FLAGS — Padrões de Fraude e Manipulação Contábil

## Manipulação de Resultado

| Padrão | Sinal | Verificação |
|---|---|---|
| Channel stuffing | Pico de receita no último dia/semana do mês/trimestre | Comparar receita diária vs média mensal |
| Diferimento de despesa | CAPEX crescente sem expansão de ativo real | Cruzar CAPEX com adições no imobilizado |
| Aceleração de receita | Receita reconhecida antes da entrega | Verificar competência vs nota fiscal |
| Cookie jar reserves | Provisões excessivas em anos bons, revertidas em anos ruins | Analisar padrão de provisões e reversões |
| Despesa em off-balance | Leasing operacional tratado como financeiro (ou vice-versa) | Verificar classificação vs IFRS 16 / CPC 06 |

## Duplicidades e Fantasmas

| Padrão | Sinal | Verificação |
|---|---|---|
| Lançamento duplicado | Mesmo valor + data + fornecedor em linhas diferentes | NI-007 automático |
| Fornecedor fantasma | Fornecedor sem CNPJ válido ou com CNPJ de empresa baixada | Cruzar CNPJ no cadastro |
| NF inválida | Número de NF fora da sequência ou reaproveitado | Verificar chave de acesso NF-e |
| Split de transação | Transação grande dividida em várias menores para evitar aprovação | Agrupar por fornecedor + período |

## Distorções de Classificação

| Padrão | Sinal | Verificação |
|---|---|---|
| CAPEX como OPEX | Ativo permanente lançado como despesa do período | Itens > R$ 5.000 com vida útil > 1 ano |
| Custo pessoal em CAPEX | Salário de funcionários ativado indevidamente | Verificar se obra/projeto justifica |
| Despesa antecipada vs corrente | Pagamento de serviço futuro lançado no mês errado | Competência vs caixa |
| Mútuo disfarçado | Adiantamento a fornecedor que nunca é quitado | Aging de fornecedores |

## Sinais de Alerta Fiscal

| Padrão | Sinal | Verificação |
|---|---|---|
| Alíquota reduzida indevida | Imposto calculado abaixo do mínimo legal | Cruzar com tabela de alíquotas |
| Base de cálculo reduzida | Deduções não permitidas pelo regime | Verificar regime: Simples, LP, LR |
| Crédito de PIS/COFINS indevido | Crédito em despesas não geradoras de crédito (regime cumulativo) | CF-004 automático |
| ICMS em operação isenta | Imposto lançado em operação com isenção | Verificar CFOP |
| Diferimento sem lastro | Receita diferida sem contrato ou obrigação correspondente | Cruzar com passivo de contrato |
