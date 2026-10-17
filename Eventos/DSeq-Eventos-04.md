# DSeq-Eventos-04 – Sequência de A1 de UC-EV-02: trocar o mês

| Campo | Valor |
|---|---|
| **Código** | `DSeq-Eventos-04` |
| **Título** | Sequência de A1 de UC-EV-02: trocar o mês |
| **Autor(a)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Revisor(a)** | Phablo Tavares Paixão (Pessoa D) |
| **Status** | Em produção (primeira versão) |
| **Rastreia para** | `DAtv-Eventos-02`, `DSeq-Eventos-01`, `DCla-Eventos-01`, `DCla-Comum-03`, `DEst-Eventos-01` |

## Diagrama

![DSeq-Eventos-04](DSeq-Eventos-04.png)

Fonte: [`DSeq-Eventos-04.puml`](DSeq-Eventos-04.puml)

## Descrição

Detalha a atividade A1 de `DAtv-Eventos-02` (eventos E2 e E3 do protótipo). O `deslocamento` é -1 (mês anterior) ou +1 (mês seguinte). `CalendarioEventos.trocarMes` muda o mês exibido e seleciona o primeiro dia dele (P-EV-3); em seguida a tela pede `recarregar()` e o ciclo de carga de `DSeq-Eventos-01` se repete.

As premissas `P-EV-n` citadas estão listadas, com o que falta confirmar nas capturas de tela do app, em [`Eventos/README.md`](README.md).

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 3 (Software Design). IEEE, 2024.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
