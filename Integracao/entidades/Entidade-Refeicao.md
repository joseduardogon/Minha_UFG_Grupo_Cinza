# Entidade Refeicao

| Campo | Valor |
|---|---|
| **Entidade** | `Refeicao` |
| **Dono (autor)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Entregue a** | Phablo Tavares Paixão (Pessoa D), para integração no `DDados-Geral` e no `DD-Geral` |
| **Usada por** | RU |
| **Status** | Entregue para integração (primeira versão) |

## Descrição

Uma refeição servida em uma data: Café da Manhã, Almoço ou Jantar (os três cartões da tela RU). Reúne os itens do cardápio dessa refeição nessa data. A tela da refeição mostra a data por extenso (ex.: "Sexta-feira, 16 de outubro de 2026").

## Entrada do dicionário de dados

| Atributo | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| id | Integer | Sim | Identificador único da refeição |
| tipo | TipoRefeicao | Sim | Qual refeição é: CAFE_DA_MANHA, ALMOCO ou JANTAR |
| data | Date | Sim | Dia em que a refeição é servida; o dia da semana (segunda a sábado, as letras do seletor) é obtido da data |
| idCardapio | Integer | Sim | Cardápio ao qual pertence (referência a `Cardapio.id`) |

## Relacionamentos

| Com | Multiplicidade | Significado |
|---|---|---|
| Cardapio | 1..* para 1 | Cada refeição pertence a um cardápio |
| ItemCardapio | 1 para 0..* | Uma refeição tem vários itens |

## Regras e restrições

- A `data` está entre `Cardapio.dataInicio` e `Cardapio.dataFim`.
- Não existe refeição do tipo JANTAR em data que cai em sábado (regra da divisão de trabalho; o sábado ainda não foi conferido nas capturas).
- Dentro de um cardápio, a combinação `tipo` e `data` não se repete.

## Premissas a confirmar

- Confirmado nas capturas (versão 3.2.0): as três refeições (Café da Manhã, Almoço e Jantar) e o seletor de dia de segunda a sábado. Falta conferir o que a tela mostra no jantar de sábado e se o domingo é atendido (premissas `P-RU-3` e `P-RU-4`, em `RU/README.md`).

## Trecho PlantUML (diagrama de dados)

Classes sem atributos e sem operações, só com as associações (formato do `DDados`).

```plantuml
class Refeicao
class Cardapio
class ItemCardapio
Cardapio "1" -- "1..*" Refeicao
Refeicao "1" -- "0..*" ItemCardapio
```
