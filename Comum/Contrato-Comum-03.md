# Contrato-Comum-03 – Contratos do componente EstadosTelaRemota

| Campo | Valor |
|---|---|
| **Código** | `Contrato-Comum-03` |
| **Título** | Contratos do componente EstadosTelaRemota |
| **Autor(a)** | Pessoa D |
| **Revisor(a)** | Pessoa C |
| **Status** | Em produção |
| **Rastreia para** | `DCla-Comum-03`, `DEst-Comum-01`, `ECA-Comum-01`, `Contrato-Radio-01`, `Contrato-Eventos-01` |

## Descrição

Contratos das operações de `ControladorTelaRemota<T>` (`DCla-Comum-03`). As operações de `IFonteDados<T>` e `IObservadorEstado` são implementadas pelas funcionalidades e têm contrato nos seus pacotes (ex.: `FonteProgramacaoRadio.carregar()` em `Contrato-Radio-01`).

### Classe ControladorTelaRemota&lt;T&gt;

*Invariantes:* `fonte` nunca é nula; `estadoAtual` é sempre um valor de `EstadoTela`; `dados` só tem itens quando `estadoAtual` é `EXIBINDO`.

**Tabela 1 – Contratos de ControladorTelaRemota**

| Operação | Pré-condição | Pós-condição | Erros |
|---|---|---|---|
| `ControladorTelaRemota(fonte)` | `fonte` não é nula | `estadoAtual` é `CARREGANDO`; `dados` é vazia; nenhum observador; `fonte.carregar()` não foi chamado | – |
| `aoEntrarNaTela()` | – | Mesmo efeito de `recarregar()`; é chamado a cada exibição da tela (`ECA-CM-01`) | – |
| `recarregar()` | – | Passou por `CARREGANDO` e chamou `fonte.carregar()` uma vez. Se a lista tem itens, `dados` é a lista e o estado é `EXIBINDO`; se é vazia, `dados` é vazia e o estado é `VAZIO` (`ECA-CM-03`); se houve `ErroApi`, `dados` é vazia e o estado é `INDISPONIVEL` (`ECA-CM-02`). Cada mudança foi notificada | – (o `ErroApi` é tratado aqui e não é repassado à tela) |
| `obterEstado()` | – | Devolve `estadoAtual`; o estado não muda | – |
| `obterDados()` | – | Devolve `dados`; o estado não muda | – |
| `registrarObservador(o)` | `o` não é nulo | `o` está entre os observadores, uma única vez | – |
| `definirEstado(novo)` (privada) | – | `estadoAtual` é `novo`; `notificar()` foi chamado | – |
| `notificar()` (privada) | – | `aoMudarEstado(estadoAtual)` foi chamado uma vez em cada observador | – |

## Referências

ANTHROPIC. **Claude Code**. Assistente de IA. Disponível em: https://claude.com/claude-code. Acesso em: 20 out. 2026.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
