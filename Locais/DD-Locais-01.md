# DD-Locais-01 – Entrada de DD de Locais e Unidades Acadêmicas

| Campo | Valor |
|---|---|
| **Código** | `DD-Locais-01` |
| **Título** | Entrada de DD de Locais e Unidades Acadêmicas |
| **Autor(a)** | Maicon Brendo da Silva |
| **Revisor(a)** | Revisor(a) a definir |
| **Status** | Em produção |
| **Rastreia para** | `DCla-Locais-02`, `DCdu-Locais-01`, `DD-Geral-01`, `DDados-Geral-01` |

## Descrição

Especificação formal das entidades compartilhadas do pacote `Locais` sob responsabilidade de Pessoa B (Maicon Brendo da Silva), destinada ao Dicionário de Dados consolidado (`DD-Geral-01`) e ao Esquema Conceitual de Dados integrado (`DDados-Geral-01`), sob coordenação da Pessoa D.

Conforme a seção 7 do `contrato-base.md`, **Unidade Acadêmica é uma especialização de Local** ("toda Unidade Acadêmica é um Local, mas nem todo Local é Unidade Acadêmica"). Quem necessita dessas entidades (em especial os módulos de Avaliação de UA) as referencia, sem redefini-las.

---

### Tabela 1 – Local

Entidade que representa um prédio, instalação ou ponto de interesse geográfico do campus.

| Atributo | Tipo | Descrição |
|---|---|---|
| `id` | Integer | Identificador primário único do local no sistema |
| `nome` | String | Nome oficial do local exibido na lista e no mapa (ex.: *"Restaurante Universitário - Samambaia"*, *"Biblioteca Central"*) |
| `fotoUrl` | String | URL ou caminho relativo da foto circular em miniatura exibida na lista de locais |
| `corMarcador` | String | Código de cor do marcador circular no mapa (ex.: verde para unidades de ensino, laranja para bibliotecas, azul para serviços) |
| `campus` | String | Nome do campus universitário de vinculação (fixo em *"Campus Samambaia"*) |

---

### Tabela 2 – UnidadeAcademica

Especialização de `Local` que representa unidades de ensino, pesquisa e extensão (faculdades e institutos). Herda todos os atributos da entidade `Local`.

| Atributo | Tipo | Descrição |
|---|---|---|
| `sigla` | String | Sigla oficial da unidade acadêmica (ex.: *"INF"*, *"FEFD"*, *"ICB"*) |
| `areaConhecimento` | String | Grande área do conhecimento conforme classificação CNPq/UFG (ex.: *"Ciências Exatas e da Terra"*, *"Ciências da Saúde"*), utilizada para cálculo e consolidação de médias nas funcionalidades de avaliação |

---

### Associações

- `Local` 1 — 1 `Coordenada`: todo local possui exatamente uma coordenada geográfica (latitude e longitude) para posicionamento no mapa.
- `Local` <|-- `UnidadeAcademica`: relação de herança/generalização.

---

### Trecho PlantUML para o modelo de dados integrado (`DDados-Geral-01`)

```plantuml
class Local {
  id: Integer
  nome: String
  fotoUrl: String
  corMarcador: String
  campus: String
}

class UnidadeAcademica {
  sigla: String
  areaConhecimento: String
}

class Coordenada <<Comum>> {
  latitude: Real
  longitude: Real
}

Local <|-- UnidadeAcademica
Local "1" *-- "1" Coordenada : localiza-se em >
```

## Referências

GOOGLE. **Antigravity**. Assistente de IA para Engenharia de Software. Disponível em: https://antigravity.google.com. Acesso em: 30 out. 2026.

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 11 (Software Engineering Models and Methods). IEEE, 2024.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |

