# Contrato-Noticias-01 – Contratos das operações do pacote Noticias

| Campo | Valor |
|---|---|
| **Código** | `Contrato-Noticias-01` |
| **Título** | Contratos das operações do pacote Noticias |
| **Autor(a)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Revisor(a)** | Phablo Tavares Paixão (Pessoa D) |
| **Status** | Em produção |
| **Rastreia para** | `DCla-Noticias-01`, `DCla-Noticias-02`, `DSeq-Noticias-01`, `DSeq-Noticias-02`, `DSeq-Noticias-03`, `DEst-Noticias-01`, `ECA-Noticias-01`, `DD-Noticias-01` |

## Descrição

Contrato de cada operação das classes de `DCla-Noticias-01` e `DCla-Noticias-02`: o que deve ser verdadeiro antes de chamar (pré-condição), o que passa a ser verdadeiro depois (pós-condição) e os erros possíveis. Invariantes são condições que valem para todo objeto da classe, o tempo todo. Operações privadas (`montarParametros`, `converter`) estão incluídas por definirem o formato da conversa com a API. Os tipos de erro são os de `ErroApi` (`DCla-Comum-02`).

Premissas usadas neste contrato (tabela de [`Noticias/README.md`](README.md)):

- **P-NO-1:** a regional é escolhida em uma faixa de abas que só aparece com a lista exibida (estado `EXIBINDO`); o toque em outra aba não foi observado.
- **P-NO-2:** a regional inicial é a primeira da lista `regionaisOferecidas`.
- **P-NO-3:** cada notícia tem título, endereço da página e, opcionalmente, resumo e imagem; tocar nela abre a página no Navegador.
- **P-NO-4:** o recurso da API é `GET /noticias`, com o parâmetro `regional` (identificador da regional); o nome da rota e do parâmetro não foram confirmados.
- **P-NO-5:** a lista segue a ordem devolvida pela API; o app não ordena.
- **P-NO-6:** `regionaisOferecidas` é uma lista fixa no app, entregue pelo menu inicial à tela; seu conteúdo é pendente de captura.
- **P-NO-8:** no estado `INDISPONIVEL` a tela mostra o corpo em branco, sem faixa de abas e sem mensagem (captura 31, modo avião); a barra de título continua.
- **P-NO-9:** a apresentação dos estados `CARREGANDO` e `VAZIO` não foi observada; presume-se o indicador de carregamento e a mensagem de vazio genéricos do Comum, sem a faixa de abas.

### Classe FiltroNoticias

*Invariante:* a regional selecionada nunca é nula.

**Tabela 1 – Contratos de FiltroNoticias**

| Operação | Pré-condição | Pós-condição | Erros |
|---|---|---|---|
| `FiltroNoticias(regionalInicial)` | `regionalInicial` não é nula | Regional selecionada é `regionalInicial` | – |
| `selecionarRegional(regional)` | `regional` não é nula e está entre as regionais oferecidas (garantido pela tela) | Regional selecionada é `regional` | – |
| `obterRegionalSelecionada()` | – | Devolve a regional selecionada; o estado não muda | – |

### Classe FonteNoticias

*Invariantes:* `acesso` e `filtro` nunca são nulos.

**Tabela 2 – Contratos de FonteNoticias e Noticia**

| Operação | Pré-condição | Pós-condição | Erros |
|---|---|---|---|
| `FonteNoticias(acesso, filtro)` | `acesso` e `filtro` não são nulos | Fonte pronta para carregar; nenhuma chamada à API foi feita | – |
| `carregar()` | – | A API foi chamada uma vez (`/noticias`, P-NO-4) para a regional lida do filtro; devolve as notícias recebidas, na ordem recebida (P-NO-5); a lista pode ser vazia; o filtro não é alterado | `ErroApi` de qualquer tipo (`SEM_CONEXAO`, `TEMPO_ESGOTADO`, `ERRO_SERVIDOR`, `RESPOSTA_INVALIDA`), repassado sem tratamento |
| `montarParametros()` (privada) | O filtro tem uma regional selecionada | Devolve o mapa `{regional: id da regional selecionada}`, com o identificador em texto | – |
| `converter(corpo)` (privada) | `corpo` é o texto da resposta da API | Devolve uma `Noticia` por item do JSON, na ordem recebida; `resumo` e `urlImagem` ausentes ou vazios ficam nulos | `ErroApi` `RESPOSTA_INVALIDA` se o texto não é JSON legível ou se algum item não tem `id`, `titulo` ou `url` preenchidos |

