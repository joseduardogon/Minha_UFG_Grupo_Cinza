# Notícias

Lista de notícias por regional com abertura de link externo.

- **Dono (autor):** Pessoa C
- **Revisor:** Pessoa D
- **Prefixo de código dos itens:** `Noticias` (ex.: `DAtv-Noticias-01`)

Cada item de informação desta pasta é um par de arquivos com o mesmo nome:
`<TIPO>-Noticias-<nn>.md` (item preenchido a partir do [modelo](../Template-Item.md)) e
`<TIPO>-Noticias-<nn>.puml` (fonte PlantUML do diagrama). Itens sem diagrama (DD, Contrato, ECA) têm só o `.md`.

## Como ler esta pasta

Os itens seguem a **ordem de produção do contrato-base** (casos de uso, atividades, protótipo de IHC, componentes e classes, sequência, estados, contratos e regras E-C-A). Cada item é um par de arquivos com o mesmo nome: o `.md` explica o item e o `.puml` tem o diagrama (a imagem `.png` é gerada a partir do `.puml`). O campo **Rastreia para** de cada `.md` indica de quais outros itens ele depende ou qual detalha. Autor: José Eduardo Gontijo de Carvalho (Pessoa C). Revisor: Phablo Tavares Paixão (Pessoa D).

Legenda de status: **Pronto** = revisado e no repositório (contrato, seção 10); **Em produção** = primeira versão escrita, ainda sem revisão; **A fazer** = ainda não iniciado.

## Itens da pasta

| Código | Título | Status |
|---|---|---|
| [`DCdu-Noticias-01`](DCdu-Noticias-01.md) | Casos de uso (2 casos de uso, UC05.1 e UC05.2) | Em produção |
| [`DAtv-Noticias-01`](DAtv-Noticias-01.md), [`02`](DAtv-Noticias-02.md) | Atividades de cada caso de uso | Em produção |
| [`DIhc-Noticias-01`](DIhc-Noticias-01.md) | Protótipo da tela, com eventos de interação E0 a E3 | Em produção |
| [`DSeq-Noticias-01`](DSeq-Noticias-01.md) a [`03`](DSeq-Noticias-03.md) | Sequência de cada atividade de interação | Em produção |
| [`DEst-Noticias-01`](DEst-Noticias-01.md) | Estados da tela | Em produção |
| [`DCmp-Noticias-01`](DCmp-Noticias-01.md) | Componentes do pacote | Em produção |
| [`DCla-Noticias-01`](DCla-Noticias-01.md), [`02`](DCla-Noticias-02.md) | Classes de cada componente | Em produção |
| [`DD-Noticias-01`](DD-Noticias-01.md) | Entrada do dicionário de dados (entidade `Noticia`) | Em produção |
| [`Contrato-Noticias-01`](Contrato-Noticias-01.md) | Contratos das operações | Em produção |
| [`ECA-Noticias-01`](ECA-Noticias-01.md) | Regras ativas (3 regras) | Em produção |

A cascata de Notícias está completa em primeira versão. Falta a revisão da Pessoa D e a conferência das premissas pendentes abaixo (outras regionais, ordem da lista, estado vazio, troca de regional). Notícias segue o mesmo padrão de Eventos (lista do servidor filtrada por regional), com a regional como único filtro. Entidade entregue para o modelo de dados: [`Noticia`](../Integracao/entidades/Entidade-Noticia.md); a entidade `Regional`, compartilhada com Eventos e Locais, está descrita em `DD-Eventos-01`.

## Premissas e conferência com as capturas de tela (versão 3.2.0)

Parte do comportamento do app não aparece nos documentos da equipe. As premissas abaixo foram assumidas para modelar e estão marcadas nos itens como `P-NO-n`. As capturas relevantes são: 5, 11 e 16 (lista de Notícias), 18 (lista rolada), 12 e 20 (página de uma notícia aberta no navegador) e 31 (Notícias em modo avião). **Nenhuma delas mostra mais de uma aba de regional, a ordem da lista, o estado vazio nem o toque em uma aba ou em um cartão (do toque em um cartão só se vê o resultado, a página aberta).**

