# Contrato-AvalConsultar-01 – Contratos de Avaliação – Consultar notas

| Campo | Valor |
|---|---|
| **Código** | `Contrato-AvalConsultar-01` |
| **Título** | Contratos de Avaliação – Consultar notas |
| **Autor(a)** | Pessoa D |
| **Revisor(a)** | Pessoa C |
| **Status** | Em produção |
| **Rastreia para** | `DCla-AvalConsultar-01`, `DCla-AvalConsultar-02`, `DD-AvalConsultar-01`, `DSeq-AvalConsultar-01`, `DSeq-AvalConsultar-02`, `DSeq-AvalConsultar-03`, `DEst-AvalConsultar-01`, `DEst-AvalConsultar-02`, `DEst-AvalConsultar-03`, `ECA-AvalConsultar-01`, `DCla-Comum-02`, `DCla-Comum-03` |

## Descrição

Contratos das operações das classes de `DCla-AvalConsultar-01` e `DCla-AvalConsultar-02`. Os tipos de erro são os de `ErroApi` (`DCla-Comum-02`). As premissas `P-AC-n` estão no [`README.md`](README.md).

### Regras de cálculo (pós-condições do Servidor/API, P-AC-6)

O app não calcula médias, mas as respostas que ele recebe têm de obedecer às regras abaixo; elas são as pós-condições das rotas da P-AC-9 e o critério para validar o servidor. Todas as notas estão entre 0 e 5. Para uma UA *u* com avaliações *a₁…aₙ*:

- **R1** nota do elemento *e* em *aᵢ* = média das notas das questões de *e* em *aᵢ* (P-AR-12);
- **R2** nota da dimensão *d* em *aᵢ* = média das notas dos elementos de *d* em *aᵢ* (enunciado);
- **R3** nota de *aᵢ* = média das notas das dimensões em *aᵢ* (enunciado);
- **R4** `NotaDimensao.nota` de *d* em *u* = média, sobre as avaliações de *u* que têm *d*, da nota de *d* (P-AC-8);
- **R5** `NotaUnidade.nota` de *u* = média das notas de *a₁…aₙ*; ausente se *n* = 0 (P-AC-3, P-AC-4);
- **R6** `MediaArea.nota` = média das `NotaUnidade.nota` presentes das UAs da área; ausente se nenhuma está presente;
- **R7** nota da UFG = média das `NotaUnidade.nota` presentes de todas as UAs; ausente se nenhuma está presente (enunciado).

A agregação usa os `id` de dimensão, elemento e questão, para que avaliações feitas com um questionário anterior continuem contando (`DD-AvalRegistrar-01`, "Para quem consome", item 3).

### Classe FormatoNota

**Tabela 1 – Contratos de FormatoNota**

| Operação | Pré-condição | Pós-condição | Erros |
|---|---|---|---|
| `formatar(nota)` | `nota` ausente ou entre 0 e 5 | Ausente: devolve "Sem avaliações"; presente: devolve a nota arredondada a uma casa decimal, com vírgula (ex.: "4,3", P-AC-5) | – |

### Classes TelaNotas, TelaNotasArea e TelaNotasUA

*Invariantes:* `fonte` e `controlador` não são nulos depois de `aoExibir()`; `area` (TelaNotasArea) e `unidade` (TelaNotasUA) nunca são nulos.

**Tabela 2 – Contratos das telas**

| Operação | Pré-condição | Pós-condição | Erros |
|---|---|---|---|
| `TelaNotas(acesso)` | `acesso` não é nulo; a tela foi aberta pelo Intent `VER_NOTAS` | Tela criada; nenhuma chamada à API | – |
| `TelaNotasArea(acesso, area)` | `acesso` e `area` não são nulos | Tela criada; nenhuma chamada à API | – |
| `TelaNotasUA(acesso, unidade)` | `acesso` e `unidade` não são nulos | Tela criada; nenhuma chamada à API | – |
| `aoExibir()` (das três) | A tela está sendo exibida (entrada ou volta de outra tela) | Uma nova fonte e um novo controlador foram criados; a tela é observadora do controlador; `controlador.aoEntrarNaTela()` foi chamado uma vez (sem cache) | – |
| `aoMudarEstado(estado)` (das três) | – | CARREGANDO: indicador; EXIBINDO: o valor agregado (nota da UFG, média da área ou nota da UA) e a lista, cada nota passada por `FormatoNota.formatar`; VAZIO: mensagem de vazio ("Sem avaliações" na `TelaNotasUA`); INDISPONIVEL: mensagem de indisponibilidade | – |
| `TelaNotas.aoEscolherArea(area)` | Estado EXIBINDO; `area` está em `controlador.obterDados()` | Uma `TelaNotasArea(acesso, area)` foi criada e exibida | – |
| `TelaNotasArea.aoEscolherUA(nota)` | Estado EXIBINDO; `nota` está em `controlador.obterDados()` | Uma `TelaNotasUA(acesso, nota.unidade)` foi criada e exibida, também quando `nota.nota` está ausente | – |
| `aoVoltar()` (das três) | – | A tela é encerrada e os dados em memória são descartados; volta-se à tela anterior (`TelaAvaliacao`, `TelaNotas` ou `TelaNotasArea`) | – |

### Classes FonteNotasUFG, FonteNotasArea e FonteNotasUnidade

*Invariantes:* `acesso` nunca é nulo; `areaConhecimento` não é nula (FonteNotasArea); `unidade` não é nula (FonteNotasUnidade).

**Tabela 3 – Contratos das fontes**

| Operação | Pré-condição | Pós-condição | Erros |
|---|---|---|---|
| Construtores | Parâmetros não nulos | Fonte pronta; valor agregado ausente; nenhuma chamada à API | – |
| `FonteNotasUFG.carregar()` | – | A API foi chamada uma vez (`/avaliacao/notas`); devolve uma `MediaArea` por área, possivelmente lista vazia; `notaUfg` atualizada (R6, R7) | `ErroApi` de qualquer tipo, repassado sem tratamento |
| `FonteNotasArea.carregar()` | – | A API foi chamada uma vez (`/avaliacao/notas/area`, `area = areaConhecimento.nome`); devolve uma `NotaUnidade` por UA da área, possivelmente vazia; `mediaArea` atualizada (R5, R6) | Idem |
| `FonteNotasUnidade.carregar()` | – | A API foi chamada uma vez (`/avaliacao/notas/unidade`, `unidade = unidade.id`); devolve uma `NotaDimensao` por dimensão avaliada, vazia se a UA não tem avaliações; `notaUnidade` atualizada (R4, R5) | Idem |
| `obterNotaUfg()`, `obterMediaArea()`, `obterNotaUnidade()` | `carregar()` terminou sem erro | Devolve o valor agregado da última carga (pode ser ausente); o estado não muda | – |
| `converter(corpo)` (privada, das três) | `corpo` é o texto da resposta | Devolve a lista e guarda o valor agregado | `ErroApi` `RESPOSTA_INVALIDA` se o texto não é JSON legível ou se alguma nota está fora de 0 a 5 |

*Invariantes das entidades (`DD-AvalConsultar-01`):* toda nota presente está entre 0 e 5; `NotaDimensao.nota` está sempre presente; `MediaArea.areaConhecimento` não é nula.

## Referências

ANTHROPIC. **Claude Code**. Assistente de IA. Disponível em: https://claude.com/claude-code. Acesso em: 1 nov. 2026.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
