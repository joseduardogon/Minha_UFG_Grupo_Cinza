# Entidade Cardapio

| Campo | Valor |
|---|---|
| **Entidade** | `Cardapio` |
| **Dono (autor)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Entregue a** | Phablo Tavares Paixão (Pessoa D), para integração no `DDados-Geral` e no `DD-Geral` |
| **Usada por** | RU |
| **Status** | Entregue para integração (atualizada em 30/10/2026) |

## Descrição

Cardápio da semana do Restaurante Universitário, agrupador das refeições no servidor (o painel web cadastra o cardápio por semana). É único para todos os restaurantes da UFG, por isso não se liga a campus nem a regional. **O app não usa nem instancia o `Cardapio`:** ele busca a semana inteira de uma refeição numa só chamada e recebe só as `Refeicao`, com a semana implícita nas datas. A entidade foi mantida para registrar a regra de unicidade por semana; a integração pode retirá-la sem afetar o app. O conteúdo desta ficha é o mesmo do `DD-RU-01` (`RU/DD-RU-01.md`).

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

- O app consulta a API por refeição, sem data, e recebe a semana inteira (rota `GET /cardapio`, com o parâmetro `refeicao`); a carga semanal é informação do autor do projeto (`P-RU-3`), e a rota e o formato da resposta não são observáveis no app (premissa de projeto `P-RU-10`, em `RU/README.md`).

## Trecho PlantUML (diagrama de dados)

Com atributos (formato do `DD`). No `DDados`, as classes ficam sem atributos e sem operações, só com as associações.

```plantuml
class Cardapio {
  id: Integer
  dataInicio: Date
  dataFim: Date
}
class Refeicao
Cardapio "1" -- "1..*" Refeicao : reúne >
```
