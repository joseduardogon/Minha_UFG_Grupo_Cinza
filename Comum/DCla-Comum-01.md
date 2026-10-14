# DCla-Comum-01 – Classes do componente LinkExterno

| Campo | Valor |
|---|---|
| **Código** | `DCla-Comum-01` |
| **Título** | Classes do componente LinkExterno |
| **Autor(a)** | Pessoa D |
| **Revisor(a)** | Pessoa C |
| **Status** | Em revisão |
| **Rastreia para** | `DCmp-Comum-01`, `DImp-Geral-01`, `DCdu-Geral-01` |

## Diagrama

![DCla-Comum-01](DCla-Comum-01.png)

Fonte: [`DCla-Comum-01.puml`](DCla-Comum-01.puml)

## Descrição

O componente LinkExterno abre conteúdo fora do app e corresponde ao ator Aplicativo externo do `DCdu-Geral-01`. Cada operação de `ILinkExterno` cobre uma especialização do ator:

| Operação | Ator | Uso no app |
|---|---|---|
| `abrirUrl(url)` | Navegador | Segurança (versão web), Rádio (player), Eventos e Notícias (link do item) |
| `abrirLoja(idPacote)` | Play Store | Segurança, Apps UFG |
| `abrirDocumento(url, tipoMime)` | Visualizador de PDF | Guia Estudantil |

`AberturaLinkExterno` monta uma `Intencao` (ação, dados e tipo MIME), verifica se algum app do aparelho a atende e a dispara. `abrirLoja` tenta primeiro o esquema `market://` (app da Play Store) e, se não houver app compatível, usa o endereço web da loja.

`ResultadoAbertura` informa o resultado à tela que chamou: `ABERTO`, `URL_INVALIDA` ou `SEM_APP_COMPATIVEL`. Na versão atual o app não mostra mensagem quando a abertura falha. A enumeração existe para que o comportamento possa ser especificado nos contratos (D-IND-08).

`Intencao` abstrai o Intent do Android, para que o modelo não dependa da API da plataforma.

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 3 (Software Design). IEEE, 2024.

ANTHROPIC. **Claude**. Assistente de IA. Disponível em: claude.ai. Acesso em: 14 out. 2026. Questão: Apêndice <X>, Seção <X.1>.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
