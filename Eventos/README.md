# Eventos

Calendário mensal, filtro por data, lista por regional e estado sem eventos.

- **Dono (autor):** Pessoa C
- **Revisor:** Pessoa D
- **Prefixo de código dos itens:** `Eventos` (ex.: `DAtv-Eventos-01`)

Cada item de informação desta pasta é um par de arquivos com o mesmo nome:
`<TIPO>-Eventos-<nn>.md` (item preenchido a partir do [modelo](../Template-Item.md)) e
`<TIPO>-Eventos-<nn>.puml` (fonte PlantUML do diagrama). Itens sem diagrama (DD, Contrato, ECA) têm só o `.md`.

## Como ler esta pasta

Os itens seguem a **ordem de produção do contrato-base** (casos de uso, atividades, protótipo de IHC, componentes e classes, sequência, estados, contratos e regras E-C-A). Cada item é um par de arquivos com o mesmo nome: o `.md` explica o item e o `.puml` tem o diagrama (a imagem `.png` é gerada a partir do `.puml`). O campo **Rastreia para** de cada `.md` indica de quais outros itens ele depende ou qual detalha. Autor: José Eduardo Gontijo de Carvalho (Pessoa C). Revisor: Phablo Tavares Paixão (Pessoa D).

Legenda de status: **Pronto** = revisado e no repositório (contrato, seção 10); **Em produção** = primeira versão escrita, ainda sem revisão; **A fazer** = ainda não iniciado.

## Itens da pasta

| Código | Título | Status |
|---|---|---|
| [`DCdu-Eventos-01`](DCdu-Eventos-01.md) | Casos de uso (3 casos de uso) | Em produção |
| [`DAtv-Eventos-01`](DAtv-Eventos-01.md), [`02`](DAtv-Eventos-02.md), [`03`](DAtv-Eventos-03.md) | Atividades de cada caso de uso | Em produção |
| [`DIhc-Eventos-01`](DIhc-Eventos-01.md) | Protótipo da tela, com eventos de interação E0 a E5 | Em produção |
| [`DSeq-Eventos-01`](DSeq-Eventos-01.md) a [`05`](DSeq-Eventos-05.md) | Sequência de cada atividade de interação | Em produção |
| [`DEst-Eventos-01`](DEst-Eventos-01.md) | Estados da tela | Em produção |
| [`DCmp-Eventos-01`](DCmp-Eventos-01.md) | Componentes do pacote | Em produção |
| [`DCla-Eventos-01`](DCla-Eventos-01.md), [`02`](DCla-Eventos-02.md) | Classes de cada componente | Em produção |
| [`Contrato-Eventos-01`](Contrato-Eventos-01.md) | Contratos das operações | Em produção |
| [`ECA-Eventos-01`](ECA-Eventos-01.md) | Regras ativas (3 regras) | Em produção |

A cascata de Eventos está completa em primeira versão. Falta a revisão da Pessoa D e a conferência das premissas abaixo. Entidades entregues para o modelo de dados: [`Evento`](../Integracao/entidades/Entidade-Evento.md), [`Regional`](../Integracao/entidades/Entidade-Regional.md) e [`Campus`](../Integracao/entidades/Entidade-Campus.md).

## Premissas e conferência com as capturas de tela (versão 3.2.0)

Parte do comportamento do app não aparece nos documentos da equipe. As premissas abaixo foram assumidas para modelar e estão marcadas nos itens como `P-EV-n`. A conferência com as 15 capturas de tela da versão 3.2.0 mostrou que **a tela de lista de Eventos (calendário) não está entre as capturas**; só aparece a página de um evento aberta no Navegador. Por isso quase todas as premissas seguem pendentes.

| Código | Premissa | Situação nas capturas | Itens afetados |
|---|---|---|---|
| P-EV-1 | A tela tem um seletor de regional visível para o usuário (o enunciado diz que os eventos são explorados por regional e por data) | **Pendente:** a tela não está nas capturas | `DIhc-Eventos-01`, `DSeq-Eventos-03` |
| P-EV-2 | A lista de regionais do seletor é fixa no app, e a regional inicial é a primeira da lista | **Pendente** (em Notícias a primeira aba é "GOIÂNIA") | `DSeq-Eventos-01`, `DCla-Eventos-01` |
| P-EV-3 | Ao trocar o mês, o primeiro dia do novo mês fica selecionado e a lista é recarregada | **Pendente** | `DSeq-Eventos-04`, `ECA-Eventos-01` |
| P-EV-4 | Cada evento mostra título e período; tocar abre a página dele no Navegador; evento sem endereço não reage ao toque | **Parcialmente confirmada:** tocar abre a página no portal da UFG (início > eventos > título), que mostra o título, o local ("Centro de Línguas, Câmpus Samambaia") e o período ("15 a 17 de Outubro 2026"). Falta conferir o que a lista mostra e o caso sem endereço | `DCdu-Eventos-01`, `DSeq-Eventos-05`, `DCla-Eventos-02` |
| P-EV-5 | A API tem a rota `GET /eventos` com os parâmetros `regional` (identificador) e `data` (aaaa-mm-dd), e devolve em JSON os eventos cujo período inclui a data (premissa de projeto, não observável no app) | Não observável | `DSeq-Eventos-01`, `DCla-Eventos-02` |
| P-EV-6 | Ao abrir a tela, a data selecionada é hoje | **Pendente** | `DCdu-Eventos-01`, `DSeq-Eventos-01` |

## Próximos passos da pasta

1. Obter uma captura da tela de lista de Eventos (calendário, seletor e lista) e conferir P-EV-1 a P-EV-3 e P-EV-6.
2. Pessoa D revisar os itens e registrar a revisão no fim de cada `.md`.
3. Atualizar o `DPac-Geral-01` com a dependência de `Regional` quando D decidir onde ela fica (pendência `D-INT-03`).
