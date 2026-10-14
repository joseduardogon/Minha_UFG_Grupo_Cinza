# DCdu-Geral-01 – Casos de uso gerais do app Minha UFG

| Campo | Valor |
|---|---|
| **Código** | `DCdu-Geral-01` |
| **Título** | Casos de uso gerais do app Minha UFG |
| **Autor(a)** | Pessoa D |
| **Revisor(a)** | Pessoa C |
| **Status** | Em produção (rascunho; versão final no D-INT-03) |
| **Rastreia para** | `DCdu-Seguranca-01`, `DCdu-Radio-01`, `DCdu-Guia-01`, `DCdu-Eventos-01`, `DCdu-Noticias-01`, `DCdu-RU-01`, `DCdu-Locais-01`, `DCdu-AppsUFG-01`, `DCdu-AvalRegistrar-01`, `DCdu-AvalConsultar-01`, `DImp-Geral-01`, `DPac-Geral-01` |

## Diagrama

![DCdu-Geral-01](DCdu-Geral-01.png)

Fonte: [`DCdu-Geral-01.puml`](DCdu-Geral-01.puml)

## Descrição

O diagrama apresenta um caso de uso macro por funcionalidade do app: as oito da versão atual (v3.1.1), obtidas por engenharia reversa, e as duas da evolução (Avaliar UA e Consultar notas de avaliação). Cada macro é detalhado pelo dono da funcionalidade no respectivo `DCdu-<Funcionalidade>-01`, com quantos casos de uso forem necessários.

**Atores primários.** O Membro da comunidade UFG usa o app de forma anônima, sem login. O Avaliador é uma especialização do Membro: é o membro que registra uma avaliação de UA, também anônimo. Consultar notas fica com o Membro, pois qualquer usuário pode vê-las.

**Atores secundários.** São sistemas com que o app interage:

| Ator | Papel | Casos de uso |
|---|---|---|
| Servidor/API | Fornece o conteúdo remoto e registra avaliações | Rádio, Eventos, Notícias, RU, Locais, Avaliar UA, Consultar notas |
| Provedor de mapa / GPS | Exibe o mapa do campus e a localização atual | Localizar locais |
| Aplicativo externo (Navegador) | Abre páginas fora do app | Segurança (versão web), Rádio (player), Eventos, Notícias |
| Aplicativo externo (Play Store) | Abre a página de um app na loja | Segurança, Apps UFG |
| Aplicativo externo (Visualizador de PDF) | Abre o guiaestudantil.pdf pelo seletor de apps do Android | Guia estudantil |

O ator abstrato Aplicativo externo agrupa todo redirecionamento para fora do app e corresponde ao componente Abertura de link externo do pacote Comum (`DCmp-Comum-01`).

**Decisões de modelagem.**
- A tela inicial é navegação, não objetivo do usuário; por isso não é caso de uso. Ela é modelada em `DIhc-Inicio-01` e `DEst-Inicio-01`.
- O Painel web não interage com o app: ele alimenta o Servidor/API (cardápio, eventos, notícias, programação, dimensões e questões da avaliação). Por isso aparece só em `DImp-Geral-01`.
- Apps UFG não acessa o Servidor/API, pois a lista é fixa (três apps).

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 11 (Software Engineering Models and Methods). IEEE, 2024.

ANTHROPIC. **Claude**. Assistente de IA. Disponível em: claude.ai. Acesso em: 14 out. 2026. Questão: Apêndice <X>, Seção <X.1>.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
