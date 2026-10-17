# Contrato-Eventos-01 – Contratos das operações do pacote Eventos

| Campo | Valor |
|---|---|
| **Código** | `Contrato-Eventos-01` |
| **Título** | Contratos das operações do pacote Eventos |
| **Autor(a)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Revisor(a)** | Phablo Tavares Paixão (Pessoa D) |
| **Status** | Em produção (primeira versão) |
| **Rastreia para** | `DCla-Eventos-01`, `DCla-Eventos-02`, `DSeq-Eventos-01`, `DSeq-Eventos-05`, `ECA-Eventos-01` |

## Descrição

Contrato de cada operação das classes de `DCla-Eventos-01` e `DCla-Eventos-02`: o que deve ser verdadeiro antes de chamar (pré-condição), o que passa a ser verdadeiro depois (pós-condição) e os erros possíveis. Invariantes são condições que valem para todo objeto da classe, o tempo todo. Operações privadas (`montarParametros`, `converter`) estão incluídas por definirem o formato da conversa com a API. Os tipos de erro são os de `ErroApi` (`DCla-Comum-02`).

### Classe CalendarioEventos

*Invariantes:* a regional selecionada nunca é nula; a data selecionada pertence sempre ao mês exibido; o mês exibido é representado pelo seu primeiro dia.

**Tabela 1 – Contratos de CalendarioEventos**

| Operação | Pré-condição | Pós-condição | Erros |
|---|---|---|---|
| `CalendarioEventos(hoje, regionalInicial)` | `regionalInicial` não é nula | Mês exibido é o mês de `hoje`; data selecionada é `hoje`; regional selecionada é `regionalInicial` | – |
| `trocarMes(deslocamento)` | `deslocamento` é -1 ou +1 | Mês exibido avançou ou recuou um mês; data selecionada é o primeiro dia do novo mês (P-EV-3); regional inalterada | – |
| `selecionarData(data)` | `data` pertence ao mês exibido | Data selecionada é `data`; mês exibido e regional inalterados | – |
| `selecionarRegional(regional)` | `regional` não é nula e está entre as regionais oferecidas | Regional selecionada é `regional`; mês e data inalterados | – |
| `obterDiasDoMes()` | – | Devolve, em ordem crescente, todas as datas do mês exibido (28 a 31); o estado não muda | – |
| `obterMesExibido()`, `obterDataSelecionada()`, `obterRegionalSelecionada()` | – | Devolve o valor atual; o estado não muda | – |

### Classe FonteEventos

*Invariantes:* `acesso` e `filtro` nunca são nulos.

**Tabela 2 – Contratos de FonteEventos e Evento**

| Operação | Pré-condição | Pós-condição | Erros |
|---|---|---|---|
| `FonteEventos(acesso, filtro)` | `acesso` e `filtro` não são nulos | Fonte pronta para carregar; nenhuma chamada à API foi feita | – |
| `carregar()` | – | Devolve a lista de eventos retornados pela API para a regional e a data lidas do filtro; a lista pode ser vazia; o filtro não é alterado; a API é chamada uma vez | `ErroApi` de qualquer tipo (`SEM_CONEXAO`, `TEMPO_ESGOTADO`, `ERRO_SERVIDOR`, `RESPOSTA_INVALIDA`), repassado sem tratamento |
| `montarParametros()` (privada) | O filtro tem data e regional | Devolve o mapa `{regional: id da regional, data: aaaa-mm-dd}` | – |
| `converter(corpo)` (privada) | `corpo` é o texto da resposta da API | Devolve um `Evento` por item do JSON, na ordem recebida | `ErroApi` `RESPOSTA_INVALIDA` se o texto não é JSON legível ou se algum evento tem `dataFim` anterior a `dataInicio` |
| `Evento.temUrl()` | – | Devolve verdadeiro se `url` não é nula nem vazia; o estado não muda | – |

*Invariante de Evento:* `dataFim` é igual ou posterior a `dataInicio`; `titulo` não é vazio.

### Classe TelaEventos

*Invariantes:* a tela sempre tem um controlador de estados e um calendário; a lista exibida é a do último estado `EXIBINDO` recebido.

**Tabela 3 – Contratos de TelaEventos**

| Operação | Pré-condição | Pós-condição | Erros |
|---|---|---|---|
| `aoExibir()` | A tela está sendo exibida (primeira vez ou retorno) | `controlador.aoEntrarNaTela()` foi chamado uma vez | – |
| `aoEscolherData(data)` | `data` pertence ao mês exibido | `calendario.selecionarData(data)` e `controlador.recarregar()` foram chamados, nessa ordem | – |
| `aoEscolherRegional(regional)` | `regional` está entre as regionais oferecidas | `calendario.selecionarRegional(regional)` e `controlador.recarregar()` foram chamados, nessa ordem | – |
| `aoTrocarMes(deslocamento)` | `deslocamento` é -1 ou +1 | `calendario.trocarMes(deslocamento)` e `controlador.recarregar()` foram chamados, nessa ordem | – |
| `aoTocarEvento(evento)` | `evento` está na lista exibida | Se `evento.temUrl()`, `linkExterno.abrirUrl(evento.url)` foi chamado uma vez e o resultado é descartado; senão, nada acontece. O estado do controlador não muda | – |
| `aoMudarEstado(estado)` | – | `CARREGANDO`: mostra o indicador de carregamento; `EXIBINDO`: mostra a lista; `VAZIO`: mostra a mensagem de "sem eventos"; `INDISPONIVEL`: mostra a mensagem de indisponibilidade | – |

As premissas `P-EV-n` citadas estão listadas, com o que falta confirmar nas capturas de tela do app, em [`Eventos/README.md`](README.md).

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 11 (Software Engineering Models and Methods). IEEE, 2024.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
