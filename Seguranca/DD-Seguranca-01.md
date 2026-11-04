# DD-Seguranca-01 – Entrada de DD da Segurança

| Campo | Valor |
|---|---|
| **Código** | `DD-Seguranca-01` |
| **Título** | Entrada de DD da Segurança |
| **Autor(a)** | Maicon Brendo da Silva |
| **Revisor(a)** | José Eduardo Gontijo de Carvalho |
| **Status** | Em produção |
| **Rastreia para** | `DCla-Seguranca-01`, `DCdu-Seguranca-01`, `DD-Geral-01`, `DDados-Geral-01` |

## Descrição

A Segurança **não tem entidade de domínio**. O endereço da versão web e o identificador do app na Play Store são constantes do app (`ConfiguracaoSeguranca`, `DCla-Seguranca-01`): não vêm do Servidor/API e não são persistidos. Por isso a Segurança não contribui com classes para o `DDados-Geral-01` nem com entradas para o `DD-Geral-01`.

Registro da configuração, só para referência (não entra no DD consolidado):

| Nome | Atributo | Tipo | Descrição |
|---|---|---|---|
| ConfiguracaoSeguranca | urlWeb | String | Endereço da versão web do sistema de segurança |
| ConfiguracaoSeguranca | idPacoteApp | String | Identificador do app de segurança na Play Store |

Trecho PlantUML para o DD consolidado: nenhum.

## Referências

ANTHROPIC. **Claude Code**. Assistente de IA. Disponível em: https://claude.com/claude-code. Acesso em: 2 nov. 2026.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
