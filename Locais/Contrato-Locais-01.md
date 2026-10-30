# Contrato-Locais-01 – Contratos das operações do pacote Locais

| Campo | Valor |
|---|---|
| **Código** | `Contrato-Locais-01` |
| **Título** | Contratos das operações do pacote Locais |
| **Autor(a)** | Maicon Brendo da Silva |
| **Revisor(a)** | Revisor(a) a definir |
| **Status** | Em produção |
| **Rastreia para** | `DCla-Locais-01`, `DCla-Locais-02`, `DSeq-Locais-01`, `DSeq-Locais-02`, `DSeq-Locais-03`, `DCla-Comum-03`, `DCla-Comum-04` |

## Descrição

Especificação formal dos contratos de operação das classes da funcionalidade `Locais` (`DCla-Locais-01` e `DCla-Locais-02`), definindo suas pré-condições, pós-condições e tratamento de exceções.

---

### Classe ControladorLocais

*Invariantes de classe:*
- Mantém referência válida e não nula para `IControladorTelaRemota<Local>`.

**Contratos de ControladorLocais**

| Operação | Pré-condição | Pós-condição | Erros / Exceções |
|---|---|---|---|
| `carregarLocais(): void` | O app foi acionado para exibir a tela de locais | Invoca `controladorRemoto.aoEntrarNaTela()`, disparando o ciclo de carregamento | Erros de rede são tratados via `EstadoTela.INDISPONIVEL` |
| `obterLocais(): List<Local>` | O estado da tela é `EstadoTela.EXIBINDO` | Retorna a lista de instâncias de `Local` carregadas da API | Retorna lista vazia se a carga não tiver sido concluída |
| `selecionarLocal(local: Local): void` | O parâmetro `local` não deve ser nulo | `localSelecionado` armazena a referência para o objeto informado | N/A |
| `obterLocalSelecionado(): Local` | Nenhuma | Retorna a referência do local atualmente em foco (ou nulo se nenhum tiver sido tocado) | N/A |

---

### Classe AbaMapaLocais

**Contratos de AbaMapaLocais**

| Operação | Pré-condição | Pós-condição | Erros / Exceções |
|---|---|---|---|
| `focarLocal(local: Local): void` | `local` não é nulo e possui coordenada válida | `provedorMapa.centralizarEm(local.coordenada)` e `provedorMapa.destacarMarcador(local.id)` foram invocados exatamente uma vez | N/A |
| `aoTocarBotaoGps(): void` | A aba do mapa está ativa em primeiro plano | `servicoLocalizacao.solicitarPermissao()` foi invocado; se concedido, `provedorMapa.centralizarEm(posicaoAtual)` é executado; se recusado, o mapa preserva as coordenadas do campus | Falha de hardware ou GPS inativo é tratada pelo diálogo nativo do sistema operacional |

---

### Classe FonteLocais

**Contratos de FonteLocais**

| Operação | Pré-condição | Pós-condição | Erros / Exceções |
|---|---|---|---|
| `carregar(): List<Local>` | Acesso de rede disponível | Executa `acessoApi.obter("/locais", vazio)`; realiza parse do JSON criando instâncias de `Local` ou `UnidadeAcademica` | Lança exceção de rede repassada ao controlador remoto caso o status HTTP seja diferente de 200 |

## Referências

GOOGLE. **Antigravity**. Assistente de IA para Engenharia de Software. Disponível em: https://antigravity.google.com. Acesso em: 30 out. 2026.

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 3 (Software Design). IEEE, 2024.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |

