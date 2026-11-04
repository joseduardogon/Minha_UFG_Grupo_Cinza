# Registro de uso de IA – Pessoa D

Autor: Phablo Tavares Paixão. Frente: transversais (DImp, DPac, pacote Comum, DCdu geral e tela inicial), Rádio, Guia Estudantil e Avaliação – Consultar notas, mais a integração (DDados e DD consolidados, recebimento das entidades e matriz de rastreabilidade) e a revisão dos itens de José Eduardo Gontijo de Carvalho.

Formato de cada entrada: identificação da IA, URL, data de acesso, resumo do uso, divisão do trabalho e prompts. A referência ABNT que vai para a bibliografia aparece no fim de cada entrada.

## D-IA-01 – Preparação do repositório e desenho transversal inicial (D-PRE e D-DST)

- **IA:** Anthropic. Claude (modelo Claude Opus 5.5). Assistente de IA.
- **URL:** claude.ai
- **Data de acesso:** 14 de outubro de 2026.
- **Contexto fornecido pelo autor:** enunciado da APS, `contrato-base.md`, `contexto-equipe.md`, o roteiro de atividades da Pessoa D para a semana 1 e 17 capturas de tela do app Minha UFG v3.1.1.

### O que o autor fez

- Definiu a estratégia da semana: primeiro destravar a equipe com a base comum, depois a produção individual e só então a integração.
- Informou o repositório da equipe e a regra de não commitar na `main` (tudo por branch e pull request, abertos por ele).
- Decidiu que o contrato prevalece sobre o `Guia_Diagramas.md` e que os documentos de apoio iam para `Docs/`.
- Tomou as decisões de modelagem do DCdu geral: não há quinto membro, o Painel web fica só no DImp e "Play Store / navegador" vira o ator **Aplicativo externo**, com as especializações Play Store, Navegador e Visualizador de PDF.
- Aplicou as alterações no repositório pela própria máquina (git bundle), revisou os diagramas e abriu os PRs.

### O que a IA fez, sob a direção do autor

- Verificou lacunas antes do D-PRE-01 e propôs a estrutura de pastas, o `Template-Item.md` e o primeiro registro de IA.
- Orientou a transferência das alterações por git bundle, com a sequência de comandos explicada.
- Redigiu o rascunho do `DCdu-Geral-01` (D-DST-01), o ajuste da seção 5 do contrato, o `DPac-Geral-01` e o `DImp-Geral-01` (D-DST-02) e os componentes, classes e estados do pacote Comum (`DCmp-Comum-01`, `DCla-Comum-01` a `04`, `DEst-Comum-01`) (D-DST-03).

### Prompts (resumo cronológico)

1. 14/10: perguntar se havia alguma dúvida importante antes do D-PRE-01, explicando a estratégia do roteiro da semana 1.
2. 14/10: informar o repositório, a proibição de commit na `main` e o foco na semana 1, e mandar seguir com o D-PRE-01.
3. 14/10: pedir o push da branch, mover os documentos para `Docs/` e manter o contrato como regra.
4. 14/10: pedir uma forma de levar as alterações do ambiente da IA para a máquina local e, depois, a sequência de comandos para aplicar os bundles no Ubuntu, conferindo a saída do terminal.
5. 14/10: seguir com o D-DST-01, respondendo às dúvidas sobre membros, Painel web e Aplicativo externo.
6. 14/10: mandar o bundle completo de D-DST-02 e D-DST-03 de uma vez, para revisão conjunta.

Os prompts completos, quando tiverem mais de um parágrafo, vão para o apêndice de prompts do documento final (regra 6 do enunciado).

### Referência (ABNT)

ANTHROPIC. **Claude**. Assistente de IA. Disponível em: claude.ai. Acesso em: 14 out. 2026. Questão: Apêndice <X>, Seção <X.1>.

## D-IA-02 – Apoio à produção, à revisão e à integração do bloco D

