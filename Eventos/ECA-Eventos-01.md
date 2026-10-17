# ECA-Eventos-01 – Regras ativas (evento-condição-ação) do pacote Eventos

| Campo | Valor |
|---|---|
| **Código** | `ECA-Eventos-01` |
| **Título** | Regras ativas (evento-condição-ação) do pacote Eventos |
| **Autor(a)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Revisor(a)** | Phablo Tavares Paixão (Pessoa D) |
| **Status** | Em produção (primeira versão) |
| **Rastreia para** | `DCla-Eventos-01`, `DEst-Eventos-01`, `DEst-Comum-01`, `Contrato-Eventos-01` |

## Descrição

Regras ativas são reações automáticas do sistema: quando acontece um **evento**, se uma **condição** é verdadeira, executa-se uma **ação**. A funcionalidade Eventos tem três regras, todas sobre as classes `TelaEventos` e `CalendarioEventos`. Elas explicam por que a lista sempre mostra os dados do filtro atual e nunca fica desatualizada.

**Tabela 1 – Regras E-C-A de Eventos**

| Código | Evento | Condição | Ação | Classe |
|---|---|---|---|---|
| ECA-EV-01 | O usuário troca o mês do calendário | Sempre | Seleciona o primeiro dia do novo mês (P-EV-3) e recarrega os eventos | `TelaEventos` e `CalendarioEventos` |
| ECA-EV-02 | O usuário escolhe outra data ou outra regional | Sempre | Recarrega os eventos com o novo filtro | `TelaEventos` |
| ECA-EV-03 | A tela volta a ser exibida (inclusive ao retornar do Navegador) | Sempre (o app não guarda cache) | Carrega os eventos de novo e volta ao estado Carregando | `TelaEventos` |

As regras ECA-EV-01 a ECA-EV-03 correspondem às transições da Tabela 1 de `DEst-Eventos-01`. Não há regra ativa para falhas de comunicação: o tratamento de `ErroApi` é comum a todas as telas e está em `DEst-Comum-01`.

As premissas `P-EV-n` citadas estão listadas, com o que falta confirmar nas capturas de tela do app, em [`Eventos/README.md`](README.md).

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 11 (Software Engineering Models and Methods). IEEE, 2024.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
