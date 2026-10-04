# Critérios de Rateio — Guia Técnico

## Princípio Fundamental

O critério de rateio deve refletir a **relação de causalidade** entre o custo indireto e o objeto de custeio. Rateios arbitrários distorcem o custo unitário e induzem decisões erradas. Sempre questionar: "o que consome esse recurso?"

---

## Critérios por Tipo de Custo Indireto

### Mão de Obra Indireta (supervisão, PCP, qualidade)
| Critério | Quando usar |
|----------|-------------|
| Horas de MOD | Quando a supervisão acompanha o esforço humano |
| Número de funcionários | Para custos de RH, benefícios gerais |
| Número de ordens/lotes | Para PCP com muitas ordens pequenas |

### Energia Elétrica
| Critério | Quando usar |
|----------|-------------|
| Horas-máquina | Quando há medição de consumo por equipamento |
| Capacidade instalada (kW) | Quando não há medição individual |
| Estimativa técnica por produto | Quando há dados de engenharia |
| Rateio por área (m²) | Para iluminação e climatização |

### Aluguel e Espaço Físico
| Critério | Quando usar |
|----------|-------------|
| Área ocupada (m²) | Padrão para espaço físico |
| Área ponderada por valor/m² | Quando há setores de maior valor |

### Manutenção
| Critério | Quando usar |
|----------|-------------|
| Horas-máquina | Manutenção de equipamentos |
| Ordens de manutenção emitidas | Para manutenção preventiva/corretiva |
| Valor dos ativos | Para contratos de manutenção proporcional ao ativo |

### Depreciação
| Critério | Quando usar |
|----------|-------------|
| Direto ao equipamento | Quando o bem atende a um processo específico |
| Horas de uso | Para bens compartilhados entre produtos |
| Unidades produzidas | Depreciação por produção (método de unidades de produção) |

### TI e Sistemas
| Critério | Quando usar |
|----------|-------------|
| Número de usuários | Para licenças e suporte |
| Transações processadas | Para sistemas transacionais |
| Faturamento do departamento | Para custos corporativos de TI |

### Despesas Administrativas
| Critério | Quando usar |
|----------|-------------|
| Faturamento | Mais comum para despesas gerais |
| Número de funcionários | Para custos de infraestrutura pessoal |
| Número de transações | Para departamentos de suporte |

### Logística e Frete de Saída
| Critério | Quando usar |
|----------|-------------|
| Peso ou volume expedido | Mais preciso para frete |
| Faturamento por canal | Para comissões e despesas comerciais |
| Número de pedidos | Para custos de picking e separação |

---

## Hierarquia de Rateio (Departamentos Auxiliares → Produtivos)

Quando há departamentos de apoio (manutenção, utilidades, almoxarifado) que servem a departamentos produtivos, o rateio deve seguir:

**Método Direto:** Rateio direto dos auxiliares para os produtivos (ignora serviços entre auxiliares). Simples, mas pode distorcer quando auxiliares se prestam serviços mutuamente.

**Método Sequencial (Step-Down):** Fecha os auxiliares em ordem de maior para menor serviço prestado a outros auxiliares. Mais preciso.

**Método Recíproco (Algébrico):** Considera serviços mútuos entre auxiliares via equações simultâneas. Mais preciso, mais complexo.

**Recomendação:** Para a maioria das PMEs, o método sequencial oferece boa precisão com esforço razoável.

---

## Alertas de Qualidade no Rateio

**⚠️ Evitar:**
- Usar faturamento como base para custos que não têm relação com volume de receita
- Aplicar o mesmo critério para todos os CIF (one-size-fits-all)
- Ratear custos fixos como se fossem variáveis
- Ignorar a capacidade ociosa no cálculo da taxa de rateio

**✅ Boas práticas:**
- Segregar CIF em grupos homogêneos antes de definir o critério
- Revisar critérios anualmente ou quando houver mudanças operacionais relevantes
- Documentar e justificar cada critério adotado
- Calcular a taxa de rateio com base na capacidade normal (não na capacidade real do período), para evitar que a ociosidade distorça o custo do produto

---

## Taxa de Rateio com Capacidade Normal vs. Real

**Erro comum:** Dividir o CIF fixo pela quantidade realmente produzida.

**Consequência:** Quando a produção cai, o custo unitário sobe artificialmente — o produto parece mais caro simplesmente porque a fábrica produziu menos.

**Correto:**
```
Taxa de Rateio = CIF Orçado / Capacidade Normal de Produção (horas ou unidades)
CIF Sub/Sobreabsorvido = CIF Real - (Taxa × Produção Real) → lançado como variância do período
```

Isso isola o custo da ociosidade e mantém o custo unitário do produto estável.
