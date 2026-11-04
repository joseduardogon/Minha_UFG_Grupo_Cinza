# DD-RU-01 – Entrada de DD do RU

| Campo | Valor |
|---|---|
| **Código** | `DD-RU-01` |
| **Título** | Entrada de DD do RU |
| **Autor(a)** | José Eduardo Gontijo de Carvalho |
| **Revisor(a)** | Phablo Tavares Paixão |
| **Status** | Em produção |
| **Rastreia para** | `DCla-RU-02`, `DCdu-RU-01`, `DD-Geral-01`, `DDados-Geral-01` |

## Descrição

Entidades do RU, para o DD consolidado (`DD-Geral-01`) e o modelo de dados integrado (`DDados-Geral-01`). Dono: Pessoa C. Não se relacionam com entidades de outros pacotes: o cardápio é único para todos os restaurantes da UFG, sem ligação com campus nem com regional. O conteúdo é o mesmo das fichas de entrega a D (`Integracao/entidades/Entidade-Cardapio.md`, `Entidade-Refeicao.md`, `Entidade-ItemCardapio.md` e `Entidade-CategoriaItem.md`).

O cardápio é cadastrado pelo painel web e consultado pelo app **por refeição, a semana inteira numa só chamada** (P-RU-3, P-RU-10). A unidade que o app recebe e usa é a `Refeicao`: uma refeição de um tipo (Café da Manhã, Almoço ou Jantar) em uma data, com os seus itens (P-RU-1). Cada item aparece na tela em uma categoria; as categorias mudam de uma refeição para outra, então cada categoria é um cadastro próprio (P-RU-5). As chaves estrangeiras não são atributos: as associações as expressam. Se "Pão francês / Bolo formigueiro", na categoria "Pães e quitandas" do Café da Manhã, é um item só ou dois itens exibidos juntos, separados por barra, não se sabe (P-RU-6).

**Decisão de modelagem: `Refeicao` por data.** Como a tela filtra a semana em memória pelo dia escolhido, cada `Refeicao` carrega a sua data, e a lista de `Refeicao` é o que o controlador do Comum guarda (`DCla-RU-02`). O dia da semana (as letras S, T, Q, Q, S, S do seletor: P-RU-4) é **derivado** da data, na tela (`TelaRefeicao.diaDaSemana`, `DCla-RU-01`); o RU não define enumeração de dia da semana. Se a Pessoa D preferir reutilizar o `DiaSemana` de `DD-Radio-01`, a decisão é da integração.

**Decisão de modelagem: sem `Cardapio`.** O painel web cadastra o cardápio por semana, mas **o app não usa nem instancia essa semana**: a resposta traz só as refeições, e a semana fica implícita nas datas. Por isso a entidade `Cardapio` foi retirada na integração (02/11/2026, `Docs/decisoes.md`), sem mudança nas classes do app (`DCla-RU-01`, `DCla-RU-02`); a regra que ela carregava passou para `Refeicao` (a combinação `tipo` e `data` não se repete).

**Tabela 1 – Refeicao**: uma refeição servida em uma data (os três cartões da tela RU); reúne os itens dessa refeição nessa data. É a unidade que o app carrega.

| Atributo | Tipo | Descrição |
|---|---|---|
| id | Integer | Identificador único da refeição |
| tipo | TipoRefeicao | Qual refeição é: CAFE_DA_MANHA, ALMOCO ou JANTAR |
| data | Date | Dia em que a refeição é servida; o dia da semana é obtido da data |

**Tabela 2 – ItemCardapio**: um item servido em uma refeição, com a categoria em que aparece. Na tela, cada categoria é um cartão com o nome da categoria e a descrição dos itens (ex.: categoria "Leite", descrição "Leite desnatado e integral"; categoria "Prato Proteico", descrição "Bife bovino acebolado (1ª)").

| Atributo | Tipo | Descrição |
|---|---|---|
| id | Integer | Identificador único do item |
| descricao | String | Texto do item, como exibido na tela; pode trazer um marcador, como "(1ª)" ou "(2ª)" |

**Tabela 3 – CategoriaItem**: grupo em que os itens de uma refeição são apresentados, o título de cada cartão da tela da refeição. No Café da Manhã: "Leite", "Fruta", "Quitanda (vegana)", "Pães e quitandas" e "Complemento vegano". No Almoço e no Jantar: "Prato Proteico", "Opção Ovolactovegetariana", "Opção Vegana", "Guarnição", "Arroz", "Feijão", "Salada", "Refresco" e "Sobremesa" (lista completa informada pela Pessoa D na revisão REV-PR10 (B4); as capturas só chegam até "Guarnição", e os nomes exatos de "Arroz" a "Sobremesa" e de "Complemento vegano" na tela não foram vistos: P-RU-5).

| Atributo | Tipo | Descrição |
|---|---|---|
| id | Integer | Identificador único da categoria |
| nome | String | Nome da categoria, como exibido na tela |

**Tabela 4 – TipoRefeicao** (enumeração): CAFE_DA_MANHA, ALMOCO, JANTAR.

**Associações:**

- Refeicao 1 — 0..* ItemCardapio ("tem").
- CategoriaItem 1 — 0..* ItemCardapio ("agrupa").

**Regras e restrições:**

- A combinação `tipo` e `data` de `Refeicao` não se repete.
- **O Jantar não tem sábado** (confirmado: o seletor do Jantar tem cinco letras, de segunda a sexta, na captura 26 da versão 3.2.0; P-RU-4): não existe `Refeicao` do tipo JANTAR em data que caia em sábado. Café da Manhã e Almoço têm refeição de segunda a sábado; nenhuma refeição tem domingo.
- Todo item tem refeição e categoria; o nome da categoria é único.

Fora do DD: a data de hoje e o dia selecionado na tela são estado da tela (`TelaRefeicao`, `DCla-RU-01`), não entidades.

Trecho PlantUML:

```plantuml
class Refeicao {
  id: Integer
  tipo: TipoRefeicao
  data: Date
}
class ItemCardapio {
  id: Integer
  descricao: String
}
class CategoriaItem {
  id: Integer
  nome: String
}
enum TipoRefeicao {
  CAFE_DA_MANHA
  ALMOCO
  JANTAR
}
Refeicao "1" -- "0..*" ItemCardapio : tem >
CategoriaItem "1" -- "0..*" ItemCardapio : agrupa >
```

As premissas `P-RU-n` citadas estão listadas, com o que as capturas de tela do app (versão 3.2.0) e o autor confirmaram e o que falta confirmar, em [`RU/README.md`](README.md).

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 11 (Software Engineering Models and Methods). IEEE, 2024.

ANTHROPIC. **Claude Code**. Assistente de IA. Disponível em: claude.ai/code. Acesso em: 30 out. 2026. Uso: apoio à redação e aos diagramas, a partir das instruções, das capturas de tela e das correções do autor (resumo em `IA/registro-C.md`). Questão: Apêndice <X>, Seção <X.1>.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
