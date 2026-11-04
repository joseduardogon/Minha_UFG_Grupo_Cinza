# REV-PR12 – Revisão de Avaliação – Consultar notas

- **PR:** #12 "Especificação de Avaliação – Consultar notas (AvalConsultar)" (branch `revisar-pr`, commits `c0bf8fb` a `93f7075`)
- **Autor:** Phablo Tavares Paixão
- **Revisor:** Maicon Brendo da Silva
- **Data:** 01/11/2026
- **Tarefa:** Revisão do PR #12 (AvalConsultar)

## 1. Resumo

Os 16 arquivos `.puml` compilam sem erros sintáticos e os identificadores em `@startuml`/`@startsalt` coincidem rigorosamente com os nomes dos arquivos. O padrão visual segue as convenções do projeto (PlantUML padrão, sem temas de cores customizados).

A cascata documental está completa e muito bem estruturada: `DCdu` (UC10.1 a UC10.3), `DAtv` (1 a 3), `DIhc` (1 a 3), `DD`, `DCmp`, `DCla` (1 e 2), `DSeq` (1 a 3), `DEst` (1 a 3), contratos de operações (`Contrato-AvalConsultar-01`) e regras ativas (`ECA-AvalConsultar-01`).

As diretrizes do professor e as regras de negócio de Avaliação foram plenamente respeitadas: anonimato do usuário garantido, notas limitadas estritamente à escala de 0 a 5 com uma casa decimal, sem operações de edição ou exclusão, tratamento explícito de UAs sem avaliações (exibindo "Sem avaliações" e desconsiderando-as nas médias agregadas), e preservação da arquitetura sem cache local com recarga a cada exibição. O desacoplamento entre `AvalRegistrar` e `AvalConsultar` via Intent implícito (`VER_NOTAS`) eliminou com elegância o ciclo de pacotes no `DPac-Geral-01`.

Foi identificado 2 bloqueantes pontuais (ausência do atributo `acesso` na classe `TelaNotasUA` em `DCla-AvalConsultar-01` e sobreposição visual de linhas na renderização dos diagramas de atividade `DAtv-AvalConsultar-01` e `02`), além de observações de alinhamento.

**Parecer: pedir mudanças.** Os bloqueantes B1 e B2 são pontuais e de rápida resolução.

## 2. Bloqueantes

| # | Local | Problema | Correção |
|---|---|---|---|
| B1 | `AvalConsultar/DCla-AvalConsultar-01.puml:56-64` e `DCla-AvalConsultar-01.md:24` | Na classe `TelaNotasUA`, o construtor recebe `acesso: IAcessoApi` (`+ TelaNotasUA(acesso: IAcessoApi, unidade: UnidadeAcademica)`), e no método `aoExibir()` ele é repassado para instanciar a fonte (`FonteNotasUnidade(acesso, unidade)`, conforme `DSeq-AvalConsultar-03.puml:17`). No entanto, ao contrário de `TelaNotas` (linha 34) e `TelaNotasArea` (linha 45), `TelaNotasUA` **não declara o atributo privado `- acesso: IAcessoApi`**. Sem esse campo, a classe não retém a referência da API para uso no ciclo de vida. | Adicionar `- acesso: IAcessoApi` na lista de atributos privados de `TelaNotasUA` no arquivo `DCla-AvalConsultar-01.puml` e alinhar a descrição no `.md`. |
| B2 | `AvalConsultar/DAtv-AvalConsultar-01.puml:26-38` e `DAtv-AvalConsultar-02.puml:26-38` | Na parte inferior da imagem renderizada (`.png`), as linhas de fluxo e nós de finalização (`stop`) das raias `Membro` e `App` estão se sobrepondo (cruzamento confuso das arestas dos ramos do `if (O que o usuário faz?)`), prejudicando a legibilidade e a qualidade gráfica exigida pelo professor. | Ajustar os parâmetros de roteamento do PlantUML (ex.: `skinparam nodesep`, `skinparam ranksep`, quebras de linha `\n` nos rótulos de transição ou reestruturação das conexões entre raias/término) para desemaranhar o fluxo inferior em ambos os diagramas e gerar novamente as imagens `.png`. |

## 3. Observações (Não-bloqueantes / Sugestões)

- **Tratamento de Vazio e Indisponível nos diagramas de atividade:** Em `DAtv-AvalConsultar-01.puml:17-22` e `DAtv-AvalConsultar-02.puml:17-22`, as decisões de falha de comunicação e lista vazia terminam diretamente em `stop`. Já em `DAtv-AvalConsultar-03.puml:17-28`, todos os ramos convergem para a ação de `:Tocar na seta de voltar;`. Embora nos DEsts correspondentes (`DEst-AvalConsultar-01`, `02` e `03`) a única saída de `Vazio` e `Indisponível` seja `aoVoltar`, nos DAtv-01 e 02 não fica explícito graficamente como o usuário sai da tela nesses estados. Sugere-se incluir uma nota explicativa em DAtv-01 e DAtv-02 (semelhante à nota existente no `DAtv-AvalRegistrar-01:19-23`) indicando que a saída ocorre pela seta de voltar (`aoVoltar`), ou unificar a modelagem com DAtv-03.
- **Nomenclatura nos pacotes importados:** Em `DCmp-AvalConsultar-01.puml:22`, usa-se `package "Locais (pacote de B)"`, enquanto em `AvalRegistrar/DCmp-AvalRegistrar-01.puml:22` consta `package "Locais (pacote de Maicon)"`. Recomenda-se manter a consistência de identificação (por letra ou por nome).

## 4. Verificações sem problema

- **Anonimato e Segurança:** O membro da comunidade UFG é ator anônimo; nenhuma operação coleta ou trafega dados pessoais do usuário.
- **Regras de Negócio e Cálculo:** Escala de notas estritamente entre 0 e 5 (com uma casa decimal via `FormatoNota.formatar`); UAs não avaliadas exibem "Sem avaliações" e não afetam a média da área nem da UFG (regras R1 a R7 no `Contrato-AvalConsultar-01`).
- **Arquitetura Servidor/API:** Conforme a decisão de 01/11/2026, as médias são calculadas dinamicamente pelo servidor; o app não persiste notas nem realiza cálculos pesados de médias em memória.
- **Desacoplamento e Ciclos:** O uso de Intent implícito (`VER_NOTAS`) pelo botão da `TelaAvaliacao` desacoplou a navegação, garantindo que `AvalRegistrar` não dependa de `AvalConsultar` e mantendo o `DPac-Geral-01` acíclico.
- **Conformidade com o pacote Comum:** Reúso integral das interfaces e classes `IAcessoApi`, `IFonteDados<T>`, `IControladorTelaRemota<T>`, `ControladorTelaRemota<T>`, `IObservadorEstado` e `EstadoTela`, sem redefinições e com as mesmas assinaturas.
- **Correspondência entre Artefatos:**
  - Eventos de IHC (`DIhc-01` a `03`: E0, E1, E2) mapeiam perfeitamente para os métodos em `DCla-AvalConsultar-01` e transições em `DEst-AvalConsultar-01` a `03`.
  - Chamadas de métodos no `DSeq-AvalConsultar-01` a `03` batem com as assinaturas e tipos de `DCla-AvalConsultar-01` e `02`.
  - Herança de `Local <|-- UnidadeAcademica` é respeitada sem atributos duplicados.
- **Rastreabilidade e Formato:** Todos os 19 arquivos `.md` do módulo `AvalConsultar` seguem o `Template-Item.md` com a seção "Rastreia para" devidamente preenchida e histórico de revisão disponível.

