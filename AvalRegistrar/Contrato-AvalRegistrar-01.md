# Contrato-AvalRegistrar-01 – Contratos das operações do pacote AvalRegistrar

| Campo | Valor |
|---|---|
| **Código** | `Contrato-AvalRegistrar-01` |
| **Título** | Contratos das operações do pacote AvalRegistrar |
| **Autor(a)** | José Eduardo Gontijo de Carvalho |
| **Revisor(a)** | Maicon Brendo da Silva (Pessoa B) |
| **Status** | Em produção |
| **Rastreia para** | `DCla-AvalRegistrar-01`, `DCla-AvalRegistrar-02`, `DCla-AvalRegistrar-03`, `DCla-AvalRegistrar-04`, `DD-AvalRegistrar-01`, `DEst-AvalRegistrar-02`, `DEst-AvalRegistrar-03`, `DSeq-AvalRegistrar-01`, `DSeq-AvalRegistrar-02`, `DSeq-AvalRegistrar-03`, `DSeq-AvalRegistrar-04`, `DSeq-AvalRegistrar-05`, `ECA-AvalRegistrar-01`, `Contrato-Comum-02`, `Contrato-Comum-03` |

## Descrição

Contrato de cada operação das classes de `DCla-AvalRegistrar-01` a `DCla-AvalRegistrar-04`: o que deve ser verdadeiro antes de chamar (pré-condição), o que passa a ser verdadeiro depois (pós-condição) e os erros possíveis. Invariantes são condições que valem para todo objeto da classe, o tempo todo. As operações privadas estão incluídas por definirem o formato da conversa com a API e o que a tela mostra. Os tipos de erro são os de `ErroApi` (`DCla-Comum-02`). As operações do Comum têm contrato em `Contrato-Comum-02` (`IAcessoApi`) e `Contrato-Comum-03` (`ControladorTelaRemota`), que aqui só são usadas.

Nas telas com conteúdo remoto, o estado "EXIBINDO" é o do controlador do Comum (`controlador.obterEstado()`), e "Enviando" é o estado da `TelaQuestionario` durante o envio (`DEst-AvalRegistrar-03`). As premissas `P-AR-n` citadas estão listadas em [`AvalRegistrar/README.md`](README.md).

### Classe TelaAvaliacao

*Invariante:* `acesso` (o `IAcessoApi` recebido no construtor) nunca é nulo.

**Tabela 1 – Contratos de TelaAvaliacao**

| Operação | Pré-condição | Pós-condição | Erros |
|---|---|---|---|
| `TelaAvaliacao(acesso)` | `acesso` não é nulo | Tela criada, guardando `acesso`; nenhuma chamada à API e nenhuma outra tela criada | – |
| `aoExibir()` | A tela está sendo exibida: entrada pelo cartão "Avaliação de UA" (P-AR-1) ou retorno da `TelaEscolherUA` (voltar) ou da `TelaConfirmacao` (concluir) | Os botões "Avaliar uma unidade" e "Ver notas" estão visíveis; nenhuma chamada à API (a tela não tem conteúdo remoto); a entrada e o retorno têm o mesmo efeito | – |
| `aoTocarAvaliar()` | A tela está exibida | `TelaEscolherUA(acesso)` foi criada e o seu `aoExibir()` foi chamado uma vez; esta tela permanece na pilha | – |
| `aoTocarConsultar()` | A tela está exibida | A tela de `AvalConsultar` foi aberta (P-AR-1); o contrato dela é de `AvalConsultar`; nenhuma chamada à API é feita por esta tela | – |
| `aoVoltar()` | – | A tela é encerrada; o app exibe a tela inicial; não há nada a descartar | – |

### Classe TelaEscolherUA

*Invariantes:* `acesso` nunca é nulo; depois do primeiro `aoExibir()`, `controlador` nunca é nulo e a tela está registrada nele uma única vez como observador; a lista mostrada é a do último estado EXIBINDO recebido.

**Tabela 2 – Contratos de TelaEscolherUA**

