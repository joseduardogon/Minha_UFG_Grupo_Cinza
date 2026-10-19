# Entidade Regional

| Campo | Valor |
|---|---|
| **Entidade** | `Regional` |
| **Dono (autor)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Entregue a** | Phablo Tavares Paixão (Pessoa D), para integração no `DDados-Geral` e no `DD-Geral` |
| **Usada por** | Eventos, Notícias e Locais (via Campus) |
| **Status** | Entregue para integração (primeira versão) |

## Descrição

Divisão administrativa da UFG que agrupa campi e à qual pertencem eventos e notícias (por exemplo, a Regional Goiânia). É a base do filtro "por regional" de Eventos e Notícias. Entidade compartilhada, de dono Pessoa C (contrato-base, seção 7).

## Entrada do dicionário de dados

| Atributo | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| id | Integer | Sim | Identificador único da regional |
| nome | String | Sim | Nome da regional, sem repetição |

## Relacionamentos

| Com | Multiplicidade | Significado |
|---|---|---|
| Campus | 1 para 0..* | Uma regional tem vários campi |
| Evento | 1 para 0..* | Uma regional tem vários eventos |
| Noticia | 1 para 0..* | Uma regional tem várias notícias |

## Regras e restrições

- O nome da regional é único.
- Uma regional pode existir sem campi, eventos ou notícias.

## Premissas a confirmar

- Na captura de Notícias (versão 3.2.0) a regional aparece como aba, e a única visível é "GOIÂNIA". Falta confirmar quais outras regionais existem e como se chamam (a faixa de abas de Notícias com outras regionais e a tela de Eventos).
- Localização da entidade no `DPac-Geral-01`: pendência da integração (`D-INT-03`). Proposta da Pessoa C: manter `Regional` e `Campus` no pacote `Comum`, já que três pacotes de funcionalidade as usam e o `DPac-Geral-01` não permite dependência entre pacotes de funcionalidade.

## Trecho PlantUML (diagrama de dados)

Classes sem atributos e sem operações, só com as associações (formato do `DDados`).

```plantuml
class Regional
class Campus
class Evento
class Noticia
Regional "1" -- "0..*" Campus
Regional "1" -- "0..*" Evento
Regional "1" -- "0..*" Noticia
```
