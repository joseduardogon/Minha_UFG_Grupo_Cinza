# DSeq-Eventos-05 – Sequência de A1 e A2 de UC04.3: tocar em um evento e voltar ao app

| Campo | Valor |
|---|---|
| **Código** | `DSeq-Eventos-05` |
| **Título** | Sequência de A1 e A2 de UC04.3: tocar em um evento e voltar ao app |
| **Autor(a)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Revisor(a)** | Phablo Tavares Paixão (Pessoa D) |
| **Status** | Em produção |
| **Rastreia para** | `DAtv-Eventos-03`, `DIhc-Eventos-01`, `DSeq-Eventos-01`, `DCla-Eventos-01`, `DCla-Eventos-02`, `Contrato-Eventos-01`, `DCla-Comum-01`, `DCla-Comum-03`, `DEst-Eventos-01` |

## Diagrama

![DSeq-Eventos-05](DSeq-Eventos-05.png)

Fonte: [`DSeq-Eventos-05.puml`](DSeq-Eventos-05.puml)

## Descrição

Detalha as atividades A1 (tocar em um evento) e A2 (voltar ao app) de `DAtv-Eventos-03` (eventos E5 e E0, retorno, de `DIhc-Eventos-01`). A primeira mensagem é a operação `aoTocarEvento(evento)` da `TelaEventos`.

- **Toque (A1).** A tela consulta `Evento.temUrl()`. Se há endereço, chama `ILinkExterno.abrirUrl(url)`; o componente LinkExterno (`DCla-Comum-01`) valida a URL, procura um app compatível e dispara a abertura no Navegador. A tela não trata o `ResultadoAbertura`, pois o app atual não mostra mensagem de falha. Sem endereço, nada acontece. Da interação só se observou a página já aberta (capturas 8 e 21: título, local e período); o toque no cartão e o caso sem endereço são a premissa P-EV-4.
- **Retorno (A2).** Ao voltar do Navegador, a tela é exibida de novo: `aoExibir()` é chamado, e a tela, que ainda tem o `CalendarioEventos` e o controlador, chama `aoEntrarNaTela()`. O grupo "Carregar e exibir" de `DSeq-Eventos-01` se repete com **o mesmo filtro** (data e regional mantidas); o filtro só é reiniciado na entrada pelo menu inicial. O estado da tela é tratado em `DEst-Eventos-01`.

Situação da premissa P-EV-4 (pendente): ver [`Eventos/README.md`](README.md).

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 3 (Software Design). IEEE, 2024.

ANTHROPIC. **Claude Code**. Assistente de IA. Disponível em: claude.ai/code. Acesso em: 30 out. 2026. Uso: apoio à redação e aos diagramas, a partir das instruções, das capturas de tela e das correções do autor (resumo em `IA/registro-C.md`). Questão: Apêndice <X>, Seção <X.1>.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
