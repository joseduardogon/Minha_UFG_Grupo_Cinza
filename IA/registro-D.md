# Registro de uso de IA – Pessoa D

Formato de cada entrada: identificação da IA, URL, data de acesso, prompt completo e uso dado à resposta.
A referência ABNT que vai para a bibliografia aparece no fim de cada entrada.

## D-IA-01 – Planejamento da preparação do repositório (D-PRE-01)

- **IA:** Anthropic. Claude (Claude Opus 5.5). Assistente de IA.
- **URL:** claude.ai
- **Data de acesso:** 14 de outubro de 2026.
- **Contexto fornecido:** enunciado da APS (2026-2-INF0290-Definio_de_APS.pdf), contrato-base.md, contexto-equipe.md, "Roteiro de atividades pessoa D semana 1" e 17 capturas de tela do app Minha UFG v3.1.1.
- **Uso da resposta:** verificação de lacunas antes do D-PRE-01; geração da estrutura de pastas do repositório, do `Template-Item.md` e deste registro; orientação para aplicar as alterações via git bundle; definição dos atores e do rascunho do DCdu geral (D-DST-01); ajuste da seção 5 do contrato; geração do DPac e do DImp (D-DST-02) e dos componentes, classes e estados do pacote Comum (D-DST-03).

### Prompt 1

> o arquivo "roteiro de atividades pessoa D semana 1" foi escrito para eu ter um passo a passo de execução da semana 1 estratégico. ele foi pensado em primeiramente destravar o time oferecento  a base inicial para eles trabalharem, posteriormente eu fazer as minhas entregas individuais, e só depois eu unificar as entregas do time para finalizar a semana 1. tem alguma pergunta importante que você deve me fazer ou já temos tudo o suficiente para seguir com o D-PRE-01? o repositório a ser usado já foi criado.

### Prompt 2

> sobre seus pontos
>
> 1. https://github.com/joseduardogon/Minha_UFG_Grupo_Cinza/tree/main -> esse é o repositório. tá desorganizado com arquivos soltos. não está permitido commits na main, então teremos que criar branches e abrir pr (essa parte deixa comigo)
>
> 2. esqueça o prazo. foque na semana 1, estamos fazendo a semana 1.
> 3. pode ser concordo, siga assim
>
> siga em frente com a implementação da d-pre-01. se tiver algum impasse, impedimento, ou dúvida me acione para esclarecimento.

### Prompt 3

> fez push da branch para que eu consiga abrir o pr?
>
> sobre as suas escolhas, tranquilo sem problemas,
>
> sobre as decisões
>
> 1. certo faz sentido. mova para Docs/
> 2. prevalece o contrato, pois foi acordado com os partifipantes. depois converso com o time para removermos Guia_Diagramas.md

### Prompt 4

> tá, parece que você clonou o repo no seu ambiente local e fez as alterções. mas eu não tenho acesso ao seu ambiente local, como vou fazer? vou precisar clonar o repo na minha maquina e acessar com o claude code? mas como eu faria isso mantendo a configuração de projeto com todos os anexo que eu criei? me passe uma maneira de resolver esse impasse

### Prompt 5

> clonei a branch e entrei no diretório. baixei os bundles e deixei na pasta de downloads(/home/asus/Downloads). estou no ubuntu. me de a sequencia de comandos e o indicativo do que cada um faz

### Prompt 6

> [saída do terminal com os comandos git pull, git bundle verify, git fetch, git checkout, git log e git rebase, omitida]
>
> até então, tudo correto né?

### Prompt 7

> abri o pr. quando ele for aceito, finalizaremos o D-PRE-01?

### Prompt 8

> vamos seguir com D-DST-01. tem alguma decisão ou informação pendente ou não deduzível que você precisa?

### Prompt 9

> 1. não tem quinto membro. eu sou o membro D. não se preocupe com nomes, pode chamar cada um de "pessoa A, pessoa B, Pessoa C"
> 2. perfeito, mantenha o Painel web só no DImp
> 3. certo, generalize "Play Store / navegador" num ator Aplicativo externo com três especializações: Play Store, Navegador e Visualizador de PDF
>
> sobre o que você assumiu e deduziu, tá tudo correto.
>
> com isso, qual a maneira mais pratica de você me enviar a implementação? via bundle? não vou abrir o PR ainda. vou deixar para abrir um pr único com os commits relativos a D-DST-01 até D-DST-03

### Prompt 10

> diagrama ok. vamos agilizar esse processo. já me mande de uma vez o bundle completo para D-DST-02 e D-DST-03. eu reviso tudo de uma vez e se tiver alguma inconsistencia e erro te aviso e vamos ajustando. mande o bundle detalhado e completo.

### Referência (ABNT)

ANTHROPIC. **Claude**. Assistente de IA. Disponível em: claude.ai. Acesso em: 14 out. 2026. Questão: Apêndice <X>, Seção <X.1>.

<!-- Os dois prompts têm mais de um parágrafo, então vão para o apêndice de prompts. Preencher <X> na editoração. -->
