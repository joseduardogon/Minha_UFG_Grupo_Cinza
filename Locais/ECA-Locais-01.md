# ECA-Locais-01 – Regras E-C-A de Locais

| Campo | Valor |
|---|---|
| **Código** | `ECA-Locais-01` |
| **Título** | Regras E-C-A de Locais |
| **Autor(a)** | Maicon Brendo da Silva |
| **Revisor(a)** | Revisor(a) a definir |
| **Status** | Em produção |
| **Rastreia para** | `DCla-Locais-01`, `DEst-Locais-01`, `Contrato-Locais-01` |

## Descrição

Especificação das regras ativas do tipo Evento-Condição-Ação (E-C-A) que determinam o comportamento reativo da interface `TelaLocais`, formalizando as transições modeladas no `DEst-Locais-01`.

### Regras E-C-A de Locais

| Código | Evento | Condição | Ação | Classe Alvo |
|---|---|---|---|---|
| **ECA-LOC-01** | Entrada na tela de Locais a partir da tela inicial | Sempre | Exibir pop-up transitório "Carregando locais...", inicializar controlador e disparar requisição assíncrona à API | `TelaLocais` |
| **ECA-LOC-02** | Conclusão da busca de dados com sucesso pela API | Lista retornada possui pelo menos 1 elemento | Encerrar pop-up de carregamento e transicionar para o estado `Exibindo Lista`, preenchendo a lista com fotos e nomes | `TelaLocais` |
| **ECA-LOC-03** | Toque do usuário em um item da lista de prédios (`E2`) | A tela está no estado `Exibindo Lista` | Alternar a aba ativa para `MAPA`, acionar `focarLocal(local)` para centralizar câmera e destacar o marcador | `TelaLocais` |
| **ECA-LOC-04** | Toque do usuário no botão flutuante de GPS (`E4`) | A tela está no estado `Exibindo Mapa` | Invocar verificação de precisão de local e recentralizar a câmera na posição geográfica atual do usuário | `AbaMapaLocais` |
| **ECA-LOC-05** | Toque do usuário no botão de retorno `[<]` na barra superior (`E1`) | A tela de Locais está ativa | Encerrar a exibição da tela de Locais e restaurar a tela inicial do Minha UFG | `TelaLocais` |

## Referências

GOOGLE. **Antigravity**. Assistente de IA para Engenharia de Software. Disponível em: https://antigravity.google.com. Acesso em: 30 out. 2026.

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 11 (Software Engineering Models and Methods). IEEE, 2024.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |

