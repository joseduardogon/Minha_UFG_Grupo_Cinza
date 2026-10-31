# Avaliação de UA – registrar

Evolução do app: escolher a unidade acadêmica (UA), responder o questionário de qualidade (dimensões, elementos educacionais e questões), validar e enviar a avaliação.

- **Dono (autor):** José Eduardo Gontijo de Carvalho (assumiu a frente que era da Pessoa A)
- **Revisor:** Maicon Brendo da Silva (Pessoa B)
- **Prefixo de código dos itens:** `AvalRegistrar` (ex.: `DAtv-AvalRegistrar-01`)

Cada item de informação desta pasta é um par de arquivos com o mesmo nome:
`<TIPO>-AvalRegistrar-<nn>.md` (item preenchido a partir do [modelo](../Template-Item.md)) e
`<TIPO>-AvalRegistrar-<nn>.puml` (fonte PlantUML do diagrama; o `.png` é gerado a partir dele). Itens sem diagrama (DD, Contrato, ECA) têm só o `.md`.

## Como ler esta pasta

Esta é a funcionalidade **nova** do projeto: o app atual (versão 3.1.1) não tem avaliação, então **não há capturas de tela** e nada foi observado no app. Toda a modelagem parte do enunciado (Apêndice A) e do contrato-base (seção 8: avaliador anônimo, sem login; a mesma UA pode ser avaliada mais de uma vez; avaliação registrada não pode ser editada nem excluída). O que o enunciado não define é registrado como premissa `P-AR-n`, na tabela abaixo.

Os itens seguem a **ordem de produção do contrato-base** (casos de uso, atividades, protótipo de IHC, dicionário de dados, componentes e classes, sequência, estados, contratos e regras E-C-A). Uma sugestão de leitura:

1. [`DCdu-AvalRegistrar-01`](DCdu-AvalRegistrar-01.md): os quatro casos de uso (UC09.1 a UC09.4), que detalham o macro UC09 "Avaliar UA" do `DCdu-Geral-01`.
2. Os `DAtv` e os `DIhc`: o fluxo de cada caso de uso e as quatro telas (`TelaAvaliacao`, `TelaEscolherUA`, `TelaQuestionario`, `TelaConfirmacao`), com os eventos de interação E0 a En marcados no desenho.
3. O `DD-AvalRegistrar-01`: as entidades do questionário e da avaliação, entrega que `AvalConsultar` (Phablo Tavares Paixão, Pessoa D) usa.
4. `DCmp`, `DCla`, `DSeq`, `DEst`, `Contrato` e `ECA`.

O campo **Rastreia para** de cada `.md` indica de quais outros itens ele depende ou qual detalha. As atividades numeradas (A1, A2...) dos `DAtv` geram, uma a uma, os `DSeq`; os rótulos E0 a En dos `DIhc` são os mesmos dos `DEst` e dos contratos. Legenda de status: **Em produção** = primeira versão escrita, ainda sem revisão (contrato, seção 10); **A fazer** = ainda não iniciado.

Quem vê só uma tela: o cartão "Avaliação de UA" da tela inicial (E9 de `DIhc-Inicio-01`) abre a `TelaAvaliacao`; "Avaliar uma unidade" leva à `TelaEscolherUA`, depois à `TelaQuestionario` (uma dimensão por vez, com notas de 0 a 5) e, se o envio for registrado, à `TelaConfirmacao`. O botão "Ver notas" da `TelaAvaliacao` abre a tela de `AvalConsultar`, que não é desta pasta.

## Itens da pasta

