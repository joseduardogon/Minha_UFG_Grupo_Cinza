# Entidade Campus

| Campo | Valor |
|---|---|
| **Entidade** | `Campus` |
| **Dono (autor)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Entregue a** | Phablo Tavares Paixão (Pessoa D), para integração no `DDados-Geral` e no `DD-Geral` |
| **Usada por** | Locais (Pessoa B); Eventos e Notícias só usam a regional |
| **Status** | Entregue para integração (primeira versão) |

## Descrição

Unidade física da UFG, vinculada a uma regional (por exemplo, o Campus Samambaia). Entidade compartilhada, de dono Pessoa C. O pacote Locais, de dono Pessoa B, referencia o campus ao qual um local pertence; não o redefine.

## Entrada do dicionário de dados

| Atributo | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| id | Integer | Sim | Identificador único do campus |
| nome | String | Sim | Nome do campus, sem repetição dentro da regional |
| idRegional | Integer | Sim | Regional à qual o campus pertence (referência a `Regional.id`) |

## Relacionamentos

| Com | Multiplicidade | Significado |
|---|---|---|
| Regional | 0..* para 1 | Cada campus pertence a uma única regional |
| Local | 1 para 0..* | Um campus contém vários locais (associação com a entidade de Pessoa B, a confirmar na integração) |

## Regras e restrições

- Todo campus pertence a exatamente uma regional.
- O nome do campus é único dentro da regional.

## Premissas a confirmar

- A captura de Locais (versão 3.2.0) mostra o título "Campus Samambaia" sobre a lista de locais (restaurantes, Instituto de Informática, laboratórios, herbário), o que sustenta a associação `Campus` e `Local`. A modelagem de `Local` é da Pessoa B; a multiplicidade acima é proposta.

## Trecho PlantUML (diagrama de dados)

Classes sem atributos e sem operações, só com as associações (formato do `DDados`).

```plantuml
class Campus
class Regional
class Local
Regional "1" -- "0..*" Campus
Campus "1" -- "0..*" Local
```
