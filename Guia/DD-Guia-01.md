# DD-Guia-01 – Entrada de DD do Guia Estudantil

| Campo | Valor |
|---|---|
| **Código** | `DD-Guia-01` |
| **Título** | Entrada de DD do Guia Estudantil |
| **Autor(a)** | Pessoa D |
| **Revisor(a)** | Pessoa C |
| **Status** | Em produção |
| **Rastreia para** | `DCla-Guia-01`, `DCdu-Guia-01`, `DD-Geral-01`, `DDados-Geral-01` |

## Descrição

O Guia Estudantil **não tem entidade de domínio**. A URL do `guiaestudantil.pdf` é uma configuração fixa no app (`ConfiguracaoGuia`, `DCla-Guia-01`): não vem do Servidor/API e não é persistida. Por isso o Guia não contribui com classes para o `DDados-Geral-01` nem com entradas para o `DD-Geral-01`.

Registro da configuração, só para referência (não entra no DD consolidado):

| Nome | Atributo | Tipo | Descrição |
|---|---|---|---|
| ConfiguracaoGuia | urlGuia | String | URL externa do arquivo guiaestudantil.pdf |
| ConfiguracaoGuia | tipoMime | String | Tipo do documento, fixo em `application/pdf` |

Trecho PlantUML para o DD consolidado: nenhum.

## Referências

ANTHROPIC. **Claude Code**. Assistente de IA. Disponível em: https://claude.com/claude-code. Acesso em: 20 out. 2026.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