| Código | Título | Status |
|---|---|---|
| [`DCdu-AvalRegistrar-01`](DCdu-AvalRegistrar-01.md) | Casos de uso UC09.1 a UC09.4 | Em produção |
| [`DAtv-AvalRegistrar-01`](DAtv-AvalRegistrar-01.md) | Atividades do UC09.1: escolher a UA (A1 abrir a lista, A2 escolher a UA) | Em produção |
| [`DAtv-AvalRegistrar-02`](DAtv-AvalRegistrar-02.md) | Atividades do UC09.2: responder o questionário (A1 dar nota, A2 navegar entre dimensões) | Em produção |
| [`DAtv-AvalRegistrar-03`](DAtv-AvalRegistrar-03.md) | Atividade do UC09.3: enviar a avaliação (A1, com a validação como passo interno) | Em produção |
| [`DAtv-AvalRegistrar-04`](DAtv-AvalRegistrar-04.md) | Atividades do UC09.4: validar o preenchimento (só o App, sem DSeq próprio) | Em produção |
| [`DIhc-AvalRegistrar-01`](DIhc-AvalRegistrar-01.md) | Protótipo da `TelaAvaliacao` (entrada), eventos E0 a E3 | Em produção |
| [`DIhc-AvalRegistrar-02`](DIhc-AvalRegistrar-02.md) | Protótipo da `TelaEscolherUA`, eventos E0 a E2 | Em produção |
| [`DIhc-AvalRegistrar-03`](DIhc-AvalRegistrar-03.md) | Protótipo da `TelaQuestionario`, eventos E0 a E5 | Em produção |
| [`DIhc-AvalRegistrar-04`](DIhc-AvalRegistrar-04.md) | Protótipo da `TelaConfirmacao`, eventos E0 e E1 | Em produção |
| [`DD-AvalRegistrar-01`](DD-AvalRegistrar-01.md) | Dicionário de dados: entidades do questionário e da avaliação | Em produção |
| [`DCmp-AvalRegistrar-01`](DCmp-AvalRegistrar-01.md) | Componentes do pacote | Em produção |
| [`DCla-AvalRegistrar-01`](DCla-AvalRegistrar-01.md) | Classes do componente `TelasAvaliacao` | Em produção |
| [`DCla-AvalRegistrar-02`](DCla-AvalRegistrar-02.md) | Classes do componente `FonteUnidades` | Em produção |
| [`DCla-AvalRegistrar-03`](DCla-AvalRegistrar-03.md) | Classes do componente `FonteQuestionario` | Em produção |
| [`DCla-AvalRegistrar-04`](DCla-AvalRegistrar-04.md) | Classes do componente `ServicoEnvioAvaliacao` | Em produção |
| [`DSeq-AvalRegistrar-01`](DSeq-AvalRegistrar-01.md) | Sequência de `DAtv-01` A1: abrir a lista de UAs | Em produção |
| [`DSeq-AvalRegistrar-02`](DSeq-AvalRegistrar-02.md) | Sequência de `DAtv-01` A2: escolher a UA | Em produção |
| [`DSeq-AvalRegistrar-03`](DSeq-AvalRegistrar-03.md) | Sequência de `DAtv-02` A1: dar nota a uma questão | Em produção |
| [`DSeq-AvalRegistrar-04`](DSeq-AvalRegistrar-04.md) | Sequência de `DAtv-02` A2: navegar entre dimensões | Em produção |
| [`DSeq-AvalRegistrar-05`](DSeq-AvalRegistrar-05.md) | Sequência de `DAtv-03` A1: enviar a avaliação | Em produção |
| [`DEst-AvalRegistrar-01`](DEst-AvalRegistrar-01.md) | Estados da `TelaAvaliacao` | Em produção |
| [`DEst-AvalRegistrar-02`](DEst-AvalRegistrar-02.md) | Estados da `TelaEscolherUA` | Em produção |
| [`DEst-AvalRegistrar-03`](DEst-AvalRegistrar-03.md) | Estados da `TelaQuestionario` | Em produção |
| [`DEst-AvalRegistrar-04`](DEst-AvalRegistrar-04.md) | Estados da `TelaConfirmacao` | Em produção |
| [`Contrato-AvalRegistrar-01`](Contrato-AvalRegistrar-01.md) | Contratos das operações | Em produção |
| [`ECA-AvalRegistrar-01`](ECA-AvalRegistrar-01.md) | Regras ativas `ECA-AR-nn` | Em produção |

