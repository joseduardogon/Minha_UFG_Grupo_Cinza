# 🎨 Guia Didático Completo dos Diagramas do Projeto APS (Minha UFG)

**Disciplina:** Projeto de Software (INF0290) - UFG 2026/2  
**Projeto:** Engenharia Reversa e Evolução do Aplicativo "Minha UFG"  
**Foco:** Manual Didático Prático de Modelagem Estrutural e Comportamental (UML)  

---

## 🎯 Apresentação do Guia

Este guia foi elaborado para transformar a especificação técnica do Apêndice D do trabalho em um manual de construção visual altamente acessível. Mesmo que alguém do grupo nunca tenha desenhado um diagrama UML, este documento explica de forma didática e passo a passo **o que é**, **quais informações foca**, **como construir elemento por elemento** e **como aplicar no contexto real do app Minha UFG** cada um dos modelos exigidos pelo professor Juliano.

---

# 🌐 PARTE I: MODELOS ESTRUTURAIS (VISÃO ESTÁTICA)

Os modelos estruturais mostram como o software é organizado por dentro e instalado por fora. Eles representam o sistema "em repouso" (a arquitetura, as tabelas, as classes, os arquivos e o hardware).

---

## 1. Diagrama de Implantação (Dimp)

### ❓ O que é e qual o seu objetivo?
Pense no Diagrama de Implantação como a **planta de infraestrutura física e de rede** do sistema. Ele não mostra código nem classes, mas sim **onde** o software roda no mundo real: quais servidores, smartphones, bancos de dados e serviços em nuvem existem, e como eles conversam entre si pela internet.

### 🔍 Quais informações ele foca?
*   **Hardware / Ambientes (Nós):** Dispositivos físicos ou virtuais (ex: "Smartphone Android/iOS", "Servidor de Aplicação AWS", "Servidor de BD PostgreSQL").
*   **Artefatos Executáveis:** O que está instalado em cada nó (ex: `minha-ufg.apk`, `backend-api.jar`).
*   **Protocolos de Comunicação:** Como os nós conversam (ex: HTTPS, REST API, JDBC, WebSocket).

### 🛠️ Como é construído? (Notação e Elementos)
1.  **Nó (Node):** Desenhado como um **cubo tridimensional**. Representa um ambiente de execução ou hardware.
2.  **Artefato (Artifact):** Um retângulo com a palavra `<<artifact>>` ou um ícone de documento no canto superior. Fica dentro do cubo do Nó.
3.  **Caminho de Comunicação (Communication Path):** Uma linha contínua conectando dois cubos, rotulada com o protocolo de rede (ex: `<<HTTPS/REST>>`).

### 📱 Aplicação Prática no "Minha UFG":
*   **Nó 1 (Cliente):** Cubo "Smartphone do Estudante (Android / iOS)" contendo o artefato `MinhaUFG_App.apk`.
*   **Nó 2 (Servidor Web/API):** Cubo "Servidor de Aplicação CERCOMP/UFG" rodando `API_Gateway_UFG`.
*   **Nó 3 (Servidor de Banco de Dados):** Cubo "Servidor de BD Relacional" rodando `PostgreSQL_Database`.
*   **Conexões:** Linha entre Smartphone e Servidor API rotulada como `<<HTTPS / JSON REST>>`. Linha entre Servidor API e Banco de Dados rotulada como `<<JDBC / SQL>>`.

---

## 2. Diagrama de Pacotes (DPac)

### ❓ O que é e qual o seu objetivo?
O Diagrama de Pacotes é a **pasta do projeto em alto nível**. Quando um software fica muito grande, colocar todas as centenas de classes em um desenho só gera um "diagrama espaguete". O Diagrama de Pacotes organiza o sistema em módulos/camadas lógicas (ex: Visão, Negócio, Persistência).

### 🔍 Quais informações ele foca?
*   **Organização Modular:** Divisão do sistema em subsistemas/camadas.
*   **Dependências Arquiteturais:** Quem pode enxergar ou usar quem (direção das setas).

### 🛠️ Como é construído? (Notação e Elementos)
1.  **Pacote (Package):** Desenhado como uma **pasta de arquivos (um retângulo com uma aba superior menor)**.
2.  **Dependência (`<<use>>` ou `<<import>>`):** Uma **seta tracejada** que vai do pacote que usa para o pacote que é usado.

