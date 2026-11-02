# REV-PR10 – Revisão de Eventos, Notícias e RU

- **PR:** #10 "Complete documentation for Events, News, and RU" (branch `ultima_entrega(c)`, commit `c5baf2d`)
- **Autor:** Pessoa C
- **Revisor:** Pessoa D
- **Data:** 31/10/2026
- **Tarefa:** D-REV-02

## 1. Resumo

Os 47 `.puml` compilam sem erro, os nomes de arquivo batem com o `@startuml` e não há
`skinparam` de cor. A cascata está completa nas três funcionalidades: DCdu, DAtv por caso
de uso, DIhc, DD, DCmp, DCla, DSeq, DEst por DIhc, contratos de todas as operações e ECA.
Os nomes entre DCla, DSeq, DEst e contratos estão consistentes, e o Comum é usado com as
mesmas assinaturas, sem classe duplicada.

Restam 7 problemas de consistência e de semântica (seção 2) que precisam de correção antes
do merge.

**Parecer: pedir mudanças.**

## 2. Bloqueantes

| # | Local | Problema | Correção |
|---|---|---|---|
| B1 | `Eventos/DCla-Eventos-01.puml:22-25`, `Eventos/DCla-Eventos-02.puml:12`, `Noticias/DCla-Noticias-01.puml:22-25`, `Noticias/DCla-Noticias-02.puml:12` | `class Regional <<Comum (proposta)>>` é declarada com atributos dentro do `package "Comum"`. O Comum não define Regional, então isso redefine um pacote alheio. | Desenhar `Regional` fora do pacote Comum, sem atributos, como entidade do `DD-Eventos-01`. A localização definitiva será decidida na integração. |
| B2 | `Eventos/DCla-Eventos-02.puml:36,44`, `Noticias/DCla-Noticias-02.puml:34,41`, `Noticias/DD-Noticias-01.md`, `Integracao/entidades/Entidade-Campus.md:22`, `Entidade-Noticia.md:24`, `Entidade-Regional.md:53-63` | O atributo `idRegional: Integer` aparece junto da associação com `Regional`, o que é redundante (critério 4.2). O próprio `DD-RU-01` diz que "as chaves estrangeiras não são atributos". | Retirar `idRegional` e manter só a associação. |
| B3 | `RU/DCla-RU-02.puml:61` e `RU/DD-RU-01.md` contra `RU/Contrato-RU-01.md:98` | A multiplicidade é `Cardapio "1" -- "1..*" Refeicao`, mas o contrato diz que "uma `Refeicao` criada pela fonte não tem `Cardapio` associado" (critério 3.2). | Retirar `Cardapio` do DCla, já que o app não o usa, ou mudar a multiplicidade para `0..1` e alinhar o contrato. |
| B4 | `RU/DD-RU-01.md:16,45`, `Entidade-CategoriaItem.md:13,34`, `Entidade-ItemCardapio.md:36`, `RU/Contrato-RU-01.md:23` (P-RU-6) | Os textos tratam como "possivelmente outras, não vistas" categorias que o contexto da equipe já lista. Almoço e jantar: arroz, feijão, salada, refresco e sobremesa. Café: complemento vegano. | Listar todas as categorias e marcar essa parte da P-RU-6 como confirmada. |
| B5 | `Noticias/DCmp-Noticias-01.md:20` contra `Noticias/DCla-Noticias-01.puml:64` | O DCmp diz que o pacote depende do Comum "apenas por interfaces", mas `TelaNoticias ..> Controlador : <<create>>` depende da classe concreta. Faltam também `IObservadorEstado` (oferecida) e `IFonteDados` no DCmp. | Ajustar a frase e acrescentar as interfaces no DCmp. |
| B6 | `Noticias/DCla-Noticias-01.puml:66` | A associação `Controlador --> "0..*" IObservadorEstado` tem como rótulo uma operação (`registrarObservador(tela)`). Ela já existe no Comum com o papel `observadores`. | Retirar a linha, ou usar `: observadores`. |
| B7 | `Noticias/DSeq-Noticias-03.puml:14-15` | `L -> N : disparar(intencao)` envia ao Navegador uma operação privada de `AberturaLinkExterno`, e `N --> M` é um retorno para quem não fez a chamada. | Usar `L -> L : disparar(intencao)` e `L -> N : abre url`, e trocar o retorno por uma mensagem. |

## 3. Observações (não dependem de C)

- **Referências a itens que ainda não estão na `main`.** `Contrato-Comum-01` a `04`,
  `ECA-Comum-01`, `DIhc-Inicio-01`, `DEst-Inicio-01`, `DCdu-Radio-01`, `DD-Radio-01` e
  `ECA-Radio-01` existem na branch `d/D-IND-producao-individual` e passam a valer com o
  merge dela. `DD-Geral-01` e `DDados-Geral-01` virão na integração (D-INT-02). Nenhuma
  correção é necessária no PR.
- **Reutilização de `DiaSemana` da Rádio no RU** (`RU/DD-RU-01.md:18`) e **local de
  `Regional` e `Campus`** (`Entidade-Regional.md:39`): ficam registrados para a integração
  (D-INT-01 e D-INT-03).
- **Marcador "Questão: Apêndice <X>, Seção <X.1>"** nas referências: é o formato atual da
  equipe e será preenchido na editoração.

## 4. Verificações sem problema

- Os nomes entre DCla, DSeq, DEst e contratos batem nas três funcionalidades.
- Os eventos E0 a E6 de Eventos coincidem entre DIhc, DEst, DAtv e DSeq.
- O Comum (`IAcessoApi`, `IFonteDados`, `IControladorTelaRemota`, `ClienteApi`,
  `AberturaLinkExterno`) é usado com as assinaturas corretas.
- O comportamento global está respeitado: sem login, sem cache, recarga ao entrar e ao
  voltar, e estados vazio e indisponível.
- Em todos os itens, o autor é C e o revisor é D.
