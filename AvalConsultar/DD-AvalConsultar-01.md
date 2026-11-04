# DD-AvalConsultar-01 – Entrada de DD de Avaliação – Consultar notas

| Campo | Valor |
|---|---|
| **Código** | `DD-AvalConsultar-01` |
| **Título** | Entrada de DD de Avaliação – Consultar notas |
| **Autor(a)** | Phablo Tavares Paixão |
| **Revisor(a)** | Maicon Brendo da Silva |
| **Status** | Em produção |
| **Rastreia para** | `DCla-AvalConsultar-02`, `DCdu-AvalConsultar-01`, `DD-AvalRegistrar-01`, `DD-Locais-01`, `DD-Geral-01`, `DDados-Geral-01` |

## Descrição

Entidades de `AvalConsultar`, para o DD consolidado (`DD-Geral-01`) e o modelo de dados integrado (`DDados-Geral-01`). Dono: Pessoa D. As entidades da avaliação (`Avaliacao`, `NotaQuestao`, `DimensaoQualidade`, `ElementoEducacional`, `Questao`) são de `AvalRegistrar` (`DD-AvalRegistrar-01`) e `UnidadeAcademica` é de `Locais` (`DD-Locais-01`); aqui são só referenciadas, sem redefinição.

### O que é armazenado e o que é calculado

**Tabela 1 – Origem de cada nota**

| Nota | Regra | Armazenada? | Onde é calculada |
|---|---|---|---|
| Nota da questão | Dada pelo avaliador, 0 a 5 | Sim (`NotaQuestao.valor`, de C) | – |
| Nota do elemento, numa avaliação | Média das notas de suas questões (P-AR-12) | Não | Servidor/API |
| Nota da dimensão, numa avaliação | Média das notas de seus elementos (enunciado) | Não | Servidor/API |
| Nota da avaliação | Média das notas das dimensões (enunciado) | Não | Servidor/API |
| Nota da dimensão na UA (`NotaDimensao.nota`) | Média, entre as avaliações da UA, da nota da dimensão (P-AC-8) | Não | Servidor/API |
| Nota da UA (`NotaUnidade.nota`) | Média das notas das avaliações da UA (P-AC-3) | Não | Servidor/API |
| Média da área (`MediaArea.nota`) | Média das notas das UAs avaliadas da área (P-AC-3, P-AC-4) | Não | Servidor/API |
| Nota da UFG | Média das notas de todas as UAs avaliadas (enunciado; P-AC-4) | Não | Servidor/API |

Só as notas por questão são guardadas; todas as médias são calculadas pelo Servidor/API a cada consulta e entregues prontas ao app (P-AC-6, decisão de 01/11/2026). Como a avaliação não pode ser editada nem excluída e não há cache, calcular na hora evita manter médias armazenadas em sincronia. As entidades abaixo são, portanto, **derivadas e somente leitura**: existem na resposta da API e na memória do app enquanto a tela está aberta, sem persistência.

**Tabela 2 – MediaArea**: média de uma grande área do conhecimento (CNPq).

| Atributo | Tipo | Descrição |
|---|---|---|
| nota | Real [0..1] | Média de 0 a 5; ausente quando nenhuma UA da área tem avaliação (P-AC-4) |

**Tabela 3 – NotaUnidade**: nota de uma unidade acadêmica.

| Atributo | Tipo | Descrição |
|---|---|---|
| nota | Real [0..1] | Média de 0 a 5; ausente quando a UA não tem avaliação (P-AC-4) |

**Tabela 4 – NotaDimensao**: nota de uma dimensão de qualidade numa UA.

| Atributo | Tipo | Descrição |
|---|---|---|
| nota | Real | Média de 0 a 5 (só existe se a UA tem avaliação) |

A nota da UFG não é entidade: é um valor único devolvido com a lista de áreas (`FonteNotasUFG.obterNotaUfg`, `DCla-AvalConsultar-02`).

**Associações:** `MediaArea` 0..* — 1 `AreaConhecimento` ("areaConhecimento"; entidade de B, `DD-Locais-01`); `NotaUnidade` 0..* — 1 `UnidadeAcademica` ("unidade"); `NotaDimensao` 0..* — 1 `DimensaoQualidade` ("dimensao").

Trecho PlantUML:

```plantuml
class MediaArea {
  nota: Real [0..1]
}
class NotaUnidade {
  nota: Real [0..1]
}
class NotaDimensao {
  nota: Real
}
MediaArea "0..*" --> "1" AreaConhecimento : areaConhecimento
NotaUnidade "0..*" --> "1" UnidadeAcademica : unidade
NotaDimensao "0..*" --> "1" DimensaoQualidade : dimensao
```

## Referências

ANTHROPIC. **Claude Code**. Assistente de IA. Disponível em: https://claude.com/claude-code. Acesso em: 1 nov. 2026.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