## Premissas

O enunciado define a escala de nota e a estrutura (dimensões, elementos, questões), mas não o comportamento do app. As premissas abaixo foram assumidas para modelar e estão marcadas nos itens como `P-AR-n`. Como a funcionalidade não existe no app, nenhuma pode ser conferida em captura de tela. A coluna "Itens que citam" lista, para cada premissa, exatamente os itens da pasta que a citam, e cada um desses itens a cita no texto.

**Tabela 1 – Premissas de Avaliação de UA (registrar)**

| Código | Premissa | Situação | Itens que citam |
|---|---|---|---|
| P-AR-1 | O ponto de entrada é o cartão "Avaliação de UA" da tela inicial (E9 de `DIhc-Inicio-01`, decisão de 20/10 em `Docs/decisoes.md`). A tela aberta por ele é a `TelaAvaliacao`, definida em `DIhc-AvalRegistrar-01`, com os botões "Avaliar uma unidade" (segue para o registro) e "Ver notas" (abre a tela de `AvalConsultar`) | Decisão desta especificação, a confirmar com Phablo (Pessoa D), que fará `AvalConsultar` | `Contrato-AvalRegistrar-01`, `DAtv-AvalRegistrar-01`, `DCdu-AvalRegistrar-01`, `DCla-AvalRegistrar-01`, `DCmp-AvalRegistrar-01`, `DEst-AvalRegistrar-01`, `DIhc-AvalRegistrar-01`, `DSeq-AvalRegistrar-01` |
| P-AR-2 | A lista de UAs vem do Servidor/API, com a entidade `UnidadeAcademica` de Maicon (especialização de `Local`, `DD-Locais-01`); a escolha é por toque em uma lista | Premissa de projeto | `DAtv-AvalRegistrar-01`, `DCdu-AvalRegistrar-01`, `DCla-AvalRegistrar-02`, `DD-AvalRegistrar-01`, `DIhc-AvalRegistrar-02`, `DSeq-AvalRegistrar-01` |
| P-AR-3 | Dimensões, elementos e questões são cadastrados no painel web e obtidos do Servidor/API a cada avaliação, sem cache | Premissa de projeto | `Contrato-AvalRegistrar-01`, `DCdu-AvalRegistrar-01`, `DCla-AvalRegistrar-03`, `DCmp-AvalRegistrar-01`, `DD-AvalRegistrar-01`, `DEst-AvalRegistrar-03`, `DIhc-AvalRegistrar-03`, `DSeq-AvalRegistrar-02`, `DSeq-AvalRegistrar-04` |
| P-AR-4 | O questionário é apresentado dimensão por dimensão, com navegação para frente e para trás | Premissa de projeto | `Contrato-AvalRegistrar-01`, `DAtv-AvalRegistrar-02`, `DCdu-AvalRegistrar-01`, `DCla-AvalRegistrar-01`, `DIhc-AvalRegistrar-03`, `DSeq-AvalRegistrar-02`, `DSeq-AvalRegistrar-04`, `ECA-AvalRegistrar-01` |
| P-AR-5 | A nota é um número inteiro de 0 (péssima) a 5 (excelente), e todas as questões são obrigatórias para enviar | Premissa de projeto (o enunciado dá a escala, não diz se é inteira nem se é obrigatória) | `Contrato-AvalRegistrar-01`, `DAtv-AvalRegistrar-02`, `DAtv-AvalRegistrar-03`, `DAtv-AvalRegistrar-04`, `DCdu-AvalRegistrar-01`, `DCla-AvalRegistrar-01`, `DCla-AvalRegistrar-04`, `DD-AvalRegistrar-01`, `DEst-AvalRegistrar-03`, `DIhc-AvalRegistrar-03`, `DSeq-AvalRegistrar-03`, `DSeq-AvalRegistrar-05` |
| P-AR-6 | O envio é uma única chamada; se falhar, as notas permanecem na tela para novo envio | Premissa de projeto | `Contrato-AvalRegistrar-01`, `DAtv-AvalRegistrar-03`, `DCdu-AvalRegistrar-01`, `DCla-AvalRegistrar-01`, `DCla-AvalRegistrar-04`, `DCmp-AvalRegistrar-01`, `DEst-AvalRegistrar-03`, `DIhc-AvalRegistrar-03`, `DSeq-AvalRegistrar-05`, `ECA-AvalRegistrar-01` |
| P-AR-7 | A avaliação enviada contém só a UA e as notas, sem identificação do avaliador | Contrato-base, seção 8 | `Contrato-AvalRegistrar-01`, `DAtv-AvalRegistrar-03`, `DCdu-AvalRegistrar-01`, `DCla-AvalRegistrar-04`, `DD-AvalRegistrar-01`, `DSeq-AvalRegistrar-05` |
| P-AR-8 | Sair da avaliação antes de enviar descarta as notas; o app não guarda rascunho | Premissa de projeto | `Contrato-AvalRegistrar-01`, `DAtv-AvalRegistrar-02`, `DCdu-AvalRegistrar-01`, `DCla-AvalRegistrar-01`, `DEst-AvalRegistrar-03`, `DIhc-AvalRegistrar-03`, `DSeq-AvalRegistrar-02`, `DSeq-AvalRegistrar-03`, `DSeq-AvalRegistrar-04`, `ECA-AvalRegistrar-01` |
| P-AR-9 | O questionário (dimensões, elementos e questões) é o mesmo para qualquer UA; a UA escolhida só entra no envio | Premissa de projeto | `Contrato-AvalRegistrar-01`, `DCdu-AvalRegistrar-01`, `DCla-AvalRegistrar-03`, `DCmp-AvalRegistrar-01`, `DD-AvalRegistrar-01`, `DEst-AvalRegistrar-03`, `DIhc-AvalRegistrar-03`, `DSeq-AvalRegistrar-02` |
| P-AR-10 | A apresentação dos estados vazio e indisponível segue o padrão do Comum (`DEst-Comum-01`); os textos exatos seguem o padrão do Comum | Premissa de projeto | `Contrato-AvalRegistrar-01`, `DAtv-AvalRegistrar-01`, `DCdu-AvalRegistrar-01`, `DCla-AvalRegistrar-01`, `DEst-AvalRegistrar-02`, `DEst-AvalRegistrar-03`, `DIhc-AvalRegistrar-02`, `DIhc-AvalRegistrar-03`, `DSeq-AvalRegistrar-01`, `DSeq-AvalRegistrar-02` |
| P-AR-11 | A API tem as rotas `GET /unidades-academicas`, `GET /avaliacao/questionario` e `POST /avaliacoes`, com corpo em JSON; não são observáveis no app | Premissa de projeto (não observável) | `Contrato-AvalRegistrar-01`, `DCla-AvalRegistrar-02`, `DCla-AvalRegistrar-03`, `DCla-AvalRegistrar-04`, `DCmp-AvalRegistrar-01`, `DSeq-AvalRegistrar-01`, `DSeq-AvalRegistrar-02`, `DSeq-AvalRegistrar-05` |
| P-AR-12 | A nota de um elemento é a média das notas de suas questões, e a de uma dimensão é a média dos seus elementos; o cálculo é de `AvalConsultar`, e aqui só se registram as notas por questão | Premissa de projeto | `DCdu-AvalRegistrar-01`, `DD-AvalRegistrar-01` |
| P-AR-13 | A nota de uma questão pode ser trocada quantas vezes o usuário quiser antes de enviar (um novo toque sobrescreve), nenhuma opção vem pré-selecionada, e a navegação entre dimensões não exige que a dimensão esteja completa: a conferência é feita só no envio (UC09.4) | Premissa de projeto | `DAtv-AvalRegistrar-02`, `DEst-AvalRegistrar-03`, `DIhc-AvalRegistrar-03` |
| P-AR-14 | Na validação reprovada, o app não envia nada, mostra um aviso com o número de questões sem nota e marca as pendentes em todas as dimensões (para qual dimensão a tela vai, ver P-AR-28); a marca de uma questão some quando ela recebe nota | Premissa de projeto | `DAtv-AvalRegistrar-03`, `DEst-AvalRegistrar-03`, `DIhc-AvalRegistrar-03` |
| P-AR-15 | Textos das mensagens: confirmação "Avaliação registrada. Obrigado por contribuir!" (definido na especificação do projeto); pendências, do tipo "Faltam N questões sem nota"; falha no envio, do tipo "Não foi possível registrar a avaliação. Suas notas foram mantidas; toque em Enviar para tentar de novo" | Premissa de projeto (o texto das duas últimas é ilustrativo) | `DAtv-AvalRegistrar-03`, `DEst-AvalRegistrar-04`, `DIhc-AvalRegistrar-03`, `DIhc-AvalRegistrar-04` |
| P-AR-16 | A `TelaAvaliacao` mostra, além dos dois botões, um texto curto de apresentação com a escala de 0 a 5 e o aviso de que a avaliação é anônima e não pode ser editada nem excluída (contrato-base, seção 8) | Premissa de projeto | `DIhc-AvalRegistrar-01` |
| P-AR-17 | Durante o envio, o app mostra um indicador de envio (estado Enviando); o bloqueio dos toques está em P-AR-27 | Premissa de projeto | `DAtv-AvalRegistrar-03`, `DEst-AvalRegistrar-03`, `DIhc-AvalRegistrar-03` |
| P-AR-18 | A lista de UAs mostra o nome e a sigla de cada UA, sem busca nem filtro (a ordem é a recebida do servidor, P-AR-25) | Premissa de projeto | `DAtv-AvalRegistrar-01`, `DIhc-AvalRegistrar-02` |
| P-AR-19 | A `TelaConfirmacao` não tem seta de voltar; a única saída é "Concluir", que volta à `TelaAvaliacao` e descarta as telas intermediárias (escolha da UA e questionário) | Premissa de projeto | `DAtv-AvalRegistrar-03`, `DEst-AvalRegistrar-04`, `DIhc-AvalRegistrar-04` |

