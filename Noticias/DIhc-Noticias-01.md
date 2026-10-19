# DIhc-Noticias-01 – Protótipo da tela Notícias

| Campo | Valor |
|---|---|
| **Código** | `DIhc-Noticias-01` |
| **Título** | Protótipo da tela Notícias |
| **Autor(a)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Revisor(a)** | Phablo Tavares Paixão (Pessoa D) |
| **Status** | Em produção (primeira versão) |
| **Rastreia para** | `DCdu-Noticias-01`, `DAtv-Noticias-01`, `DAtv-Noticias-02` |

## Diagrama

![DIhc-Noticias-01](DIhc-Noticias-01.png)

Fonte: [`DIhc-Noticias-01.puml`](DIhc-Noticias-01.puml)

## Descrição

Protótipo da tela Notícias em PlantUML Salt, conforme a captura de tela da versão 3.2.0: abaixo do título, uma faixa de abas de regional (na captura, "GOIÂNIA" selecionada) e, abaixo, a lista de notícias, cada uma em um cartão com imagem, título e resumo curto. Os dados do desenho são ilustrativos. Não há tela de detalhe: tocar em uma notícia abre a página dela no Navegador. Os rótulos `(E0)` a `(E2)` identificam os eventos de interação.

**Tabela 1 – Eventos de interação da tela**

| Rótulo | Elemento | Gesto | Efeito | Atividade |
|---|---|---|---|---|
| E0 | Tela (ao ser exibida) | Entrada na tela | Seleciona a primeira aba de regional e carrega as notícias | `DAtv-Noticias-01`, A1 |
| E1 | Aba de regional | Toque | Seleciona a regional e recarrega a lista | `DAtv-Noticias-01`, A2 |
| E2 | Cartão de notícia | Toque | Abre a página da notícia no Navegador | `DAtv-Noticias-02`, A1 |

Os diagramas de estados (`DEst-Noticias-01`) serão produzidos junto com os de classes.

As premissas `P-NO-n` citadas estão listadas, com o que as capturas de tela do app (versão 3.2.0) confirmaram e o que falta confirmar, em [`Noticias/README.md`](README.md).

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 11 (Software Engineering Models and Methods). IEEE, 2024.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
