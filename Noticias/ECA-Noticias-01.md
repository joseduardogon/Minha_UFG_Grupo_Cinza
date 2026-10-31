# ECA-Noticias-01 – Regras ativas (evento-condição-ação) do pacote Noticias

| Campo | Valor |
|---|---|
| **Código** | `ECA-Noticias-01` |
| **Título** | Regras ativas (evento-condição-ação) do pacote Noticias |
| **Autor(a)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Revisor(a)** | Phablo Tavares Paixão (Pessoa D) |
| **Status** | Em produção |
| **Rastreia para** | `DCla-Noticias-01`, `DEst-Noticias-01`, `DEst-Comum-01`, `ECA-Comum-01`, `Contrato-Noticias-01` |

## Descrição

Regras ativas são reações automáticas do sistema: quando acontece um **evento**, se uma **condição** é verdadeira, executa-se uma **ação**. A funcionalidade Notícias tem três regras, todas sobre as classes `TelaNoticias` e `FiltroNoticias`. Elas explicam por que a lista sempre mostra as notícias da regional atual e nunca fica desatualizada.

**Tabela 1 – Regras E-C-A de Notícias**

| Código | Evento | Condição | Ação | Classe |
|---|---|---|---|---|
| ECA-NO-01 | A tela volta a ser exibida (entrada pelo menu inicial ou retorno do Navegador, depois de abrir uma notícia, P-NO-3) | Sempre (o app não guarda cache) | Carrega as notícias de novo e volta ao estado Carregando; na entrada pelo menu usa a primeira regional da lista, no retorno mantém a regional escolhida. **Especializa `ECA-CM-01`** (`ECA-Comum-01`) | `TelaNoticias` |
| ECA-NO-02 | O usuário toca em uma aba de regional | A lista está exibida (estado Exibindo), o único estado em que a faixa de abas aparece (captura 31, P-NO-1) | Seleciona a regional no filtro e recarrega as notícias | `TelaNoticias` e `FiltroNoticias` |
| ECA-NO-03 | O usuário toca na seta de voltar | Sempre | Encerra a tela e descarta o filtro, o controlador e as notícias em memória; a próxima entrada pelo menu recomeça pela primeira regional | `TelaNoticias` |

As regras ECA-NO-01 a ECA-NO-03 correspondem às transições da Tabela 1 de `DEst-Noticias-01`. Não há regra ativa para falhas de comunicação nem para lista vazia: o tratamento de `ErroApi` e de lista vazia é comum a todas as telas (`ECA-CM-02` e `ECA-CM-03`, `DEst-Comum-01`); em Notícias, a apresentação da falha é a tela em branco (`DEst-Noticias-01`).

As premissas P-NO-1 e P-NO-3 estão na tabela de [`Noticias/README.md`](README.md), com o que as capturas de tela do app (versão 3.2.0) confirmaram e o que falta confirmar.

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 11 (Software Engineering Models and Methods). IEEE, 2024.

ANTHROPIC. **Claude Code**. Assistente de IA. Disponível em: claude.ai/code. Acesso em: 30 out. 2026. Uso: apoio à redação e aos diagramas, a partir das instruções, das capturas de tela e das correções do autor (resumo em `IA/registro-C.md`). Questão: Apêndice <X>, Seção <X.1>.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
