# DImp-Geral-01 – Implantação do sistema Minha UFG

| Campo | Valor |
|---|---|
| **Código** | `DImp-Geral-01` |
| **Título** | Implantação do sistema Minha UFG |
| **Autor(a)** | Pessoa D |
| **Revisor(a)** | Pessoa C |
| **Status** | Em revisão |
| **Rastreia para** | `DCdu-Geral-01`, `DPac-Geral-01`, `DCmp-Comum-01`, `DCla-Comum-01`, `DCla-Comum-02`, `DCla-Comum-04` |

## Diagrama

![DImp-Geral-01](DImp-Geral-01.png)

Fonte: [`DImp-Geral-01.puml`](DImp-Geral-01.puml)

## Descrição

O diagrama mostra os nós físicos e ambientes de execução do sistema Minha UFG e os protocolos entre eles. O escopo do trabalho é o app, mas o painel web e os sistemas externos aparecem porque o app depende deles em execução.

| Nó | Papel | Elementos implantados |
|---|---|---|
| Smartphone (Android) | Executa o app e os aplicativos externos | `minha-ufg.apk`, Navegador, Play Store, Visualizador de PDF |
| Receptor GNSS (GPS) | Fornece a posição do aparelho | — |
| Servidor de aplicação UFG | Expõe o conteúdo e registra avaliações | API Minha UFG |
| Servidor de banco de dados UFG | Persiste os dados do sistema | Base Minha UFG |
| Servidor do painel web UFG | Interface de gestão do conteúdo | Painel web Minha UFG |
| Estação do gestor | Acesso ao painel web | Navegador do gestor |
| Provedor de mapa | Fornece os blocos do mapa do campus | — |
| Google Play | Loja de aplicativos | — |
| Sites da UFG | Portal de notícias e eventos, streaming da Rádio UFG, sistema web de segurança | — |

**Comunicação.**

| Origem → destino | Protocolo | Uso |
|---|---|---|
| App → API Minha UFG | HTTPS / REST (JSON) | Todo conteúdo remoto e o registro de avaliações; componente AcessoApi (`DCla-Comum-02`) |
| App → Provedor de mapa | HTTPS | Blocos do mapa; componente ProvedorMapa (`DCla-Comum-04`) |
| App → Receptor GNSS | Android Location API | Localização atual; componente ProvedorMapa |
| App → Navegador, Play Store, Visualizador de PDF | Intent Android | Redirecionamentos; componente LinkExterno (`DCla-Comum-01`) |
| Navegador → Sites da UFG | HTTPS | Páginas abertas a partir do app |
| Play Store → Google Play | HTTPS | Página do app na loja |
| Painel web → API | HTTPS / REST (JSON) | Cadastro de conteúdo |
| API → Base | TCP/IP (SQL) | Persistência |
| Navegador do gestor → Painel web | HTTPS | Uso do painel |

**Premissas da engenharia reversa.** A tecnologia do servidor, do SGBD e do provedor de mapa não é visível no app; os nós são nomeados pelo papel, não pelo produto. Supõe-se que o painel web grava por meio da mesma API, e não diretamente na base. Supõe-se que o `guiaestudantil.pdf` é obtido por HTTPS e entregue ao Visualizador de PDF por Intent; se estiver embutido no `.apk`, o diagrama não muda.

O Painel web aparece só neste diagrama, e não nos DCdu, pois não interage com o app (contrato-base.md, seção 5).

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 3 (Software Design). IEEE, 2024.

INTERNATIONAL ORGANIZATION FOR STANDARDIZATION; INTERNATIONAL ELECTROTECHNICAL COMMISSION; INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **ISO/IEC/IEEE 12207:2026**: Systems and software engineering – Software life cycle processes. Cláusula 6.4.5 (Design Definition Process). 2026.

ANTHROPIC. **Claude**. Assistente de IA. Disponível em: claude.ai. Acesso em: 14 out. 2026. Questão: Apêndice <X>, Seção <X.1>.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
