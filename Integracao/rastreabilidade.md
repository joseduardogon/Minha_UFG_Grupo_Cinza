# Matriz de rastreabilidade (D-INT-04)

| Campo | Valor |
|---|---|
| **Tarefa** | `D-INT-04` – Rastreabilidade |
| **Responsável** | Pessoa D (integração) |
| **Data** | 02/11/2026 |
| **Critério** | Apêndice B, critério 5.2 |

Material de trabalho da integração: não entra no PDF como item de informação. Gerada a partir do campo "Rastreia para" de cada item. "Rastreado por" é o inverso: os itens que apontam para ele.

## 1. Verificações

| Verificação | Resultado |
|---|---|
| Todo item tem o campo "Rastreia para" preenchido | OK: 171 itens, nenhum vazio |
| Todo código citado no "Rastreia para" existe | OK: nenhum código inexistente |
| Nenhum item rastreia para si mesmo | OK |
| Cascata: DAtv → DCdu, DIhc → DAtv, DSeq → DAtv, DEst → DIhc, DCla → DCmp, Contrato → DCla, ECA → DCla, DCdu detalhado → `DCdu-Geral-01` | OK após a correção do R-01 (seção 2) |

## 2. Achados

| Código | Item | Achado | Situação |
|---|---|---|---|
| R-01 | `DCla-Locais-02` | Não rastreia para `DCmp-Locais-01`, ao contrário do `DCla-Locais-01` | Corrigido |

Observação, sem correção (decisão da Pessoa D, 02/11/2026): itens que nenhum outro aponta, mas que rastreiam para o seu DCla, o que basta para o critério 5.2: `Contrato-Comum-04`, `ECA-AppsUFG-01`, `ECA-Locais-01`, `ECA-Seguranca-01`.

## 3. Matriz


### Geral (dono: Pessoa D)

| Item | Rastreia para | Rastreado por |
|---|---|---|
| `DCdu-Geral-01` | `DCdu-Seguranca-01`, `DCdu-Radio-01`, `DCdu-Guia-01`, `DCdu-Eventos-01`, `DCdu-Noticias-01`, `DCdu-RU-01`, `DCdu-Locais-01`, `DCdu-AppsUFG-01`, `DCdu-AvalRegistrar-01`, `DCdu-AvalConsultar-01`, `DImp-Geral-01`, `DPac-Geral-01` | `DCdu-AppsUFG-01`, `DCdu-AvalConsultar-01`, `DCdu-AvalRegistrar-01`, `DCdu-Eventos-01`, `DCdu-Guia-01`, `DCdu-Locais-01`, `DCdu-Noticias-01`, `DCdu-RU-01`, `DCdu-Radio-01`, `DCdu-Seguranca-01`, `DCla-Comum-01`, `DCla-Comum-04`, `DIhc-Inicio-01`, `DImp-Geral-01`, `DPac-Geral-01` |
| `DD-Geral-01` | `DDados-Geral-01`, `DD-Eventos-01`, `DD-Noticias-01`, `DD-RU-01`, `DD-Radio-01`, `DD-Locais-01`, `DD-AvalRegistrar-01`, `DD-AvalConsultar-01`, `DD-Guia-01`, `DD-Seguranca-01`, `DD-AppsUFG-01`, `DCla-Comum-04` | `DD-AppsUFG-01`, `DD-AvalConsultar-01`, `DD-AvalRegistrar-01`, `DD-Eventos-01`, `DD-Guia-01`, `DD-Locais-01`, `DD-Noticias-01`, `DD-RU-01`, `DD-Radio-01`, `DD-Seguranca-01`, `DDados-Geral-01`, `DPac-Geral-01` |
| `DDados-Geral-01` | `DD-Geral-01`, `DD-Eventos-01`, `DD-Noticias-01`, `DD-RU-01`, `DD-Radio-01`, `DD-Locais-01`, `DD-AvalRegistrar-01`, `DD-AvalConsultar-01`, `DD-Guia-01`, `DD-Seguranca-01`, `DD-AppsUFG-01`, `DPac-Geral-01` | `DD-AppsUFG-01`, `DD-AvalConsultar-01`, `DD-AvalRegistrar-01`, `DD-Eventos-01`, `DD-Geral-01`, `DD-Guia-01`, `DD-Locais-01`, `DD-Noticias-01`, `DD-RU-01`, `DD-Radio-01`, `DD-Seguranca-01`, `DPac-Geral-01` |
| `DPac-Geral-01` | `DCdu-Geral-01`, `DImp-Geral-01`, `DCmp-Comum-01`, `DCmp-Seguranca-01`, `DCmp-Radio-01`, `DCmp-Guia-01`, `DCmp-Eventos-01`, `DCmp-Noticias-01`, `DCmp-RU-01`, `DCmp-Locais-01`, `DCmp-AppsUFG-01`, `DCmp-AvalRegistrar-01`, `DCmp-AvalConsultar-01`, `DIhc-Inicio-01`, `DDados-Geral-01`, `DD-Geral-01` | `DCdu-AppsUFG-01`, `DCdu-AvalRegistrar-01`, `DCdu-Geral-01`, `DCdu-Locais-01`, `DCdu-Seguranca-01`, `DCla-AppsUFG-01`, `DCla-Locais-01`, `DCla-Locais-02`, `DCla-Seguranca-01`, `DCmp-AppsUFG-01`, `DCmp-AvalConsultar-01`, `DCmp-AvalRegistrar-01`, `DCmp-Comum-01`, `DCmp-Eventos-01`, `DCmp-Guia-01`, `DCmp-Locais-01`, `DCmp-Noticias-01`, `DCmp-RU-01`, `DCmp-Radio-01`, `DCmp-Seguranca-01`, `DDados-Geral-01`, `DEst-Inicio-01`, `DIhc-Inicio-01`, `DImp-Geral-01` |
| `DImp-Geral-01` | `DCdu-Geral-01`, `DPac-Geral-01`, `DCmp-Comum-01`, `DCla-Comum-01`, `DCla-Comum-02`, `DCla-Comum-04` | `Contrato-Comum-02`, `Contrato-Comum-04`, `DCdu-Geral-01`, `DCla-Comum-01`, `DCla-Comum-02`, `DCla-Comum-04`, `DCmp-AppsUFG-01`, `DCmp-Comum-01`, `DCmp-Locais-01`, `DCmp-Seguranca-01`, `DPac-Geral-01` |

### Inicio (dono: Pessoa D)

| Item | Rastreia para | Rastreado por |
|---|---|---|
| `DIhc-Inicio-01` | `DCdu-Geral-01`, `DPac-Geral-01`, `DEst-Inicio-01`, `DIhc-Guia-01`, `DIhc-Radio-01`, `DIhc-Eventos-01` | `DCdu-AvalRegistrar-01`, `DEst-AppsUFG-01`, `DEst-Inicio-01`, `DEst-Seguranca-01`, `DIhc-AvalRegistrar-01`, `DIhc-Guia-01`, `DIhc-RU-01`, `DPac-Geral-01`, `DSeq-Guia-01` |
| `DEst-Inicio-01` | `DIhc-Inicio-01`, `DEst-Guia-01`, `DEst-Radio-01`, `DEst-Eventos-01`, `DPac-Geral-01` | `DEst-Guia-01`, `DEst-RU-01`, `DIhc-Inicio-01` |

### Comum (dono: Pessoa D)

