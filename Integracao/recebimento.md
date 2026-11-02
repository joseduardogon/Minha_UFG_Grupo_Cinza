# Recebimento e validação das entidades (D-INT-01)

| Campo | Valor |
|---|---|
| **Tarefa** | `D-INT-01` – Receber e validar as entidades |
| **Responsável** | Pessoa D (integração) |
| **Data** | 02/11/2026 |
| **Base** | `main` sincronizada com a branch `d/D-IND-producao-individual` em 02/11/2026 |
| **Critérios** | Contrato-base, seção 7 (donos e formato de entrega) e seção 8 (avaliação); Apêndice B, critérios 4.1 e 4.2 |

Material de trabalho da integração: não entra no PDF como item de informação. As correções são feitas pela Pessoa D na D-INT-08 (seção 4).

## 1. Checklist de recebimento

Formato exigido (contrato, seção 7): entrada de DD com nome, atributos, tipos e descrição, mais trecho PlantUML.

| Pacote | Dono | Entrega | Formato | Dono correto | Situação |
|---|---|---|---|---|---|
| Eventos | C | `DD-Eventos-01` + fichas `Entidade-Regional`, `Entidade-Campus`, `Entidade-Evento` | OK | OK | Aceita, com pendências I-04 e I-05 |
| Notícias | C | `DD-Noticias-01` + ficha `Entidade-Noticia` | OK; trecho PlantUML sem `[0..1]` nos opcionais (I-10) | OK | Aceita, com ajuste de forma |
| RU | C | `DD-RU-01` + fichas `Entidade-Cardapio`, `Entidade-Refeicao`, `Entidade-ItemCardapio`, `Entidade-CategoriaItem` | OK | OK | Aceita, com decisões I-06 e I-07 |
| AvalRegistrar | C | `DD-AvalRegistrar-01` (sem fichas em `entidades/`) | OK | OK; `UnidadeAcademica` só referenciada | Aceita, com pendências I-03 e I-11 |
| Locais | B | `DD-Locais-01` (sem fichas em `entidades/`) | OK | **Não**: redefine `Campus` como atributo (I-01) | **A corrigir** (I-01, I-02) |
| Segurança | B | Nenhuma entrada de DD | – | – | **A corrigir** (I-09) |
| Apps UFG | B | Nenhuma entrada de DD | – | – | **A corrigir** (I-08) |
| Rádio | D | `DD-Radio-01` | OK | OK | Aceita |
| Guia | D | `DD-Guia-01` (declara que não há entidade) | OK | OK | Aceita |
| AvalConsultar | D | `DD-AvalConsultar-01` | OK | OK; entidades de B e C só referenciadas | Aceita, depende de I-02 |
| Comum | D | `Coordenada` (`DCla-Comum-04`) | – | OK | Aceita; usada por `Local` sem redefinição |

## 2. Verificações obrigatórias

| Verificação | Resultado |
|---|---|
| `UnidadeAcademica` herda de `Local` | **OK**: `Local <|-- UnidadeAcademica` em `DD-Locais-01` e `DCla-Locais-02`. |
| Regional e Campus definidas só por C | **Falha**: `Local.campus: String` em `DD-Locais-01` (I-01). |
| Local, UA e Área CNPq definidas só por B | **Parcial**: Local e UA OK; Área CNPq não existe como entidade (I-02). |
| Usuário/Avaliador definido por C | **Conflito com o contrato**: C não modela avaliador (I-03). |
| Regras da avaliação (anônima, várias por UA, sem edição nem exclusão, notas de 0 a 5) | **OK** em `DD-AvalRegistrar-01`. |
| Entidades de outro dono só referenciadas | OK em Eventos, Notícias, AvalRegistrar e AvalConsultar; falha em Locais (I-01). |

## 3. Conflitos e inconsistências

