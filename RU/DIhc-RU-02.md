# DIhc-RU-02 – Protótipo da tela da refeição (cardápio do dia)

| Campo | Valor |
|---|---|
| **Código** | `DIhc-RU-02` |
| **Título** | Protótipo da tela da refeição (cardápio do dia) |
| **Autor(a)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Revisor(a)** | Phablo Tavares Paixão (Pessoa D) |
| **Status** | Em produção (primeira versão) |
| **Rastreia para** | `DCdu-RU-01`, `DAtv-RU-01`, `DAtv-RU-02`, `DIhc-RU-01` |

## Diagrama

![DIhc-RU-02](DIhc-RU-02.png)

Fonte: [`DIhc-RU-02.puml`](DIhc-RU-02.puml)

## Descrição

Protótipo da tela de uma refeição (exemplo: Café da Manhã), conforme a captura de tela da versão 3.2.0: a data por extenso no topo, os itens em cartões por categoria e, na lateral esquerda, o seletor de dia da semana com as letras S, T, Q, Q, S, S (segunda a sábado), com o dia escolhido destacado. Os itens do desenho são os da captura (sexta-feira, 16 de outubro de 2026). Os rótulos `(E0)` e `(E1)` identificam os eventos de interação.

**Tabela 1 – Eventos de interação da tela**

| Rótulo | Elemento | Gesto | Efeito | Atividade |
|---|---|---|---|---|
| E0 | Tela (ao ser exibida) | Entrada na tela | Seleciona hoje e carrega o cardápio da refeição | `DAtv-RU-01`, A1 |
| E1 | Letra do seletor de dia | Toque | Destaca o dia, atualiza a data e recarrega o cardápio | `DAtv-RU-02`, A1 |

Ao entrar na tela o app sempre recarrega o cardápio, pois não guarda cache. As categorias dependem da refeição (P-RU-5). Os diagramas de estados (`DEst-RU-02`) serão produzidos junto com os de classes.

As premissas `P-RU-n` citadas estão listadas, com o que as capturas de tela do app (versão 3.2.0) confirmaram e o que falta confirmar, em [`RU/README.md`](README.md).

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 11 (Software Engineering Models and Methods). IEEE, 2024.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
