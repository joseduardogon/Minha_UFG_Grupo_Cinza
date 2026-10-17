<div class="capa" markdown="1">

**Universidade Federal de Goiás – Instituto de Informática** · Bacharelado em Engenharia de Software  
Disciplina: INF 0290 – Projeto de Software – 2026/2 · Docente: Prof. Juliano Lopes de Oliveira  
Tarefa: Atividades Práticas Supervisionadas – sistema de informação Minha UFG

# Relatório de Evolução do Projeto nº 01 – Versão resumida

**Equipe Cinza** · Ponto de partida do acompanhamento · **16 de outubro de 2026** · período: 7 a 16 de outubro de 2026

| Campo | Valor |
|---|---|
| **Integrantes** (em ordem alfabética) | Daniel Noleto de Oliveira · José Eduardo Gontijo de Carvalho · Maicon Brendo da Silva · Phablo Tavares Paixão · Waldson Ferreira Barbosa Júnior |
| **Onde está o trabalho** | Repositório online da equipe: github.com/joseduardogon/Minha_UFG_Grupo_Cinza (versão principal em 14/10; a parte de José Eduardo, seção 3.3, está pronta para revisão e ainda será incorporada) |
| **Prazo final** | 4 de novembro de 2026, 23h59, pelo SIGAA (sistema acadêmico da UFG); PDF pronto para a equipe em 2 de novembro |

</div>

## 1. O projeto e o que precisamos entregar

O **Minha UFG** é um aplicativo de celular da UFG com oito serviços: Segurança, Rádio UFG, Guia Estudantil, Eventos, Notícias, cardápio do Restaurante Universitário (RU), Locais (mapa do campus) e Apps UFG. Nesta disciplina não programamos o aplicativo: fazemos o seu **projeto**, isto é, desenhamos e explicamos como ele é organizado por dentro e como se comporta quando alguém o usa. O trabalho tem duas partes: **(1)** descrever o app que já existe a partir das suas telas (nas capturas mais recentes, versão 3.2.0), sem acesso ao código; **(2)** projetar uma novidade, a **avaliação da qualidade das unidades acadêmicas** (cursos e institutos, como o Instituto de Informática): a comunidade dá notas de 0 a 5 a itens como salas, laboratórios e corpo docente, e o app mostra a nota de cada unidade, de cada área do conhecimento e da UFG inteira. A entrega é **um único PDF**, no qual todo desenho tem um autor e um revisor diferentes. A Tabela 1 explica, em palavras simples, cada tipo de desenho exigido.

**Tabela 1 – Os desenhos exigidos pelo enunciado**

| Desenho | Para que serve |
|---|---|
| Modelo de dados (diagrama e dicionário) | Mostra quais informações o sistema guarda (ex.: evento, notícia) e como se relacionam |
| Implantação | Mostra onde cada parte roda (celular, servidor, mapa) e como elas se comunicam |
| Pacotes, componentes e classes | Mostram, em três níveis de detalhe, como o programa é dividido em módulos, peças e unidades menores |
| Casos de uso | Listam o que o usuário consegue fazer no app |
| Fluxo de atividades | Conta, passo a passo, cada uso, separando o que o usuário faz do que o app e o servidor fazem |
| Protótipo de tela | Desenha a tela e marca onde o usuário pode tocar |
| Sequência | Mostra a "conversa" entre as peças do app e o servidor a cada toque |
| Estados | Mostra como a tela muda quando o usuário age (ex.: carregando, sem resultado) |
| Contratos e regras automáticas | Dizem o que cada operação exige e garante, e quais reações automáticas existem |

## 2. Como a equipe se organizou

**Ideia central: dividir sem esquartejar.** Cada pessoa cuida de alguns serviços do início ao fim (do caso de uso até as regras), e o que vale para o sistema inteiro tem um responsável que junta tudo, para que os desenhos de pessoas diferentes se encaixem. Os serviços foram pesados pela quantidade de desenhos que cada um exige, de modo que o esforço estimado ficou parecido para todos (cerca de 7 pontos por pessoa). Cada pessoa revisa o trabalho de outra, nunca o próprio.