| Item | Rastreia para | Rastreado por |
|---|---|---|
| `DCmp-Comum-01` | `DPac-Geral-01`, `DImp-Geral-01`, `DCla-Comum-01`, `DCla-Comum-02`, `DCla-Comum-03`, `DCla-Comum-04`, `DEst-Comum-01` | `Contrato-Comum-01`, `Contrato-Comum-02`, `Contrato-Comum-04`, `DCla-Comum-01`, `DCla-Comum-02`, `DCla-Comum-03`, `DCla-Comum-04`, `DCmp-AppsUFG-01`, `DCmp-AvalConsultar-01`, `DCmp-AvalRegistrar-01`, `DCmp-Eventos-01`, `DCmp-Guia-01`, `DCmp-Locais-01`, `DCmp-Noticias-01`, `DCmp-RU-01`, `DCmp-Radio-01`, `DCmp-Seguranca-01`, `DEst-Comum-01`, `DImp-Geral-01`, `DPac-Geral-01` |
| `DCla-Comum-01` | `DCmp-Comum-01`, `DImp-Geral-01`, `DCdu-Geral-01` | `Contrato-AppsUFG-01`, `Contrato-Comum-01`, `Contrato-Guia-01`, `Contrato-Seguranca-01`, `DAtv-AppsUFG-01`, `DAtv-Eventos-03`, `DAtv-Guia-01`, `DAtv-Noticias-02`, `DAtv-Radio-03`, `DAtv-Seguranca-01`, `DCdu-AppsUFG-01`, `DCdu-Eventos-01`, `DCdu-Guia-01`, `DCdu-Noticias-01`, `DCdu-Seguranca-01`, `DCla-AppsUFG-01`, `DCla-Eventos-01`, `DCla-Guia-01`, `DCla-Noticias-01`, `DCla-Radio-01`, `DCla-Seguranca-01`, `DCmp-Comum-01`, `DImp-Geral-01`, `DSeq-AppsUFG-01`, `DSeq-Eventos-05`, `DSeq-Guia-01`, `DSeq-Noticias-03`, `DSeq-Radio-03`, `DSeq-Seguranca-01`, `DSeq-Seguranca-02`, `ECA-Comum-01` |
| `DCla-Comum-02` | `DCmp-Comum-01`, `DImp-Geral-01`, `DCla-Comum-03` | `Contrato-AvalConsultar-01`, `Contrato-Comum-02`, `DAtv-Locais-01`, `DCdu-AvalRegistrar-01`, `DCdu-Locais-01`, `DCla-AvalConsultar-02`, `DCla-AvalRegistrar-01`, `DCla-AvalRegistrar-02`, `DCla-AvalRegistrar-03`, `DCla-AvalRegistrar-04`, `DCla-Comum-03`, `DCla-Eventos-01`, `DCla-Eventos-02`, `DCla-Locais-02`, `DCla-Noticias-01`, `DCla-Noticias-02`, `DCla-RU-01`, `DCla-RU-02`, `DCla-Radio-02`, `DCmp-Comum-01`, `DImp-Geral-01`, `DSeq-AvalConsultar-01`, `DSeq-AvalRegistrar-01`, `DSeq-AvalRegistrar-02`, `DSeq-AvalRegistrar-05`, `DSeq-Eventos-01`, `DSeq-Locais-01`, `DSeq-Noticias-01`, `DSeq-RU-01`, `DSeq-Radio-01`, `ECA-Comum-01` |
| `DCla-Comum-03` | `DCmp-Comum-01`, `DCla-Comum-02`, `DEst-Comum-01` | `Contrato-AvalConsultar-01`, `Contrato-Comum-03`, `Contrato-Locais-01`, `DAtv-Locais-01`, `DCla-AvalConsultar-01`, `DCla-AvalConsultar-02`, `DCla-AvalRegistrar-01`, `DCla-AvalRegistrar-02`, `DCla-AvalRegistrar-03`, `DCla-Comum-02`, `DCla-Eventos-01`, `DCla-Eventos-02`, `DCla-Locais-01`, `DCla-Locais-02`, `DCla-Noticias-01`, `DCla-Noticias-02`, `DCla-RU-01`, `DCla-RU-02`, `DCla-Radio-01`, `DCla-Radio-02`, `DCmp-Comum-01`, `DEst-AvalRegistrar-02`, `DEst-AvalRegistrar-03`, `DEst-Comum-01`, `DEst-Eventos-01`, `DEst-Noticias-01`, `DEst-RU-02`, `DSeq-AvalConsultar-01`, `DSeq-AvalRegistrar-01`, `DSeq-AvalRegistrar-02`, `DSeq-AvalRegistrar-04`, `DSeq-Eventos-01`, `DSeq-Eventos-02`, `DSeq-Eventos-03`, `DSeq-Eventos-04`, `DSeq-Eventos-05`, `DSeq-Locais-01`, `DSeq-Noticias-01`, `DSeq-Noticias-02`, `DSeq-RU-01`, `DSeq-Radio-01`, `ECA-Comum-01` |
| `DCla-Comum-04` | `DCmp-Comum-01`, `DImp-Geral-01`, `DCdu-Geral-01` | `Contrato-Comum-04`, `Contrato-Locais-01`, `DAtv-Locais-02`, `DAtv-Locais-03`, `DCdu-Locais-01`, `DCla-Locais-01`, `DCmp-Comum-01`, `DD-Geral-01`, `DImp-Geral-01`, `DSeq-Locais-02`, `DSeq-Locais-03` |
| `DEst-Comum-01` | `DCla-Comum-03`, `DCmp-Comum-01` | `Contrato-Comum-03`, `DAtv-AvalConsultar-01`, `DAtv-AvalConsultar-02`, `DAtv-AvalConsultar-03`, `DAtv-AvalRegistrar-01`, `DAtv-AvalRegistrar-02`, `DAtv-Eventos-01`, `DAtv-Noticias-01`, `DAtv-RU-01`, `DAtv-RU-02`, `DAtv-Radio-01`, `DCdu-AvalConsultar-01`, `DCdu-AvalRegistrar-01`, `DCdu-Noticias-01`, `DCdu-RU-01`, `DCla-Comum-03`, `DCmp-Comum-01`, `DEst-AvalConsultar-01`, `DEst-AvalConsultar-02`, `DEst-AvalConsultar-03`, `DEst-AvalRegistrar-02`, `DEst-AvalRegistrar-03`, `DEst-Eventos-01`, `DEst-Locais-01`, `DEst-Noticias-01`, `DEst-RU-02`, `DEst-Radio-01`, `DIhc-AvalConsultar-01`, `DIhc-AvalConsultar-02`, `DIhc-AvalConsultar-03`, `DIhc-AvalRegistrar-02`, `DIhc-AvalRegistrar-03`, `DIhc-RU-02`, `DSeq-AvalRegistrar-01`, `DSeq-AvalRegistrar-02`, `DSeq-Eventos-01`, `DSeq-Noticias-01`, `DSeq-RU-01`, `ECA-AvalConsultar-01`, `ECA-AvalRegistrar-01`, `ECA-Comum-01`, `ECA-Eventos-01`, `ECA-Noticias-01`, `ECA-RU-01`, `ECA-Radio-01` |
| `Contrato-Comum-01` | `DCla-Comum-01`, `DCmp-Comum-01`, `ECA-Comum-01`, `DSeq-Guia-01`, `DSeq-Radio-03` | `Contrato-Eventos-01`, `ECA-Comum-01` |
| `Contrato-Comum-02` | `DCla-Comum-02`, `DCmp-Comum-01`, `DImp-Geral-01`, `ECA-Comum-01`, `DSeq-Radio-01`, `DSeq-Eventos-01` | `Contrato-AvalRegistrar-01`, `Contrato-Eventos-01`, `ECA-Comum-01` |
| `Contrato-Comum-03` | `DCla-Comum-03`, `DEst-Comum-01`, `ECA-Comum-01`, `Contrato-Radio-01`, `Contrato-Eventos-01` | `Contrato-AvalRegistrar-01`, `Contrato-Eventos-01`, `ECA-Comum-01` |
| `Contrato-Comum-04` | `DCla-Comum-04`, `DCmp-Comum-01`, `DImp-Geral-01` | – |
| `ECA-Comum-01` | `DCla-Comum-01`, `DCla-Comum-02`, `DCla-Comum-03`, `DEst-Comum-01`, `Contrato-Comum-01`, `Contrato-Comum-02`, `Contrato-Comum-03` | `Contrato-Comum-01`, `Contrato-Comum-02`, `Contrato-Comum-03`, `ECA-AvalRegistrar-01`, `ECA-Eventos-01`, `ECA-Noticias-01`, `ECA-RU-01` |

### Seguranca (dono: Pessoa B)

| Item | Rastreia para | Rastreado por |
|---|---|---|
| `DCdu-Seguranca-01` | `DCdu-Geral-01`, `DPac-Geral-01`, `DAtv-Seguranca-01`, `DIhc-Seguranca-01`, `DCla-Comum-01` | `DAtv-Seguranca-01`, `DCdu-Geral-01`, `DD-Seguranca-01`, `DEst-Seguranca-01`, `DIhc-Seguranca-01`, `DSeq-Seguranca-01`, `DSeq-Seguranca-02` |
| `DAtv-Seguranca-01` | `DCdu-Seguranca-01`, `DIhc-Seguranca-01`, `DCla-Comum-01`, `DSeq-Seguranca-01`, `DSeq-Seguranca-02` | `DCdu-Seguranca-01`, `DIhc-Seguranca-01`, `DSeq-Seguranca-01`, `DSeq-Seguranca-02` |
| `DIhc-Seguranca-01` | `DCdu-Seguranca-01`, `DAtv-Seguranca-01`, `DEst-Seguranca-01`, `DSeq-Seguranca-01`, `DSeq-Seguranca-02` | `DAtv-Seguranca-01`, `DCdu-Seguranca-01`, `DCla-Seguranca-01`, `DEst-Seguranca-01`, `DSeq-Seguranca-01`, `DSeq-Seguranca-02` |
| `DD-Seguranca-01` | `DCla-Seguranca-01`, `DCdu-Seguranca-01`, `DD-Geral-01`, `DDados-Geral-01` | `DD-Geral-01`, `DDados-Geral-01` |
| `DCmp-Seguranca-01` | `DPac-Geral-01`, `DImp-Geral-01`, `DCmp-Comum-01`, `DCla-Seguranca-01` | `DCla-Seguranca-01`, `DPac-Geral-01` |
| `DCla-Seguranca-01` | `DPac-Geral-01`, `DCmp-Seguranca-01`, `DCla-Comum-01`, `DIhc-Seguranca-01`, `DSeq-Seguranca-01`, `DSeq-Seguranca-02` | `Contrato-Seguranca-01`, `DCmp-Seguranca-01`, `DD-Seguranca-01`, `DSeq-Seguranca-01`, `DSeq-Seguranca-02`, `ECA-Seguranca-01` |
| `DSeq-Seguranca-01` | `DCdu-Seguranca-01`, `DAtv-Seguranca-01`, `DIhc-Seguranca-01`, `DCla-Seguranca-01`, `DCla-Comum-01` | `Contrato-Seguranca-01`, `DAtv-Seguranca-01`, `DCla-Seguranca-01`, `DEst-Seguranca-01`, `DIhc-Seguranca-01` |
| `DSeq-Seguranca-02` | `DCdu-Seguranca-01`, `DAtv-Seguranca-01`, `DIhc-Seguranca-01`, `DCla-Seguranca-01`, `DCla-Comum-01` | `Contrato-Seguranca-01`, `DAtv-Seguranca-01`, `DCla-Seguranca-01`, `DEst-Seguranca-01`, `DIhc-Seguranca-01` |
| `DEst-Seguranca-01` | `DCdu-Seguranca-01`, `DIhc-Seguranca-01`, `DIhc-Inicio-01`, `DSeq-Seguranca-01`, `DSeq-Seguranca-02` | `DIhc-Seguranca-01`, `ECA-Seguranca-01` |
| `Contrato-Seguranca-01` | `DCla-Seguranca-01`, `DSeq-Seguranca-01`, `DSeq-Seguranca-02`, `DCla-Comum-01` | `ECA-Seguranca-01` |
| `ECA-Seguranca-01` | `DCla-Seguranca-01`, `DEst-Seguranca-01`, `Contrato-Seguranca-01` | – |

### Locais (dono: Pessoa B)

