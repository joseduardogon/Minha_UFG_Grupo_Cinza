# Contrato-Eventos-01 – Contratos das operações do pacote Eventos

| Campo | Valor |
|---|---|
| **Código** | `Contrato-Eventos-01` |
| **Título** | Contratos das operações do pacote Eventos |
| **Autor(a)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Revisor(a)** | Phablo Tavares Paixão (Pessoa D) |
| **Status** | Em produção |
| **Rastreia para** | `DCla-Eventos-01`, `DCla-Eventos-02`, `DSeq-Eventos-01`, `DSeq-Eventos-02`, `DSeq-Eventos-03`, `DSeq-Eventos-04`, `DSeq-Eventos-05`, `ECA-Eventos-01`, `Contrato-Comum-01`, `Contrato-Comum-02`, `Contrato-Comum-03` |

## Descrição

Contrato de cada operação das classes de `DCla-Eventos-01` e `DCla-Eventos-02`: o que deve ser verdadeiro antes de chamar (pré-condição), o que passa a ser verdadeiro depois (pós-condição) e os erros possíveis. Invariantes são condições que valem para todo objeto da classe, o tempo todo. Operações privadas (`montarParametros`, `converter`) estão incluídas por definirem o formato da conversa com a API. Os tipos de erro são os de `ErroApi` (`DCla-Comum-02`). As operações do pacote Comum que a tela usa têm contrato nos itens do Comum: `ILinkExterno.abrirUrl` em `Contrato-Comum-01`, `IAcessoApi.obter` em `Contrato-Comum-02` e `IControladorTelaRemota` (`aoEntrarNaTela`, `recarregar`, `obterEstado`, `obterDados`, `registrarObservador`) em `Contrato-Comum-03`.

A tela de lista de Eventos foi capturada na versão 3.2.0 (capturas 19, 28 e 29), mas nem tudo o que os contratos afirmam foi observado. A situação de cada premissa está na tabela de [`Eventos/README.md`](README.md); as usadas aqui são:

- **P-EV-1** (confirmada): o cartão do evento mostra miniatura, título e período; não mostra local.
- **P-EV-2** (parcial): a regional é escolhida em abas, só "GOIÂNIA" foi vista; a lista de regionais é fixa no app e a regional inicial é a primeira da lista (não observado).
- **P-EV-3** (refutada): a premissa antiga de selecionar o dia 1 ao trocar o mês foi substituída por P-EV-7 e P-EV-8.
- **P-EV-4** (pendente): tocar em um evento com endereço abre a página dele no Navegador; sem endereço, o toque não tem efeito.
- **P-EV-5** (não observável): a API tem a rota `GET /eventos`, com os parâmetros `regional` (identificador) e `data` (aaaa-mm-dd), e devolve os eventos cujo período inclui a data, com o endereço da miniatura.
- **P-EV-6** (confirmada): ao abrir a tela pelo menu, a data selecionada é hoje.
- **P-EV-7** (confirmada): ao trocar o mês, o número do dia selecionado é mantido.
- **P-EV-8** (pendente): se o novo mês é mais curto que o dia selecionado, a data passa a ser o último dia do mês.
- **P-EV-10** (confirmada): sem eventos, a tela mostra "Sem eventos" e "Não há eventos para esse dia!", com o calendário visível e a faixa de abas de regional oculta.
- **P-EV-11** (pendente): o estado indisponível de Eventos não foi capturado; supõe-se calendário visível e faixa de abas oculta.
- **P-EV-12** (pendente): tocar em um dia seleciona-o e a lista passa a mostrar os eventos dele.
- **P-EV-13** (não observável): a lista é recarregada da API a cada troca de mês, de dia ou de regional.
- **P-EV-14** (pendente): a ordem da lista é a recebida da API.

### Classe Regional

*Invariantes:* `id` é positivo; `nome` não é vazio e é único entre as regionais. A classe não tem operações.

### Interface IFiltroEventos

*Invariantes:* `obterDataSelecionada()` e `obterRegionalSelecionada()` nunca devolvem nulo; ler o filtro não o altera. Quem lê (a `FonteEventos`) nunca o modifica. As operações são implementadas por `CalendarioEventos`, na Tabela 1.

