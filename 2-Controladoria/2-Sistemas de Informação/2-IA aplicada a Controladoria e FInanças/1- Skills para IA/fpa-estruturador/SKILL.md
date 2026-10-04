---
name: fpa-estruturador
description: >
  Estrutura qualquer entrada financeira (DRE, FCF, extratos bancários, lançamentos avulsos)
  no modelo padronizado de 17 colunas da empresa, pronto para integração com Power BI.
  USAR SEMPRE que o usuário enviar uma mensagem iniciada com "tratar dados", ou quando
  mencionar DRE, fluxo de caixa, extrato, lançamentos financeiros e pedir estruturação,
  padronização ou exportação para BI. Também acionar quando o usuário quiser consolidar
  dados financeiros entre empresas ou centros de custo.
---

# FP&A Estruturador — Skill de Padronização Financeira

## Objetivo
Transformar qualquer entrada financeira bruta em uma tabela CSV padronizada com 17 colunas fixas, pronta para Power BI e consolidação corporativa.

---

## Colunas Obrigatórias (NUNCA alterar nomes)

```
CENTRO DE CUSTOS | CC - SINTÉTICO | CC REDUZIDO | P.C. SINTÉTICO | GRUPO |
EMPRESA | VALOR | MÊS DE PAGAMENTO | MÊS DE EMISSÃO | B.U. |
FASE DO NEGÓCIO | GESTOR DA AREA | DIRETOR DA AREA | OBSERVAÇÃO |
FONTE | STATUS | DATA
```

---

## Regras de Processamento

### 1. Formatação
- **VALOR**: sempre numérico com ponto decimal (ex: `-1500.00`). Sem R$, sem vírgula.
- **Datas** (DATA): formato `YYYY-MM-DD`
- **Meses** (MÊS DE PAGAMENTO, MÊS DE EMISSÃO): formato `YYYY-MM`
- Receitas: valor **positivo** | Custos e Despesas: valor **negativo**

### 2. GRUPO
| Valor | Quando usar |
|-------|-------------|
| Receita | Vendas, faturamento, recebimentos |
| Custo | CMV, produção, entrega, fabril |
| Despesa | Operacional, administrativo, comercial |
| Investimento | Capex, ativos, infraestrutura |

### 3. P.C. SINTÉTICO
Exemplos: `Receita Bruta`, `Deduções`, `CMV`, `Despesas Operacionais`, `Despesas Financeiras`, `Investimento`, `Impostos`

---

### 4. CENTRO DE CUSTOS — Matriz Oficial

Usar a tabela abaixo para preencher CENTRO DE CUSTOS (nome completo), CC - SINTÉTICO (sub-grupo pai) e CC REDUZIDO (código numérico).

> CCs marcados como INATIVAR ou inativo NAO recebem lancamentos — alertar e sugerir substituto ativo.
> CCs "Nao aceita lancamentos" sao agrupadores — usar o CC filho mais especifico.

**GRUPO 1 — Fabricas**

