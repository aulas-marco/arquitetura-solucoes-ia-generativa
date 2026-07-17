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

**Situação**

Uma empresa fictícia quer um assistente de despesas. A entrada pode ser uma foto de recibo, mas a aprovação e o lançamento financeiro continuam sendo responsabilidades da aplicação e de uma pessoa autorizada.

**Seu papel**

Você é o arquiteto responsável por separar o que pode variar linguisticamente do que precisa obedecer a uma regra verificável.

**Insumos disponíveis**

Use os conceitos de [modelo, aplicação e sistema sociotécnico](conceitos.md#modelo-aplicacao-e-sistema-sociotecnico), a seção de padrões e o caso fictício descrito acima. Não é necessário instalar uma ferramenta.

**Como conduzir**

1. Classifique autenticação, extração, verificação de limite, redação e gravação como predominantemente determinísticas ou probabilísticas.
2. Desenhe duas fronteiras: uma entre extração e regra de negócio, e outra entre proposta e efeito financeiro.
3. Para a foto, defina uma validação que compare o valor extraído com o recibo e encaminhe a divergência para revisão.

**Entrega esperada**

Entregue uma tabela com cinco linhas, duas justificativas de fronteira e um fluxo curto de validação da extração.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Classificação | 25% | Separa geração de texto e percepção de regra, sem tratar todo o sistema como “IA”. |
| Fronteiras | 30% | Localiza onde a saída probabilística deixa de ser autoridade. |
| Validação | 25% | Propõe comparação, limiar e revisão para um erro plausível de extração. |
| Justificativa | 20% | Liga cada escolha a risco, responsabilidade e evidência observável. |

### 9. Cenário de qualidade

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

## Analisar

### 10. Comparação arquitetural

**Situação**

No caso Horizonte, documentos mudam, algumas perguntas exigem fonte e o acervo contém informação que não deve ser enviada para qualquer usuário. Você precisa comparar três formas de fornecer conhecimento ao modelo, não escolher uma tecnologia por popularidade.

**Seu papel**

Você é o arquiteto que conduz uma decisão inicial e precisa mostrar quais consequências ainda não foram medidas.

**Insumos disponíveis**

Use o [exemplo arquitetural](exemplo-arquitetural.md), os padrões deste módulo e as definições de atualização, proveniência e autorização em [conceitos](conceitos.md).

**Como conduzir**

1. Escreva uma linha para geração direta, documentos completos no contexto e recuperação de trechos.
2. Para cada alternativa, registre atualização, proveniência, autorização, latência, custo, operação e evidência disponível.
3. Separe fatos do caso de hipóteses que ainda exigem medição.
4. Escolha uma alternativa provisória e formule uma incógnita que poderia inverter a escolha.

**Entrega esperada**

Entregue uma matriz comparativa, uma recomendação provisória de até um parágrafo e um experimento para a incógnita.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Critérios comparáveis | 20% | Usa os mesmos eixos para as três alternativas. |
| Consequências | 25% | Explica efeitos arquiteturais concretos, não apenas vantagens genéricas. |
| Evidências e limites | 25% | Distingue dado fornecido, hipótese e lacuna de medição. |
| Decisão provisória | 15% | Recomenda uma opção condicionada ao contexto, sem declarar vencedor universal. |
| Investigação | 15% | Propõe uma medida capaz de confirmar ou refutar a hipótese principal. |

## Avaliar

### 11. Contestação da ADR

**Situação**

A equipe propõe aceitar uma ADR preliminar porque “RAG é o padrão de mercado”. A frase é uma justificativa de tendência, não uma evidência de adequação ao caso Horizonte.

**Seu papel**

Você é o revisor arquitetural. Seu trabalho é testar a decisão, localizar premissas e dizer o que precisa acontecer antes de uma adoção.

**Insumos disponíveis**

Leia a ADR preliminar do módulo, a matriz do exercício anterior e o [catálogo de atributos de qualidade](../referencia/atributos-de-qualidade.md).

**Como conduzir**

1. Escreva o julgamento inicial: aceitar, rejeitar ou manter como experimento.
2. Liste dois direcionadores do caso e mostre como eles favorecem ou enfraquecem a ADR.
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

## Criar

### 12. Leitura arquitetural mínima

**Situação**

Uma equipe quer um assistente que resuma atas fornecidas pelo usuário e, opcionalmente, consulte um diretório somente para normalizar nomes. Ele não pode enviar mensagens e deve apagar a memória da conversa após 24 horas.

**Seu papel**

Você é o arquiteto que precisa compor um desenho mínimo, deixando claro onde existe inferência, onde existe regra e quem responde por cada efeito.

**Insumos disponíveis**

Use os conceitos e padrões do módulo 1, o [template de ADR](../referencia/template-adr.md) e o diagrama de exemplo arquitetural. O diretório e as atas são fictícios; não use dados reais.

**Como conduzir**

1. Preencha primeiro propósito, fora de escopo, stakeholders e preocupações.
2. Separe componentes determinísticos e probabilísticos e desenhe o fluxo principal.
3. Marque fronteiras de dados, autorização, retenção e as duas falhas mais relevantes.
4. Escreva um cenário de qualidade e um experimento que possa refutar a hipótese de maior risco.
5. Revise o diagrama verificando se cada seta tem um responsável e se nenhum componente promete o efeito sozinho.

**Entrega esperada**

Entregue a ficha abaixo preenchida e um diagrama de contexto ou componentes acompanhado do equivalente textual.

**Template do entregável**

```text
Propósito e fora de escopo:
Stakeholders e duas preocupações:
Componentes determinísticos:
Componente(s) probabilístico(s):
Fluxo principal:
Fronteiras de dados e autorização:
Falha 1 — consequência — contenção:
Falha 2 — consequência — contenção:
Cenário de qualidade mensurável:
Hipótese de maior risco e experimento:
Diagrama:
```

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Escopo e responsabilidades | 15% | Define usuário, fora de escopo e fronteiras entre regra, modelo e aplicação. |
| Dados e autorização | 20% | Explica acesso, retenção de 24 horas e descarte sem pressupor confiança implícita. |
| Falhas e qualidade | 15% | Liga falhas a consequência, contenção e cenário mensurável. |
| Diagrama e texto | 15% | Mantém componentes, fluxos e responsabilidades consistentes nas duas formas. |
| Experimento | 15% | Define hipótese, variável, evidência e condição de revisão. |
| Clareza arquitetural | 20% | Permite que outro arquiteto reconstrua a decisão sem adivinhar premissas. |

Concluída a prática, faça a [síntese e autoavaliação](sintese-e-referencias.md).
