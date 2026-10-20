# Contrato-Radio-01 – Contratos das operações do pacote Radio

| Campo | Valor |
|---|---|
| **Código** | `Contrato-Radio-01` |
| **Título** | Contratos das operações do pacote Radio |
| **Autor(a)** | Pessoa D |
| **Revisor(a)** | Pessoa C |
| **Status** | Em produção |
| **Rastreia para** | `DCla-Radio-01`, `DCla-Radio-02`, `DSeq-Radio-01`, `DSeq-Radio-02`, `DSeq-Radio-03`, `ECA-Radio-01` |

## Descrição

Contratos das operações das classes de `DCla-Radio-01` e `DCla-Radio-02`. Os tipos de erro são os de `ErroApi` (`DCla-Comum-02`). As premissas são:

- **P-RA-1:** o recurso da API para a programação da semana atual é `/radio/programacao`, sem parâmetros (nome não confirmado).
- **P-RA-2:** o botão de play está sempre visível na tela.

### Classe ConfiguracaoRadio

*Invariante:* `urlPlayer` é uma URL absoluta, não vazia, sem parâmetros.

### Classe TelaRadio

*Invariantes:* `controlador` e `linkExterno` nunca são nulos; `diaSelecionado` nunca é nulo.

**Tabela 1 – Contratos de TelaRadio**

| Operação | Pré-condição | Pós-condição | Erros |
|---|---|---|---|
| `aoExibir()` | A tela está sendo exibida (entrada pela tela inicial ou retorno do navegador) | Na entrada pela tela inicial, `diaSelecionado` é o dia atual; no retorno, `diaSelecionado` é mantido. `controlador.aoEntrarNaTela()` foi chamado uma vez | – |
| `aoTocarAba(dia)` | O estado é EXIBINDO | `diaSelecionado` é `dia`; a lista exibida é `programasDoDia(dia)` ou a mensagem de vazio, se ela for vazia; nenhuma chamada à API | – |
| `aoTocarPlay()` | – | `linkExterno.abrirUrl(ConfiguracaoRadio.urlPlayer)` foi chamado uma vez e o resultado é descartado; o estado da tela não muda | – |
| `aoVoltar()` | – | A tela é encerrada e a programação em memória é descartada; o app exibe a tela inicial | – |
| `aoMudarEstado(estado)` | – | CARREGANDO: indicador de carregamento; EXIBINDO: `programasDoDia(diaSelecionado)` ou mensagem de vazio, se vazia; VAZIO: mensagem de vazio; INDISPONIVEL: mensagem de indisponibilidade | – |
| `programasDoDia(dia)` (privada) | – | Devolve os `HorarioPrograma` de `controlador.obterDados()` com `diaSemana = dia`, em ordem crescente de `horaInicio`; o estado não muda | – |

### Classe FonteProgramacaoRadio

*Invariante:* `acesso` nunca é nulo.

**Tabela 2 – Contratos de FonteProgramacaoRadio**

| Operação | Pré-condição | Pós-condição | Erros |
|---|---|---|---|
| `FonteProgramacaoRadio(acesso)` | `acesso` não é nulo | Fonte pronta; nenhuma chamada à API foi feita | – |
| `carregar()` | – | A API foi chamada uma vez (`/radio/programacao`, P-RA-1); devolve os horários de todos os dias da semana atual, possivelmente vazia | `ErroApi` de qualquer tipo (`SEM_CONEXAO`, `TEMPO_ESGOTADO`, `ERRO_SERVIDOR`, `RESPOSTA_INVALIDA`), repassado sem tratamento |
| `converter(corpo)` (privada) | `corpo` é o texto da resposta da API | Devolve um `HorarioPrograma` por horário recebido, cada um associado ao seu `ProgramaRadio`; programas com o mesmo nome e descrição são um só objeto | `ErroApi` `RESPOSTA_INVALIDA` se o texto não é JSON legível ou se algum horário tem `horaFim` igual ou anterior a `horaInicio`, exceto quando termina à meia-noite |

*Invariantes das entidades:* `ProgramaRadio.nome` não é vazio; todo `ProgramaRadio` tem ao menos um `HorarioPrograma`.

## Referências

ANTHROPIC. **Claude Code**. Assistente de IA. Disponível em: https://claude.com/claude-code. Acesso em: 20 out. 2026.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
