# APS INF0290 – Divisão de Trabalho da Equipe Cinza

Oct 7, 2026 · @Phablo Tavares

## Princípio da divisão

Cada pessoa fica com uma fatia de funcionalidades e produz sozinha toda a cascata de diagramas dela (Apêndice D). Os artefatos que pertencem ao sistema inteiro, os "transversais", têm um dono que integra a contribuição de todos.

O motivo é o próprio enunciado: o Apêndice C critica o "esquartejamento" e o critério 4.2 avalia a consistência entre modelos. Se cada um fizer seu próprio modelo de dados ou sua própria arquitetura, a integração final quebra.

Somos 4 pessoas, chamadas aqui de A, B, C e D até definirmos os nomes.

## Pesos e justificativa

O trabalho total soma cerca de 28 pontos, ou 7 por pessoa. Os pesos foram estimados a partir dos prints do app e medem quanto cada parte gera de diagramas: quanto mais telas, estados, dados e regras, mais longa fica a cascata do Apêndice D.

| Parte | Por que tem esse peso | Peso |
| --- | --- | --- |
| Segurança | Só dois botões que abrem links externos (versão web e Play Store). Sem dados próprios. | 1 |
| Guia Estudantil | Só abre um PDF estático pelo Android. O app não modela o conteúdo. | 1 |
| Apps UFG | Lista fixa de 3 apps; tocar em qualquer parte abre a loja. | 1 |
| Notícias | Lista por regional; tocar abre link externo. Sem tela de detalhe. | 1 |
| Rádio | Grade semanal com abas por dia (horário, nome, descrição). O play só abre um site externo. | 2 |
| RU | Cardápio único para todos os restaurantes. Três refeições com categorias diferentes e seletor de dia (jantar sem sábado). Dados ricos, interação simples. | 2,5 |
| Eventos | Calendário com troca de mês, filtro por data, eventos com intervalo de datas e estado "sem eventos". | 3 |
| Locais | Lista que leva ao mapa com o local destacado, pinos por categoria e botão de GPS. Integração com mapa e permissão de localização. | 3,5 |
| Avaliação de UA: registrar | Funcionalidade nova, projetada do zero: dimensões, elementos, questões, notas de 0 a 5, validação e identificação do avaliador (hoje o app não tem login). | 6 |
| Avaliação de UA: consultar notas | Nota por UA, por área CNPq e da UFG, com as regras de cálculo das médias. | 3 |
| Transversais | Artefatos do sistema inteiro e integração do documento (ver seção própria). | 4 |

Todas as telas do app atual recarregam ao entrar e não têm cache. Sem internet, cada uma mostra um estado vazio ou uma mensagem de indisponibilidade. Esse comportamento é igual em todas, por isso é modelado uma vez só nos transversais.

## Divisão por pessoa

| Pessoa | Fatia | Peso | Revisor |
| --- | --- | --- | --- |
| A | Avaliação: registrar (dona do modelo de dados da avaliação) + Segurança | 7 | B |
| B | Avaliação: consultar notas (dona das regras de cálculo) + Locais + Apps UFG | 7,5 | A |
| C | Eventos + RU + Notícias | 6,5 | D |
| D | Transversais + Rádio + Guia Estudantil | 7 | C |

A Avaliação foi dividida em duas fatias com fronteira clara. A cuida de como uma avaliação nasce: estrutura de dimensões, elementos e questões, registro e validação. B cuida do que se calcula a partir dela: elementos → dimensão → avaliação → UA → área → UFG.

B também fica com Locais porque o Instituto de Informática aparece como local no mapa e como UA avaliada; o mesmo dono decide como os dois se relacionam. C fica com o padrão "lista do servidor filtrada por regional e data", comum a Eventos, Notícias e RU.

As revisões são em dupla (A↔B, C↔D): o revisor já conhece o contexto, e todos são autores e revisores sem revisar o próprio item (regra 5).

