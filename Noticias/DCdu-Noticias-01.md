# DCdu-Noticias-01 – Casos de uso da funcionalidade Notícias

| Campo | Valor |
|---|---|
| **Código** | `DCdu-Noticias-01` |
| **Título** | Casos de uso da funcionalidade Notícias |
| **Autor(a)** | José Eduardo Gontijo de Carvalho (Pessoa C) |
| **Revisor(a)** | Phablo Tavares Paixão (Pessoa D) |
| **Status** | Em produção |
| **Rastreia para** | `DCdu-Geral-01`, `DAtv-Noticias-01`, `DAtv-Noticias-02`, `DIhc-Noticias-01`, `DCla-Comum-01`, `DEst-Comum-01` |

## Diagrama

![DCdu-Noticias-01](DCdu-Noticias-01.png)

Fonte: [`DCdu-Noticias-01.puml`](DCdu-Noticias-01.puml)

## Descrição

Detalha o caso de uso macro UC05 "Consultar notícias" do `DCdu-Geral-01` em dois casos de uso, numerados `UC05.1` e `UC05.2` como os da Rádio (`DCdu-Radio-01`). O ator primário é o Membro da comunidade UFG (anônimo). Os atores secundários são o Servidor/API, que fornece as notícias cadastradas pelo painel web, e o Navegador, que abre a notícia no site da UFG. O Navegador é uma especialização do ator abstrato Aplicativo externo, que corresponde ao componente LinkExterno do Comum (`DCla-Comum-01`). O app não tem tela de detalhe da notícia: tocar em um item abre a página dela no navegador (capturas 12 e 20 da versão 3.2.0: portal ufg.br, trilha "INÍCIO > NOTÍCIAS", título, data e hora de publicação, texto e créditos "Texto:" e "Foto de capa:", estes fora do modelo do app).

O caso de uso UC05.2 estende o UC05.1: ele só pode ocorrer depois que a lista de notícias foi exibida.

**Tabela 1 – Casos de uso de Notícias**

| Código | Caso de uso | Objetivo do usuário | Atores secundários |
|---|---|---|---|
| UC05.1 | Consultar notícias de uma regional | Ver as notícias de uma regional | Servidor/API |
| UC05.2 | Abrir a notícia (estende UC05.1) | Ler a notícia completa no site da UFG | Navegador |

**UC05.1 – Consultar notícias de uma regional**

- *Pré-condição:* o usuário tocou no cartão Notícias do menu inicial.
- *Fluxo principal:* (1) o app abre a tela "Notícias" com a regional inicial selecionada, que é a primeira da faixa de abas ("GOIÂNIA" nas capturas 5 e 11; P-NO-2); (2) o app pede ao servidor as notícias da regional; (3) o app mostra a faixa de abas e lista as notícias, cada uma em um cartão com imagem de banner, título em negrito e um resumo curto (P-NO-3); a faixa rola junto com a lista (captura 18); (4) com a lista exibida, o usuário pode tocar em outra aba de regional (P-NO-1), e o fluxo volta ao passo 2.
- *Fluxos alternativos:* **A1** a regional não tem notícias: segue o ciclo genérico de `DEst-Comum-01`, com a mensagem de vazio e sem a faixa de abas; esse estado não foi observado (P-NO-9); **A2** sem internet ou servidor indisponível: o app mostra a tela em branco, sem a faixa de abas e sem mensagem (captura 31, modo avião, P-NO-8). Em A1 e A2 não há aba para tocar: o usuário só sai voltando ao menu ou entrando de novo na tela.
- *Pós-condição:* a tela mostra as notícias da regional selecionada.

**UC05.2 – Abrir a notícia**

- *Pré-condição:* a lista exibe ao menos uma notícia.
- *Fluxo principal:* (1) o usuário toca em uma notícia; (2) o app pede ao Navegador que abra a página dela, no portal de notícias da UFG; (3) o Navegador exibe a página, que mostra o título, a data e hora de publicação, o texto e os créditos (capturas 12 e 20; o toque em si não foi capturado, só o resultado, P-NO-3).
- *Fluxos alternativos:* **A1** endereço inválido ou nenhum navegador disponível: o app atual não mostra mensagem (`DCla-Comum-01`).
- *Pós-condição:* ao voltar ao app, a tela de Notícias é exibida de novo e recarrega as notícias da regional que estava selecionada (sem cache).

As premissas P-NO-1, P-NO-2, P-NO-3, P-NO-8 e P-NO-9 estão na tabela de [`Noticias/README.md`](README.md), com o que as capturas de tela do app (versão 3.2.0) confirmaram e o que falta confirmar.

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 11 (Software Engineering Models and Methods). IEEE, 2024.

ANTHROPIC. **Claude Code**. Assistente de IA. Disponível em: claude.ai/code. Acesso em: 30 out. 2026. Uso: apoio à redação e aos diagramas, a partir das instruções, das capturas de tela e das correções do autor (resumo em `IA/registro-C.md`). Questão: Apêndice <X>, Seção <X.1>.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
