# DCla-Comum-04 – Classes do componente ProvedorMapa

| Campo | Valor |
|---|---|
| **Código** | `DCla-Comum-04` |
| **Título** | Classes do componente ProvedorMapa |
| **Autor(a)** | Pessoa D |
| **Revisor(a)** | Pessoa C |
| **Status** | Em revisão |
| **Rastreia para** | `DCmp-Comum-01`, `DImp-Geral-01`, `DCdu-Geral-01` |

## Diagrama

![DCla-Comum-04](DCla-Comum-04.png)

Fonte: [`DCla-Comum-04.puml`](DCla-Comum-04.puml)

## Descrição

O componente ProvedorMapa isola o app do serviço de mapa e do GPS, que correspondem ao ator Provedor de mapa / GPS do `DCdu-Geral-01`. É genérico: não conhece Local nem categoria, que são conceitos do pacote `Locais` (Pessoa B).

- `IProvedorMapa`: exibe o mapa centrado numa coordenada, adiciona marcadores, destaca um marcador (usado quando o usuário toca num local da lista e o app muda para a aba Mapa) e recentraliza o mapa.
- `ILocalizacao`: verifica e solicita a permissão de localização e obtém a posição atual (botão de localização da aba Mapa).
- `Marcador`: pino no mapa, com identificador, rótulo, cor e indicação de destaque. A cor por categoria (estacionamento, instituto, laboratório etc.) é atribuída por `Locais`; o Comum só recebe a cor.
- `Coordenada`: latitude e longitude em graus decimais.

`AdaptadorProvedorMapa` e `AdaptadorGps` adaptam o SDK do provedor e a Android Location API às interfaces. Assim, trocar o provedor de mapa não afeta o pacote `Locais`.

## Referências

INSTITUTE OF ELECTRICAL AND ELECTRONICS ENGINEERS. **Guide to the Software Engineering Body of Knowledge – SWEBOK v4**. Cap. 3 (Software Design). IEEE, 2024.

ANTHROPIC. **Claude**. Assistente de IA. Disponível em: claude.ai. Acesso em: 14 out. 2026. Questão: Apêndice <X>, Seção <X.1>.

---

## Registro de revisão

| Data | Revisor(a) | Situação | Observações |
|---|---|---|---|
| | | | |
