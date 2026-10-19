# DAtv-Eventos-01 – Atividades de UC-EV-01: consultar eventos por regional e data

| Campo | Valor |
|---|---|
| **Código** | `DAtv-Eventos-01` |
| **Título** | Atividades de UC-EV-01: consultar eventos por regional e data |
| **Autor(a)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Revisor(a)** | Phablo Tavares Paixão (Pessoa D) |
| **Status** | Em produção (primeira versão) |
| **Rastreia para** | `DCdu-Eventos-01`, `DSeq-Eventos-01`, `DSeq-Eventos-02`, `DSeq-Eventos-03`, `DIhc-Eventos-01`, `DEst-Comum-01` |

## Diagrama

![DAtv-Eventos-01](DAtv-Eventos-01.png)

Fonte: [`DAtv-Eventos-01.puml`](DAtv-Eventos-01.puml)

## Descrição

Fluxo do caso de uso UC-EV-01 em raias: o Membro, o App e o Servidor/API. As ações em que o usuário interage com o app são numeradas e cada uma gera um diagrama de sequência (contrato-base, seção 6):

| Atividade | Ação do usuário | Diagrama de sequência |
|---|---|---|
| A1 | Abrir a tela Eventos (o app carrega os eventos de hoje na regional inicial) | `DSeq-Eventos-01` |
| A2 | Escolher outra data no calendário | `DSeq-Eventos-02` |
| A3 | Escolher outra regional | `DSeq-Eventos-03` |

A chamada ao servidor e a exibição do resultado (lista, "sem eventos" ou indisponibilidade) acontecem em cada uma dessas atividades. Por isso são mensagens dentro do diagrama de sequência da atividade que as dispara, e não atividades separadas; separá-las duplicaria diagramas sem acrescentar informação. Os três desfechos da consulta seguem o ciclo genérico de `DEst-Comum-01`.

As premissas `P-EV-n` citadas estão listadas, com o que falta confirmar nas capturas de tela do app, em [`Eventos/README.md`](README.md).

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 11 (Software Engineering Models and Methods). IEEE, 2024.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
