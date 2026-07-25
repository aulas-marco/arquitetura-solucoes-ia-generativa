# Exercícios

Tente responder antes de abrir os blocos de feedback. Nas atividades avançadas, siga o roteiro, declare suas premissas e use os critérios de avaliação para revisar a qualidade da decisão. A progressão segue a [Taxonomia de Bloom](../comecar/taxonomia-de-bloom.md).

## Recordar

### 1. Unidades de análise

Nomeie as três unidades usadas neste módulo para analisar uma solução de IA.

<details>
<summary>Ver resposta</summary>

Modelo, aplicação de IA e sistema de IA. O sistema inclui a aplicação e o contexto sociotécnico de pessoas, processos, políticas, fornecedores e efeitos.
</details>

### 2. Execução do modelo

Defina treinamento e inferência em uma frase para cada termo.

<details>
<summary>Ver resposta</summary>

Treinamento ajusta parâmetros a partir de dados e objetivo de otimização; inferência usa o modelo já treinado para produzir uma saída a partir de uma entrada.
</details>

### 3. Contexto

Liste quatro elementos que podem compor o contexto de uma chamada.

<details>
<summary>Ver resposta</summary>

Exemplos: instruções do sistema, pedido do usuário, histórico permitido, exemplos, trechos recuperados, resultado de ferramenta e especificação da saída. Quaisquer quatro são suficientes.
</details>

### 4. Parâmetro de geração

Nomeie o parâmetro de geração apresentado neste módulo que influencia a variabilidade na seleção de tokens.

<details>
<summary>Ver resposta</summary>

Temperatura.
</details>

## Compreender

### 5. “Baixa temperatura elimina alucinação”

Explique por que essa frase está errada.

<details>
<summary>Ver resposta</summary>

Temperatura influencia variabilidade na seleção de tokens, não a verdade das afirmações. Uma resposta estável pode repetir sempre o mesmo erro. Fundamentação depende de escopo, evidências, validação e avaliação, entre outros controles.
</details>

### 6. Modelo versus sistema

Explique como um modelo melhor em benchmark pode compor um sistema pior.

<details>
<summary>Ver resposta</summary>

O sistema depende também de contexto, instruções, autorização, latência, custo, interface e processo humano. Um modelo com melhor métrica média pode ser mais lento, expor dados a fornecedor inadequado ou não oferecer a modalidade e os controles exigidos.
</details>

### 7. Contexto longo versus conhecimento atualizado

Explique por que uma janela grande não resolve sozinha atualização e proveniência.

<details>
<summary>Ver resposta</summary>

A janela apenas define capacidade de entrada. A aplicação ainda precisa escolher a versão vigente, respeitar acesso, remover conteúdo irrelevante, preservar identificadores e resolver conflitos. Caber não significa ser localizado nem corretamente utilizado.
</details>

## Aplicar

### 8. Classificação de responsabilidades

**O que é:** uma classificação de responsabilidades identifica quais partes do fluxo precisam de regra repetível e quais partes lidam com percepção ou linguagem incertas. Ela não classifica o sistema inteiro como “IA”.

