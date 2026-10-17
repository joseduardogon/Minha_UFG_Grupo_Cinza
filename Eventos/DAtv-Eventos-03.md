# DAtv-Eventos-03 – Atividades de UC-EV-03: abrir a página do evento

| Campo | Valor |
|---|---|
| **Código** | `DAtv-Eventos-03` |
| **Título** | Atividades de UC-EV-03: abrir a página do evento |
| **Autor(a)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Revisor(a)** | Phablo Tavares Paixão (Pessoa D) |
| **Status** | Em produção (primeira versão) |
| **Rastreia para** | `DCdu-Eventos-01`, `DSeq-Eventos-05`, `DCla-Comum-01`, `DEst-Eventos-01` |

## Diagrama

![DAtv-Eventos-03](DAtv-Eventos-03.png)

Fonte: [`DAtv-Eventos-03.puml`](DAtv-Eventos-03.puml)

## Descrição

Fluxo do caso de uso UC-EV-03. A única atividade de interação é **A1 – tocar em um evento**, detalhada em `DSeq-Eventos-05`. Se o evento tem endereço, o app pede ao Navegador que o abra, por meio do componente LinkExterno do pacote Comum; se não tem, o toque não tem efeito (P-EV-4). Quando o usuário volta ao app, a tela recarrega os eventos (`DEst-Eventos-01`).

As premissas `P-EV-n` citadas estão listadas, com o que falta confirmar nas capturas de tela do app, em [`Eventos/README.md`](README.md).

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 11 (Software Engineering Models and Methods). IEEE, 2024.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
