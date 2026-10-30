# Contrato-RU-01 – Contratos das operações do pacote RU

| Campo | Valor |
|---|---|
| **Código** | `Contrato-RU-01` |
| **Título** | Contratos das operações do pacote RU |
| **Autor(a)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Revisor(a)** | Phablo Tavares Paixão (Pessoa D) |
| **Status** | Em produção |
| **Rastreia para** | `DCla-RU-01`, `DCla-RU-02`, `DD-RU-01`, `DSeq-RU-01`, `DSeq-RU-02`, `DEst-RU-01`, `DEst-RU-02`, `ECA-RU-01` |

## Descrição

Contrato de cada operação das classes de `DCla-RU-01` e `DCla-RU-02`: o que deve ser verdadeiro antes de chamar (pré-condição), o que passa a ser verdadeiro depois (pós-condição) e os erros possíveis. Invariantes são condições que valem para todo objeto da classe, o tempo todo. Operações privadas estão incluídas por definirem o que a tela mostra e o formato da conversa com a API. Os tipos de erro são os de `ErroApi` (`DCla-Comum-02`); o controlador do Comum trata o `ErroApi` e ele não chega à tela (`Contrato-Comum-03`). As operações do controlador e do observador são as do Comum e têm contrato em `Contrato-Comum-03`.

Premissas usadas:

- **P-RU-1:** o RU tem três refeições: Café da Manhã, Almoço e Jantar (confirmada).
- **P-RU-2:** a tela RU é estática (não consulta o servidor).
- **P-RU-3:** ao abrir a tela da refeição, uma só chamada traz a semana inteira da refeição; trocar o dia filtra os dados em memória, sem chamada à API (confirmada pelo autor).
- **P-RU-4:** o seletor vai de segunda a sábado no Café da Manhã e no Almoço (seis datas) e de segunda a sexta no Jantar (cinco datas); não há letra para domingo (confirmada). O Jantar não tem refeição em sábado.
- **P-RU-5:** os itens são agrupados em cartões por categoria; categorias do Café da Manhã e do Almoço e Jantar (confirmada).
- **P-RU-6:** o separador " / " entre os itens da mesma categoria, se a categoria tem mais de um item, não foi confirmado; categorias abaixo de "Guarnição" não foram vistas.
- **P-RU-7:** a barra e o fundo da tela têm a cor do dia selecionado: terça roxo, quarta vermelho, quinta laranja, sexta verde, sábado marrom (confirmada).
- **P-RU-8:** no estado indisponível, a tela mostra barra azul, ilustração e "Cardápio indisponível.", sem data nem seletor (confirmada).
- **P-RU-9:** os estados vazio e carregando e o dia sem itens não foram observados: o vazio usa a mensagem genérica do Comum; Carregando e Vazio supõem o mesmo layout do estado indisponível; o dia sem itens mantém cabeçalho e seletor.
- **P-RU-10:** a rota é `GET /cardapio`, com o parâmetro `refeicao` (`CAFE_DA_MANHA`, `ALMOCO` ou `JANTAR`), sem data, e a resposta é um JSON com as refeições da semana, cada uma com a sua data e os seus itens, cada item com a sua categoria.
- **P-RU-11:** a seta de voltar da tela da refeição leva à tela RU, e a da tela RU leva ao menu inicial.
- **P-RU-12:** a cor da segunda-feira (azul) é inferida pela cor da letra do seletor.
- **P-RU-13:** quando hoje não tem letra no seletor (domingo, ou sábado no Jantar), a tela seleciona a segunda-feira da semana que contém hoje (segunda a domingo).

### Classe TelaRU

*Invariante:* `acesso` nunca é nulo.

**Tabela 1 – Contratos de TelaRU**