| CENTRO DE CUSTOS | CC - SINTÉTICO | CC REDUZIDO | B.U. | GESTOR |
|---|---|---|---|---|
| 1.1.1.1 Preparação | 1.1 Advanced | 1.1.1.1 | Farma | Lucas Caetano |
| 1.1.1.2.1 Pesagem 1 - Advanced | 1.1 Advanced | 1.1.1.2 | Farma | Lucas Caetano |
| 1.1.1.2.2 Pesagem 2 - Advanced | 1.1 Advanced | 1.1.1.2 | Farma | Lucas Caetano |
| 1.1.1.3 Homogenização - Advanced | 1.1 Advanced | 1.1.1.3 | Farma | Lucas Caetano |
| 1.1.1.4.1 Encapsuladora 1200 - Advanced | 1.1 Advanced | 1.1.1.4 | Farma | Lucas Caetano |
| 1.1.1.4.2 Encapsuladora 3200 - Advanced | 1.1 Advanced | 1.1.1.4 | Farma | Lucas Caetano |
| 1.1.1.4.3 Encapsuladora Semi Automática - Advanced | 1.1 Advanced | 1.1.1.4 | Farma | Lucas Caetano |
| 1.1.1.5 Compressora 1200 - Advanced | 1.1 Advanced | 1.1.1.5 | Farma | Lucas Caetano |
| 1.1.1.6.1 Envase CC180 K - Advanced | 1.1 Advanced | 1.1.1.6 | Farma | Lucas Caetano |
| 1.1.1.6.2 Envase CCACCM 8L - Advanced | 1.1 Advanced | 1.1.1.6 | Farma | Lucas Caetano |
| 1.1.1.6.3 Envase IQ66 - Advanced | 1.1 Advanced | 1.1.1.6 | Farma | Lucas Caetano |
| 1.1.1.7 Dosadora FLG 1000 - Advanced | 1.1 Advanced | 1.1.1.7 | Farma | Lucas Caetano |
| 1.1.1.8 Encaixotamento e Rotulagem - Advanced | 1.1 Advanced | 1.1.1.8 | Farma | Lucas Caetano |
| 1.1.1.9 Sachê - MASIPACK VS 300 - Advanced | 1.1 Advanced | 1.1.1.9 | Farma | Lucas Caetano |
| 1.1.2.1 Estoque - Advanced | 1.1 Advanced | 1.1.2.1 | Farma | Lucas Caetano |
| 1.1.2.2 PCP - Advanced | 1.1 Advanced | 1.1.2.2 | Farma | Lucas Caetano |
| 1.1.2.3 Manutenção de Equipamentos - Advanced | 1.1 Advanced | 1.1.2.3 | Farma | Lucas Caetano |
| 1.1.2.4 P & D - Advanced | 1.1 Advanced | 1.1.2.4 | Farma | Lucas Caetano |
| 1.1.2.7 Segurança - Advanced | 1.1 Advanced | 1.1.2.7 | Farma | Lucas Caetano |
| 1.1.3.1 Administrativo - Advanced | 1.1 Advanced | 1.1.3.1 | Farma | Lucas Caetano |
| 1.1.3.2 Áreas Comuns - Advanced | 1.1 Advanced | 1.1.3.2 | Farma | Lucas Caetano |
| 1.1.3.3 Estoque Extrema | 1.1 Advanced | 1.1.3.3 | Farma | — |
| 1.2.1.1 Preparação - São Roque | 1.2 São Roque | 1.2.1.1 | Farma | Lucas Caetano |
| 1.2.1.2.1 Pesagem 1 - São Roque | 1.2 São Roque | 1.2.1.2 | Farma | Lucas Caetano |
| 1.2.1.2.2 Pesagem 2 - São Roque | 1.2 São Roque | 1.2.1.2 | Farma | Lucas Caetano |
| 1.2.1.3 Homogenização - São Roque | 1.2 São Roque | 1.2.1.3 | Farma | Lucas Caetano |
| 1.2.1.4.1 Envase IQ66 - São Roque | 1.2 São Roque | 1.2.1.4 | Farma | Lucas Caetano |
| 1.2.1.4.2 Envase Manual - São Roque | 1.2 São Roque | 1.2.1.4 | Farma | Lucas Caetano |
| 1.2.1.5.1 Encapsuladora Manual - São Roque | 1.2 São Roque | 1.2.1.5 | Farma | Lucas Caetano |
| 1.2.1.5.2 Encapsuladora Semi-Automática - São Roque | 1.2 São Roque | 1.2.1.5 | Farma | Lucas Caetano |
| 1.2.1.6 Rotulagem - São Roque | 1.2 São Roque | 1.2.1.6 | Farma | Lucas Caetano |
| 1.2.1.7 Sachê - São Roque | 1.2 São Roque | 1.2.1.7 | Farma | Lucas Caetano |
| 1.2.1.8 Semi-Sólidos e Líquidos Manual (Derma) | 1.2 São Roque | 1.2.1.8 | Farma | Lucas Caetano |
| 1.2.2.1 Manutenção Geral | 1.2 São Roque | 1.2.2.1 | Farma | Lucas Caetano |
| 1.2.2.2 Estoque - São Roque | 1.2 São Roque | 1.2.2.2 | Farma | Lucas Caetano |
| 1.2.2.3 PCP - São Roque | 1.2 São Roque | 1.2.2.3 | Farma | Lucas Caetano |
| 1.2.2.4 Qualidade - São Roque | 1.2 São Roque | 1.2.2.4 | Farma | Lucas Caetano |
| 1.2.2.6 Segurança - São Roque | 1.2 São Roque | 1.2.2.6 | Farma | Lucas Caetano |
| 1.2.3.1 Administrativo - São Roque | 1.2 São Roque | 1.2.3.1 | Farma | Lucas Caetano |
| 1.2.3.2 Áreas Comuns - São Roque | 1.2 São Roque | 1.2.3.2 | Farma | Lucas Caetano |
| 1.3.1.1 Terceiros - Derma | 1.3 Derma | 1.3.1.1 | Derma | Elaine |
| 1.3.1.2 Estoque - Derma | 1.3 Derma | 1.3.1.2 | Derma | Elaine |
| 1.3.1.3 PCP - Derma | 1.3 Derma | 1.3.1.3 | Derma | Elaine |
| 1.3.1.4 Qualidade - Derma | 1.3 Derma | 1.3.1.4 | Derma | Elaine |
| 1.3.1.6 Segurança - Derma | 1.3 Derma | 1.3.1.6 | Derma | Elaine |
| 1.3.1.7 Administrativo - Derma | 1.3 Derma | 1.3.1.7 | Derma | Elaine |
| 1.3.1.8 Áreas Comuns - Derma | 1.3 Derma | 1.3.1.8 | Derma | Elaine |
| 1.4.1.1 Laboratório - São Caetano | 1.4 São Caetano | 1.4.1.1 | Farma | Lucas Caetano |
| 1.4.1.2 Estoque - São Caetano | 1.4 São Caetano | 1.4.1.2 | Farma | Lucas Caetano |
| 1.4.1.3 Recepção - São Caetano | 1.4 São Caetano | 1.4.1.3 | Farma | Lucas Caetano |