| Item | Rastreia para | Rastreado por |
|---|---|---|
| `DCdu-Locais-01` | `DCdu-Geral-01`, `DPac-Geral-01`, `DAtv-Locais-01`, `DAtv-Locais-02`, `DAtv-Locais-03`, `DIhc-Locais-01`, `DIhc-Locais-02`, `DCla-Comum-02`, `DCla-Comum-04` | `DAtv-Locais-01`, `DAtv-Locais-02`, `DAtv-Locais-03`, `DCdu-Geral-01`, `DD-Locais-01`, `DEst-Locais-01`, `DIhc-Locais-01`, `DIhc-Locais-02`, `DSeq-Locais-01`, `DSeq-Locais-02`, `DSeq-Locais-03` |
| `DAtv-Locais-01` | `DCdu-Locais-01`, `DIhc-Locais-01`, `DCla-Comum-02`, `DCla-Comum-03`, `DSeq-Locais-01` | `DCdu-Locais-01`, `DIhc-Locais-01`, `DSeq-Locais-01` |
| `DAtv-Locais-02` | `DCdu-Locais-01`, `DIhc-Locais-01`, `DIhc-Locais-02`, `DCla-Comum-04`, `DSeq-Locais-02` | `DCdu-Locais-01`, `DIhc-Locais-02`, `DSeq-Locais-02` |
| `DAtv-Locais-03` | `DCdu-Locais-01`, `DIhc-Locais-02`, `DCla-Comum-04`, `DSeq-Locais-03` | `DCdu-Locais-01`, `DIhc-Locais-02`, `DSeq-Locais-03` |
| `DIhc-Locais-01` | `DCdu-Locais-01`, `DAtv-Locais-01`, `DIhc-Locais-02`, `DEst-Locais-01`, `DSeq-Locais-02` | `DAtv-Locais-01`, `DAtv-Locais-02`, `DCdu-Locais-01`, `DCla-Locais-01`, `DEst-Locais-01`, `DIhc-Locais-02`, `DSeq-Locais-01`, `DSeq-Locais-02` |
| `DIhc-Locais-02` | `DCdu-Locais-01`, `DAtv-Locais-02`, `DAtv-Locais-03`, `DIhc-Locais-01`, `DEst-Locais-01`, `DSeq-Locais-03` | `DAtv-Locais-02`, `DAtv-Locais-03`, `DCdu-Locais-01`, `DCla-Locais-01`, `DEst-Locais-01`, `DIhc-Locais-01`, `DSeq-Locais-02`, `DSeq-Locais-03` |
| `DD-Locais-01` | `DCla-Locais-02`, `DCdu-Locais-01`, `DD-Eventos-01`, `DD-Geral-01`, `DDados-Geral-01` | `DCdu-AvalConsultar-01`, `DCdu-AvalRegistrar-01`, `DCla-AvalConsultar-01`, `DCla-AvalConsultar-02`, `DCla-AvalRegistrar-01`, `DCla-AvalRegistrar-02`, `DCla-AvalRegistrar-04`, `DCla-Locais-02`, `DCmp-AvalRegistrar-01`, `DD-AvalConsultar-01`, `DD-AvalRegistrar-01`, `DD-Geral-01`, `DDados-Geral-01`, `DIhc-AvalConsultar-01`, `DIhc-AvalConsultar-02`, `DIhc-AvalRegistrar-02` |
| `DCmp-Locais-01` | `DPac-Geral-01`, `DImp-Geral-01`, `DCmp-Comum-01`, `DCla-Locais-01`, `DCla-Locais-02` | `DCla-Locais-01`, `DCla-Locais-02`, `DPac-Geral-01` |
| `DCla-Locais-01` | `DPac-Geral-01`, `DCmp-Locais-01`, `DCla-Comum-03`, `DCla-Comum-04`, `DIhc-Locais-01`, `DIhc-Locais-02`, `DSeq-Locais-01`, `DSeq-Locais-02`, `DSeq-Locais-03` | `Contrato-Locais-01`, `DCla-Locais-02`, `DCmp-Locais-01`, `DSeq-Locais-01`, `DSeq-Locais-02`, `DSeq-Locais-03`, `ECA-Locais-01` |
| `DCla-Locais-02` | `DPac-Geral-01`, `DCmp-Locais-01`, `DD-Locais-01`, `DCla-Locais-01`, `DCla-Comum-02`, `DCla-Comum-03`, `DSeq-Locais-01`, `DD-Eventos-01` | `Contrato-Locais-01`, `DCmp-Locais-01`, `DD-Locais-01`, `DSeq-Locais-01` |
| `DSeq-Locais-01` | `DCdu-Locais-01`, `DAtv-Locais-01`, `DIhc-Locais-01`, `DCla-Locais-01`, `DCla-Locais-02`, `DCla-Comum-02`, `DCla-Comum-03` | `Contrato-Locais-01`, `DAtv-Locais-01`, `DCla-Locais-01`, `DCla-Locais-02`, `DEst-Locais-01` |
| `DSeq-Locais-02` | `DCdu-Locais-01`, `DAtv-Locais-02`, `DIhc-Locais-01`, `DIhc-Locais-02`, `DCla-Locais-01`, `DCla-Comum-04` | `Contrato-Locais-01`, `DAtv-Locais-02`, `DCla-Locais-01`, `DEst-Locais-01`, `DIhc-Locais-01` |
| `DSeq-Locais-03` | `DCdu-Locais-01`, `DAtv-Locais-03`, `DIhc-Locais-02`, `DCla-Locais-01`, `DCla-Comum-04` | `Contrato-Locais-01`, `DAtv-Locais-03`, `DCla-Locais-01`, `DEst-Locais-01`, `DIhc-Locais-02` |
| `DEst-Locais-01` | `DCdu-Locais-01`, `DIhc-Locais-01`, `DIhc-Locais-02`, `DEst-Comum-01`, `DSeq-Locais-01`, `DSeq-Locais-02`, `DSeq-Locais-03` | `DIhc-Locais-01`, `DIhc-Locais-02`, `ECA-Locais-01` |
| `Contrato-Locais-01` | `DCla-Locais-01`, `DCla-Locais-02`, `DSeq-Locais-01`, `DSeq-Locais-02`, `DSeq-Locais-03`, `DCla-Comum-03`, `DCla-Comum-04` | `ECA-Locais-01` |
| `ECA-Locais-01` | `DCla-Locais-01`, `DEst-Locais-01`, `Contrato-Locais-01` | – |

### AppsUFG (dono: Pessoa B)

| Item | Rastreia para | Rastreado por |
|---|---|---|
| `DCdu-AppsUFG-01` | `DCdu-Geral-01`, `DPac-Geral-01`, `DAtv-AppsUFG-01`, `DIhc-AppsUFG-01`, `DCla-Comum-01` | `DAtv-AppsUFG-01`, `DCdu-Geral-01`, `DD-AppsUFG-01`, `DEst-AppsUFG-01`, `DIhc-AppsUFG-01`, `DSeq-AppsUFG-01` |
| `DAtv-AppsUFG-01` | `DCdu-AppsUFG-01`, `DIhc-AppsUFG-01`, `DCla-Comum-01`, `DSeq-AppsUFG-01` | `DCdu-AppsUFG-01`, `DIhc-AppsUFG-01`, `DSeq-AppsUFG-01` |
| `DIhc-AppsUFG-01` | `DCdu-AppsUFG-01`, `DAtv-AppsUFG-01`, `DEst-AppsUFG-01`, `DSeq-AppsUFG-01` | `DAtv-AppsUFG-01`, `DCdu-AppsUFG-01`, `DCla-AppsUFG-01`, `DEst-AppsUFG-01`, `DSeq-AppsUFG-01` |
| `DD-AppsUFG-01` | `DCla-AppsUFG-01`, `DCdu-AppsUFG-01`, `DD-Geral-01`, `DDados-Geral-01` | `DD-Geral-01`, `DDados-Geral-01` |
| `DCmp-AppsUFG-01` | `DPac-Geral-01`, `DImp-Geral-01`, `DCmp-Comum-01`, `DCla-AppsUFG-01` | `DCla-AppsUFG-01`, `DPac-Geral-01` |
| `DCla-AppsUFG-01` | `DPac-Geral-01`, `DCmp-AppsUFG-01`, `DCla-Comum-01`, `DIhc-AppsUFG-01`, `DSeq-AppsUFG-01` | `Contrato-AppsUFG-01`, `DCmp-AppsUFG-01`, `DD-AppsUFG-01`, `DSeq-AppsUFG-01`, `ECA-AppsUFG-01` |
| `DSeq-AppsUFG-01` | `DCdu-AppsUFG-01`, `DAtv-AppsUFG-01`, `DIhc-AppsUFG-01`, `DCla-AppsUFG-01`, `DCla-Comum-01` | `Contrato-AppsUFG-01`, `DAtv-AppsUFG-01`, `DCla-AppsUFG-01`, `DEst-AppsUFG-01`, `DIhc-AppsUFG-01` |
| `DEst-AppsUFG-01` | `DCdu-AppsUFG-01`, `DIhc-AppsUFG-01`, `DIhc-Inicio-01`, `DSeq-AppsUFG-01` | `DIhc-AppsUFG-01`, `ECA-AppsUFG-01` |
| `Contrato-AppsUFG-01` | `DCla-AppsUFG-01`, `DSeq-AppsUFG-01`, `DCla-Comum-01` | `ECA-AppsUFG-01` |
| `ECA-AppsUFG-01` | `DCla-AppsUFG-01`, `DEst-AppsUFG-01`, `Contrato-AppsUFG-01` | – |

### Radio (dono: Pessoa D)

| Item | Rastreia para | Rastreado por |
|---|---|---|
| `DCdu-Radio-01` | `DCdu-Geral-01`, `DAtv-Radio-01`, `DAtv-Radio-02`, `DAtv-Radio-03`, `DIhc-Radio-01` | `DAtv-Radio-01`, `DAtv-Radio-02`, `DAtv-Radio-03`, `DCdu-Geral-01`, `DD-Radio-01`, `DIhc-Radio-01` |
| `DAtv-Radio-01` | `DCdu-Radio-01`, `DIhc-Radio-01`, `DEst-Comum-01` | `DAtv-Radio-02`, `DAtv-Radio-03`, `DCdu-Radio-01`, `DCmp-Radio-01`, `DIhc-Radio-01`, `DSeq-Radio-01` |
| `DAtv-Radio-02` | `DCdu-Radio-01`, `DAtv-Radio-01`, `DIhc-Radio-01` | `DCdu-Radio-01`, `DIhc-Radio-01`, `DSeq-Radio-02` |
| `DAtv-Radio-03` | `DCdu-Radio-01`, `DIhc-Radio-01`, `DCla-Comum-01`, `DAtv-Radio-01` | `DCdu-Radio-01`, `DIhc-Radio-01`, `DSeq-Radio-03` |
| `DIhc-Radio-01` | `DCdu-Radio-01`, `DAtv-Radio-01`, `DAtv-Radio-02`, `DAtv-Radio-03`, `DEst-Radio-01` | `DAtv-Radio-01`, `DAtv-Radio-02`, `DAtv-Radio-03`, `DCdu-Radio-01`, `DCla-Radio-01`, `DEst-Radio-01`, `DIhc-Inicio-01`, `DSeq-Radio-01`, `DSeq-Radio-02`, `DSeq-Radio-03` |
| `DD-Radio-01` | `DCla-Radio-02`, `DCdu-Radio-01`, `DD-Geral-01`, `DDados-Geral-01` | `DCla-Radio-02`, `DD-Geral-01`, `DDados-Geral-01` |
| `DCmp-Radio-01` | `DPac-Geral-01`, `DCmp-Comum-01`, `DCla-Radio-01`, `DCla-Radio-02`, `DAtv-Radio-01` | `DCla-Radio-01`, `DCla-Radio-02`, `DPac-Geral-01` |
| `DCla-Radio-01` | `DCmp-Radio-01`, `DIhc-Radio-01`, `DCla-Radio-02`, `DCla-Comum-01`, `DCla-Comum-03` | `Contrato-Radio-01`, `DCla-Radio-02`, `DCmp-Radio-01`, `DSeq-Radio-01`, `DSeq-Radio-02`, `DSeq-Radio-03`, `ECA-Radio-01` |
| `DCla-Radio-02` | `DCmp-Radio-01`, `DD-Radio-01`, `DCla-Comum-02`, `DCla-Comum-03`, `DCla-Radio-01` | `Contrato-Radio-01`, `DCla-Radio-01`, `DCmp-Radio-01`, `DD-Radio-01`, `DSeq-Radio-01` |
| `DSeq-Radio-01` | `DAtv-Radio-01`, `DIhc-Radio-01`, `DCla-Radio-01`, `DCla-Radio-02`, `DCla-Comum-02`, `DCla-Comum-03`, `Contrato-Radio-01` | `Contrato-Comum-02`, `Contrato-Radio-01`, `DEst-Radio-01`, `DSeq-Radio-03` |
| `DSeq-Radio-02` | `DAtv-Radio-02`, `DIhc-Radio-01`, `DCla-Radio-01`, `Contrato-Radio-01` | `Contrato-Radio-01`, `DEst-Radio-01` |
| `DSeq-Radio-03` | `DAtv-Radio-03`, `DIhc-Radio-01`, `DCla-Radio-01`, `DCla-Comum-01`, `DSeq-Radio-01`, `ECA-Radio-01` | `Contrato-Comum-01`, `Contrato-Radio-01`, `DEst-Radio-01` |
| `DEst-Radio-01` | `DIhc-Radio-01`, `DEst-Comum-01`, `DSeq-Radio-01`, `DSeq-Radio-02`, `DSeq-Radio-03`, `ECA-Radio-01` | `DEst-Inicio-01`, `DIhc-Radio-01`, `ECA-Radio-01` |
| `Contrato-Radio-01` | `DCla-Radio-01`, `DCla-Radio-02`, `DSeq-Radio-01`, `DSeq-Radio-02`, `DSeq-Radio-03`, `ECA-Radio-01` | `Contrato-Comum-03`, `DSeq-Radio-01`, `DSeq-Radio-02`, `ECA-Radio-01` |
| `ECA-Radio-01` | `DCla-Radio-01`, `DEst-Radio-01`, `DEst-Comum-01`, `Contrato-Radio-01` | `Contrato-Radio-01`, `DEst-Radio-01`, `DSeq-Radio-03` |

