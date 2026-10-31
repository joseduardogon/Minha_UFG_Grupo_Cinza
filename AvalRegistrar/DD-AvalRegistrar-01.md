# DD-AvalRegistrar-01 – Entrada de DD de Avaliação de UA (registrar)

| Campo | Valor |
|---|---|
| **Código** | `DD-AvalRegistrar-01` |
| **Título** | Entrada de DD de Avaliação de UA (registrar) |
| **Autor(a)** | José Eduardo Gontijo de Carvalho |
| **Revisor(a)** | Maicon Brendo da Silva (Pessoa B) |
| **Status** | Em produção |
| **Rastreia para** | `DCdu-AvalRegistrar-01`, `DCla-AvalRegistrar-03`, `DCla-AvalRegistrar-04`, `DD-Locais-01`, `DD-Geral-01`, `DDados-Geral-01` |

## Descrição

Entidades de `AvalRegistrar`, para o DD consolidado (`DD-Geral-01`) e o modelo de dados integrado (`DDados-Geral-01`). Dono: José Eduardo Gontijo de Carvalho. É também o ponto de partida de `AvalConsultar` (Phablo), que lê estas entidades para calcular as notas; por isso a seção "Para quem consome" explica como elas se agregam.

O enunciado (Apêndice A) define uma **dimensão de qualidade** como uma categoria de elementos educacionais correlatos, e cada dimensão é caracterizada por **elementos educacionais**. Para cada elemento há **questões** predefinidas, e a **avaliação** é o registro das notas que um usuário deu a essas questões para uma unidade acadêmica (UA). Dimensões, elementos e questões são cadastrados no painel web e o app os recebe do Servidor/API a cada avaliação, sem cache (P-AR-3). O questionário é o mesmo para toda UA (P-AR-9).

Os identificadores (`id`) de dimensão, elemento e questão são inteiros atribuídos pelo servidor e a `ordem` define a ordem de apresentação (P-AR-20). O que é alterado ou retirado no painel web continua existindo no servidor para as avaliações já registradas (P-AR-21).

**Tabela 1 – DimensaoQualidade**: categoria de elementos educacionais correlatos (ex.: infraestrutura física, corpo docente, recursos pedagógicos, condições ambientais).

| Atributo | Tipo | Descrição |
|---|---|---|
| id | Integer | Identificador da dimensão, atribuído pelo servidor |
| nome | String | Nome da dimensão, exibido no questionário |
| ordem | Integer | Posição da dimensão no questionário (crescente) |

**Tabela 2 – ElementoEducacional**: aspecto avaliado dentro de uma dimensão (ex.: salas de aula, laboratórios, limpeza). Pertence a uma só dimensão.

| Atributo | Tipo | Descrição |
|---|---|---|
| id | Integer | Identificador do elemento, atribuído pelo servidor |
| nome | String | Nome do elemento, exibido no questionário |
| ordem | Integer | Posição do elemento dentro da sua dimensão (crescente) |

**Tabela 3 – Questao**: pergunta predefinida sobre um elemento, respondida com uma nota (ex.: "Em uma escala de zero (péssima) a cinco (excelente), qual a sua avaliação da limpeza do prédio da Unidade Acadêmica?"). Pertence a um só elemento.

| Atributo | Tipo | Descrição |
|---|---|---|
| id | Integer | Identificador da questão, atribuído pelo servidor; é o que o app envia para dizer a que questão a nota se refere |
| texto | String | Enunciado da questão, exibido ao usuário |
| ordem | Integer | Posição da questão dentro do seu elemento (crescente) |

**Tabela 4 – Avaliacao**: registro da opinião de um usuário sobre a qualidade de uma UA. É anônima e, depois de registrada, não pode ser editada nem excluída (contrato-base, seção 8). O mesmo usuário pode avaliar a mesma UA mais de uma vez; cada envio cria uma `Avaliacao` nova.

| Atributo | Tipo | Descrição |
|---|---|---|
| id | Integer | **Só no servidor.** Identificador da avaliação, atribuído no registro (P-AR-22) |
| dataHoraRegistro | Date | **Só no servidor.** Data e hora em que o servidor registrou a avaliação (P-AR-22); o app não a envia nem a recebe |

No app, `Avaliacao` tem apenas as associações com `UnidadeAcademica` e `NotaQuestao` (`unidade` e `notas` em `DCla-AvalRegistrar-04`).

**Tabela 5 – NotaQuestao**: a nota dada a uma questão dentro de uma avaliação.

| Atributo | Tipo | Descrição |
|---|---|---|
| valor | Integer | Nota inteira de 0 (péssima) a 5 (excelente), obrigatória (P-AR-5) |

A questão a que a nota se refere é a associação `NotaQuestao` — `Questao` (abaixo); no envio, vai como `idQuestao`.