**GRUPO 2 — Lojas**

| CENTRO DE CUSTOS | CC - SINTÉTICO | CC REDUZIDO | B.U. | GESTOR |
|---|---|---|---|---|
| 2.1.1.1 Laboratório - Figueiras | 2 Lojas | 2.1.1.1 | Farma | Ana Lucia |
| 2.1.2.1 Recepção Derma - Figueiras | 2 Lojas | 2.1.2.1 | Derma | Elaine |
| 2.1.2.2 Recepção Nutri - Figueiras | 2 Lojas | 2.1.2.2 | Farma | Ana Lucia |
| 2.1.2.3 Recepção Magistral - Figueiras | 2 Lojas | 2.1.2.3 | Farma | Ana Lucia |
| 2.1.2.4 Segurança - Figueiras | 2 Lojas | 2.1.2.4 | Farma | Ana Lucia |
| 2.1.2.6 Estoque - Figueiras | 2 Lojas | 2.1.2.6 | Farma | Ana Lucia |
| 2.1.3.1 Áreas Comuns - Figueiras | 2 Lojas | 2.1.3.1 | Farma | Ana Lucia |
| 2.2.1.1 Laboratório - São Caetano | 2 Lojas | 2.2.1.1 | Farma | Ana Lucia |
| 2.2.2.1 Recepção Derma - São Caetano | 2 Lojas | 2.2.2.1 | Derma | Elaine |
| 2.2.2.2 Recepção Nutri - São Caetano | 2 Lojas | 2.2.2.2 | Farma | Ana Lucia |
| 2.2.2.3 Recepção Magistral - São Caetano | 2 Lojas | 2.2.2.3 | Farma | Ana Lucia |
| 2.2.2.6 Estoque - São Caetano | 2 Lojas | 2.2.2.6 | Farma | Ana Lucia |
| 2.2.3.1 Áreas Comuns - São Caetano | 2 Lojas | 2.2.3.1 | Farma | Ana Lucia |
| 2.3.1.1 Laboratório - Vila América | 2 Lojas | 2.3.1.1 | Farma | Ana Lucia |
| 2.3.2.1 Recepção Derma - Vila América | 2 Lojas | 2.3.2.1 | Derma | Elaine |
| 2.3.2.2 Recepção Nutri - Vila América | 2 Lojas | 2.3.2.2 | Farma | Ana Lucia |
| 2.3.2.3 Recepção Magistral - Vila América | 2 Lojas | 2.3.2.3 | Farma | Ana Lucia |
| 2.3.2.5 Estoque - Vila América | 2 Lojas | 2.3.2.5 | Farma | Ana Lucia |
| 2.3.3.1 Áreas Comuns - Vila América | 2 Lojas | 2.3.3.1 | Farma | Ana Lucia |
| 2.4.1.1 Laboratório - Graciosa | 2 Lojas | 2.4.1.1 | Farma | Ana Lucia |
| 2.4.2.1 Recepção Derma - Graciosa | 2 Lojas | 2.4.2.1 | Derma | Elaine |
| 2.4.2.2 Recepção Nutri - Graciosa | 2 Lojas | 2.4.2.2 | Farma | Ana Lucia |
| 2.4.2.3 Recepção Magistral - Graciosa | 2 Lojas | 2.4.2.3 | Farma | Ana Lucia |
| 2.4.2.5 Estoque - Graciosa | 2 Lojas | 2.4.2.5 | Farma | Ana Lucia |
| 2.4.3.1 Áreas Comuns - Graciosa | 2 Lojas | 2.4.3.1 | Farma | Ana Lucia |
| 2.5.1.1 Laboratório - São Roque | 2 Lojas | 2.5.1.1 | Farma | Ana Lucia |
| 2.5.2.1 Recepção Derma - São Roque | 2 Lojas | 2.5.2.1 | Derma | Elaine |
| 2.5.2.2 Recepção Nutri - São Roque | 2 Lojas | 2.5.2.2 | Farma | Ana Lucia |
| 2.5.2.3 Recepção Magistral - São Roque | 2 Lojas | 2.5.2.3 | Farma | Ana Lucia |
| 2.5.2.5 Estoque - São Roque | 2 Lojas | 2.5.2.5 | Farma | Ana Lucia |
| 2.5.3.1 Áreas Comuns - São Roque | 2 Lojas | 2.5.3.1 | Farma | Ana Lucia |
| 2.6.1.1 Laboratório - Loja Derma | 2.6 Loja Derma | 2.6.1.1 | Derma | Elaine |
| 2.6.2.2 Recepção - Loja Derma | 2.6 Loja Derma | 2.6.2.2 | Derma | Elaine |
| 2.6.3.1 Áreas Comuns - Loja Derma | 2.6 Loja Derma | 2.6.3.1 | Derma | Elaine |
| 2.7 Administrativo Lojas | 2.7 Administrativo Lojas | 2.7 | Farma | Ana Lucia |

