# Restaurante Universitário

Cardápio por refeição e dia da semana.

- **Dono (autor):** Pessoa C
- **Revisor:** Pessoa D
- **Prefixo de código dos itens:** `RU` (ex.: `DAtv-RU-01`)

Cada item de informação desta pasta é um par de arquivos com o mesmo nome:
`<TIPO>-RU-<nn>.md` (item preenchido a partir do [modelo](../Template-Item.md)) e
`<TIPO>-RU-<nn>.puml` (fonte PlantUML do diagrama). Itens sem diagrama (DD, Contrato, ECA) têm só o `.md`.

## Como ler esta pasta

Os itens seguem a **ordem de produção do contrato-base** (casos de uso, atividades, protótipo de IHC, entidades, componentes e classes, sequência, estados, contratos e regras E-C-A). Cada item é um par de arquivos com o mesmo nome: o `.md` explica o item e o `.puml` tem o diagrama (a imagem `.png` é gerada a partir do `.puml`). O campo **Rastreia para** de cada `.md` indica de quais outros itens ele depende ou qual detalha. Autor: José Eduardo Gontijo de Carvalho (Pessoa C). Revisor: Phablo Tavares Paixão (Pessoa D).

Legenda de status: **Pronto** = revisado e no repositório (contrato, seção 10); **Em produção** = primeira versão escrita, ainda sem revisão; **A fazer** = ainda não iniciado.

## Itens da pasta

| Código | Título | Status |
|---|---|---|
| [`DCdu-RU-01`](DCdu-RU-01.md) | Casos de uso `UC06.1` e `UC06.2` (macro UC06 do `DCdu-Geral-01`) | Em produção |
| [`DAtv-RU-01`](DAtv-RU-01.md), [`02`](DAtv-RU-02.md) | Atividades de cada caso de uso (a `02` não consulta o servidor) | Em produção |
| [`DIhc-RU-01`](DIhc-RU-01.md) | Protótipo da tela RU (cartões das três refeições), eventos E0 a E2 | Em produção |
| [`DIhc-RU-02`](DIhc-RU-02.md) | Protótipo da tela da refeição (cor do dia, data, categorias, seletor vertical de dia e estado indisponível), eventos E0 a E2 | Em produção |
| [`DD-RU-01`](DD-RU-01.md) | Entradas de DD: `Cardapio`, `Refeicao` (por data), `ItemCardapio`, `CategoriaItem` e `TipoRefeicao` | Em produção |
| [`DSeq-RU-01`](DSeq-RU-01.md), [`02`](DSeq-RU-02.md) | Sequência de cada atividade de interação (tocar numa refeição, que carrega a semana; tocar num dia, que filtra em memória) | Em produção |
| [`DEst-RU-01`](DEst-RU-01.md), [`02`](DEst-RU-02.md) | Estados da tela RU e da tela da refeição | Em produção |
| [`DCmp-RU-01`](DCmp-RU-01.md) | Componentes do pacote (`TelasRU` e `FonteCardapio`) | Em produção |
| [`DCla-RU-01`](DCla-RU-01.md), [`02`](DCla-RU-02.md) | Classes de cada componente | Em produção |
| [`Contrato-RU-01`](Contrato-RU-01.md) | Contratos das operações | Em produção |
| [`ECA-RU-01`](ECA-RU-01.md) | Regras ativas (3 regras da tela da refeição e a regra confirmada do Jantar sem sábado) | Em produção |

A cascata de RU está completa e foi atualizada em 30/10/2026 com as novas capturas e a informação do autor sobre a carga semanal. Falta a revisão da Pessoa D e a conferência das premissas pendentes abaixo. Entidades entregues para o modelo de dados (o conteúdo é o mesmo do `DD-RU-01`): [`Cardapio`](../Integracao/entidades/Entidade-Cardapio.md), [`Refeicao`](../Integracao/entidades/Entidade-Refeicao.md), [`CategoriaItem`](../Integracao/entidades/Entidade-CategoriaItem.md) e [`ItemCardapio`](../Integracao/entidades/Entidade-ItemCardapio.md).

**Rótulos dos eventos de interação** (iguais em `DIhc`, `DEst`, `DSeq`, `DCla`, `Contrato` e `ECA`). A atividade `A1` de cada `DAtv` é a ação de interação que gera um `DSeq`.

| Tela | Rótulo | Evento | Operação | Atividade |
|---|---|---|---|---|
| RU (`DIhc-RU-01`) | E0 | Entrada na tela | `TelaRU.aoExibir()` | Passo interno de `DAtv-RU-01` |
| RU | E1 | Tocar no cartão de uma refeição | `TelaRU.aoTocarRefeicao(tipo)` | `DAtv-RU-01`, A1 (`DSeq-RU-01`) |
| RU | E2 | Seta de voltar | `TelaRU.aoVoltar()` | Navegação, sem atividade |
| Refeição (`DIhc-RU-02`) | E0 | Entrada ou retorno à tela | `TelaRefeicao.aoExibir()` | Dentro de `DSeq-RU-01` |
| Refeição | E1 | Tocar numa letra do seletor de dia (só no estado Exibindo) | `TelaRefeicao.aoEscolherDia(dia)` | `DAtv-RU-02`, A1 (`DSeq-RU-02`) |
| Refeição | E2 | Seta de voltar | `TelaRefeicao.aoVoltar()` | Navegação, sem atividade |

