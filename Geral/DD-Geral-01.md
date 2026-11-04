# DD-Geral-01 – Dicionário de dados consolidado

| Campo | Valor |
|---|---|
| **Código** | `DD-Geral-01` |
| **Título** | Dicionário de dados consolidado |
| **Autor(a)** | Phablo Tavares Paixão |
| **Revisor(a)** | José Eduardo Gontijo de Carvalho |
| **Status** | Em produção |
| **Rastreia para** | `DDados-Geral-01`, `DD-Eventos-01`, `DD-Noticias-01`, `DD-RU-01`, `DD-Radio-01`, `DD-Locais-01`, `DD-AvalRegistrar-01`, `DD-AvalConsultar-01`, `DD-Guia-01`, `DD-Seguranca-01`, `DD-AppsUFG-01`, `DCla-Comum-04` |

## Descrição

Atributos de todas as entidades do `DDados-Geral-01`, consolidados das entradas de DD de cada pacote depois da validação (D-INT-01) e da correção dos achados (D-INT-08), registradas em `Integracao/recebimento.md`. Cada tabela indica o dono e a entrada de origem, onde estão as premissas e as justificativas. As chaves estrangeiras não são atributos: as ligações entre entidades estão nas associações (Tabela 24). Guia, Segurança e Apps UFG não têm entidade (`DD-Guia-01`, `DD-Seguranca-01`, `DD-AppsUFG-01`).

Na coluna "Obr.", "Não" corresponde à multiplicidade `[0..1]`.

### Pacote Comum

**Tabela 1 – Regional** (dono: Pessoa C; origem: `DD-Eventos-01`): divisão administrativa da UFG que agrupa campi e à qual pertencem eventos e notícias.

| Atributo | Tipo | Obr. | Descrição |
|---|---|---|---|
| id | Integer | Sim | Identificador único da regional |
| nome | String | Sim | Nome da regional, sem repetição |

**Tabela 2 – Campus** (dono: Pessoa C; origem: `DD-Eventos-01`): unidade física da UFG, vinculada a uma regional.

| Atributo | Tipo | Obr. | Descrição |
|---|---|---|---|
| id | Integer | Sim | Identificador único do campus |
| nome | String | Sim | Nome do campus, sem repetição dentro da regional |

**Tabela 3 – Coordenada** (dono: Pessoa D; origem: `DCla-Comum-04`, referenciada em `DD-Locais-01`): posição geográfica de um local no mapa.

| Atributo | Tipo | Obr. | Descrição |
|---|---|---|---|
| latitude | Real | Sim | Latitude, em graus decimais |
| longitude | Real | Sim | Longitude, em graus decimais |

### Pacote Eventos

**Tabela 4 – Evento** (dono: Pessoa C; origem: `DD-Eventos-01`): acontecimento divulgado pela UFG, consultado por regional e por data.

| Atributo | Tipo | Obr. | Descrição |
|---|---|---|---|
| id | Integer | Sim | Identificador único do evento |
| titulo | String | Sim | Nome do evento, como exibido na lista |
| dataInicio | Date | Sim | Primeiro dia do evento |
| dataFim | Date | Sim | Último dia do evento; igual ou posterior a `dataInicio` |
| url | String | Não | Página do evento, aberta no navegador ao tocar no item |
| urlImagem | String | Não | Imagem exibida como miniatura no cartão |

### Pacote Noticias

**Tabela 5 – Noticia** (dono: Pessoa C; origem: `DD-Noticias-01`): notícia da UFG sobre uma regional.

| Atributo | Tipo | Obr. | Descrição |
|---|---|---|---|
| id | Integer | Sim | Identificador único da notícia |
| titulo | String | Sim | Título exibido no cartão; não vazio |
| resumo | String | Não | Texto curto abaixo do título |
| urlImagem | String | Não | Imagem de banner do cartão |
| url | String | Sim | Endereço da notícia no portal, aberto no navegador |

### Pacote RU

**Tabela 6 – Refeicao** (dono: Pessoa C; origem: `DD-RU-01`): refeição servida em uma data. A combinação `tipo` e `data` não se repete; não há Jantar no sábado nem refeição no domingo.

| Atributo | Tipo | Obr. | Descrição |
|---|---|---|---|
| id | Integer | Sim | Identificador único da refeição |
| tipo | TipoRefeicao | Sim | Café da manhã, almoço ou jantar |
| data | Date | Sim | Dia em que é servida; o dia da semana é derivado dela |

**Tabela 7 – ItemCardapio** (dono: Pessoa C; origem: `DD-RU-01`): item servido em uma refeição, numa categoria.

| Atributo | Tipo | Obr. | Descrição |
|---|---|---|---|
| id | Integer | Sim | Identificador único do item |
| descricao | String | Sim | Texto do item, como exibido na tela |

