# Entidade CategoriaItem

| Campo | Valor |
|---|---|
| **Entidade** | `CategoriaItem` |
| **Dono (autor)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Entregue a** | Phablo Tavares Paixão (Pessoa D), para integração no `DDados-Geral` e no `DD-Geral` |
| **Usada por** | RU |
| **Status** | Entregue para integração (atualizada em 30/10/2026) |

## Descrição

Grupo em que os itens de uma refeição são apresentados, como o título de cada cartão da tela da refeição. As categorias mudam de uma refeição para outra, então cada categoria é um cadastro próprio. No Café da Manhã: "Leite", "Fruta", "Quitanda (vegana)" e "Pães e quitandas". No Almoço e no Jantar: "Prato Proteico", "Opção Ovolactovegetariana", "Opção Vegana" e "Guarnição". O conteúdo desta ficha é o mesmo do `DD-RU-01` (`RU/DD-RU-01.md`).

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

- Confirmadas nas capturas (versão 3.2.0): as categorias do Café da Manhã e as quatro do Almoço e do Jantar (`P-RU-5`). Abaixo de "Guarnição" a captura é cortada, e outras categorias podem existir (`P-RU-6`, em `RU/README.md`).

## Trecho PlantUML (diagrama de dados)

Com atributos (formato do `DD`). No `DDados`, as classes ficam sem atributos e sem operações, só com as associações.

```plantuml
class CategoriaItem {
  id: Integer
  nome: String
}
class ItemCardapio
CategoriaItem "1" -- "0..*" ItemCardapio : agrupa >
```
