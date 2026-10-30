# Entidade Refeicao

| Campo | Valor |
|---|---|
| **Entidade** | `Refeicao` |
| **Dono (autor)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Entregue a** | Phablo Tavares Paixão (Pessoa D), para integração no `DDados-Geral` e no `DD-Geral` |
| **Usada por** | RU |
| **Status** | Entregue para integração (atualizada em 30/10/2026) |

## Descrição

Uma refeição servida em uma data: Café da Manhã, Almoço ou Jantar (os três cartões da tela RU). Reúne os itens do cardápio dessa refeição nessa data. É a unidade que o app carrega: ao abrir a tela de uma refeição, uma só chamada traz as `Refeicao` da semana inteira (uma por data), e a troca de dia filtra essa lista em memória pela `data`. A tela mostra a data por extenso (ex.: "Terça-feira, 27 de outubro de 2026"). O conteúdo desta ficha é o mesmo do `DD-RU-01` (`RU/DD-RU-01.md`).

## Entrada do dicionário de dados

| Atributo | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| id | Integer | Sim | Identificador único da refeição |
| tipo | TipoRefeicao | Sim | Qual refeição é: CAFE_DA_MANHA, ALMOCO ou JANTAR |
| data | Date | Sim | Dia em que a refeição é servida; o dia da semana (segunda a sábado, as letras do seletor) é derivado da data |

**Enumeração TipoRefeicao:** CAFE_DA_MANHA, ALMOCO, JANTAR.

## Relacionamentos

| Com | Multiplicidade | Significado |
|---|---|---|
| Cardapio | 1..* para 1 | Cada refeição pertence a um cardápio (semana) no servidor; o app não usa essa ligação |
| ItemCardapio | 1 para 0..* | Uma refeição tem vários itens |

## Regras e restrições

- A `data` está entre `Cardapio.dataInicio` e `Cardapio.dataFim`.
- Dentro de um cardápio, a combinação `tipo` e `data` não se repete.
- **O Jantar não tem sábado** (confirmado pelo seletor de cinco letras do Jantar, captura 26, versão 3.2.0; `P-RU-4`): não existe `Refeicao` do tipo JANTAR em data que caia em sábado. Café da Manhã e Almoço têm refeição de segunda a sábado, e nenhuma refeição tem domingo.

## Premissas a confirmar

- Confirmado (versão 3.2.0): as três refeições (`P-RU-1`) e o seletor de dia, de segunda a sábado no Café da Manhã e no Almoço e de segunda a sexta no Jantar (`P-RU-4`). Falta conferir o que a tela seleciona quando hoje é domingo ou sábado no Jantar (`P-RU-13`), em `RU/README.md`.
- O dia da semana é derivado da `data`; o RU não define enumeração própria de dia da semana. Se D preferir reutilizar o `DiaSemana` do `DD-Radio-01`, a decisão é da integração.

## Trecho PlantUML (diagrama de dados)

Com atributos (formato do `DD`). No `DDados`, as classes ficam sem atributos e sem operações, só com as associações.

```plantuml
class Refeicao {
  id: Integer
  tipo: TipoRefeicao
  data: Date
}
enum TipoRefeicao {
  CAFE_DA_MANHA
  ALMOCO
  JANTAR
}
class Cardapio
class ItemCardapio
Cardapio "1" -- "1..*" Refeicao : reúne >
Refeicao "1" -- "0..*" ItemCardapio : tem >
```
