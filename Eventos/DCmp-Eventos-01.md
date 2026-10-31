# DCmp-Eventos-01 – Componentes do pacote Eventos

| Campo | Valor |
|---|---|
| **Código** | `DCmp-Eventos-01` |
| **Título** | Componentes do pacote Eventos |
| **Autor(a)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Revisor(a)** | Phablo Tavares Paixão (Pessoa D) |
| **Status** | Em produção |
| **Rastreia para** | `DPac-Geral-01`, `DCmp-Comum-01`, `DCla-Eventos-01`, `DCla-Eventos-02`, `DSeq-Eventos-01` |

## Diagrama

![DCmp-Eventos-01](DCmp-Eventos-01.png)

Fonte: [`DCmp-Eventos-01.puml`](DCmp-Eventos-01.puml)

## Descrição

O pacote `Eventos` tem dois componentes. Eles dependem do pacote `Comum` apenas por interfaces, como pede o `DPac-Geral-01`, e não dependem de nenhum outro pacote de funcionalidade.

**Tabela 1 – Componentes do pacote Eventos**

| Componente | Responsabilidade | Interface oferecida | Interfaces requeridas (pacote Comum) | Classes |
|---|---|---|---|---|
| TelaEventos | Exibe o calendário, a faixa de abas de regional e a lista de cartões; guarda a data e a regional selecionadas; trata os toques do usuário | `IFiltroEventos` | `IControladorTelaRemota`, `ILinkExterno`, `IAcessoApi` (só para entregá-lo à `FonteEventos`) | `DCla-Eventos-01` |
| FonteEventos | Busca os eventos da regional e da data selecionadas na API e os converte em objetos `Evento` | `IFonteDados` (implementada para `Evento`) | `IAcessoApi`, `IFiltroEventos` | `DCla-Eventos-02` |

**Como os componentes cooperam.** Na primeira exibição, a `TelaEventos` cria a `FonteEventos` (entregando a ela o `IAcessoApi` e o seu calendário como `IFiltroEventos`) e um controlador de estados (`ControladorTelaRemota<Evento>`, pacote Comum), que recebe a `FonteEventos` como fonte de dados; a tela se registra nele como observador (`DSeq-Eventos-01`). Quando a data ou a regional mudam, a tela pede `recarregar()` ao controlador, e a `FonteEventos` lê o novo filtro pela interface `IFiltroEventos`. Esse desenho segue o modelo de uso descrito em `DCmp-Comum-01`.

**Decisão de projeto.** O estado do filtro (mês exibido, data e regional) fica na tela, no `CalendarioEventos`, e é lido pela fonte de dados por uma interface. Assim, a fonte não conhece a interface gráfica e pode ser testada sozinha.

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 3 (Software Design). IEEE, 2024.

ANTHROPIC. **Claude Code**. Assistente de IA. Disponível em: claude.ai/code. Acesso em: 30 out. 2026. Uso: apoio à redação e aos diagramas, a partir das instruções, das capturas de tela e das correções do autor (resumo em `IA/registro-C.md`). Questão: Apêndice <X>, Seção <X.1>.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
