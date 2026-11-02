# DAtv-Noticias-01 – Atividades de UC05.1: consultar notícias de uma regional

| Campo | Valor |
|---|---|
| **Código** | `DAtv-Noticias-01` |
| **Título** | Atividades de UC05.1: consultar notícias de uma regional |
| **Autor(a)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Revisor(a)** | Phablo Tavares Paixão (Pessoa D) |
| **Status** | Em produção |
| **Rastreia para** | `DCdu-Noticias-01`, `DIhc-Noticias-01`, `DEst-Comum-01`, `DSeq-Noticias-01`, `DSeq-Noticias-02` |

## Diagrama

![DAtv-Noticias-01](DAtv-Noticias-01.png)

Fonte: [`DAtv-Noticias-01.puml`](DAtv-Noticias-01.puml)

## Descrição

Fluxo do caso de uso UC05.1 do `DCdu-Noticias-01`, em raias: Membro, App e Servidor/API. As ações de interação com o app são **A1 – abrir a tela Notícias** (evento E0 do `DIhc-Noticias-01`, sequência em `DSeq-Noticias-01`) e **A2 – tocar em outra aba de regional** (evento E1, sequência em `DSeq-Noticias-02`). A chamada ao servidor e a exibição do resultado fazem parte de cada atividade (contrato-base, seção 6), com os desfechos do ciclo genérico de `DEst-Comum-01`: exibindo (faixa de abas e um cartão por notícia), vazio ou indisponível.

A tela abre com a primeira aba de regional selecionada (P-NO-2). **Só no desfecho "exibindo" a faixa de abas aparece e o usuário pode tocar em outra aba** (P-NO-1), e então o ciclo se repete com a nova regional. No desfecho indisponível o app mostra a tela em branco, sem abas e sem mensagem (captura 31, modo avião, P-NO-8); no desfecho vazio, não observado, presume-se a mensagem de vazio, também sem abas (P-NO-9). Nesses dois desfechos o usuário só sai voltando ao menu ou saindo e entrando de novo na tela. Ao tocar na seta de voltar (evento E3, passo trivial sem diagrama de sequência, fixa na barra de título em todos os estados) a tela é encerrada e a regional escolhida e as notícias em memória são descartadas. O retorno do Navegador, depois de tocar em uma notícia (`DAtv-Noticias-02`), faz a tela ser exibida de novo e repete o ciclo com a regional que estava selecionada.

As premissas P-NO-1, P-NO-2, P-NO-8 e P-NO-9 estão na tabela de [`Noticias/README.md`](README.md), com o que as capturas de tela do app (versão 3.2.0) confirmaram e o que falta confirmar.

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 11 (Software Engineering Models and Methods). IEEE, 2024.

ANTHROPIC. **Claude Code**. Assistente de IA. Disponível em: claude.ai/code. Acesso em: 30 out. 2026. Uso: apoio à redação e aos diagramas, a partir das instruções, das capturas de tela e das correções do autor (resumo em `IA/registro-C.md`). Questão: Apêndice <X>, Seção <X.1>.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
