# APIs públicas para dados externos

Origem: conteúdo da antiga skill `especialista-apis-publicas`, incorporado aqui em 06/10/2026 porque a função (escolher e integrar fonte de dado externo) pertence à engenharia de dados.

Use quando um projeto (planilha, dashboard, automação, script) precisar puxar um dado externo: câmbio, CEP, CNPJ, indicadores econômicos, geolocalização, validação de dados, clima ou dados governamentais.

## O que o catálogo genérico é (e não é)

O repositório `public-apis/public-apis` (e listas parecidas, como `publicapis.dev`) é uma **tabela de referência**, não um pacote instalável: reúne mais de 1.400 APIs gratuitas em cerca de 50 categorias, com descrição, tipo de autenticação (nenhuma, chave gratuita ou OAuth), uso de HTTPS e CORS. Não há código, SLA nem garantia de disponibilidade. Quem mantém é a comunidade.

Categorias úteis para controladoria, FP&A, automações e dashboards: câmbio e finanças, geocodificação (CEP, coordenadas), validação de dados (e-mail, telefone, documentos), clima, dados abertos governamentais e utilitários de desenvolvimento.

## Fontes brasileiras (preferir quando o dado for brasileiro)

| Fonte | O que oferece | Observação |
|---|---|---|
| Banco Central, SGS (Sistema Gerenciador de Séries Temporais) | Câmbio, Selic, CDI, IPCA e outras séries históricas oficiais | Fonte oficial para indicadores e câmbio |
| BrasilAPI | CNPJ, CEP, bancos, feriados nacionais, DDD, tabela FIPE | Mantida pela comunidade, sem chave |
| ViaCEP | Consulta de CEP | Gratuita, sem chave |
| IBGE, API de Localidades e SIDRA | Municípios, UFs, população e indicadores | Fonte oficial |
| AwesomeAPI (economia) | Cotações de câmbio em tempo real | Alternativa simples ao SGS para casos rápidos |

## Procedimento

1. **Identifique a necessidade real:** que dado, com que frequência, e em que formato será consumido.
2. **Escolha a API:** prefira fonte brasileira oficial para dado brasileiro; use o catálogo genérico só quando não houver equivalente nacional.
3. **Confirme que está ativa:** teste uma chamada ou pesquise o estado atual antes de construir em cima. Formatos mudam e listas ficam defasadas.
4. **Escreva a integração no formato do projeto:**
   - Python (`requests`) para scripts e automações;
   - Power Query (`Web.Contents`) para Excel e Power BI;
   - conector HTTP do Power Automate para fluxos;
   - Google Apps Script (`UrlFetchApp`) para Google Sheets.
5. **Isole a chamada** em uma função própria, fácil de trocar, com tratamento de erro, limite de tentativas, registro (log) e cache quando fizer sentido.
6. **Não trate como instalação de plugin:** é código de integração.

## Limitações a declarar ao usuário

- Nenhuma dessas fontes garante SLA. Se houver dependência crítica em produção, considere provedor pago com contrato.
- O formato de resposta pode mudar sem aviso.
- Não envie dados sensíveis (por exemplo, dados pessoais) a APIs de terceiros sem avaliar LGPD e termos de uso.
- Registre a data da consulta e a fonte do dado na base, para rastreabilidade.