| Operação | Pré-condição | Pós-condição | Erros |
|---|---|---|---|
| `TelaEscolherUA(acesso)` | `acesso` não é nulo | Tela criada, guardando `acesso`; `controlador` ainda não existe; nenhuma chamada à API | – |
| `aoExibir()` | A tela está sendo exibida. *Entrada:* `controlador` ainda não existe. *Retorno* (ao voltar da `TelaQuestionario`): `controlador` existe | *Entrada:* foram criados `FonteUnidades(acesso)` e `ControladorTelaRemota<UnidadeAcademica>(fonte)`, atribuído a `controlador`; `controlador.registrarObservador(this)` e `controlador.aoEntrarNaTela()` foram chamados. *Retorno:* só `controlador.aoEntrarNaTela()` foi chamado; fonte e controlador não são recriados nem a tela é registrada de novo. Nos dois casos, `aoEntrarNaTela()` foi chamado uma vez e o estado passa por CARREGANDO (`ECA-CM-01`) | – |
| `aoEscolherUA(unidade)` | O estado é EXIBINDO e `unidade` é um dos itens de `controlador.obterDados()` | `TelaQuestionario(unidade, acesso)` foi criada e o seu `aoExibir()` foi chamado uma vez; esta tela permanece na pilha; nenhuma chamada direta à API | – |
| `aoVoltar()` | – | A tela é encerrada e a lista em memória é descartada; o app exibe a `TelaAvaliacao` (`aoExibir()` dela) | – |
| `aoMudarEstado(estado)` | O controlador acabou de mudar de estado | CARREGANDO: indicador de carregamento; EXIBINDO: lista com nome e sigla de cada UA de `controlador.obterDados()`, na ordem recebida (P-AR-25); VAZIO: mensagem de vazio; INDISPONIVEL: mensagem de indisponibilidade (P-AR-10); nenhuma chamada à API | – |

### Classe TelaQuestionario

*Invariantes:* `unidade` e `acesso` nunca são nulos; depois de `aoExibir()`, `rascunho`, `controlador` e `servicoEnvio` nunca são nulos e `rascunho` é da mesma `unidade`; `dimensaoAtual` vale 0 antes do carregamento e, no estado EXIBINDO, está entre 0 e *n* − 1, sendo *n* o número de dimensões de `controlador.obterDados()`; o rascunho só é alterado por `aoDarNota`; há no máximo um envio em curso; **a tela nunca é encerrada nem recebe outro evento com o envio em curso**: durante o estado Enviando os toques são ignorados (P-AR-27); nada do avaliador é guardado (P-AR-7).

**Tabela 3 – Contratos de TelaQuestionario**

