# Contrato-Seguranca-01 – Contratos das operações do pacote Seguranca

| Campo | Valor |
|---|---|
| **Código** | `Contrato-Seguranca-01` |
| **Título** | Contratos das operações do pacote Seguranca |
| **Autor(a)** | Maicon Brendo da Silva |
| **Revisor(a)** | Revisor(a) a definir |
| **Status** | Em produção |
| **Rastreia para** | `DCla-Seguranca-01`, `DSeq-Seguranca-01`, `DSeq-Seguranca-02`, `DCla-Comum-01` |

## Descrição

Especificação formal dos contratos de operação das classes do pacote `Seguranca` (`DCla-Seguranca-01`). A classe `ConfiguracaoSeguranca` encapsula unicamente constantes estáticas e não possui operações dinâmicas.

### Classe ConfiguracaoSeguranca

*Invariantes de classe:*
- `urlWeb` é uma URL absoluta válida iniciada por `https://` (`"https://seguranca.web.ufg.br"`).
- `idPacoteApp` é um identificador de pacote Android não vazio (`"br.ufg.cercomp.sistemaseguranca"`).

---

### Classe ControladorSeguranca

*Invariantes de classe:*
- O controlador mantém referência não nula para a interface `ILinkExterno`.

**Contratos de ControladorSeguranca**

| Operação | Pré-condição | Pós-condição | Erros / Exceções |
|---|---|---|---|
| `abrirVersaoWeb(): ResultadoAbertura` | Nenhuma | `ILinkExterno.abrirUrl(ConfiguracaoSeguranca.urlWeb)` foi invocado exatamente uma vez; o retorno de `ResultadoAbertura` é propagado | Retorna `ResultadoAbertura.SEM_APP_COMPATIVEL` se não houver navegador compatível instalado |
| `abrirPlayStore(): ResultadoAbertura` | Nenhuma | `ILinkExterno.abrirLoja(ConfiguracaoSeguranca.idPacoteApp)` foi invocado exatamente uma vez; o retorno de `ResultadoAbertura` é propagado | Retorna `ResultadoAbertura.SEM_APP_COMPATIVEL` se a loja não estiver disponível no dispositivo |

---

### Classe TelaSeguranca

| Operação | Pré-condição | Pós-condição | Erros / Exceções |
|---|---|---|---|
| `exibirTela(): void` | A tela foi instanciada | Os cartões "Acessar Versao Web" e "Baixar na Play Store (Android)" são renderizados | N/A |
| `aoTocarVersaoWeb(): void` | Toque no cartão "Acessar Versao Web" | Invoca `controlador.abrirVersaoWeb()` | N/A |
| `aoTocarPlayStore(): void` | Toque no cartão "Baixar na Play Store" | Invoca `controlador.abrirPlayStore()` | N/A |
| `aoTocarVoltar(): void` | Toque no botão `[<]` na barra superior | Encerra a visualização de Segurança e restaura a tela inicial | N/A |

## Referências

GOOGLE. **Antigravity**. Assistente de IA para Engenharia de Software. Disponível em: https://antigravity.google.com. Acesso em: 29 out. 2026.

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 3 (Software Design). IEEE, 2024.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |

