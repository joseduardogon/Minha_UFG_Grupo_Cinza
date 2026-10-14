# DCla-Comum-02 – Classes do componente AcessoApi

| Campo | Valor |
|---|---|
| **Código** | `DCla-Comum-02` |
| **Título** | Classes do componente AcessoApi |
| **Autor(a)** | Pessoa D |
| **Revisor(a)** | Pessoa C |
| **Status** | Em revisão |
| **Rastreia para** | `DCmp-Comum-01`, `DImp-Geral-01`, `DCla-Comum-03` |

## Diagrama

![DCla-Comum-02](DCla-Comum-02.png)

Fonte: [`DCla-Comum-02.puml`](DCla-Comum-02.puml)

## Descrição

O componente AcessoApi centraliza a comunicação do app com a API Minha UFG (HTTPS/REST, JSON; `DImp-Geral-01`).

- `obter(caminho, parametros)` faz uma consulta (GET). É usada por todas as funcionalidades com conteúdo remoto. Exemplo: `obter("/eventos", {data: "2026-10-07"})`.
- `enviar(caminho, corpo)` envia dados (POST). Na versão atual não há envio; a operação existe para o registro de avaliação (AvalRegistrar).

`RespostaApi` devolve o código de status e o corpo em JSON como texto. A conversão do JSON nas entidades é feita pela funcionalidade, que conhece o formato, e não pelo Comum.

Quando a requisição não pode ser concluída, `ClienteApi` lança `ErroApi` com um `TipoErroApi`:

| Tipo | Situação |
|---|---|
| `SEM_CONEXAO` | Aparelho sem internet (verificado por `haConexao()` antes da requisição) |
| `TEMPO_ESGOTADO` | Sem resposta dentro de `tempoLimiteMs` |
| `ERRO_SERVIDOR` | Status HTTP 5xx |
| `RESPOSTA_INVALIDA` | Status inesperado ou corpo ilegível |

Não há cache: cada chamada vai ao servidor (contexto da equipe, seção 1). O valor de `tempoLimiteMs` (15 s) é uma premissa de projeto, não um dado observado no app.

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 3 (Software Design). IEEE, 2024.

ANTHROPIC. **Claude**. Assistente de IA. Disponível em: claude.ai. Acesso em: 14 out. 2026. Questão: Apêndice <X>, Seção <X.1>.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
