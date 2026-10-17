# Entidade CategoriaItem

| Campo | Valor |
|---|---|
| **Entidade** | `CategoriaItem` |
| **Dono (autor)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Entregue a** | Phablo Tavares Paixão (Pessoa D), para integração no `DDados-Geral` e no `DD-Geral` |
| **Usada por** | RU |
| **Status** | Entregue para integração (primeira versão) |

## Descrição

Grupo em que os itens de uma refeição são apresentados, como o título de cada cartão da tela da refeição (ex.: "Leite", "Fruta", "Pães e quitandas"). As categorias mudam de uma refeição para outra, então cada categoria é um cadastro próprio.

## Entrada do dicionário de dados

| Atributo | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| id | Integer | Sim | Identificador único da categoria |
| nome | String | Sim | Nome da categoria, como exibido na tela |

## Relacionamentos

| Com | Multiplicidade | Significado |
|---|---|---|
| ItemCardapio | 1 para 0..* | Uma categoria agrupa vários itens |

## Regras e restrições

- O nome da categoria é único.

## Premissas a confirmar

- Categorias vistas na captura do Café da Manhã (versão 3.2.0): "Leite", "Fruta", "Quitanda (vegana)" e "Pães e quitandas". Faltam as categorias do Almoço e do Jantar (premissa `P-RU-5`).

## Trecho PlantUML (diagrama de dados)

Classes sem atributos e sem operações, só com as associações (formato do `DDados`).

```plantuml
class CategoriaItem
class ItemCardapio
CategoriaItem "1" -- "0..*" ItemCardapio
```
