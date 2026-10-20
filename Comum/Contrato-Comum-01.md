# Contrato-Comum-01 – Contratos do componente LinkExterno

| Campo | Valor |
|---|---|
| **Código** | `Contrato-Comum-01` |
| **Título** | Contratos do componente LinkExterno |
| **Autor(a)** | Pessoa D |
| **Revisor(a)** | Pessoa C |
| **Status** | Em produção |
| **Rastreia para** | `DCla-Comum-01`, `DCmp-Comum-01`, `ECA-Comum-01`, `DSeq-Guia-01`, `DSeq-Radio-03` |

## Descrição

Contratos das operações de `ILinkExterno` e `AberturaLinkExterno` (`DCla-Comum-01`). Nenhuma operação lança exceção: o resultado é sempre informado por `ResultadoAbertura`, e a tela que chama decide se o usa. Na versão atual, todas as telas descartam o resultado.

### Classe AberturaLinkExterno

*Invariantes:* `prefixoLoja` é `market://details?id=`; `prefixoLojaWeb` é `https://play.google.com/store/apps/details?id=`.

**Tabela 1 – Contratos de AberturaLinkExterno**

| Operação | Pré-condição | Pós-condição | Erros |
|---|---|---|---|
| `abrirUrl(url)` | – | Se `urlValida(url)` e existe app compatível, uma `Intencao` de visualização com `dados = url` foi disparada e devolve `ABERTO`; se a URL é inválida, devolve `URL_INVALIDA` e nada é disparado; se não há app compatível, devolve `SEM_APP_COMPATIVEL` | – |
| `abrirLoja(idPacote)` | `idPacote` não é vazio | Dispara `prefixoLoja + idPacote` se há app da Play Store; senão dispara `prefixoLojaWeb + idPacote` no navegador (`ECA-CM-05`); devolve `ABERTO`, ou `SEM_APP_COMPATIVEL` se nenhuma das duas pôde ser aberta | – |
| `abrirDocumento(url, tipoMime)` | `tipoMime` não é vazio | Se `urlValida(url)`, uma `Intencao` de visualização com `dados = url` e `tipoMime` foi disparada e o Android exibe o seletor de apps; devolve `ABERTO`, `URL_INVALIDA` ou `SEM_APP_COMPATIVEL`, como em `abrirUrl`. Falhas do app escolhido (ex.: formato incompatível) não retornam ao app | – |
| `urlValida(url)` (privada) | – | Devolve verdadeiro se `url` não é vazia e é absoluta, com esquema `http` ou `https`; o estado não muda | – |
| `existeAppCompativel(intencao)` (privada) | `intencao` não é nula | Devolve verdadeiro se algum app do aparelho atende a `intencao`; o estado não muda | – |
| `disparar(intencao)` (privada) | `existeAppCompativel(intencao)` é verdadeiro | A `intencao` foi entregue ao Android uma vez; o app sai do primeiro plano | – |

## Referências

ANTHROPIC. **Claude Code**. Assistente de IA. Disponível em: https://claude.com/claude-code. Acesso em: 20 out. 2026.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
