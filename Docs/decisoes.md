# Registro de decisões – Equipe Cinza

Decisões de planejamento e de modelagem que alteram o contrato ou o roteiro. Uma entrada por decisão, da mais recente para a mais antiga.

## 20/10/2026 – Cartão "Avaliação de UA" na tela inicial

- **Decisão:** a tela inicial mantém os oito cartões da versão 3.1.1 e ganha um nono, "Avaliação de UA", ponto de entrada único de `AvalRegistrar` e `AvalConsultar`. A tela aberta por ele é definida por A e B. O texto do `DPac-Geral-01` foi ajustado; o diagrama não muda.
- **Motivo:** nenhuma fonte define o ponto de entrada da evolução; um único cartão novo preserva a tela real e não depende de decisões ainda não tomadas por A e B.
- **Alternativas:** oito cartões, com a avaliação acessada por Locais (descartada: depende de decisão de A e B e exige mudar o DPac); dez cartões, um para avaliar e outro para consultar (descartada: duplica o ponto de entrada).

## 20/10/2026 – Entidades da Rádio

- **Decisão:** a programação é modelada como `ProgramaRadio` (nome, descrição) 1 — 1..* `HorarioPrograma` (dia da semana, hora de início, hora de fim). O controlador genérico do Comum trabalha com `HorarioPrograma`; a tela filtra pelo dia e trata sozinha o vazio de um único dia.
- **Motivo:** o mesmo programa vai ao ar em vários dias e horários (print 03); separar evita repetir nome e descrição (critério 4.2). O controlador do Comum decide VAZIO pela lista inteira, e a carga é semanal.
- **Alternativas:** uma única entidade `ItemProgramacao` com todos os campos (descartada: redundância); um controlador por dia (descartada: a carga é única para a semana).

## 20/10/2026 – Carga semanal da programação da Rádio

- **Decisão:** a tela da Rádio busca a programação da semana atual inteira numa única chamada ao entrar. A troca de aba filtra os dados em memória, sem nova chamada. Ao sair e entrar de novo, nova chamada é feita. A URL do player é fixa no app, sem parâmetros. Dia sem programas usa a mensagem genérica de vazio do Comum.
- **Motivo:** comportamento informado pela equipe a partir do app real; os dados são só texto e pesam pouco. O estado vazio não pôde ser observado, porque a programação da semana está cheia.
- **Alternativas:** uma chamada por dia ao trocar de aba (descartada: não é o comportamento do app); URL do player vinda da API (descartada: é fixa).

## 20/10/2026 – URL do Guia Estudantil como configuração fixa

- **Decisão:** a URL do `guiaestudantil.pdf` é uma constante do app (`ConfiguracaoGuia`, `DCla-Guia-01`). O Guia não tem entidade de domínio e não entra no DDados nem no DD consolidados.
- **Motivo:** o seletor de apps abre logo após o toque, sem estado de carregando nem chamada ao servidor (prints 04 e 05).
- **Alternativas:** entidade `DocumentoGuia` obtida do Servidor/API (descartada: exigiria tela remota e chamada à API, sem indício no app).

## 20/10/2026 – Guia Estudantil sem tela própria

- **Decisão:** o `DIhc-Guia-01` mostra o trecho da tela inicial com o cartão do Guia e o seletor de apps do Android, marcado como componente do sistema. O app só passa a URL externa do `guiaestudantil.pdf` ao `ILinkExterno.abrirDocumento`; o download, a exibição e as falhas de abertura ficam com o app externo ou com o Android e não retornam ao app.
- **Motivo:** no app real (prints 04 e 05), tocar no cartão abre direto o seletor de apps, sem tela intermediária. Erros como formato incompatível são mostrados pelo próprio aparelho.
- **Alternativas:** DIhc só com o seletor de apps (descartada: perde o evento de entrada); tratar `SEM_APP_COMPATIVEL` no Guia (descartada: o app não trata esse caso).

## 19/10/2026 – Integração de D só depois das entregas das etapas 1 e 2

- **Decisão:** a ordem do trabalho muda. A, B e C entregam as etapas 1 e 2: ao menos uma funcionalidade com a cascata completa, ou todas, se quiserem, mais as entradas do dicionário de dados das suas entidades, tudo junto no fim da etapa 2. D conclui toda a sua produção individual (Guia, Rádio, tela inicial e fechamento do Comum) e só então faz a integração: modelo de dados integrado (DDados e DD), fechamento do DCdu geral, do DPac e do DImp, e rastreabilidade.
