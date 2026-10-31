# Eventos

Calendário mensal, filtro por data, lista por regional e estado sem eventos.

- **Dono (autor):** Pessoa C
- **Revisor:** Pessoa D
- **Prefixo de código dos itens:** `Eventos` (ex.: `DAtv-Eventos-01`)

Cada item de informação desta pasta é um par de arquivos com o mesmo nome:
`<TIPO>-Eventos-<nn>.md` (item preenchido a partir do [modelo](../Template-Item.md)) e
`<TIPO>-Eventos-<nn>.puml` (fonte PlantUML do diagrama). Itens sem diagrama (DD, Contrato, ECA) têm só o `.md`.

## Como ler esta pasta

Os itens seguem a **ordem de produção do contrato-base** (casos de uso, atividades, protótipo de IHC, dicionário de dados, componentes e classes, sequência, estados, contratos e regras E-C-A). Cada item é um par de arquivos com o mesmo nome: o `.md` explica o item e o `.puml` tem o diagrama (a imagem `.png` é gerada a partir do `.puml`). O campo **Rastreia para** de cada `.md` indica de quais outros itens ele depende ou qual detalha. Autor: José Eduardo Gontijo de Carvalho (Pessoa C). Revisor: Phablo Tavares Paixão (Pessoa D).

Legenda de status: **Pronto** = revisado e no repositório (contrato, seção 10); **Em produção** = escrito, ainda sem revisão do revisor; **A fazer** = ainda não iniciado.

**Rótulos dos eventos de interação** (iguais em `DIhc`, `DEst`, `DAtv`, `DSeq` e `Contrato`): E0 entrada na tela (`aoExibir`), E1 escolher regional (aba, `aoEscolherRegional`), E2 mês anterior, E3 mês seguinte (`aoTrocarMes`), E4 escolher data (`aoEscolherData`), E5 tocar em evento (`aoTocarEvento`), E6 seta de voltar (`aoVoltar`).

**Códigos de caso de uso:** UC04.1, UC04.2 e UC04.3, detalhes do caso de uso macro UC04 do `DCdu-Geral-01`.

## Itens da pasta

| Código | Título | Status |
|---|---|---|
| [`DCdu-Eventos-01`](DCdu-Eventos-01.md) | Casos de uso (UC04.1 a UC04.3) | Em produção |
| [`DAtv-Eventos-01`](DAtv-Eventos-01.md), [`02`](DAtv-Eventos-02.md), [`03`](DAtv-Eventos-03.md) | Atividades de cada caso de uso | Em produção |
| [`DIhc-Eventos-01`](DIhc-Eventos-01.md) | Protótipo da tela, com eventos de interação E0 a E6 | Em produção |
| [`DD-Eventos-01`](DD-Eventos-01.md) | Entrada de DD: Regional, Campus e Evento | Em produção |
| [`DCmp-Eventos-01`](DCmp-Eventos-01.md) | Componentes do pacote | Em produção |
| [`DCla-Eventos-01`](DCla-Eventos-01.md), [`02`](DCla-Eventos-02.md) | Classes de cada componente | Em produção |
| [`DSeq-Eventos-01`](DSeq-Eventos-01.md) a [`05`](DSeq-Eventos-05.md) | Sequência de cada atividade de interação (a 05 inclui o retorno do Navegador) | Em produção |
| [`DEst-Eventos-01`](DEst-Eventos-01.md) | Estados da tela | Em produção |
| [`Contrato-Eventos-01`](Contrato-Eventos-01.md) | Contratos das operações | Em produção |
| [`ECA-Eventos-01`](ECA-Eventos-01.md) | Regras ativas (4 regras) | Em produção |

A cascata de Eventos está completa e já foi conferida com a tela de lista capturada em 30/10/2026. Falta a revisão da Pessoa D e a conferência das premissas pendentes abaixo. Entidades entregues para o modelo de dados (mesmo conteúdo do `DD-Eventos-01`): [`Evento`](../Integracao/entidades/Entidade-Evento.md), [`Regional`](../Integracao/entidades/Entidade-Regional.md) e [`Campus`](../Integracao/entidades/Entidade-Campus.md).

## Capturas consultadas (versão 3.2.0)

Capturas da versão 3.2.0 (iPhone) que dizem algo sobre Eventos. A lista de Eventos não existia no primeiro conjunto de 15 capturas; as capturas 19, 28 e 29 (30/10/2026) a mostram.

| Captura | O que mostra | Uso nesta pasta |
|---|---|---|
| 1 | Menu inicial, com o cartão "Eventos" | Entrada na funcionalidade (UC04.1) |
| 8 | Página de um evento no portal da UFG, aberta no Navegador: "Semana das Bibliotecas Humanas...", "Local: Centro de Línguas, Câmpus Samambaia", "Período do Evento: 15 a 17 de Outubro 2026" | Existência da página aberta no Navegador (UC04.3). O local aparece só na página do portal |
| 19 | **Lista de Eventos em 30/10/2026:** barra roxa "Eventos" com seta de voltar; cartão de calendário (setas, "Outubro", "2026", DOM a SAB, grade com células vazias antes do dia 1, dia 30 com círculo branco); aba "GOIÂNIA" única e sublinhada; cartões com miniatura circular, título e período "19/10/2026 à 30/10/2026" | `DIhc-Eventos-01` (desenho), P-EV-1, P-EV-2, P-EV-6, P-EV-9 |
| 21 | Página de outro evento no portal: "Local: Biblioteca Seccional Cepae Prof. Geraldo Faria Campos, Campus Samambaia", "Período do Evento: 19 a 30 de Outubro 2026" | Confirma que o local só está na página do portal, não no cartão (fora do modelo) |
| 28 | **Novembro de 2026:** o dia 30 continua selecionado; um evento de "30/09/2026 à 14/12/2026" na lista | P-EV-7 (mês mantém o dia), P-EV-9 (evento com intervalo aparece em todos os dias) |
| 29 | **Dezembro de 2026, dia 30:** ilustração, "Sem eventos", "Não há eventos para esse dia!"; a aba "GOIÂNIA" não aparece e o calendário continua visível | P-EV-7, P-EV-10, estado Vazio de `DEst-Eventos-01` |

Os estados Carregando e Indisponível de Eventos não foram capturados e seguem o ciclo genérico de `DEst-Comum-01` (P-EV-11). Notícias e RU têm capturas próprias de indisponibilidade; não se transpõe a de Notícias (corpo em branco) para Eventos sem captura.

## Premissas e conferência com as capturas de tela (versão 3.2.0)

As premissas abaixo estão marcadas nos itens como `P-EV-n`. Cada item listado como afetado cita a premissa no próprio texto. Com as capturas 19, 28 e 29, parte delas foi **confirmada**, uma foi **refutada** e as demais seguem **pendentes** ou **não observáveis**.