| Operação | Pré-condição | Pós-condição | Erros |
|---|---|---|---|
| `TelaQuestionario(unidade, acesso)` | `unidade` e `acesso` não são nulos | Tela criada, guardando `unidade` e `acesso`; `dimensaoAtual` é 0; `rascunho`, `controlador` e `servicoEnvio` ainda não existem; nenhuma chamada à API | – |
| `aoExibir()` | A tela está sendo exibida pela primeira vez: `rascunho` ainda não existe. **Não há retorno a esta tela**: voltar a descarta (P-AR-8) e concluir encerra o fluxo | Foram criados `RascunhoAvaliacao(unidade)`, sem notas, `FonteQuestionario(acesso)`, `ControladorTelaRemota<DimensaoQualidade>(fonte)` (em `controlador`) e `ServicoEnvioAvaliacao(acesso)`; `controlador.registrarObservador(this)` foi chamado; `dimensaoAtual` é 0; `controlador.aoEntrarNaTela()` foi chamado uma vez (`ECA-CM-01`) | – |
| `aoDarNota(questao, valor)` | O estado é EXIBINDO e não é Enviando; `questao` pertence à dimensão exibida; `valor` é inteiro de 0 a 5 (P-AR-5; a tela só oferece essas seis opções) | `rascunho.obterNota(questao)` é `valor`, substituindo a nota anterior da questão, se havia; o destaque de pendência da questão foi removido e `mostrarDimensao()` atualizou a marca de dimensão completa ou incompleta; se a tela estava em Validação reprovada, volta a Preenchendo; nenhuma chamada à API | – |
| `aoAvancarDimensao()` | O estado é EXIBINDO e não é Enviando; `dimensaoAtual` < *n* − 1 (o botão "Próxima" não existe na última dimensão); não se exige dimensão completa (P-AR-4) | `dimensaoAtual` aumentou em 1 e `mostrarDimensao()` foi chamada; o rascunho não mudou; nenhuma chamada à API | – |
| `aoVoltarDimensao()` | O estado é EXIBINDO e não é Enviando; `dimensaoAtual` > 0 (o botão "Anterior" não existe na primeira dimensão) | `dimensaoAtual` diminuiu em 1 e `mostrarDimensao()` foi chamada; o rascunho não mudou; nenhuma chamada à API | – |
| `aoEnviar()` | O estado é EXIBINDO e não é Enviando; `dimensaoAtual` é *n* − 1 (o botão "Enviar" só existe na última dimensão) | Seja `dimensoes = controlador.obterDados()`. *Se `rascunho.estaCompleto(dimensoes)` é falso:* `marcarPendentes(rascunho.questoesPendentes(dimensoes))` foi chamada, nada foi enviado e a tela está em Validação reprovada (`UC09.4`). *Se é verdadeiro:* a tela esteve em Enviando e `servicoEnvio.enviar(rascunho.montarAvaliacao())` foi chamada uma vez; com `REGISTRADA`, `TelaConfirmacao` foi criada, o seu `aoExibir()` foi chamado, o rascunho foi descartado e esta tela foi encerrada; com `NAO_REGISTRADA`, `mostrarFalhaNoEnvio()` foi chamada e o rascunho e `dimensaoAtual` ficaram como estavam, para novo envio (P-AR-6) | – (`enviar` não lança exceção; nenhum erro chega à tela) |
| `aoVoltar()` | Não é Enviando; durante o envio o toque é ignorado (P-AR-27) | O rascunho e o controlador foram descartados, nada foi enviado (P-AR-8); a tela é encerrada e a `TelaEscolherUA` é exibida de novo (`aoExibir()` de retorno dela, que recarrega a lista) | – |
| `aoMudarEstado(estado)` | O controlador acabou de mudar de estado (o controlador só muda de estado na carga do questionário, nunca durante o envio) | CARREGANDO: indicador de carregamento; EXIBINDO: `mostrarDimensao()` foi chamada, com `dimensaoAtual` em 0 na primeira carga; VAZIO: mensagem de vazio, sem botões de nota nem de envio; INDISPONIVEL: mensagem de indisponibilidade (P-AR-10); nenhuma chamada à API | – |
| `mostrarDimensao()` (privada) | O estado é EXIBINDO; `dimensaoAtual` está entre 0 e *n* − 1 | A tela mostra o nome da UA (`unidade`), "Dimensão *k* de *n*" com *k* = `dimensaoAtual` + 1, o nome da dimensão, os elementos e, em cada um, as questões, cada uma com o seletor de nota de 0 a 5 mostrando `rascunho.obterNota(questao)`; "Anterior" só se `dimensaoAtual` > 0, "Próxima" só se `dimensaoAtual` < *n* − 1, "Enviar" só se `dimensaoAtual` = *n* − 1; destaca a dimensão como completa ou incompleta e mantém o destaque das questões pendentes sem nota; o estado não muda | – |
| `marcarPendentes(pendentes)` (privada) | `pendentes` não é vazia e só tem questões do questionário carregado | Cada questão de `pendentes` está destacada como pendente, em todas as dimensões; `dimensaoAtual` é o índice da dimensão da primeira questão pendente, na ordem do questionário (P-AR-28); `mostrarDimensao()` foi chamada; o rascunho não mudou | – |
| `mostrarFalhaNoEnvio()` (privada) | O envio terminou com `NAO_REGISTRADA` | A tela avisa que a avaliação não foi registrada e pode ser enviada de novo; as notas continuam na tela, "Enviar" está disponível e a tela está em Falha no envio (P-AR-6) | – |

### Classe TelaConfirmacao

*Invariante:* só é criada depois de uma avaliação registrada; não guarda nenhum dado da avaliação.

**Tabela 4 – Contratos de TelaConfirmacao**

| Operação | Pré-condição | Pós-condição | Erros |
|---|---|---|---|
| `TelaConfirmacao()` | O envio terminou com `REGISTRADA` | Tela criada; nenhuma chamada à API | – |
| `aoExibir()` | A tela está sendo exibida | A tela mostra "Avaliação registrada. Obrigado por contribuir!" e o botão "Concluir"; nenhuma chamada à API | – |
| `aoConcluir()` | A tela está exibida | A tela é encerrada e a `TelaAvaliacao` é exibida (`aoExibir()` dela); as telas da lista de UAs e do questionário já não estão na pilha; nada é enviado | – |