**GRUPO 3 — Logística e Facilities**

| CENTRO DE CUSTOS | CC - SINTÉTICO | CC REDUZIDO | B.U. | GESTOR |
|---|---|---|---|---|
| 3.1.2.1 Expedição | 3.1 Estoque | 3.1.2.1 | Farma | Lucas Caetano |
| 3.1.2.2 Recebimento / Expedição | 3.1 Estoque | 3.1.2.2 | Farma | Lucas Caetano |
| 3.1.2.3 Separação / Expedição | 3.1 Estoque | 3.1.2.3 | Farma | Lucas Caetano |
| 3.1.2.4 Embarque / Expedição | 3.1 Estoque | 3.1.2.4 | Farma | Lucas Caetano |
| 3.1.2.5 Segurança / Expedição | 3.1 Estoque | 3.1.2.5 | Farma | Lucas Caetano |
| 3.1.2.7 Matéria Prima - Almoxarifado | 3.1 Estoque | 3.1.2.7 | Farma | Lucas Caetano |
| 3.1.2.9 Segurança / Almoxarifado | 3.1 Estoque | 3.1.2.9 | Farma | Lucas Caetano |
| 3.1.2.10 Transporte | 3.1 Estoque | 3.1.2.10 | Farma | Lucas Caetano |
| 3.2.1 Manutenção Predial | 3.2 Obras & Manutenção | 3.2.1 | Farma | Lucas Caetano |
| 3.2.2 Manutenção Geral | 3.2 Obras & Manutenção | 3.2.2 | Farma | Lucas Caetano |
| 3.3.1 Limpeza Cidade Viva | 3.3 Limpeza | 3.3.1 | Farma | Lucas Caetano |
| 3.3.2 Limpeza Absoluto | 3.3 Limpeza | 3.3.2 | Farma | Lucas Caetano |
| 3.3.3 Limpeza Advanced | 3.3 Limpeza | 3.3.3 | Farma | Lucas Caetano |
| 3.3.4 Limpeza Estoque | 3.3 Limpeza | 3.3.4 | Farma | Lucas Caetano |
| 3.3.5 Limpeza CT | 3.3 Limpeza | 3.3.5 | CT | Lucas Caetano |
| 3.3.6 Limpeza Estoque Derma | 3.3 Limpeza | 3.3.6 | Derma | Lucas Caetano |
| 3.3.7 Limpeza Lojas | 3.3 Limpeza | 3.3.7 | Farma | Lucas Caetano |

**GRUPO 4 — Backoffice**

