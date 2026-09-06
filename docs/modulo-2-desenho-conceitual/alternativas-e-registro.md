# Alternativas e ADRs

Comparar a menor capacidade suficiente, registrar a escolha num ADR e verificar depois se a solução ainda corresponde ao que foi decidido.

## Análise arquitetural leve

Uma árvore de utilidade reduzida prioriza o que realmente deve orientar a estrutura:

```text
objetivo de negócio
└── característica arquitetural
    └── cenário de qualidade priorizado
        ├── tática e mecanismo candidato
        ├── ponto de sensibilidade
        ├── ponto de trade-off
        ├── risco ou incerteza
        └── experimento ou evidência
```

- **Ponto de sensibilidade** é uma propriedade cuja pequena variação altera de modo relevante a resposta de qualidade, como tamanho do contexto sobre latência e cobertura.
- **Ponto de trade-off** afeta mais de uma característica em direções concorrentes, como retenção de traces sobre auditabilidade e privacidade.
- **Risco arquitetural** é uma consequência adversa plausível associada a uma decisão ou lacuna de conhecimento.
- **Premissa** é algo tratado provisoriamente como verdadeiro; precisa de responsável e data de confirmação.
- **Incerteza** é o que ainda não sabemos com confiança suficiente para decidir; deve levar a experimento, pesquisa ou redução de escopo.

O objetivo não é produzir pontuação aparente. É selecionar de três a cinco cenários prioritários, localizar decisões sensíveis e descobrir o que precisa ser provado antes de ampliar o compromisso.

## 4. Comparar a menor capacidade suficiente e preparar os próximos módulos

<a id="alternativas-de-conhecimento"></a><a id="alternativas-de-acao"></a><a id="alternativas-de-integracao-e-plataforma"></a>

Com RAS e cenários visíveis, a equipe compara alternativas pelo que elas acrescentam ao sistema.

| Decisão | Alternativas | Responsabilidade adicional |
|---|---|---|
| Conhecimento | consulta estruturada, contexto selecionado, RAG, fine-tuning | seleção, ingestão ou curadoria; vigência e proveniência continuam explícitas |
| Ação | regra, workflow, agente | autorização, contratos, recuperação e avaliação proporcionais ao efeito |
| Plataforma | integração local, capacidade comum, serviço hospedado ou autogerido | operação, dependências, portabilidade e custo total |

Contexto selecionado serve quando a fonte já é conhecida e pequena. RAG é candidato quando localização, atualização e autorização de fontes exigem recuperação própria; o Módulo 3 detalha essa decisão. Fine-tuning muda comportamento em tarefa repetida, mas não governa vigência ou proveniência. Workflow mantém transições conhecidas; agente só se justifica quando a sequência variável cria valor mensurável, tema do Módulo 4. Gateway e serviços compartilhados atendem controles realmente comuns; o Módulo 7 trata sua operação.

Antes de ampliar capacidade, defina a menor evidência que permite decidir: teste de contrato, casos representativos, modo sombra ou experimento limitado. Uma alternativa pode ser rejeitada quando uma regra, consulta ou melhoria de processo atende o mesmo objetivo com menos risco.

Esta comparação não encerra o desenho; ela escolhe qual família de táticas precisa de detalhamento posterior. Uma escolha estrutural pode combinar várias famílias e precisa aparecer nas visões afetadas.

| Se o RAS exige… | O módulo seguinte aprofunda… | Táticas que serão detalhadas |
|---|---|---|
| conhecimento atualizado, autorizado e explicável | [Módulo 3 — RAG](../modulo-3-rag/index.md) | ingestão, segmentação, proveniência, vigência, filtro de autorização, recuperação e abstenção |
| efeito controlado ou sequência variável | [Módulo 4 — Agentes](../modulo-4-agentes/index.md) | contratos de ferramenta, política externa, aprovação, orçamento, idempotência, compensação e reconciliação |
| proteção contra abuso, exposição ou decisão inadequada | [Módulo 6 — Confiança](../modulo-6-confianca/index.md) | modelagem de ameaça, guardrails em profundidade, minimização, segregação, retenção, avaliação e bloqueio |
| mudança contínua, falha de dependência ou escala compartilhada | [Módulo 7 — Operação](../modulo-7-operacao/index.md) | manifesto, regressão, canary, rollback, circuit breaker, fallback, trace, SLO e resposta a incidente |

