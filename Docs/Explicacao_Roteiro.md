# 🚀 Guia Mestre e Planejamento do Projeto Final de APS: Sistema "Minha UFG"
**Disciplina:** Projeto de Software - NBC (INF0290) - UFG 2026/2  
**Docente:** Prof. Juliano Lopes de Oliveira  
**Estudante:** Maicon Brendo da Silva | **Equipe:** Cinza  
**Data de Entrega:** 03/11/2026 (via SIGAA)  

---

## 📌 1. Visão Geral do Projeto e Escopo do Software

O trabalho de Atividades Práticas Supervisionadas (APS) consiste em **analisar e projetar o aplicativo móvel (App) do Sistema de Informação "Minha UFG"**, aplicando de forma rigorosa os conceitos de Engenharia e Design de Software vistos em aula.

O trabalho exige uma abordagem combinada em duas frentes de modelagem:
1. **Engenharia Reversa da Versão Atual do App:** Modelar as 8 funcionalidades que o aplicativo móvel já implementa:
   * **Segurança:** Solicitação de apoio imediato à central de segurança da UFG.
   * **Rádio:** Programação semanal e streaming ao vivo da Rádio UFG.
   * **Guia Estudantil:** Guia de oportunidades e serviços ao discente.
   * **Eventos:** Busca e navegação de eventos por regional e data.
   * **Notícias:** Feed de notícias atualizadas por regional da UFG.
   * **Restaurante Universitário (RU):** Cardápio semanal dos RUs.
   * **Locais:** Mapa digital interativo de pontos de interesse e unidades na UFG.
   * **Apps UFG:** Catálogo e download de outros aplicativos institucionais.
2. **Engenharia Avante (Evolução / Extensão do App):** Projetar a estrutura e o comportamento de uma **nova funcionalidade**:
   * **Avaliação de Qualidade das Unidades Acadêmicas (UAs):** Permitir que a comunidade acadêmica avalie as UAs (ex: INF, Faculdade de Medicina, etc.).
   * **Dimensões de Qualidade:** Agrupamento de elementos educacionais (ex: *Infraestrutura Física* com salas/laboratórios/banheiros; *Corpo Docente* com qualificação/regime de trabalho; *Recursos Pedagógicos* com bibliografia/materiais; *Condições Ambientais* com ruído/iluminação/climatização).
   * **Mecanismo de Avaliação:** Notas de 0 a 5 em questões sobre cada elemento. A média dos elementos gera a nota da dimensão; a média das dimensões gera a nota final da UA.
   * **Visualização de Indicadores:** Exibição da nota por UA individual, nota média por área de conhecimento (CNPq) e nota média geral da UFG.

---

## 📋 2. Regras de Entrega, Formatação e Avaliação

### 📝 Formato do Documento
* **Arquivo Único PDF:** Nomeado estritamente como `INF0290-APS-Cinza.pdf`.
* **Estrutura Exigida:**
  * **Cabeçalho:** Identificação da disciplina, tarefa e integrantes da equipe em ordem alfabética.
  * **Seção I: Projeto Estrutural** (modelos estáticos).
  * **Seção II: Projeto Comportamental** (modelos dinâmicos).
  * **Referências Bibliográficas:** Citação adequada de todas as fontes (SWEBOK v4, ISO/IEC/IEEE 12207:2026, etc.) e **citação obrigatória de ferramentas de IA Generativa** utilizadas, especificando os prompts completos aplicados (em apêndice se forem longos).
  * **Apêndices:** Registros de reuniões/comunicações da equipe e apêndices de prompts de IA.

### 👥 Regra Cruzada de Autoria e Revisão
* Cada item de informação/modelo **deve identificar explicitamente o seu Autor e o seu Revisor**.
* **Regra Rígida:** A mesma pessoa **não pode ser autora e revisora do mesmo item**. Todos os membros da equipe devem atuar em ambos os papéis cruzados.

### 🛡️ Composição da Equipe Cinza
Integrantes oficiais da sua equipe:
* Daniel Noleto de Oliveira
* José Eduardo Gontijo de Carvalho
* **Maicon Brendo da Silva**
* Phablo Tavares Paixão
* Waldson Ferreira Barbosa Júnior

