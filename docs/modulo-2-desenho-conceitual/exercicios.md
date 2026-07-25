# Exercícios

Responda antes do feedback. Recordar e Compreender têm respostas públicas; os níveis avançados têm critérios. Veja a [Taxonomia de Bloom](../comecar/taxonomia-de-bloom.md).

## Recordar

### 1. Oportunidade e requisito

Qual é a diferença entre uma oportunidade de negócio e um requisito arquiteturalmente significativo?

<details>
<summary>Ver resposta</summary>

Uma oportunidade descreve uma melhoria desejada em uma situação; não escolhe tecnologia. Um requisito arquiteturalmente significativo (RAS) influencia estrutura, interfaces, mecanismos ou uma decisão difícil de reverter. Um RAS pode surgir da oportunidade, mas não é a própria oportunidade.
</details>

### 2. IA como componente

Nomeie três aspectos que o desenho conceitual deve prever quando um modelo de linguagem é integrado a um sistema maior.

<details>
<summary>Ver resposta</summary>

Conhecimento e dados autorizados, integrações com APIs ou ferramentas e controles de autonomia e segurança são três aspectos. Fronteiras de confiança, observabilidade, responsabilidades humanas e operação também são respostas válidas.
</details>

### 3. Seis partes de um cenário de qualidade

Liste as seis partes usadas para descrever um cenário de atributo de qualidade.

<details>
<summary>Ver resposta</summary>

Fonte, estímulo, ambiente, artefato, resposta e medida. Prioridade, dono, verificação e origem podem complementar o cenário para torná-lo rastreável.
</details>

### 4. Critério probabilístico

Liste cinco elementos que tornam verificável um critério de aceitação para comportamento probabilístico.

<details>
<summary>Ver resposta</summary>

População, amostra, métrica ou critério qualitativo, limiar, tratamento de incerteza, falha intolerável e ação resultante. Cinco deles atendem ao pedido, desde que estejam definidos para o caso.
</details>

## Compreender

### 5. Componente, não solução completa

Explique por que uma boa demonstração de um modelo não prova que a solução está pronta para uso organizacional.

<details>
<summary>Ver resposta</summary>

Uma demonstração avalia uma capacidade sob condições selecionadas. Uma solução também precisa de dados e autorizações, integrações, limites de autonomia, evidências, operação, recuperação e responsáveis. O modelo é um componente; não substitui esses elementos arquiteturais.
</details>

### 6. RAG e fine-tuning

Explique por que RAG costuma ser mais adequado que fine-tuning para conhecimento factual que muda com frequência e precisa ser citado.

<details>
<summary>Ver resposta</summary>

RAG recupera evidências externas no momento da inferência, permitindo atualização e proveniência por fonte. Fine-tuning altera parâmetros e tendências de comportamento; atualizar fatos exige novo ciclo de curadoria, treinamento e avaliação. RAG também cria riscos próprios de recuperação, autorização e latência.
</details>

### 7. Gateway e mediador

Distinga o papel de um gateway de IA do papel de um mediador entre um agente e uma API de negócio.

<details>
<summary>Ver resposta</summary>

O gateway aplica controles transversais, como quotas, redação de dados, fallback e telemetria. O mediador recebe uma intenção ou chamada proposta pelo agente e executa a ação de forma determinística, validando autorização, contrato e registro. Um não substitui o outro.
</details>

## Aplicar

### 8. Decisão de conhecimento para suporte técnico

**O que é:** uma decisão de conhecimento define de onde o sistema obtém informação e como preserva atualização, autorização e evidência.

