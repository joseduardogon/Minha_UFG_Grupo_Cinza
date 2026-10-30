# Entidade Regional

| Campo | Valor |
|---|---|
| **Entidade** | `Regional` |
| **Dono (autor)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Entregue a** | Phablo Tavares Paixão (Pessoa D), para integração no `DDados-Geral` e no `DD-Geral` |
| **Usada por** | Eventos, Notícias e Locais (via Campus) |
| **Status** | Entregue para integração |
| **Conteúdo igual ao de** | `DD-Eventos-01` (Tabela 1 e associações) |

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
| Noticia | 1 para 0..* | Uma regional tem várias notícias (associação descrita no DD de Notícias) |

## Regras e restrições

- O nome da regional é único.
- Uma regional pode existir sem campi, eventos ou notícias.

## Premissas a confirmar

- Em Eventos, como em Notícias (capturas 5 e 11), a regional é escolhida em abas, e a única visível é "GOIÂNIA", selecionada ao abrir (capturas 19, 28 e 29, versão 3.2.0). A faixa de abas some quando não há eventos (captura 29). Falta confirmar quais outras regionais existem e como se chamam, se a lista é fixa no app e se Eventos e Notícias usam a mesma lista (P-EV-2, `Eventos/README.md`).
- Localização da entidade no `DPac-Geral-01`: pendência da integração (`D-INT-03`). Proposta da Pessoa C: manter `Regional` e `Campus` no pacote `Comum`, já que três pacotes de funcionalidade as usam e o `DPac-Geral-01` não permite dependência entre pacotes de funcionalidade.

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
class Evento {
  id: Integer
  titulo: String
  dataInicio: Date
  dataFim: Date
  url: String [0..1]
  urlImagem: String [0..1]
  idRegional: Integer
}
class Noticia
Regional "1" -- "0..*" Campus : agrupa >
Regional "1" -- "0..*" Evento : promove >
Regional "1" -- "0..*" Noticia
```