| CENTRO DE CUSTOS | CC - SINTÉTICO | CC REDUZIDO | B.U. | GESTOR |
|---|---|---|---|---|
| 4.1.3.1 Presidência | 4.1.3 Presidência | 4.1.3.1 | Farma | Stefany |
| 4.1.3.2 Secretaria Executiva | 4.1.3 Presidência | 4.1.3.2 | Farma | Stefany |
| 4.2.3.1 Administrativo/Financeiro | 4.2.3 Adm/Financeiro | 4.2.3.1 | Farma | Ingrid |
| 4.2.3.2.1 Financeiro | 4.2.3 Adm/Financeiro | 4.2.3.2 | Farma | Ingrid |
| 4.2.3.2.2 Contas a Pagar | 4.2.3 Adm/Financeiro | 4.2.3.2 | Farma | Ingrid |
| 4.2.3.2.3 Contas a Receber | 4.2.3 Adm/Financeiro | 4.2.3.2 | Farma | Ingrid |
| 4.2.3.2.4 Tesouraria | 4.2.3 Adm/Financeiro | 4.2.3.2 | Farma | Ingrid |
| 4.2.3.3 Controladoria | 4.2.3 Adm/Financeiro | 4.2.3.3 | Farma | Ingrid |
| 4.2.3.4 Cadastro | 4.2.3 Adm/Financeiro | 4.2.3.4 | Farma | Ingrid |
| 4.2.3.5 Compras | 4.2.3 Adm/Financeiro | 4.2.3.5 | Farma | Ingrid |
| 4.2.3.6.1 Gente & Gestão | 4.2.3 Adm/Financeiro | 4.2.3.6 | Farma | Ingrid |
| 4.2.3.6.2 DP - Departamento Pessoal | 4.2.3 Adm/Financeiro | 4.2.3.6 | Farma | Ingrid |
| 4.2.3.6.3 RS - Recrutamento e Seleção | 4.2.3 Adm/Financeiro | 4.2.3.6 | Farma | Ingrid |
| 4.2.3.6.4 DHO - Desenvolvimento Humano Organizacional | 4.2.3 Adm/Financeiro | 4.2.3.6 | Farma | Ingrid |
| 4.2.3.6.5 SST - Segurança do Trabalho | 4.2.3 Adm/Financeiro | 4.2.3.6 | Farma | Ingrid |
| 4.2.3.7 Prevenção à Fraude | 4.2.3 Adm/Financeiro | 4.2.3.7 | Farma | Ingrid |
| 4.2.3.8 Paralegal | 4.2.3 Adm/Financeiro | 4.2.3.8 | Farma | Ingrid |
| 4.2.3.9 Jurídico | 4.2.3 Adm/Financeiro | 4.2.3.9 | Farma | Ingrid |
| 4.2.3.10.1 Contabilidade | 4.2.3 Adm/Financeiro | 4.2.3.10 | Farma | Ingrid |
| 4.2.3.10.2 Fiscal | 4.2.3 Adm/Financeiro | 4.2.3.10 | Farma | Ingrid |
| 4.3.3.1 Gestão E-commerce | 4.3.3 E-commerce | 4.3.3.1 | Farma | Welby |
| 4.3.3.2 Mídia Interna | 4.3.3 E-commerce | 4.3.3.2 | Farma | Welby |
| 4.3.3.3 Mídia Externa | 4.3.3 E-commerce | 4.3.3.3 | Farma | Welby |
| 4.4.3.1 Gestão Comercial | 4.4.3 Comercial | 4.4.3.1 | Farma | Welby |
| 4.4.3.2 Comercial - Magistral | 4.4.3 Comercial | 4.4.3.2 | Farma | Welby |
| 4.4.3.3 Comercial - Derma | 4.4.3 Comercial | 4.4.3.3 | Derma | Welby |
| 4.4.3.4 Comercial - Nutri | 4.4.3 Comercial | 4.4.3.4 | Farma | Welby |
| 4.4.3.5 Propagandistas | 4.4.3 Comercial | 4.4.3.5 | Farma | Welby |
| 4.5.3.1 Gestão Marketing | 4.5.3 Marketing | 4.5.3.1 | Farma | Welby |
| 4.5.3.2 Marketing | 4.5.3 Marketing | 4.5.3.2 | Farma | Welby |
| 4.5.3.3 Eventos | 4.5.3 Marketing | 4.5.3.3 | Farma | Welby |
| 4.5.3.4 Criação | 4.5.3 Marketing | 4.5.3.4 | Farma | Welby |
| 4.5.3.5 C.T. Oficial | 4.5.3 Marketing | 4.5.3.5 | CT | Welby |
| 4.5.3.6 Podcast | 4.5.3 Marketing | 4.5.3.6 | Farma | Welby |
| 4.5.3.7 Marketing de Influenciadores | 4.5.3 Marketing | 4.5.3.7 | Farma | Welby |
| 4.6.3.1 Atendimento ao Cliente - SAC | 4.6.3 SAC | 4.6.3.1 | Farma | Welby |
| 4.7.3.1 Operações | 4.7.3 Operações | 4.7.3.1 | Farma | Lucas Caetano |
| 4.8.3.1 Tecnologia da Informação | 4.8.3 TI | 4.8.3.1 | Farma | Leandro |
| 4.8.3.2 Infraestrutura | 4.8.3 TI | 4.8.3.2 | Farma | Leandro |
| 4.8.3.3 Sistemas | 4.8.3 TI | 4.8.3.3 | Farma | Leandro |
| 4.8.3.4 Desenvolvedores | 4.8.3 TI | 4.8.3.4 | Farma | Leandro |
| 4.8.3.5 Dados | 4.8.3 TI | 4.8.3.5 | Farma | Leandro |
| 4.9.3.1 Gestão Inovação & Regulatório | 4.9.3 Inovação & Regulatório | 4.9.3.1 | Farma | Elaine |
| 4.9.3.2 Qualidade | 4.9.3 Inovação & Regulatório | 4.9.3.2 | Farma | Elaine |
| 4.9.3.3 Inovação & Tendência Derma | 4.9.3 Inovação & Regulatório | 4.9.3.3 | Derma | Elaine |
| 4.9.3.4 Centro Técnico | 4.9.3 Inovação & Regulatório | 4.9.3.4 | Farma | Elaine |
| 4.9.3.5 Regulatório | 4.9.3 Inovação & Regulatório | 4.9.3.5 | Farma | Elaine |
| 4.9.3.6 Inovação e Estabilidade Nutri | 4.9.3 Inovação & Regulatório | 4.9.3.6 | Nutri | Elaine |
| 4.11.3.1 Dep. Técnico | 4.11.3 Dep. Técnico | 4.11.3.1 | Farma | Welby |
| 4.11.3.2 Qualidade Magistral | 4.11.3 Dep. Técnico | 4.11.3.2 | Farma | Welby |
| 4.11.3.3 Treinamentos | 4.11.3 Dep. Técnico | 4.11.3.3 | Farma | Welby |
| 4.12.3.1 Regulatório de Empresas | 4.12.3 Regulatório de Empresas | 4.12.3.1 | Farma | Marcus |