- **IA:** Anthropic. Claude Code (modelo Claude Opus 5.5). Assistente de IA.
- **URL:** https://claude.com/claude-code
- **Data de acesso:** de 19 de outubro a 2 de novembro de 2026.
- **Contexto fornecido pelo autor:** enunciado da APS, repositório da equipe (contrato-base, divisão de trabalho, itens de B e C), `contexto-equipe.md`, o roteiro da Pessoa D, as capturas de tela do app e as instruções e correções descritas abaixo.

### O que o autor fez

- Replanejou o próprio trabalho em duas ocasiões: em 19/10, para fazer a integração só depois das entregas individuais de todos; em 31/10, após a saída da Pessoa A, assumindo Avaliação – Consultar notas e a revisão do PR de Avaliação – Registrar.
- Definiu as regras de trabalho: branch única para a fase 2, um commit por código, nenhum commit na `main`, PRs abertos em nome dele e sem menção à IA.
- Aprovou ou ajustou cada plano antes da execução e respondeu às dúvidas sobre o comportamento real do app, com base no uso do aplicativo:
  - Guia Estudantil: o PDF sempre vem de uma URL externa, e erros de abertura são do aparelho e não voltam ao app.
  - Rádio: o app busca a semana inteira de uma vez e filtra o dia em memória; a URL do player é fixa; não há troca de dia por gesto; a nova entrada na tela refaz a chamada.
  - Tela inicial: a versão é texto fixo.
