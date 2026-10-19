# DEst-Eventos-01 – Estados da tela Eventos

| Campo | Valor |
|---|---|
| **Código** | `DEst-Eventos-01` |
| **Título** | Estados da tela Eventos |
| **Autor(a)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Revisor(a)** | Phablo Tavares Paixão (Pessoa D) |
| **Status** | Em produção (primeira versão) |
| **Rastreia para** | `DIhc-Eventos-01`, `DEst-Comum-01`, `DCla-Comum-03`, `DSeq-Eventos-01`, `DSeq-Eventos-05` |

## Diagrama

![DEst-Eventos-01](DEst-Eventos-01.png)

Fonte: [`DEst-Eventos-01.puml`](DEst-Eventos-01.puml)

## Descrição

Especifica como a tela Eventos reage a cada evento de interação do protótipo (`DIhc-Eventos-01`). Os estados Carregando, Exibindo, Vazio e Indisponível são os do ciclo genérico de `DEst-Comum-01`; aqui, Exibindo, Vazio e Indisponível ficam reunidos no estado composto `Resultado`. A tela de Eventos acrescenta:

- as ações que levam a nova carga: **E1** escolher regional, **E2** e **E3** trocar o mês e **E4** escolher data. Todas saem de qualquer estado de resultado e levam a Carregando, pois o filtro mudou;
- o estado **Fora do app**: ao tocar em um evento com endereço (**E5**), o Navegador é aberto e o app fica em segundo plano. Ao voltar, o evento `aoEntrarNaTela` leva a Carregando, e os dados são buscados de novo (sem cache). Um toque em evento sem endereço não muda de estado.

**Tabela 1 – Transições da tela Eventos**

| Origem | Evento | Condição | Destino |
|---|---|---|---|
| (início) | `aoEntrarNaTela` (E0) | – | Carregando |
| Carregando | carga concluída | há eventos | Exibindo |
| Carregando | carga concluída | não há eventos | Vazio |
| Carregando | `ErroApi` | qualquer tipo | Indisponível |
| Resultado (Exibindo, Vazio ou Indisponível) | E1, E2, E3 ou E4 | – | Carregando |
| Resultado | `aoEntrarNaTela` | – | Carregando |
| Exibindo | E5 | o evento tem URL | Fora do app |
| Exibindo | E5 | o evento não tem URL | Exibindo |
| Fora do app | `aoEntrarNaTela` (voltar ao app) | – | Carregando |
| Resultado ou Fora do app | sair da tela | – | (fim) |

As premissas `P-EV-n` citadas estão listadas, com o que falta confirmar nas capturas de tela do app, em [`Eventos/README.md`](README.md).

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 11 (Software Engineering Models and Methods). IEEE, 2024.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