**Tabela 2 – Quem faz o quê**

| Pessoa | Quem | Serviços e responsabilidades | Quem revisa |
|---|---|---|---|
| A | Um dos três outros integrantes (a confirmar) | Avaliação das unidades – registrar notas; Segurança | B |
| B | Um dos três outros integrantes (a confirmar) | Avaliação – consultar notas e médias; Locais; Apps UFG | A |
| **C** | **José Eduardo Gontijo de Carvalho** | **Eventos; RU; Notícias** | D (Phablo) |
| **D** | **Phablo Tavares Paixão** | Parte comum a todo o app (visão geral, peças compartilhadas, tela inicial, junção dos modelos e montagem do PDF); Rádio; Guia Estudantil | C (José Eduardo) |

**Regras combinadas por escrito** (arquivo `contrato-base.md`, 12 seções), em resumo:

- **Calendário:** reunião rápida com ata toda quarta, às 19h; nas últimas semanas só correções, sem desenhos novos.
- **Padrão de trabalho:** todos os diagramas na mesma ferramenta (PlantUML), com nomes padronizados e uma ficha única para cada item (autor, revisor, itens relacionados, explicação, referências).
- **Quem usa o app:** a pessoa comum da comunidade UFG e o avaliador, ambos **anônimos** (sem login); o servidor, os aplicativos externos (navegador, loja de apps, leitor de PDF) e o provedor de mapa são "atores externos".
- **Avaliação:** quem avalia não se identifica, pode avaliar a mesma unidade mais de uma vez e não pode editar nem apagar uma avaliação enviada.
- **Nível de detalhe:** cada ação em que o usuário toca no app, ou em que o app fala com o servidor, ganha o seu desenho de sequência; passos internos triviais, não.
- **Informações compartilhadas:** cada informação usada por mais de um serviço tem um dono (regional e campus: José Eduardo; local, unidade acadêmica e área do conhecimento: B; identificação do avaliador: A); os demais apenas a referenciam.
- **Estrutura do app:** um módulo por serviço mais um módulo "comum" com as peças repetidas (abrir links, falar com o servidor, tratar telas que carregam, mapa).
- **Revisão:** devolvida em até 1 dia; um item só está pronto quando foi revisado e está no repositório. Mudanças nas regras passam por Phablo.

O repositório tem uma pasta por serviço. Cada item é um conjunto de três arquivos com o mesmo nome: **o texto explicativo**, **o arquivo-fonte do diagrama** e **a imagem**. Nada entra na versão principal sem revisão.

## 3. O que já foi feito

**3.1 Base da equipe (7 a 14 de outubro).** Criação do repositório; divisão do trabalho; contrato com as regras acima; estrutura de pastas e ficha-modelo de item; documentos de apoio guardados em `Docs/`.

**3.2 Phablo Tavares Paixão (Pessoa D) – visão geral e peças compartilhadas.** Nove itens, entregues em 14/10 e aguardando a revisão de José Eduardo (Tabela 3).

**Tabela 3 – Entregas de Phablo**

| Item | O que mostra |
|---|---|
| Casos de uso gerais (rascunho) | Os dez serviços do app (oito atuais e dois da avaliação) e quem interage com cada um |
| Pacotes do app | 12 módulos: um por serviço, a tela inicial e o módulo comum. A tela inicial usa todos; todos usam o comum; o comum não depende de ninguém. Só a avaliação depende de outro serviço (Locais) |
| Implantação | Celular, servidores da UFG (aplicativo e banco de dados), painel web, mapa, loja de apps e sites da UFG, com os meios de comunicação entre eles |
| Módulo comum (componentes e quatro conjuntos de classes) | Abertura de links externos; comunicação com o servidor e tipos de falha; tratamento padrão de telas que carregam dados; mapa e localização do aparelho |
| Estados de uma tela que carrega dados | Carregando, mostrando, sem resultado e indisponível; a tela recarrega ao voltar, pois o app não guarda cópia dos dados |

**3.3 José Eduardo Gontijo de Carvalho (Pessoa C) – Eventos, RU e Notícias.** Trabalho preparado em 16/10 e conferido com as 15 capturas de tela do app (versão 3.2.0); **pronto para a revisão de Phablo** e ainda não incorporado à versão principal. Segue a ordem de produção do contrato.