### Guia (dono: Pessoa D)

| Item | Rastreia para | Rastreado por |
|---|---|---|
| `DCdu-Guia-01` | `DCdu-Geral-01`, `DAtv-Guia-01`, `DIhc-Guia-01`, `DCla-Comum-01` | `DAtv-Guia-01`, `DCdu-Geral-01`, `DD-Guia-01`, `DIhc-Guia-01`, `DSeq-Guia-02` |
| `DAtv-Guia-01` | `DCdu-Guia-01`, `DIhc-Guia-01`, `DCla-Comum-01` | `DCdu-Guia-01`, `DCla-Guia-01`, `DCmp-Guia-01`, `DIhc-Guia-01`, `DSeq-Guia-01`, `DSeq-Guia-02` |
| `DIhc-Guia-01` | `DCdu-Guia-01`, `DAtv-Guia-01`, `DIhc-Inicio-01`, `DEst-Guia-01` | `DAtv-Guia-01`, `DCdu-Guia-01`, `DEst-Guia-01`, `DIhc-Inicio-01`, `DSeq-Guia-01`, `DSeq-Guia-02` |
| `DD-Guia-01` | `DCla-Guia-01`, `DCdu-Guia-01`, `DD-Geral-01`, `DDados-Geral-01` | `DCla-Guia-01`, `DD-Geral-01`, `DDados-Geral-01` |
| `DCmp-Guia-01` | `DPac-Geral-01`, `DCmp-Comum-01`, `DCla-Guia-01`, `DAtv-Guia-01` | `DCla-Guia-01`, `DPac-Geral-01` |
| `DCla-Guia-01` | `DCmp-Guia-01`, `DCla-Comum-01`, `DD-Guia-01`, `DAtv-Guia-01` | `Contrato-Guia-01`, `DCmp-Guia-01`, `DD-Guia-01`, `DSeq-Guia-01` |
| `DSeq-Guia-01` | `DAtv-Guia-01`, `DIhc-Guia-01`, `DCla-Guia-01`, `DCla-Comum-01`, `Contrato-Guia-01`, `DIhc-Inicio-01` | `Contrato-Comum-01`, `Contrato-Guia-01`, `DEst-Guia-01` |
| `DSeq-Guia-02` | `DAtv-Guia-01`, `DIhc-Guia-01`, `DEst-Guia-01`, `DCdu-Guia-01` | `DEst-Guia-01` |
| `DEst-Guia-01` | `DIhc-Guia-01`, `DSeq-Guia-01`, `DSeq-Guia-02`, `DEst-Inicio-01` | `DEst-Inicio-01`, `DIhc-Guia-01`, `DSeq-Guia-02` |
| `Contrato-Guia-01` | `DCla-Guia-01`, `DSeq-Guia-01`, `DCla-Comum-01` | `DSeq-Guia-01` |

### AvalConsultar (dono: Pessoa D)

| Item | Rastreia para | Rastreado por |
|---|---|---|
| `DCdu-AvalConsultar-01` | `DCdu-Geral-01`, `DIhc-AvalRegistrar-01`, `DD-AvalRegistrar-01`, `DD-Locais-01`, `DEst-Comum-01`, `DAtv-AvalConsultar-01`, `DAtv-AvalConsultar-02`, `DAtv-AvalConsultar-03`, `DIhc-AvalConsultar-01`, `DIhc-AvalConsultar-02`, `DIhc-AvalConsultar-03` | `DAtv-AvalConsultar-01`, `DAtv-AvalConsultar-02`, `DAtv-AvalConsultar-03`, `DCdu-Geral-01`, `DD-AvalConsultar-01`, `DIhc-AvalConsultar-01`, `DIhc-AvalConsultar-02`, `DIhc-AvalConsultar-03` |
| `DAtv-AvalConsultar-01` | `DCdu-AvalConsultar-01`, `DIhc-AvalConsultar-01`, `DIhc-AvalRegistrar-01`, `DAtv-AvalConsultar-02`, `DEst-Comum-01` | `DAtv-AvalConsultar-02`, `DCdu-AvalConsultar-01`, `DCla-AvalConsultar-01`, `DIhc-AvalConsultar-01`, `DSeq-AvalConsultar-01` |
| `DAtv-AvalConsultar-02` | `DCdu-AvalConsultar-01`, `DIhc-AvalConsultar-01`, `DIhc-AvalConsultar-02`, `DAtv-AvalConsultar-01`, `DAtv-AvalConsultar-03`, `DEst-Comum-01` | `DAtv-AvalConsultar-01`, `DAtv-AvalConsultar-03`, `DCdu-AvalConsultar-01`, `DCla-AvalConsultar-01`, `DIhc-AvalConsultar-02`, `DSeq-AvalConsultar-02` |
| `DAtv-AvalConsultar-03` | `DCdu-AvalConsultar-01`, `DIhc-AvalConsultar-02`, `DIhc-AvalConsultar-03`, `DAtv-AvalConsultar-02`, `DD-AvalRegistrar-01`, `DEst-Comum-01` | `DAtv-AvalConsultar-02`, `DCdu-AvalConsultar-01`, `DCla-AvalConsultar-01`, `DIhc-AvalConsultar-03`, `DSeq-AvalConsultar-03` |
| `DIhc-AvalConsultar-01` | `DCdu-AvalConsultar-01`, `DAtv-AvalConsultar-01`, `DIhc-AvalRegistrar-01`, `DIhc-AvalConsultar-02`, `DEst-Comum-01`, `DD-Locais-01` | `DAtv-AvalConsultar-01`, `DAtv-AvalConsultar-02`, `DCdu-AvalConsultar-01`, `DCla-AvalConsultar-01`, `DCmp-AvalConsultar-01`, `DEst-AvalConsultar-01`, `DIhc-AvalConsultar-02`, `DSeq-AvalConsultar-01`, `DSeq-AvalConsultar-02` |
| `DIhc-AvalConsultar-02` | `DCdu-AvalConsultar-01`, `DAtv-AvalConsultar-02`, `DIhc-AvalConsultar-01`, `DIhc-AvalConsultar-03`, `DEst-Comum-01`, `DD-Locais-01` | `DAtv-AvalConsultar-02`, `DAtv-AvalConsultar-03`, `DCdu-AvalConsultar-01`, `DCla-AvalConsultar-01`, `DCmp-AvalConsultar-01`, `DEst-AvalConsultar-02`, `DIhc-AvalConsultar-01`, `DIhc-AvalConsultar-03`, `DSeq-AvalConsultar-02`, `DSeq-AvalConsultar-03` |
| `DIhc-AvalConsultar-03` | `DCdu-AvalConsultar-01`, `DAtv-AvalConsultar-03`, `DIhc-AvalConsultar-02`, `DD-AvalRegistrar-01`, `DEst-Comum-01` | `DAtv-AvalConsultar-03`, `DCdu-AvalConsultar-01`, `DCla-AvalConsultar-01`, `DCmp-AvalConsultar-01`, `DEst-AvalConsultar-03`, `DIhc-AvalConsultar-02`, `DSeq-AvalConsultar-03` |
| `DD-AvalConsultar-01` | `DCla-AvalConsultar-02`, `DCdu-AvalConsultar-01`, `DD-AvalRegistrar-01`, `DD-Locais-01`, `DD-Geral-01`, `DDados-Geral-01` | `Contrato-AvalConsultar-01`, `DCla-AvalConsultar-02`, `DCmp-AvalConsultar-01`, `DD-Geral-01`, `DDados-Geral-01` |
| `DCmp-AvalConsultar-01` | `DPac-Geral-01`, `DCmp-Comum-01`, `DCmp-AvalRegistrar-01`, `DCla-AvalConsultar-01`, `DCla-AvalConsultar-02`, `DD-AvalConsultar-01`, `DIhc-AvalConsultar-01`, `DIhc-AvalConsultar-02`, `DIhc-AvalConsultar-03` | `DCla-AvalConsultar-01`, `DCla-AvalConsultar-02`, `DPac-Geral-01` |
| `DCla-AvalConsultar-01` | `DCmp-AvalConsultar-01`, `DCla-AvalConsultar-02`, `DCla-Comum-03`, `DIhc-AvalConsultar-01`, `DIhc-AvalConsultar-02`, `DIhc-AvalConsultar-03`, `DAtv-AvalConsultar-01`, `DAtv-AvalConsultar-02`, `DAtv-AvalConsultar-03`, `DD-Locais-01` | `Contrato-AvalConsultar-01`, `DCla-AvalConsultar-02`, `DCmp-AvalConsultar-01`, `DEst-AvalConsultar-01`, `DEst-AvalConsultar-02`, `DEst-AvalConsultar-03`, `DSeq-AvalConsultar-01`, `DSeq-AvalConsultar-02`, `DSeq-AvalConsultar-03`, `ECA-AvalConsultar-01` |
| `DCla-AvalConsultar-02` | `DCmp-AvalConsultar-01`, `DCla-AvalConsultar-01`, `DD-AvalConsultar-01`, `DCla-Comum-02`, `DCla-Comum-03`, `DD-AvalRegistrar-01`, `DD-Locais-01` | `Contrato-AvalConsultar-01`, `DCla-AvalConsultar-01`, `DCmp-AvalConsultar-01`, `DD-AvalConsultar-01`, `DSeq-AvalConsultar-01`, `DSeq-AvalConsultar-02`, `DSeq-AvalConsultar-03` |
| `DSeq-AvalConsultar-01` | `DAtv-AvalConsultar-01`, `DIhc-AvalConsultar-01`, `DIhc-AvalRegistrar-01`, `DCla-AvalConsultar-01`, `DCla-AvalConsultar-02`, `DCla-AvalRegistrar-01`, `DCla-Comum-02`, `DCla-Comum-03`, `DEst-AvalConsultar-01`, `Contrato-AvalConsultar-01` | `Contrato-AvalConsultar-01`, `DEst-AvalConsultar-01`, `DSeq-AvalConsultar-02`, `DSeq-AvalConsultar-03` |
| `DSeq-AvalConsultar-02` | `DAtv-AvalConsultar-02`, `DIhc-AvalConsultar-01`, `DIhc-AvalConsultar-02`, `DCla-AvalConsultar-01`, `DCla-AvalConsultar-02`, `DSeq-AvalConsultar-01`, `DEst-AvalConsultar-02`, `Contrato-AvalConsultar-01` | `Contrato-AvalConsultar-01`, `DEst-AvalConsultar-02` |
| `DSeq-AvalConsultar-03` | `DAtv-AvalConsultar-03`, `DIhc-AvalConsultar-02`, `DIhc-AvalConsultar-03`, `DCla-AvalConsultar-01`, `DCla-AvalConsultar-02`, `DSeq-AvalConsultar-01`, `DEst-AvalConsultar-03`, `Contrato-AvalConsultar-01` | `Contrato-AvalConsultar-01`, `DEst-AvalConsultar-03` |
| `DEst-AvalConsultar-01` | `DIhc-AvalConsultar-01`, `DCla-AvalConsultar-01`, `DEst-Comum-01`, `DSeq-AvalConsultar-01`, `ECA-AvalConsultar-01`, `Contrato-AvalConsultar-01`, `DEst-AvalConsultar-02` | `Contrato-AvalConsultar-01`, `DSeq-AvalConsultar-01`, `ECA-AvalConsultar-01` |
| `DEst-AvalConsultar-02` | `DIhc-AvalConsultar-02`, `DCla-AvalConsultar-01`, `DEst-Comum-01`, `DSeq-AvalConsultar-02`, `ECA-AvalConsultar-01`, `Contrato-AvalConsultar-01`, `DEst-AvalConsultar-03` | `Contrato-AvalConsultar-01`, `DEst-AvalConsultar-01`, `DSeq-AvalConsultar-02`, `ECA-AvalConsultar-01` |
| `DEst-AvalConsultar-03` | `DIhc-AvalConsultar-03`, `DCla-AvalConsultar-01`, `DEst-Comum-01`, `DSeq-AvalConsultar-03`, `ECA-AvalConsultar-01`, `Contrato-AvalConsultar-01` | `Contrato-AvalConsultar-01`, `DEst-AvalConsultar-02`, `DSeq-AvalConsultar-03`, `ECA-AvalConsultar-01` |
| `Contrato-AvalConsultar-01` | `DCla-AvalConsultar-01`, `DCla-AvalConsultar-02`, `DD-AvalConsultar-01`, `DSeq-AvalConsultar-01`, `DSeq-AvalConsultar-02`, `DSeq-AvalConsultar-03`, `DEst-AvalConsultar-01`, `DEst-AvalConsultar-02`, `DEst-AvalConsultar-03`, `ECA-AvalConsultar-01`, `DCla-Comum-02`, `DCla-Comum-03` | `DEst-AvalConsultar-01`, `DEst-AvalConsultar-02`, `DEst-AvalConsultar-03`, `DSeq-AvalConsultar-01`, `DSeq-AvalConsultar-02`, `DSeq-AvalConsultar-03`, `ECA-AvalConsultar-01` |
| `ECA-AvalConsultar-01` | `DCla-AvalConsultar-01`, `DEst-AvalConsultar-01`, `DEst-AvalConsultar-02`, `DEst-AvalConsultar-03`, `DEst-Comum-01`, `Contrato-AvalConsultar-01` | `Contrato-AvalConsultar-01`, `DEst-AvalConsultar-01`, `DEst-AvalConsultar-02`, `DEst-AvalConsultar-03` |