**GRUPO 5 — Não Operacionais**

| CENTRO DE CUSTOS | CC - SINTÉTICO | CC REDUZIDO | B.U. | GESTOR |
|---|---|---|---|---|
| 5.1.4.1 Patrimonial | 5.1.4 Não Operacional | 5.1.4.1 | Patrimonial | Marcus |
| 5.1.4.1.1 Marcus | 5.1.4 Não Operacional | 5.1.4.1.1 | Patrimonial | Marcus |
| 5.1.4.1.2 Fernanda | 5.1.4 Não Operacional | 5.1.4.1.2 | Patrimonial | Marcus |
| 5.1.4.2 Haras | 5.1.4 Não Operacional | 5.1.4.2 | Haras | Marcus |
| 5.1.4.3 Ship | 5.1.4 Não Operacional | 5.1.4.3 | Ship | Marcus |

**GRUPO 6 — Projetos & Novos Negócios**

| CENTRO DE CUSTOS | CC - SINTÉTICO | CC REDUZIDO | B.U. | GESTOR |
|---|---|---|---|---|
| 6.1.1.1 Projeto Food | 6 Projetos & Novos Negócios | 6.1.1.1 | Food | Alessandro |
| 6.2.1.2 Projeto CT | 6 Projetos & Novos Negócios | 6.2.1.2 | CT | Alessandro |
| 6.2.1.3 Projeto Gym | 6 Projetos & Novos Negócios | 6.2.1.3 | Gym | Alessandro |
| 6.2.1.4 Projeto Dress | 6 Projetos & Novos Negócios | 6.2.1.4 | Dress | Alessandro |
| 6.2.1.5 Projeto Itts | 6 Projetos & Novos Negócios | 6.2.1.5 | Itts | Alessandro |

**GRUPO 7 — Oficial Gym**