As premissas P-AR-20 a P-AR-31 foram criadas pelas frentes de estrutura (P-AR-20 a P-AR-29) e de sequências (P-AR-30 e P-AR-31) e estão na Tabela 2. Os textos de P-AR-20 a P-AR-29 foram redigidos a partir do uso nos itens `DD`, `DCla`, `Contrato` e `ECA`; os de P-AR-30 e P-AR-31 são os do `DSeq-AvalRegistrar-05`. A conferência final deve comparar esses textos com os relatórios dessas frentes.

**Tabela 2 – Premissas de estrutura e de sequências**

| Código | Premissa | Situação | Itens que citam |
|---|---|---|---|
| P-AR-20 | Os identificadores (`id`) de dimensão, elemento e questão são inteiros únicos atribuídos pelo servidor, e a `ordem` (inteira) define a ordem de apresentação | Premissa de projeto | `Contrato-AvalRegistrar-01`, `DCla-AvalRegistrar-03`, `DD-AvalRegistrar-01` |
| P-AR-21 | O que é alterado ou retirado do questionário no painel web continua existindo no servidor para as avaliações já registradas | Premissa de projeto | `DD-AvalRegistrar-01` |
| P-AR-22 | O identificador e a data e hora do registro da avaliação são atribuídos pelo servidor; o app não os envia nem os recebe | Premissa de projeto | `Contrato-AvalRegistrar-01`, `DCla-AvalRegistrar-04`, `DD-AvalRegistrar-01` |
| P-AR-23 | Os corpos JSON trocados com a API têm os campos: unidade (`id`, `nome`, `sigla`); questionário com dimensões, elementos e questões aninhados (`id`, `nome` ou `texto`, `ordem`); envio com `idUnidade` e a lista `notas` de `{idQuestao, valor}` | Premissa de projeto (não observável) | `Contrato-AvalRegistrar-01`, `DCla-AvalRegistrar-02`, `DCla-AvalRegistrar-03`, `DCla-AvalRegistrar-04` |
| P-AR-24 | Ao montar a avaliação, cada `NotaQuestao` leva uma `Questao` identificada só pelo `id`, pois o rascunho guarda apenas o `id` da questão | Premissa de projeto | `Contrato-AvalRegistrar-01`, `DCla-AvalRegistrar-01` |
| P-AR-25 | As UAs são mostradas na ordem recebida do servidor, e dimensões, elementos e questões, em ordem crescente de `ordem` | Premissa de projeto | `Contrato-AvalRegistrar-01`, `DCla-AvalRegistrar-02`, `DCla-AvalRegistrar-03`, `DIhc-AvalRegistrar-02` |
| P-AR-26 | Um reenvio depois de uma resposta perdida pode criar uma segunda avaliação no servidor; o app não tenta de novo sozinho | Premissa de projeto | `Contrato-AvalRegistrar-01`, `DCla-AvalRegistrar-04` |
| P-AR-27 | Durante o envio, a tela ignora os toques (botões e seta de voltar), para que um toque repetido não crie duas avaliações | Premissa de projeto | `Contrato-AvalRegistrar-01`, `DAtv-AvalRegistrar-03`, `DCla-AvalRegistrar-01`, `DEst-AvalRegistrar-03`, `DIhc-AvalRegistrar-03`, `ECA-AvalRegistrar-01` |
| P-AR-28 | Na validação reprovada, o app marca as questões pendentes em todas as dimensões e vai à dimensão da primeira questão pendente, na ordem do questionário | Premissa de projeto | `Contrato-AvalRegistrar-01`, `DAtv-AvalRegistrar-03`, `DAtv-AvalRegistrar-04`, `DCla-AvalRegistrar-01`, `DEst-AvalRegistrar-03`, `DIhc-AvalRegistrar-03`, `ECA-AvalRegistrar-01` |
| P-AR-29 | Um questionário malformado (falta de campo, dimensão sem elemento, elemento sem questão ou `id` repetido) é rejeitado como `RESPOSTA_INVALIDA` | Premissa de projeto | `Contrato-AvalRegistrar-01`, `DCla-AvalRegistrar-03` |
| P-AR-30 | Registrada a avaliação, a `TelaConfirmacao` substitui a `TelaQuestionario` na navegação e o rascunho é descartado: voltar a partir da confirmação não retorna ao questionário (evita reenvio); "Concluir" leva à `TelaAvaliacao` | Premissa de projeto | `DSeq-AvalRegistrar-05` |
| P-AR-31 | O app só distingue sucesso (status 2xx) de falha no envio: não lê o corpo da resposta ao POST nem recebe um identificador da avaliação; qualquer resposta de erro do servidor é tratada como `NAO_REGISTRADA` | Premissa de projeto | `DSeq-AvalRegistrar-05` |

