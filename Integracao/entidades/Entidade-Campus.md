# Entidade Campus

| Campo | Valor |
|---|---|
| **Entidade** | `Campus` |
| **Dono (autor)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Entregue a** | Phablo Tavares Paixão (Pessoa D), para integração no `DDados-Geral` e no `DD-Geral` |
| **Usada por** | Locais (Pessoa B); Eventos e Notícias só usam a regional |
| **Status** | Entregue para integração |
| **Conteúdo igual ao de** | `DD-Eventos-01` (Tabela 2 e associações) |

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
| Local | 1 para 0..* | Um campus contém vários locais. **A confirmar:** `Local` é entidade da Pessoa B, e a multiplicidade é proposta da Pessoa C |

## Regras e restrições

- Todo campus pertence a exatamente uma regional.
- O nome do campus é único dentro da regional.

## Premissas a confirmar

- A captura 6 (Locais, versão 3.2.0) mostra o título "Campus Samambaia" sobre a lista de locais (restaurantes, Instituto de Informática, laboratórios, herbário), o que sustenta a existência do campus e a associação com `Local`. Os demais atributos (`id`, `idRegional`) são escolha de modelagem, não observada. A modelagem de `Local` é da Pessoa B.
- Em Eventos o filtro é só por regional (aba "GOIÂNIA", capturas 19, 28 e 29); o campus aparece apenas no texto do local, na página do evento no portal (capturas 8 e 21), e por isso `Evento` não se liga a `Campus`.

## Trecho PlantUML (diagrama de dados)

Classes com atributos, como em `DD-Eventos-01`.

```plantuml
class Regional {
  id: Integer
  nome: String
}
class Campus {
  id: Integer
  nome: String
  idRegional: Integer
}
class Local <<Pessoa B>>
Regional "1" -- "0..*" Campus : agrupa >
Campus "1" -- "0..*" Local : contém >
note on link : a confirmar com a Pessoa B
```