| CENTRO DE CUSTOS | CC - SINTÉTICO | CC REDUZIDO | B.U. |
|---|---|---|---|
| 7.1.1.1 Administrativo Gym | 7 Oficial Gym | 7.1.1.1 | Gym |
| 7.1.2.1 Gym SBC | 7 Oficial Gym | 7.1.2.1 | Gym |
| 7.1.2.2 Gym Campinas | 7 Oficial Gym | 7.1.2.2 | Gym |
| 7.1.2.3 Gym Santo André | 7 Oficial Gym | 7.1.2.3 | Gym |
| 7.1.2.4 Gym Alto do Ipiranga | 7 Oficial Gym | 7.1.2.4 | Gym |

**GRUPO 8 — Incorporadora**

| CENTRO DE CUSTOS | CC - SINTÉTICO | CC REDUZIDO | B.U. |
|---|---|---|---|
| 8.1.1.1 Vaticana | 8 Incorporadora | 8.1.1.1 | Incorporadora |
| 8.1.1.2 Cruz de Malta | 8 Incorporadora | 8.1.1.2 | Incorporadora |
| 8.1.1.3 Manutenção Predial - Incorporadora | 8 Incorporadora | 8.1.1.3 | Incorporadora |
| 8.1.1.4 Transporte - Incorporadora | 8 Incorporadora | 8.1.1.4 | Incorporadora |
| 8.1.2.1 Diretoria - Incorporadora | 8 Incorporadora | 8.1.2.1 | Incorporadora |
| 8.1.2.2 Comercial - Incorporadora | 8 Incorporadora | 8.1.2.2 | Incorporadora |
| 8.1.3.1 TI - Incorporadora | 8 Incorporadora | 8.1.3.1 | Incorporadora |
| 8.1.3.2 Marketing - Incorporadora | 8 Incorporadora | 8.1.3.2 | Incorporadora |
| 8.1.3.3 Financeiro - Incorporadora | 8 Incorporadora | 8.1.3.3 | Incorporadora |
| 8.1.3.4 RH - Incorporadora | 8 Incorporadora | 8.1.3.4 | Incorporadora |
| 8.1.3.5 Contabilidade - Incorporadora | 8 Incorporadora | 8.1.3.5 | Incorporadora |
| 8.1.3.6 Paralegal - Incorporadora | 8 Incorporadora | 8.1.3.6 | Incorporadora |

**GRUPO 9 — Ginger**

| CENTRO DE CUSTOS | CC - SINTÉTICO | CC REDUZIDO | B.U. | GESTOR |
|---|---|---|---|---|
| 9.1.1 Estilo | 9 Ginger | 9.1 | Ginger | Pamela |
| 9.1.2 Modelagem | 9 Ginger | 9.1 | Ginger | Pamela |
| 9.2.1 PCP | 9 Ginger | 9.2 | Ginger | Pamela |
| 9.2.2 Corte | 9 Ginger | 9.2 | Ginger | Pamela |
| 9.2.3 Pilotagem | 9 Ginger | 9.2 | Ginger | Pamela |
| 9.2.4 Acabamento | 9 Ginger | 9.2 | Ginger | Pamela |
| 9.2.5 Estoque | 9 Ginger | 9.2 | Ginger | Pamela |
| 9.3.1 Logística | 9 Ginger | 9.3 | Ginger | Pamela |
| 9.4.1 Presidência | 9 Ginger | 9.4 | Ginger | Pamela |
| 9.5.1 Comercial Geral | 9 Ginger | 9.5 | Ginger | Pamela |
| 9.5.2 Comercial Loja | 9 Ginger | 9.5 | Ginger | Pamela |
| 9.5.3 Comercial Atacado | 9 Ginger | 9.5 | Ginger | Pamela |
| 9.6.1 Social Media | 9 Ginger | 9.6 | Ginger | Pamela |
| 9.6.2 Criação | 9 Ginger | 9.6 | Ginger | Pamela |
| 9.7.1 SAC | 9 Ginger | 9.7 | Ginger | Pamela |
| 9.8.1 Compras | 9 Ginger | 9.8 | Ginger | Ingrid |
| 9.9.1 Financeiro | 9 Ginger | 9.9 | Ginger | Ingrid |
| 9.10.1 Contábil | 9 Ginger | 9.10 | Ginger | Ingrid |
| 9.10.2 Fiscal | 9 Ginger | 9.10 | Ginger | Ingrid |
| 9.11.1 Infraestrutura | 9 Ginger | 9.11 | Ginger | Leandro |
| 9.11.2 Sistemas | 9 Ginger | 9.11 | Ginger | Leandro |

---

### 5. EMPRESA / B.U. — Mapeamento por empresa pagadora