**Tabela 8 – CategoriaItem** (dono: Pessoa C; origem: `DD-RU-01`): grupo em que os itens aparecem na tela.

| Atributo | Tipo | Obr. | Descrição |
|---|---|---|---|
| id | Integer | Sim | Identificador único da categoria |
| nome | String | Sim | Nome da categoria, sem repetição |

**Tabela 9 – TipoRefeicao** (enumeração; dono: Pessoa C): `CAFE_DA_MANHA`, `ALMOCO`, `JANTAR`.

### Pacote Radio

**Tabela 10 – ProgramaRadio** (dono: Pessoa D; origem: `DD-Radio-01`): programa da grade da Rádio UFG.

| Atributo | Tipo | Obr. | Descrição |
|---|---|---|---|
| nome | String | Sim | Nome do programa |
| descricao | String | Sim | Texto descritivo do programa |

**Tabela 11 – HorarioPrograma** (dono: Pessoa D; origem: `DD-Radio-01`): horário em que um programa vai ao ar na semana atual.

| Atributo | Tipo | Obr. | Descrição |
|---|---|---|---|
| diaSemana | DiaSemana | Sim | Dia da semana em que vai ao ar |
| horaInicio | Time | Sim | Hora de início (hh:mm) |
| horaFim | Time | Sim | Hora de fim (hh:mm) |

**Tabela 12 – DiaSemana** (enumeração; dono: Pessoa D): `DOM`, `SEG`, `TER`, `QUA`, `QUI`, `SEX`, `SAB`. Usada só pela Rádio; o RU deriva o dia da data (decisão I-07).

### Pacote Locais

**Tabela 13 – Local** (dono: Pessoa B; origem: `DD-Locais-01`): prédio, instalação ou ponto de interesse do campus.

| Atributo | Tipo | Obr. | Descrição |
|---|---|---|---|
| id | Integer | Sim | Identificador único do local |
| nome | String | Sim | Nome exibido na lista e no mapa |
| fotoUrl | String | Sim | Foto em miniatura exibida na lista |
| corMarcador | String | Sim | Cor do marcador no mapa |

**Tabela 14 – UnidadeAcademica** (dono: Pessoa B; origem: `DD-Locais-01`): especialização de `Local` (faculdades e institutos); herda os atributos de `Local`.

| Atributo | Tipo | Obr. | Descrição |
|---|---|---|---|
| sigla | String | Sim | Sigla oficial da unidade (ex.: "INF") |

**Tabela 15 – AreaConhecimento** (dono: Pessoa B; origem: `DD-Locais-01`): grande área do conhecimento (CNPq) de uma UA.

| Atributo | Tipo | Obr. | Descrição |
|---|---|---|---|
| nome | String | Sim | Nome da grande área, sem repetição |

### Pacote AvalRegistrar

**Tabela 16 – DimensaoQualidade** (dono: Pessoa C; origem: `DD-AvalRegistrar-01`): categoria de elementos educacionais correlatos.

| Atributo | Tipo | Obr. | Descrição |
|---|---|---|---|
| id | Integer | Sim | Identificador, atribuído pelo servidor |
| nome | String | Sim | Nome exibido no questionário |
| ordem | Integer | Sim | Posição no questionário |

**Tabela 17 – ElementoEducacional** (dono: Pessoa C; origem: `DD-AvalRegistrar-01`): aspecto avaliado dentro de uma dimensão.

| Atributo | Tipo | Obr. | Descrição |
|---|---|---|---|
| id | Integer | Sim | Identificador, atribuído pelo servidor |
| nome | String | Sim | Nome exibido no questionário |
| ordem | Integer | Sim | Posição dentro da dimensão |

**Tabela 18 – Questao** (dono: Pessoa C; origem: `DD-AvalRegistrar-01`): pergunta predefinida sobre um elemento.

| Atributo | Tipo | Obr. | Descrição |
|---|---|---|---|
| id | Integer | Sim | Identificador, atribuído pelo servidor e enviado com a nota |
| texto | String | Sim | Enunciado exibido ao usuário |
| ordem | Integer | Sim | Posição dentro do elemento |

**Tabela 19 – Avaliacao** (dono: Pessoa C; origem: `DD-AvalRegistrar-01`): opinião anônima sobre uma UA. Uma UA pode receber várias avaliações, inclusive da mesma pessoa; a avaliação registrada não é editada nem excluída.

| Atributo | Tipo | Obr. | Descrição |
|---|---|---|---|
| id | Integer | Sim | Só no servidor; atribuído no registro |
| dataHoraRegistro | DateTime | Sim | Só no servidor; data e hora do registro |

