# ECA-Radio-01 – Regras E-C-A da Rádio

| Campo | Valor |
|---|---|
| **Código** | `ECA-Radio-01` |
| **Título** | Regras E-C-A da Rádio |
| **Autor(a)** | Pessoa D |
| **Revisor(a)** | Pessoa C |
| **Status** | Em produção |
| **Rastreia para** | `DCla-Radio-01`, `DEst-Radio-01`, `DEst-Comum-01`, `Contrato-Radio-01` |

## Descrição

Regras ativas da Rádio, sobre a classe `TelaRadio`. Correspondem às transições do `DEst-Radio-01`.

**Tabela 1 – Regras E-C-A da Rádio**

| Código | Evento | Condição | Ação | Classe |
|---|---|---|---|---|
| ECA-RA-01 | A tela da Rádio volta a ser exibida (entrada pela tela inicial ou retorno do navegador) | Sempre (o app não guarda cache) | Carrega a programação da semana de novo e volta ao estado Carregando | `TelaRadio` |
| ECA-RA-02 | O usuário toca na aba de um dia | O estado é EXIBINDO | Exibe os programas do dia a partir dos dados em memória, sem recarregar | `TelaRadio` |
| ECA-RA-03 | O usuário sai da tela da Rádio | Sempre | Descarta a programação em memória | `TelaRadio` |

Não há regra ativa para falhas de comunicação: o tratamento de `ErroApi` é comum a todas as telas (`DEst-Comum-01`).

## Referências

ANTHROPIC. **Claude Code**. Assistente de IA. Disponível em: https://claude.com/claude-code. Acesso em: 20 out. 2026.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
