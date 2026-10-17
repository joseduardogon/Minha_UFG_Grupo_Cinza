# DSeq-Eventos-01 – Sequência de A1: abrir a tela Eventos

| Campo | Valor |
|---|---|
| **Código** | `DSeq-Eventos-01` |
| **Título** | Sequência de A1: abrir a tela Eventos |
| **Autor(a)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Revisor(a)** | Phablo Tavares Paixão (Pessoa D) |
| **Status** | Em produção (primeira versão) |
| **Rastreia para** | `DAtv-Eventos-01`, `DCla-Eventos-01`, `DCla-Eventos-02`, `DCla-Comum-02`, `DCla-Comum-03`, `DEst-Comum-01` |

## Diagrama

![DSeq-Eventos-01](DSeq-Eventos-01.png)

Fonte: [`DSeq-Eventos-01.puml`](DSeq-Eventos-01.puml)

## Descrição

Detalha a atividade A1 de `DAtv-Eventos-01`: o usuário abre a tela e o app carrega os eventos de hoje na regional inicial (P-EV-2, P-EV-6). A tela cria o `CalendarioEventos` e chama `aoEntrarNaTela()` no controlador de estados do pacote Comum (`DCla-Comum-03`). O controlador pede a carga à `FonteEventos`, que lê a data e a regional selecionadas, consulta a API por meio de `IAcessoApi` (`DCla-Comum-02`) e converte a resposta em eventos. O desfecho define o estado da tela: `EXIBINDO` (lista), `VAZIO` ("sem eventos") ou `INDISPONIVEL` (qualquer `ErroApi`). A rota `/eventos` e seus parâmetros são premissa de projeto (P-EV-5). O mesmo grupo "Carregar e exibir" é referenciado nos diagramas `DSeq-Eventos-02` a `04`.

As premissas `P-EV-n` citadas estão listadas, com o que falta confirmar nas capturas de tela do app, em [`Eventos/README.md`](README.md).

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 3 (Software Design). IEEE, 2024.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
