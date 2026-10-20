# Contrato-Guia-01 – Contratos das operações do pacote Guia

| Campo | Valor |
|---|---|
| **Código** | `Contrato-Guia-01` |
| **Título** | Contratos das operações do pacote Guia |
| **Autor(a)** | Pessoa D |
| **Revisor(a)** | Pessoa C |
| **Status** | Em produção |
| **Rastreia para** | `DCla-Guia-01`, `DSeq-Guia-01`, `DCla-Comum-01` |

## Descrição

Contratos das operações das classes do `DCla-Guia-01`. `ConfiguracaoGuia` só tem constantes, sem operações. As operações de `ILinkExterno` têm contrato no pacote Comum (D-IND-08).

### Classe ConfiguracaoGuia

*Invariantes:* `urlGuia` é uma URL absoluta, não vazia; `tipoMime` é sempre `application/pdf`.

### Classe ControladorGuia

*Invariantes:* o controlador sempre tem uma referência a `ILinkExterno`.

**Tabela 1 – Contratos de ControladorGuia**

| Operação | Pré-condição | Pós-condição | Erros |
|---|---|---|---|
| `abrirGuia()` | O usuário tocou no cartão "Guia Estudantil" na tela inicial | `linkExterno.abrirDocumento(ConfiguracaoGuia.urlGuia, ConfiguracaoGuia.tipoMime)` foi chamado uma vez e o resultado é descartado; o app continua na tela inicial | – (falhas de abertura são tratadas pelo Android e não retornam ao app) |

### Regras E-C-A

O Guia não tem regras E-C-A: não há dados remotos, recarga nem mudança de estado do app em reação a eventos. Por isso não há item `ECA-Guia-nn`.

## Referências

ANTHROPIC. **Claude Code**. Assistente de IA. Disponível em: https://claude.com/claude-code. Acesso em: 20 out. 2026.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
