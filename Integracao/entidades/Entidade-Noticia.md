# Entidade Noticia

| Campo | Valor |
|---|---|
| **Entidade** | `Noticia` |
| **Dono (autor)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Entregue a** | Phablo Tavares Paixão (Pessoa D), para integração no `DDados-Geral` e no `DD-Geral` |
| **Usada por** | Notícias (`DCla-Noticias-02`, `DD-Noticias-01`) |
| **Status** | Entregue para integração (primeira versão) |

## Descrição

Notícia divulgada pela UFG sobre uma regional, cadastrada pelo painel web e listada no app, em um cartão com imagem de banner, título e resumo. O app não tem tela de detalhe: tocar na notícia abre o endereço dela no Navegador. A lista da tela é a das notícias da regional selecionada, na ordem em que a API devolve.

## Entrada do dicionário de dados

| Atributo | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| id | Integer | Sim | Identificador único da notícia |
| titulo | String | Sim | Título da notícia, como exibido em negrito no cartão |
| resumo | String | Não | Texto curto exibido abaixo do título no cartão |
| urlImagem | String | Não | Endereço da imagem de banner exibida no topo do cartão |
| url | String | Sim | Endereço da notícia no portal da UFG, aberto no Navegador |
| idRegional | Integer | Sim | Regional da notícia (referência a `Regional.id`) |

## Relacionamentos

| Com | Multiplicidade | Significado |
|---|---|---|
| Regional | 0..* para 1 | Cada notícia pertence a uma regional |

## Regras e restrições

- Toda notícia tem `url`, pois é por ela que o usuário lê o conteúdo; `titulo` não é vazio.
- A lista exibida é a das notícias da regional selecionada.
- A data e a hora de publicação não fazem parte da entidade: aparecem só na página da notícia no portal da UFG (ex.: "Em 29/10/26 18:18."), não no cartão da lista. Os créditos "Texto:" e "Foto de capa:" da página do portal também ficam fora da entidade.

## Premissas a confirmar

- Confirmado nas capturas (versão 3.2.0, P-NO-3): o cartão mostra imagem de banner, título e resumo; a data não aparece na lista, só na página aberta no Navegador (capturas 12 e 20; o toque em si não foi capturado, só o resultado). Falta confirmar a ordem da lista (P-NO-5) e quais regionais existem (P-NO-6); a rota `/noticias` é premissa de projeto (P-NO-4). As premissas `P-NO-n` estão em `Noticias/README.md`.

## Trecho PlantUML (diagrama de dados)

Classes sem atributos e sem operações, só com as associações (formato do `DDados`).

```plantuml
class Noticia
class Regional
Regional "1" -- "0..*" Noticia
```