---

## 📐 3. Detalhamento de Cada Modelo Necessário (Apêndice D)

A especificação exige uma hierarquia estruturada de modelos cobrindo as visões estática e dinâmica:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        HIERARQUIA DE MODELOS                           │
├───────────────────────────────────┬────────────────────────────────────┤
│         MODELO ESTRUTURAL         │        MODELO COMPORTAMENTAL       │
├───────────────────────────────────┼────────────────────────────────────┤
│ 1. Esquema Conceitual de BD       │ 1. Diagramas de Casos de Uso (DCdu)│
│    • Diagrama de Dados (sem op/atrib)│ 2. Diagramas de Atividades (DAtv)  │
│    • Dicionário de Dados (DD)     │ 3. Diagramas de Sequência (DSeq)   │
│ 2. Estrutura Externa             │ 4. Protótipos e Diag. IHC (DIhc)   │
│    • Diagrama de Implantação      │ 5. Diag. Transição Estados (DEst)  │
│ 3. Estrutura Interna              │ 6. Contratos de Operação           │
│    • Diagrama de Pacotes (DPac)   │ 7. Especificação de Regras E-C-A   │
│    • Diagramas de Componentes     │                                    │
│    • Diagramas de Classes (DCla)  │                                    │
└───────────────────────────────────┴────────────────────────────────────┘
```

### A. Modelos Estruturais (Visão Estática)
1. **Esquema Conceitual de Banco de Dados:**
   * **Diagrama de Dados:** Diagrama de Classes enxuto, mostrando apenas as entidades conceituais e suas associações/cardinalidades (sem operações e sem atributos visíveis).
   * **Dicionário de Dados (DD):** Tabela detalhando cada entidade, especificando o nome de todos os atributos, tipos de dados, restrições e chaves.
2. **Estrutura Externa (Arquitetura de Implantação):**
   * **Diagrama de Implantação:** Mapeia a distribuição física do software em nós de hardware/plataformas (Dispositivo Móvel Android/iOS, Servidores Web/Aplicação UFG, Servidor de SGBD) e os protocolos de comunicação (HTTPS, REST/JSON, WSS).
3. **Estrutura Interna (Decomposição Modular):**
   * **Diagrama de Pacotes (DPac):** Organiza o sistema em módulos de alto nível (ex: `ui`, `security`, `radio`, `evaluation`, `persistence`) exibindo suas dependências.
   * **Diagrama de Componentes (DCmp):** Para cada pacote, detalha os blocos modulares internos, suas interfaces fornecidas/requeridas e dependências físicas.
   * **Diagrama de Classes (DCla):** Para cada componente, apresenta o diagrama de classes detalhado completo, contendo atributos com visibilidade, operações com assinaturas/parâmetros e relacionamentos de associação, agregação, composição e herança.

### B. Modelos Comportamentais (Visão Dinâmica)
1. **Diagrama de Casos de Uso (DCdu):** Mapeia os atores (Discente, Docente, Comunidade, Central de Segurança) e todas as funcionalidades/casos de uso do sistema (as 8 atuais + as novas de avaliação).
2. **Diagrama de Atividades (DAtv):** Para cada caso de uso, detalha o fluxo de controle e decisões, utilizando raias de atividade (*swimlanes*) para separar as ações do usuário e do aplicativo.
3. **Diagrama de Sequência (DSeq):** Para cada atividade, demonstra a troca temporal síncrona/assíncrona de mensagens entre os objetos em tempo de execução para satisfazer o fluxo.
4. **Diagrama e Protótipo de IHC (DIhc):** Protótipo visual das telas do aplicativo móvel, mapeando os eventos de interação do usuário (toques, gestos, submissões).
5. **Diagrama de Transição de Estados (DEst):** Para cada tela/componente de IHC, detalha a máquina de estados reativa e as transições causadas pelos eventos do usuário.
6. **Especificação de Contratos de Operação:** Para cada operação de classe em DCla, define formalmente o contrato contendo pré-condições, pós-condições e invariantes.
7. **Regras Ativas (E-C-A):** Especificação de regras do tipo Evento-Condição-Ação para disparos automáticos (ex: ao atingir nota média < 2.0 em uma dimensão, disparar alerta automático de auditoria).

---

## 🧭 4. Roteiro Prático de Trabalho em 5 Etapas ("Dividir e Conquistar")

Para evitar o erro de "esquartejar" o trabalho sem integração, a Equipe Cinza deve seguir o princípio de **decomposição lógica e integração contínua**:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        ROTEIRO DE EXECUÇÃO                             │
│                                                                        │
│  [Etapa 1] Alinhamento & Engenharia de Requisitos (Semanas 05-06)      │
│      └─► [Etapa 2] Projeto da Estrutura de Alto Nível (Semanas 07-09)  │
│              └─► [Etapa 3] Projeto Comportamental e IHC (Semanas 10-11)│
│                      └─► [Etapa 4] Detalhamento Estrutural (Semana 12) │
│                              └─► [Etapa 5] Auditoria, Revisão e Envio  │
└────────────────────────────────────────────────────────────────────────┘
```

