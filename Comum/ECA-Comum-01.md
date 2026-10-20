# ECA-Comum-01 – Regras E-C-A do pacote Comum

| Campo | Valor |
|---|---|
| **Código** | `ECA-Comum-01` |
| **Título** | Regras E-C-A do pacote Comum |
| **Autor(a)** | Pessoa D |
| **Revisor(a)** | Pessoa C |
| **Status** | Em produção |
| **Rastreia para** | `DCla-Comum-01`, `DCla-Comum-02`, `DCla-Comum-03`, `DEst-Comum-01`, `Contrato-Comum-01`, `Contrato-Comum-02`, `Contrato-Comum-03` |

## Descrição

Regras ativas do comportamento global do app (sem cache, recarga ao entrar na tela, estados vazio e indisponível), válidas para todas as telas com conteúdo remoto. As regras de cada funcionalidade (ex.: `ECA-Radio-01`, `ECA-Eventos-01`) só especializam estas.

**Tabela 1 – Regras E-C-A do Comum**

| Código | Evento | Condição | Ação | Classe |
|---|---|---|---|---|
| ECA-CM-01 | Uma tela com conteúdo remoto é exibida (primeira entrada ou retorno de outra tela ou de app externo) | Sempre (o app não guarda cache) | Chama `aoEntrarNaTela()`: vai a Carregando e carrega os dados de novo | `ControladorTelaRemota` |
| ECA-CM-02 | A carga termina com `ErroApi` | Qualquer tipo (inclusive `SEM_CONEXAO`) | Descarta os dados e vai ao estado Indisponível | `ControladorTelaRemota` |
| ECA-CM-03 | A carga termina com sucesso | A lista recebida é vazia | Vai ao estado Vazio | `ControladorTelaRemota` |
| ECA-CM-04 | Uma requisição à API é iniciada | `haConexao()` é falso | Não envia a requisição e lança `ErroApi` `SEM_CONEXAO` | `ClienteApi` |
| ECA-CM-05 | Pedido de abertura da Play Store | Não há app da Play Store no aparelho | Abre o endereço web da loja no navegador | `AberturaLinkExterno` |

As regras ECA-CM-01 a ECA-CM-03 correspondem às transições do `DEst-Comum-01`.

## Referências

ANTHROPIC. **Claude Code**. Assistente de IA. Disponível em: https://claude.com/claude-code. Acesso em: 20 out. 2026.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
