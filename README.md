# Minha_UFG_Grupo_Cinza

Repositório da Equipe Cinza para o Projeto de Software (INF0290/UFG, 2026/2). Centraliza a modelagem estrutural e comportamental (engenharia reversa e evolução) do aplicativo "Minha UFG".

Regras de trabalho: [contrato-base.md](contrato-base.md). Modelo de item de informação: [Template-Item.md](Template-Item.md).

## Estrutura

| Pasta | Conteúdo | Dono | Revisor |
|---|---|---|---|
| `Geral/` | DCdu, DImp, DPac, DDados e DD do sistema inteiro | D | C |
| `Comum/` | Componentes compartilhados (link externo, API, estados de tela remota, mapa) | D | C |
| `Inicio/` | Tela inicial | D | C |
| `Radio/` | Rádio | D | C |
| `Guia/` | Guia Estudantil | D | C |
| `Seguranca/` | Segurança | A | B |
| `AvalRegistrar/` | Avaliação de UA – registrar | A | B |
| `AvalConsultar/` | Avaliação de UA – consultar notas | B | A |
| `Locais/` | Locais | B | A |
| `AppsUFG/` | Apps UFG | B | A |
| `Eventos/` | Eventos | C | D |
| `RU/` | Restaurante Universitário | C | D |
| `Noticias/` | Notícias | C | D |
| `Integracao/` | Recebimento de entidades e rastreabilidade (trabalho de D) | D | – |
| `Atas/` | Atas dos checkpoints e registro de comunicações | todos | – |
| `IA/` | Registro de uso de IA, um arquivo por pessoa | todos | – |
| `Docs/` | Documentos de apoio (enunciado, guias) | – | – |

## Convenções rápidas

- Nome de arquivo e de diagrama: `<TIPO>-<Funcionalidade>-<nn>`, ex.: `DAtv-RU-01`. O sufixo de funcionalidade é o nome da pasta.
- Cada item é um `.md` (do modelo) e, se tiver diagrama, um `.puml` com o mesmo nome ao lado.
- Diagramas em PlantUML, estilo padrão, sem tema. Elementos em português: `camelCase` para atributos e operações, `PascalCase` para classes.
- Nada entra direto na `main`: branch + pull request.