| Código | Premissa | Situação nas capturas | Itens afetados |
|---|---|---|---|
| P-EV-1 | Composição da tela: barra de título roxa com a seta de voltar; cartão de calendário (setas de mês, mês, ano, cabeçalho DOM a SAB, grade com células vazias antes do dia 1, dia selecionado com círculo branco); faixa de regional em abas; cartões de evento com miniatura circular, título e período "dd/mm/aaaa à dd/mm/aaaa", sem local e sem horário | **Confirmada** (capturas 19, 28 e 29). O que o cartão mostra se o evento não tiver imagem não foi observado | `DCdu-Eventos-01`, `DIhc-Eventos-01`, `DEst-Eventos-01`, `DSeq-Eventos-02`, `DCla-Eventos-01`, `DCla-Eventos-02`, `Contrato-Eventos-01`, `DD-Eventos-01`, `Entidade-Evento` |
| P-EV-2 | A regional é escolhida em abas e a regional inicial é a primeira; a lista de regionais é fixa no app (a tela a recebe como `regionaisOferecidas`) | **Parcialmente confirmada.** Confirmado: abas, só "GOIÂNIA" visível e selecionada ao abrir (capturas 19, 28 e 29). **Pendente:** lista fixa no app, nome e número das outras regionais, efeito de tocar em outra aba | `DCdu-Eventos-01`, `DAtv-Eventos-01`, `DIhc-Eventos-01`, `DSeq-Eventos-01`, `DSeq-Eventos-03`, `DEst-Eventos-01`, `DCla-Eventos-01`, `Contrato-Eventos-01`, `ECA-Eventos-01`, `DD-Eventos-01`, `Entidade-Regional` |
| P-EV-3 | (Antiga) Ao trocar o mês, o primeiro dia do novo mês fica selecionado | **Refutada.** Capturas 19, 28 e 29: o dia 30 permanece selecionado em outubro, novembro e dezembro. **Decisão corrigida:** vale o número do dia mantido (P-EV-7 e P-EV-8); a modelagem foi alterada em `CalendarioEventos.trocarMes`. O código P-EV-3 não é reaproveitado | `DCla-Eventos-01`, `DSeq-Eventos-04`, `Contrato-Eventos-01` (só registram a correção) |
| P-EV-4 | Tocar em um cartão de evento com endereço abre a página dele no Navegador; sem endereço, o toque não tem efeito | **Pendente.** Só a página já aberta foi observada (capturas 8 e 21); o toque no cartão e o caso sem endereço não foram capturados | `DCdu-Eventos-01`, `DAtv-Eventos-03`, `DIhc-Eventos-01`, `DSeq-Eventos-05`, `DEst-Eventos-01`, `DCla-Eventos-02`, `Contrato-Eventos-01`, `DD-Eventos-01`, `Entidade-Evento` |
| P-EV-5 | A API tem a rota `GET /eventos` com os parâmetros `regional` (identificador) e `data` (aaaa-mm-dd), e devolve em JSON os eventos cujo período inclui a data, com o endereço da miniatura (premissa de projeto) | **Não observável** no app | `DCdu-Eventos-01`, `DSeq-Eventos-01`, `DCla-Eventos-02`, `Contrato-Eventos-01`, `DD-Eventos-01`, `Entidade-Evento` |
| P-EV-6 | Ao abrir a tela pelo menu, a data selecionada é hoje | **Confirmada** (captura 19: dia 30 selecionado em 30/10/2026) | `DCdu-Eventos-01`, `DAtv-Eventos-01`, `DIhc-Eventos-01`, `DSeq-Eventos-01`, `DEst-Eventos-01`, `DCla-Eventos-01`, `Contrato-Eventos-01` |
| P-EV-7 | Ao trocar o mês, o número do dia selecionado é mantido | **Confirmada** (capturas 19, 28 e 29: 30 de outubro, 30 de novembro, 30 de dezembro) | `DCdu-Eventos-01`, `DAtv-Eventos-02`, `DIhc-Eventos-01`, `DSeq-Eventos-04`, `DEst-Eventos-01`, `DCla-Eventos-01`, `Contrato-Eventos-01`, `ECA-Eventos-01` |
| P-EV-8 | Se o novo mês é mais curto que o número do dia (por exemplo, 31 de outubro para novembro), a data selecionada passa ao último dia do mês | **Pendente.** Caso não observado; é premissa de projeto | `DCdu-Eventos-01`, `DAtv-Eventos-02`, `DIhc-Eventos-01`, `DSeq-Eventos-04`, `DEst-Eventos-01`, `DCla-Eventos-01`, `Contrato-Eventos-01`, `ECA-Eventos-01` |
| P-EV-9 | Um evento com intervalo de datas aparece na lista de todos os dias do intervalo | **Confirmada** (captura 19: "19/10/2026 à 30/10/2026" listado em 30/10; captura 28: "30/09/2026 à 14/12/2026" listado em 30/11) | `DCdu-Eventos-01`, `DIhc-Eventos-01`, `DD-Eventos-01`, `Entidade-Evento` |
| P-EV-10 | Sem eventos na data, a tela mostra uma ilustração, "Sem eventos" e "Não há eventos para esse dia!"; o calendário continua visível e a aba de regional some | **Confirmada** (captura 29). Por isso E1 só ocorre em EXIBINDO, e E2, E3 e E4 ocorrem também em VAZIO | `DCdu-Eventos-01`, `DAtv-Eventos-01`, `DIhc-Eventos-01`, `DSeq-Eventos-01`, `DSeq-Eventos-02`, `DSeq-Eventos-03`, `DSeq-Eventos-04`, `DEst-Eventos-01`, `DCla-Eventos-01`, `Contrato-Eventos-01` |
| P-EV-11 | O estado indisponível de Eventos segue o ciclo genérico; supõe-se o calendário visível e a aba de regional oculta | **Pendente.** Não capturado em Eventos (em Notícias, captura 31, o corpo fica em branco; não se sabe se vale aqui) | `DCdu-Eventos-01`, `DAtv-Eventos-01`, `DIhc-Eventos-01`, `DSeq-Eventos-01`, `DEst-Eventos-01`, `Contrato-Eventos-01` |
| P-EV-12 | Tocar em um dia do calendário o seleciona e a lista passa a mostrar os eventos dele | **Pendente.** O toque em si não foi capturado; só o dia selecionado resultante (capturas 28 e 29, após trocar o mês) | `DCdu-Eventos-01`, `DAtv-Eventos-01`, `DIhc-Eventos-01`, `DSeq-Eventos-02`, `DEst-Eventos-01`, `ECA-Eventos-01`, `Contrato-Eventos-01` |
| P-EV-13 | O app recarrega a lista da API a cada troca de mês, de dia ou de regional (e não filtra em memória) | **Não observável** no app; o modelo consulta a API (`recarregar()`) | `DIhc-Eventos-01`, `DSeq-Eventos-01`, `DSeq-Eventos-02`, `DSeq-Eventos-04`, `DEst-Eventos-01`, `Contrato-Eventos-01` |
| P-EV-14 | A ordem da lista é a recebida da API, sem reordenação no app | **Pendente.** A ordem vista na captura 19 (término em 30/10, 13/11 e 14/12; início em 19/10, 13/10 e 30/09) não permite concluir o critério | `DIhc-Eventos-01`, `DCla-Eventos-02`, `Contrato-Eventos-01` |

