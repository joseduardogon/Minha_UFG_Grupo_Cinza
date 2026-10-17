# Entidade ItemCardapio

| Campo | Valor |
|---|---|
| **Entidade** | `ItemCardapio` |
| **Dono (autor)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Entregue a** | Phablo Tavares Paixão (Pessoa D), para integração no `DDados-Geral` e no `DD-Geral` |
| **Usada por** | RU |
| **Status** | Entregue para integração (primeira versão) |

## Descrição

Um item servido em uma refeição, com a categoria em que aparece. Na tela, cada categoria é um cartão com o nome da categoria e, abaixo, a descrição dos itens (ex.: categoria "Leite", descrição "Leite desnatado e integral").

## Entrada do dicionário de dados

| Atributo | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| id | Integer | Sim | Identificador único do item |
| descricao | String | Sim | Texto do item, como exibido na tela |
| idRefeicao | Integer | Sim | Refeição à qual o item pertence (referência a `Refeicao.id`) |
| idCategoria | Integer | Sim | Categoria em que o item aparece (referência a `CategoriaItem.id`) |

## Relacionamentos

| Com | Multiplicidade | Significado |
|---|---|---|
| Refeicao | 0..* para 1 | Cada item pertence a uma refeição |
| CategoriaItem | 0..* para 1 | Cada item tem uma categoria |

## Regras e restrições

- Todo item tem refeição e categoria.

## Trecho PlantUML (diagrama de dados)

Classes sem atributos e sem operações, só com as associações (formato do `DDados`).

```plantuml
class ItemCardapio
class Refeicao
class CategoriaItem
Refeicao "1" -- "0..*" ItemCardapio
CategoriaItem "1" -- "0..*" ItemCardapio
```