**Onde encontrar:** consulte [critérios de adequação](conceitos.md#criterios-de-adequacao-da-ia-generativa), [fronteiras](conceitos.md#fronteiras-e-fora-de-escopo) e o [processo de desenho](padroes-e-decisoes.md#processo-de-desenho).

**Situação**

Uma equipe quer responder dúvidas sobre 800 manuais técnicos, atualizados semanalmente. Parte das perguntas é sobre dados de uma ordem de serviço já aberta; outra exige localizar uma política vigente. O patrocinador propõe treinar um modelo com todos os manuais.

**Seu papel**

Você conduz a primeira decisão arquitetural. Deve separar o que é dado estruturado, contexto já selecionado e conhecimento que precisa ser localizado.

**Insumos disponíveis**

Use [fronteiras de dados](conceitos.md#fronteiras-e-fora-de-escopo), o trecho sobre prompt, RAG e fine-tuning em [padrões de decisão](padroes-e-decisoes.md#processo-de-desenho) e o [template de ADR](../referencia/template-adr.md). Trabalhe apenas com manuais fictícios.

**Como conduzir**

1. Classifique três perguntas do cenário por fonte: consulta estruturada, contexto fornecido ou recuperação de conhecimento.
2. Compare prompt com contexto, RAG e fine-tuning para as políticas que mudam semanalmente.
3. Declare dados, permissões, atualização e proveniência da evidência: origem, versão, transformação e uso na resposta.
4. Registre uma decisão provisória e uma condição que a faria ser revista.

**Entrega esperada**

Entregue uma matriz de decisão e o núcleo de uma ADR com contexto, alternativas, decisão, consequências e gatilho de revisão.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Classificação do conhecimento | 25% | Distingue dado de ordem, contexto selecionado e informação a localizar. |
| Trade-offs | 30% | Compara atualização, proveniência, custo e complexidade das alternativas. |
| Fronteiras e controles | 20% | Explicita autorização, versão, transformação e uso da evidência. |
| Decisão revisável | 25% | Registra consequência e medida capaz de alterar a escolha. |

**Como verificar antes de entregar:** confira se a proposta não usa fine-tuning como banco de dados e se cada fonte possui controle de acesso e atualização.

### 9. Critérios para uma cadeia de extração

**O que é:** pipes-and-filters separa etapas de geração e validação para impedir que um erro probabilístico avance sem controle.

**Onde encontrar:** consulte [atributos de qualidade](../referencia/atributos-de-qualidade.md), [responsabilidade humano–IA](conceitos.md#responsabilidade-humanoia) e [critérios probabilísticos](padroes-e-decisoes.md#como-medir-a-aderencia-criterios-probabilisticos-de-aceitacao).

**Situação**

Um sistema extrai obrigações de licenças ambientais, valida datas e identificadores e prepara uma síntese para especialista. Campos estruturados têm formato obrigatório; a síntese pode variar, mas não pode omitir uma obrigação crítica. A saída só segue ao especialista depois das validações.

**Seu papel**

Você desenha a cadeia de tarefas e os critérios que determinam quando cada resultado pode avançar, ser corrigido ou ser bloqueado.

**Insumos disponíveis**

Use os [modos operacionais](conceitos.md#modos-operacionais), o padrão de encadeamento em [processo de desenho](padroes-e-decisoes.md#processo-de-desenho) e os critérios probabilísticos. Use licenças fictícias com exceções.

**Como conduzir**

1. Desenhe quatro etapas: extração, validação determinística, síntese e revisão humana.
2. Defina o contrato de entrada, saída e falha para cada filtro.
3. Escreva um critério determinístico para campos e um probabilístico para a síntese.
4. Defina uma falha intolerável, o modo acionado e a pessoa informada.

**Entrega esperada**

Entregue o fluxo com equivalente textual, dois critérios de aceitação e uma regra operacional de bloqueio ou recuperação.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Encadeamento | 25% | Separa geração, validação e revisão em responsabilidades compreensíveis. |
| Contratos | 25% | Define entradas, saídas e ação diante de falha em cada etapa. |
| Critérios | 30% | Distingue validação determinística de aceitação probabilística. |
| Operação | 20% | Indica bloqueio, preservação do estado e retorno seguro. |

**Como verificar antes de entregar:** confira se nenhuma síntese avança quando o filtro de campos falha e se a revisão possui evidências para discordar.

## Analisar

### 10. Arquitetura de ação para reembolso

**O que é:** uma decisão de autonomia compara o valor de delegar passos ao modelo com os novos riscos de ferramentas e efeitos no negócio.

**Onde encontrar:** use [responsabilidade humano–IA](conceitos.md#responsabilidade-humanoia), [modos operacionais](conceitos.md#modos-operacionais) e [padrões de ação e autonomia](padroes-e-decisoes.md#processo-de-desenho).

**Situação**

Um processo de reembolso tem regras estáveis para elegibilidade, mas analistas precisam interpretar justificativas e reunir anexos. A equipe sugere um agente que consulte cadastro, calcule valor e envie a solicitação. As APIs de envio não são idempotentes e valores acima de R$ 5 mil exigem aprovação.

**Seu papel**

Você analisa onde a IA agrega interpretação e onde regras, workflow, mediador e aprovação devem manter o controle.

**Insumos disponíveis**

Use o [quando rejeitar GenAI](conceitos.md#quando-rejeitar-ia-generativa), [fronteiras de decisão](conceitos.md#fronteiras-e-fora-de-escopo), o padrão de mediador e o [template de ADR](../referencia/template-adr.md).

**Como conduzir**

1. Separe as atividades em regra, interpretação, proposta e efeito externo.
2. Compare automação convencional, workflow com LLM e agente para cada atividade.
3. Descreva um mediador para as APIs: intenção permitida, validação, aprovação, idempotência e registro.
4. Defina modos normal, baixa confiança e bloqueado para o fluxo.
5. Aponte a evidência que poderia justificar ampliar a autonomia.

**Entrega esperada**

Entregue uma matriz de atividades e controles, um fluxo de responsabilidade e uma ADR curta.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Decomposição | 20% | Distingue decisão determinística, interpretação e efeito externo. |
| Alternativas | 25% | Compara workflow, agente e automação com razões do contexto. |
| Mediação e aprovação | 25% | Protege a API por contrato, autorização, idempotência e evidência. |
| Modos operacionais | 15% | Define transições, estado preservado e pessoa informada. |
| Revisão | 15% | Define medida e limite para ampliar ou reduzir autonomia. |

**Como verificar antes de entregar:** confira se o modelo não executa diretamente a API de envio e se aprovação não é reduzida a um clique sem evidências.

## Avaliar

### 11. Gateway, chassi e múltiplos modelos

**O que é:** uma decisão de plataforma avalia controles compartilhados e diversidade de modelos sem confundir padronização com uma solução única.

**Onde encontrar:** consulte [ferramentas no mercado](conceitos.md#ferramentas-no-mercado), [stakeholders](conceitos.md#stakeholders-e-preocupacoes) e [integração e infraestrutura](padroes-e-decisoes.md#processo-de-desenho).

**Situação**

Três produtos internos querem usar modelos hospedados. Atendimento precisa de baixa latência; jurídico exige redação de dados pessoais e rastreabilidade; pesquisa tolera maior custo para tarefas complexas. A plataforma propõe um gateway obrigatório e um roteador entre modelo principal e fallback local.

**Seu papel**

Você emite uma recomendação sobre gateway, chassi compartilhado e modelo único ou múltiplos modelos, sem assumir que redundância é sempre segura.

**Insumos disponíveis**

Use a tabela de [stakeholders e preocupações](conceitos.md#stakeholders-e-preocupacoes), a seção de gateway e chassi em [padrões de decisão](padroes-e-decisoes.md#processo-de-desenho), o [guia de ferramentas](../referencia/guia-de-ferramentas.md) e o template de ADR.

**Como conduzir**

1. Liste controles que pertencem ao gateway e controles que continuam no produto.
2. Compare modelo único e roteamento por tarefa quanto a contrato, avaliação, custo, latência e degradação.
3. Avalie se o fallback atende à mesma categoria de risco e quais testes periódicos são necessários.
4. Declare a menor diversidade suficiente e as condições para adicionar ou remover um modelo.

**Entrega esperada**

Entregue um parecer de uma página, uma tabela de controles e uma ADR com recomendação condicionada.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Controles transversais | 25% | Localiza quotas, redação, telemetria e fallback na fronteira adequada. |
| Comparação | 25% | Relaciona diversidade de modelos a contratos, avaliações e operação. |
| Risco de degradação | 25% | Verifica compatibilidade e teste do fallback para cada categoria. |
| Recomendação | 25% | Assume posição condicionada por evidências e gatilhos explícitos. |

**Como verificar antes de entregar:** confira se o gateway não substitui política do produto e se o fallback não é declarado seguro sem teste.

## Criar

### 12. Dossiê conceitual de um assistente administrativo clínico

**O que é:** dossiê conceitual reúne oportunidade, operação, decisões e evidências suficientes para uma revisão independente antes da implementação.

**Onde encontrar:** consulte [o desenho conceitual](conceitos.md), [processo de desenho](padroes-e-decisoes.md#processo-de-desenho), [critérios probabilísticos](padroes-e-decisoes.md#como-medir-a-aderencia-criterios-probabilisticos-de-aceitacao) e o [template de ADR](../referencia/template-adr.md).

**Situação**

Um sistema ajuda equipes a preparar documentação administrativa para autorização de procedimentos. Pode resumir registros autorizados e políticas, mas não diagnostica, prescreve nem envia solicitação sem revisão. Há dados sensíveis, fontes conflitantes e uma dependência indisponível em manutenção semanal.

**Seu papel**

Você é o arquiteto que compõe um dossiê independente de fornecedor para decisão conjunta com domínio, privacidade, segurança e operações.

**Insumos disponíveis**

Use [CONOPS](conceitos.md#conops-o-sistema-em-operacao), [fronteiras](conceitos.md#fronteiras-e-fora-de-escopo), [modos](conceitos.md#modos-operacionais), [responsabilidade](conceitos.md#responsabilidade-humanoia), padrões de conhecimento, ação e infraestrutura, e o template de ADR. O caso é fictício; não use prontuários reais.

**Como conduzir**

1. Declare oportunidade, baseline, stakeholders, finalidade, fora de escopo e responsabilidades por verbo.
2. Descreva os modos normal, baixa confiança, degradado e bloqueado, com transições e trabalho manual.
3. Escolha e justifique o padrão de conhecimento, a cadeia de validação, os controles de gateway e a autonomia permitida.
4. Rastreie objetivos de negócio, produto, dados e IA até RAS, mecanismos, critérios e evidências; priorize as características e declare a tensão aceita.
5. Compare alternativas em uma ADR e encerre com experimento, falhas intoleráveis e gatilhos de revisão.

**Entrega esperada**

Entregue o dossiê, um diagrama com equivalente textual e uma ADR. O texto deve permitir revisão independente.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Escopo e operação | 15% | Delimita finalidade, fora de escopo, modos e trabalho humano. |
| Decisões arquiteturais | 20% | Justifica conhecimento, autonomia, cadeia e controles compartilhados. |
| Fronteiras e responsabilidades | 15% | Explicita dados, decisão, fornecedor e autoridade humana. |
| Rastreabilidade | 20% | Liga objetivos, RAS, mecanismos, critérios e evidências. |
| Alternativas e ADR | 15% | Expõe consequências e condições de revisão sem apelar a marca. |
| Experimento e falhas | 15% | Define teste refutável, falhas intoleráveis e recuperação. |

**Como verificar antes de entregar:** confira modos, fronteiras, fontes, controles, critérios, ADR e gatilhos de revisão.

Concluída a prática, faça a [síntese e autoavaliação](sintese-e-referencias.md).