### Eventos (dono: Pessoa C)

| Item | Rastreia para | Rastreado por |
|---|---|---|
| `DCdu-Eventos-01` | `DCdu-Geral-01`, `DAtv-Eventos-01`, `DAtv-Eventos-02`, `DAtv-Eventos-03`, `DIhc-Eventos-01`, `DCla-Comum-01`, `DD-Eventos-01` | `DAtv-Eventos-01`, `DAtv-Eventos-02`, `DAtv-Eventos-03`, `DCdu-Geral-01`, `DD-Eventos-01`, `DIhc-Eventos-01` |
| `DAtv-Eventos-01` | `DCdu-Eventos-01`, `DSeq-Eventos-01`, `DSeq-Eventos-02`, `DSeq-Eventos-03`, `DIhc-Eventos-01`, `DEst-Eventos-01`, `DEst-Comum-01` | `DAtv-Eventos-02`, `DCdu-Eventos-01`, `DIhc-Eventos-01`, `DSeq-Eventos-01`, `DSeq-Eventos-02`, `DSeq-Eventos-03` |
| `DAtv-Eventos-02` | `DCdu-Eventos-01`, `DSeq-Eventos-04`, `DAtv-Eventos-01`, `DIhc-Eventos-01` | `DCdu-Eventos-01`, `DIhc-Eventos-01`, `DSeq-Eventos-04` |
| `DAtv-Eventos-03` | `DCdu-Eventos-01`, `DSeq-Eventos-05`, `DCla-Comum-01`, `DEst-Eventos-01` | `DCdu-Eventos-01`, `DIhc-Eventos-01`, `DSeq-Eventos-05` |
| `DIhc-Eventos-01` | `DCdu-Eventos-01`, `DAtv-Eventos-01`, `DAtv-Eventos-02`, `DAtv-Eventos-03`, `DEst-Eventos-01`, `DCla-Eventos-01`, `DSeq-Eventos-01`, `DSeq-Eventos-02`, `DSeq-Eventos-03`, `DSeq-Eventos-04`, `DSeq-Eventos-05` | `DAtv-Eventos-01`, `DAtv-Eventos-02`, `DCdu-Eventos-01`, `DCla-Eventos-01`, `DEst-Eventos-01`, `DIhc-Inicio-01`, `DSeq-Eventos-01`, `DSeq-Eventos-02`, `DSeq-Eventos-03`, `DSeq-Eventos-04`, `DSeq-Eventos-05` |
| `DD-Eventos-01` | `DCla-Eventos-01`, `DCla-Eventos-02`, `DCdu-Eventos-01`, `DD-Geral-01`, `DDados-Geral-01` | `DCdu-Eventos-01`, `DCla-Eventos-01`, `DCla-Eventos-02`, `DCla-Locais-02`, `DCla-Noticias-01`, `DCla-Noticias-02`, `DD-Geral-01`, `DD-Locais-01`, `DD-Noticias-01`, `DDados-Geral-01` |
| `DCmp-Eventos-01` | `DPac-Geral-01`, `DCmp-Comum-01`, `DCla-Eventos-01`, `DCla-Eventos-02`, `DSeq-Eventos-01` | `DCla-Eventos-01`, `DCla-Eventos-02`, `DPac-Geral-01` |
| `DCla-Eventos-01` | `DCmp-Eventos-01`, `DCla-Eventos-02`, `DCla-Comum-01`, `DCla-Comum-02`, `DCla-Comum-03`, `DIhc-Eventos-01`, `DSeq-Eventos-01`, `DEst-Eventos-01`, `Contrato-Eventos-01`, `DD-Eventos-01` | `Contrato-Eventos-01`, `DCla-Eventos-02`, `DCmp-Eventos-01`, `DD-Eventos-01`, `DIhc-Eventos-01`, `DSeq-Eventos-01`, `DSeq-Eventos-02`, `DSeq-Eventos-03`, `DSeq-Eventos-04`, `DSeq-Eventos-05`, `ECA-Eventos-01` |
| `DCla-Eventos-02` | `DCmp-Eventos-01`, `DCla-Comum-02`, `DCla-Comum-03`, `DCla-Eventos-01`, `DSeq-Eventos-01`, `DSeq-Eventos-05`, `Contrato-Eventos-01`, `DD-Eventos-01` | `Contrato-Eventos-01`, `DCla-Eventos-01`, `DCmp-Eventos-01`, `DD-Eventos-01`, `DSeq-Eventos-01`, `DSeq-Eventos-05` |
| `DSeq-Eventos-01` | `DAtv-Eventos-01`, `DIhc-Eventos-01`, `DCla-Eventos-01`, `DCla-Eventos-02`, `Contrato-Eventos-01`, `DCla-Comum-02`, `DCla-Comum-03`, `DEst-Comum-01` | `Contrato-Comum-02`, `Contrato-Eventos-01`, `DAtv-Eventos-01`, `DCla-Eventos-01`, `DCla-Eventos-02`, `DCmp-Eventos-01`, `DEst-Eventos-01`, `DIhc-Eventos-01`, `DSeq-Eventos-02`, `DSeq-Eventos-03`, `DSeq-Eventos-04`, `DSeq-Eventos-05` |
| `DSeq-Eventos-02` | `DAtv-Eventos-01`, `DIhc-Eventos-01`, `DSeq-Eventos-01`, `DCla-Eventos-01`, `Contrato-Eventos-01`, `DCla-Comum-03`, `DEst-Eventos-01` | `Contrato-Eventos-01`, `DAtv-Eventos-01`, `DEst-Eventos-01`, `DIhc-Eventos-01` |
| `DSeq-Eventos-03` | `DAtv-Eventos-01`, `DIhc-Eventos-01`, `DSeq-Eventos-01`, `DCla-Eventos-01`, `Contrato-Eventos-01`, `DCla-Comum-03`, `DEst-Eventos-01` | `Contrato-Eventos-01`, `DAtv-Eventos-01`, `DEst-Eventos-01`, `DIhc-Eventos-01` |
| `DSeq-Eventos-04` | `DAtv-Eventos-02`, `DIhc-Eventos-01`, `DSeq-Eventos-01`, `DCla-Eventos-01`, `Contrato-Eventos-01`, `DCla-Comum-03`, `DEst-Eventos-01` | `Contrato-Eventos-01`, `DAtv-Eventos-02`, `DEst-Eventos-01`, `DIhc-Eventos-01` |
| `DSeq-Eventos-05` | `DAtv-Eventos-03`, `DIhc-Eventos-01`, `DSeq-Eventos-01`, `DCla-Eventos-01`, `DCla-Eventos-02`, `Contrato-Eventos-01`, `DCla-Comum-01`, `DCla-Comum-03`, `DEst-Eventos-01` | `Contrato-Eventos-01`, `DAtv-Eventos-03`, `DCla-Eventos-02`, `DEst-Eventos-01`, `DIhc-Eventos-01` |
| `DEst-Eventos-01` | `DIhc-Eventos-01`, `DEst-Comum-01`, `DCla-Comum-03`, `DSeq-Eventos-01`, `DSeq-Eventos-02`, `DSeq-Eventos-03`, `DSeq-Eventos-04`, `DSeq-Eventos-05`, `ECA-Eventos-01` | `DAtv-Eventos-01`, `DAtv-Eventos-03`, `DCla-Eventos-01`, `DEst-Inicio-01`, `DIhc-Eventos-01`, `DSeq-Eventos-02`, `DSeq-Eventos-03`, `DSeq-Eventos-04`, `DSeq-Eventos-05`, `ECA-Eventos-01` |
| `Contrato-Eventos-01` | `DCla-Eventos-01`, `DCla-Eventos-02`, `DSeq-Eventos-01`, `DSeq-Eventos-02`, `DSeq-Eventos-03`, `DSeq-Eventos-04`, `DSeq-Eventos-05`, `ECA-Eventos-01`, `Contrato-Comum-01`, `Contrato-Comum-02`, `Contrato-Comum-03` | `Contrato-Comum-03`, `DCla-Eventos-01`, `DCla-Eventos-02`, `DSeq-Eventos-01`, `DSeq-Eventos-02`, `DSeq-Eventos-03`, `DSeq-Eventos-04`, `DSeq-Eventos-05`, `ECA-Eventos-01` |
| `ECA-Eventos-01` | `DCla-Eventos-01`, `DEst-Eventos-01`, `DEst-Comum-01`, `Contrato-Eventos-01`, `ECA-Comum-01` | `Contrato-Eventos-01`, `DEst-Eventos-01` |