| Operação | Pré-condição | Pós-condição | Erros |
|---|---|---|---|
| `TelaRU(acesso)` | `acesso` não é nulo | Tela pronta; nenhuma chamada à API foi feita | – |
| `aoExibir()` | A tela está sendo exibida (entrada pelo menu inicial ou retorno da tela da refeição) | Mostra a seta de voltar, o título "RU", os cartões Café da Manhã, Almoço e Jantar e o aviso "Cardápio sujeito a alterações!"; nenhuma chamada à API (P-RU-1, P-RU-2) | – |
| `aoTocarRefeicao(tipo)` | `tipo` não é nulo | Foi criada uma `TelaRefeicao(tipo, hoje, acesso)`, em que `hoje` é a data atual do aparelho, e a nova tela foi exibida (`aoExibir()` chamado uma vez nela); a `TelaRU` fica sob a nova tela; nenhuma chamada à API foi feita pela `TelaRU` | – |
| `aoVoltar()` | – | A tela é encerrada e o app exibe o menu inicial (P-RU-11) | – |

### Classe TelaRefeicao

*Invariantes:* `tipoRefeicao`, `hoje` e `acesso` nunca são nulos; `selecao` e `controlador` são ambos nulos até a primeira chamada de `aoExibir()` e, depois dela, nunca mais são nulos; depois da primeira `aoExibir()`, a tela é observadora do `controlador` e `diaSelecionado` está em `diasDisponiveis(tipoRefeicao)`; o título mostrado é o nome da refeição ("Café da Manhã", "Almoço" ou "Jantar").

**Tabela 2 – Contratos de TelaRefeicao**