| Código | Premissa | Situação nas capturas | Itens afetados |
|---|---|---|---|
| P-NO-1 | A regional é escolhida pelo usuário, tocando em uma aba da faixa abaixo do título; a faixa rola junto com a lista e só aparece com a lista exibida (estado Exibindo); portanto o toque em uma aba (E1) só ocorre nesse estado | **Parcialmente confirmada:** há uma faixa de abas de regional, só com a aba "GOIÂNIA" (sublinhada e selecionada), que rola junto com a lista (captura 18, com a barra de título fixa) e não existe no estado indisponível (captura 31). **Pendente:** o toque em outra aba, o que a tela mostra durante a nova carga e se existem outras regionais | `DCdu-Noticias-01`, `DAtv-Noticias-01`, `DIhc-Noticias-01`, `DEst-Noticias-01`, `DSeq-Noticias-02`, `DCla-Noticias-01`, `Contrato-Noticias-01`, `ECA-Noticias-01` |
| P-NO-2 | A regional inicial é a primeira da lista de regionais oferecidas | **Parcialmente confirmada:** "GOIÂNIA" aparece selecionada ao abrir, mas não se sabe se ela é a primeira aba da faixa ou a única | `DCdu-Noticias-01`, `DAtv-Noticias-01`, `DIhc-Noticias-01`, `DSeq-Noticias-01`, `DCla-Noticias-01`, `Contrato-Noticias-01` |
| P-NO-3 | Cada notícia mostra imagem de banner, título (em negrito) e resumo (em itálico ou em fonte normal); a data não aparece no cartão; ao tocar, a página dela abre no Navegador, sem tela de detalhe | **Confirmada:** o cartão tem imagem, título e resumo, sem data (capturas 5, 11 e 16); a página aberta (portal da UFG, trilha início > notícias) mostra título, data e hora ("Em 29/10/26 18:18."), texto e os créditos "Texto:" e "Foto de capa:", estes fora do modelo do app (capturas 12 e 20). O resultado da abertura foi observado; **o toque no cartão, em si, não foi capturado** | `DCdu-Noticias-01`, `DAtv-Noticias-02`, `DIhc-Noticias-01`, `DSeq-Noticias-03`, `DEst-Noticias-01`, `DD-Noticias-01`, `Contrato-Noticias-01`, `ECA-Noticias-01`, `Entidade-Noticia` |
| P-NO-4 | A API tem a rota `GET /noticias` com o parâmetro `regional` (identificador da regional); premissa de projeto | **Não observável** | `DSeq-Noticias-01`, `DCla-Noticias-02`, `Contrato-Noticias-01`, `Entidade-Noticia` |
| P-NO-5 | A lista segue a ordem em que a API devolve (presume-se da mais recente para a mais antiga); o app não ordena | **Pendente:** a data não aparece no cartão e a ordem não é verificável | `DIhc-Noticias-01`, `DCla-Noticias-02`, `DD-Noticias-01`, `Contrato-Noticias-01`, `Entidade-Noticia` |
| P-NO-6 | A lista de regionais de Notícias é fixa no app (`regionaisOferecidas`) e é a mesma de Eventos | **Pendente:** falta ver as demais abas | `DIhc-Noticias-01`, `DSeq-Noticias-01`, `DCla-Noticias-01`, `DD-Noticias-01`, `Contrato-Noticias-01`, `Entidade-Noticia` |
| P-NO-8 | No estado indisponível a tela mostra a barra de título e o corpo totalmente em branco, sem faixa de abas e sem mensagem | **Confirmada** na captura 31 (modo avião, `SEM_CONEXAO`). Presume-se o mesmo para os demais tipos de `ErroApi`, que o controlador do Comum trata do mesmo modo | `DCdu-Noticias-01`, `DAtv-Noticias-01`, `DIhc-Noticias-01`, `DEst-Noticias-01`, `DSeq-Noticias-01`, `DCla-Noticias-01`, `Contrato-Noticias-01` |
| P-NO-9 | No estado vazio (regional sem notícias) a tela mostra a mensagem de vazio genérica do Comum, sem a faixa de abas (como em Eventos, captura 29); o estado Carregando mostra o indicador de carregamento, também sem abas | **Pendente:** nenhum dos dois estados foi capturado | `DCdu-Noticias-01`, `DAtv-Noticias-01`, `DIhc-Noticias-01`, `DEst-Noticias-01`, `DSeq-Noticias-01`, `DCla-Noticias-01`, `Contrato-Noticias-01` |