### RU (dono: Pessoa C)

| Item | Rastreia para | Rastreado por |
|---|---|---|
| `DCdu-RU-01` | `DCdu-Geral-01`, `DAtv-RU-01`, `DAtv-RU-02`, `DIhc-RU-01`, `DIhc-RU-02`, `DEst-Comum-01` | `DAtv-RU-01`, `DAtv-RU-02`, `DCdu-Geral-01`, `DD-RU-01`, `DIhc-RU-01`, `DIhc-RU-02` |
| `DAtv-RU-01` | `DCdu-RU-01`, `DSeq-RU-01`, `DIhc-RU-01`, `DIhc-RU-02`, `DEst-Comum-01` | `DAtv-RU-02`, `DCdu-RU-01`, `DIhc-RU-01`, `DIhc-RU-02`, `DSeq-RU-01` |
| `DAtv-RU-02` | `DCdu-RU-01`, `DAtv-RU-01`, `DSeq-RU-02`, `DIhc-RU-02`, `DEst-Comum-01` | `DCdu-RU-01`, `DIhc-RU-02`, `DSeq-RU-02` |
| `DIhc-RU-01` | `DCdu-RU-01`, `DAtv-RU-01`, `DIhc-RU-02`, `DIhc-Inicio-01`, `DEst-RU-01`, `DSeq-RU-01` | `DAtv-RU-01`, `DCdu-RU-01`, `DCla-RU-01`, `DEst-RU-01`, `DIhc-RU-02`, `DSeq-RU-01` |
| `DIhc-RU-02` | `DCdu-RU-01`, `DAtv-RU-01`, `DAtv-RU-02`, `DIhc-RU-01`, `DEst-RU-02`, `DSeq-RU-01`, `DSeq-RU-02`, `DEst-Comum-01` | `DAtv-RU-01`, `DAtv-RU-02`, `DCdu-RU-01`, `DCla-RU-01`, `DEst-RU-02`, `DIhc-RU-01`, `DSeq-RU-01`, `DSeq-RU-02` |
| `DD-RU-01` | `DCla-RU-02`, `DCdu-RU-01`, `DD-Geral-01`, `DDados-Geral-01` | `Contrato-RU-01`, `DCla-RU-02`, `DD-Geral-01`, `DDados-Geral-01` |
| `DCmp-RU-01` | `DPac-Geral-01`, `DCmp-Comum-01`, `DCla-RU-01`, `DCla-RU-02`, `DSeq-RU-01` | `DCla-RU-01`, `DCla-RU-02`, `DPac-Geral-01` |
| `DCla-RU-01` | `DCmp-RU-01`, `DCla-RU-02`, `DCla-Comum-02`, `DCla-Comum-03`, `DIhc-RU-01`, `DIhc-RU-02`, `DSeq-RU-01`, `DSeq-RU-02`, `Contrato-RU-01` | `Contrato-RU-01`, `DCla-RU-02`, `DCmp-RU-01`, `DEst-RU-01`, `DSeq-RU-01`, `DSeq-RU-02`, `ECA-RU-01` |
| `DCla-RU-02` | `DCmp-RU-01`, `DD-RU-01`, `DCla-RU-01`, `DCla-Comum-02`, `DCla-Comum-03`, `DSeq-RU-01`, `Contrato-RU-01` | `Contrato-RU-01`, `DCla-RU-01`, `DCmp-RU-01`, `DD-RU-01`, `DSeq-RU-01` |
| `DSeq-RU-01` | `DAtv-RU-01`, `DIhc-RU-01`, `DIhc-RU-02`, `DCla-RU-01`, `DCla-RU-02`, `DCla-Comum-02`, `DCla-Comum-03`, `DEst-Comum-01`, `Contrato-RU-01` | `Contrato-RU-01`, `DAtv-RU-01`, `DCla-RU-01`, `DCla-RU-02`, `DCmp-RU-01`, `DEst-RU-01`, `DEst-RU-02`, `DIhc-RU-01`, `DIhc-RU-02`, `DSeq-RU-02` |
| `DSeq-RU-02` | `DAtv-RU-02`, `DIhc-RU-02`, `DSeq-RU-01`, `DCla-RU-01`, `Contrato-RU-01`, `ECA-RU-01` | `Contrato-RU-01`, `DAtv-RU-02`, `DCla-RU-01`, `DEst-RU-02`, `DIhc-RU-02` |
| `DEst-RU-01` | `DIhc-RU-01`, `DEst-RU-02`, `DEst-Inicio-01`, `DSeq-RU-01`, `DCla-RU-01`, `Contrato-RU-01` | `Contrato-RU-01`, `DEst-RU-02`, `DIhc-RU-01` |
| `DEst-RU-02` | `DIhc-RU-02`, `DEst-RU-01`, `DEst-Comum-01`, `DCla-Comum-03`, `DSeq-RU-01`, `DSeq-RU-02`, `ECA-RU-01` | `Contrato-RU-01`, `DEst-RU-01`, `DIhc-RU-02`, `ECA-RU-01` |
| `Contrato-RU-01` | `DCla-RU-01`, `DCla-RU-02`, `DD-RU-01`, `DSeq-RU-01`, `DSeq-RU-02`, `DEst-RU-01`, `DEst-RU-02`, `ECA-RU-01` | `DCla-RU-01`, `DCla-RU-02`, `DEst-RU-01`, `DSeq-RU-01`, `DSeq-RU-02`, `ECA-RU-01` |
| `ECA-RU-01` | `DCla-RU-01`, `DEst-RU-02`, `DEst-Comum-01`, `ECA-Comum-01`, `Contrato-RU-01` | `Contrato-RU-01`, `DEst-RU-02`, `DSeq-RU-02` |

### Noticias (dono: Pessoa C)

| Item | Rastreia para | Rastreado por |
|---|---|---|
| `DCdu-Noticias-01` | `DCdu-Geral-01`, `DAtv-Noticias-01`, `DAtv-Noticias-02`, `DIhc-Noticias-01`, `DCla-Comum-01`, `DEst-Comum-01` | `DAtv-Noticias-01`, `DAtv-Noticias-02`, `DCdu-Geral-01`, `DD-Noticias-01`, `DIhc-Noticias-01` |
| `DAtv-Noticias-01` | `DCdu-Noticias-01`, `DIhc-Noticias-01`, `DEst-Comum-01`, `DSeq-Noticias-01`, `DSeq-Noticias-02` | `DAtv-Noticias-02`, `DCdu-Noticias-01`, `DIhc-Noticias-01`, `DSeq-Noticias-01`, `DSeq-Noticias-02` |
| `DAtv-Noticias-02` | `DCdu-Noticias-01`, `DIhc-Noticias-01`, `DCla-Comum-01`, `DAtv-Noticias-01`, `DSeq-Noticias-03` | `DCdu-Noticias-01`, `DIhc-Noticias-01`, `DSeq-Noticias-03` |
| `DIhc-Noticias-01` | `DCdu-Noticias-01`, `DAtv-Noticias-01`, `DAtv-Noticias-02`, `DEst-Noticias-01`, `DCla-Noticias-01`, `DSeq-Noticias-01`, `DSeq-Noticias-02`, `DSeq-Noticias-03` | `DAtv-Noticias-01`, `DAtv-Noticias-02`, `DCdu-Noticias-01`, `DCla-Noticias-01`, `DEst-Noticias-01`, `DSeq-Noticias-01`, `DSeq-Noticias-02`, `DSeq-Noticias-03` |
| `DD-Noticias-01` | `DCla-Noticias-02`, `DCdu-Noticias-01`, `DD-Eventos-01`, `DD-Geral-01`, `DDados-Geral-01` | `Contrato-Noticias-01`, `DCla-Noticias-01`, `DCla-Noticias-02`, `DD-Geral-01`, `DDados-Geral-01` |
| `DCmp-Noticias-01` | `DPac-Geral-01`, `DCmp-Comum-01`, `DCla-Noticias-01`, `DCla-Noticias-02`, `DSeq-Noticias-01` | `DCla-Noticias-01`, `DCla-Noticias-02`, `DPac-Geral-01` |
| `DCla-Noticias-01` | `DCmp-Noticias-01`, `DCla-Noticias-02`, `DCla-Comum-01`, `DCla-Comum-02`, `DCla-Comum-03`, `DIhc-Noticias-01`, `DSeq-Noticias-01`, `DSeq-Noticias-02`, `DSeq-Noticias-03`, `DEst-Noticias-01`, `Contrato-Noticias-01`, `DD-Noticias-01`, `DD-Eventos-01` | `Contrato-Noticias-01`, `DCla-Noticias-02`, `DCmp-Noticias-01`, `DIhc-Noticias-01`, `DSeq-Noticias-01`, `DSeq-Noticias-02`, `DSeq-Noticias-03`, `ECA-Noticias-01` |
| `DCla-Noticias-02` | `DCmp-Noticias-01`, `DCla-Comum-02`, `DCla-Comum-03`, `DCla-Noticias-01`, `DSeq-Noticias-01`, `Contrato-Noticias-01`, `DD-Noticias-01`, `DD-Eventos-01` | `Contrato-Noticias-01`, `DCla-Noticias-01`, `DCmp-Noticias-01`, `DD-Noticias-01`, `DSeq-Noticias-01` |
| `DSeq-Noticias-01` | `DAtv-Noticias-01`, `DIhc-Noticias-01`, `DCla-Noticias-01`, `DCla-Noticias-02`, `Contrato-Noticias-01`, `DCla-Comum-02`, `DCla-Comum-03`, `DEst-Comum-01` | `Contrato-Noticias-01`, `DAtv-Noticias-01`, `DCla-Noticias-01`, `DCla-Noticias-02`, `DCmp-Noticias-01`, `DEst-Noticias-01`, `DIhc-Noticias-01`, `DSeq-Noticias-02`, `DSeq-Noticias-03` |
| `DSeq-Noticias-02` | `DAtv-Noticias-01`, `DIhc-Noticias-01`, `DSeq-Noticias-01`, `DCla-Noticias-01`, `Contrato-Noticias-01`, `DCla-Comum-03` | `Contrato-Noticias-01`, `DAtv-Noticias-01`, `DCla-Noticias-01`, `DEst-Noticias-01`, `DIhc-Noticias-01` |
| `DSeq-Noticias-03` | `DAtv-Noticias-02`, `DIhc-Noticias-01`, `DSeq-Noticias-01`, `DCla-Noticias-01`, `DCla-Comum-01`, `Contrato-Noticias-01`, `ECA-Noticias-01` | `Contrato-Noticias-01`, `DAtv-Noticias-02`, `DCla-Noticias-01`, `DEst-Noticias-01`, `DIhc-Noticias-01` |
| `DEst-Noticias-01` | `DIhc-Noticias-01`, `DEst-Comum-01`, `DCla-Comum-03`, `DSeq-Noticias-01`, `DSeq-Noticias-02`, `DSeq-Noticias-03`, `ECA-Noticias-01` | `Contrato-Noticias-01`, `DCla-Noticias-01`, `DIhc-Noticias-01`, `ECA-Noticias-01` |
| `Contrato-Noticias-01` | `DCla-Noticias-01`, `DCla-Noticias-02`, `DSeq-Noticias-01`, `DSeq-Noticias-02`, `DSeq-Noticias-03`, `DEst-Noticias-01`, `ECA-Noticias-01`, `DD-Noticias-01` | `DCla-Noticias-01`, `DCla-Noticias-02`, `DSeq-Noticias-01`, `DSeq-Noticias-02`, `DSeq-Noticias-03`, `ECA-Noticias-01` |
| `ECA-Noticias-01` | `DCla-Noticias-01`, `DEst-Noticias-01`, `DEst-Comum-01`, `ECA-Comum-01`, `Contrato-Noticias-01` | `Contrato-Noticias-01`, `DEst-Noticias-01`, `DSeq-Noticias-03` |