O Módulo 2 já introduz essas táticas como repertório de desenho. Os módulos seguintes mostram como combiná-las, testá-las e operá-las em cada contexto.

## O processo de decisão e o uso de ADRs

ADRs preservam escolhas arquiteturais relevantes, não substituem visões ou análise. Uma ADR registra:

- status, contexto e preocupações;
- RAS e direcionadores;
- alternativas comparadas e racional da escolha;
- decisão e elementos afetados nas visões;
- consequências, riscos residuais e premissas;
- evidências esperadas e gatilhos de revisão;
- relação com ADRs anteriores, quando substitui uma decisão.

## 5. Registrar a escolha e sua revisão

Uma **ADR** registra decisão relevante para que ela sobreviva ao contexto da conversa. Use-a quando a escolha altera estrutura, fronteira, dependência, responsabilidade ou característica prioritária.

![Comparação entre modelo estrutural, cenário de comportamento e ADR para a mesma solução](../assets/images/m02-modelo-cenario-adr.png)

*Figura — O modelo mostra a estrutura; o cenário mostra o comportamento; a ADR explica a escolha.*

Uma ADR contém status, contexto, preocupações, RAS, opções, racional, decisão, visões afetadas, consequências, riscos residuais, premissas, evidência esperada e gatilho de revisão. O registro antigo permanece como histórico quando uma decisão é substituída.

## 6. Verificar correspondência e risco residual

Antes de aprovar uma direção, percorra o desenho nos dois sentidos:

| Verificação | Pergunta |
|---|---|
| contexto ↔ interação | todo participante e dependência da sequência existe no contexto? |
| interação ↔ responsabilidades | cada passo tem responsável, autoridade e contrato? |
| interação ↔ informação | cada leitura, transformação, persistência e envio está representado? |
| informação ↔ implantação | região, provedor, armazenamento, identidade e rede preservam finalidade e classificação? |
| RAS ↔ tática ↔ visões | a resposta de qualidade altera elementos identificáveis e possui critério de verificação? |
| ADR ↔ análise | o racional cita sensibilidades, trade-offs, riscos, premissas e alternativas? |
| evidência ↔ decisão | o experimento pode confirmar, restringir ou refutar a escolha? |

Registre separadamente **risco**, **premissa**, **incerteza** e **dependência**. Dar o mesmo nome a todos esconde a ação necessária: risco pede contenção; premissa pede confirmação; incerteza pede aprendizagem; dependência pede acordo e acompanhamento.

## Preparação para a progressão de decisões

Este módulo estabelece a fundação para RAG, agentes, confiança e operação. Os módulos 3 a 6 detalham mecanismos; o Módulo 2 estabelece por que eles seriam necessários, que RAS realizam, que visões alteram e como sua consequência será verificada.

## Ferramentas no mercado

São exemplos; consulte o [Guia de ferramentas](../referencia/guia-de-ferramentas.md).

| Ferramenta          | Quando ajuda             | Pré-requisito                               | Limite arquitetural                      |
| ------------------- | ------------------------ | ------------------------------------------- | ---------------------------------------- |
| OpenAI SDK          | Adaptar contrato de API. | Credencial real ou fixture.                 | Não define política.                     |
| LiteLLM             | Normalizar endpoints.    | Modelos, credenciais e falhas configurados. | Não elimina diferenças entre provedores. |
| Docker Model Runner | Prototipar modelo local. | Docker, modelo e recursos.                  | Não substitui critérios ou operação.     |

**Próxima página:** [Exemplo arquitetural](exemplo-arquitetural.md).
