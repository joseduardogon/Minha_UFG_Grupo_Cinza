# ECA-AvalRegistrar-01 – Regras E-C-A de Avaliação de UA (registrar)

| Campo | Valor |
|---|---|
| **Código** | `ECA-AvalRegistrar-01` |
| **Título** | Regras E-C-A de Avaliação de UA (registrar) |
| **Autor(a)** | José Eduardo Gontijo de Carvalho |
| **Revisor(a)** | Maicon Brendo da Silva (Pessoa B) |
| **Status** | Em produção |
| **Rastreia para** | `DCla-AvalRegistrar-01`, `DCla-AvalRegistrar-04`, `DEst-AvalRegistrar-02`, `DEst-AvalRegistrar-03`, `DEst-Comum-01`, `ECA-Comum-01`, `Contrato-AvalRegistrar-01` |

## Descrição

Regras ativas são reações automáticas do sistema: quando acontece um **evento**, se uma **condição** é verdadeira, executa-se uma **ação**. As regras de `AvalRegistrar` são sobre as telas `TelaEscolherUA`, `TelaQuestionario` e `TelaConfirmacao` e correspondem às transições do `DEst-AvalRegistrar-02` e do `DEst-AvalRegistrar-03`. Explicam por que a lista e o questionário são sempre carregados de novo, por que nada é enviado com pendências e por que as notas não se perdem quando o envio falha.

**Tabela 1 – Regras E-C-A de Avaliação de UA (registrar)**

| Código | Evento | Condição | Ação | Classe |
|---|---|---|---|---|
| ECA-AR-01 | A `TelaEscolherUA` é exibida (entrada pela `TelaAvaliacao` ou retorno do questionário). Especializa `ECA-CM-01` | Sempre (o app não guarda cache) | Carrega a lista de UAs de novo e volta ao estado Carregando; na entrada, cria antes a fonte e o controlador | `TelaEscolherUA` |
| ECA-AR-02 | A `TelaQuestionario` é exibida (só há entrada: voltar descarta, P-AR-8). Especializa `ECA-CM-01` | Sempre | Cria o rascunho vazio, vai à primeira dimensão e carrega o questionário (o mesmo para toda UA) | `TelaQuestionario` |
| ECA-AR-03 | O usuário dá uma nota a uma questão | O estado é EXIBINDO e não há envio em curso (P-AR-27) | Atualiza o rascunho (a nota nova substitui a anterior), retira o destaque de pendência da questão e atualiza a marca de dimensão completa ou incompleta; se estava em Validação reprovada, volta a Preenchendo; não chama o servidor | `TelaQuestionario` e `RascunhoAvaliacao` |
| ECA-AR-04 | O usuário toca em "Próxima" ou "Anterior" | O estado é EXIBINDO, não há envio em curso e há dimensão seguinte ou anterior; não se exige dimensão completa (P-AR-4) | Muda a dimensão exibida a partir dos dados em memória; não chama o servidor | `TelaQuestionario` |
| ECA-AR-05 | O usuário toca em "Enviar" | Há questão sem nota (o rascunho não está completo) | Marca as questões pendentes em todas as dimensões, vai à dimensão da primeira pendente (P-AR-28) e **não envia**; vai a Validação reprovada | `TelaQuestionario` e `RascunhoAvaliacao` |
| ECA-AR-06 | O usuário toca em "Enviar" | Toda questão tem nota (o rascunho está completo) | Monta a avaliação, só com a UA e as notas, e a envia ao servidor uma única vez (P-AR-6); vai a Enviando, e a tela ignora novos toques até o resultado (P-AR-27) | `TelaQuestionario` e `ServicoEnvioAvaliacao` |
| ECA-AR-07 | O envio termina | O resultado é `REGISTRADA` | Descarta o rascunho, encerra o questionário e abre a `TelaConfirmacao` | `TelaQuestionario` |
| ECA-AR-08 | O envio termina | O resultado é `NAO_REGISTRADA` (qualquer falha de comunicação ou resposta não bem-sucedida) | Avisa que a avaliação não foi registrada, **mantém as notas** e a dimensão atual e deixa "Enviar" disponível para nova tentativa (P-AR-6); vai a Falha no envio | `TelaQuestionario` |
| ECA-AR-09 | O usuário toca na seta de voltar do questionário | Não há envio em curso (se há, o toque é ignorado, P-AR-27) | Descarta o rascunho (nada é enviado, P-AR-8), encerra o questionário e volta à `TelaEscolherUA`, que carrega a lista de novo (`ECA-AR-01`) | `TelaQuestionario` |
| ECA-AR-10 | O usuário toca em "Concluir" | Sempre | Encerra a `TelaConfirmacao` e volta à `TelaAvaliacao`, a tela de entrada | `TelaConfirmacao` |

As regras ECA-AR-01 e ECA-AR-02 apenas especializam `ECA-CM-01` (`ECA-Comum-01`) para as duas telas com conteúdo remoto; as falhas na carga da lista e do questionário seguem `ECA-CM-02` e `ECA-CM-03` e o ciclo do `DEst-Comum-01`. As regras ECA-AR-05 a ECA-AR-08 são próprias de `AvalRegistrar`, pois o envio é um POST e não passa pelo controlador do Comum (`DCla-AvalRegistrar-04`).

As premissas `P-AR-n` citadas estão listadas em [`AvalRegistrar/README.md`](README.md).

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 11 (Software Engineering Models and Methods). IEEE, 2024.

ANTHROPIC. **Claude Code**. Assistente de IA. Disponível em: claude.ai/code. Acesso em: 30 out. 2026. Uso: rascunho do texto e dos diagramas a partir da especificação e das instruções do autor, que revisou o conteúdo. Questão: Apêndice <X>, Seção <X.1>.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
