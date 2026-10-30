# Registro de uso de IA – Pessoa B (Maicon Brendo da Silva)

Formato de cada entrada: identificação da IA, URL, data de acesso, prompt completo e uso dado à resposta.
A referência ABNT que vai para a bibliografia aparece no fim de cada entrada.

## B-IA-01 – Modelagem completa da funcionalidade Apps UFG

- **IA:** Google. Antigravity (Gemini 2.5 Flash). Assistente de IA para Engenharia de Software.
- **URL:** antigravity.google.com
- **Data de acesso:** 29 de outubro de 2026.
- **Contexto fornecido:** Enunciado da APS (INF0290/UFG), contrato-base.md, capturas de tela do app Minha UFG v3.1.1 (telas inicial, Apps UFG, Segurança, Locais e Mapa) e pacotes Comum e Geral do repositório.
- **Uso da resposta:** Análise de engenharia reversa das telas reais de Apps UFG; formulação e refinamento participativo dos casos de uso (`DCdu-AppsUFG-01`), fluxo de atividades com raias (`DAtv-AppsUFG-01`), protótipo Salt com mapeamento de eventos (`DIhc-AppsUFG-01`), diagrama de classes e componentes com integração ao `ILinkExterno` (`DCla-AppsUFG-01`, `DCmp-AppsUFG-01`), diagrama de sequência (`DSeq-AppsUFG-01`), diagrama de estados de tela (`DEst-AppsUFG-01`), contratos formais de operação (`Contrato-AppsUFG-01`) e regras ativas Evento-Condição-Ação (`ECA-AppsUFG-01`).

### Prompt principal

> esse é o projeto final que nós precisamos fazer em grupo. houveram mudanças nas divisões das partes e atualmente eu sou responsável pelas partes: Locais + Apps UFG + Segurança. voce entendeu o projeto e consegue me ajudar? [...] primeiro de tudo, quero garantir que voce não faça nenhuma suposição de informações sobre o app. somente utilize o que já existe no repositório e quando formos trabalhar nas minhas funçoes, me pergunte exatamente o que precisa saber sobre o aplicativo para que eu lhe forneça as informações exatas. além disso, vamos fazer passo a passo tudo, e voce vai me informar o que voce irá trabalhar e validar comigo antes de gerar qualquer artefato. [...] vamos com a estratégia A [...] [fornecimento dos prints e dados exatos dos apps]

### Referência bibliográfica

GOOGLE. **Antigravity**. Assistente de IA para Engenharia de Software. Disponível em: https://antigravity.google.com. Acesso em: 29 out. 2026.

---

## B-IA-02 – Modelagem completa da funcionalidade Segurança

- **IA:** Google. Antigravity (Gemini 2.5 Flash). Assistente de IA para Engenharia de Software.
- **URL:** antigravity.google.com
- **Data de acesso:** 29 de outubro de 2026.
- **Contexto fornecido:** Captura da tela real "Minha UFG - Segurança" (v3.1.1), componentes compartilhados em Comum/ (`ILinkExterno`) e contrato da Equipe Cinza.
- **Uso da resposta:** Elaboração da cascata completa de diagramas e especificações para a funcionalidade Segurança: casos de uso (`DCdu-Seguranca-01`), fluxo de atividades com raias (`DAtv-Seguranca-01`), protótipo Salt (`DIhc-Seguranca-01`), classes e componentes (`DCla-Seguranca-01`, `DCmp-Seguranca-01`), sequências para Navegador e Play Store (`DSeq-Seguranca-01`, `DSeq-Seguranca-02`), diagrama de estados (`DEst-Seguranca-01`), contratos formais (`Contrato-Seguranca-01`) e regras E-C-A (`ECA-Seguranca-01`), além da renderização automatizada dos diagramas PNG via script Python.

### Prompt principal

> antes de irmos para a parte de seguranças, precisamos dos .png dos diagramas. voce consegue renderizar a partir do .puml ou devo usar outra ferramenta (qual)? [...] vamos iniciar o alinhamento [...] [validação de cada decisão e autorização para geração completa dos artefatos]

### Referência bibliográfica

GOOGLE. **Antigravity**. Assistente de IA para Engenharia de Software. Disponível em: https://antigravity.google.com. Acesso em: 29 out. 2026.

---

## B-IA-03 – Modelagem completa da funcionalidade Locais

- **IA:** Google. Antigravity (Gemini 2.5 Flash). Assistente de IA para Engenharia de Software.
- **URL:** antigravity.google.com
- **Data de acesso:** 30 de outubro de 2026.
- **Contexto fornecido:** Capturas reais do Campus Samambaia (Aba Lista de Locais e Aba Mapa com marcadores coloridos e botão flutuante de GPS), contrato-base.md (propriedade das entidades compartilhadas Local e UnidadeAcademica) e componentes reutilizáveis de Comum/ (`IProvedorMapa`, `ILocalizacao`, `IControladorTelaRemota`, `IAcessoApi`).
- **Uso da resposta:** Modelagem conceitual e comportamental completa de Locais: Casos de Uso (`DCdu-Locais-01`), fluxos de atividades modulares para cada caso de uso (`DAtv-Locais-01`, `DAtv-Locais-02`, `DAtv-Locais-03`), protótipos de tela Salt para a lista e para o mapa (`DIhc-Locais-01`, `DIhc-Locais-02`), Dicionário de Dados oficial de `Local` e `UnidadeAcademica` (`DD-Locais-01`), diagramas de classes de interface, controle, dados e domínio (`DCla-Locais-01`, `DCla-Locais-02`), componentes com dependências arquiteturais (`DCmp-Locais-01`), diagramas de sequência para carga remota, foco no mapa e centralização GPS (`DSeq-Locais-01`, `DSeq-Locais-02`, `DSeq-Locais-03`), diagrama de estados de tela (`DEst-Locais-01`), contratos formais de operação (`Contrato-Locais-01`) e regras ativas Evento-Condição-Ação (`ECA-Locais-01`), além de correções geométricas de layout e renderização de todos os diagramas em PNG.

### Prompt principal

> então, a lista de locais aparentemente vem de uma api. portanto acho que não precisamos listar todos os locais, podemos apenas definir a estrutura dessa classe. como foi feito para eventos [...] me explique como funciona essa diferenciação entre UA e não UA? [...] como funciona a implementação do mapa com gps no aplicativo e como funciona o clique no local abrindo o local no mapa [...] [validação modular passo a passo da cascata inteira de Locais]

### Referência bibliográfica

GOOGLE. **Antigravity**. Assistente de IA para Engenharia de Software. Disponível em: https://antigravity.google.com. Acesso em: 30 out. 2026.
