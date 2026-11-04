# Avaliação de UA – consultar notas

Evolução: notas por UA, por área de conhecimento (CNPq) e da UFG.

- **Dono (autor):** Phablo Tavares Paixão
- **Revisor:** Maicon Brendo da Silva
- **Prefixo de código dos itens:** `AvalConsultar` (ex.: `DAtv-AvalConsultar-01`)

Cada item de informação desta pasta é um par de arquivos com o mesmo nome:
`<TIPO>-AvalConsultar-<nn>.md` (item preenchido a partir do [modelo](../Template-Item.md)) e
`<TIPO>-AvalConsultar-<nn>.puml` (fonte PlantUML do diagrama). Itens sem diagrama (DD, Contrato, ECA) têm só o `.md`.

## Itens

| Item | Conteúdo | Status |
|---|---|---|
| [`DCdu-AvalConsultar-01`](DCdu-AvalConsultar-01.md) | Casos de uso UC10.1 a UC10.3 | Em produção |
| [`DAtv-AvalConsultar-01`](DAtv-AvalConsultar-01.md) | Atividades do UC10.1 (UFG e áreas) | Em produção |
| [`DAtv-AvalConsultar-02`](DAtv-AvalConsultar-02.md) | Atividades do UC10.2 (UAs de uma área) | Em produção |
| [`DAtv-AvalConsultar-03`](DAtv-AvalConsultar-03.md) | Atividades do UC10.3 (dimensões de uma UA) | Em produção |
| [`DIhc-AvalConsultar-01`](DIhc-AvalConsultar-01.md) | Protótipo da `TelaNotas` | Em produção |
| [`DIhc-AvalConsultar-02`](DIhc-AvalConsultar-02.md) | Protótipo da `TelaNotasArea` | Em produção |
| [`DIhc-AvalConsultar-03`](DIhc-AvalConsultar-03.md) | Protótipo da `TelaNotasUA` | Em produção |
| [`DD-AvalConsultar-01`](DD-AvalConsultar-01.md) | Entidades derivadas e origem de cada nota | Em produção |
| [`DCmp-AvalConsultar-01`](DCmp-AvalConsultar-01.md) | Componentes do pacote | Em produção |
| [`DCla-AvalConsultar-01`](DCla-AvalConsultar-01.md) | Classes do componente `TelasNotas` | Em produção |
| [`DCla-AvalConsultar-02`](DCla-AvalConsultar-02.md) | Classes das fontes de notas | Em produção |
| [`DSeq-AvalConsultar-01`](DSeq-AvalConsultar-01.md) | Sequência de A1: tocar em "Ver notas" e carregar as notas da UFG | Em produção |
| [`DSeq-AvalConsultar-02`](DSeq-AvalConsultar-02.md) | Sequência de A2: tocar em uma área e carregar as notas das UAs | Em produção |
| [`DSeq-AvalConsultar-03`](DSeq-AvalConsultar-03.md) | Sequência de A3: tocar em uma UA e carregar as notas por dimensão | Em produção |
| [`DEst-AvalConsultar-01`](DEst-AvalConsultar-01.md) | Estados da TelaNotas | Em produção |
| [`DEst-AvalConsultar-02`](DEst-AvalConsultar-02.md) | Estados da TelaNotasArea | Em produção |
| [`DEst-AvalConsultar-03`](DEst-AvalConsultar-03.md) | Estados da TelaNotasUA | Em produção |
| [`Contrato-AvalConsultar-01`](Contrato-AvalConsultar-01.md) | Contratos de Avaliação – Consultar notas | Em produção |
| [`ECA-AvalConsultar-01`](ECA-AvalConsultar-01.md) | Regras E-C-A de Avaliação – Consultar notas | Em produção |

## Premissas

A consulta de notas é evolução do app e não tem comportamento observado. O que o enunciado não define está abaixo.

| Código | Premissa | Origem |
|---|---|---|
| P-AC-1 | A consulta começa pelo botão "Ver notas" da `TelaAvaliacao` (E2 de `DIhc-AvalRegistrar-01`), que abre a `TelaNotas` (confirma a P-AR-1) | Decisão de 31/10/2026 (`Docs/decisoes.md`) |
| P-AC-2 | Navegação em três níveis: `TelaNotas` (UFG e áreas CNPq) → `TelaNotasArea` (UAs da área) → `TelaNotasUA` (dimensões da UA); cada tela faz a sua carga no servidor | Decisão de 31/10/2026 |
| P-AC-3 | Nota da UA = média das notas de suas avaliações; média da área = média das notas das UAs da área; nota da UFG = média das notas de todas as UAs (enunciado) | Decisão de 31/10/2026 |
| P-AC-4 | UA sem avaliação aparece com "Sem avaliações" e não entra na média da área nem na da UFG; área ou UFG sem nenhuma UA avaliada também mostra "Sem avaliações"; na `TelaNotasUA`, é o estado vazio | Decisão de 31/10/2026 |
| P-AC-5 | Notas exibidas na escala de 0 a 5, com uma casa decimal | Premissa de projeto |
| P-AC-6 | O Servidor/API calcula as médias a cada consulta e entrega as notas prontas; só as notas por questão são armazenadas, e o app só exibe | Decisão de 01/11/2026 |
| P-AC-7 | Listas na ordem recebida do servidor, sem busca, filtro nem ordenação no app | Premissa de projeto |
| P-AC-8 | A nota de uma dimensão na UA é a média, entre as avaliações da UA, da nota daquela dimensão em cada avaliação; mostram-se as dimensões que aparecem nas avaliações da UA, agregadas pelo `id` (`DD-AvalRegistrar-01`, "Para quem consome", item 3) | Premissa de projeto |
| P-AC-9 | A API tem as rotas `GET /avaliacao/notas`, `GET /avaliacao/notas/area` (parâmetro `area`) e `GET /avaliacao/notas/unidade` (parâmetro `unidade`), com corpo em JSON; não são observáveis | Premissa de projeto (não observável) |
