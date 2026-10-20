# Contrato-Comum-02 – Contratos do componente AcessoApi

| Campo | Valor |
|---|---|
| **Código** | `Contrato-Comum-02` |
| **Título** | Contratos do componente AcessoApi |
| **Autor(a)** | Pessoa D |
| **Revisor(a)** | Pessoa C |
| **Status** | Em produção |
| **Rastreia para** | `DCla-Comum-02`, `DCmp-Comum-01`, `DImp-Geral-01`, `ECA-Comum-01`, `DSeq-Radio-01`, `DSeq-Eventos-01` |

## Descrição

Contratos das operações de `IAcessoApi`, `ClienteApi` e `RespostaApi` (`DCla-Comum-02`). Os erros são `ErroApi`, com o `TipoErroApi` indicado.

### Classe ClienteApi

*Invariantes:* `urlBase` é uma URL HTTPS absoluta, não vazia; `tempoLimiteMs` é positivo (15000, premissa de projeto).

**Tabela 1 – Contratos de ClienteApi**

| Operação | Pré-condição | Pós-condição | Erros |
|---|---|---|---|
| `obter(caminho, parametros)` | `caminho` começa com `/`; `parametros` não é nulo (pode ser vazio) | Uma requisição GET foi feita a `montarUrl(caminho, parametros)`; devolve `RespostaApi` com status 2xx e o corpo recebido. Nada é guardado em cache | `SEM_CONEXAO` se `haConexao()` é falso (nenhuma requisição é feita); `TEMPO_ESGOTADO` sem resposta em `tempoLimiteMs`; `ERRO_SERVIDOR` com status 5xx; `RESPOSTA_INVALIDA` com outro status fora de 2xx ou corpo ilegível |
| `enviar(caminho, corpo)` | `caminho` começa com `/`; `corpo` é JSON não vazio | Uma requisição POST foi feita a `urlBase + caminho` com `corpo`; devolve `RespostaApi` com status 2xx. Só é usada por AvalRegistrar | Os mesmos de `obter` |
| `haConexao()` (privada) | – | Devolve verdadeiro se o aparelho tem rede disponível; o estado não muda | – |
| `montarUrl(caminho, parametros)` (privada) | Como em `obter` | Devolve `urlBase + caminho`, seguido dos parâmetros em query string codificada, se houver | – |

### Classe RespostaApi

*Invariante:* `codigoStatus` está entre 100 e 599.

| Operação | Pré-condição | Pós-condição | Erros |
|---|---|---|---|
| `bemSucedida()` | – | Devolve verdadeiro se `codigoStatus` está entre 200 e 299 | – |

## Referências

ANTHROPIC. **Claude Code**. Assistente de IA. Disponível em: https://claude.com/claude-code. Acesso em: 20 out. 2026.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