## Pendências para outros

- **Phablo Tavares Paixão (Pessoa D), responsável por `AvalConsultar`:** (1) confirmar que a tela de "Ver notas" é aberta pelo botão "Ver notas" da `TelaAvaliacao` (`DIhc-AvalRegistrar-01`, evento E2 `aoTocarConsultar`) e fornecer o nome da tela; (2) confirmar a premissa P-AR-1 (a `TelaAvaliacao` como tela aberta pelo cartão E9, decisão desta especificação, ainda não registrada em `Docs/decisoes.md`); (3) decidir onde ficam as entidades do questionário e da avaliação no modelo integrado (`DD-Geral-01`), usando o `DD-AvalRegistrar-01`. (4) decidir o ciclo de dependência entre pacotes que o botão "Ver notas" cria: a `TelaAvaliacao`, que está em `AvalRegistrar`, abre a tela de `AvalConsultar` (dependência `AvalRegistrar` → `AvalConsultar`), e o `DPac-Geral-01` já prevê `AvalConsultar` → `AvalRegistrar`; as duas opções estão na decisão proposta abaixo.
- **Maicon Brendo da Silva (Pessoa B), revisor:** confirmar o questionário (dimensões, elementos e questões, premissas P-AR-3, P-AR-9 e P-AR-13 a P-AR-15), a referência à `UnidadeAcademica` de `DD-Locais-01` (premissa P-AR-2) e o uso do Comum (premissa P-AR-10).

