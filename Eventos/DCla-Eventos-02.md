# DCla-Eventos-02 – Classes do componente FonteEventos

| Campo | Valor |
|---|---|
| **Código** | `DCla-Eventos-02` |
| **Título** | Classes do componente FonteEventos |
| **Autor(a)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Revisor(a)** | Phablo Tavares Paixão (Pessoa D) |
| **Status** | Em produção (primeira versão) |
| **Rastreia para** | `DCmp-Eventos-01`, `DCla-Comum-02`, `DCla-Comum-03`, `DCla-Eventos-01`, `DSeq-Eventos-01`, `Contrato-Eventos-01`, `Entidade-Evento` |

## Diagrama

![DCla-Eventos-02](DCla-Eventos-02.png)

Fonte: [`DCla-Eventos-02.puml`](DCla-Eventos-02.puml)

## Descrição

Classes do componente FonteEventos.

- **FonteEventos** implementa a interface `IFonteDados<Evento>` do pacote Comum (`DCla-Comum-03`). Em `carregar()`, lê a data e a regional pela `IFiltroEventos`, monta os parâmetros (`regional` e `data`), consulta a API com `IAcessoApi.obter("/eventos", ...)` (`DCla-Comum-02`) e converte o JSON em uma lista de `Evento`. Não trata falhas: o `ErroApi` lançado pelo acesso à API segue até o controlador de estados, que define o estado Indisponível.
- **Evento** é a entidade exibida na lista: título, período (data de início e de fim, que pode ser a mesma), local, endereço opcional da página e regional. O `local` aparece na página do evento (captura da versão 3.2.0); falta confirmar se a lista também o mostra. `temUrl()` diz se o toque no evento abre o Navegador. Atributos completos no dicionário de dados (`Integracao/entidades/Entidade-Evento.md`).
- A conversão do JSON em objetos fica nesta fonte, e não no pacote Comum, porque só a funcionalidade conhece o formato (`DCla-Comum-02`). A rota `/eventos` e o formato da resposta são premissa de projeto (P-EV-5): o app real não deixa o contrato da API visível.

Os contratos das operações estão em `Contrato-Eventos-01`.

As premissas `P-EV-n` citadas estão listadas, com o que falta confirmar nas capturas de tela do app, em [`Eventos/README.md`](README.md).

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 3 (Software Design). IEEE, 2024.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
