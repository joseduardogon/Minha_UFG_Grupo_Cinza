# DAtv-RU-02 – Atividades de UC06.2: escolher o dia da semana

| Campo | Valor |
|---|---|
| **Código** | `DAtv-RU-02` |
| **Título** | Atividades de UC06.2: escolher o dia da semana |
| **Autor(a)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Revisor(a)** | Phablo Tavares Paixão (Pessoa D) |
| **Status** | Em produção |
| **Rastreia para** | `DCdu-RU-01`, `DAtv-RU-01`, `DSeq-RU-02`, `DIhc-RU-02`, `DEst-Comum-01` |

## Diagrama

![DAtv-RU-02](DAtv-RU-02.png)

Fonte: [`DAtv-RU-02.puml`](DAtv-RU-02.puml)

## Descrição

Fluxo do caso de uso UC06.2 do `DCdu-RU-01`, que estende o UC06.1. Há uma só ação de interação (contrato-base, seção 6):

| Atividade | Ação do usuário | Diagrama de sequência |
|---|---|---|
| A1 | Tocar em uma letra do seletor de dia (evento E1 do `DIhc-RU-02`) | `DSeq-RU-02` |

Ao tocar, o app destaca o dia escolhido, muda a cor da barra e do fundo, atualiza a data por extenso e **filtra o cardápio da semana, que já está em memória, pelo dia escolhido**. Não há chamada ao servidor nem estado de carregamento (P-RU-3), e por isso este fluxo não tem a raia Servidor/API, ao contrário de `DAtv-RU-01`. O seletor tem seis letras (segunda a sábado) e, no Jantar, cinco (segunda a sexta), como no `DIhc-RU-02` (P-RU-4). Se o dia não tem itens, o app mostra a mensagem genérica de vazio, como a Rádio faz com um dia sem programas; esse caso não foi observado (P-RU-9). O destaque, a cor e a data são passos internos que fazem parte da atividade A1 e do seu `DSeq-RU-02`.

As premissas `P-RU-n` citadas estão listadas, com o que as capturas de tela do app (versão 3.2.0) e o autor confirmaram e o que falta confirmar, em [`RU/README.md`](README.md).

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 11 (Software Engineering Models and Methods). IEEE, 2024.

ANTHROPIC. **Claude Code**. Assistente de IA. Disponível em: claude.ai/code. Acesso em: 30 out. 2026. Uso: apoio à redação e aos diagramas, a partir das instruções, das capturas de tela e das correções do autor (resumo em `IA/registro-C.md`). Questão: Apêndice <X>, Seção <X.1>.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