- Escolheu entre as opções de modelagem apresentadas pela IA: URL do Guia como configuração fixa; navegação em três níveis na consulta de notas; UA sem avaliação exibida como "Sem avaliações" e fora das médias; média de médias; cálculo das notas no servidor; quebra do ciclo entre os pacotes de avaliação mantendo só a dependência de entidade.
- Na revisão dos PRs #10 e #11 da Pessoa C, filtrou os achados: manteve só os bloqueantes, descartou as sugestões e a análise do registro de IA, e combinou com a Pessoa C aceitar o PR #11 e corrigir ele mesmo os bloqueantes.
- Recebeu as revisões da Pessoa B (PR #12 e problemas visuais nos diagramas de atividades) e mandou corrigir.
- Na integração, combinou com a equipe que corrigiria ele mesmo todos os achados nos arquivos de B e C, aprovou as recomendações para cada conflito, autorizou a renumeração dos casos de uso e decidiu o que ficava só como observação.
- Conferiu todos os itens produzidos e decidiu o que foi commitado, enviado e incluído nos PRs.

### O que a IA fez, sob a direção do autor

- Ajustou o roteiro local e as instruções de trabalho a cada replanejamento e montou o plano de cada código antes da execução.
- Fase 2 (D-PLN-01 e D-IND-01 a 08): redigiu a cascata do Guia Estudantil (`DCdu`, `DAtv`, `DIhc`, `DD`, `DCmp`, `DCla`, `DSeq-Guia-01` e `02`, `DEst`, `Contrato`), a da Rádio (`DCdu`, `DAtv-Radio-01` a `03`, `DIhc`, `DD`, `DCmp`, `DCla-Radio-01` e `02`, `DSeq-Radio-01` a `03`, `DEst`, `Contrato`, `ECA`), a tela inicial (`DIhc-Inicio-01` e `DEst-Inicio-01`) e o fechamento do Comum (`Contrato-Comum-01` a `04`, `ECA-Comum-01`), além das decisões correspondentes em `Docs/decisoes.md`.
- Revisões (D-REV-01 e D-REV-02): compilou os diagramas dos PRs #10 e #11, levantou os achados e redigiu os pareceres `REV-PR10` e `REV-PR11` e os textos publicados nos PRs; corrigiu o `DCla-Comum-03` apontado na revisão.
- Avaliação – Consultar notas (D-AVC-01 a 03): corrigiu os bloqueantes B1 e B2 do PR #11 nos `DAtv-AvalRegistrar-01` e `02` e redigiu a cascata completa (`DCdu`, `DAtv-AvalConsultar-01` a `03`, `DIhc-01` a `03`, `DD`, `DCmp`, `DCla-01` e `02`, `DSeq-01` a `03`, `DEst-01` a `03`, `Contrato` com as regras de cálculo R1 a R7, `ECA`), com ajustes em `AvalRegistrar` e no `DPac-Geral-01`.
- Ajustou os arquivos versionados ao replanejamento de 31/10 (D-INT-07) e aplicou as correções da revisão do PR #12 e das setas sobrepostas nos DAtv de avaliação.
- Integração (D-INT-01 a 04 e 08): redigiu o `Integracao/recebimento.md` (checagem de donos, da herança UA–Local e 12 conflitos), recomendou as soluções e aplicou as correções nos arquivos de B, C e D (incluindo os novos `DD-Seguranca-01` e `DD-AppsUFG-01`); redigiu o `DDados-Geral-01` e o `DD-Geral-01`; fechou o `DCdu-Geral-01`, o `DPac-Geral-01` e o `DImp-Geral-01`, com a renumeração dos casos de uso; montou a matriz `Integracao/rastreabilidade.md`.
- Gerou as imagens dos diagramas com o PlantUML, conferiu nomes, links e rastreabilidade por script e redigiu as mensagens de commit e os textos dos PRs.
- Os textos produzidos foram revisados e ajustados pelo autor; o que não foi confirmado no app está marcado como premissa nos READMEs de cada pasta.

### Prompts (resumo cronológico)

1. 19/10: resumir o papel da Pessoa D e o que faltava para fechar o D-DST-01.
2. 19/10: replanejar o roteiro para entregar as etapas 1 e 2 antes da integração, aprovando as mudanças propostas e respondendo às dúvidas (D-PLN-01).
3. 19/10: iniciar a fase 2 numa branch única, com um commit por código, e apresentar o plano do D-IND-01.
4. 20/10: aprovar os planos e responder às dúvidas do Guia (D-IND-01 a 03), da Rádio (D-IND-04 a 06) e da tela inicial (D-IND-07), e seguir para o fechamento do Comum (D-IND-08).
5. 20/10: recapitular a produção individual do dia.
6. 31/10: tirar os prazos fixos dos arquivos locais de apoio, mantendo só as entregas.
7. 31/10: registrar localmente a nova divisão de trabalho após a saída da Pessoa A e refazer o roteiro com checkboxes, incluindo a revisão do PR de Avaliação – Registrar e a consulta de notas.
8. 31/10: revisar os PRs #10 e #11 da Pessoa C, filtrar os achados, publicar o parecer do #10 em nome do autor e aceitar o #11 com os bloqueantes corrigidos pelo próprio autor.
9. 31/10 e 01/11: implementar D-AVC-01, 02 e 03, respondendo às perguntas de modelagem.
10. 01/11: remover a atividade D-INT-06, ajustar os arquivos versionados à nova divisão (D-INT-07), redigir e abrir o PR da produção individual em nome do autor.
11. 01/11: discutir a flexibilização da regra de registro de uso de IA combinada com o professor.
12. 02/11: corrigir os bloqueantes e as sugestões da revisão do PR #12 feita pela Pessoa B.
13. 02/11: revisar todos os diagramas e corrigir as setas sobrepostas relatadas pela Pessoa B.
14. 02/11: iniciar a fase 3 (D-INT-01), permitir a alteração dos arquivos de B e C e registrar no roteiro que o autor corrige todos os achados (D-INT-08).
15. 02/11: implementar D-INT-02, D-INT-03 (com a renumeração dos casos de uso) e D-INT-04, e preparar o texto do PR da integração.
16. 02/11: refazer este registro no formato resumido usado pela Pessoa C.

Os prompts completos, quando tiverem mais de um parágrafo, vão para o apêndice de prompts do documento final (regra 6 do enunciado).

### Referência (ABNT)

ANTHROPIC. **Claude Code**. Assistente de IA. Disponível em: https://claude.com/claude-code. Acesso em: 2 nov. 2026. Questão: Apêndice <X>, Seção <X.1>.

<!-- Preencher <X> na editoração, junto com o apêndice de prompts. -->