### 📱 Aplicação Prática no "Minha UFG":
*   **Pacote `br.ufg.minhaufg.ui` (Interface):** Contém as telas (Notícias, Cardápio, Avaliação).
*   **Pacote `br.ufg.minhaufg.domain` (Regras de Negócio):** Contém a lógica de cálculo de médias das UAs e regras de matrícula.
*   **Pacote `br.ufg.minhaufg.data` (Persistência/API):** Contém a comunicação com o banco de dados e APIs externas.
*   **Regra de Dependência:** `ui` apontará com seta tracejada para `domain`, e `domain` apontará para `data`. Jamais o contrário!

---

## 3. Esquema Conceitual de Dados (Diagrama de Classes de Dados + Dicionário de Dados)

### ❓ O que é e qual o seu objetivo?
É a **planta baixa do Banco de Dados** do aplicativo. Ele define como as informações serão armazenadas no banco relacional de forma persistente.

### 🔍 Quais informações ele foca?
*   **Tabelas/Entidades de Dados:** Entidades que precisam ser salvas (ex: `Estudante`, `UnidadeAcademica`, `Avaliacao`).
*   **Atributos e Tipos:** O nome de cada campo e seu tipo de dado (ex: `id: Long`, `nota: Double`, `comentario: String`).
*   **Relacionamentos e Cardinalidades:** Como as tabelas se conectam (1:1, 1:N, N:N).
*   **Atenção:** **NÃO possui métodos/operações!** Apenas atributos de dados.

### 🛠️ Como é construído? (Notação e Elementos)
1.  **Classes de Dados:** Retângulos divididos em duas partes (Nome da entidade e Atributos).
2.  **Chave Primária (PK) e Chave Estrangeira (FK):** Marcadas com `<<PK>>` ou `<<FK>>`.
3.  **Dicionário de Dados (Tabela Auxiliar):** Uma tabela textual que explica detalhadamente cada atributo, dizendo se é obrigatório (NOT NULL), o tamanho máximo e a regra de preenchimento.

### 📱 Aplicação Prática no "Minha UFG":
*   **Entidade `UnidadeAcademica`:** Atributos `idUA`, `nome`, `sigla`, `centroRegiao`.
*   **Entidade `AvaliacaoUA`:** Atributos `idAvaliacao`, `notaEstrutura`, `notaCorpoDocente`, `comentario`, `dataAvaliacao`.
*   **Relacionamento:** 1 `UnidadeAcademica` possui N `AvaliacaoUA` (1 : 0..*).

---

## 4. Diagrama de Componentes (DCmp)

### ❓ O que é e qual o seu objetivo?
Se o Diagrama de Pacotes mostra pastas lógicas, o Diagrama de Componentes mostra **blocos reutilizáveis de software real** (módulos, APIs, bibliotecas, JARs, serviços). Ele descreve as interfaces de entrada e saída que cada componente expõe.

### 🔍 Quais informações ele foca?
*   **Componentes do Sistema:** Módulos autônomos de código (ex: `ModuloAutenticacao`, `ServicoAvaliacaoUA`).
*   **Interfaces Fornecidas (Provided Interfaces):** O que o componente oferece para os outros usarem (ícone da **tomada fêmea / círculo com haste**).
*   **Interfaces Requeridas (Required Interfaces):** O que o componente precisa que os outros forneçam (ícone do **plugue macho / semi-círculo com haste**).

### 🛠️ Como é construído? (Notação e Elementos)
1.  **Componente:** Um retângulo com a palavra `<<component>>` e dois pequenos retângulos sobrepostos na borda esquerda.
2.  **Interface Provida (Ball):** Círculo em linha contínua ligado ao componente.
3.  **Interface Requerida (Socket):** Semi-círculo envolvente ligado ao componente dependente.

### 📱 Aplicação Prática no "Minha UFG":
*   **Componente `ServicoNoticias`:** Fornece a interface `INoticias` (para a tela de feed ler).
*   **Componente `ModuloAvaliacao`:** Requer a interface `IAutenticacao` (para garantir que só estudante logado avalie) e fornece `IAvaliacaoUA`.

---

## 5. Diagrama de Classes Detalhado (DCla)

### ❓ O que é e qual o seu objetivo?
É o **blueprint mais detalhado do código-fonte em Orientação a Objetos**. Ele é o mapa exato que um programador Java lê para criar as classes, atributos, métodos, modificadores de acesso e heranças.

### 🔍 Quais informações ele foca?
*   **Estrutura completa das classes:** Nome, Atributos e Métodos com parâmetros e tipos de retorno.
*   **Visibilidade:** `+` (público), `-` (privado), `#` (protegido).
*   **Relações formais:** Associação, Agregação, Composição, Herança (Generalização) e Interface (Realização).