Decisões de modelagem relacionadas:

- O **local** do evento não é atributo de `Evento`: aparece só na página do portal (capturas 8 e 21) e o cartão da lista não o mostra (captura 19).
- `Evento` ganhou o atributo opcional **`urlImagem`**, pois o cartão mostra uma miniatura circular (capturas 19 e 28) e a tela precisa de um dado de onde tirá-la (`DD-Eventos-01`, `DCla-Eventos-02`).
- **Decisão corrigida:** `CalendarioEventos.trocarMes` deixou de selecionar o dia 1 e passou a manter o número do dia (P-EV-3 refutada, P-EV-7 e P-EV-8). A mudança está em `DCla-Eventos-01`, `Contrato-Eventos-01`, `DSeq-Eventos-04`, `DAtv-Eventos-02`, `DCdu-Eventos-01`, `ECA-Eventos-01` (ECA-EV-01) e `DEst-Eventos-01`.
- A faixa de abas de regional só existe no estado EXIBINDO: o evento E1 sai somente dele (`DEst-Eventos-01`), enquanto os eventos de calendário (E2, E3 e E4) saem de qualquer estado de resultado.

## Próximos passos da pasta

1. Capturar o que ainda falta de Eventos: o **toque em um dia** e o **toque em um cartão** (P-EV-12, P-EV-4), inclusive um evento sem endereço; a troca de mês para um **mês mais curto que o dia** (por exemplo, a partir do dia 31, P-EV-8); a tela com **mais de uma regional** (P-EV-2); a tela de Eventos em **modo avião**, para o estado indisponível (P-EV-11); e a **ordem** da lista em um dia com muitos eventos (P-EV-14). Se o app recarrega da API ao trocar mês ou dia (P-EV-13) só pode ser inferido por teste de rede, não por captura de tela.
2. Pessoa D revisar os itens e registrar a revisão no fim de cada `.md`.
3. Pessoa D decidir onde ficam `Regional` e `Campus` (pendência `D-INT-03`) e atualizar o `DPac-Geral-01` com a dependência; criar `DD-Geral-01` e `DDados-Geral-01`, que o `DD-Eventos-01` referencia; incluir `Evento.urlImagem` na consolidação do dicionário de dados.