## O que são os transversais

Transversal é tudo o que não pertence a uma funcionalidade, mas atravessa todas. O Apêndice D pede vários desses itens como artefato único do sistema, então eles precisam de um dono (D) em vez de serem divididos.

- **Modelo conceitual de dados (diagrama + dicionário):** cada pessoa escreve as entradas das suas entidades; D junta tudo em um diagrama só e elimina duplicações e conflitos.
- **Diagrama de implantação:** app no celular, servidor/API, painel web e sistemas externos (navegador, Play Store, mapa, GPS, login).
- **Diagrama de pacotes:** camadas e módulos do app e suas dependências. Cada pessoa detalha os componentes e classes dos seus pacotes.
- **Casos de uso geral:** todos os atores e casos de uso numa visão só. Cada pessoa detalha os seus.
- **Componentes e padrões compartilhados:** abertura de link externo (usada por 6 funcionalidades), acesso à API e o padrão de estados de tela remota (carregando, exibindo, vazio, indisponível, recarregar ao voltar). Modelados uma vez; os outros só referenciam.
- **Tela inicial:** o menu com os 8 cartões, com protótipo de IHC e diagrama de estados.
- **Editoração do documento:** cabeçalho, nome do arquivo, índice, legendas, referências, apêndice de prompts de IA e apêndice de atas. Os critérios 1.1, 1.3 e 8.3 a 8.5 avaliam isso.

O peso 4 inclui autoria (implantação, pacotes, componentes comuns, tela inicial) e coordenação (integrar, apontar inconsistências e garantir a rastreabilidade do critério 5.2). Por isso D tem menos funcionalidades.

## Contrato inicial

Para cada um trabalhar sozinho sem conflitos depois, a equipe combina estes pontos nos primeiros dias, e D registra tudo num contrato:

- Ferramenta de modelagem, template de cada item (com autor e revisor) e convenções de nomes.
- Atores e o rascunho do diagrama de casos de uso geral.
- Granularidade da cascata: o que conta como "atividade" para gerar sequência e IHC. Confirmar com o professor.
- Entidades compartilhadas e seus donos: Regional e Campus (C), Unidade Acadêmica e Local (B), Usuário e identificação (A).
- Como o avaliador é identificado (por exemplo, o Login Único da UFG). Isso afeta a implantação de D.
- Esqueleto de pacotes e os componentes e padrões compartilhados.

Depois disso, qualquer mudança nesses pontos passa por D.

Ordem de produção dentro de cada fatia, para não refazer diagramas: casos de uso → atividades → IHC → entidades → componentes e classes → sequência → estados → contratos e regras E-C-A.

## Timeline (4 semanas)

> **Nota (19/10/2026):** esta timeline é o plano original. A ordem foi alterada: D integra o modelo de dados e os modelos gerais só depois das entregas das etapas 1 e 2 de A, B e C. A versão vigente está no `contrato-base.md`, seção 2, e a decisão em `Docs/decisoes.md`.

1. **Semana 1:** reunião de contrato nos primeiros 2 a 3 dias; depois, casos de uso, atividades e IHC de cada fatia. Marco: contrato publicado e entidades de todos entregues a D.
2. **Semana 2:** classes, sequências e estados. D fecha implantação, pacotes e modelo de dados integrado. Marco: cada pessoa com ao menos uma funcionalidade com a cascata completa.
3. **Semana 3:** terminar tudo, incluindo contratos e regras E-C-A; na segunda metade, revisões em dupla. Marco: tudo revisado.
4. **Semana 4:** correções, montagem do PDF por D e leitura final conjunta. Marco: entrega 2 dias antes do prazo.

Regras:

- Checkpoint semanal de 30 minutos, com ata. As atas viram apêndice e contam na avaliação individual.
- A entrega o modelo de dados da Avaliação até o meio da semana 1. Enquanto isso, B começa por Locais.
- Ninguém produz diagrama novo na semana 4.
