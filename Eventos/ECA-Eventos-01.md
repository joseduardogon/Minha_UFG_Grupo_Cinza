# ECA-Eventos-01 – Regras ativas (evento-condição-ação) do pacote Eventos

| Campo | Valor |
|---|---|
| **Código** | `ECA-Eventos-01` |
| **Título** | Regras ativas (evento-condição-ação) do pacote Eventos |
| **Autor(a)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Revisor(a)** | Phablo Tavares Paixão (Pessoa D) |
| **Status** | Em produção |
| **Rastreia para** | `DCla-Eventos-01`, `DEst-Eventos-01`, `DEst-Comum-01`, `Contrato-Eventos-01`, `ECA-Comum-01` |

## Descrição

Regras ativas são reações automáticas do sistema: quando acontece um **evento**, se uma **condição** é verdadeira, executa-se uma **ação**. A funcionalidade Eventos tem quatro regras, todas sobre as classes `TelaEventos` e `CalendarioEventos`. Elas explicam por que a lista sempre mostra os dados do filtro atual e nunca fica desatualizada. Correspondem às transições de `DEst-Eventos-01`.

**Tabela 1 – Regras E-C-A de Eventos**

| Código | Evento | Condição | Ação | Classe |
|---|---|---|---|---|
| ECA-EV-01 | O usuário troca o mês do calendário | Sempre | Mantém o número do dia selecionado no novo mês (ajustado ao último dia, se o mês novo for mais curto) e recarrega os eventos (P-EV-7, P-EV-8) | `TelaEventos` e `CalendarioEventos` |
| ECA-EV-02 | O usuário escolhe outra data (P-EV-12) ou outra regional (P-EV-2) | Sempre. A troca de regional só ocorre com a lista exibida, pois a aba de regional some no estado sem eventos | Recarrega os eventos com o novo filtro | `TelaEventos` |
| ECA-EV-03 | A tela volta a ser exibida (entrada pelo menu ou retorno do Navegador) | Sempre (o app não guarda cache) | Carrega os eventos de novo e volta ao estado Carregando. É a especialização de `ECA-CM-01` (`ECA-Comum-01`) para Eventos: no retorno o filtro é mantido, e só na entrada pelo menu ele é reiniciado | `TelaEventos` |
| ECA-EV-04 | O usuário sai da tela Eventos pela seta de voltar | Sempre | Encerra a tela e descarta o estado do filtro e os eventos em memória; uma nova entrada cria o filtro de novo | `TelaEventos` |

A regra ECA-EV-04 é análoga à `ECA-RA-03` da Rádio (`ECA-Radio-01`). As regras ECA-EV-01 a ECA-EV-04 correspondem às transições da Tabela 1 de `DEst-Eventos-01`. Não há regra ativa para falhas de comunicação: o tratamento de `ErroApi` é comum a todas as telas e está em `DEst-Comum-01` e em `ECA-Comum-01`.

A regra ECA-EV-01 corrige a premissa antiga de selecionar o dia 1 ao trocar o mês, refutada pelas capturas 19, 28 e 29 (o dia 30 se mantém). A situação das premissas P-EV-2, P-EV-7, P-EV-8 e P-EV-12 está na tabela de [`Eventos/README.md`](README.md).

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 11 (Software Engineering Models and Methods). IEEE, 2024.

ANTHROPIC. **Claude Code**. Assistente de IA. Disponível em: claude.ai/code. Acesso em: 30 out. 2026. Uso: apoio à redação e aos diagramas, a partir das instruções, das capturas de tela e das correções do autor (resumo em `IA/registro-C.md`). Questão: Apêndice <X>, Seção <X.1>.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
