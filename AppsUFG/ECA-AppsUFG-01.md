# ECA-AppsUFG-01 – Regras E-C-A de Apps UFG

| Campo | Valor |
|---|---|
| **Código** | `ECA-AppsUFG-01` |
| **Título** | Regras E-C-A de Apps UFG |
| **Autor(a)** | Maicon Brendo da Silva |
| **Revisor(a)** | Revisor(a) a definir |
| **Status** | Em produção |
| **Rastreia para** | `DCla-AppsUFG-01`, `DEst-AppsUFG-01`, `Contrato-AppsUFG-01` |

## Descrição

Especificação das regras ativas do tipo Evento-Condição-Ação (E-C-A) que regem o comportamento da interface `TelaAppsUFG`, correspondendo formalmente às transições mapeadas no `DEst-AppsUFG-01`.

### Regras E-C-A de Apps UFG

| Código | Evento | Condição | Ação | Classe Alvo |
|---|---|---|---|---|
| **ECA-AU-01** | Toque do usuário em qualquer ponto de um cartão de aplicativo (`E2`, `E3` ou `E4`) | A tela está no estado "Exibindo catálogo" | Invocar `ControladorAppsUFG.abrirNaLoja(app)` e delegar abertura ao componente `ILinkExterno` | `TelaAppsUFG` |
| **ECA-AU-02** | Retorno ao app Minha UFG a partir do aplicativo da Play Store | A tela `TelaAppsUFG` continua ativa na pilha de navegação | Restaurar a interface visual mantendo a lista fixa exibida, sem necessidade de recarga remota | `TelaAppsUFG` |
| **ECA-AU-03** | Toque do usuário no botão de retorno `[<]` na barra superior (`E1`) | A tela está ativa | Encerra a visualização do catálogo e restaura o estado da tela inicial | `TelaAppsUFG` |

## Referências

GOOGLE. **Antigravity**. Assistente de IA para Engenharia de Software. Disponível em: https://antigravity.google.com. Acesso em: 29 out. 2026.

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 11 (Software Engineering Models and Methods). IEEE, 2024.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |

