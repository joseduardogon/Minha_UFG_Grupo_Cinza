# DCla-Comum-03 – Classes do componente EstadosTelaRemota

| Campo | Valor |
|---|---|
| **Código** | `DCla-Comum-03` |
| **Título** | Classes do componente EstadosTelaRemota |
| **Autor(a)** | Pessoa D |
| **Revisor(a)** | Pessoa C |
| **Status** | Em revisão |
| **Rastreia para** | `DCmp-Comum-01`, `DCla-Comum-02`, `DEst-Comum-01` |

## Diagrama

![DCla-Comum-03](DCla-Comum-03.png)

Fonte: [`DCla-Comum-03.puml`](DCla-Comum-03.puml)

## Descrição

O componente EstadosTelaRemota padroniza o comportamento de toda tela que exibe conteúdo remoto: carregando, exibindo, vazio, indisponível e recarregar ao voltar (contrato, seção 9). O ciclo de estados está em `DEst-Comum-01`.

- `IFonteDados<T>` é implementada por cada funcionalidade. `carregar()` busca os dados pela `IAcessoApi` e devolve a lista de entidades do tipo `T` (por exemplo, `List<Evento>`).
- `ControladorTelaRemota<T>` recebe a fonte no construtor, chama `carregar()`, guarda os dados e define o estado:

| Resultado de `carregar()` | Estado |
|---|---|
| Lista com itens | `EXIBINDO` |
| Lista vazia | `VAZIO` |
| `ErroApi` (qualquer tipo) | `INDISPONIVEL` |

- `aoEntrarNaTela()` é chamado sempre que a tela é exibida, inclusive ao voltar de outra tela, e dispara nova carga, porque o app não tem cache.
- `recarregar()` é chamado pela própria tela quando um filtro muda, como a data em Eventos ou o dia no RU. A Rádio não usa `recarregar`: carrega a semana inteira e filtra a aba em memória (`DCla-Radio-01`).
- `IObservadorEstado` é implementada pela tela, que é notificada a cada mudança de estado para atualizar o que mostra.

Na versão atual, sem internet, o app mostra uma tela em branco ou uma mensagem genérica. O modelo separa `VAZIO` de `INDISPONIVEL` porque são situações distintas; cada funcionalidade decide no seu DIhc como apresentar cada uma.

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 3 (Software Design). IEEE, 2024.

ANTHROPIC. **Claude**. Assistente de IA. Disponível em: claude.ai. Acesso em: 14 out. 2026. Questão: Apêndice <X>, Seção <X.1>.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
