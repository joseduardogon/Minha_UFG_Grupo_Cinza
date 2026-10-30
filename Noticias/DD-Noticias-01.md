# DD-Noticias-01 – Entrada de DD de Notícias

| Campo | Valor |
|---|---|
| **Código** | `DD-Noticias-01` |
| **Título** | Entrada de DD de Notícias |
| **Autor(a)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Revisor(a)** | Phablo Tavares Paixão (Pessoa D) |
| **Status** | Em produção |
| **Rastreia para** | `DCla-Noticias-02`, `DCdu-Noticias-01`, `DD-Eventos-01`, `DD-Geral-01`, `DDados-Geral-01` |

## Descrição

Entidade de Notícias, para o DD consolidado (`DD-Geral-01`) e o modelo de dados integrado (`DDados-Geral-01`). Dono: Pessoa C. A mesma entrada está na ficha de entrega [`Entidade-Noticia`](../Integracao/entidades/Entidade-Noticia.md).

Notícia divulgada pela UFG sobre uma regional, cadastrada pelo painel web e listada no app, em um cartão com imagem de banner, título e resumo (P-NO-3). O app não tem tela de detalhe: tocar na notícia abre o endereço dela no Navegador. A lista da tela é a das notícias da regional selecionada, na ordem em que a API devolve (P-NO-5).

**Tabela 1 – Noticia**: notícia exibida na lista de Notícias.

| Atributo | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| id | Integer | Sim | Identificador único da notícia |
| titulo | String | Sim | Título da notícia, como exibido em negrito no cartão |
| resumo | String | Não | Texto curto exibido abaixo do título no cartão |
| urlImagem | String | Não | Endereço da imagem de banner exibida no topo do cartão |
| url | String | Sim | Endereço da notícia no portal da UFG, aberto no Navegador |
| idRegional | Integer | Sim | Regional da notícia (referência a `Regional.id`) |

**Associações:** Regional 1 — 0..* Noticia ("publica"). A entidade `Regional` (id, nome) é de dono C, compartilhada com Eventos e Locais, e tem a sua entrada em `DD-Eventos-01`; aqui ela só é referenciada.

**Regras e restrições:** toda notícia tem `url`, pois é por ela que o usuário lê o conteúdo; `titulo` não é vazio.

Fora do DD:
- a data e a hora de publicação: aparecem só na página da notícia no portal da UFG (capturas 12 e 20 da versão 3.2.0, ex.: "Em 29/10/26 18:18."), não no cartão da lista, e portanto não fazem parte do que o app recebe nem exibe; por isso a entidade não tem `dataPublicacao`;
- os créditos "Texto:" e "Foto de capa:", vistos só na página do portal (captura 20): ficam fora do modelo do app;
- a lista de regionais da tela: é fixa no app (`regionaisOferecidas`, `DCla-Noticias-01`, P-NO-6), não vem do servidor.

Trecho PlantUML:

```plantuml
class Noticia {
  id: Integer
  titulo: String
  resumo: String
  urlImagem: String
  url: String
  idRegional: Integer
}
class Regional <<DD-Eventos-01>>
Regional "1" -- "0..*" Noticia : publica >
```

As premissas P-NO-3, P-NO-5 e P-NO-6 estão na tabela de [`Noticias/README.md`](README.md), com o que as capturas de tela do app (versão 3.2.0) confirmaram e o que falta confirmar.

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 11 (Software Engineering Models and Methods). IEEE, 2024.

ANTHROPIC. **Claude Code**. Assistente de IA. Disponível em: claude.ai/code. Acesso em: 30 out. 2026. Uso: apoio à redação e aos diagramas, a partir das instruções, das capturas de tela e das correções do autor (resumo em `IA/registro-C.md`). Questão: Apêndice <X>, Seção <X.1>.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