### 🗓️ Etapa 1: Alinhamento de Escopo & Elicitação de Requisitos
* **Ação:** Reunião síncrona da Equipe Cinza para listar todos os 8 módulos atuais + o módulo de Avaliação de UAs.
* **Entregáveis:** Lista padronizada de Casos de Uso e Dicionário de Termos do Domínio.
* **Membros responsáveis:** Atribuição inicial de autores/revisores.

### 🗓️ Etapa 2: Projeto da Estrutura de Alto Nível & Casos de Uso
* **Ação:** Construir a arquitetura macro do app antes de desenhar classes individuais.
* **Entregáveis:**
  1. Diagrama de Casos de Uso (DCdu).
  2. Diagrama de Implantação (Estrutura Externa).
  3. Diagrama de Pacotes (DPac) e Diagrama de Dados do BD.

### 🗓️ Etapa 3: Modelagem Comportamental Detalhada & Protótipos de IHC
* **Ação:** Mapear a dinâmica de funcionamento das telas e a troca de mensagens.
* **Entregáveis:**
  1. Protótipos de IHC (DIhc) das telas do app e seus Diagramas de Estados (DEst).
  2. Diagramas de Atividades (DAtv) dos fluxos principais.
  3. Diagramas de Sequência (DSeq) detalhando as chamadas de métodos.

### 🗓️ Etapa 4: Detalhamento Estrutural Interno & Contratos
* **Ação:** Refinar o Diagrama de Classes e Componentes com base nos métodos descobertos nos diagramas de sequência.
* **Entregáveis:**
  1. Diagrama de Componentes (DCmp) e Diagrama de Classes (DCla) completo.
  2. Dicionário de Dados (DD) completo com atributos e tipos.
  3. Especificação dos Contratos de Operação e Regras E-C-A.

### 🗓️ Etapa 5: Auditoria de Rastreabilidade, Revisão Cruzada e Compilação PDF
* **Ação:** Verificar a consistência inter-modelos (ex: métodos do Diagrama de Sequência declarados no Diagrama de Classes).
* **Entregáveis:**
  1. Revisão cruzada obrigatória (Autor X Revisor trocados).
  2. Compilação do relatório único em PDF: `INF0290-APS-Cinza.pdf`.
  3. Registro das atas de reuniões e apêndice com citação de IAs no documento.
  4. Submissão no SIGAA até **03/11/2026**.

---

## 🏆 5. Checklist de Qualidade do SWEBOK antes de Enviar

- [ ] **Conformidade:** O PDF está nomeado como `INF0290-APS-Cinza.pdf` e contém os autores e revisores devidamente cruzados?
- [ ] **Completude:** As 8 funcionalidades originais do app E a extensão de avaliação de UAs foram contempladas?
- [ ] **Consistência:** Os métodos usados no Diagrama de Sequência batem exatamente com as assinaturas de operações do Diagrama de Classes?
- [ ] **Rastreabilidade:** É possível rastrear um requisito do Caso de Uso até o protótipo de tela e sua classe de controle?
- [ ] **Ética e IA:** Todos os prompts utilizados em IAs gerativas foram citados no Apêndice conforme o Guia da UFG?