## Texto proposto para `Docs/decisoes.md`

O registro de decisões é de Phablo (`Docs/decisoes.md`). Estas duas entradas estão prontas para ele colar, se concordar, na ordem do arquivo (mais recente primeiro). Nada foi alterado no arquivo dele.

### 30/10/2026 – Tela de entrada da Avaliação de UA (`TelaAvaliacao`)

- **Decisão:** o cartão "Avaliação de UA" da tela inicial (E9 de `DIhc-Inicio-01`) abre a `TelaAvaliacao`, definida em `DIhc-AvalRegistrar-01`, com dois botões: "Avaliar uma unidade" (segue para o registro, em `AvalRegistrar`) e "Ver notas" (abre a tela de `AvalConsultar`). A `TelaAvaliacao` é estática: não chama o servidor e mostra um texto de apresentação com a escala de 0 a 5 e o aviso de que a avaliação é anônima e não pode ser editada nem excluída.
- **Motivo:** a decisão de 20/10 deixou a tela a cargo de "A e B", e a Pessoa A deixou de existir na equipe; a frente `AvalRegistrar` passou a José Eduardo, e `AvalConsultar` a Phablo. Uma tela de escolha com dois botões mantém um único ponto de entrada, como foi decidido em 20/10.
- **Alternativas:** abrir direto o registro, com as notas acessadas por outro caminho (descartada: `AvalConsultar` ficaria sem ponto de entrada); dois cartões na tela inicial (já descartada em 20/10).

