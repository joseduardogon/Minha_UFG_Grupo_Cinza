# Avaliação de UA – consultar notas

Evolução: notas por UA, por área de conhecimento (CNPq) e da UFG.

- **Dono (autor):** Pessoa B
- **Revisor:** Pessoa A
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

## Premissas

A consulta de notas é evolução do app e não tem comportamento observado. O que o enunciado não define está abaixo.

| Código | Premissa | Origem |
|---|---|---|
| P-AC-1 | A consulta começa pelo botão "Ver notas" da `TelaAvaliacao` (E2 de `DIhc-AvalRegistrar-01`), que abre a `TelaNotas` (confirma a P-AR-1) | Decisão de 31/10/2026 (`Docs/decisoes.md`) |
| P-AC-2 | Navegação em três níveis: `TelaNotas` (UFG e áreas CNPq) → `TelaNotasArea` (UAs da área) → `TelaNotasUA` (dimensões da UA); cada tela faz a sua carga no servidor | Decisão de 31/10/2026 |
| P-AC-3 | Nota da UA = média das notas de suas avaliações; média da área = média das notas das UAs da área; nota da UFG = média das notas de todas as UAs (enunciado) | Decisão de 31/10/2026 |
| P-AC-4 | UA sem avaliação aparece com "Sem avaliações" e não entra na média da área nem na da UFG; área ou UFG sem nenhuma UA avaliada também mostra "Sem avaliações"; na `TelaNotasUA`, é o estado vazio | Decisão de 31/10/2026 |
| P-AC-5 | Notas exibidas na escala de 0 a 5, com uma casa decimal | Premissa de projeto |
| P-AC-6 | O Servidor/API entrega as notas já calculadas e o app só as exibe (provisória; decisão formal no D-AVC-02) | Premissa de projeto |
| P-AC-7 | Listas na ordem recebida do servidor, sem busca, filtro nem ordenação no app | Premissa de projeto |
| P-AC-8 | A nota de uma dimensão na UA é a média, entre as avaliações da UA, da nota daquela dimensão em cada avaliação; mostram-se as dimensões que aparecem nas avaliações da UA, agregadas pelo `id` (`DD-AvalRegistrar-01`, "Para quem consome", item 3) | Premissa de projeto |
