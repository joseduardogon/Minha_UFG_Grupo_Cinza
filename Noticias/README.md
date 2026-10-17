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
| [`DCdu-Noticias-01`](DCdu-Noticias-01.md) | Casos de uso (2 casos de uso) | Em produção |
| [`DAtv-Noticias-01`](DAtv-Noticias-01.md), [`02`](DAtv-Noticias-02.md) | Atividades de cada caso de uso | Em produção |
| [`DIhc-Noticias-01`](DIhc-Noticias-01.md) | Protótipo da tela, com eventos de interação E0 a E2 | Em produção |
| `DSeq-Noticias-01` a `03` | Sequência das atividades | A fazer |
| `DEst-Noticias-01` | Estados da tela | A fazer |
| `DCmp-Noticias-01`, `DCla-Noticias-nn` | Componentes e classes | A fazer |
| `Contrato-Noticias-01`, `ECA-Noticias-01` | Contratos e regras ativas | A fazer |

Etapa atual: casos de uso, atividades e protótipo (primeira versão), já conferidos com as capturas de tela. Notícias segue o mesmo padrão de Eventos (lista do servidor filtrada por regional), então boa parte do restante é reaproveitamento. Entidade entregue para o modelo de dados: [`Noticia`](../Integracao/entidades/Entidade-Noticia.md).

## Premissas e conferência com as capturas de tela (versão 3.2.0)

| Código | Premissa | Situação nas capturas | Itens afetados |
|---|---|---|---|
| P-NO-1 | A regional é escolhida pelo usuário | **Confirmada:** abaixo do título há uma faixa de abas de regional. Só a aba "GOIÂNIA" aparece na captura; as outras regionais não estão visíveis | `DIhc-Noticias-01`, `DAtv-Noticias-01` |
| P-NO-2 | A regional inicial é a primeira da faixa de abas | **Confirmada:** "GOIÂNIA" aparece selecionada ao abrir | `DCdu-Noticias-01` |
| P-NO-3 | Cada notícia mostra imagem, título e resumo, e ao ser tocada abre a página dela no Navegador, sem tela de detalhe | **Confirmada:** o cartão tem imagem, título e resumo; a página aberta (portal da UFG, início > notícias) mostra o título e a data e hora de publicação | `DCdu-Noticias-01`, `DAtv-Noticias-02`, `Entidade-Noticia` |
| P-NO-4 | A API tem a rota `GET /noticias` com o parâmetro `regional` (premissa de projeto, não observável no app) | Não observável | `Entidade-Noticia` |
| P-NO-5 | A lista vem da mais recente para a mais antiga | **Pendente:** a data não aparece no cartão e a ordem não é verificável; a data só aparece na página da notícia | `DIhc-Noticias-01`, `Entidade-Noticia` |
| P-NO-6 | A lista de regionais de Notícias é a mesma de Eventos | **Pendente:** falta ver as demais abas | `DCdu-Noticias-01` |

## Próximos passos da pasta

1. Obter uma captura com as demais abas de regional e conferir P-NO-5 e P-NO-6.
2. Produzir sequências, estados, componentes e classes, contratos e regras E-C-A.
3. Pessoa D revisar os itens.
