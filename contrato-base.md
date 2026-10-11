# Contrato Base – Equipe Cinza (APS INF0290)

Regras que todos seguem para produzir sua fatia sem conflitos na integração. Responsável pelo contrato: **Pessoa D**.

## 1. Equipe e fatias

| Pessoa | Fatia | Revisor |
|---|---|---|
| A | Avaliação: registrar + Segurança | B |
| B | Avaliação: consultar notas + Locais + Apps UFG | A |
| C | Eventos + RU + Notícias | D |
| D | Transversais + Rádio + Guia Estudantil | C |

## 2. Datas

- Entrega no SIGAA: **04/11/2026, 23h59**.
- Entrega interna (PDF pronto): **02/11/2026**.
- Checkpoint semanal: **quartas, 19h**, 30 min, com ata.

| Semana | Período | Marco |
|---|---|---|
| 1 | até 13/10 | Contrato publicado; entidades de todos entregues a D |
| 2 | 14/10 a 20/10 | Cada pessoa com ao menos uma funcionalidade com a cascata completa; D fecha implantação, pacotes e modelo de dados integrado |
| 3 | 21/10 a 27/10 | Tudo produzido (incluindo contratos e regras E-C-A) e revisado |
| 4 | 28/10 a 04/11 | Só correções e montagem do PDF. Nenhum diagrama novo |

A entrega o modelo de dados da Avaliação até 10/10. Enquanto isso, B começa por Locais.

## 3. Ferramentas

- Todos os diagramas em **PlantUML**, inclusive os protótipos de IHC (Salt). Estilo visual padrão do PlantUML, sem tema.
- Tudo versionado no **repositório GitHub** da equipe.
- Comunicação: grupo de **WhatsApp**.

## 4. Convenções

- **Nome de arquivo e de diagrama:** `<TIPO>-<Funcionalidade>-<nn>`. Ex.: `DAtv-RU-01`, `DSeq-AvalRegistrar-02`.
- **Tipos:** DDados (diagrama de dados), DD (dicionário), DImp, DPac, DCmp, DCla, DCdu, DAtv, DSeq, DIhc, DEst, Contrato, ECA.
- **Elementos dos modelos:** em português, `camelCase` para atributos e operações, `PascalCase` para classes.
- **Template de cada item de informação:**
  - Código e título
  - Autor / Revisor
  - Rastreia para (itens relacionados)
  - Diagrama
  - Descrição
  - Referências
- **Referências bibliográficas:** ABNT.

## 5. Atores

- **Membro da comunidade UFG** (anônimo)
- **Avaliador** (membro da comunidade que registra avaliação; anônimo)
- **Servidor/API**
- **Painel web**
- **Play Store / navegador**
- **Provedor de mapa / GPS**

D publica o rascunho do diagrama de casos de uso geral; cada pessoa detalha os casos de uso da sua fatia, sem limite de quantidade: os que forem necessários para cobrir a funcionalidade por completo.

## 6. Granularidade da cascata

- **Atividade** = cada ação do DAtv em que o usuário interage com o app ou o app interage com o servidor/sistema externo. Cada uma gera um DSeq.
- Passos internos triviais não geram DSeq.
- Ordem de produção: casos de uso → atividades → IHC → entidades → componentes e classes → sequência → estados → contratos e regras E-C-A.

## 7. Entidades compartilhadas

| Entidade | Dono |
|---|---|
| Regional, Campus | C |
| Local, Unidade Acadêmica, Área de conhecimento (CNPq) | B |
| Usuário / identificação do avaliador | A |

- Unidade Acadêmica **é um** Local; nem todo Local é Unidade Acadêmica.
- Quem precisa de uma entidade de outro dono a referencia, não a redefine.
- **Formato de entrega a D:** entrada do dicionário de dados (nome, atributos, tipos, descrição) + trecho PlantUML.

## 8. Avaliação

- O avaliador é **anônimo**. Não há login.
- Pode avaliar a mesma UA **mais de uma vez**.
- Avaliação registrada **não pode ser editada nem excluída**.

## 9. Arquitetura

- Um pacote por funcionalidade + um pacote **Comum**.
- Componentes compartilhados (pacote Comum), modelados uma vez por D e só referenciados pelos demais:
  - **Abertura de link externo**
  - **Acesso à API**
  - **Estados de tela remota:** carregando, exibindo, vazio, indisponível, recarregar ao voltar
  - **Provedor de mapa** (genérico)

## 10. Revisão

- O revisor devolve a revisão em até **1 dia**.
- Um item está pronto quando foi revisado e está no repositório.

## 11. Mudanças no contrato

- Toda mudança nos pontos deste contrato passa por D.
- Mudança simples: D faz.
- Mudança que exige retrabalho: D pede às pessoas afetadas.

## 12. Uso de IA

- Uso livre.
- Cada pessoa registra o próprio uso (IA, URL, data e prompt) para o apêndice exigido pela regra 6.