## Capturas consultadas

Todas da versão 3.2.0, iPhone.

- **1:** menu inicial, com o cartão RU.
- **13 e 17:** tela RU, com os três cartões de refeição e o aviso "Cardápio sujeito a alterações!".
- **14:** Café da Manhã (sexta-feira, 16 de outubro de 2026), com as quatro categorias, o seletor de seis letras e a barra verde.
- **22 a 25 e 27:** Almoço, um dia por captura (terça 27/10, quinta 29/10, sexta 30/10, sábado 31/10 e quarta 28/10): categorias do Almoço, cor da barra e do fundo conforme o dia, data por extenso e seletor de seis letras. As capturas 22 e 25 têm o ícone de modo avião com o cardápio exibido.
- **26:** Jantar (sexta-feira, 30/10): mesmas categorias e seletor de cinco letras, sem sábado.
- **30:** Jantar sem rede: barra azul, ilustração e "Cardápio indisponível.", sem data nem seletor.

Além das capturas, vale a **informação do autor do projeto**, José Eduardo (30/10/2026): ao abrir a tela de uma refeição, o app carrega o cardápio da semana inteira numa só chamada, e trocar o dia não chama o servidor.

## Premissas e conferência com as capturas de tela (versão 3.2.0)

O app tem duas telas (a partir do cartão RU do menu, captura 1): **RU**, com barra de título roxa e seta de voltar, um cartão com imagem para cada refeição e o aviso "Cardápio sujeito a alterações!" (capturas 13 e 17); e a **tela da refeição**, com seta de voltar, barra e fundo na cor do dia selecionado, a data por extenso, cartões por categoria e o seletor de dia em coluna vertical na borda esquerda, com seis letras (S, T, Q, Q, S, S) no Café da Manhã e no Almoço e cinco (S, T, Q, Q, S) no Jantar (capturas 14 e 22 a 27). A tela da refeição carrega a semana toda ao abrir, e trocar o dia só filtra os dados em memória (como a Rádio de `Radio/`). Sem rede, mostra a barra azul com a ilustração e "Cardápio indisponível." (captura 30). Os estados vazio e carregando não foram capturados e seguem o ciclo genérico do Comum (`DEst-Comum-01`).

