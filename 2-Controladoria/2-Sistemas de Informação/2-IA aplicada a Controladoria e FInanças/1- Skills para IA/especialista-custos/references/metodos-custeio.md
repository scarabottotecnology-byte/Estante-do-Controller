# Métodos de Custeio — Referência Técnica

## 1. Custeio por Absorção

**Definição:** Todos os custos de produção (fixos e variáveis, diretos e indiretos) são absorvidos pelo produto. É o único método aceito pela legislação fiscal brasileira (IR/CSLL) e pelos padrões contábeis (CPC 16).

**Quando usar:**
- Obrigação legal/fiscal
- Empresas com linha de produtos homogênea
- Ambientes com baixa variação de volume

**Limitações gerenciais:**
- Custo unitário varia com o volume (diluição dos fixos)
- Pode induzir decisões erradas sobre mix de produtos
- Oculta a real contribuição marginal de cada produto

**Rateio dos CIF:** Necessário definir base de rateio consistente:
- Horas de MOD
- Horas-máquina
- Volume produzido
- Custo de MOD
- Faturamento

---

## 2. Custeio Variável (Direto)

**Definição:** Apenas os custos variáveis (diretos e indiretos variáveis) compõem o custo do produto. Custos fixos são tratados como despesa do período.

**Quando usar:**
- Análise gerencial de rentabilidade por produto/canal/cliente
- Decisões de mix de produtos
- Cálculo da margem de contribuição real
- Análise de ponto de equilíbrio
- Pricing e simulações de cenário

**Vantagem-chave:** O custo unitário não muda com o volume — permite comparações fidedignas entre períodos e produtos.

**Limitação:** Não aceito para fins fiscais; subavalua estoques (sem absorção dos fixos).

---

## 3. ABC — Activity-Based Costing

**Definição:** Aloca custos indiretos com base nas atividades consumidas pelos produtos, não por rateio arbitrário. Parte do princípio: atividades consomem recursos, produtos consomem atividades.

**Fases:**
1. Identificar atividades (setup, movimentação, inspeção, etc.)
2. Atribuir custos às atividades (cost pools)
3. Definir direcionadores de atividade (cost drivers)
4. Alocar custos das atividades aos produtos

**Quando usar:**
- Alta diversidade de produtos com volumes e complexidades diferentes
- Elevado peso dos custos indiretos
- Suspeita de subsídio cruzado entre produtos
- Empresas de serviços com múltiplos processos

**Limitação:** Custo de implantação elevado; demanda mapeamento detalhado de atividades.

---

## 4. Custeio Padrão

**Definição:** Define custos-padrão (ideais ou normais) para cada componente do custo, comparando-os com os custos reais para identificar desvios.

**Tipos de padrão:**
- **Ideal:** o melhor desempenho possível (sem perdas, sem ociosidade)
- **Normal:** desempenho atingível considerando condições normais de operação

**Variâncias a calcular:**
- Variância de preço de MP
- Variância de quantidade de MP
- Variância de eficiência de MOD
- Variância de taxa de MOD
- Variância de volume (absorção de fixos)
- Variância de eficiência de CIF

**Quando usar:**
- Indústrias com processo produtivo repetitivo e padronizado
- Controle de desempenho operacional
- Base para orçamento e forecast

---

## 5. Custeio por Processo

**Definição:** Adequado para produção contínua e homogênea. Os custos são acumulados por departamento/etapa produtiva e divididos pela quantidade produzida no período.

**Quando usar:**
- Indústrias com fluxo contínuo (química, alimentos, papel, petroquímica)
- Produto único ou poucos produtos com processo similar
- Difícil rastreamento por ordem específica

**Conceito-chave:** Unidades equivalentes — ajusta as unidades em processo considerando o grau de conclusão.

---

## 6. Custeio por Ordem

**Definição:** Os custos são acumulados por ordem de produção específica. Cada ordem é uma "ficha de custo" individualizada.

**Quando usar:**
- Produção sob encomenda
- Projetos de engenharia, construção civil
- Gráficas, roupas customizadas, manutenção industrial
- Quando cada produto/lote tem características únicas

---

## 7. TDABC — Time-Driven Activity-Based Costing

**Definição:** Simplificação do ABC tradicional. Usa dois parâmetros: custo por unidade de tempo do recurso e tempo consumido por cada transação/atividade.

**Fórmula:**
```
Taxa de Custo do Recurso = Custo Total do Departamento / Capacidade Prática (horas)
Custo da Atividade = Taxa × Tempo da Atividade
```

**Vantagem sobre o ABC:** Muito mais simples de manter e atualizar; escala para grandes volumes de transações; identifica capacidade ociosa automaticamente.

**Quando usar:**
- Empresas de serviços com alta variedade de transações
- Operações logísticas e de distribuição
- Bancos, seguradoras, saúde

---

## Combinações Recomendadas por Perfil de Empresa

| Perfil | Método Principal | Método Complementar |
|--------|-----------------|---------------------|
| Indústria de processo, produto único | Por Processo | Custeio Padrão |
| Indústria com múltiplos produtos | Absorção (fiscal) | Variável (gestão) |
| Manufatura diversificada, alto CIF | ABC | Variável |
| Produção sob encomenda | Por Ordem | Padrão |
| Serviços com muitas transações | TDABC | Variável |
| PME sem sistema robusto | Variável | Absorção simplificada |
