# Entidade Evento

| Campo | Valor |
|---|---|
| **Entidade** | `Evento` |
| **Dono (autor)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Entregue a** | Phablo Tavares Paixão (Pessoa D), para integração no `DDados-Geral` e no `DD-Geral` |
| **Usada por** | Eventos (`DCla-Eventos-02`) |
| **Status** | Entregue para integração |
| **Conteúdo igual ao de** | `DD-Eventos-01` (Tabela 3 e associações) |

## Descrição

Acontecimento divulgado pela UFG, cadastrado pelo painel web e consultado no app por regional e por data. Pode durar mais de um dia (data de início e data de fim), pode ter uma imagem e pode ter o endereço de uma página com detalhes. O cartão do evento na lista mostra a miniatura, o título e o período (capturas 19 e 28; P-EV-1).

## Entrada do dicionário de dados

| Atributo | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| id | Integer | Sim | Identificador único do evento |
| titulo | String | Sim | Nome do evento, como exibido na lista |
| dataInicio | Date | Sim | Primeiro dia do evento |
| dataFim | Date | Sim | Último dia do evento; igual a `dataInicio` se o evento dura um dia |
| url | String | Não | Endereço da página do evento, aberto no Navegador ao tocar no item; sem `url`, o toque não tem efeito (P-EV-4) |
| urlImagem | String | Não | Endereço da imagem do evento, mostrada como miniatura circular no cartão da lista (P-EV-5: o formato do dado vem da API) |
| idRegional | Integer | Sim | Regional do evento (referência a `Regional.id`) |

## Relacionamentos

| Com | Multiplicidade | Significado |
|---|---|---|
| Regional | 0..* para 1 | Cada evento pertence a uma regional |

## Regras e restrições

- `dataFim` é igual ou posterior a `dataInicio`.
- O evento aparece na consulta de toda data entre `dataInicio` e `dataFim`, inclusive (observado nas capturas 19 e 28: um evento de 30/09/2026 a 14/12/2026 aparece em 30/10 e em 30/11; P-EV-9).
- Sem `url`, o toque no evento no app não tem efeito.

## Premissas a confirmar

- **O local do evento não é atributo.** A página do evento no portal da UFG, aberta no Navegador, mostra o título, o local e o período: "Local: Centro de Línguas, Câmpus Samambaia" e "15 a 17 de Outubro 2026" (captura 8); "Local: Biblioteca Seccional Cepae Prof. Geraldo Faria Campos, Campus Samambaia" e "19 a 30 de Outubro 2026" (captura 21), versão 3.2.0. O cartão da lista não mostra local nem horário (capturas 19 e 28).
- **`urlImagem`.** O cartão mostra uma miniatura circular em todos os eventos vistos; como a tela precisa de um dado de onde tirar a imagem, o atributo foi acrescentado. É opcional porque não se sabe se todo evento tem imagem nem o que o cartão mostra sem ela.
- Da lista foram observados a miniatura, o título e o período (P-EV-1); da interação, só a página já aberta no Navegador (capturas 8 e 21). O toque no cartão e o caso sem endereço são a premissa P-EV-4, pendente (`Eventos/README.md`).

## Trecho PlantUML (diagrama de dados)

Classes com atributos, como em `DD-Eventos-01`.

```plantuml
class Regional {
  id: Integer
  nome: String
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
Regional "1" -- "0..*" Evento : promove >
```
