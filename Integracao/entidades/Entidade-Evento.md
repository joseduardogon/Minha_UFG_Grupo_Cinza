# Entidade Evento

| Campo | Valor |
|---|---|
| **Entidade** | `Evento` |
| **Dono (autor)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Entregue a** | Phablo Tavares Paixão (Pessoa D), para integração no `DDados-Geral` e no `DD-Geral` |
| **Usada por** | Eventos (`DCla-Eventos-02`) |
| **Status** | Entregue para integração (primeira versão) |

## Descrição

Acontecimento divulgado pela UFG, cadastrado pelo painel web e consultado no app por regional e por data. Pode durar mais de um dia (data de início e data de fim) e pode ter o endereço de uma página com detalhes.

## Entrada do dicionário de dados

| Atributo | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| id | Integer | Sim | Identificador único do evento |
| titulo | String | Sim | Nome do evento, como exibido na lista |
| dataInicio | Date | Sim | Primeiro dia do evento |
| dataFim | Date | Sim | Último dia do evento; igual a `dataInicio` se o evento dura um dia |
| local | String | Não | Onde o evento acontece, em texto livre (ex.: "Centro de Línguas, Câmpus Samambaia"), visto na página do evento |
| url | String | Não | Endereço da página do evento, aberto no Navegador ao tocar no item |
| idRegional | Integer | Sim | Regional do evento (referência a `Regional.id`) |

## Relacionamentos

| Com | Multiplicidade | Significado |
|---|---|---|
| Regional | 0..* para 1 | Cada evento pertence a uma regional |

## Regras e restrições

- `dataFim` é igual ou posterior a `dataInicio`.
- O evento aparece na consulta de toda data entre `dataInicio` e `dataFim`, inclusive.
- Sem `url`, o toque no evento no app não tem efeito.

## Premissas a confirmar

- A captura da página do evento (aberta no Navegador) mostra o título, o local e o período ("15 a 17 de Outubro 2026"). A captura da tela de lista de Eventos (calendário) ainda não foi conferida: falta confirmar quais desses dados ela exibe.

## Trecho PlantUML (diagrama de dados)

Classes sem atributos e sem operações, só com as associações (formato do `DDados`).

```plantuml
class Evento
class Regional
Regional "1" -- "0..*" Evento
```