| Operação | Pré-condição | Pós-condição | Erros |
|---|---|---|---|
| `TelaRefeicao(tipo, hoje, acesso)` | `tipo`, `hoje` e `acesso` não são nulos | `tipoRefeicao`, `hoje` e `acesso` guardados; `selecao`, `controlador` e `diaSelecionado` ainda nulos; nenhuma chamada à API foi feita | – |
| `aoExibir()` | A tela está sendo exibida: entrada (primeira chamada, logo após a criação, com `controlador` nulo) ou retorno ao app (`controlador` já criado) | **Entrada:** foram criados `SelecaoCardapio(tipoRefeicao)`, `FonteCardapio(acesso, selecao)` e `ControladorTelaRemota<Refeicao>(fonte)`, a tela se registrou como observador (`registrarObservador`), `diaSelecionado` é `diaInicial()` e `controlador.aoEntrarNaTela()` foi chamado uma vez. **Retorno:** nada foi criado, `diaSelecionado` e `selecao` são mantidos e `controlador.aoEntrarNaTela()` foi chamado uma vez, o que recarrega a semana (`ECA-RU-01`). Nos dois casos, a tela só desenha o cabeçalho e o cardápio pelo `aoMudarEstado` que o controlador notifica | – |
| `aoEscolherDia(dia)` | `dia` está em `diasDisponiveis(tipoRefeicao)`; o estado do controlador é EXIBINDO (o seletor só aparece nesse estado: P-RU-8, P-RU-9) | `diaSelecionado` é `dia`; `mostrarCabecalho()` e `mostrarCardapioDoDia()` foram chamados, nessa ordem. **Nenhuma chamada à API:** `fonte.carregar()`, `controlador.recarregar()` e `controlador.aoEntrarNaTela()` não foram chamados; o estado do controlador continua EXIBINDO e a semana em memória não mudou (P-RU-3) | – |
| `aoVoltar()` | – | A tela é encerrada; `selecao`, `controlador` e a semana em memória são descartados; o app exibe a tela RU (P-RU-11) | – |
| `aoMudarEstado(estado)` | O estado notificado é o `controlador.obterEstado()` | CARREGANDO: barra azul, título e indicador de carregamento; EXIBINDO: `mostrarCabecalho()` e `mostrarCardapioDoDia()`; VAZIO: barra azul, título e mensagem de vazio; INDISPONIVEL: barra azul, título, ilustração e a mensagem "Cardápio indisponível.". Em CARREGANDO, VAZIO e INDISPONIVEL não há data nem seletor (P-RU-8, P-RU-9) | – |
| `diasDisponiveis(tipo)` (privada) | `tipo` não é nulo | Devolve, em ordem crescente, as datas da semana (segunda a domingo) que contém `hoje`: de segunda a sábado (seis datas) se `tipo` é CAFE_DA_MANHA ou ALMOCO, e de segunda a sexta (cinco datas) se é JANTAR; nunca há domingo, e nunca há sábado no Jantar (P-RU-4); o estado não muda | – |
| `diaInicial()` (privada) | – | Devolve `hoje` se `hoje` está em `diasDisponiveis(tipoRefeicao)`; caso contrário (domingo, ou sábado no Jantar), devolve a segunda-feira, o primeiro elemento de `diasDisponiveis(tipoRefeicao)` (P-RU-13); o estado não muda | – |
| `mostrarCabecalho()` (privada) | O estado do controlador é EXIBINDO e `diaSelecionado` não é nulo | Mostra a seta de voltar, o nome da refeição, a barra e o fundo na cor `corDoDia(diaSelecionado)`, `dataPorExtenso(diaSelecionado)` e, para cada data de `diasDisponiveis(tipoRefeicao)`, um círculo com `letraDoDia(dia)`, destacado se e somente se `dia` é `diaSelecionado`; o estado não muda | – |
| `mostrarCardapioDoDia()` (privada) | O estado do controlador é EXIBINDO e `diaSelecionado` não é nulo | Seja `r` o resultado de `refeicaoDoDia(diaSelecionado)`: se `r` existe e tem itens, mostra um cartão para cada grupo de `agruparPorCategoria(r.itens)`, com o nome da categoria e as descrições dos itens separadas por " / " (P-RU-6); senão, mostra a mensagem de vazio (P-RU-9). Nenhuma chamada à API; o estado não muda | – |
| `refeicaoDoDia(dia)` (privada) | O estado do controlador é EXIBINDO | Devolve a `Refeicao` de `controlador.obterDados()` cuja `data` é `dia`, ou nulo se a semana não tem refeição nessa data; o estado não muda | – |
| `agruparPorCategoria(itens)` (privada) | `itens` não é nula | Devolve um mapa com uma entrada para cada categoria presente em `itens`, na ordem em que aparecem pela primeira vez; cada entrada traz os itens dessa categoria, na ordem recebida; todo item está em exatamente uma entrada; o estado não muda | – |
| `diaDaSemana(data)` (privada) | `data` não é nula | Devolve de 1 (segunda-feira) a 7 (domingo), conforme o dia da semana de `data`; o estado não muda | – |
| `letraDoDia(dia)` (privada) | `dia` está em `diasDisponiveis(tipoRefeicao)` | Devolve "S" para segunda-feira, "T" para terça, "Q" para quarta, "Q" para quinta, "S" para sexta e "S" para sábado, conforme `diaDaSemana(dia)` (P-RU-4); o estado não muda | – |
| `corDoDia(dia)` (privada) | `dia` está em `diasDisponiveis(tipoRefeicao)` | Devolve o nome da cor do dia: "azul" para segunda-feira (P-RU-12), "roxo" para terça, "vermelho" para quarta, "laranja" para quinta, "verde" para sexta e "marrom" para sábado (P-RU-7), conforme `diaDaSemana(dia)`; o estado não muda | – |
| `dataPorExtenso(data)` (privada) | `data` não é nula | Devolve o dia da semana, a vírgula, o dia do mês, o mês e o ano, em português, como em "Terça-feira, 27 de outubro de 2026" (nomes: Segunda-feira, Terça-feira, Quarta-feira, Quinta-feira, Sexta-feira, Sábado, Domingo; mês em minúsculas); o estado não muda | – |

### Interface IFiltroCardapio e classe SelecaoCardapio

