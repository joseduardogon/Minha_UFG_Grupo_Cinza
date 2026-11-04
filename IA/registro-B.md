# Registro de uso de IA – Pessoa B

Autor: Maicon Brendo da Silva. Frente: Segurança, Locais e Apps UFG, mais a revisão dos PRs #12 (Avaliação – Consultar notas) e #13 (Integração).

Formato de cada entrada: identificação da IA, URL, data de acesso, resumo do uso, divisão do trabalho e prompts. A referência ABNT que vai para a bibliografia aparece no fim.

## B-IA-01 – Apoio à elaboração de rascunhos da fatia B e conferência de revisões

- **IA:** Google. Antigravity (Gemini 2.5 Flash). Assistente de IA para Engenharia de Software.
- **URL:** https://antigravity.google.com
- **Data de acesso:** de 29 de outubro a 03 de novembro de 2026.
- **Contexto fornecido pelo autor:** enunciado da APS (INF0290/UFG), contrato-base da Equipe Cinza, capturas de tela reais do app Minha UFG v3.1.1 (telas inicial, Apps UFG, Segurança, Locais e Mapa do Campus Samambaia) e artefatos de Comum e Geral do repositório.

### O que o autor fez

- Estabeleceu as diretrizes de trabalho e regras de conduta para o assistente: proibição total de inventar informações ou fazer suposições sem respaldo nas capturas do app real, determinando um processo estritamente iterativo com validação e aprovação prévia antes de qualquer avanço.
- Realizou a engenharia reversa das telas reais das suas três funcionalidades, extraindo as regras de negócio a partir do uso do aplicativo:
  - **Apps UFG:** identificou que o catálogo de aplicativos é fixo e que a interação se limita ao redirecionamento externo para a Play Store.
  - **Segurança:** constatou que a funcionalidade possui apenas opções diretas de redirecionamento institucional (web via navegador e app via Play Store), sem necessidade de telas intermediárias ou de persistência de entidades.
  - **Locais:** analisou a dinâmica entre lista textual e mapa interativo, a centralização GPS e os marcadores de cores; definiu a modelagem da herança `Local <|-- UnidadeAcademica` vinculada ao Campus Samambaia.
- Avaliou criticamente, corrigiu, refinou e validou cada rascunho de diagrama e especificação gerado pela IA, ajustando textos, navegabilidade, parâmetros PlantUML e aderência ao roteiro antes de aprovar os artefatos definitivos.
- Conduziu as revisões de integração (PRs #12 e #13), identificando inconsistências a partir da sua própria experiência de modelagem (como o erro visual de sobreposição de setas em diagramas de atividades, a falta de atributos privados em classes e divergências nos códigos de casos de uso), incumbindo a IA de checar os arquivos envolvidos e auxiliar na estruturação dos relatórios.
- Decidiu o que seria versionado e submetido via branches e pull requests.

### O que a IA fez, sob a direção do autor

- Gerou rascunhos iniciais e propostas estruturais de código PlantUML e texto em Markdown para as funcionalidades da fatia B (`AppsUFG`, `Segurança` e `Locais`), baseando-se estritamente nas instruções, capturas e restrições fornecidas pelo autor.
- Apoiou a formalização das entradas `DD-Seguranca-01` e `DD-AppsUFG-01` a partir da constatação do autor de que os módulos tratam de configurações fixas sem entidades de domínio.
- Atuou como ferramenta de suporte nas revisões: realizou a checagem cruzada de sintaxe PlantUML, conferiu a existência de arquivos e métodos conforme as suspeitas levantadas pelo autor e auxiliou na formatação dos pareceres `REV-PR12-AvalConsultar.md` e `REV-PR13-Integracao.md`.
- Todos os rascunhos gerados passaram por triagem, correção e aprovação manual do autor antes de qualquer consolidação no repositório.

### Prompts (resumo cronológico)

1. 29/10: Definição das regras de conduta para a IA, exigindo processo iterativo sem suposições não comprovadas por capturas do app.
2. 29/10: Envio dos dados e telas de Apps UFG, solicitando rascunhos iniciais da cascata de casos de uso, fluxo de atividades, classes e contratos para posterior validação do autor.
3. 29/10: Envio da tela de Segurança e solicitação de rascunhos para os fluxos externos de navegador e Play Store.
4. 30/10: Discussão conceitual sobre a diferenciação entre `Local` e `UnidadeAcademica`, definição dos fluxos do mapa com GPS e elaboração de rascunhos dos diagramas de Locais para correção do autor.
5. 01/11: Organização do processo de revisão por pares e solicitação de verificação das regras de negócio de Avaliação no PR #12, com validação do autor sobre a sobreposição de setas nos diagramas de atividades.
6. 02/11: Apoio na auditoria do PR #13 (Integração), realizando a checagem cruzada dos diagramas gerais e localizando os arquivos com divergências de prefixo (`UC011.1` e `UC031.1`) apontadas pelo autor.
7. 03/11: Conferência dos ajustes realizados no PR #13 e adequação do registro de IA ao padrão resumido da equipe.

Os prompts completos, quando tiverem mais de um parágrafo, vão para o apêndice de prompts do documento final (regra 6 do enunciado).

### Referência (ABNT)

GOOGLE. **Antigravity**. Assistente de IA para Engenharia de Software. Disponível em: https://antigravity.google.com. Acesso em: 03 nov. 2026. Questão: Apêndice <X>, Seção <X.1>.

<!-- Preencher <X> na editoração, junto com o apêndice de prompts. -->
