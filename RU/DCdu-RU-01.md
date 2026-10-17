# DCdu-RU-01 – Casos de uso da funcionalidade Restaurante Universitário

| Campo | Valor |
|---|---|
| **Código** | `DCdu-RU-01` |
| **Título** | Casos de uso da funcionalidade Restaurante Universitário |
| **Autor(a)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Revisor(a)** | Phablo Tavares Paixão (Pessoa D) |
| **Status** | Em produção (primeira versão) |
| **Rastreia para** | `DCdu-Geral-01`, `DAtv-RU-01`, `DAtv-RU-02`, `DIhc-RU-01`, `DIhc-RU-02` |

## Diagrama

![DCdu-RU-01](DCdu-RU-01.png)

Fonte: [`DCdu-RU-01.puml`](DCdu-RU-01.puml)

## Descrição

Detalha o caso de uso macro "Consultar cardápio do RU" do `DCdu-Geral-01` em dois casos de uso. O ator primário é o Membro da comunidade UFG (anônimo) e o ator secundário é o Servidor/API, que fornece o cardápio cadastrado pelo painel web. O cardápio é único para todos os restaurantes da UFG, por isso o app não pede a escolha de restaurante nem de regional.

O app tem duas telas nesta funcionalidade (capturas de tela da versão 3.2.0): a tela **RU**, com um cartão para cada refeição (Café da Manhã, Almoço e Jantar) e o aviso "Cardápio sujeito a alterações!", e a tela da **refeição escolhida**, que mostra a data por extenso, os itens do cardápio em cartões por categoria e, na lateral esquerda, o seletor de dia da semana (letras S, T, Q, Q, S, S, de segunda a sábado).

**Tabela 1 – Casos de uso de RU**

| Código | Caso de uso | Objetivo do usuário | Ator secundário |
|---|---|---|---|
| UC-RU-01 | Consultar o cardápio de uma refeição | Ver o que será servido em uma refeição no dia de hoje | Servidor/API |
| UC-RU-02 | Escolher o dia da semana | Ver o cardápio da mesma refeição em outro dia da semana | Servidor/API |

**UC-RU-01 – Consultar o cardápio de uma refeição**

- *Pré-condição:* o usuário tocou no cartão RU do menu inicial.
- *Fluxo principal:* (1) o app mostra os três cartões de refeição e o aviso de que o cardápio está sujeito a alterações; (2) o usuário toca no cartão de uma refeição; (3) o app abre a tela da refeição, com o dia de hoje selecionado e a data por extenso no topo (P-RU-2); (4) o app pede ao servidor o cardápio da refeição e da data (P-RU-6); (5) o app mostra um cartão para cada categoria de item, com o nome da categoria e a descrição dos itens (P-RU-5).
- *Fluxos alternativos:* **A1** não há itens cadastrados para a refeição na data: o app mostra a mensagem de vazio; **A2** sem internet ou servidor indisponível: o app mostra a mensagem de indisponibilidade (`DEst-Comum-01`); **A3** jantar aos sábados: não há jantar, e o comportamento da tela não aparece nas capturas (P-RU-3).
- *Pós-condição:* a tela mostra o cardápio da refeição escolhida no dia de hoje.

**UC-RU-02 – Escolher o dia da semana**

- *Pré-condição:* a tela de uma refeição está exibida.
- *Fluxo principal:* (1) o usuário toca em uma letra do seletor de dia; (2) o app destaca o dia escolhido e atualiza a data por extenso para o dia escolhido na semana atual (P-RU-4); (3) o app pede ao servidor o cardápio da refeição na nova data e o mostra, como nos passos 4 e 5 do UC-RU-01.
- *Fluxos alternativos:* os mesmos A1 a A3 do UC-RU-01.

As premissas `P-RU-n` citadas estão listadas, com o que as capturas de tela do app (versão 3.2.0) confirmaram e o que falta confirmar, em [`RU/README.md`](README.md).

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 11 (Software Engineering Models and Methods). IEEE, 2024.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
