# DAtv-Eventos-02 – Atividades de UC04.2: trocar o mês do calendário

| Campo | Valor |
|---|---|
| **Código** | `DAtv-Eventos-02` |
| **Título** | Atividades de UC04.2: trocar o mês do calendário |
| **Autor(a)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Revisor(a)** | Phablo Tavares Paixão (Pessoa D) |
| **Status** | Em produção |
| **Rastreia para** | `DCdu-Eventos-01`, `DSeq-Eventos-04`, `DAtv-Eventos-01`, `DIhc-Eventos-01` |

## Diagrama

![DAtv-Eventos-02](DAtv-Eventos-02.png)

Fonte: [`DAtv-Eventos-02.puml`](DAtv-Eventos-02.puml)

## Descrição

Fluxo do caso de uso UC04.2, que estende o UC04.1. Há uma só atividade de interação, **A1 – tocar na seta de mês** (E2, mês anterior; E3, mês seguinte, em `DIhc-Eventos-01`), detalhada em `DSeq-Eventos-04`. Depois de exibir o novo mês, o app **mantém o número do dia selecionado** (P-EV-7, confirmada nas capturas 19, 28 e 29: o dia 30 permanece selecionado de outubro a dezembro) e, se o novo mês for mais curto que o dia, passa ao último dia dele (P-EV-8, premissa não observada). Em seguida repete a consulta de eventos já descrita em `DAtv-Eventos-01`, por isso o fluxo apenas a referencia. O comportamento antigo suposto, selecionar o dia 1, foi refutado pelas capturas.

A situação das premissas P-EV-7 e P-EV-8 está na tabela de [`Eventos/README.md`](README.md).

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 11 (Software Engineering Models and Methods). IEEE, 2024.

ANTHROPIC. **Claude Code**. Assistente de IA. Disponível em: claude.ai/code. Acesso em: 30 out. 2026. Uso: apoio à redação e aos diagramas, a partir das instruções, das capturas de tela e das correções do autor (resumo em `IA/registro-C.md`). Questão: Apêndice <X>, Seção <X.1>.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
