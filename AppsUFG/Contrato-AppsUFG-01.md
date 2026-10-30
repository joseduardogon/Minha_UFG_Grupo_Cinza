# Contrato-AppsUFG-01 – Contratos das operações do pacote Apps UFG

| Campo | Valor |
|---|---|
| **Código** | `Contrato-AppsUFG-01` |
| **Título** | Contratos das operações do pacote Apps UFG |
| **Autor(a)** | Maicon Brendo da Silva |
| **Revisor(a)** | Revisor(a) a definir |
| **Status** | Em produção |
| **Rastreia para** | `DCla-AppsUFG-01`, `DSeq-AppsUFG-01`, `DCla-Comum-01` |

## Descrição

Especificação formal dos contratos de operação das classes do pacote `AppsUFG` (`DCla-AppsUFG-01`), definindo suas pré-condições, pós-condições e tratamento de falhas.

### Classe AplicativoUFG

*Invariantes de classe:*
- Os atributos `id`, `nome` e `idPacote` são imutáveis e não nulos.
- A lista estática de aplicativos possui cardinalidade fixa igual a 3.

**Contratos de AplicativoUFG**

| Operação | Pré-condição | Pós-condição | Erros / Exceções |
|---|---|---|---|
| `obterTodos(): List<AplicativoUFG>` | Nenhuma | Retorna a lista contendo as 3 instâncias pré-definidas (`RU_UFG`, `INVENTARIO_PATRIMONIAL` e `CS_CANDIDATO`) | N/A |

---

### Classe ControladorAppsUFG

*Invariantes de classe:*
- O controlador mantém referência não nula para a interface `ILinkExterno`.

**Contratos de ControladorAppsUFG**

| Operação | Pré-condição | Pós-condição | Erros / Exceções |
|---|---|---|---|
| `obterAplicativos(): List<AplicativoUFG>` | Nenhuma | Delega para `AplicativoUFG.obterTodos()` e retorna a lista para a camada de visualização | N/A |
| `abrirNaLoja(aplicativo: AplicativoUFG): ResultadoAbertura` | O parâmetro `aplicativo` não deve ser nulo e deve conter um `idPacote` válido | `ILinkExterno.abrirLoja(aplicativo.idPacote)` foi invocado exatamente uma vez; o retorno `ResultadoAbertura` é propagado | Retorna `ResultadoAbertura.URL_INVALIDA` se o pacote for malformatado; falhas internas da loja são tratadas pelo Android |

---

### Classe TelaAppsUFG

| Operação | Pré-condição | Pós-condição | Erros / Exceções |
|---|---|---|---|
| `exibirCatalogo(): void` | A tela foi instanciada | Obtém a lista via controlador e renderiza os 3 cartões visuais em tela | N/A |
| `aoTocarAplicativo(aplicativo: AplicativoUFG): void` | Usuário tocou no cartão correspondente | Invoca `controlador.abrirNaLoja(aplicativo)` | N/A |
| `aoTocarVoltar(): void` | Usuário tocou no botão `[<]` da barra superior | Encerra a tela atual e restaura a visualização da tela inicial | N/A |

## Referências

GOOGLE. **Antigravity**. Assistente de IA para Engenharia de Software. Disponível em: https://antigravity.google.com. Acesso em: 29 out. 2026.

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 3 (Software Design). IEEE, 2024.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |

