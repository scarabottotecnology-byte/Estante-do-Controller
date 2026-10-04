---
name: especialista-apis-publicas
description: Ajuda a escolher e integrar APIs públicas gratuitas (câmbio, CEP, CNPJ, clima, validação de dados, geocoding, dados governamentais, etc.) em qualquer projeto. ACIONAR SEMPRE que o usuário precisar puxar um dado externo pra dentro de um projeto — planilha, dashboard, automação, script — e mencionar coisas como "preciso de uma API pra X", "puxar cotação do dólar", "validar CNPJ", "consultar CEP", "dados do IBGE/Banco Central", "integrar API pública", ou quando o projeto chegar numa fase que exige dado externo (câmbio, geolocalização, validação, clima, indicadores econômicos) sem que o usuário precise pedir explicitamente. Também acionar quando o usuário mencionar o catálogo public-apis/public-apis ou pedir uma lista de APIs gratuitas.
---

# Especialista em APIs Públicas

Este skill existe pra evitar duas armadilhas: (1) achar que uma lista de referência tipo `public-apis/public-apis` é algo "instalável" — não é, é só uma tabela markdown de +1.400 APIs gratuitas, sem código nenhum — e (2) perder tempo garimpando manualmente toda vez que um projeto precisa de um dado externo. A função deste skill é: identificar a API certa pra necessidade do momento e já escrever a integração, no formato que o projeto pede.

## Como o catálogo genérico funciona

O `public-apis/public-apis` (e listas irmãs como `publicapis.dev`) organizam ~50 categorias. Cada entrada tem: nome, descrição curta, tipo de autenticação (nenhuma / apiKey gratuita / OAuth), se usa HTTPS, se libera CORS. A maioria não pede cadastro. Não há SLA nem garantia de uptime — é uma lista mantida pela comunidade, não uma plataforma.

Categorias mais úteis pro tipo de projeto que costuma aparecer aqui (controladoria, FP&A, automações, dashboards, apps internos):

- **Currency Exchange / Finance** — cotação de moedas, indicadores de mercado
- **Geocoding** — CEP, coordenadas, IP geolocation
- **Data Validation** — validação de e-mail, telefone, documentos
- **Weather** — clima atual e histórico
- **Government / Open Data** — bases públicas diversas
- **Development** — utilitários (encurtador de URL, gerador de dados de teste, OCR, tradução)

## Fontes brasileiras (mais relevantes que o catálogo genérico pro contexto do usuário)

O `public-apis/public-apis` é majoritariamente internacional. Pra projetos com dado brasileiro, estas costumam ser a escolha melhor — gratuitas, sem necessidade de conta na maioria dos casos:

- **Banco Central — SGS (Sistema Gerenciador de Séries Temporais)**: câmbio (dólar, euro), SELIC, CDI, IPCA e outras séries históricas oficiais.
- **BrasilAPI**: CNPJ, CEP, bancos, feriados nacionais, DDD, tabela FIPE — mantida pela comunidade, sem chave.
- **ViaCEP**: consulta de CEP, gratuita, sem chave.
- **IBGE — API de Localidades e SIDRA**: municípios, UFs, dados de população e indicadores do Censo.
- **AwesomeAPI (economia)**: cotações de câmbio em tempo real, alternativa mais simples que o SGS pra casos rápidos.

Antes de usar qualquer uma: fazer uma checagem rápida (web search ou tentativa de chamada) pra confirmar que o endpoint ainda está no ar e que o formato de resposta não mudou — listas assim vivem defasadas em relação à realidade.

## O que fazer quando este skill for acionado

1. **Identificar a necessidade real**: que dado o projeto precisa (câmbio, CEP, validação, clima, etc.) e em que formato ele vai ser consumido (planilha, script Python, automação, dashboard).
2. **Escolher a API**: preferir fonte brasileira oficial quando o dado for brasileiro (câmbio → Banco Central; CEP/CNPJ → BrasilAPI/ViaCEP); usar o catálogo genérico só quando não houver equivalente nacional.
3. **Confirmar que está ativa**: pesquisar rapidamente se o endpoint segue funcionando antes de codar em cima dele.
4. **Escrever a integração já no formato do projeto**:
   - Python (`requests`) pra scripts e automações
   - Power Query (`Web.Contents`) pra Excel/Power BI
   - Conector HTTP do Power Automate pra fluxos
   - Google Apps Script (`UrlFetchApp`) pra Google Sheets
5. **Nunca tratar isso como instalação de plugin** — é código de integração, não um pacote a ser instalado via marketplace.

## Limitações a deixar claras pro usuário

- Nenhuma dessas fontes tem SLA garantido; para uso em produção com dependência crítica, vale considerar um provedor pago com contrato.
- Formatos de resposta podem mudar sem aviso — vale isolar a chamada da API numa função própria, fácil de trocar depois.