| Empresa pagadora | B.U. | CC obrigatório |
|---|---|---|
| JJ | Derma | Grupo 1.3 ou 2.x Derma |
| Max | Derma | Grupo 1.3 ou 2.x Derma |
| Layneskin | Derma | Grupo 1.3 ou 2.x Derma |
| CT | CT | Grupo 3.3.5 ou 4.5.3.5 |
| Haras | Haras | **SEMPRE 5.1.4.2** |
| Patrimonial | Patrimonial | **SEMPRE 5.1.4.1.x** |
| Ship | Ship | **SEMPRE 5.1.4.3** |
| Lojas / Majestic / Majestics | Farma | Grupo 2 |
| Advanced | Farma | Grupo 1.1 |
| Food | Food | 6.1.1.1 |
| Ginger | Ginger | Grupo 9 |
| Não informado (PF) | Pessoal | 4.2.3.1 |
| Não informado (PJ) | Matriz | 4.2.3.1 |

> REGRA CRITICA: Haras, Patrimonial e Ship devem SEMPRE usar CCs do Grupo 5 (Não Operacionais). Nunca lançar em CCs operacionais. Isso garante isolamento nos filtros de BI.

---

### 6. FASE DO NEGÓCIO
`Pré-lançamento` | `Lançamento` | `Ramp-up` | `Maturidade` | `Otimização`
- **Padrão: `Maturidade`**
- CCs dos Grupos 6, 7, 9 marcados como "Novo" → usar `Lançamento`

### 7. STATUS
- `Realizado` (padrão) | `Previsto` | `Orçado`

### 8. FONTE
`DRE` | `FCF` | `Extrato` | `Input Manual`

---

## Lógica de matching de CC (quando não informado explicitamente)

1. **Nome exato** → buscar na matriz pelo nome do CC
2. **Palavra-chave parcial** → ex: "pesagem" → CCs 1.1.1.2.x ou 1.2.1.2.x (desambiguar pela empresa/BU)
3. **Tipo de custo + BU** → ex: "salário + Ginger" → 9.8.1 Compras ou área mais adequada
4. **Fallback por natureza**:

| Natureza | CC fallback |
|---|---|
| Marketing / Mídia / Ads | 4.5.3.2 Marketing |
| RH / Salário / Folha / DP | 4.2.3.6.2 DP |
| TI / Tecnologia / Sistema | 4.8.3.1 TI |
| Financeiro / Tesouraria | 4.2.3.2.4 Tesouraria |
| Jurídico / Paralegal | 4.2.3.9 Jurídico |
| Compras / Fornecedor | 4.2.3.5 Compras |
| Sem contexto suficiente | 4.2.3.1 Adm/Financeiro — registrar em OBSERVAÇÃO |

---

## Saída Obrigatória (3 blocos)

### Bloco 1 — TABELA CSV
- Cabeçalho com as 17 colunas exatas
- Separador: ponto e vírgula (`;`)
- Uma linha por lançamento
- Sem texto fora do CSV dentro deste bloco

### Bloco 2 — INTERPRETAÇÃO
- Tipo de dado identificado (DRE / FCF / Extrato / Misto)
- Qualidade dos dados: Alta / Média / Baixa
- Premissas utilizadas

### Bloco 3 — ALERTAS
- Campos não informados
- Inferências realizadas (CC, BU, FASE)
- CCs inativos ou não-operacionais identificados
- Possíveis inconsistências

---

## Exemplo de Saída CSV

```csv
CENTRO DE CUSTOS;CC - SINTÉTICO;CC REDUZIDO;P.C. SINTÉTICO;GRUPO;EMPRESA;VALOR;MÊS DE PAGAMENTO;MÊS DE EMISSÃO;B.U.;FASE DO NEGÓCIO;GESTOR DA AREA;DIRETOR DA AREA;OBSERVAÇÃO;FONTE;STATUS;DATA
4.5.3.2 Marketing;4.5.3 Marketing;4.5.3.2;Despesas Operacionais;Despesa;Farma;-3500.00;2024-03;2024-03;Farma;Maturidade;Welby;;Inferido por palavra-chave marketing;Input Manual;Realizado;2024-03-15
```

---

## Restrições
- NUNCA inventar valores financeiros
- NUNCA alterar nomes das colunas
- NUNCA omitir colunas (deixar em branco se sem dado, incluir separador `;`)
- NUNCA usar CCs marcados como INATIVAR/inativo — alertar e sugerir substituto ativo
- NUNCA usar CC operacional para Haras, Patrimonial ou Ship
