# Qualidade multidimensional e medição

Sete dimensões que não se resumem a uma média, duas camadas de medição e as tensões que só se priorizam, nunca se resolvem.

## Qualidade tem várias dimensões

Uma resposta “boa” precisa ser decomposta:

- **factualidade:** afirmações correspondem aos fatos verificáveis;
- **relevância:** resposta aborda a intenção e evita material dispersivo;
- **fundamentação:** afirmações importantes são sustentadas pelas evidências autorizadas apresentadas;
- **segurança:** conteúdo e ações respeitam políticas e não expõem ativos;
- **utilidade:** o usuário consegue avançar, inclusive quando a resposta correta é recusar ou escalar;
- **latência:** o tempo atende ao cenário e não induz repetição ou abandono;
- **custo:** consumo por resposta e por tarefa concluída cabe no orçamento.

As dimensões não são substituíveis. Alta relevância não compensa vazamento; baixa latência não compensa política desatualizada. Defina **critérios de bloqueio** para eventos intoleráveis e **metas** para dimensões negociáveis. Meça também por fatias — público, idioma, tipo de pergunta, nível de acesso e rota de fallback — porque a média mascara grupos frágeis.

A avaliação fornece evidência sobre uma distribuição de casos observados. Ela não garante comportamento para toda entrada possível. Essa limitação conduz ao próximo capítulo: controles em profundidade e decisões de governança que permanecem ativos quando o teste não antecipou o caso.

## Duas camadas de medição

Uma métrica pontua um caso. Uma avaliação descreve um conjunto. Confundir as duas coisas é o erro mais comum de quem começa a medir sistemas generativos: a equipe olha cinco notas na tela, vê números altos e conclui que o sistema está pronto.

**Camada 1, por caso.** Antes de aceitar qualquer número, cinco perguntas sobre a métrica que o produziu:

| Elemento | Pergunta |
|---|---|
| Entradas exigidas | precisa da pergunta, da resposta esperada, do contexto recuperado? |
| Régua | quem escreveu o critério, e ele é inspecionável? |
| Escala e limiar | a partir de que valor o caso passa, e quem decidiu esse valor? |
| Ponto cego | o que essa métrica deixa passar por construção? |
| Custo | quantas chamadas ao modelo por caso? |

As famílias se distinguem pelo que exigem. Métricas determinísticas comparam texto por regra, custam zero chamadas e devolvem sempre o mesmo resultado, ao preço de não enxergar equivalência semântica. Métricas com juiz usam um modelo para pontuar, enxergam paráfrase e trazem para dentro do portão de qualidade a mesma incerteza que se quer medir. Quando o juiz também escreve a própria régua, duas execuções idênticas podem divergir, porque a régua mudou entre elas.

O cálculo de cada uma, com fórmula e exemplo numérico, está em [Métricas de avaliação](../referencia/metricas-de-avaliacao.md).

**Camada 2, sobre o conjunto.** Decidir se um sistema pode ser liberado exige métricas clássicas de classificação, calculadas sobre o rótulo de referência de cada caso:

| Métrica | O que responde |
|---|---|
| Acurácia | fração de decisões corretas, enganosa quando as classes são desbalanceadas |
| Precisão por classe | dos casos que o sistema bloqueou, quantos deviam ser bloqueados |
| Recall por classe | dos casos que deviam ser bloqueados, quantos o sistema pegou |
| F1 por classe | resumo dos dois quando a classe é rara |
| Matriz de confusão | qual erro específico acontece, e não apenas quantos erros existem |

A decisão de arquitetura mora na assimetria entre os dois erros. Recall alto na classe de bloqueio custa falsa recusa, e falsa recusa manda usuário legítimo para fila humana. Nenhum limiar otimiza os dois ao mesmo tempo, e escolher qual erro se tolera é decisão de produto e de segurança, com responsável declarado.

`Recall@k`, MRR e nDCG medem ordenação de recuperação e exigem contexto recuperado. Elas pertencem ao [Módulo 3](../modulo-3-rag/index.md) e avaliam o caminho do conhecimento, sem dizer nada sobre a decisão tomada.

## Prioridades e tensões da confiança

| Característica | Prioridade | Tensão aceita | Medida e responsável |
|---|---|---|---|
| Segurança e privacidade | Não negociável | bloqueios e minimização podem reduzir utilidade | acesso cruzado e dado sensível exposto: zero; Segurança e Privacidade |
| Confiabilidade e fundamentação | Alta | recuperação e validação elevam latência e custo | respostas com evidência vigente e escalonamentos corretos; Produto e domínio |
| Auditabilidade | Alta | trace preserva metadados técnicos sob retenção limitada | execução reconstruível por versão; Operação e Auditoria |
| Utilidade, latência e custo | Importante | orçamento e filtros podem encaminhar mais casos | p95, custo por jornada e falsa recusa por fatia; Produto e Plataforma |
| Modificabilidade | Importante | contratos, adaptadores e regressão acrescentam componentes | mudança localizada e teste de contrato; Arquitetura |

Uma solução confiável atende às prioridades declaradas no cenário. Ela não maximiza simultaneamente coleta, velocidade, automação e cobertura de casos.

## Ferramentas no mercado

Condições e alternativas estão no [Guia de ferramentas](../referencia/guia-de-ferramentas.md).

| Ferramenta | Quando ajuda | Pré-requisito | Limite arquitetural |
|---|---|---|---|
| Langfuse | Registrar traços e avaliações. | Telemetria, retenção e acesso. | Não substitui controles de domínio. |
| Phoenix | Investigar traços. | Instrumentação e dados minimizados. | Não prova segurança fora da amostra. |
| Guardrails AI | Validar formatos. | Esquemas, critérios e rota de falha. | Não substitui autorização ou revisão. |

Continue em [Governança e responsabilidade](governanca-e-responsabilidade.md).