**Tabela 4 – Entregas de José Eduardo**

| Serviço | O que foi produzido | Situação |
|---|---|---|
| **Eventos** | Três casos de uso (consultar por regional e data, trocar o mês, abrir a página do evento); três fluxos; protótipo da tela com seis eventos de interação; cinco desenhos de sequência; estados da tela; módulos e classes; contratos de todas as operações; três regras automáticas | **Completo na primeira versão** (16 itens) |
| **RU** | Dois casos de uso (ver o cardápio de uma refeição, escolher o dia); fluxos; dois protótipos (tela das três refeições e tela do cardápio com o seletor de dia) | Início: faltam sequências, estados, classes e contratos |
| **Notícias** | Dois casos de uso (ver notícias de uma regional, abrir a notícia); fluxos; protótipo da tela | Início: faltam as mesmas etapas |
| **Informações para o modelo de dados** | Oito fichas entregues a Phablo: regional, campus, evento, notícia, cardápio, refeição, categoria e item do cardápio, com campos, relações e regras | Entregues |

Os desenhos de Eventos reaproveitam as peças do módulo comum de Phablo, sem refazê-las.

**3.4 Conferência com as telas do app.** As capturas confirmaram o desenho de **Notícias** (abas de regional, cartões com imagem, título e resumo, e página aberta no navegador) e de **RU** (três cartões de refeição; tela da refeição com data, itens por categoria e seletor de dia de segunda a sábado). Mostraram também que a lista de locais fica sob o título "Campus Samambaia", o que sustenta a relação entre campus e local. **Falta a captura da tela de lista de Eventos** (calendário e lista): só aparece a página de um evento. Por isso as suposições de Eventos sobre regional, troca de mês e data inicial seguem a confirmar. A Tabela 5 resume a conferência.

**Tabela 5 – Conferência das telas**

| Serviço | Confirmado nas capturas | Ainda a confirmar |
|---|---|---|
| Notícias | Abas de regional (Goiânia selecionada); cartão com imagem, título e resumo; toque abre a página no navegador | Demais regionais; ordem da lista |
| RU | Três refeições; seletor de segunda a sábado; hoje selecionado; categorias do café da manhã | Almoço, jantar e jantar de sábado |
| Eventos | Página do evento no navegador (título, local e período de vários dias) | Toda a tela de lista (regional, calendário, troca de mês) |

## 4. Onde estamos em relação ao calendário

**Tabela 6 – Panorama em 16/10/2026**

| Indicador | Valor | Indicador | Valor |
|---|---|---|---|
| Itens produzidos (Phablo / José Eduardo) | 34 (9 / 25) | Itens revisados e prontos | 0 |
| Serviços com todos os desenhos | 1 de 10 (Eventos) | Serviços iniciados | 3 de 10 |
| Módulos com peças detalhadas | 2 de 12 | Atas registradas | 0 |
| Dias até o PDF da equipe / até o prazo | 17 / 19 | Entregas de A e B no repositório | 0 |

**Tabela 7 – Marcos do contrato**

| Período | O que se esperava | Situação |
|---|---|---|
| Semana 1 (até 13/10) | Contrato publicado; informações compartilhadas entregues a Phablo | Contrato publicado em 10/10; entregas de A e B pendentes (a da avaliação era devida em 10/10) |
| Semana 2 (14 a 20/10) | Um serviço completo por pessoa; Phablo fecha implantação, pacotes e modelo de dados | **Em andamento:** implantação e pacotes feitos; Eventos completo; modelo de dados depende de A e B |
| Semana 3 (21 a 27/10) | Tudo produzido e revisado | Não iniciada |
| Semana 4 (28/10 a 04/11) | Só correções e montagem do PDF | Não iniciada |

## 5. O que preocupa