### Classe CalendarioEventos

*Invariantes:* a regional selecionada nunca é nula; a data selecionada pertence sempre ao mês exibido; o mês exibido é representado pelo seu primeiro dia.

**Tabela 1 – Contratos de CalendarioEventos**

| Operação | Pré-condição | Pós-condição | Erros |
|---|---|---|---|
| `CalendarioEventos(hoje, regionalInicial)` | `hoje` e `regionalInicial` não são nulos | Mês exibido é o mês de `hoje`; data selecionada é `hoje` (P-EV-6); regional selecionada é `regionalInicial` | – |
| `trocarMes(deslocamento)` | `deslocamento` é -1 ou +1 | Mês exibido avançou ou recuou um mês. A data selecionada **mantém o número do dia** no novo mês (P-EV-7: 30/10 passa a 30/11 e depois a 30/12); se o novo mês tem menos dias que o número do dia, a data selecionada é o **último dia do novo mês** (P-EV-8, não observado). Isso corrige a premissa antiga P-EV-3, que selecionava o dia 1. A regional fica inalterada | – |
| `selecionarData(data)` | `data` pertence ao mês exibido | Data selecionada é `data`; mês exibido e regional inalterados | – |
| `selecionarRegional(regional)` | `regional` não é nula | Regional selecionada é `regional`; mês e data inalterados. A tela garante que `regional` está entre as oferecidas (`TelaEventos.aoEscolherRegional`) | – |
| `obterDiasDoMes()` | – | Devolve, em ordem crescente, todas as datas do mês exibido (28 a 31); o estado não muda | – |
| `obterMesExibido()`, `obterDataSelecionada()`, `obterRegionalSelecionada()` | – | Devolve o valor atual; o estado não muda | – |

### Classe FonteEventos

*Invariantes:* `acesso` e `filtro` nunca são nulos.

**Tabela 2 – Contratos de FonteEventos**

| Operação | Pré-condição | Pós-condição | Erros |
|---|---|---|---|
| `FonteEventos(acesso, filtro)` | `acesso` e `filtro` não são nulos | Fonte pronta para carregar; nenhuma chamada à API foi feita | – |
| `carregar()` | – | A API foi chamada uma vez, na rota `/eventos` (P-EV-5), com a regional e a data lidas do filtro; devolve os eventos retornados, na ordem recebida (P-EV-14), e a lista pode ser vazia; o filtro não é alterado | `ErroApi` de qualquer tipo (`SEM_CONEXAO`, `TEMPO_ESGOTADO`, `ERRO_SERVIDOR`, `RESPOSTA_INVALIDA`), repassado sem tratamento |
| `montarParametros()` (privada) | O filtro tem data e regional | Devolve o mapa `{regional: id da regional, data: aaaa-mm-dd}` (P-EV-5) | – |
| `converter(corpo)` (privada) | `corpo` é o texto da resposta da API | Devolve um `Evento` por item do JSON, na ordem recebida, com `url` e `urlImagem` nulas quando o item não as traz | `ErroApi` `RESPOSTA_INVALIDA` se o texto não é JSON legível, se algum evento tem `titulo` vazio ou se algum tem `dataFim` anterior a `dataInicio` |

### Classe Evento

*Invariantes:* `titulo` não é vazio; `dataFim` é igual ou posterior a `dataInicio`; `idRegional` referencia uma regional existente; `url` é nula ou texto (um endereço vazio equivale a nenhum); `urlImagem` é nula ou texto (miniatura mostrada no cartão, P-EV-1). O local do evento não faz parte do objeto.

**Tabela 3 – Contratos de Evento**

| Operação | Pré-condição | Pós-condição | Erros |
|---|---|---|---|
| `temUrl()` | – | Devolve verdadeiro se `url` não é nula nem vazia (P-EV-4); o estado não muda | – |

### Classe TelaEventos

*Invariantes:* `regionaisOferecidas` nunca é nula nem vazia; `acesso` e `linkExterno` nunca são nulos; depois da primeira exibição a tela sempre tem um calendário e um controlador de estados; a lista exibida é a do último estado `EXIBINDO` recebido.

