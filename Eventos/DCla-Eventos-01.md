# DCla-Eventos-01 – Classes do componente TelaEventos

| Campo | Valor |
|---|---|
| **Código** | `DCla-Eventos-01` |
| **Título** | Classes do componente TelaEventos |
| **Autor(a)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Revisor(a)** | Phablo Tavares Paixão (Pessoa D) |
| **Status** | Em produção (primeira versão) |
| **Rastreia para** | `DCmp-Eventos-01`, `DCla-Comum-01`, `DCla-Comum-03`, `DIhc-Eventos-01`, `DSeq-Eventos-01`, `Contrato-Eventos-01` |

## Diagrama

![DCla-Eventos-01](DCla-Eventos-01.png)

Fonte: [`DCla-Eventos-01.puml`](DCla-Eventos-01.puml)

## Descrição

Classes do componente TelaEventos.

- **TelaEventos** representa a tela. Cada método `ao...` corresponde a um evento de interação do protótipo (`DIhc-Eventos-01`): `aoExibir` (E0), `aoEscolherRegional` (E1), `aoTrocarMes` (E2 e E3), `aoEscolherData` (E4) e `aoTocarEvento` (E5). Implementa `IObservadorEstado` (pacote Comum, `DCla-Comum-03`) e, em `aoMudarEstado`, mostra a lista, a mensagem de "sem eventos", a de indisponibilidade ou o indicador de carregamento.
- **CalendarioEventos** guarda o mês exibido, a data selecionada e a regional selecionada, e oferece a lista de dias do mês para desenhar o calendário. Implementa `IFiltroEventos`, interface que a `FonteEventos` usa para ler a data e a regional (`DCla-Eventos-02`).
- **Regional** é entidade de dono Pessoa C, compartilhada com Notícias e Locais (`Integracao/entidades/Entidade-Regional.md`). Aparece aqui só como referência; sua localização no `DPac-Geral-01` é pendência da integração, e a proposta da Pessoa C é mantê-la em `Comum`.

As classes e interfaces dos estereótipos `<<Comum>>` pertencem ao pacote Comum e não são redefinidas aqui. Os contratos das operações estão em `Contrato-Eventos-01`.

As premissas `P-EV-n` citadas estão listadas, com o que falta confirmar nas capturas de tela do app, em [`Eventos/README.md`](README.md).

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 3 (Software Design). IEEE, 2024.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