### 🛠️ Como é construído? (Notação e Elementos)
1.  **Caixa de Classe:** Retângulo dividido em **3 seções**:
    *   Topo: Nome da Classe (ex: `AvaliacaoController`).
    *   Meio: Atributos privados (ex: `- notaFinal: double`).
    *   Base: Métodos públicos (ex: `+ registrarAvaliacao(dt: AvaliacaoDTO): boolean`).
2.  **Herança:** Seta com triângulo vazado apontando para a Superclasse.
3.  **Composição (Diamante Preenchido):** Indica vínculo forte de ciclo de vida (se o todo morre, a parte morre).
4.  **Agregação (Diamante Vazado):** Indica vínculo fraco (a parte existe sem o todo).

---

# ⚡ PARTE II: MODELOS COMPORTAMENTAIS (VISÃO DINÂMICA)

Os modelos comportamentais mostram o software "em movimento". Eles descrevem como o sistema reage a cliques do usuário, troca mensagens ao longo do tempo e muda de estado.

---

## 6. Diagrama de Casos de Uso (DCdu)

### ❓ O que é e qual o seu objetivo?
É o mapa de **fronteira e escopo do sistema do ponto de vista do usuário**. Ele responde à pergunta: *"Quem usa o sistema e o que essa pessoa consegue fazer nele?"*.

### 🔍 Quais informações ele foca?
*   **Atores (Actors):** Pessoas ou sistemas externos que interagem com o app (ex: "Estudante", "Professor", "Sistema SIGAA").
*   **Casos de Uso (Use Cases):** As funcionalidades de valor (ex: "Avaliar Unidade Acadêmica", "Consultar Cardápio").
*   **Relações de Inclusão (`<<include>>`):** Passos obrigatórios (ex: para Avaliar UA, é **obrigatório** "Autenticar Usuário").
*   **Relações de Extensão (`<<extend>>`):** Passos opcionais/condicionais (ex: ao Avaliar UA, o usuário **pode opcionalmente** "Anexar Foto da Estrutura").

### 🛠️ Como é construído? (Notação e Elementos)
1.  **Ator:** Boneco de palito (*stick figure*) fora da caixa do sistema.
2.  **Caso de Uso:** Uma **elipse na horizontal** contendo um verbo no infinitivo (ex: `Avaliar Unidade Acadêmica`).
3.  **Limite do Sistema (System Boundary):** Um grande retângulo envolvendo as elipses, deixando os atores do lado de fora.

---

## 7. Diagrama de Atividades (DAtv)

### ❓ O que é e qual o seu objetivo?
Pense no Diagrama de Atividades como um **fluxograma avançado**. Ele mostra o passo a passo lógico e sequencial de um processo de negócio, incluindo decisões (`if/else`), caminhos paralelos e divisões de responsabilidades.

### 🔍 Quais informações ele foca?
*   **Fluxo de passos:** A ordem em que os cliques e ações do sistema acontecem.
*   **Pontos de Decisão (Losangos):** Bifurcações no caminho (ex: "Nota válida? Sim / Não").
*   **Raias de Atividade (Swimlanes):** Colunas que dividem de quem é a responsabilidade de cada passo (ex: Coluna "Usuário", Coluna "Aplicativo", Coluna "Servidor Backend").

### 🛠️ Como é construído? (Notação e Elementos)
1.  **Início:** Círculo preto preenchido.
2.  **Fim:** Círculo preto dentro de outro círculo (alvo).
3.  **Atividade (Ação):** Retângulo com cantos arredondados.
4.  **Decisão (Losango):** Caminhos com condições de guarda entre colchetes (ex: `[Nota > 0]`).
5.  **Raias (Swimlanes):** Linhas verticais organizando as colunas de atores/sistemas.

---

## 8. Diagrama de Sequência (DSeq)

### ❓ O que é e qual o seu objetivo?
É o diagrama dinâmico mais importante da engenharia de software! Ele detalha a **troca de mensagens em ordem cronológica (de cima para baixo)** entre as telas, controllers e banco de dados para realizar **um** caso de uso específico.

### 🔍 Quais informações ele foca?
*   **Linhas de Vida (Lifelines):** Os objetos ou componentes que participam da cena (alinhados no topo).
*   **Barra de Ativação:** Retângulos verticais indicando o tempo em que o objeto está executando algo.
*   **Mensagens Síncronas (Seta Preenchida `->`):** Chamadas de métodos que esperam resposta.
*   **Mensagens de Retorno (Seta Tracejada `<--`):** Respostas de dados voltando.

