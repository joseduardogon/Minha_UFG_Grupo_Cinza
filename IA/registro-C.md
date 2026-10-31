# Registro de uso de IA – Pessoa C

Autor: José Eduardo Gontijo de Carvalho (Pessoa C). Frente: Eventos, RU e Notícias, mais as entidades Regional e Campus.

Formato de cada entrada: identificação da IA, URL, data de acesso, resumo do uso, divisão do trabalho e prompts. A referência ABNT que vai para a bibliografia aparece no fim.

## C-IA-01 – Apoio à produção do bloco C (Eventos, RU e Notícias)

- **IA:** Anthropic. Claude Code (modelo Claude Sonnet 5.5, com subagentes). Assistente de IA.
- **URL:** claude.ai/code
- **Data de acesso:** de 16 a 30 de outubro de 2026.
- **Contexto fornecido pelo autor:** enunciado da APS, repositório da equipe (contrato-base, divisão de trabalho, itens de Pessoa D como padrão), 31 capturas de tela do app Minha UFG versão 3.2.0 feitas pelo autor, e as instruções e correções descritas abaixo.

### O que o autor fez

- Definiu o escopo do trabalho, a ordem de produção e as regras de conduta: não alterar nada de outras pessoas, não fazer commit antes de revisar, usar linguagem simples nos relatórios.
- Decidiu quais artefatos entrariam e como seriam avaliados, e conduziu a revisão em várias rodadas, pedindo ajustes de forma, de conteúdo e de consistência.
- Observou o aplicativo real e forneceu as 31 capturas de tela, incluindo testes no aparelho: troca de mês e de dia, almoço e jantar de vários dias, estado sem eventos e telas com o aparelho em modo avião.
- Corrigiu o modelo com conhecimento direto do app: informou que o RU carrega a semana toda de uma vez, o que levou a refazer sequência, estados, classes e contratos do RU; as capturas que ele fez refutaram suposições anteriores (por exemplo, a troca de mês mantém o dia, e o jantar não tem sábado).
- Escolheu o que mantinha como premissa e o que passava a ser fato confirmado, e decide o que vai para a entrega e como a IA é citada.

### O que a IA fez, sob a direção do autor

- Leu o repositório e as capturas e fez auditorias do bloco C contra o contrato, o modelo de item e o padrão de Pessoa D.
- Redigiu as primeiras versões dos itens (casos de uso, atividades, protótipos, sequências, estados, componentes, classes, dicionários de dados, contratos e regras E-C-A), o código PlantUML dos diagramas e as fichas de entidade, e reescreveu esses itens depois de cada correção do autor.
- Gerou as imagens dos diagramas, conferiu links, rastreabilidade e consistência entre itens por script, e redigiu o relatório de evolução e sua versão resumida.
- Os textos produzidos foram revisados e ajustados pelo autor; o que ele não confirmou nas capturas está marcado como premissa nos READMEs de cada pasta.

### Prompts (resumo cronológico)

1. 16/10: pedido do relatório de evolução do projeto, em Markdown e PDF, para o professor, a partir do repositório e do enunciado.
2. 16/10: aplicar à Pessoa C o mesmo tratamento dado à Pessoa D, criando e preenchendo os arquivos da frente C de forma organizada e documentada, sem mexer em nada de Pessoa D e sem commitar.
3. 16/10: envio das capturas de tela do app para corrigir RU, Notícias e Eventos conforme o app real.
4. 30/10: "precisamos finalizar o bloco C": revisar todos os documentos do repositório, ver o que falta da documentação do bloco C, corrigir e garantir que está de acordo com as telas e com o app, usando subagentes.
5. 30/10: envio de 16 novas capturas, entre elas a lista de Eventos, o Almoço e o Jantar do RU e as telas em modo avião, com a informação de que o RU carrega a semana toda.

Os prompts completos, quando tiverem mais de um parágrafo, vão para o apêndice de prompts do documento final (regra 6 do enunciado).

### Referência (ABNT)

ANTHROPIC. **Claude Code**. Assistente de IA. Disponível em: claude.ai/code. Acesso em: 30 out. 2026. Questão: Apêndice <X>, Seção <X.1>.

<!-- Preencher <X> na editoração, junto com o apêndice de prompts. -->
