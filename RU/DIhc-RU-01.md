# DIhc-RU-01 – Protótipo da tela RU (escolha da refeição)

| Campo | Valor |
|---|---|
| **Código** | `DIhc-RU-01` |
| **Título** | Protótipo da tela RU (escolha da refeição) |
| **Autor(a)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Revisor(a)** | Phablo Tavares Paixão (Pessoa D) |
| **Status** | Em produção (primeira versão) |
| **Rastreia para** | `DCdu-RU-01`, `DAtv-RU-01`, `DIhc-RU-02` |

## Diagrama

![DIhc-RU-01](DIhc-RU-01.png)

Fonte: [`DIhc-RU-01.puml`](DIhc-RU-01.puml)

## Descrição

Protótipo da tela RU em PlantUML Salt, conforme a captura de tela da versão 3.2.0: um cartão com imagem para cada refeição (Café da Manhã, Almoço e Jantar) e o aviso "Cardápio sujeito a alterações!" no fim. A tela é estática. O rótulo `(E1)` identifica o evento de interação.

**Tabela 1 – Eventos de interação da tela**

| Rótulo | Elemento | Gesto | Efeito | Atividade |
|---|---|---|---|---|
| E1 | Cartão de uma refeição | Toque | Abre a tela da refeição escolhida (`DIhc-RU-02`) e carrega o cardápio de hoje | `DAtv-RU-01`, A1 |

Os diagramas de estados (`DEst-RU-01`) serão produzidos junto com os de classes.

As premissas `P-RU-n` citadas estão listadas, com o que as capturas de tela do app (versão 3.2.0) confirmaram e o que falta confirmar, em [`RU/README.md`](README.md).

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 11 (Software Engineering Models and Methods). IEEE, 2024.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
