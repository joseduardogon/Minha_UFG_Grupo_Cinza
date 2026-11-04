# REV-PR13 – Revisão da Fase 3: Integração

- **PR:** #13 "Fechamento da fase 3 (integração): validação de entidades, modelo de dados integrado, modelos gerais e rastreabilidade" (branch `rev-pr-13`, commits `82f595a` a `5271abd`)
- **Autor:** Phablo Tavares Paixão
- **Revisor:** Maicon Brendo da Silva
- **Data:** 02/11/2026
- **Tarefa:** Revisão do PR #13 (Integração)

## 1. Resumo

O PR consolida a Fase 3 (integração) do projeto, abrangendo as tarefas `D-AVC`, `D-INT-01`, `D-INT-08`, `D-INT-02`, `D-INT-03` e `D-INT-04`.

A integração foi executada com alto nível de rigor metodológico e aderência às diretrizes da disciplina INF0290:
1. **Validação e Resolução de Entidades (`D-INT-01` e `D-INT-08`):** Todos os 12 achados (I-01 a I-12) foram tratados. Destacam-se a criação da entidade `AreaConhecimento` (atribuída a B), a alocação de `Regional` e `Campus` no pacote `Comum` (resolvendo dependências interpacotes sem ciclos), a retirada de `Cardapio` (obedecendo ao comportamento observado), a confirmação do anonimato do avaliador (sem entidade) e a formalização da ausência de entidades em Segurança e Apps UFG (`DD-Seguranca-01` e `DD-AppsUFG-01`).
2. **Modelo de Dados Integrado (`D-INT-02`):** O diagrama `DDados-Geral-01` atende estritamente ao Apêndice D da APS (apenas classes e associações, sem atributos nem métodos). O `DD-Geral-01` consolida com clareza as 23 tabelas de entidades/enumerações e a tabela de 18 associações com seus respectivos donos.
3. **Modelos Gerais e Renumeração (`D-INT-03`):** Unificação da nomenclatura dos casos de uso para o padrão hierárquico `UCnn.m`, tabela de mapeamento macro/detalhado no `DCdu-Geral-01` e fechamento do `DPac-Geral-01`.
4. **Matriz de Rastreabilidade (`D-INT-04`):** Matriz abrangendo os 171 itens de informação do projeto em `Integracao/rastreabilidade.md`, com mapeamento bidirecional completo ("Rastreia para" e "Rastreado por") e correção do item R-01 (`DCla-Locais-02`).
5. **Correção dos DAtv de Avaliação (`D-AVC`):** Resolução das setas sobrepostas nos diagramas de atividades de `AvalConsultar` e `AvalRegistrar`.

Foi identificado **1 bloqueante pontual** decorrente da renumeração automática dos casos de uso (erro de digitação gerando códigos com dígitos extras nos `.puml` de Segurança e Guia) e **1 observação** de preenchimento de cabeçalho.

**Parecer: pedir mudanças.** O ajuste nos dois arquivos `.puml` e regeneração de seus PNGs é rápido e garante a nota integral nos critérios de consistência formal e semântica da APS.

## 2. Bloqueantes

| # | Local | Problema | Correção |
|---|---|---|---|
| B1 | `Seguranca/DCdu-Seguranca-01.puml:14-15`, `Guia/DCdu-Guia-01.puml:12` e respectivos `.png` | Na renumeração dos casos de uso detalhados para o padrão `UCnn.m`, ocorreu um erro de digitação nos arquivos PlantUML: <br>• Em `Seguranca/DCdu-Seguranca-01.puml`, os casos foram rotulados como `UC011.1` e `UC011.2` (três dígitos no prefixo), divergindo do markdown (`Seguranca/DCdu-Seguranca-01.md:30,44`) e do `DCdu-Geral-01.md:45`, que definem `UC01.1` e `UC01.2`.<br>• Em `Guia/DCdu-Guia-01.puml`, o caso foi rotulado como `UC031.1`, divergindo de `Guia/DCdu-Guia-01.md:30` e `Geral/DCdu-Geral-01.md:47`, que definem `UC03.1`. | Corrigir os rótulos nos arquivos `.puml` para `UC01.1`, `UC01.2` e `UC03.1`, e gerar novamente os arquivos de imagem `Seguranca/DCdu-Seguranca-01.png` e `Guia/DCdu-Guia-01.png`. |

## 3. Observações (Não-bloqueantes / Sugestões)

- **Revisor nos cabeçalhos:** Em `Seguranca/DCdu-Seguranca-01.md:8`, `Locais/DCdu-Locais-01.md:8` e `Locais/DCla-Locais-02.md:8`, o campo de revisor constava como "Revisor(a) a definir". Foi devidamente padronizado com o revisor da fatia (`José Eduardo Gontijo de Carvalho`), sanando a pendência em conformidade com o achado I-12.

## 4. Verificações sem problema

- **Critério 4.1 e 4.2 (Modelo de Dados Integrado):** O `DDados-Geral-01` não contém classes duplicadas, nomes concorrentes nem classes sem pacote definido. As chaves estrangeiras foram devidamente modeladas como associações (não atributos).
- **Herança e Associações entre Fatias:**
  - `Local <|-- UnidadeAcademica` respeitada sem redefinição de atributos.
  - Associação `Campus 1 — 0..* Local` e `UnidadeAcademica 0..* — 1 AreaConhecimento` devidamente formalizadas.
  - `Regional` e `Campus` pertencem ao `Comum`, garantindo que `Locais`, `Eventos` e `Noticias` as referenciem sem introduzir acoplamento entre fatias.
- **Regras da Avaliação Institucional:** Anonimato rigoroso mantido (sem entidade de avaliador); notas na escala de 0 a 5; sem operações de alteração ou exclusão de avaliação; as médias derivadas (`MediaArea`, `NotaUnidade`, `NotaDimensao`) são somente leitura e computadas na API.
- **Rastreabilidade (Critério 5.2):** A matriz em `Integracao/rastreabilidade.md` é exaustiva (171 itens), sem elos quebrados ou itens autorreferenciais. O apontamento pendente de `DCla-Locais-02` para `DCmp-Locais-01` (R-01) foi devidamente corrigido.
- **Legibilidade dos DAtv de Avaliação:** As alterações em `DAtv-AvalConsultar-01`, `02` e `DAtv-AvalRegistrar-02`, `03` sanaram com sucesso a sobreposição de setas e a confusão de raias nos fluxos inferiores.
- **Conformidade de Pacotes e Ciclos:** `DPac-Geral-01` e `DImp-Geral-01` mantêm a arquitetura limpa, estável e livre de dependências circulares.