**Referência a `UnidadeAcademica`.** A UA é entidade de Maicon (Pessoa B), especialização de `Local`, e está definida em `DD-Locais-01`; aqui só é referenciada, sem ser redefinida (contrato-base, seção 7). `AvalRegistrar` usa dela `id` e `nome` (herdados de `Local`) e `sigla`. A lista de UAs vem do Servidor/API (P-AR-2).

**Associações:**

- `DimensaoQualidade` 1 — 1..* `ElementoEducacional` ("é caracterizada por"): toda dimensão tem ao menos um elemento.
- `ElementoEducacional` 1 — 1..* `Questao` ("tem"): todo elemento tem ao menos uma questão.
- `Avaliacao` * — 1 `UnidadeAcademica` ("avalia"): uma UA recebe muitas avaliações; cada avaliação é de uma só UA.
- `Avaliacao` 1 — 1..* `NotaQuestao` ("é composta por"): composição; uma `NotaQuestao` não existe fora de uma avaliação.
- `NotaQuestao` * — 1 `Questao` ("responde a"): uma questão recebe muitas notas, uma por avaliação.

**Restrições:**

- O `valor` de uma `NotaQuestao` é inteiro e está entre 0 e 5, inclusive (P-AR-5).
- Em cada `Avaliacao` há exatamente uma `NotaQuestao` por questão do questionário: nenhuma questão fica sem nota e nenhuma tem duas (P-AR-5).
- Uma `Avaliacao` registrada não é editada nem excluída; corrigir uma opinião é registrar outra avaliação.
- Não existe avaliador: nenhuma entidade ou atributo identifica, nem de forma indireta, quem avaliou (P-AR-7).
- Só `Avaliacao.id` e `Avaliacao.dataHoraRegistro` existem apenas no servidor; as demais informações existem no app e no servidor.

### Para quem consome (AvalConsultar)

1. Cada `NotaQuestao` liga uma nota (0 a 5) a uma `Questao`, e a `Questao` leva à sua `DimensaoQualidade` pelo caminho `Questao` → `ElementoEducacional` → `DimensaoQualidade`; é por esse caminho que as notas se agregam.
2. Dentro de uma `Avaliacao`, a nota de um elemento é a média das notas de suas questões, a nota de uma dimensão é a média de seus elementos e a nota da avaliação é a média das dimensões (P-AR-12); o cálculo é de `AvalConsultar` e aqui só se registra.
3. Como toda questão tem nota em toda avaliação (P-AR-5), essas médias não têm lacunas. Mas o questionário pode mudar entre uma avaliação e outra (P-AR-3, P-AR-21): avaliações antigas podem referenciar questões, elementos ou dimensões que já não estão no questionário vigente, e a agregação deve ser feita pelos `id`.
4. A nota de uma UA, de uma área do conhecimento ou da UFG agrega várias avaliações, a partir de `Avaliacao.unidade` e de `UnidadeAcademica.areaConhecimento` (`DD-Locais-01`); como esta entrada não define a forma de agregar entre avaliações, ela é decisão de `AvalConsultar`.
5. Não há atributo de avaliador: não é possível filtrar, agrupar ou eliminar duplicatas por pessoa, e duas avaliações da mesma UA são independentes. Para ordenar ou filtrar no tempo, use `dataHoraRegistro`, que só existe no servidor.

Trecho PlantUML:

```plantuml
class DimensaoQualidade {
  id: Integer
  nome: String
  ordem: Integer
}
class ElementoEducacional {
  id: Integer
  nome: String
  ordem: Integer
}
class Questao {
  id: Integer
  texto: String
  ordem: Integer
}
class Avaliacao {
  id: Integer {só no servidor}
  dataHoraRegistro: Date {só no servidor}
}
class NotaQuestao {
  valor: Integer {0..5}
}
class UnidadeAcademica <<Locais>>

DimensaoQualidade "1" -- "1..*" ElementoEducacional : é caracterizada por >
ElementoEducacional "1" -- "1..*" Questao : tem >
Avaliacao "*" -- "1" UnidadeAcademica : avalia >
Avaliacao "1" *-- "1..*" NotaQuestao : é composta por >
NotaQuestao "*" -- "1" Questao : responde a >
```

As premissas `P-AR-n` citadas estão listadas em [`AvalRegistrar/README.md`](README.md).

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 11 (Software Engineering Models and Methods). IEEE, 2024.

UNIVERSIDADE FEDERAL DE GOIÁS. Instituto de Informática. **Definição de Atividades Práticas Supervisionadas (APS) da Disciplina**: INF 0290 – Projeto de Software, 2026/2. Goiânia, 2026. Apêndice A.

ANTHROPIC. **Claude Code**. Assistente de IA. Disponível em: claude.ai/code. Acesso em: 30 out. 2026. Uso: rascunho do texto e dos diagramas a partir da especificação e das instruções do autor, que revisou o conteúdo. Questão: Apêndice <X>, Seção <X.1>.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
