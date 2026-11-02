# ECA-RU-01 – Regras ativas (evento-condição-ação) do pacote RU

| Campo | Valor |
|---|---|
| **Código** | `ECA-RU-01` |
| **Título** | Regras ativas (evento-condição-ação) do pacote RU |
| **Autor(a)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Revisor(a)** | Phablo Tavares Paixão (Pessoa D) |
| **Status** | Em produção |
| **Rastreia para** | `DCla-RU-01`, `DEst-RU-02`, `DEst-Comum-01`, `ECA-Comum-01`, `Contrato-RU-01` |

## Descrição

Regras ativas são reações automáticas do sistema: quando acontece um **evento**, se uma **condição** é verdadeira, executa-se uma **ação**. A funcionalidade RU tem quatro regras, todas sobre a tela da refeição (`TelaRefeicao`). A tela RU é estática e não tem regras (P-RU-2). Elas seguem o padrão da Rádio (`ECA-Radio-01`): a semana é carregada de uma vez e a troca de dia só filtra a memória.

**Tabela 1 – Regras E-C-A do RU**

| Código | Evento | Condição | Ação | Classe |
|---|---|---|---|---|
| ECA-RU-01 | A tela da refeição volta a ser exibida (entrada pela tela RU ou retorno ao app) | Sempre (o app não guarda cache) | Carrega a semana da refeição de novo (`aoEntrarNaTela()`) e volta ao estado Carregando; no retorno, o dia selecionado é mantido. Especializa `ECA-CM-01` (`ECA-Comum-01`) | `TelaRefeicao` |
| ECA-RU-02 | O usuário toca em uma letra do seletor de dia | O estado é EXIBINDO (o seletor só aparece nesse estado: P-RU-8, P-RU-9) | Seleciona o dia, atualiza a cor, a data por extenso e o destaque do seletor, e mostra o cardápio do dia a partir da semana em memória, sem chamada à API e sem passar por Carregando (P-RU-3) | `TelaRefeicao` |
| ECA-RU-03 | O usuário sai da tela da refeição pela seta de voltar | Sempre | Descarta a seleção, o controlador, a semana em memória e o dia selecionado; ao tocar de novo em uma refeição, uma tela nova é criada e o dia volta a ser hoje (P-RU-13) | `TelaRefeicao` |
| ECA-RU-04 | O seletor de dia da tela da refeição é montado | A refeição é o Jantar | O seletor oferece de segunda a sexta (cinco letras), sem sábado; nas demais refeições, oferece de segunda a sábado (P-RU-4, confirmada: capturas 14, 22 a 27) | `TelaRefeicao` |

As regras ECA-RU-01 a ECA-RU-03 correspondem às transições de `DEst-RU-02`. **A regra ECA-RU-04 é um fato confirmado**, e não uma premissa: a captura 26 (versão 3.2.0) mostra o seletor do Jantar com cinco letras, S, T, Q, Q, S, e as capturas do Café da Manhã e do Almoço mostram seis. Ela substitui a hipótese anterior de que o jantar de sábado abriria sem itens. Não há regra ativa para falhas de comunicação nem para o vazio: o tratamento de `ErroApi` e da lista vazia é comum a todas as telas e está em `DEst-Comum-01` (`ECA-CM-02` e `ECA-CM-03`); o vazio de um único dia, não observado, é tratado pela tela (P-RU-9).

As premissas `P-RU-n` citadas estão listadas, com o que as capturas de tela do app (versão 3.2.0) e o autor confirmaram e o que falta confirmar, em [`RU/README.md`](README.md).

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 11 (Software Engineering Models and Methods). IEEE, 2024.

ANTHROPIC. **Claude Code**. Assistente de IA. Disponível em: claude.ai/code. Acesso em: 30 out. 2026. Uso: apoio à redação e aos diagramas, a partir das instruções, das capturas de tela e das correções do autor (resumo em `IA/registro-C.md`). Questão: Apêndice <X>, Seção <X.1>.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
