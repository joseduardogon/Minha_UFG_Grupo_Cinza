# Restaurante Universitário

Cardápio por refeição e dia da semana.

- **Dono (autor):** Pessoa C
- **Revisor:** Pessoa D
- **Prefixo de código dos itens:** `RU` (ex.: `DAtv-RU-01`)

Cada item de informação desta pasta é um par de arquivos com o mesmo nome:
`<TIPO>-RU-<nn>.md` (item preenchido a partir do [modelo](../Template-Item.md)) e
`<TIPO>-RU-<nn>.puml` (fonte PlantUML do diagrama). Itens sem diagrama (DD, Contrato, ECA) têm só o `.md`.

## Como ler esta pasta

Os itens seguem a **ordem de produção do contrato-base** (casos de uso, atividades, protótipo de IHC, componentes e classes, sequência, estados, contratos e regras E-C-A). Cada item é um par de arquivos com o mesmo nome: o `.md` explica o item e o `.puml` tem o diagrama (a imagem `.png` é gerada a partir do `.puml`). O campo **Rastreia para** de cada `.md` indica de quais outros itens ele depende ou qual detalha. Autor: José Eduardo Gontijo de Carvalho (Pessoa C). Revisor: Phablo Tavares Paixão (Pessoa D).

Legenda de status: **Pronto** = revisado e no repositório (contrato, seção 10); **Em produção** = primeira versão escrita, ainda sem revisão; **A fazer** = ainda não iniciado.

## Itens da pasta

| Código | Título | Status |
|---|---|---|
| [`DCdu-RU-01`](DCdu-RU-01.md) | Casos de uso (2 casos de uso) | Em produção |
| [`DAtv-RU-01`](DAtv-RU-01.md), [`02`](DAtv-RU-02.md) | Atividades de cada caso de uso | Em produção |
| [`DIhc-RU-01`](DIhc-RU-01.md) | Protótipo da tela RU (cartões das três refeições) | Em produção |
| [`DIhc-RU-02`](DIhc-RU-02.md) | Protótipo da tela da refeição (data, itens por categoria e seletor de dia) | Em produção |
| `DSeq-RU-01` e `02` | Sequência das atividades | A fazer |
| `DEst-RU-01` e `02` | Estados das telas | A fazer |
| `DCmp-RU-01`, `DCla-RU-nn` | Componentes e classes | A fazer |
| `Contrato-RU-01`, `ECA-RU-01` | Contratos e regras ativas (inclui a regra "não há jantar aos sábados") | A fazer |

Etapa atual: casos de uso, atividades e protótipos (primeira versão), já conferidos com as capturas de tela. O restante da cascata vem depois de Eventos. Entidades entregues para o modelo de dados: [`Cardapio`](../Integracao/entidades/Entidade-Cardapio.md), [`Refeicao`](../Integracao/entidades/Entidade-Refeicao.md), [`CategoriaItem`](../Integracao/entidades/Entidade-CategoriaItem.md) e [`ItemCardapio`](../Integracao/entidades/Entidade-ItemCardapio.md).

## Premissas e conferência com as capturas de tela (versão 3.2.0)

O app tem duas telas: **RU**, com um cartão (com imagem) para cada refeição e o aviso "Cardápio sujeito a alterações!"; e a **tela da refeição**, com a data por extenso, cartões por categoria e o seletor de dia na lateral esquerda (letras S, T, Q, Q, S, S).

| Código | Premissa | Situação nas capturas | Itens afetados |
|---|---|---|---|
| P-RU-1 | A tela RU tem três refeições (Café da Manhã, Almoço e Jantar) e é estática, sem chamada ao servidor | **Refeições confirmadas.** Que a tela não consulta o servidor é suposição | `DCdu-RU-01`, `DAtv-RU-01`, `DIhc-RU-01` |
| P-RU-2 | Ao abrir a tela da refeição, o dia selecionado é hoje; trocar o dia pede nova consulta à API, como prevê `DCla-Comum-03` | **Confirmada** a seleção de hoje (sexta-feira, 16 de outubro de 2026, destacada). A nova consulta ao trocar o dia é suposição | `DAtv-RU-01`, `DAtv-RU-02` |
| P-RU-3 | Aos sábados não há jantar | **Pendente:** o que a tela mostra no jantar de sábado não está nas capturas | `DCdu-RU-01`, `Entidade-Refeicao` |
| P-RU-4 | O seletor de dias vai de segunda a sábado | **Confirmada:** seis letras, de segunda a sábado, sem domingo; a data por extenso muda com o dia | `DIhc-RU-02`, `Entidade-Refeicao` |
| P-RU-5 | Os itens aparecem em cartões por categoria, e as categorias mudam de uma refeição para outra | **Confirmada para o Café da Manhã:** "Leite", "Fruta", "Quitanda (vegana)" e "Pães e quitandas". Faltam Almoço e Jantar | `DCdu-RU-01`, `Entidade-CategoriaItem` |
| P-RU-6 | A API devolve o cardápio de uma refeição em uma data (rota `GET /cardapio`, com os parâmetros `refeicao` e `data`; premissa de projeto, não observável no app) | Não observável | `Entidade-Cardapio` |

## Próximos passos da pasta

1. Obter capturas do Almoço, do Jantar e do jantar de sábado, e conferir P-RU-3 e P-RU-5.
2. Produzir as sequências, os estados, os componentes e as classes, os contratos e as regras E-C-A, reaproveitando o padrão de Eventos e os componentes do pacote Comum.
3. Pessoa D revisar os itens.
