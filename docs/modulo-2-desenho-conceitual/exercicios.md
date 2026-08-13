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

**Onde encontrar:** consulte [critérios de adequação](conceitos.md#criterios-de-adequacao-da-ia-generativa), [fronteiras](conceitos.md#fronteiras-e-fora-de-escopo) e a [sequência de decisão](padroes-e-decisoes.md#sequencia-de-decisao).

**Situação**

Uma equipe quer responder dúvidas sobre 800 manuais técnicos de equipamentos, atualizados semanalmente pelo fabricante. O suporte recebe três tipos de pergunta: o status de uma ordem de serviço já aberta no sistema interno, o procedimento descrito em um manual específico e qual política de garantia vigente se aplica a um modelo de equipamento. O patrocinador propõe treinar um modelo com todos os manuais e encerrar o assunto.

**Seu papel**

Você conduz a primeira decisão arquitetural do sistema de suporte. Antes de escolher qualquer tecnologia, precisa separar o que já é dado estruturado, o que é contexto selecionável de antemão e o que exige recuperação de conhecimento no momento da resposta.

**Insumos disponíveis**

Use [fronteiras de dados](conceitos.md#fronteiras-e-fora-de-escopo), as [alternativas de conhecimento](padroes-e-decisoes.md#alternativas-de-conhecimento) e o [template de ADR](../referencia/template-adr.md). Trabalhe apenas com manuais fictícios.

**Vocabulário rápido (antes de começar)**

- **Consulta estruturada** — o dado já existe num sistema, num campo exato. Como perguntar seu saldo num caixa eletrônico: o sistema só busca o número.
- **Contexto selecionado** — você já sabe qual documento vale e pode entregá-lo de antemão. Como dar o manual certo na mão de alguém antes de ele responder.
- **Conhecimento a recuperar** — ninguém sabe de antemão em qual documento, entre muitos, está a resposta; é preciso buscar no momento da pergunta. Como perguntar a um bibliotecário que primeiro precisa achar o livro certo entre milhares.

**Como conduzir**

Produza os quatro entregáveis abaixo, na ordem, preenchendo as tabelas e a ficha prontas. Cada um é pequeno e pode ser verificado isoladamente antes de avançar para o próximo.

1. **Classificação das perguntas.** A primeira linha já vem resolvida, como exemplo — complete as outras duas do mesmo jeito:

    | Pergunta | Onde o dado mora hoje | Classificação |
    |---|---|---|
    | Qual o status da OS nº 4521? | Sistema interno de ordens de serviço, campo "status" | Consulta estruturada |
    | Como trocar o filtro do modelo X200? | *(preencher)* | *(preencher)* |
    | Qual garantia vale para o modelo X200 hoje? | *(preencher)* | *(preencher)* |

    *Entregável 1 — a tabela acima, preenchida.*

2. **Comparação das alternativas de conhecimento**, só para a pergunta da garantia (a única que muda toda semana). A linha "Atualização" já vem resolvida, como exemplo — complete as outras duas:

    | Critério | Contexto fornecido | RAG | Fine-tuning |
    |---|---|---|---|
    | Atualização | Alguém precisa reescrever o texto da política no prompt sempre que ela mudar | Busca automaticamente a versão mais recente indexada | Exige novo treinamento — lento demais para mudança semanal |
    | Proveniência | *(preencher)* | *(preencher)* | *(preencher)* |
    | Custo operacional | *(preencher)* | *(preencher)* | *(preencher)* |

    *Entregável 2 — a tabela acima, preenchida.*

3. **Ficha de proveniência**, ainda para a pergunta da garantia. O primeiro campo já vem resolvido, como exemplo — complete os outros quatro:

    | Campo | Resposta |
    |---|---|
    | Origem (de onde vem o texto da política) | Documento oficial de garantia publicado pelo fabricante |
    | Autoridade que mantém essa versão atualizada | *(preencher)* |
    | Versão e vigência (desde quando vale) | *(preencher)* |
    | Transformação aplicada antes da resposta (resumo? tradução? nenhuma?) | *(preencher)* |
    | Uso na resposta final ao suporte | *(preencher)* |

    *Entregável 3 — a ficha acima, preenchida.*

4. **Decisão provisória e gatilho de revisão.** Complete as três frases:

    - Escolhemos **______** para a política de garantia porque ______.
    - Rejeitamos **______** porque ______.
    - Revisaríamos essa escolha se ______ (condição observável e mensurável).

    *Entregável 4 — as três frases acima, completas.*

**Entrega esperada**

Os quatro entregáveis dos passos 1 a 4 — nenhum texto livre adicional é necessário. Juntos, formam o núcleo de uma ADR: contexto (entregável 1), alternativas (entregável 2), evidência (entregável 3) e decisão com gatilho (entregável 4).

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Classificação do conhecimento (entregável 1) | 20% | Distingue corretamente dado de ordem, contexto selecionado e informação a localizar. |
| Comparação de alternativas (entregável 2) | 30% | Compara atualização, proveniência e custo sem declarar uma alternativa superior em tudo. |
| Ficha de proveniência (entregável 3) | 25% | Preenche os cinco campos com informação específica do caso, não genérica. |
| Decisão e gatilho (entregável 4) | 25% | Registra decisão, alternativa rejeitada com motivo e uma condição mensurável de revisão. |

**Como verificar antes de entregar:** confira se cada um dos quatro entregáveis existe isoladamente, não apenas embutido em um texto corrido, e se a decisão do entregável 4 não usa fine-tuning como banco de dados para fatos que mudam semanalmente.

## Analisar

### 9. Modificabilidade em evidência: da troca controlada à ADR

**O que é:** uma decisão de modificabilidade não se sustenta em uma tecnologia citada por nome; ela se sustenta em uma tática e um mecanismo identificáveis, e em evidência real de que a troca funcionou sem reescrever o cliente.

**Onde encontrar:** consulte [cenário, tática, mecanismo e padrão](conceitos.md#da-caracteristica-a-estrutura), a tabela de táticas por intenção — linha de Modificabilidade — em [padrões e decisões](padroes-e-decisoes.md), as [correspondências entre visões](conceitos.md#correspondencias-entre-visoes) e o [template de ADR](../referencia/template-adr.md).

**Pré-requisito:** este exercício usa os artefatos que você mesmo produziu na [oficina de ferramentas](oficina-de-ferramentas.md#evidencia-a-entregar) (Experimentos A e B). Se ainda não a fez, faça-a agora e volte com o manifesto antes da troca, o manifesto depois da troca, `request.json` e as duas respostas JSON em mãos — não redija um cenário novo para substituí-los.

**Situação**

Você trocou, no manifesto do LiteLLM Proxy, o destino de `boreal-local` de um modelo Ollama para outro, mantendo `request.json` e o alias inalterados, e obteve duas respostas JSON pela mesma chamada `curl`. Isso é uma evidência real de um mecanismo de modificabilidade — não uma alegação sobre a ferramenta.

**Seu papel**

Você decide se essa evidência sustenta registrar a fronteira de consumo (gateway e manifesto) como mecanismo padrão de modificabilidade do sistema, e declara o que ela ainda não decide.

**Insumos disponíveis**

Os três artefatos e as duas respostas da oficina; a tabela de táticas por intenção de [padrões e decisões](padroes-e-decisoes.md); as regras de [correspondências entre visões](conceitos.md#correspondencias-entre-visoes) (você usará quatro das sete); o [template de ADR](../referencia/template-adr.md).

**Como conduzir**

1. Reúna os artefatos reais: manifesto antes, manifesto depois, `request.json` e as duas respostas JSON. Não descreva um cenário fictício no lugar deles.
2. Classifique, pela tabela de táticas por intenção, qual **tática** de modificabilidade essa troca evidencia e qual **mecanismo**, neste laboratório específico, a realiza. Distinga os dois: a tática é a intenção geral; o mecanismo é a realização concreta que você observou.
3. Preencha a tabela de correspondência abaixo citando, em cada linha, o artefato real que confirma (ou não confirma) a regra — não uma suposição genérica:

    | Regra de correspondência | Artefato ou evidência da oficina | Confirma ou não confirma? |
    |---|---|---|
    | todo ator ou sistema externo usado na interação existe no contexto | *(preencher)* | *(preencher)* |
    | todo dado enviado ou recebido aparece na visão de informação | *(preencher)* | *(preencher)* |
    | toda travessia de fronteira de confiança tem controle associado | *(preencher)* | *(preencher)* |
    | todo RAS chega a uma tática, a elementos das visões e a um método de verificação | *(preencher)* | *(preencher)* |

4. Releia a abertura da oficina: "o experimento observa um mecanismo de adaptador; não prova, sozinho, a modificabilidade da arquitetura inteira." Liste ao menos duas coisas que sua evidência **não** decide (por exemplo: equivalência semântica entre os dois modelos, latência sob carga real, modificabilidade de outros componentes do sistema).
5. Redija uma ADR curta pelo template, citando o manifesto antes/depois e `request.json` como evidência anexada. Não repita o mini-ADR da oficina — avance-o com a classificação do passo 2, a tabela do passo 3 e os limites do passo 4.

**Entrega esperada**

A tabela de correspondência preenchida com evidência real, a classificação de tática e mecanismo, a lista de limites não decididos e uma ADR de até 200 palavras que cite os artefatos reais como evidência.

**Checklist de verificação**

- [ ] A tática e o mecanismo citados vêm da tabela de padrões e decisões, não de memória livre sobre a ferramenta.
- [ ] Cada linha da tabela de correspondência aponta um artefato real (manifesto, `request.json` ou resposta), não uma suposição.
- [ ] Pelo menos duas limitações da evidência estão listadas e são coerentes com a advertência da própria oficina.
- [ ] A ADR cita o manifesto antes/depois e `request.json` como evidência e termina em gatilho de revisão mensurável.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Uso da evidência real | 30% | Tabela e ADR citam os artefatos efetivamente produzidos na oficina, não um cenário paralelo. |
| Classificação de tática e mecanismo | 25% | Distingue tática de mecanismo e localiza ambos na tabela de padrões e decisões. |
| Correspondência entre visões | 25% | Verifica as quatro regras com evidência específica do laboratório, não genérica. |
| Limites da evidência | 20% | Declara o que a troca controlada não prova, alinhado ao limite já declarado na oficina. |

### 10. Arquitetura de ação para reembolso

**O que é:** uma decisão de autonomia compara o valor de delegar passos ao modelo com os novos riscos de ferramentas e efeitos no negócio.

**Onde encontrar:** use [responsabilidade humano–IA](conceitos.md#responsabilidade-humanoia), [modos operacionais](conceitos.md#modos-operacionais) e [alternativas de ação](padroes-e-decisoes.md#alternativas-de-acao).

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

### 11. Plataforma comum e múltiplos modelos

**O que é:** uma decisão de plataforma avalia controles compartilhados e diversidade de modelos sem confundir padronização com uma solução única.

**Onde encontrar:** consulte [ferramentas no mercado](conceitos.md#ferramentas-no-mercado), [stakeholders](conceitos.md#stakeholders-e-preocupacoes) e [alternativas de integração e plataforma](padroes-e-decisoes.md#alternativas-de-integracao-e-plataforma).

**Situação**

Três produtos internos querem usar modelos hospedados. Atendimento precisa de baixa latência; jurídico exige redação de dados pessoais e rastreabilidade; pesquisa tolera maior custo para tarefas complexas. A plataforma propõe um gateway obrigatório e um roteador entre modelo principal e fallback local.

**Seu papel**

Você emite uma recomendação sobre gateway, capacidade comum de plataforma e modelo único ou múltiplos modelos, sem assumir que redundância é sempre segura.

**Insumos disponíveis**

Use a tabela de [stakeholders e preocupações](conceitos.md#stakeholders-e-preocupacoes), as [alternativas de integração e plataforma](padroes-e-decisoes.md#alternativas-de-integracao-e-plataforma), o [guia de ferramentas](../referencia/guia-de-ferramentas.md) e o template de ADR.

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

### 12. Documento de Arquitetura de Software de um assistente administrativo clínico

**O que é:** o Documento de Arquitetura de Software reúne oportunidade, operação, decisões e evidências suficientes para uma revisão independente antes da implementação.

**Onde encontrar:** consulte [o Documento de Arquitetura de Software](conceitos.md#o-documento-de-arquitetura-de-software), [sequência de decisão](padroes-e-decisoes.md#sequencia-de-decisao), [critérios probabilísticos](padroes-e-decisoes.md#como-medir-a-aderencia-criterios-probabilisticos-de-aceitacao) e o [template de ADR](../referencia/template-adr.md).

**Situação**

Um sistema ajuda equipes a preparar documentação administrativa para autorização de procedimentos. Pode resumir registros autorizados e políticas, mas não diagnostica, prescreve nem envia solicitação sem revisão. Há dados sensíveis, fontes conflitantes e uma dependência indisponível em manutenção semanal.

**Seu papel**

Você é o arquiteto que compõe um documento independente de fornecedor para decisão conjunta com domínio, privacidade, segurança e operações.

**Insumos disponíveis**

Use [CONOPS](conceitos.md#conops-o-sistema-em-operacao), [fronteiras](conceitos.md#fronteiras-e-fora-de-escopo), [modos](conceitos.md#modos-operacionais), [responsabilidade](conceitos.md#responsabilidade-humanoia), padrões de conhecimento, ação e infraestrutura, e o template de ADR. O caso é fictício; não use prontuários reais.

**Como conduzir**

1. Declare oportunidade, baseline, stakeholders, finalidade, fora de escopo e responsabilidades por verbo.
2. Descreva os modos normal, baixa confiança, degradado e bloqueado, com transições e trabalho manual.
3. Escolha e justifique o padrão de conhecimento, a cadeia de validação, os controles de gateway e a autonomia permitida.
4. Produza visões de contexto, responsabilidades, interação, informação e implantação; declare ao menos uma exclusão de cada ponto de vista.
5. Verifique correspondências entre participantes, passos, dados, alocações, fronteiras, RAS e controles.
6. Rastreie objetivos até RAS, táticas, mecanismos, elementos das visões, critérios e evidências.
7. Construa uma árvore de utilidade reduzida com três cenários, sensibilidades, trade-offs, riscos e premissas.
8. Compare alternativas em uma ADR e encerre com experimento, falhas intoleráveis e gatilhos de revisão.

**Entrega esperada**

Entregue o documento, as cinco visões com equivalentes textuais, a matriz de correspondência, a árvore de utilidade e uma ADR. O texto deve permitir revisão independente.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Escopo e operação | 10% | Delimita finalidade, fora de escopo, modos e trabalho humano. |
| Visões e correspondências | 25% | Representa contexto, responsabilidades, interação, informação e implantação sem contradições. |
| Análise arquitetural | 20% | Liga cenários a táticas e explicita sensibilidades, trade-offs, riscos e premissas. |
| Rastreabilidade | 20% | Liga objetivos, RAS, mecanismos, elementos das visões, critérios e evidências. |
| Alternativas e ADR | 15% | Expõe racional, visões afetadas, consequências e revisão sem apelar a marca. |
| Experimento e falhas | 10% | Define teste refutável, falhas intoleráveis e recuperação. |

**Como verificar antes de entregar:** percorra cada correspondência nos dois sentidos e confira modos, fontes, alocação, controles, riscos, ADR e gatilhos de revisão.

Concluída a prática, siga para a [oficina de ferramentas](oficina-de-ferramentas.md).