**Tabela 4 – Contratos de TelaEventos**

| Operação | Pré-condição | Pós-condição | Erros |
|---|---|---|---|
| `TelaEventos(regionaisOferecidas, acesso, linkExterno)` | `regionaisOferecidas` não é nula nem vazia, sem repetições (P-EV-2); `acesso` e `linkExterno` não são nulos | A tela guarda os três argumentos. **O `CalendarioEventos`, a `FonteEventos` e o controlador ainda não foram criados:** são criados em `aoExibir()` na primeira exibição. Nenhuma chamada à API nem ao controlador. A tela é criada pelo menu inicial a cada toque no cartão Eventos | – |
| `aoExibir()` | A tela está sendo exibida (entrada pelo menu inicial ou retorno do Navegador) | **Entrada pelo menu (primeira chamada da instância):** criou, nesta ordem, `CalendarioEventos(hoje, regionaisOferecidas[0])` (filtro reiniciado: data de hoje e primeira regional, P-EV-2 e P-EV-6), a `FonteEventos(acesso, calendario)` e o `ControladorTelaRemota<Evento>(fonte)`, e registrou a tela como observador do controlador (`registrarObservador(this)`). **Retorno do Navegador:** o calendário, o controlador e o registro foram mantidos, e o filtro (mês, data e regional) é o mesmo de antes. **Nos dois casos:** `controlador.aoEntrarNaTela()` foi chamado uma vez, depois do registro | – |
| `aoEscolherData(data)` | `data` pertence ao mês exibido; o estado é qualquer um de resultado (o calendário é visível também sem eventos, P-EV-10) | `calendario.selecionarData(data)` e `controlador.recarregar()` foram chamados, nessa ordem (P-EV-12 e P-EV-13); a regional é a mesma | – |
| `aoEscolherRegional(regional)` | `regional` está entre `regionaisOferecidas`; o estado do controlador é `EXIBINDO`, único em que a faixa de abas é mostrada (P-EV-2 e P-EV-10) | `calendario.selecionarRegional(regional)` e `controlador.recarregar()` foram chamados, nessa ordem; a data é a mesma | – |
| `aoTrocarMes(deslocamento)` | `deslocamento` é -1 ou +1; o estado é qualquer um de resultado | `calendario.trocarMes(deslocamento)` e `controlador.recarregar()` foram chamados, nessa ordem (P-EV-13); a data selecionada é a definida por `trocarMes` (mesmo número do dia, P-EV-7 e P-EV-8) | – |
| `aoTocarEvento(evento)` | `evento` está na lista exibida | Se `evento.temUrl()`, `linkExterno.abrirUrl(evento.url)` foi chamado uma vez e o resultado é descartado; senão, nada acontece (P-EV-4). O estado do controlador e o filtro não mudam | – |
| `aoVoltar()` | – | A tela é encerrada: o calendário (filtro) e os eventos em memória do controlador são descartados e o app exibe o menu inicial. Nenhuma chamada à API. Uma nova entrada pelo menu cria uma tela nova, com o filtro reiniciado | – |
| `aoMudarEstado(estado)` | – | `CARREGANDO`: mostra o indicador de carregamento; `EXIBINDO`: mostra a lista `controlador.obterDados()` (cartões com miniatura, título e período) e a faixa de abas de regional; `VAZIO`: mostra a ilustração, "Sem eventos" e "Não há eventos para esse dia!", com o calendário visível e a faixa de abas oculta (P-EV-10); `INDISPONIVEL`: mostra a mensagem de indisponibilidade, com o calendário visível e a faixa de abas oculta (P-EV-11, não observado) | – |

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 11 (Software Engineering Models and Methods). IEEE, 2024.

ANTHROPIC. **Claude Code**. Assistente de IA. Disponível em: claude.ai/code. Acesso em: 30 out. 2026. Uso: apoio à redação e aos diagramas, a partir das instruções, das capturas de tela e das correções do autor (resumo em `IA/registro-C.md`). Questão: Apêndice <X>, Seção <X.1>.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
