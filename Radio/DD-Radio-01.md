# DD-Radio-01 – Entrada de DD da Rádio

| Campo | Valor |
|---|---|
| **Código** | `DD-Radio-01` |
| **Título** | Entrada de DD da Rádio |
| **Autor(a)** | Pessoa D |
| **Revisor(a)** | Pessoa C |
| **Status** | Em produção |
| **Rastreia para** | `DCla-Radio-02`, `DCdu-Radio-01`, `DD-Geral-01`, `DDados-Geral-01` |

## Descrição

Entidades da Rádio, para o DD consolidado (`DD-Geral-01`) e o modelo de dados integrado (`DDados-Geral-01`). Dono: Pessoa D. Não se relacionam com entidades de outros pacotes.

A programação é a da semana atual, obtida inteira numa única chamada ao Servidor/API. Um mesmo programa pode ir ao ar em vários dias e horários (ex.: "Brasil de canto a canto", diariamente das 5h às 7h); por isso o horário é uma entidade separada do programa.

**Tabela 1 – ProgramaRadio**: programa da grade da Rádio UFG 88,5 FM.

| Atributo | Tipo | Descrição |
|---|---|---|
| nome | String | Nome do programa, exibido em negrito |
| descricao | String | Texto descritivo do programa |

**Tabela 2 – HorarioPrograma**: um horário em que um programa vai ao ar na semana atual.

| Atributo | Tipo | Descrição |
|---|---|---|
| diaSemana | DiaSemana | Dia da semana (aba) em que o programa vai ao ar |
| horaInicio | Time | Hora de início, formato hh:mm |
| horaFim | Time | Hora de fim, formato hh:mm |

**Tabela 3 – DiaSemana** (enumeração): DOM, SEG, TER, QUA, QUI, SEX, SAB.

**Associações:** ProgramaRadio 1 — 1..* HorarioPrograma ("vai ao ar em").

Fora do DD: a URL do player é constante do app (`ConfiguracaoRadio.urlPlayer`, `DCla-Radio-01`), não entidade.

Trecho PlantUML:

```plantuml
class ProgramaRadio {
  nome: String
  descricao: String
}
class HorarioPrograma {
  diaSemana: DiaSemana
  horaInicio: Time
  horaFim: Time
}
enum DiaSemana {
  DOM
  SEG
  TER
  QUA
  QUI
  SEX
  SAB
}
ProgramaRadio "1" -- "1..*" HorarioPrograma : vai ao ar em >
```

## Referências

ANTHROPIC. **Claude Code**. Assistente de IA. Disponível em: https://claude.com/claude-code. Acesso em: 20 out. 2026.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