Resumo do status: **confirmadas** são a existência das abas de regional (uma visível, "GOIÂNIA", selecionada ao abrir), o cartão com imagem, título e resumo, a página aberta no navegador e o estado indisponível em branco; **pendentes** são as outras regionais, a ordem da lista, o estado vazio e o que acontece ao trocar de regional; **não observável** é a rota da API.

Decisão corrigida: a premissa antiga **P-NO-7** (barra de título e faixa de abas continuam visíveis nos estados vazio e indisponível) foi **refutada** pela captura 31, em que o estado indisponível mostra a barra de título e um corpo em branco, sem abas. Ela foi retirada, e o código P-NO-7 não é reutilizado. A regra vigente é: a barra de título é fixa em todos os estados, e a faixa de abas só aparece com a lista exibida (P-NO-1, P-NO-8 e P-NO-9); por isso o evento E1 (trocar de regional) só ocorre no estado Exibindo.

Decisão registrada: a entidade `Noticia` não tem `dataPublicacao`. A data só aparece na página do portal aberta no Navegador (capturas 12 e 20), não no cartão da lista, e portanto não faz parte do que o app recebe e exibe. O mesmo vale para os créditos "Texto:" e "Foto de capa:".

## Capturas consultadas

- Capturas 5, 11 e 16 (versão 3.2.0): tela "Notícias", com seta de voltar, faixa de abas com "GOIÂNIA" sublinhada e cartões com imagem de banner, título em negrito e resumo (itálico ou normal).
- Captura 18 (versão 3.2.0): a lista rolada; a barra de título fica fixa e a faixa de abas rola junto com a lista.
- Captura 12 e captura 20 (versão 3.2.0): página de uma notícia aberta no navegador (portal ufg.br, trilha "INÍCIO > NOTÍCIAS", título, "Em dd/mm/aa hh:mm.", texto, "Texto:" e "Foto de capa:").
- Captura 31 (versão 3.2.0): Notícias em modo avião: barra de título com seta de voltar e corpo totalmente em branco (estado indisponível).
- Captura 1 (versão 3.2.0): menu inicial, com o cartão Notícias (ponto de entrada da tela).

## Próximos passos da pasta

1. Conferir a ordem da lista (P-NO-5) sem nova captura: abrir a página de cada cartão da lista e comparar as datas "Em dd/mm/aa hh:mm." com a ordem dos cartões.
2. Verificar com a equipe ou com o painel web se existe outra regional com notícias cadastradas (P-NO-1, P-NO-2, P-NO-6). Se só existir "GOIÂNIA", registrar que a faixa tem uma única aba e que a troca de regional não é exercitável na versão 3.2.0.
3. O estado vazio (P-NO-9) depende de uma regional sem notícias e dificilmente será observável; se não for, mantê-lo como premissa pendente, explícita no PDF.
4. Pessoa D revisar os itens e registrar a revisão no fim de cada `.md`.
5. Pessoa D decidir onde fica a entidade `Regional` (pendência D-INT-03 do `DPac-Geral-01`), usada por Notícias, Eventos e Locais; hoje ela é referenciada com o estereótipo `<<Comum (proposta)>>`.
