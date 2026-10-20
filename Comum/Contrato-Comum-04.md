# Contrato-Comum-04 – Contratos do componente ProvedorMapa

| Campo | Valor |
|---|---|
| **Código** | `Contrato-Comum-04` |
| **Título** | Contratos do componente ProvedorMapa |
| **Autor(a)** | Pessoa D |
| **Revisor(a)** | Pessoa C |
| **Status** | Em produção |
| **Rastreia para** | `DCla-Comum-04`, `DCmp-Comum-01`, `DImp-Geral-01` |

## Descrição

Contratos das operações de `AdaptadorProvedorMapa` e `AdaptadorGps` (`DCla-Comum-04`). O componente é usado só pelo pacote Locais (Pessoa B), que tem contratos próprios para as suas classes.

### Classe AdaptadorProvedorMapa

*Invariantes:* `zoomPadrao` é positivo; os `id` dos marcadores são únicos; no máximo um marcador está destacado.

**Tabela 1 – Contratos de AdaptadorProvedorMapa**

| Operação | Pré-condição | Pós-condição | Erros |
|---|---|---|---|
| `exibirMapa(centro, zoom)` | `centro` não é nulo; `zoom` é positivo | O mapa está visível, centrado em `centro`, com o zoom dado | – |
| `adicionarMarcador(marcador)` | `marcador` não é nulo; nenhum marcador com o mesmo `id` | `marcador` está no mapa, na sua posição e cor | – |
| `destacarMarcador(idMarcador)` | Existe marcador com `idMarcador` | Esse marcador está destacado e os demais não; o mapa está centrado nele | – |
| `centralizarEm(posicao)` | `posicao` não é nula | O mapa está centrado em `posicao`; os marcadores não mudam | – |
| `limparMarcadores()` | – | Não há marcadores no mapa | – |

### Classe AdaptadorGps

**Tabela 2 – Contratos de AdaptadorGps**

| Operação | Pré-condição | Pós-condição | Erros |
|---|---|---|---|
| `permissaoConcedida()` | – | Devolve verdadeiro se o app tem permissão de localização; o estado não muda | – |
| `solicitarPermissao()` | – | O Android pediu a permissão ao usuário, se ela ainda não foi concedida; devolve a resposta | – |
| `obterLocalizacaoAtual()` | `permissaoConcedida()` é verdadeiro | Devolve uma `Coordenada` com a posição atual do aparelho | – |

*Invariante de Coordenada:* `latitude` entre -90 e 90; `longitude` entre -180 e 180.

## Referências

ANTHROPIC. **Claude Code**. Assistente de IA. Disponível em: https://claude.com/claude-code. Acesso em: 20 out. 2026.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
