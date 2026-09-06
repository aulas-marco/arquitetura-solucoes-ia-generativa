# O que muda quando o componente é probabilístico

A transição que obriga a rever o que se considera um componente confiável, e o anti-padrão que ela produz quando é ignorada.

## O que muda no sistema

A introdução de geração probabilística não substitui o software determinístico. Ela cria uma zona em que a saída precisa ser julgada por adequação, enquanto autenticação, cálculo, validação de esquema e execução de transações continuam sujeitos a regras explícitas.

### Do determinístico ao probabilístico

Um **componente determinístico** deve produzir a mesma saída quando recebe a mesma entrada no mesmo estado. Um **componente probabilístico** produz saídas segundo distribuições aprendidas. Um modelo de linguagem estima tokens plausíveis no contexto recebido; duas respostas diferentes podem ser aceitáveis, e uma resposta estável pode continuar errada.

![Comparação visual entre um fluxo determinístico, que segue regras explícitas, e um fluxo probabilístico, que produz respostas variáveis dentro de limites](../assets/images/m01-deterministico-probabilistico.png)
*Figura 1 — Regras determinísticas permitem asserções exatas; geração probabilística exige avaliação sobre casos e contenção de falhas.*

A fronteira entre essas zonas define responsabilidades. O modelo pode extrair valores de um recibo ou redigir uma explicação. Regras verificam limites; uma pessoa autorizada aprova; um serviço transacional produz o efeito. A chamada ao modelo participa de uma composição maior.

### Modelo, aplicação e sistema sociotécnico

Essa composição pode ser observada em três unidades. Um **modelo** é um artefato treinado que recebe entradas e produz saídas. Uma **aplicação de IA** combina modelo, interface, instruções, regras, dados e integrações para atender uma necessidade. Um **sistema de IA** inclui também pessoas, processos, fornecedores, políticas, responsabilidades e efeitos no ambiente.

| Unidade | Pergunta |
|---|---|
| Modelo | Que capacidade e limites aparecem sob determinada configuração? |
| Aplicação | Como software, contexto e controles transformam essa capacidade em função? |
| Sistema sociotécnico | Que resultado, risco e responsabilidade emergem no uso real? |

Um benchmark do modelo não mede autorização, utilidade no processo, carga de revisão ou recuperação. O [AI Risk Management Framework do NIST](https://doi.org/10.6028/NIST.AI.100-1) trata riscos ao longo do ciclo de vida. Para a arquitetura, o sistema sociotécnico é a unidade principal de julgamento; o modelo é uma de suas dependências.

Essa distinção leva à pergunta seguinte: se o comportamento não vem apenas do modelo, que conjunto de elementos o produz?

## Anti-padrão: uma caixa probabilística para tudo

O anti-padrão aparece quando a mesma chamada recebe conteúdo, decide acesso, calcula regras, escolhe ações e produz a resposta. Prompt crescente, credenciais amplas, falhas irreproduzíveis e retries com efeito duplicado são sintomas.

A correção consiste em separar contratos conforme risco e mudança: regras permanecem explícitas; conhecimento conserva fonte; ferramentas passam por política; geração recebe escopo; estado e memória têm retenção; observabilidade correlaciona versões. Isso não exige um microsserviço para cada responsabilidade.
