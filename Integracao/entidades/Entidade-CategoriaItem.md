# Entidade CategoriaItem

| Campo | Valor |
|---|---|
| **Entidade** | `CategoriaItem` |
| **Dono (autor)** | José Eduardo Gontijo de Carvalho |
| **Entregue a** | Phablo Tavares Paixão, para integração no `DDados-Geral` e no `DD-Geral` |
| **Usada por** | RU |
| **Status** | Entregue para integração (atualizada em 30/10/2026) |

## Descrição

Grupo em que os itens de uma refeição são apresentados, como o título de cada cartão da tela da refeição. As categorias mudam de uma refeição para outra, então cada categoria é um cadastro próprio. No Café da Manhã: "Leite", "Fruta", "Quitanda (vegana)", "Pães e quitandas" e "Complemento vegano". No Almoço e no Jantar: "Prato Proteico", "Opção Ovolactovegetariana", "Opção Vegana", "Guarnição", "Arroz", "Feijão", "Salada", "Refresco" e "Sobremesa" (lista completa informada pela Pessoa D na revisão REV-PR10 (B4); as capturas só chegam até "Guarnição", e os nomes exatos de "Arroz" a "Sobremesa" e de "Complemento vegano" na tela não foram vistos: `P-RU-5`). O conteúdo desta ficha é o mesmo do `DD-RU-01` (`RU/DD-RU-01.md`).

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

- Confirmadas: as categorias do Café da Manhã e as quatro primeiras do Almoço e do Jantar, vistas nas capturas (versão 3.2.0), e as demais, informadas pela Pessoa D na revisão REV-PR10 (B4): "Arroz", "Feijão", "Salada", "Refresco" e "Sobremesa" no Almoço e no Jantar e "Complemento vegano" no Café da Manhã (`P-RU-5`, em `RU/README.md`). Os nomes exatos dessas últimas na tela não foram vistos.

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
