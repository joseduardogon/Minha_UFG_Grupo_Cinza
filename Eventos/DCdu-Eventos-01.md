# DCdu-Eventos-01 – Casos de uso da funcionalidade Eventos

| Campo | Valor |
|---|---|
| **Código** | `DCdu-Eventos-01` |
| **Título** | Casos de uso da funcionalidade Eventos |
| **Autor(a)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Revisor(a)** | Phablo Tavares Paixão (Pessoa D) |
| **Status** | Em produção (primeira versão) |
| **Rastreia para** | `DCdu-Geral-01`, `DAtv-Eventos-01`, `DAtv-Eventos-02`, `DAtv-Eventos-03`, `DIhc-Eventos-01` |

## Diagrama

![DCdu-Eventos-01](DCdu-Eventos-01.png)

Fonte: [`DCdu-Eventos-01.puml`](DCdu-Eventos-01.puml)

## Descrição

Detalha o caso de uso macro "Consultar eventos" do `DCdu-Geral-01` em três casos de uso, um por objetivo do usuário. O único ator primário é o Membro da comunidade UFG (anônimo). Os atores secundários são o Servidor/API, que fornece os eventos cadastrados pelo painel web, e o Navegador, que abre a página de um evento. A abertura do Navegador é feita pelo componente `LinkExterno` do pacote Comum (`DCla-Comum-01`).

**Tabela 1 – Casos de uso de Eventos**

| Código | Caso de uso | Objetivo do usuário | Atores secundários |
|---|---|---|---|
| UC-EV-01 | Consultar eventos por regional e data | Ver os eventos de uma regional que acontecem em uma data | Servidor/API |
| UC-EV-02 | Trocar o mês do calendário | Navegar para o mês anterior ou o seguinte | Servidor/API |
| UC-EV-03 | Abrir a página do evento | Ler os detalhes do evento no site da UFG | Navegador |

**UC-EV-01 – Consultar eventos por regional e data**

- *Pré-condição:* o usuário tocou no cartão Eventos do menu inicial.
- *Fluxo principal:* (1) o app exibe o calendário do mês atual, com a data de hoje selecionada e a regional inicial escolhida (P-EV-2, P-EV-6); (2) o app pede ao servidor os eventos da regional e da data selecionadas; (3) o app lista os eventos; (4) o usuário pode escolher outra data ou outra regional, e o fluxo volta ao passo 2.
- *Fluxos alternativos:* **A1** não há eventos na data: o app mostra a mensagem de "sem eventos"; **A2** sem internet ou servidor indisponível: o app mostra a mensagem de indisponibilidade (estados em `DEst-Comum-01`); **A3** evento com intervalo de datas: aparece em todas as datas do intervalo, do início ao fim.
- *Pós-condição:* a tela mostra o resultado da consulta da regional e da data selecionadas.

**UC-EV-02 – Trocar o mês do calendário**

- *Pré-condição:* a tela Eventos está exibida.
- *Fluxo principal:* (1) o usuário toca na seta de mês anterior ou seguinte; (2) o app exibe o novo mês e seleciona o primeiro dia dele (P-EV-3); (3) o app consulta os eventos como no passo 2 do UC-EV-01.
- *Fluxos alternativos:* os mesmos A1 e A2 do UC-EV-01.

**UC-EV-03 – Abrir a página do evento**

- *Pré-condição:* a lista exibe ao menos um evento.
- *Fluxo principal:* (1) o usuário toca em um evento; (2) o app pede ao Navegador que abra o endereço do evento (P-EV-4); (3) o Navegador exibe a página.
- *Fluxos alternativos:* **A1** evento sem endereço: o app não reage ao toque; **A2** endereço inválido ou nenhum navegador disponível: o app atual não mostra mensagem (`ResultadoAbertura`, `DCla-Comum-01`).
- *Pós-condição:* ao voltar ao app, a tela recarrega os eventos, pois o app não guarda cache (`DEst-Comum-01`).

As premissas `P-EV-n` citadas estão listadas, com o que falta confirmar nas capturas de tela do app, em [`Eventos/README.md`](README.md).

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 11 (Software Engineering Models and Methods). IEEE, 2024.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