1. **A e B ainda não têm nada no repositório**, e as informações que Phablo precisa para fechar o modelo de dados dependem deles. *Ação:* cobrar no próximo encontro.
2. **Nenhum item foi revisado.** São 34 itens e a regra é devolver em 1 dia. *Ação:* José Eduardo revisa os de Phablo e Phablo os de José Eduardo, anotando no fim de cada ficha.
3. **As capturas mostram o app em iPhone (loja App Store, versão 3.2.0)**, enquanto a visão geral de Phablo fala em Android, Play Store e versão 3.1.1. *Ação:* ajustar na revisão.
4. **Falta a tela de lista de Eventos** e parte das telas de RU e Notícias. *Ação:* obter as capturas e ajustar os itens.
5. **Faltam as atas** dos encontros de quarta, que contam na avaliação individual. *Ação:* registrar a de 14/10 e as próximas.
6. **Onde ficam regional e campus** na divisão em módulos ainda não está decidido. *Ação:* proposta de José Eduardo (módulo comum) para Phablo decidir.
7. **Segurança (versão web) pede login com a conta gov.br**, o que pode conflitar com a regra de usuário anônimo. *Ação:* Pessoa A confirmar.
8. **Documentos do início** (roteiro e guia de diagramas) divergem do contrato. *Ação:* vale o contrato; revisar ou remover.
9. **Prazo curto:** 17 dias para o PDF da equipe. *Ação:* priorizar o que sustenta outros serviços.

## 6. Próximos passos

**Até 20/10.** (1) A e B entregam a Phablo as informações compartilhadas e concluem ao menos um serviço completo. (2) Phablo recebe e junta as informações, monta o modelo de dados do sistema e inicia a tela inicial, a Rádio e o Guia. (3) José Eduardo obtém as capturas que faltam, ajusta Eventos e conclui RU e Notícias (sequências, estados, classes, contratos e regras), reaproveitando Eventos. (4) Revisões cruzadas entre C e D. (5) Atas de 14/10 e 21/10 e registro das conversas da equipe.

**21 a 27/10.** Terminar tudo, inclusive contratos e regras; fechar os casos de uso gerais e atualizar os módulos com o que os demais descobrirem; revisões em duplas (A com B, C com D); verificar a coerência entre os desenhos e montar a tabela de ligações entre eles.

**28/10 a 04/11.** Sem desenhos novos. Montar o PDF `INF0290-APS-Cinza` (autores em ordem alfabética, índice, legendas, referências, atas e comunicações), ler em conjunto, entregar à equipe em 2/11 e no SIGAA até 4/11.

## 7. Perguntas ao Prof. Juliano

1. O nível de detalhe combinado (um desenho de sequência para cada toque do usuário ou conversa com o servidor) atende à disciplina?
2. Um caso de uso geral por serviço, detalhado depois por cada responsável, é aceitável?
3. Como o app é descrito só pelas telas, algumas escolhas (como o formato das consultas ao servidor) são suposições de projeto, mantidas explícitas nos itens. Esse tratamento basta?

## 8. Como os próximos relatórios continuarão este

Este é o **ponto de partida**. Os próximos relatórios terão o mesmo formato e mostrarão **só o que mudou**: (1) resumo com os números da Tabela 6 comparados aos de hoje; (2) itens novos, alterados e revisados no período; (3) marcos da Tabela 7 atualizados; (4) decisões tomadas e mudanças nas regras; (5) preocupações resolvidas, novas e persistentes; (6) próximos passos. **Referência de hoje:** 34 itens produzidos e 0 prontos; 1 serviço completo de 10; 0 atas; versão principal do repositório no commit `3b06a17`.

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 3 e 11. IEEE, 2024. · INTERNATIONAL ORGANIZATION FOR STANDARDIZATION; INTERNATIONAL ELECTROTECHNICAL COMMISSION; INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **ISO/IEC/IEEE 12207:2026**: Systems and software engineering – Software life cycle processes. 2026. · UNIVERSIDADE FEDERAL DE GOIÁS. Instituto de Informática. **Definição de Atividades Práticas Supervisionadas (APS) da Disciplina**: INF 0290 – Projeto de Software, 2026/2. Goiânia, 2026. · EQUIPE CINZA. **Contrato Base – Equipe Cinza (APS INF0290)**. Repositório da equipe, 2026.
