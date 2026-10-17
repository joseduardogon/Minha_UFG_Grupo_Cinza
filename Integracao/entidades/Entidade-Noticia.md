# Entidade Noticia

| Campo | Valor |
|---|---|
| **Entidade** | `Noticia` |
| **Dono (autor)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Entregue a** | Phablo Tavares Paixão (Pessoa D), para integração no `DDados-Geral` e no `DD-Geral` |
| **Usada por** | Notícias |
| **Status** | Entregue para integração (primeira versão) |

## Descrição

Notícia divulgada pela UFG sobre uma regional, cadastrada pelo painel web e listada no app. O app não tem tela de detalhe: tocar na notícia abre o endereço dela no Navegador.

## Entrada do dicionário de dados

| Atributo | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| id | Integer | Sim | Identificador único da notícia |
| titulo | String | Sim | Título da notícia, como exibido na lista |
| resumo | String | Não | Texto curto exibido abaixo do título no cartão da lista |
| urlImagem | String | Não | Endereço da imagem exibida no topo do cartão |
| dataPublicacao | Date | Não | Data e hora de publicação; aparece na página da notícia (ex.: "Em 15/10/26 19:42"), não no cartão da lista |
| url | String | Sim | Endereço da notícia no portal da UFG, aberto no Navegador |
| idRegional | Integer | Sim | Regional da notícia (referência a `Regional.id`) |

## Relacionamentos

| Com | Multiplicidade | Significado |
|---|---|---|
| Regional | 0..* para 1 | Cada notícia pertence a uma regional |

## Regras e restrições

- Toda notícia tem `url`, pois é por ela que o usuário lê o conteúdo.
- A lista exibida é a das notícias da regional selecionada.

## Premissas a confirmar

- Confirmado nas capturas (versão 3.2.0): o cartão mostra imagem, título e resumo; a data não aparece na lista. Falta confirmar a ordem da lista e quais regionais existem (premissas `P-NO-n`, em `Noticias/README.md`).

## Trecho PlantUML (diagrama de dados)

Classes sem atributos e sem operações, só com as associações (formato do `DDados`).

```plantuml
class Noticia
class Regional
Regional "1" -- "0..*" Noticia
```
