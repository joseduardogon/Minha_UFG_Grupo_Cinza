# Registro de decisões – Equipe Cinza

Decisões de planejamento e de modelagem que alteram o contrato ou o roteiro. Uma entrada por decisão, da mais recente para a mais antiga.

## 02/11/2026 – Correção dos achados da integração pela Pessoa D

- **Decisão:** os achados do recebimento das entidades (`Integracao/recebimento.md`), curtos ou não, são corrigidos pela Pessoa D diretamente nos arquivos de B e de C (atividade D-INT-08), sem repasse aos autores, que são avisados das mudanças.
- **Motivo:** agilizar a integração, acordado com a equipe.
- **Alternativas:** devolver cada achado ao autor (descartada: atrasa a integração).

## 02/11/2026 – Modelo de dados da integração

- **Decisão:** (1) não há entidade de usuário nem de avaliador; o Avaliador é só ator (linha retirada da seção 7 do contrato-base); (2) `Regional` e `Campus` ficam no pacote Comum, com C como dona da definição; (3) `Local.campus: String` vira a associação `Local 0..* — 1 Campus`; (4) a Área de conhecimento (CNPq) vira a entidade `AreaConhecimento` (só `nome`), de B, com `UnidadeAcademica 0..* — 1 AreaConhecimento`, e `MediaArea` se associa a ela; (5) `Cardapio` é retirado do modelo, e a regra "o par `tipo` e `data` não se repete" passa para `Refeicao`; (6) o RU continua derivando o dia da semana da data, sem reutilizar o `DiaSemana` da Rádio; (7) `AplicativoUFG` é configuração do app, e Segurança e Apps UFG não têm entidade (`DD-Seguranca-01`, `DD-AppsUFG-01`).
- **Motivo:** (1) a avaliação é anônima e não guarda quem avaliou; (2) três pacotes de funcionalidade usam as entidades, e o `DPac-Geral-01` não permite dependência entre eles; (3) e (4) quem usa entidade de outro dono a referencia, não a redefine (contrato, seção 7); (5) o app não usa nem instancia `Cardapio` (critério 6); (6) Rádio (grade semanal sem datas) e RU (refeições com data) são conceitos diferentes, e o reuso criaria dependência entre pacotes; (7) o catálogo é fixo no app, como a URL do Guia.
- **Alternativas:** (1) entidade vazia de avaliador (descartada: critério 6); (2) manter as entidades em Eventos (descartada: dependência entre pacotes de funcionalidade); (4) manter a área como `String` (descartada: contraria o dono definido no contrato); (5) manter `Cardapio` só como entidade do servidor (descartada); (6) enumeração `DiaSemana` compartilhada no Comum (descartada: sem ganho).

## 01/11/2026 – Cálculo das notas e dependências de AvalConsultar

- **Decisão:** (1) só as notas por questão são armazenadas (`NotaQuestao`, de C); todas as médias (elemento, dimensão, avaliação, dimensão na UA, UA, área e UFG) são calculadas pelo Servidor/API a cada consulta e entregues prontas; o app só exibe (`DD-AvalConsultar-01`); (2) o botão "Ver notas" da `TelaAvaliacao` abre a `TelaNotas` por um Intent implícito do Android (ação `VER_NOTAS`), e não por referência de classe; (3) com isso, `AvalRegistrar` não depende de `AvalConsultar`, e `AvalConsultar` depende de `AvalRegistrar` só pela entidade `DimensaoQualidade`; `Inicio` deixa de depender de `AvalConsultar`, pois o cartão abre a `TelaAvaliacao`. Foram ajustados `DCla-AvalRegistrar-01`, `DCmp-AvalRegistrar-01` e `DPac-Geral-01`.
- **Motivo:** a avaliação não pode ser editada nem excluída e o app não tem cache, então calcular na hora evita médias armazenadas fora de sincronia e mantém uma chamada pequena por tela. O Intent implícito remove o ciclo entre os dois pacotes da avaliação apontado no README de `AvalRegistrar`. Nenhuma interface do Comum muda.
- **Alternativas:** o app calcular as médias a partir de todas as avaliações (descartada: muito tráfego e mais classes); guardar as médias no servidor (descartada: exige atualização a cada avaliação, sem ganho para o app); `NotaDimensao` com cópia do nome da dimensão (descartada: redundância com `DimensaoQualidade`); aceitar o ciclo de pacotes (descartada).

## 31/10/2026 – Consulta de notas da Avaliação de UA (AvalConsultar)

- **Decisão:** (1) confirma-se a P-AR-1: o cartão "Avaliação de UA" abre a `TelaAvaliacao`, e o botão "Ver notas" abre a `TelaNotas`; (2) a consulta tem três telas em profundidade: `TelaNotas` (nota da UFG e médias por área CNPq), `TelaNotasArea` (UAs da área com notas) e `TelaNotasUA` (notas por dimensão); (3) nota da UA = média das notas de suas avaliações; média da área = média das notas das UAs; nota da UFG = média das notas das UAs; (4) UA sem avaliação aparece com "Sem avaliações" e fica fora das médias; (5) dependência entre pacotes: só `AvalRegistrar` → `AvalConsultar`, pela navegação do botão "Ver notas"; `AvalConsultar` lê as entidades da avaliação pelo Servidor/API e não depende de `AvalRegistrar` na navegação. O ajuste do `DPac-Geral-01` fica para o D-AVC-02.
- **Motivo:** o enunciado exige a nota por UA, a média por área CNPq e a nota da UFG, mas não define as telas nem a agregação entre avaliações. A média de médias segue a definição de nota da UFG do enunciado e mantém a mesma regra nos três níveis. Contar uma UA sem avaliação como zero distorceria as médias. Uma só direção de dependência evita o ciclo de pacotes apontado no README de `AvalRegistrar`.
- **Alternativas:** duas telas, sem as notas por dimensão (descartada: perde a informação que o enunciado define no cálculo); tela única (descartada: lista longa e mistura níveis); média da área ponderada pelas avaliações (descartada: UAs com mais avaliações pesariam mais, diferente da regra da UFG); esconder UAs sem avaliação (descartada: o usuário não saberia se a UA existe).

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