### Classe RascunhoAvaliacao

*Invariantes:* `unidade` nunca é nula; todo valor de `notas` é inteiro de 0 a 5; há no máximo uma nota por questão (a chave `idQuestao` é única no mapa); o rascunho só existe em memória e deixa de existir quando a `TelaQuestionario` é encerrada (P-AR-8); não guarda nenhum dado do avaliador (P-AR-7).

**Tabela 5 – Contratos de RascunhoAvaliacao**

| Operação | Pré-condição | Pós-condição | Erros |
|---|---|---|---|
| `RascunhoAvaliacao(unidade)` | `unidade` não é nula | Rascunho criado para `unidade`, com `notas` vazio | – |
| `definirNota(questao, valor)` | `questao` não é nula; `valor` é inteiro de 0 a 5 (P-AR-5) | `notas` tem exatamente uma entrada para `questao.id`, com `valor`, substituindo a anterior, se havia; as demais notas não mudaram | – |
| `obterNota(questao)` | `questao` não é nula | Devolve o valor guardado para `questao.id`, ou nulo se a nota não foi informada; o estado não muda | – |
| `questoesPendentes(dimensoes)` | `dimensoes` é o questionário carregado (não nula) | Devolve, na ordem do questionário (dimensão, elemento, questão), as questões de `dimensoes` sem nota; a lista é vazia se todas têm nota; o estado não muda | – |
| `estaCompleto(dimensoes)` | `dimensoes` é o questionário carregado e não é vazia | Devolve verdadeiro se, e somente se, `questoesPendentes(dimensoes)` é vazia, isto é, se toda questão tem nota; o estado não muda | – |
| `montarAvaliacao()` | O rascunho foi verificado como completo para o questionário carregado (`estaCompleto` é verdadeiro), logo `notas` não é vazio | Devolve uma `Avaliacao` com `unidade` igual à do rascunho e uma `NotaQuestao` por entrada de `notas`, em ordem crescente de `idQuestao`; cada `Questao` das notas é identificada só pelo `id` (P-AR-24); não há nenhum dado do avaliador (P-AR-7); o rascunho não muda | – |

### Classe FonteUnidades

*Invariante:* `acesso` nunca é nulo.

**Tabela 6 – Contratos de FonteUnidades**

| Operação | Pré-condição | Pós-condição | Erros |
|---|---|---|---|
| `FonteUnidades(acesso)` | `acesso` não é nulo | Fonte pronta; nenhuma chamada à API foi feita | – |
| `carregar()` | – | A API foi chamada uma vez, com `acesso.obter("/unidades-academicas", {})` (P-AR-11); devolve as unidades acadêmicas na ordem recebida (P-AR-25), possivelmente vazia; nada é guardado em cache | `ErroApi` de qualquer tipo (`SEM_CONEXAO`, `TEMPO_ESGOTADO`, `ERRO_SERVIDOR`, `RESPOSTA_INVALIDA`), repassado sem tratamento |
| `converter(corpo)` (privada) | `corpo` é o texto da resposta da API | Devolve uma `UnidadeAcademica` por item do JSON, com `id`, `nome` e `sigla` (P-AR-23), na ordem recebida | `ErroApi` `RESPOSTA_INVALIDA` se o texto não é JSON legível, se algum item não tem `id`, `nome` ou `sigla`, ou se há `id` repetido |

*Invariantes de `UnidadeAcademica` no app* (a entidade é de Maicon, `DD-Locais-01`; aqui só se exige o que `AvalRegistrar` usa): `id` é único na lista; `nome` e `sigla` não são vazios.

### Classe FonteQuestionario

*Invariante:* `acesso` (o `IAcessoApi` recebido no construtor) nunca é nulo.

**Tabela 7 – Contratos de FonteQuestionario**