### 🛠️ Como construir passo a passo:
1.  Coloque no topo, da esquerda para a direita: `[Ator] -> [Tela/IHC] -> [Controller] -> [Servidor/BD]`.
2.  Desenhe uma linha tracejada vertical descendo de cada elemento (Linha de Vida).
3.  Desenhe setas horizontais ordenadas de cima para baixo representando cada chamada de método (ex: `1: clicarSalvar()`, `2: validarDados()`, `3: INSERT no Banco`).

---

## 9. Protótipos de Tela / Diagramas de IHC (DIhc)

### ❓ O que é e qual o seu objetivo?
São os **wireframes/layouts visuais das telas do aplicativo**. Eles mostram como o usuário enxerga e interage com o Minha UFG na prática (botões, formulários, listas, menus).

### 🔍 Quais informações ele foca?
*   Layout da Interface de Usuário (User Interface - UI).
*   Disposição dos elementos gráficos (Campos de texto, botões de estrela para nota, imagens, barras de navegação).

---

## 10. Diagrama de Transição de Estados da Interface (DEst)

### ❓ O que é e qual o seu objetivo?
Mostra o **ciclo de vida das telas ou de uma entidade**. No contexto de IHC do nosso trabalho, ele mapeia **como o aplicativo navega entre as telas** a partir de ações do usuário (cliques em botões).

### 🔍 Quais informações ele foca?
*   **Estados:** A tela atual em que o usuário está (ex: `TelaInicial`, `TelaFormularioAvaliacao`, `TelaSucesso`).
*   **Transições:** As setas conectando os estados, rotuladas pelo evento que disparou a mudança (ex: `clicarBotãoAvaliar()`).

---

## 11. Especificação de Contratos de Operação e Regras Ativas (E-C-A)

### ❓ O que é e qual o seu objetivo?
É a **documentação textual/formal das regras mais críticas do sistema**.
*   **Contratos de Operação:** Definem rigorosamente as **Pré-condições** (o que precisa ser verdade antes de executar um método) e as **Pós-condições** (o que muda no sistema depois que o método roda).
*   **Regras Ativas (E-C-A: Evento-Condição-Ação):** Mapeiam reações automáticas do sistema no formato: **QUANDO** [Evento] acontece, **SE** [Condição] for verdadeira, **FAÇA** [Ação].

### 📱 Exemplo no "Minha UFG":
*   **Contrato de Operação `submeterAvaliacao()`:**
    *   *Pré-condição:* Estudante precisa estar autenticado com vínculo ativo no SIGAA.
    *   *Pós-condição:* Nova instância de `AvaliacaoUA` criada no banco e média da UA recalculada.
*   **Regra Ativa ECA (Alerta de Nota Baixa):**
    *   **Evento:** Nova avaliação registrada.
    *   **Condição:** Nota da estrutura da UA < 2.0.
    *   **Ação:** Disparar notificação automática para a ouvidoria da UFG.

---

# 🚀 RESUMO DA OPERAÇÃO PARA A EQUIPE CINZA

| Modelo UML | Foco Principal | Dica de Ouro do Tutor |
| :--- | :--- | :--- |
| **Implantação (Dimp)** | Hardware/Infra | Não desenhe classes aqui, use cubos para os servidores/smartphones. |
| **Pacotes (DPac)** | Pastas/Camadas | Garanta que as setas de dependência vão da UI para o Domínio. |
| **Dados (Conceitual)** | Banco de Dados | Coloque apenas atributos de dados, zero métodos. Crie o Dicionário de Dados! |
| **Componentes (DCmp)** | Módulos executáveis | Use os ícones de tomada e plugue (provido/requerido). |
| **Classes (DCla)** | Código Java | Coloque visibilidade (+/-), atributos, métodos e tipos de retorno. |
| **Casos de Uso (DCdu)** | Escopo do Usuário | Mantenha os atores fora da caixa do sistema. Verbos no infinitivo. |
| **Atividades (DAtv)** | Fluxograma | Use raias (Swimlanes) para separar o Usuário do Servidor. |
| **Sequência (DSeq)** | Tempo/Mensagens | Ordene as chamadas de cima para baixo com setas de métodos. |
| **Protótipos (DIhc)** | Telas/UI | Desenhe as telas do app para a nova função de Avaliar UAs. |
| **Estados (DEst)** | Navegação de telas | Mostre qual botão leva de qual tela para qual tela. |
| **Contratos / ECA** | Regras de Negócio | Escreva Pré/Pós condições e regras no formato Evento-Condição-Ação. |