| Código | Tipo | Onde | Descrição | Encaminhamento |
|---|---|---|---|---|
| I-01 | Entidade redefinida | `DD-Locais-01`, `DCla-Locais-02` (B) | `Local.campus` é `String` (fixo em "Campus Samambaia"), mas `Campus` é entidade de C (`DD-Eventos-01`). C propõe a associação `Campus 1 — 0..* Local`, marcada "a confirmar com a Pessoa B". | Corrigir: trocar o atributo pela associação com `Campus` e confirmar a multiplicidade. |
| I-02 | Entidade ausente | `DD-Locais-01` (B) | O contrato (seção 7) dá a B a entidade Área de conhecimento (CNPq), mas ela aparece só como `UnidadeAcademica.areaConhecimento: String`. Afeta `MediaArea.areaConhecimento` (`DD-AvalConsultar-01`). | Corrigir: criar `AreaConhecimento` e a associação `UnidadeAcademica 0..* — 1 AreaConhecimento`. D depois troca o atributo de `MediaArea` pela associação. |
| I-03 | Conflito entre fontes | Contrato, seção 7 × `DD-AvalRegistrar-01` (C) | O contrato lista "Usuário / identificação do avaliador" como entidade de C; C registra que não há avaliador em nenhuma entidade (P-AR-7), coerente com o anonimato (contrato, seção 8). | Decisão da Pessoa D com C: tirar a linha do contrato ou manter o avaliador só como ator. |
| I-04 | Pacote indefinido | `DD-Eventos-01`, `Entidade-Regional` (C) | C propõe pôr `Regional` e `Campus` no pacote `Comum`, já que Eventos, Notícias e Locais as usam. | Decidir no D-INT-03 (DPac). |
| I-05 | Associação sem dono confirmado | `Campus — Local` | Associação proposta por C entre a entidade dele e a de B. | Fecha com I-01: dono passa a ser B (lado `Local`), com o aceite de C. |
| I-06 | Entidade fora do app | `Cardapio` (C) | Só existe no servidor; o app não a usa. C deixa a retirada a critério da integração. | Decisão da Pessoa D para o DDados e o DD. |
| I-07 | Possível reuso | `Refeicao.data` × `DiaSemana` (`DD-Radio-01`) | RU deriva o dia da semana da data e não cria enumeração; C pergunta se deve reusar `DiaSemana`. | Decisão da Pessoa D. Não há duplicação hoje. |
| I-08 | Entrega ausente | Apps UFG (B) | `AplicativoUFG` (`DCla-AppsUFG-01`) é catálogo fixo no app, com instâncias estáticas, mas não tem entrada de DD dizendo se é entidade ou configuração. | Criar o `DD-AppsUFG-01`, como o `DD-Guia-01`; antes, decidir se é entidade ou configuração. |
| I-09 | Entrega ausente | Segurança (B) | `DCla-Seguranca-01` só tem constantes (`ConfiguracaoSeguranca`); falta a entrada que declara que não há entidade. | Criar o `DD-Seguranca-01`, como o `DD-Guia-01`. |
| I-10 | Forma | `DD-Noticias-01` (C) | A tabela marca `resumo` e `urlImagem` como opcionais, mas o trecho PlantUML não usa `[0..1]`, ao contrário de `DD-Eventos-01`. | Corrigir o trecho PlantUML. |
| I-11 | Tipo | `DD-AvalRegistrar-01` (C) | `Avaliacao.dataHoraRegistro` guarda data e hora, mas o tipo é `Date`. | Trocar o tipo por `DateTime`. |
| I-12 | Forma | `DD-Locais-01` (B) | Revisor "a definir"; sem coluna de obrigatoriedade (as entradas de C têm). | Corrigir (preencher o revisor). Não impede a integração. |

Não foram encontrados nomes divergentes para o mesmo conceito nem atributos duplicados entre pacotes: `Regional` aparece em Eventos e Notícias só como referência; `UnidadeAcademica` e `DimensaoQualidade` aparecem em AvalRegistrar e AvalConsultar só como referência.

## 4. Correções

Por decisão de 02/11/2026, todos os achados são corrigidos pela Pessoa D (D-INT-08), sem repasse aos autores. O autor de cada pacote alterado é avisado.

| Código | Situação |
|---|---|
| I-01, I-02, I-05, I-08, I-09, I-10, I-11, I-12 | A corrigir (D-INT-08) |
| I-03, I-04, I-06, I-07 | Decisão da Pessoa D em aberto |

O D-INT-02 começa depois da D-INT-08; `Local`, `UnidadeAcademica` e `MediaArea` dependem de I-01 e I-02.
