# ECA-Seguranca-01 – Regras E-C-A de Segurança

| Campo | Valor |
|---|---|
| **Código** | `ECA-Seguranca-01` |
| **Título** | Regras E-C-A de Segurança |
| **Autor(a)** | Maicon Brendo da Silva |
| **Revisor(a)** | Revisor(a) a definir |
| **Status** | Em produção |
| **Rastreia para** | `DCla-Seguranca-01`, `DEst-Seguranca-01`, `Contrato-Seguranca-01` |

## Descrição

Especificação das regras ativas do tipo Evento-Condição-Ação (E-C-A) que determinam as respostas automáticas da interface `TelaSeguranca`, correspondendo formalmente às transições mapeadas no `DEst-Seguranca-01`.

### Regras E-C-A de Segurança

| Código | Evento | Condição | Ação | Classe Alvo |
|---|---|---|---|---|
| **ECA-SG-01** | Toque do usuário no cartão "Acessar Versao Web" (`E2`) | A tela de Segurança está ativa | Invocar `ControladorSeguranca.abrirVersaoWeb()` e transferir foco ao navegador | `TelaSeguranca` |
| **ECA-SG-02** | Toque do usuário no cartão "Baixar na Play Store (Android)" (`E3`) | A tela de Segurança está ativa | Invocar `ControladorSeguranca.abrirPlayStore()` e transferir foco à loja de aplicativos | `TelaSeguranca` |
| **ECA-SG-03** | Retorno ao app Minha UFG a partir do navegador ou da Play Store | A tela `TelaSeguranca` continua ativa na pilha | Restaurar a interface visual mantendo os dois cartões prontos para nova seleção | `TelaSeguranca` |
| **ECA-SG-04** | Toque do usuário no botão de retorno `[<]` na barra superior (`E1`) | A tela de Segurança está ativa | Encerrar a exibição da tela e restaurar a tela inicial | `TelaSeguranca` |

## Referências

GOOGLE. **Antigravity**. Assistente de IA para Engenharia de Software. Disponível em: https://antigravity.google.com. Acesso em: 29 out. 2026.

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 11 (Software Engineering Models and Methods). IEEE, 2024.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |

