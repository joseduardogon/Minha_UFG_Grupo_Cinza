# DAtv-RU-01 – Atividades de UC06.1: consultar o cardápio de uma refeição

| Campo | Valor |
|---|---|
| **Código** | `DAtv-RU-01` |
| **Título** | Atividades de UC06.1: consultar o cardápio de uma refeição |
| **Autor(a)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Revisor(a)** | Phablo Tavares Paixão (Pessoa D) |
| **Status** | Em produção |
| **Rastreia para** | `DCdu-RU-01`, `DSeq-RU-01`, `DIhc-RU-01`, `DIhc-RU-02`, `DEst-Comum-01` |

## Diagrama

![DAtv-RU-01](DAtv-RU-01.png)

Fonte: [`DAtv-RU-01.puml`](DAtv-RU-01.puml)

## Descrição

Fluxo do caso de uso UC06.1 do `DCdu-RU-01` em raias: Membro, App e Servidor/API. As ações em que o usuário interage com o app são numeradas, e cada uma gera um diagrama de sequência (contrato-base, seção 6):

| Atividade | Ação do usuário | Diagrama de sequência |
|---|---|---|
| A1 | Tocar no cartão de uma refeição (o app abre a tela da refeição e carrega o cardápio da semana inteira) | `DSeq-RU-01` |

Tocar no cartão RU do menu inicial é o evento E7 do `DIhc-Inicio-01`; a tela RU que se abre é estática (P-RU-2) e mostra as três refeições (P-RU-1), então a sua exibição é um passo interno trivial e não gera diagrama de sequência. A chamada ao servidor e a exibição do resultado fazem parte da atividade A1, e por isso são mensagens do `DSeq-RU-01`, e não atividades separadas. O app pede **uma só vez** o cardápio da semana da refeição (P-RU-3); a partir daí, o servidor não é mais consultado enquanto a tela estiver aberta (`DAtv-RU-02`). Os desfechos são três: falha de comunicação, que mostra a ilustração e "Cardápio indisponível." (observado na captura 30: P-RU-8); semana sem refeições, que mostra a mensagem de vazio; e semana com refeições, que seleciona o dia (hoje, ou a segunda-feira se hoje não tem letra no seletor: P-RU-13) e mostra um cartão por categoria, ou a mensagem de vazio se aquele dia não tem itens (os dois casos de vazio não foram observados: P-RU-9). Todos seguem o ciclo genérico de `DEst-Comum-01`.

A seta de voltar das duas telas não é atividade deste fluxo: é modelada em `DIhc-RU-01`, `DIhc-RU-02` e `DEst-RU-01`.

As premissas `P-RU-n` citadas estão listadas, com o que as capturas de tela do app (versão 3.2.0) e o autor confirmaram e o que falta confirmar, em [`RU/README.md`](README.md).

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 11 (Software Engineering Models and Methods). IEEE, 2024.

ANTHROPIC. **Claude Code**. Assistente de IA. Disponível em: claude.ai/code. Acesso em: 30 out. 2026. Uso: apoio à redação e aos diagramas, a partir das instruções, das capturas de tela e das correções do autor (resumo em `IA/registro-C.md`). Questão: Apêndice <X>, Seção <X.1>.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
