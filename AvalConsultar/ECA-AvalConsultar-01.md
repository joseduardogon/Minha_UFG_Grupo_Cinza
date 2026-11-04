# ECA-AvalConsultar-01 – Regras E-C-A de Avaliação – Consultar notas

| Campo | Valor |
|---|---|
| **Código** | `ECA-AvalConsultar-01` |
| **Título** | Regras E-C-A de Avaliação – Consultar notas |
| **Autor(a)** | Phablo Tavares Paixão |
| **Revisor(a)** | Maicon Brendo da Silva |
| **Status** | Em produção |
| **Rastreia para** | `DCla-AvalConsultar-01`, `DEst-AvalConsultar-01`, `DEst-AvalConsultar-02`, `DEst-AvalConsultar-03`, `DEst-Comum-01`, `Contrato-AvalConsultar-01` |

## Descrição

Regras ativas da consulta de notas, sobre as classes de `DCla-AvalConsultar-01`. Correspondem às transições dos `DEst-AvalConsultar-01` a `03`.

**Tabela 1 – Regras E-C-A de Avaliação – Consultar notas**

| Código | Evento | Condição | Ação | Classe |
|---|---|---|---|---|
| ECA-AC-01 | Uma tela da consulta é exibida (entrada ou volta de outra tela) | Sempre (o app não guarda cache) | Cria fonte e controlador, carrega as notas do servidor e vai a Carregando | `TelaNotas`, `TelaNotasArea`, `TelaNotasUA` |
| ECA-AC-02 | O controlador entra em EXIBINDO | Uma nota (agregada ou da lista) está ausente | Mostra "Sem avaliações" no lugar da nota | `TelaNotas`, `TelaNotasArea` |
| ECA-AC-03 | O usuário toca em uma área | O estado é EXIBINDO | Abre a `TelaNotasArea` da área | `TelaNotas` |
| ECA-AC-04 | O usuário toca em uma UA | O estado é EXIBINDO | Abre a `TelaNotasUA` da UA, mesmo sem avaliações | `TelaNotasArea` |
| ECA-AC-05 | O usuário sai de uma tela da consulta | Sempre | Descarta as notas em memória | `TelaNotas`, `TelaNotasArea`, `TelaNotasUA` |

Não há regra para falhas de comunicação: o tratamento de `ErroApi` é comum a todas as telas (`DEst-Comum-01`). Não há regra de escrita: a consulta só lê, e a avaliação não pode ser editada nem excluída.

## Referências

ANTHROPIC. **Claude Code**. Assistente de IA. Disponível em: https://claude.com/claude-code. Acesso em: 1 nov. 2026.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