### AvalRegistrar (dono: Pessoa C)

| Item | Rastreia para | Rastreado por |
|---|---|---|
| `DCdu-AvalRegistrar-01` | `DCdu-Geral-01`, `DPac-Geral-01`, `DIhc-Inicio-01`, `DD-Locais-01`, `DCla-Comum-02`, `DEst-Comum-01`, `DAtv-AvalRegistrar-01`, `DAtv-AvalRegistrar-02`, `DAtv-AvalRegistrar-03`, `DAtv-AvalRegistrar-04`, `DIhc-AvalRegistrar-01`, `DIhc-AvalRegistrar-02`, `DIhc-AvalRegistrar-03`, `DIhc-AvalRegistrar-04`, `DD-AvalRegistrar-01`, `DCmp-AvalRegistrar-01`, `DCla-AvalRegistrar-01`, `DCla-AvalRegistrar-02`, `DCla-AvalRegistrar-03`, `DCla-AvalRegistrar-04`, `DSeq-AvalRegistrar-01`, `DSeq-AvalRegistrar-02`, `DSeq-AvalRegistrar-03`, `DSeq-AvalRegistrar-04`, `DSeq-AvalRegistrar-05`, `DEst-AvalRegistrar-01`, `DEst-AvalRegistrar-02`, `DEst-AvalRegistrar-03`, `DEst-AvalRegistrar-04`, `Contrato-AvalRegistrar-01`, `ECA-AvalRegistrar-01` | `DAtv-AvalRegistrar-01`, `DAtv-AvalRegistrar-02`, `DAtv-AvalRegistrar-03`, `DAtv-AvalRegistrar-04`, `DCdu-Geral-01`, `DD-AvalRegistrar-01`, `DIhc-AvalRegistrar-01`, `DIhc-AvalRegistrar-02`, `DIhc-AvalRegistrar-03`, `DIhc-AvalRegistrar-04`, `DSeq-AvalRegistrar-01`, `DSeq-AvalRegistrar-02`, `DSeq-AvalRegistrar-03`, `DSeq-AvalRegistrar-04`, `DSeq-AvalRegistrar-05` |
| `DAtv-AvalRegistrar-01` | `DCdu-AvalRegistrar-01`, `DIhc-AvalRegistrar-01`, `DIhc-AvalRegistrar-02`, `DEst-AvalRegistrar-02`, `DEst-Comum-01`, `DSeq-AvalRegistrar-01`, `DSeq-AvalRegistrar-02`, `DAtv-AvalRegistrar-02` | `DAtv-AvalRegistrar-02`, `DCdu-AvalRegistrar-01`, `DIhc-AvalRegistrar-01`, `DIhc-AvalRegistrar-02`, `DSeq-AvalRegistrar-01`, `DSeq-AvalRegistrar-02` |
| `DAtv-AvalRegistrar-02` | `DCdu-AvalRegistrar-01`, `DAtv-AvalRegistrar-01`, `DAtv-AvalRegistrar-03`, `DIhc-AvalRegistrar-03`, `DEst-AvalRegistrar-03`, `DSeq-AvalRegistrar-02`, `DSeq-AvalRegistrar-03`, `DSeq-AvalRegistrar-04`, `DEst-Comum-01` | `DAtv-AvalRegistrar-01`, `DAtv-AvalRegistrar-03`, `DCdu-AvalRegistrar-01`, `DIhc-AvalRegistrar-03`, `DSeq-AvalRegistrar-03`, `DSeq-AvalRegistrar-04` |
| `DAtv-AvalRegistrar-03` | `DCdu-AvalRegistrar-01`, `DAtv-AvalRegistrar-02`, `DAtv-AvalRegistrar-04`, `DIhc-AvalRegistrar-03`, `DIhc-AvalRegistrar-04`, `DEst-AvalRegistrar-03`, `DEst-AvalRegistrar-04`, `DSeq-AvalRegistrar-05` | `DAtv-AvalRegistrar-02`, `DAtv-AvalRegistrar-04`, `DCdu-AvalRegistrar-01`, `DIhc-AvalRegistrar-03`, `DIhc-AvalRegistrar-04`, `DSeq-AvalRegistrar-05` |
| `DAtv-AvalRegistrar-04` | `DCdu-AvalRegistrar-01`, `DAtv-AvalRegistrar-03`, `DCla-AvalRegistrar-01`, `DEst-AvalRegistrar-03`, `DSeq-AvalRegistrar-05`, `Contrato-AvalRegistrar-01`, `ECA-AvalRegistrar-01` | `DAtv-AvalRegistrar-03`, `DCdu-AvalRegistrar-01` |
| `DIhc-AvalRegistrar-01` | `DCdu-AvalRegistrar-01`, `DIhc-Inicio-01`, `DAtv-AvalRegistrar-01`, `DEst-AvalRegistrar-01`, `DSeq-AvalRegistrar-01`, `DCla-AvalRegistrar-01` | `DAtv-AvalConsultar-01`, `DAtv-AvalRegistrar-01`, `DCdu-AvalConsultar-01`, `DCdu-AvalRegistrar-01`, `DCla-AvalRegistrar-01`, `DEst-AvalRegistrar-01`, `DIhc-AvalConsultar-01`, `DIhc-AvalRegistrar-02`, `DIhc-AvalRegistrar-04`, `DSeq-AvalConsultar-01`, `DSeq-AvalRegistrar-01` |
| `DIhc-AvalRegistrar-02` | `DCdu-AvalRegistrar-01`, `DIhc-AvalRegistrar-01`, `DAtv-AvalRegistrar-01`, `DEst-AvalRegistrar-02`, `DEst-Comum-01`, `DSeq-AvalRegistrar-01`, `DSeq-AvalRegistrar-02`, `DCla-AvalRegistrar-01`, `DD-Locais-01` | `DAtv-AvalRegistrar-01`, `DCdu-AvalRegistrar-01`, `DCla-AvalRegistrar-01`, `DEst-AvalRegistrar-02`, `DIhc-AvalRegistrar-03`, `DSeq-AvalRegistrar-01`, `DSeq-AvalRegistrar-02` |
| `DIhc-AvalRegistrar-03` | `DCdu-AvalRegistrar-01`, `DIhc-AvalRegistrar-02`, `DIhc-AvalRegistrar-04`, `DAtv-AvalRegistrar-02`, `DAtv-AvalRegistrar-03`, `DEst-AvalRegistrar-03`, `DEst-Comum-01`, `DSeq-AvalRegistrar-02`, `DSeq-AvalRegistrar-03`, `DSeq-AvalRegistrar-04`, `DSeq-AvalRegistrar-05`, `DCla-AvalRegistrar-01` | `DAtv-AvalRegistrar-02`, `DAtv-AvalRegistrar-03`, `DCdu-AvalRegistrar-01`, `DCla-AvalRegistrar-01`, `DEst-AvalRegistrar-03`, `DIhc-AvalRegistrar-04`, `DSeq-AvalRegistrar-02`, `DSeq-AvalRegistrar-03`, `DSeq-AvalRegistrar-04`, `DSeq-AvalRegistrar-05` |
| `DIhc-AvalRegistrar-04` | `DCdu-AvalRegistrar-01`, `DIhc-AvalRegistrar-01`, `DIhc-AvalRegistrar-03`, `DAtv-AvalRegistrar-03`, `DEst-AvalRegistrar-04`, `DSeq-AvalRegistrar-05`, `DCla-AvalRegistrar-01` | `DAtv-AvalRegistrar-03`, `DCdu-AvalRegistrar-01`, `DCla-AvalRegistrar-01`, `DEst-AvalRegistrar-04`, `DIhc-AvalRegistrar-03`, `DSeq-AvalRegistrar-05` |
| `DD-AvalRegistrar-01` | `DCdu-AvalRegistrar-01`, `DCla-AvalRegistrar-03`, `DCla-AvalRegistrar-04`, `DD-Locais-01`, `DD-Geral-01`, `DDados-Geral-01` | `Contrato-AvalRegistrar-01`, `DAtv-AvalConsultar-03`, `DCdu-AvalConsultar-01`, `DCdu-AvalRegistrar-01`, `DCla-AvalConsultar-02`, `DCla-AvalRegistrar-03`, `DCla-AvalRegistrar-04`, `DCmp-AvalRegistrar-01`, `DD-AvalConsultar-01`, `DD-Geral-01`, `DDados-Geral-01`, `DIhc-AvalConsultar-03` |
| `DCmp-AvalRegistrar-01` | `DPac-Geral-01`, `DCmp-Comum-01`, `DCla-AvalRegistrar-01`, `DCla-AvalRegistrar-02`, `DCla-AvalRegistrar-03`, `DCla-AvalRegistrar-04`, `DD-AvalRegistrar-01`, `DD-Locais-01`, `DSeq-AvalRegistrar-05` | `DCdu-AvalRegistrar-01`, `DCla-AvalRegistrar-01`, `DCla-AvalRegistrar-02`, `DCla-AvalRegistrar-03`, `DCla-AvalRegistrar-04`, `DCmp-AvalConsultar-01`, `DPac-Geral-01` |
| `DCla-AvalRegistrar-01` | `DCmp-AvalRegistrar-01`, `DIhc-AvalRegistrar-01`, `DIhc-AvalRegistrar-02`, `DIhc-AvalRegistrar-03`, `DIhc-AvalRegistrar-04`, `DCla-AvalRegistrar-02`, `DCla-AvalRegistrar-03`, `DCla-AvalRegistrar-04`, `DCla-Comum-02`, `DCla-Comum-03`, `DEst-AvalRegistrar-02`, `DEst-AvalRegistrar-03`, `DD-Locais-01` | `Contrato-AvalRegistrar-01`, `DAtv-AvalRegistrar-04`, `DCdu-AvalRegistrar-01`, `DCla-AvalRegistrar-02`, `DCla-AvalRegistrar-03`, `DCla-AvalRegistrar-04`, `DCmp-AvalRegistrar-01`, `DEst-AvalRegistrar-01`, `DEst-AvalRegistrar-02`, `DEst-AvalRegistrar-03`, `DEst-AvalRegistrar-04`, `DIhc-AvalRegistrar-01`, `DIhc-AvalRegistrar-02`, `DIhc-AvalRegistrar-03`, `DIhc-AvalRegistrar-04`, `DSeq-AvalConsultar-01`, `DSeq-AvalRegistrar-01`, `DSeq-AvalRegistrar-02`, `DSeq-AvalRegistrar-03`, `DSeq-AvalRegistrar-04`, `DSeq-AvalRegistrar-05`, `ECA-AvalRegistrar-01` |
| `DCla-AvalRegistrar-02` | `DCmp-AvalRegistrar-01`, `DCla-AvalRegistrar-01`, `DCla-Comum-02`, `DCla-Comum-03`, `DD-Locais-01`, `DSeq-AvalRegistrar-01` | `Contrato-AvalRegistrar-01`, `DCdu-AvalRegistrar-01`, `DCla-AvalRegistrar-01`, `DCmp-AvalRegistrar-01`, `DSeq-AvalRegistrar-01` |
| `DCla-AvalRegistrar-03` | `DCmp-AvalRegistrar-01`, `DD-AvalRegistrar-01`, `DCla-AvalRegistrar-01`, `DCla-AvalRegistrar-04`, `DCla-Comum-02`, `DCla-Comum-03`, `DSeq-AvalRegistrar-02` | `Contrato-AvalRegistrar-01`, `DCdu-AvalRegistrar-01`, `DCla-AvalRegistrar-01`, `DCla-AvalRegistrar-04`, `DCmp-AvalRegistrar-01`, `DD-AvalRegistrar-01`, `DSeq-AvalRegistrar-02` |
| `DCla-AvalRegistrar-04` | `DCmp-AvalRegistrar-01`, `DD-AvalRegistrar-01`, `DCla-AvalRegistrar-01`, `DCla-AvalRegistrar-03`, `DCla-Comum-02`, `DD-Locais-01`, `DSeq-AvalRegistrar-05` | `Contrato-AvalRegistrar-01`, `DCdu-AvalRegistrar-01`, `DCla-AvalRegistrar-01`, `DCla-AvalRegistrar-03`, `DCmp-AvalRegistrar-01`, `DD-AvalRegistrar-01`, `DSeq-AvalRegistrar-02`, `DSeq-AvalRegistrar-05`, `ECA-AvalRegistrar-01` |
| `DSeq-AvalRegistrar-01` | `DCdu-AvalRegistrar-01`, `DAtv-AvalRegistrar-01`, `DIhc-AvalRegistrar-01`, `DIhc-AvalRegistrar-02`, `DCla-AvalRegistrar-01`, `DCla-AvalRegistrar-02`, `DCla-Comum-02`, `DCla-Comum-03`, `DEst-Comum-01`, `Contrato-AvalRegistrar-01` | `Contrato-AvalRegistrar-01`, `DAtv-AvalRegistrar-01`, `DCdu-AvalRegistrar-01`, `DCla-AvalRegistrar-02`, `DEst-AvalRegistrar-01`, `DEst-AvalRegistrar-02`, `DIhc-AvalRegistrar-01`, `DIhc-AvalRegistrar-02`, `DSeq-AvalRegistrar-02` |
| `DSeq-AvalRegistrar-02` | `DCdu-AvalRegistrar-01`, `DAtv-AvalRegistrar-01`, `DIhc-AvalRegistrar-02`, `DIhc-AvalRegistrar-03`, `DCla-AvalRegistrar-01`, `DCla-AvalRegistrar-03`, `DCla-AvalRegistrar-04`, `DCla-Comum-02`, `DCla-Comum-03`, `DEst-Comum-01`, `DSeq-AvalRegistrar-01`, `Contrato-AvalRegistrar-01` | `Contrato-AvalRegistrar-01`, `DAtv-AvalRegistrar-01`, `DAtv-AvalRegistrar-02`, `DCdu-AvalRegistrar-01`, `DCla-AvalRegistrar-03`, `DEst-AvalRegistrar-02`, `DEst-AvalRegistrar-03`, `DIhc-AvalRegistrar-02`, `DIhc-AvalRegistrar-03` |
| `DSeq-AvalRegistrar-03` | `DCdu-AvalRegistrar-01`, `DAtv-AvalRegistrar-02`, `DIhc-AvalRegistrar-03`, `DEst-AvalRegistrar-03`, `DCla-AvalRegistrar-01`, `Contrato-AvalRegistrar-01` | `Contrato-AvalRegistrar-01`, `DAtv-AvalRegistrar-02`, `DCdu-AvalRegistrar-01`, `DEst-AvalRegistrar-03`, `DIhc-AvalRegistrar-03` |
| `DSeq-AvalRegistrar-04` | `DCdu-AvalRegistrar-01`, `DAtv-AvalRegistrar-02`, `DIhc-AvalRegistrar-03`, `DEst-AvalRegistrar-03`, `DCla-AvalRegistrar-01`, `DCla-Comum-03`, `Contrato-AvalRegistrar-01` | `Contrato-AvalRegistrar-01`, `DAtv-AvalRegistrar-02`, `DCdu-AvalRegistrar-01`, `DEst-AvalRegistrar-03`, `DIhc-AvalRegistrar-03` |
| `DSeq-AvalRegistrar-05` | `DCdu-AvalRegistrar-01`, `DAtv-AvalRegistrar-03`, `DIhc-AvalRegistrar-03`, `DIhc-AvalRegistrar-04`, `DEst-AvalRegistrar-03`, `DCla-AvalRegistrar-01`, `DCla-AvalRegistrar-04`, `DCla-Comum-02`, `Contrato-AvalRegistrar-01` | `Contrato-AvalRegistrar-01`, `DAtv-AvalRegistrar-03`, `DAtv-AvalRegistrar-04`, `DCdu-AvalRegistrar-01`, `DCla-AvalRegistrar-04`, `DCmp-AvalRegistrar-01`, `DEst-AvalRegistrar-03`, `DEst-AvalRegistrar-04`, `DIhc-AvalRegistrar-03`, `DIhc-AvalRegistrar-04` |
| `DEst-AvalRegistrar-01` | `DIhc-AvalRegistrar-01`, `DEst-AvalRegistrar-02`, `DEst-AvalRegistrar-04`, `DSeq-AvalRegistrar-01`, `DCla-AvalRegistrar-01` | `DCdu-AvalRegistrar-01`, `DEst-AvalRegistrar-02`, `DEst-AvalRegistrar-04`, `DIhc-AvalRegistrar-01` |
| `DEst-AvalRegistrar-02` | `DIhc-AvalRegistrar-02`, `DEst-Comum-01`, `DCla-Comum-03`, `DEst-AvalRegistrar-01`, `DEst-AvalRegistrar-03`, `DSeq-AvalRegistrar-01`, `DSeq-AvalRegistrar-02`, `DCla-AvalRegistrar-01` | `Contrato-AvalRegistrar-01`, `DAtv-AvalRegistrar-01`, `DCdu-AvalRegistrar-01`, `DCla-AvalRegistrar-01`, `DEst-AvalRegistrar-01`, `DEst-AvalRegistrar-03`, `DIhc-AvalRegistrar-02`, `ECA-AvalRegistrar-01` |
| `DEst-AvalRegistrar-03` | `DIhc-AvalRegistrar-03`, `DEst-Comum-01`, `DCla-Comum-03`, `DEst-AvalRegistrar-02`, `DEst-AvalRegistrar-04`, `DSeq-AvalRegistrar-02`, `DSeq-AvalRegistrar-03`, `DSeq-AvalRegistrar-04`, `DSeq-AvalRegistrar-05`, `DCla-AvalRegistrar-01` | `Contrato-AvalRegistrar-01`, `DAtv-AvalRegistrar-02`, `DAtv-AvalRegistrar-03`, `DAtv-AvalRegistrar-04`, `DCdu-AvalRegistrar-01`, `DCla-AvalRegistrar-01`, `DEst-AvalRegistrar-02`, `DEst-AvalRegistrar-04`, `DIhc-AvalRegistrar-03`, `DSeq-AvalRegistrar-03`, `DSeq-AvalRegistrar-04`, `DSeq-AvalRegistrar-05`, `ECA-AvalRegistrar-01` |
| `DEst-AvalRegistrar-04` | `DIhc-AvalRegistrar-04`, `DEst-AvalRegistrar-01`, `DEst-AvalRegistrar-03`, `DSeq-AvalRegistrar-05`, `DCla-AvalRegistrar-01` | `DAtv-AvalRegistrar-03`, `DCdu-AvalRegistrar-01`, `DEst-AvalRegistrar-01`, `DEst-AvalRegistrar-03`, `DIhc-AvalRegistrar-04` |
| `Contrato-AvalRegistrar-01` | `DCla-AvalRegistrar-01`, `DCla-AvalRegistrar-02`, `DCla-AvalRegistrar-03`, `DCla-AvalRegistrar-04`, `DD-AvalRegistrar-01`, `DEst-AvalRegistrar-02`, `DEst-AvalRegistrar-03`, `DSeq-AvalRegistrar-01`, `DSeq-AvalRegistrar-02`, `DSeq-AvalRegistrar-03`, `DSeq-AvalRegistrar-04`, `DSeq-AvalRegistrar-05`, `ECA-AvalRegistrar-01`, `Contrato-Comum-02`, `Contrato-Comum-03` | `DAtv-AvalRegistrar-04`, `DCdu-AvalRegistrar-01`, `DSeq-AvalRegistrar-01`, `DSeq-AvalRegistrar-02`, `DSeq-AvalRegistrar-03`, `DSeq-AvalRegistrar-04`, `DSeq-AvalRegistrar-05`, `ECA-AvalRegistrar-01` |
| `ECA-AvalRegistrar-01` | `DCla-AvalRegistrar-01`, `DCla-AvalRegistrar-04`, `DEst-AvalRegistrar-02`, `DEst-AvalRegistrar-03`, `DEst-Comum-01`, `ECA-Comum-01`, `Contrato-AvalRegistrar-01` | `Contrato-AvalRegistrar-01`, `DAtv-AvalRegistrar-04`, `DCdu-AvalRegistrar-01` |
