# Entidade ItemCardapio

| Campo | Valor |
|---|---|
| **Entidade** | `ItemCardapio` |
| **Dono (autor)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Entregue a** | Phablo Tavares Paixão (Pessoa D), para integração no `DDados-Geral` e no `DD-Geral` |
| **Usada por** | RU |
| **Status** | Entregue para integração (atualizada em 30/10/2026) |

## Descrição

Um item servido em uma refeição, com a categoria em que aparece. Na tela, cada categoria é um cartão com o nome da categoria e, abaixo, a descrição dos itens (ex.: categoria "Leite", descrição "Leite desnatado e integral"; categoria "Prato Proteico", descrição "Bife bovino acebolado (1ª)"). O conteúdo desta ficha é o mesmo do `DD-RU-01` (`RU/DD-RU-01.md`).

## Entrada do dicionário de dados

| Atributo | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| id | Integer | Sim | Identificador único do item |
| descricao | String | Sim | Texto do item, como exibido na tela; pode trazer um marcador, como "(1ª)" ou "(2ª)" |

## Relacionamentos

| Com | Multiplicidade | Significado |
|---|---|---|
| Refeicao | 0..* para 1 | Cada item pertence a uma refeição (de uma data) |
| CategoriaItem | 0..* para 1 | Cada item tem uma categoria |

## Regras e restrições

- Todo item tem refeição e categoria.
- A descrição não é vazia.

## Premissas a confirmar

- Se "Pão francês / Bolo formigueiro", na categoria "Pães e quitandas" do Café da Manhã, é um item só ou dois itens exibidos juntos, separados por barra, não se sabe (premissa `P-RU-6`, em `RU/README.md`). As categorias do Almoço e do Jantar vistas nas capturas estão confirmadas (`P-RU-5`).

## Trecho PlantUML (diagrama de dados)

Com atributos (formato do `DD`). No `DDados`, as classes ficam sem atributos e sem operações, só com as associações.

```plantuml
class ItemCardapio {
  id: Integer
  descricao: String
}
class Refeicao
class CategoriaItem
Refeicao "1" -- "0..*" ItemCardapio : tem >
CategoriaItem "1" -- "0..*" ItemCardapio : agrupa >
```