*Invariantes de Noticia:* `id` identifica a notícia e não se repete na lista; `titulo` e `url` não são vazios (toda notícia pode ser aberta no Navegador); `resumo` e `urlImagem` são opcionais. A classe não tem operações.

### Classe TelaNoticias

*Invariantes:* `regionaisOferecidas` não é vazia; `acesso` e `linkExterno` nunca são nulos; depois da primeira `aoExibir()`, `filtro` e `controlador` nunca são nulos e a regional selecionada do filtro pertence a `regionaisOferecidas`; a lista exibida é a do último estado `EXIBINDO` recebido; a faixa de abas só está visível quando o último estado recebido é `EXIBINDO`.

**Tabela 3 – Contratos de TelaNoticias**

| Operação | Pré-condição | Pós-condição | Erros |
|---|---|---|---|
| `TelaNoticias(regionaisOferecidas, acesso, linkExterno)` | `regionaisOferecidas` não é vazia; `acesso` e `linkExterno` não são nulos | Tela pronta; filtro, fonte e controlador ainda não foram criados; nenhuma chamada à API foi feita. O menu inicial cria uma tela nova a cada toque no cartão Notícias | – |
| `aoExibir()` | A tela está sendo exibida (primeira vez ou retorno do Navegador) | **Entrada pelo menu (primeira exibição, ainda sem controlador):** criou o `FiltroNoticias` com a primeira regional de `regionaisOferecidas` (P-NO-2), a `FonteNoticias(acesso, filtro)` e o `ControladorTelaRemota<Noticia>(fonte)`, e se registrou com `controlador.registrarObservador(this)`; **retorno do Navegador (controlador já existe):** nada foi criado e a regional selecionada foi mantida. Nos dois casos, `controlador.aoEntrarNaTela()` foi chamado uma vez | – |
| `aoEscolherRegional(regional)` | `aoExibir()` já foi chamado; o estado do controlador é `EXIBINDO` (a faixa de abas só aparece nele, P-NO-1); `regional` está entre `regionaisOferecidas` | `filtro.selecionarRegional(regional)` e `controlador.recarregar()` foram chamados, nessa ordem, uma vez cada | – |
| `aoTocarNoticia(noticia)` | O estado é `EXIBINDO` e `noticia` está na lista exibida | `linkExterno.abrirUrl(noticia.url)` foi chamado uma vez e o resultado é descartado; o estado do controlador não muda; nenhuma chamada à API | – |
| `aoVoltar()` | – | A tela foi encerrada: filtro, controlador e notícias em memória foram descartados; o app exibe o menu inicial | – |
| `aoMudarEstado(estado)` | O `estado` é o do controlador registrado | `CARREGANDO`: mostra o indicador de carregamento, sem a faixa de abas (P-NO-9); `EXIBINDO`: mostra a faixa de abas, com a regional selecionada sublinhada, e um cartão (imagem, título e resumo) por notícia de `controlador.obterDados()`; faixa e lista rolam juntas; `VAZIO`: mostra a mensagem de vazio, sem a faixa de abas (P-NO-9); `INDISPONIVEL`: mostra a tela em branco, sem a faixa de abas e sem mensagem (P-NO-8). Em todos, a barra de título, com a seta de voltar, continua fixa | – |

O estado `INDISPONIVEL` foi observado só em modo avião (`SEM_CONEXAO`); presume-se a mesma tela para os outros tipos de `ErroApi`, que o controlador do Comum trata do mesmo modo (`DEst-Comum-01`). O estado `VAZIO` não foi capturado e segue o ciclo genérico do Comum.

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 11 (Software Engineering Models and Methods). IEEE, 2024.

ANTHROPIC. **Claude Code**. Assistente de IA. Disponível em: claude.ai/code. Acesso em: 30 out. 2026. Uso: apoio à redação e aos diagramas, a partir das instruções, das capturas de tela e das correções do autor (resumo em `IA/registro-C.md`). Questão: Apêndice <X>, Seção <X.1>.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
