# REV-PR11 – Revisão de Avaliação – Registrar

- **PR:** #11 "Reapply 'Document AvalRegistrar specification'" (branch `a/avalregistrar-pr`, commit `e6dbf88`)
- **Autor:** Pessoa C
- **Revisor:** Pessoa D
- **Data:** 31/10/2026
- **Tarefa:** D-REV-01

## 1. Resumo

Os 23 `.puml` compilam sem erro, e os nomes de arquivo batem com o `@startuml`. A cascata
está completa: DCdu, DAtv por caso de uso, DIhc, DD, DCmp, DCla, DSeq, DEst por DIhc,
contratos de todas as operações e ECA. As regras da avaliação estão respeitadas: avaliador
anônimo, várias avaliações por UA, nenhuma operação de edição ou exclusão e notas de 0 a 5.
`UnidadeAcademica` herda de `Local` e é só referenciada. O Comum é usado sem redefinição.

**Parecer: aprovar.** Os dois bloqueantes da seção 2 serão corrigidos pela Pessoa D,
junto com a cascata de Avaliação – Consultar notas (D-AVC-01). A Pessoa C concordou com
isso para não atrasar o início do AvalConsultar, que depende deste PR.

## 2. Bloqueantes (correção a cargo da Pessoa D)

| # | Local | Problema | Correção |
|---|---|---|---|
| B1 | `AvalRegistrar/DAtv-AvalRegistrar-01.puml:32-35`, `AvalRegistrar/DAtv-AvalRegistrar-02.puml` e `.md:20` | A carga do questionário não está em nenhum DAtv. O DAtv-01 termina em "Abrir a TelaQuestionario", e o DAtv-02 parte do questionário "já em memória". Assim, o passo (1) e o fluxo alternativo A1 do UC09.2 (pedido ao servidor, vazio ou indisponível) não têm atividade, embora tenham `DEst-AvalRegistrar-03` e `DSeq-AvalRegistrar-02`. | No início do DAtv-02, acrescentar o pedido do questionário na raia Servidor/API e a decisão "falha / vazio / exibe", e alinhar o texto dos dois `.md`. |
| B2 | `AvalRegistrar/DAtv-AvalRegistrar-02.puml:16-31` | O abandono do questionário (UC09.2, A2; P-AR-8) não tem caminho: o laço só termina em "Enviar". Mesmo assim, o `DEst-AvalRegistrar-03` trata "E5 aoVoltar (descarta o rascunho)". | Acrescentar ao laço o ramo "Tocar na seta de voltar" → "Descartar o rascunho" → fim. |

## 3. Verificações sem problema

- Não há operação de editar nem de excluir avaliação, e nenhum dado do avaliador é guardado.
- A nota fica entre 0 e 5 no DD (`NotaQuestao.valor {0..5}`), no contrato e no ECA.
- `Local <|-- UnidadeAcademica` (`DCla-AvalRegistrar-02.puml:53`). Os atributos de UA são um
  subconjunto do `DD-Locais-01`, ou seja, a entidade é referenciada, não redefinida.
- As assinaturas do Comum (`IAcessoApi`, `RespostaApi`, `IFonteDados<T>`,
  `ControladorTelaRemota`) batem com `DCla-Comum-02` e `DCla-Comum-03`.
- Os eventos dos DIhc 01 a 04 são exatamente os tratados nos DEst 01 a 04.
- Os nomes de operação nos DSeq batem com os DCla e o contrato.
- O "Rastreia para" está preenchido em todos os itens.
