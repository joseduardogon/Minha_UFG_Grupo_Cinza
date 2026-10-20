# DEst-Comum-01 – Estados genéricos de tela com conteúdo remoto

| Campo | Valor |
|---|---|
| **Código** | `DEst-Comum-01` |
| **Título** | Estados genéricos de tela com conteúdo remoto |
| **Autor(a)** | Pessoa D |
| **Revisor(a)** | Pessoa C |
| **Status** | Em revisão |
| **Rastreia para** | `DCla-Comum-03`, `DCmp-Comum-01` |

## Diagrama

![DEst-Comum-01](DEst-Comum-01.png)

Fonte: [`DEst-Comum-01.puml`](DEst-Comum-01.puml)

## Descrição

O diagrama especifica o ciclo de vida de toda tela com conteúdo remoto, implementado por `ControladorTelaRemota` (`DCla-Comum-03`). Os DEst de cada funcionalidade referenciam este diagrama em vez de repetir esses estados.

| Estado | Ação de entrada | Sai por |
|---|---|---|
| Carregando | `fonte.carregar()` | Fim da carga ou `ErroApi` |
| Exibindo | Exibe os dados | `recarregar`, `aoEntrarNaTela` ou sair da tela |
| Vazio | Exibe mensagem de vazio (ex.: "sem eventos") | Idem |
| Indisponível | Exibe mensagem de indisponibilidade | Idem |

**Eventos.**
- `aoEntrarNaTela`: a tela foi exibida, seja na primeira entrada, seja ao voltar de outra tela ou de um aplicativo externo. Sempre leva a Carregando, pois o app não guarda cache. É assim que se realiza o "recarregar ao voltar" do contrato.
- `recarregar`: a tela pediu nova carga por mudança de filtro (data, dia).
- `ErroApi`: falha na comunicação com a API, de qualquer tipo (`DCla-Comum-02`).
- `sair da tela`: o usuário volta ao menu ou sai do app; o controlador é descartado.

A versão atual não tem botão de "tentar novamente". De Indisponível, o usuário só sai por `recarregar` (trocar o filtro) ou saindo e voltando à tela.

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 3 (Software Design). IEEE, 2024.

ANTHROPIC. **Claude**. Assistente de IA. Disponível em: claude.ai. Acesso em: 14 out. 2026. Questão: Apêndice <X>, Seção <X.1>.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