*Invariante de SelecaoCardapio:* `tipoRefeicao` nunca é nulo e nunca muda depois da criação. A interface `IFiltroCardapio` só tem `obterTipoRefeicao()`; a data nunca é informada à fonte.

**Tabela 3 – Contratos de SelecaoCardapio (implementa IFiltroCardapio)**

| Operação | Pré-condição | Pós-condição | Erros |
|---|---|---|---|
| `SelecaoCardapio(tipo)` | `tipo` não é nulo | `tipoRefeicao` é `tipo` | – |
| `obterTipoRefeicao()` | – | Devolve `tipoRefeicao`; o estado não muda | – |

### Classe FonteCardapio (implementa IFonteDados&lt;Refeicao&gt;)

*Invariantes:* `acesso` e `filtro` nunca são nulos.

**Tabela 4 – Contratos de FonteCardapio**

| Operação | Pré-condição | Pós-condição | Erros |
|---|---|---|---|
| `FonteCardapio(acesso, filtro)` | `acesso` e `filtro` não são nulos | Fonte pronta para carregar; nenhuma chamada à API foi feita | – |
| `carregar()` | – | A API foi chamada uma vez (`/cardapio`, P-RU-10) apenas com a refeição lida do filtro; devolve as refeições da semana inteira dessa refeição, uma para cada data, na ordem recebida, todas com o tipo do filtro e cada uma com os seus itens; a lista pode ser vazia (semana sem refeições); o filtro não é alterado | `ErroApi` de qualquer tipo (`SEM_CONEXAO`, `TEMPO_ESGOTADO`, `ERRO_SERVIDOR`, `RESPOSTA_INVALIDA`), repassado sem tratamento |
| `montarParametros()` (privada) | O filtro tem refeição | Devolve o mapa `{refeicao: nome do valor de TipoRefeicao}`, sem data (P-RU-10) | – |
| `converter(corpo)` (privada) | `corpo` é o texto da resposta da API | Devolve uma `Refeicao` por refeição do JSON, na ordem recebida, com o tipo do filtro e a data recebida, cada uma com os seus `ItemCardapio`, e cada item associado à sua `CategoriaItem` (categorias de mesmo nome, em toda a resposta, são um só objeto) | `ErroApi` `RESPOSTA_INVALIDA` se o texto não é JSON legível, se alguma refeição não tem data ou repete a data de outra, ou se algum item não tem descrição ou categoria |

### Entidades (`DD-RU-01`)

Invariantes das entidades; elas não têm operações, só atributos e associações.

- **Cardapio:** `dataFim` é igual ou posterior a `dataInicio`. A fonte não instancia `Cardapio` (P-RU-10).
- **Refeicao:** `tipo` e `data` não são nulos; a combinação `tipo` e `data` é única. **Se `tipo` é JANTAR, a `data` não cai em sábado** (o Jantar não tem sábado: P-RU-4, confirmada na captura 26); por isso `diasDisponiveis(JANTAR)` não tem sábado. Uma `Refeicao` criada pela fonte não tem `Cardapio` associado.
- **ItemCardapio:** `descricao` não é vazia (pode trazer marcador, como "(1ª)"); tem exatamente uma `CategoriaItem` e pertence a uma `Refeicao`.
- **CategoriaItem:** `nome` não é vazio.
- **TipoRefeicao:** só admite `CAFE_DA_MANHA`, `ALMOCO` e `JANTAR` (P-RU-1).

As premissas `P-RU-n` citadas estão listadas, com o que as capturas de tela do app (versão 3.2.0) e o autor confirmaram e o que falta confirmar, em [`RU/README.md`](README.md).

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 11 (Software Engineering Models and Methods). IEEE, 2024.

ANTHROPIC. **Claude Code**. Assistente de IA. Disponível em: claude.ai/code. Acesso em: 30 out. 2026. Uso: apoio à redação e aos diagramas, a partir das instruções, das capturas de tela e das correções do autor (resumo em `IA/registro-C.md`). Questão: Apêndice <X>, Seção <X.1>.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