| Operação | Pré-condição | Pós-condição | Erros |
|---|---|---|---|
| `FonteQuestionario(acesso)` | `acesso` não é nulo | Fonte pronta; nenhuma chamada à API foi feita | – |
| `carregar()` | – | A API foi chamada uma vez, com `acesso.obter("/avaliacao/questionario", {})` (P-AR-11), sem informar a UA, pois o questionário é o mesmo para toda UA (P-AR-9); devolve as dimensões em ordem crescente de `ordem`, cada uma com seus elementos e questões também em ordem crescente (P-AR-25), possivelmente vazia; nada é guardado em cache (P-AR-3) | `ErroApi` de qualquer tipo, repassado sem tratamento |
| `converter(corpo)` (privada) | `corpo` é o texto da resposta da API | Devolve uma `DimensaoQualidade` por item do JSON, com `id`, `nome`, `ordem` e os `elementos` e `questoes` aninhados (P-AR-23), ordenados por `ordem` (P-AR-25) | `ErroApi` `RESPOSTA_INVALIDA` se o texto não é JSON legível, se falta algum campo, se uma dimensão não tem elemento ou um elemento não tem questão, ou se há `id` repetido entre dimensões, entre elementos ou entre questões (P-AR-29) |

*Invariantes das entidades:* `DimensaoQualidade`, `ElementoEducacional` e `Questao` têm `id` único entre as do mesmo tipo e `ordem` inteira (P-AR-20), e `nome` ou `texto` não vazio; toda dimensão tem ao menos um elemento e todo elemento ao menos uma questão (`DD-AvalRegistrar-01`); as entidades não têm operações e não mudam depois de criadas.

### Classe ServicoEnvioAvaliacao

*Invariantes:* `acesso` nunca é nulo; o serviço não guarda estado entre envios (sem cache e sem nova tentativa automática); `enviar` **nunca lança exceção** e sempre devolve um `ResultadoEnvio`.

**Tabela 8 – Contratos de ServicoEnvioAvaliacao**

| Operação | Pré-condição | Pós-condição | Erros |
|---|---|---|---|
| `ServicoEnvioAvaliacao(acesso)` | `acesso` não é nulo | Serviço pronto; nenhuma chamada à API foi feita | – |
| `enviar(avaliacao)` | `avaliacao` não é nula e cumpre as invariantes de `Avaliacao` (unidade, ao menos uma nota, valores de 0 a 5, sem questão repetida) | `acesso.enviar("/avaliacoes", serializar(avaliacao))` foi chamada uma vez (P-AR-11). Devolve `REGISTRADA` se a resposta é `bemSucedida()`; devolve `NAO_REGISTRADA` se houve `ErroApi` de qualquer tipo ou se a resposta não é bem-sucedida. A `avaliacao` não mudou, nada foi guardado e não há nova tentativa. Quem tenta de novo cria, se a primeira chegou ao servidor, outra avaliação (P-AR-26) | – (o `ErroApi` é capturado aqui e vira `NAO_REGISTRADA`; não chega à tela) |
| `serializar(avaliacao)` (privada) | Como em `enviar` | Devolve um JSON não vazio com `idUnidade` (o `id` da unidade) e a lista `notas` de objetos `{idQuestao, valor}`, na ordem de `avaliacao.notas` (P-AR-23); **não contém nenhum dado do avaliador** (P-AR-7), nem identificador ou data e hora da avaliação, que o servidor atribui (P-AR-22); a `avaliacao` não muda | – |

### Entidades Avaliacao e NotaQuestao

*Invariantes de `Avaliacao`:* `unidade` nunca é nula; há ao menos uma `NotaQuestao` e, no envio completo, exatamente uma por questão do questionário carregado (P-AR-5); **nunca há duas notas para a mesma questão**; não existe nenhum atributo ou dado do avaliador (P-AR-7); depois de criada, não é alterada e, depois de registrada no servidor, não pode ser editada nem excluída (contrato-base, seção 8); `id` e data e hora do registro existem só no servidor (P-AR-22).

*Invariantes de `NotaQuestao`:* `questao` nunca é nula; `valor` é inteiro **entre 0 e 5**, inclusive (P-AR-5).

*Invariante de `ResultadoEnvio`:* só tem os valores `REGISTRADA` e `NAO_REGISTRADA`.

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 11 (Software Engineering Models and Methods). IEEE, 2024.

ANTHROPIC. **Claude Code**. Assistente de IA. Disponível em: claude.ai/code. Acesso em: 30 out. 2026. Uso: rascunho do texto e dos diagramas a partir da especificação e das instruções do autor, que revisou o conteúdo. Questão: Apêndice <X>, Seção <X.1>.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
