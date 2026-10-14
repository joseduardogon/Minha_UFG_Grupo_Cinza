# DCmp-Comum-01 – Componentes do pacote Comum

| Campo | Valor |
|---|---|
| **Código** | `DCmp-Comum-01` |
| **Título** | Componentes do pacote Comum |
| **Autor(a)** | Pessoa D |
| **Revisor(a)** | Pessoa C |
| **Status** | Em revisão |
| **Rastreia para** | `DPac-Geral-01`, `DImp-Geral-01`, `DCla-Comum-01`, `DCla-Comum-02`, `DCla-Comum-03`, `DCla-Comum-04`, `DEst-Comum-01` |

## Diagrama

![DCmp-Comum-01](DCmp-Comum-01.png)

Fonte: [`DCmp-Comum-01.puml`](DCmp-Comum-01.puml)

## Descrição

O pacote `Comum` reúne os quatro componentes compartilhados definidos no contrato (seção 9). Eles são modelados uma vez aqui; os demais pacotes só os referenciam, pelas interfaces.

| Componente | Interface oferecida | Usada por | Classes |
|---|---|---|---|
| LinkExterno | `ILinkExterno` | Seguranca, Radio, Guia, Eventos, Noticias, AppsUFG | `DCla-Comum-01` |
| AcessoApi | `IAcessoApi` | Todas as funcionalidades com conteúdo remoto | `DCla-Comum-02` |
| EstadosTelaRemota | `IControladorTelaRemota` | Todas as telas com conteúdo remoto | `DCla-Comum-03` |
| ProvedorMapa | `IProvedorMapa`, `ILocalizacao` | Locais | `DCla-Comum-04` |

**Interface implementada pelas funcionalidades.** `IFonteDados` é definida em `Comum` e implementada por cada funcionalidade. O controlador de estados a usa para pedir a carga dos dados sem conhecer a funcionalidade.

**Dependências.**
- EstadosTelaRemota usa `IAcessoApi` só para reconhecer `ErroApi` e decidir entre os estados vazio e indisponível. Quem faz a requisição é a funcionalidade, dentro de `IFonteDados.carregar()`.
- LinkExterno, AcessoApi e ProvedorMapa usam serviços da plataforma: Intent Android, HTTPS/REST, SDK do provedor de mapa e Android Location API. Eles correspondem às conexões do `DImp-Geral-01`.

**Como as funcionalidades usam o Comum.** Uma tela com conteúdo remoto cria um `ControladorTelaRemota` com a sua implementação de `IFonteDados`. Essa implementação chama `IAcessoApi.obter(...)` e converte o JSON nas suas entidades. A tela observa o estado do controlador (`DEst-Comum-01`) e, quando o usuário toca num item com URL, chama `ILinkExterno`.

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 3 (Software Design). IEEE, 2024.

ANTHROPIC. **Claude**. Assistente de IA. Disponível em: claude.ai. Acesso em: 14 out. 2026. Questão: Apêndice <X>, Seção <X.1>.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
