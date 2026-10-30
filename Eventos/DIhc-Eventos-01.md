# DIhc-Eventos-01 – Protótipo da tela Eventos

| Campo | Valor |
|---|---|
| **Código** | `DIhc-Eventos-01` |
| **Título** | Protótipo da tela Eventos |
| **Autor(a)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Revisor(a)** | Phablo Tavares Paixão (Pessoa D) |
| **Status** | Em produção |
| **Rastreia para** | `DCdu-Eventos-01`, `DAtv-Eventos-01`, `DAtv-Eventos-02`, `DAtv-Eventos-03`, `DEst-Eventos-01`, `DCla-Eventos-01`, `DSeq-Eventos-01`, `DSeq-Eventos-02`, `DSeq-Eventos-03`, `DSeq-Eventos-04`, `DSeq-Eventos-05` |

## Diagrama

![DIhc-Eventos-01](DIhc-Eventos-01.png)

Fonte: [`DIhc-Eventos-01.puml`](DIhc-Eventos-01.puml)

## Descrição

Protótipo da tela Eventos, desenhado em PlantUML Salt a partir das capturas da versão 3.2.0 (iPhone): a lista de Eventos em 30/10/2026 (captura 19), em novembro (captura 28) e o estado sem eventos em dezembro (captura 29). O desenho mostra, de cima para baixo:

- **Barra de título** roxa com a seta de voltar e o título "Eventos" (E6), como nas demais telas do app.
- **Cartão de calendário** roxo: setas de mês anterior (E2) e seguinte (E3), o nome do mês ("Outubro"), o ano ("2026"), o cabeçalho de dias DOM, SEG, TER, QUA, QUI, SEX, SAB e a grade do mês, com células vazias antes do dia 1 (neste mês, o dia 1 cai na quinta-feira). O **dia selecionado** (30, hoje) é marcado por um círculo branco; os dias são tocáveis (E4).
- **Aba de regional.** A regional é escolhida em **abas** (e não em lista suspensa), como em Notícias. Só a aba "GOIÂNIA" é visível, sublinhada em roxo por estar selecionada; tocar em uma aba é E1. Quais outras regionais existem e se a lista é fixa no app não foi observado (P-EV-2).
- **Cartões de evento.** Cada cartão mostra uma miniatura circular, o título e o período no formato "dd/mm/aaaa à dd/mm/aaaa" (P-EV-1). **Não mostra local nem horário**: o local só aparece na página do evento no portal (capturas 8 e 21). Um evento com intervalo é listado em todos os dias do intervalo (P-EV-9): "30/09/2026 à 14/12/2026" aparece em 30/10 (captura 19) e em 30/11 (captura 28). A ordem da lista não é conhecida (P-EV-14). O toque no cartão (E5) abre a página do evento no Navegador; só a página aberta foi observada (P-EV-4).
- **Estado sem eventos** (parte de baixo do desenho, captura 29): no lugar da lista aparecem uma ilustração, o título "Sem eventos" e o texto "Não há eventos para esse dia!" (P-EV-10). O calendário continua visível e **a aba de regional some**; por isso E1 só ocorre com a lista exibida e os eventos de calendário (E2, E3 e E4) ocorrem também no estado vazio. O estado de indisponibilidade de Eventos não foi capturado (P-EV-11).

Os dados do desenho são os das capturas: dia atual 30/10/2026 e os três primeiros cartões de outubro. Ao abrir a tela, a data selecionada é hoje (P-EV-6), que na captura 19 é o dia 30. Ao trocar o mês, o número do dia é mantido (30 de outubro, 30 de novembro, 30 de dezembro: P-EV-7); o caso de um mês mais curto que o dia não foi observado (P-EV-8). Toque em um dia do calendário não foi capturado em si, só o resultado (P-EV-12).

Os rótulos `E0` a `E6` identificam os eventos de interação, tratados em `DEst-Eventos-01`.

**Tabela 1 – Eventos de interação da tela**

| Rótulo | Elemento | Gesto | Efeito | Operação da tela | Diagrama de sequência |
|---|---|---|---|---|---|
| E0 | Tela (ao ser exibida) | Entrada na tela | Carrega os eventos de hoje na regional inicial; no retorno do Navegador, recarrega com o filtro mantido | `aoExibir()` | `DSeq-Eventos-01`, `DSeq-Eventos-05` |
| E1 | Aba de regional | Toque | Seleciona a regional e recarrega a lista; só com a lista exibida (a aba some no estado sem eventos) | `aoEscolherRegional(regional)` | `DSeq-Eventos-03` |
| E2 | Seta de mês anterior | Toque | Mostra o mês anterior, mantém o número do dia (ajustado ao último dia se o mês for mais curto) e recarrega | `aoTrocarMes(-1)` | `DSeq-Eventos-04` |
| E3 | Seta de mês seguinte | Toque | Mostra o mês seguinte, mantém o número do dia (ajustado ao último dia se o mês for mais curto) e recarrega | `aoTrocarMes(+1)` | `DSeq-Eventos-04` |
| E4 | Dia do calendário | Toque | Seleciona a data e recarrega a lista | `aoEscolherData(data)` | `DSeq-Eventos-02` |
| E5 | Cartão de evento | Toque | Abre a página do evento no Navegador, se houver endereço | `aoTocarEvento(evento)` | `DSeq-Eventos-05` |
| E6 | Seta de voltar (barra de título) | Toque | Encerra a tela, descarta o filtro e os eventos em memória e volta ao menu inicial | `aoVoltar()` | (passo trivial, sem diagrama de sequência) |

O evento E0 ocorre sempre que a tela é exibida, inclusive ao voltar do Navegador, pois o app não guarda cache. Só na entrada pelo menu inicial o filtro é reiniciado (hoje e regional inicial); no retorno do Navegador ele é mantido. Se o app consulta o servidor a cada troca de mês ou de dia, ou filtra em memória, não é observável (P-EV-13); o modelo consulta (`recarregar()`).

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 11 (Software Engineering Models and Methods). IEEE, 2024.

ANTHROPIC. **Claude Code**. Assistente de IA. Disponível em: claude.ai/code. Acesso em: 30 out. 2026. Uso: apoio à redação e aos diagramas, a partir das instruções, das capturas de tela e das correções do autor (resumo em `IA/registro-C.md`). Questão: Apêndice <X>, Seção <X.1>.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
