# Entidade Cardapio

| Campo | Valor |
|---|---|
| **Entidade** | `Cardapio` |
| **Dono (autor)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Entregue a** | Phablo Tavares Paixão (Pessoa D), para integração no `DDados-Geral` e no `DD-Geral` |
| **Usada por** | RU |
| **Status** | Entregue para integração (primeira versão) |

## Descrição

Cardápio da semana do Restaurante Universitário. É único para todos os restaurantes da UFG, por isso não se liga a campus nem a regional. Reúne as refeições de cada dia da semana.

## Entrada do dicionário de dados

| Atributo | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| id | Integer | Sim | Identificador único do cardápio |
| dataInicio | Date | Sim | Primeiro dia da semana do cardápio |
| dataFim | Date | Sim | Último dia da semana do cardápio |

## Relacionamentos

| Com | Multiplicidade | Significado |
|---|---|---|
| Refeicao | 1 para 1..* | Um cardápio reúne as refeições da semana |

## Regras e restrições

- `dataFim` é igual ou posterior a `dataInicio`.
- Existe no máximo um cardápio para cada semana.

## Premissas a confirmar

- A tela mostra apenas o dia escolhido; se o servidor devolve só o cardápio do dia, e não o da semana, `Cardapio` pode ser tratado como o agrupador de uma consulta. O formato da resposta da API não é observável no app (premissa `P-RU-6`, em `RU/README.md`).

## Trecho PlantUML (diagrama de dados)

Classes sem atributos e sem operações, só com as associações (formato do `DDados`).

```plantuml
class Cardapio
class Refeicao
Cardapio "1" -- "1..*" Refeicao
```