**Onde encontrar:** consulte [modelo, aplicação e sistema sociotécnico](conceitos.md#modelo-aplicacao-e-sistema-sociotecnico) e o [exemplo arquitetural](exemplo-arquitetural.md). Use o cenário de recibo abaixo.

**Situação**

Uma empresa fictícia quer um assistente de despesas. A entrada pode ser uma foto de recibo, mas a aprovação e o lançamento financeiro continuam sendo responsabilidades da aplicação e de uma pessoa autorizada.

**Seu papel**

Você é o arquiteto responsável por separar o que pode variar linguisticamente do que precisa obedecer a uma regra verificável.

**Insumos disponíveis**

Use os conceitos de [modelo, aplicação e sistema sociotécnico](conceitos.md#modelo-aplicacao-e-sistema-sociotecnico), o [panorama de padrões](padroes-e-decisoes.md#panorama-das-abordagens) e o caso fictício descrito acima. Não é necessário instalar uma ferramenta.

**Como conduzir**

1. Classifique autenticação, extração, verificação de limite, redação e gravação como predominantemente determinísticas ou probabilísticas.
2. Desenhe um diagrama de componentes com quatro caixas nomeadas: **Extração do recibo**, **Regra de limite**, **Proposta de despesa** e **Lançamento financeiro**. A primeira fronteira fica entre “Extração do recibo” e “Regra de limite”; a segunda fica entre “Proposta de despesa” e “Lançamento financeiro”.
3. Rotule cada seta com o dado que atravessa a fronteira: imagem e campos extraídos; valor, moeda e política vigente; proposta com justificativa; comando de lançamento com identificador do aprovador. A última seta somente pode existir depois de autorização explícita.
4. Para a foto, defina uma validação que compare o valor extraído com o recibo e encaminhe a divergência para revisão. Registre quem pode corrigir o campo e quem pode autorizar o efeito financeiro.

**Entrega esperada**

Entregue uma tabela com cinco linhas, duas justificativas de fronteira e um fluxo curto de validação da extração.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Classificação | 25% | Separa geração de texto e percepção de regra, sem tratar todo o sistema como “IA”. |
| Fronteiras | 30% | Localiza onde a saída probabilística deixa de ser autoridade. |
| Validação | 25% | Propõe comparação, limiar e revisão para um erro plausível de extração. |
| Justificativa | 20% | Liga cada escolha a risco, responsabilidade e evidência observável. |

**Como verificar antes de entregar:** confirme que as quatro caixas aparecem com esses nomes, que as duas fronteiras estão desenhadas, que cada seta tem dado e responsável e que “Lançamento financeiro” exige autorização registrada. Verifique também se uma divergência de extração não vira lançamento automático.

### 9. Cenário de qualidade

**O que é:** um cenário de qualidade transforma uma expectativa como “responder rápido” em evento, condição e medida observáveis, permitindo repetir a avaliação.

**Onde encontrar:** consulte o [Catálogo de atributos de qualidade](../referencia/atributos-de-qualidade.md), especialmente as seis partes do cenário e os exemplos de percentil.

**Situação**

O assistente documental transmite uma resposta parcial enquanto trabalha. A equipe precisa saber se o usuário recebe o primeiro conteúdo em tempo aceitável e se a resposta completa chega dentro do limite do canal.

**Seu papel**

Você é o arquiteto que transforma a palavra “rápido” em um cenário que outra pessoa consegue medir.

**Insumos disponíveis**

Consulte o [Catálogo de atributos de qualidade](../referencia/atributos-de-qualidade.md) e identifique fonte, estímulo, ambiente, artefato, resposta e medida.

**Como conduzir**

1. Escolha uma jornada, como uma pergunta sobre um documento, e declare quem inicia o estímulo.
2. Preencha as seis partes do cenário sem usar “baixa latência” como medida final.
3. Escolha percentil, população, condição de carga e janela de observação.
4. Decida se precisa medir tempo até o primeiro conteúdo, resposta completa ou os dois, e justifique.

**Entrega esperada**

Entregue um cenário em seis linhas e uma ficha de medição com população, percentil, carga e decisão quando o limite falhar.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Cenário completo | 25% | Identifica as seis partes com um evento observável e um artefato específico. |
| Medição | 35% | Define percentil, população, carga e janela que permitam repetir a medida. |
| Escolha de tempos | 25% | Distingue primeiro conteúdo de resposta completa ou explica por que um deles basta. |
| Ação | 15% | Define o que a equipe fará quando o limite não for atendido. |

**Como verificar antes de entregar:** confira se fonte, estímulo, ambiente, artefato, resposta e medida estão identificados; se a medida tem população, percentil, carga e janela; e se há uma ação definida para o caso de falha.

## Analisar

### 10. Comparação das quatro decisões

**O que é:** separar produção, conhecimento, efeito e operação evita que “usar um modelo” esconda decisões independentes.

**Onde encontrar:** use o [exemplo arquitetural](exemplo-arquitetural.md), os [padrões e decisões](padroes-e-decisoes.md#panorama-das-abordagens) e as definições de atualização, proveniência e autorização em [conceitos](conceitos.md#o-novo-contrato-arquitetural).

**Situação**

No caso Horizonte, documentos mudam, algumas perguntas exigem fonte e poucos casos podem abrir chamado após confirmação. A liderança pede um agente completo. Você precisa comparar alternativas sem condensar tudo nessa preferência.

**Seu papel**

Você é o arquiteto que conduz uma decisão inicial e precisa mostrar quais consequências ainda não foram medidas.

**Insumos disponíveis**

Use o [exemplo arquitetural](exemplo-arquitetural.md), os padrões deste módulo e as definições de atualização, proveniência e autorização em [conceitos](conceitos.md).

**Como conduzir**

1. Crie linhas para produção, conhecimento, efeito e operação.
2. Em cada linha, compare ao menos uma alternativa convencional e uma generativa.
3. Registre capacidade, responsabilidade, característica afetada e evidência disponível.
4. Separe fatos de hipóteses e formule a incógnita que poderia inverter cada direção.

**Entrega esperada**

Entregue uma matriz das quatro decisões, recomendação incremental e experimento para a incógnita de maior risco.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Decisões separadas | 20% | Não confunde produção, conhecimento, efeito e operação. |
| Consequências | 25% | Explica efeitos arquiteturais concretos, não apenas vantagens genéricas. |
| Evidências e limites | 25% | Distingue dado fornecido, hipótese e lacuna de medição. |
| Decisão provisória | 15% | Recomenda uma opção condicionada ao contexto, sem declarar vencedor universal. |
| Investigação | 15% | Propõe uma medida capaz de confirmar ou refutar a hipótese principal. |

**Como verificar antes de entregar:** confira que cada decisão possui alternativa convencional, responsabilidade e evidência; que fato e hipótese estão separados; e que o experimento pode inverter uma direção.

## Avaliar

### 11. Contestação da ficha de decisão

**O que é:** contestar uma ficha inicial significa verificar se ela contém problema, responsabilidades, alternativas e evidência suficientes para seguir ao desenho conceitual.

**Onde encontrar:** leia a [Ficha de decisão inicial](padroes-e-decisoes.md#ficha-de-decisao-inicial), a matriz anterior e o [catálogo de atributos de qualidade](../referencia/atributos-de-qualidade.md).

**Situação**

A equipe quer seguir diretamente para RAG e agente porque “são o padrão de mercado”. A frase não demonstra adequação ao caso Horizonte.

**Seu papel**

Você é o revisor arquitetural. Seu trabalho é testar a decisão, localizar premissas e dizer o que precisa acontecer antes de uma adoção.

**Insumos disponíveis**

Leia a [Ficha de decisão inicial](padroes-e-decisoes.md#ficha-de-decisao-inicial), a matriz anterior e o [catálogo de atributos de qualidade](../referencia/atributos-de-qualidade.md).

**Como conduzir**

1. Escreva o julgamento inicial: aceitar, rejeitar ou manter como experimento.
2. Liste dois direcionadores e mostre como favorecem ou enfraquecem as direções propostas.
3. Separe evidência existente de hipótese e escolha uma consequência que ainda precisa ser medida.
4. Defina limite, responsável e gatilho que fariam você rever o julgamento.

**Entrega esperada**

Entregue um parecer de até 300 palavras e uma tabela com evidência atual, hipótese, medida e gatilho de revisão.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Julgamento | 25% | Toma uma posição explícita e proporcional ao que se sabe. |
| Direcionadores | 25% | Relaciona a posição a requisitos e riscos do caso, não à tendência. |
| Evidência | 25% | Separa fato, hipótese e ausência de dado. |
| Revisão | 25% | Define medida, limite e gatilho que podem mudar a decisão. |

**Como verificar antes de entregar:** confira se o parecer declara aceitar, rejeitar ou experimentar; se cada razão aponta para um direcionador do caso; se fato, hipótese e lacuna estão separados; e se limite, responsável e gatilho permitem rever a decisão.

## Criar

### 12. Leitura arquitetural mínima

**O que é:** uma leitura arquitetural mínima é um desenho pequeno, mas completo o suficiente para mostrar propósito, responsabilidades, fronteiras, falhas e evidências de qualidade.

**Onde encontrar:** use os [conceitos](conceitos.md), a [ficha de decisão](padroes-e-decisoes.md#ficha-de-decisao-inicial), o [mapa de responsabilidades](padroes-e-decisoes.md#mapa-de-responsabilidades) e o [exemplo Horizonte](exemplo-arquitetural.md).

**Situação**

Uma equipe quer um assistente que resuma atas fornecidas pelo usuário e, opcionalmente, consulte um diretório somente para normalizar nomes. Ele não pode enviar mensagens e deve apagar a memória da conversa após 24 horas.

**Seu papel**

Você é o arquiteto que precisa compor um desenho mínimo, deixando claro onde existe inferência, onde existe regra e quem responde por cada efeito.

**Insumos disponíveis**

Use os [conceitos do módulo 1](conceitos.md#o-novo-contrato-arquitetural), o [panorama de padrões](padroes-e-decisoes.md#panorama-das-abordagens), a [ficha inicial](padroes-e-decisoes.md#ficha-de-decisao-inicial) e o mapa de exemplo. O diretório e as atas são fictícios; não use dados reais.

**Como conduzir**

1. Preencha primeiro propósito, fora de escopo, stakeholders e preocupações.
2. Separe geração, decisão, autorização e efeito; desenhe o fluxo principal.
3. Classifique conhecimento, contexto, estado, memória, evidência e trace usados.
4. Registre modelo, parâmetros, prompt, fontes, ferramentas, políticas e implantação que compõem a superfície comportamental.
5. Escreva um cenário, um teste de software, uma avaliação comportamental e uma fitness function.
6. Defina um experimento que possa refutar a hipótese de maior risco.

**Entrega esperada**

Entregue a ficha abaixo preenchida e um diagrama de contexto ou componentes acompanhado do equivalente textual.

**Template do entregável**

```text
Propósito e fora de escopo:
Stakeholders e duas preocupações:
Componentes determinísticos:
Componente(s) probabilístico(s):
Geração — decisão — autorização — efeito:
Fluxo principal:
Conhecimento — contexto — estado — memória — evidência — trace:
Superfície comportamental:
Falha 1 — consequência — contenção:
Falha 2 — consequência — contenção:
Cenário de qualidade mensurável:
Teste — avaliação — fitness function:
Hipótese de maior risco e experimento:
Diagrama:
```

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Escopo e responsabilidades | 15% | Define usuário, fora de escopo e separa geração, decisão, autorização e efeito. |
| Ciclos de informação | 20% | Separa conhecimento, contexto, estado, memória, evidência e trace. |
| Falhas e qualidade | 15% | Liga falhas a consequência, contenção e cenário mensurável. |
| Diagrama e texto | 15% | Mantém componentes, fluxos e responsabilidades consistentes nas duas formas. |
| Verificação e experimento | 15% | Distingue teste, avaliação, fitness function e experimento refutável. |
| Clareza arquitetural | 20% | Permite que outro arquiteto reconstrua a decisão sem adivinhar premissas. |

**Como verificar antes de entregar:** confira o equivalente textual, os quatro verbos de responsabilidade, os seis ciclos de informação, a superfície comportamental, as três formas de verificação e a hipótese refutável.

Concluída a prática, faça a [síntese e autoavaliação](sintese-e-referencias.md).
