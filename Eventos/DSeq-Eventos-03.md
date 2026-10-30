# DSeq-Eventos-03 – Sequência de A3: escolher outra regional

| Campo | Valor |
|---|---|
| **Código** | `DSeq-Eventos-03` |
| **Título** | Sequência de A3: escolher outra regional |
| **Autor(a)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Revisor(a)** | Phablo Tavares Paixão (Pessoa D) |
| **Status** | Em produção |
| **Rastreia para** | `DAtv-Eventos-01`, `DIhc-Eventos-01`, `DSeq-Eventos-01`, `DCla-Eventos-01`, `Contrato-Eventos-01`, `DCla-Comum-03`, `DEst-Eventos-01` |

## Diagrama

![DSeq-Eventos-03](DSeq-Eventos-03.png)

Fonte: [`DSeq-Eventos-03.puml`](DSeq-Eventos-03.puml)

## Descrição

Detalha a atividade A3 de `DAtv-Eventos-01` (evento E1 de `DIhc-Eventos-01`). A primeira mensagem é a operação `aoEscolherRegional(regional)` da `TelaEventos`, com uma das regionais de `regionaisOferecidas` (P-EV-2). A tela atualiza a regional no `CalendarioEventos` e pede `recarregar()` ao controlador, que repete o ciclo de carga de `DSeq-Eventos-01`. A data selecionada não muda. A regional é escolhida em abas, como em Notícias: só a aba "GOIÂNIA" foi vista, selecionada ao abrir a tela. As demais regionais, a lista fixa no app e o que acontece ao tocar em outra aba não foram observados (P-EV-2). A faixa de abas só aparece com a lista exibida e some no estado sem eventos (captura 29, P-EV-10), de modo que esta operação só ocorre no estado `EXIBINDO`. A situação das premissas está em [`Eventos/README.md`](README.md).

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 3 (Software Design). IEEE, 2024.

ANTHROPIC. **Claude Code**. Assistente de IA. Disponível em: claude.ai/code. Acesso em: 30 out. 2026. Uso: apoio à redação e aos diagramas, a partir das instruções, das capturas de tela e das correções do autor (resumo em `IA/registro-C.md`). Questão: Apêndice <X>, Seção <X.1>.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
