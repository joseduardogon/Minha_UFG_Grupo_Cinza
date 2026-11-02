# DD-AppsUFG-01 – Entrada de DD dos Apps UFG

| Campo | Valor |
|---|---|
| **Código** | `DD-AppsUFG-01` |
| **Título** | Entrada de DD dos Apps UFG |
| **Autor(a)** | Maicon Brendo da Silva |
| **Revisor(a)** | Pessoa C |
| **Status** | Em produção |
| **Rastreia para** | `DCla-AppsUFG-01`, `DCdu-AppsUFG-01`, `DD-Geral-01`, `DDados-Geral-01` |

## Descrição

Os Apps UFG **não têm entidade de domínio**. O catálogo de aplicativos é fixo no app (`AplicativoUFG`, `DCla-AppsUFG-01`), com três instâncias estáticas (`RU_UFG`, `INVENTARIO_PATRIMONIAL` e `CS_CANDIDATO`): não vem do Servidor/API e não é persistido. `AplicativoUFG` é, portanto, configuração do app, e os Apps UFG não contribuem com classes para o `DDados-Geral-01` nem com entradas para o `DD-Geral-01`.

Registro da configuração, só para referência (não entra no DD consolidado):

| Nome | Atributo | Tipo | Descrição |
|---|---|---|---|
| AplicativoUFG | id | String | Identificador do aplicativo no catálogo |
| AplicativoUFG | nome | String | Nome exibido no catálogo |
| AplicativoUFG | idPacote | String | Identificador do aplicativo na Play Store |
| AplicativoUFG | iconeRes | String | Recurso local do ícone exibido no catálogo |

Trecho PlantUML para o DD consolidado: nenhum.

## Referências

ANTHROPIC. **Claude Code**. Assistente de IA. Disponível em: https://claude.com/claude-code. Acesso em: 2 nov. 2026.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