**Tabela 20 – NotaQuestao** (dono: Pessoa C; origem: `DD-AvalRegistrar-01`): nota dada a uma questão numa avaliação. Cada avaliação tem exatamente uma nota por questão do questionário.

| Atributo | Tipo | Obr. | Descrição |
|---|---|---|---|
| valor | Integer | Sim | Nota inteira de 0 (péssima) a 5 (excelente) |

### Pacote AvalConsultar

Entidades derivadas e somente leitura: calculadas pelo Servidor/API a cada consulta, não armazenadas (`DD-AvalConsultar-01`). A nota da dimensão é a média dos elementos; a da avaliação, a média das dimensões; a da UA, a média das suas avaliações; a da área, a média das suas UAs avaliadas. A nota da UFG é um valor único devolvido com a lista de áreas, não entidade.

**Tabela 21 – MediaArea** (dono: Pessoa D): média de uma grande área do conhecimento.

| Atributo | Tipo | Obr. | Descrição |
|---|---|---|---|
| nota | Real | Não | Média de 0 a 5; ausente quando nenhuma UA da área tem avaliação |

**Tabela 22 – NotaUnidade** (dono: Pessoa D): nota de uma UA.

| Atributo | Tipo | Obr. | Descrição |
|---|---|---|---|
| nota | Real | Não | Média de 0 a 5; ausente quando a UA não tem avaliação |

**Tabela 23 – NotaDimensao** (dono: Pessoa D): nota de uma dimensão numa UA.

| Atributo | Tipo | Obr. | Descrição |
|---|---|---|---|
| nota | Real | Sim | Média de 0 a 5; só existe se a UA tem avaliação |

### Associações

**Tabela 24 – Associações do modelo integrado**

| Entre | Multiplicidade | Nome | Dono | Origem |
|---|---|---|---|---|
| Regional e Campus | 1 — 0..* | agrupa | C | `DD-Eventos-01` |
| Regional e Evento | 1 — 0..* | promove | C | `DD-Eventos-01` |
| Regional e Noticia | 1 — 0..* | publica | C | `DD-Noticias-01` |
| Campus e Local | 1 — 0..* | contém | B | `DD-Locais-01` |
| Local e Coordenada | 1 — 1 (composição) | localiza-se em | B | `DD-Locais-01` |
| Local e UnidadeAcademica | generalização | – | B | `DD-Locais-01` |
| UnidadeAcademica e AreaConhecimento | 0..* — 1 | pertence a | B | `DD-Locais-01` |
| Refeicao e ItemCardapio | 1 — 0..* | tem | C | `DD-RU-01` |
| CategoriaItem e ItemCardapio | 1 — 0..* | agrupa | C | `DD-RU-01` |
| ProgramaRadio e HorarioPrograma | 1 — 1..* | vai ao ar em | D | `DD-Radio-01` |
| DimensaoQualidade e ElementoEducacional | 1 — 1..* | é caracterizada por | C | `DD-AvalRegistrar-01` |
| ElementoEducacional e Questao | 1 — 1..* | tem | C | `DD-AvalRegistrar-01` |
| Avaliacao e UnidadeAcademica | 0..* — 1 | avalia | C | `DD-AvalRegistrar-01` |
| Avaliacao e NotaQuestao | 1 — 1..* (composição) | é composta por | C | `DD-AvalRegistrar-01` |
| NotaQuestao e Questao | 0..* — 1 | responde a | C | `DD-AvalRegistrar-01` |
| MediaArea e AreaConhecimento | 0..* — 1 | areaConhecimento | D | `DD-AvalConsultar-01` |
| NotaUnidade e UnidadeAcademica | 0..* — 1 | unidade | D | `DD-AvalConsultar-01` |
| NotaDimensao e DimensaoQualidade | 0..* — 1 | dimensao | D | `DD-AvalConsultar-01` |

### Verificação da consolidação

- Nenhuma entidade definida em mais de um pacote; `Regional`, `Campus`, `UnidadeAcademica`, `AreaConhecimento` e `DimensaoQualidade` são só referenciadas fora do dono.
- Nenhum nome divergente para o mesmo conceito nem atributo duplicado entre pacotes.
- Toda associação entre pacotes tem dono.
- `UnidadeAcademica` é um `Local` (generalização).

## Referências

UNIVERSIDADE FEDERAL DE GOIÁS. Instituto de Informática. **Definição de Atividades Práticas Supervisionadas (APS) da Disciplina**: INF 0290 – Projeto de Software, 2026/2. Goiânia, 2026. Apêndice D.

ANTHROPIC. **Claude Code**. Assistente de IA. Disponível em: https://claude.com/claude-code. Acesso em: 2 nov. 2026.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