### 30/10/2026 – Dependência entre `AvalRegistrar` e `AvalConsultar` pelo botão "Ver notas"

- **Problema:** como a `TelaAvaliacao` está em `AvalRegistrar` e o botão "Ver notas" abre uma tela de `AvalConsultar`, surge a dependência `AvalRegistrar` → `AvalConsultar`. O `DPac-Geral-01` já prevê `AvalConsultar` → `AvalRegistrar` (as notas agregam avaliações): as duas juntas formam um ciclo entre pacotes.
- **Opção 1 (recomendada):** mover a `TelaAvaliacao` para o pacote `Inicio`, que já depende de todas as funcionalidades; `AvalRegistrar` e `AvalConsultar` deixam de se conhecer na direção da tela de entrada, e o ciclo desaparece. Exige mudar `DCmp-AvalRegistrar-01`, `DCla-AvalRegistrar-01` e o pacote do `DIhc-AvalRegistrar-01`; o `DPac-Geral-01` não muda.
- **Opção 2:** manter a `TelaAvaliacao` em `AvalRegistrar` e aceitar a dependência `AvalRegistrar` → `AvalConsultar` no `DPac-Geral-01` (acrescentar a seta e justificar o ciclo). Não exige mudar os itens de `AvalRegistrar`.

## Conferência da tabela de premissas

A coluna "Itens que citam" é gerada a partir do texto de cada `.md` da pasta (código `P-AR-n` citado) e deve ser reconferida depois de qualquer edição dos itens.
