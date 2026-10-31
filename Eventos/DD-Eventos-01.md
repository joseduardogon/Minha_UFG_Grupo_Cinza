# DD-Eventos-01 – Entrada de DD de Eventos

| Campo | Valor |
|---|---|
| **Código** | `DD-Eventos-01` |
| **Título** | Entrada de DD de Eventos |
| **Autor(a)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Revisor(a)** | Phablo Tavares Paixão (Pessoa D) |
| **Status** | Em produção |
| **Rastreia para** | `DCla-Eventos-01`, `DCla-Eventos-02`, `DCdu-Eventos-01`, `DD-Geral-01`, `DDados-Geral-01` |

## Descrição

Entidades de Eventos, para o DD consolidado (`DD-Geral-01`) e o modelo de dados integrado (`DDados-Geral-01`): **Regional**, **Campus** e **Evento**. Dono das três: Pessoa C (contrato-base, seção 7). `Regional` e `Campus` são compartilhadas: `Regional` é usada também por Notícias e, via `Campus`, por Locais (Pessoa B). A localização delas no `DPac-Geral-01` é a pendência `D-INT-03`; a proposta da Pessoa C é mantê-las no pacote `Comum` (os `DCla` de Eventos as usam como referência, estereótipo `<<Comum (proposta)>>`). As fichas de entrega a D são [`Entidade-Regional`](../Integracao/entidades/Entidade-Regional.md), [`Entidade-Campus`](../Integracao/entidades/Entidade-Campus.md) e [`Entidade-Evento`](../Integracao/entidades/Entidade-Evento.md), com o mesmo conteúdo deste item.

Um evento acontece em um período (data de início e data de fim, que podem ser iguais) e é consultado no app por regional e por data: aparece na consulta de toda data entre `dataInicio` e `dataFim`, inclusive (observado: um evento de 30/09/2026 a 14/12/2026 aparece em 30/10 e em 30/11, capturas 19 e 28; P-EV-9). Os eventos são cadastrados pelo painel web e chegam ao app pelo Servidor/API.

**Tabela 1 – Regional**: divisão administrativa da UFG que agrupa campi e à qual pertencem eventos e notícias (por exemplo, a Regional Goiânia). É a base do filtro "por regional".

| Atributo | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| id | Integer | Sim | Identificador único da regional |
| nome | String | Sim | Nome da regional, sem repetição |

**Tabela 2 – Campus**: unidade física da UFG, vinculada a uma regional (por exemplo, o Campus Samambaia). O pacote Locais, de dono Pessoa B, referencia o campus ao qual um local pertence; não o redefine. Eventos e Notícias só usam a regional.

| Atributo | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| id | Integer | Sim | Identificador único do campus |
| nome | String | Sim | Nome do campus, sem repetição dentro da regional |
| idRegional | Integer | Sim | Regional à qual o campus pertence (referência a `Regional.id`) |

**Tabela 3 – Evento**: acontecimento divulgado pela UFG, cadastrado pelo painel web e consultado no app por regional e por data. Pode durar mais de um dia, pode ter uma imagem e pode ter o endereço de uma página com detalhes. O cartão do evento na lista mostra a miniatura, o título e o período (capturas 19 e 28; P-EV-1).

| Atributo | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| id | Integer | Sim | Identificador único do evento |
| titulo | String | Sim | Nome do evento, como exibido na lista |
| dataInicio | Date | Sim | Primeiro dia do evento |
| dataFim | Date | Sim | Último dia do evento; igual a `dataInicio` se o evento dura um dia |
| url | String | Não | Endereço da página do evento, aberto no Navegador ao tocar no item; sem `url`, o toque não tem efeito (P-EV-4) |
| urlImagem | String | Não | Endereço da imagem do evento, mostrada como miniatura circular no cartão da lista (P-EV-5: o formato do dado vem da API) |
| idRegional | Integer | Sim | Regional do evento (referência a `Regional.id`) |

**Associações:**

| Entre | Multiplicidade | Significado |
|---|---|---|
| Regional e Campus | 1 — 0..* | Uma regional tem vários campi; cada campus pertence a uma única regional |
| Regional e Evento | 1 — 0..* | Uma regional tem vários eventos; cada evento pertence a uma regional |
| Regional e Noticia | 1 — 0..* | Uma regional tem várias notícias (associação descrita no DD de Notícias; aparece aqui só para completar a `Regional`) |
| Campus e Local | 1 — 0..* | Um campus contém vários locais. **A confirmar:** `Local` é entidade da Pessoa B, e a multiplicidade é proposta da Pessoa C |

**Regras e restrições:** o nome da regional é único; o nome do campus é único dentro da regional; `dataFim` é igual ou posterior a `dataInicio`; uma regional pode existir sem campi, eventos ou notícias.

**Fora do DD: o local do evento.** A página do evento no portal da UFG, aberta no Navegador, mostra o título, o local e o período: "Local: Centro de Línguas, Câmpus Samambaia" e "15 a 17 de Outubro 2026" (captura 8); "Local: Biblioteca Seccional Cepae Prof. Geraldo Faria Campos, Campus Samambaia" e "19 a 30 de Outubro 2026" (captura 21), versão 3.2.0. O cartão da lista não mostra local nem horário (capturas 19 e 28), e por isso `Evento` não tem o atributo `local`.

**Atributo `urlImagem`.** O cartão do evento mostra uma miniatura circular em todos os eventos vistos (capturas 19 e 28). Como a tela precisa de um dado de onde tirar essa imagem, o atributo foi acrescentado. É opcional porque não se sabe se todo evento tem imagem nem o que o cartão mostra sem ela.

**Premissas a confirmar:**

- Regional: em Eventos, como em Notícias, a regional é escolhida em abas, e a única visível é "GOIÂNIA", selecionada ao abrir (capturas 19, 28 e 29). A aba some quando não há eventos (captura 29). Quais outras regionais existem e como se chamam, e se a lista é fixa no app, não foi observado (P-EV-2, `Eventos/README.md`).
- Campus: a captura 6 (versão 3.2.0) mostra o título "Campus Samambaia" sobre a lista de locais (restaurantes, Instituto de Informática, laboratórios, herbário), o que sustenta a existência do campus e a associação com `Local`. Em Eventos o filtro é só por regional; o campus aparece apenas no texto do local, na página do portal (capturas 8 e 21), e por isso `Evento` não se liga a `Campus`. Os demais atributos de `Campus` (`id`, `idRegional`) são escolha de modelagem, não observada.
- Evento: da lista foram observados a miniatura, o título e o período (P-EV-1); da interação, só a página já aberta no Navegador (capturas 8 e 21). O toque no cartão e o caso sem endereço são a premissa P-EV-4, pendente.

Trecho PlantUML:

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
class Local <<Pessoa B>>
Regional "1" -- "0..*" Campus : agrupa >
Regional "1" -- "0..*" Evento : promove >
Campus "1" -- "0..*" Local : contém >
note on link : a confirmar com a Pessoa B
```

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 11 (Software Engineering Models and Methods). IEEE, 2024.

ANTHROPIC. **Claude Code**. Assistente de IA. Disponível em: claude.ai/code. Acesso em: 30 out. 2026. Uso: apoio à redação e aos diagramas, a partir das instruções, das capturas de tela e das correções do autor (resumo em `IA/registro-C.md`). Questão: Apêndice <X>, Seção <X.1>.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