| Código | Premissa | Situação nas capturas | Itens afetados |
|---|---|---|---|
| P-RU-1 | O RU tem três refeições: Café da Manhã, Almoço e Jantar | **Confirmada** (capturas 13 e 17) | `DCdu-RU-01`, `DAtv-RU-01`, `DIhc-RU-01`, `DEst-RU-01`, `DD-RU-01`, `Contrato-RU-01`, `Entidade-Refeicao` |
| P-RU-2 | A tela RU é estática, sem chamada ao servidor | **Não observável** (premissa de projeto) | `DCdu-RU-01`, `DAtv-RU-01`, `DIhc-RU-01`, `DEst-RU-01`, `DCmp-RU-01`, `DCla-RU-01`, `Contrato-RU-01`, `ECA-RU-01` |
| P-RU-3 | Ao abrir a tela da refeição, o app busca a semana inteira da refeição numa só chamada; trocar o dia filtra os dados em memória, sem chamada ao servidor | **Confirmada** pelo autor (30/10/2026) e coerente com as capturas 22 e 25, com o cardápio exibido em modo avião | `DCdu-RU-01`, `DAtv-RU-01`, `DAtv-RU-02`, `DIhc-RU-02`, `DSeq-RU-01`, `DSeq-RU-02`, `DEst-RU-02`, `DCmp-RU-01`, `DCla-RU-01`, `DCla-RU-02`, `DD-RU-01`, `Contrato-RU-01`, `ECA-RU-01`, `Entidade-Cardapio` |
| P-RU-4 | O seletor de dia vai de segunda a sábado (seis letras) no Café da Manhã e no Almoço e de segunda a sexta (cinco letras) no Jantar, que não tem sábado; domingo não tem letra em nenhuma refeição | **Confirmada** (capturas 14 e 22 a 27; seletor do Jantar de cinco letras na captura 26) | `DCdu-RU-01`, `DAtv-RU-02`, `DIhc-RU-02`, `DSeq-RU-02`, `DEst-RU-02`, `DCla-RU-01`, `DCla-RU-02`, `DD-RU-01`, `Contrato-RU-01`, `ECA-RU-01`, `Entidade-Refeicao` |
| P-RU-5 | Os itens aparecem em cartões por categoria. Café da Manhã: "Leite", "Fruta", "Quitanda (vegana)" e "Pães e quitandas". Almoço e Jantar: "Prato Proteico", "Opção Ovolactovegetariana", "Opção Vegana" e "Guarnição"; a descrição pode ter marcador, como "(1ª)" | **Confirmada** (captura 14 e capturas 22 a 27) | `DCdu-RU-01`, `DCla-RU-01`, `DD-RU-01`, `DIhc-RU-02`, `Contrato-RU-01`, `Entidade-CategoriaItem`, `Entidade-ItemCardapio` |
| P-RU-6 | Pode haver categorias abaixo de "Guarnição" no Almoço e no Jantar; e não se sabe se "Pão francês / Bolo formigueiro" é um item ou dois, nem qual é o separador de itens da mesma categoria | **Pendente:** as capturas são cortadas em "Guarnição" | `DIhc-RU-02`, `DD-RU-01`, `Contrato-RU-01`, `Entidade-CategoriaItem`, `Entidade-ItemCardapio` |
| P-RU-7 | A barra de título e o fundo da tela da refeição têm a cor do dia selecionado: terça roxo, quarta vermelho, quinta laranja, sexta verde, sábado marrom | **Confirmada** (capturas 14 e 22 a 27) | `DCdu-RU-01`, `DIhc-RU-02`, `DSeq-RU-02`, `DEst-RU-02`, `DCla-RU-01`, `Contrato-RU-01` |
| P-RU-8 | Estado indisponível: barra de título azul com a seta de voltar, ilustração de documentos e a mensagem "Cardápio indisponível.", sem data nem seletor de dia | **Confirmada** (captura 30, Jantar em modo avião). Que os outros tipos de `ErroApi` se comportam igual é suposição | `DCdu-RU-01`, `DAtv-RU-01`, `DIhc-RU-02`, `DSeq-RU-01`, `DEst-RU-02`, `Contrato-RU-01`, `ECA-RU-01` |
| P-RU-9 | Estado vazio (a semana sem refeições) e dia sem itens: mensagem genérica de vazio do Comum, como na Rádio; Carregando e Vazio com o mesmo layout do indisponível (barra azul, sem data nem seletor); o dia sem itens mantém a data e o seletor | **Pendente:** nenhum desses estados foi capturado | `DCdu-RU-01`, `DAtv-RU-01`, `DAtv-RU-02`, `DIhc-RU-02`, `DSeq-RU-01`, `DSeq-RU-02`, `DEst-RU-02`, `Contrato-RU-01`, `ECA-RU-01` |
| P-RU-10 | A API devolve as refeições da semana de uma refeição (rota `GET /cardapio`, com o parâmetro `refeicao`, sem data), cada uma com a sua data e os seus itens (categoria e descrição) | **Não observável** (premissa de projeto) | `DCdu-RU-01`, `DSeq-RU-01`, `DCla-RU-01`, `DCla-RU-02`, `DD-RU-01`, `Contrato-RU-01`, `Entidade-Cardapio` |
| P-RU-11 | A seta de voltar da tela da refeição leva à tela RU, e a da tela RU leva ao menu inicial (navegação em pilha) | **Parcial:** a seta aparece nas duas telas (capturas 13, 14, 22 a 27 e 30); o destino é suposição | `DCdu-RU-01`, `DIhc-RU-01`, `DIhc-RU-02`, `DEst-RU-01`, `DEst-RU-02`, `Contrato-RU-01` |
| P-RU-12 | A segunda-feira tem a barra e o fundo azuis (cor da primeira letra do seletor) e o cardápio carrega como os demais dias | **Pendente:** nenhuma captura é da segunda-feira; a cor é inferida | `DIhc-RU-02`, `Contrato-RU-01` |
| P-RU-13 | Quando hoje não tem letra no seletor (domingo, ou sábado no Jantar), a tela seleciona a segunda-feira da semana que contém hoje; qual semana a API devolve nesses dias também não se sabe | **Pendente:** as capturas são de dias úteis e de sábado, só do Almoço | `DCdu-RU-01`, `DAtv-RU-01`, `DIhc-RU-02`, `DSeq-RU-01`, `DEst-RU-02`, `DCla-RU-01`, `Contrato-RU-01`, `ECA-RU-01`, `Entidade-Refeicao` |

## Próximos passos da pasta

1. Capturar o que falta: a tela da refeição na segunda-feira (P-RU-12), a rolagem até o fim do Almoço e do Jantar, para ver se há categorias abaixo de "Guarnição" (P-RU-6), e um dia ou uma semana sem cardápio, se for possível (P-RU-9).
2. Abrir o app num domingo e, no Jantar, num sábado, para ver qual dia é selecionado e qual semana é carregada (P-RU-13); e conferir o destino da seta de voltar nas duas telas (P-RU-11).
3. Pessoa D revisar os itens e registrar a revisão no fim de cada `.md`; decidir na integração se `Cardapio` fica no `DD-Geral` (o app não o usa: `DD-RU-01`) e se o dia da semana reutiliza o `DiaSemana` da Rádio.
