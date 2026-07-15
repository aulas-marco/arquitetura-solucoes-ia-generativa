# Exercícios

Tente responder antes de abrir os blocos de feedback. Nas atividades de projeto, use as rubricas como critérios de qualidade, não como lista mecânica. A progressão segue a [Taxonomia de Bloom](../comecar/taxonomia-de-bloom.md).

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

### 4. Abordagens

Identifique duas abordagens que mantêm o fluxo sob controle explícito e duas que acrescentam conhecimento ou capacidade externa.

<details>
<summary>Ver resposta</summary>

Geração direta e workflow com LLM preservam um caminho explícito. Contexto fornecido e RAG acrescentam conhecimento externo; uso de ferramentas acrescenta consulta ou ação. Outras combinações são válidas se justificadas.
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

Para um assistente de despesas, classifique como predominantemente determinística ou probabilística: autenticar usuário; extrair valor de uma foto; verificar limite de R$ 500; redigir explicação; gravar aprovação. Justifique duas fronteiras e proponha validação para a extração.

**Rubrica (0–3 pontos):** 1 ponto pela classificação coerente; 1 pelas justificativas relacionando regra e variabilidade; 1 por validar tipo, faixa e conferência com a evidência visual antes de qualquer efeito.

### 9. Cenário de qualidade

Use o [Catálogo de atributos de qualidade](../referencia/atributos-de-qualidade.md) para escrever um cenário mensurável de latência para o assistente documental. Inclua as seis partes e proponha uma forma de medição.

**Rubrica (0–3 pontos):** 1 ponto pelas seis partes completas; 1 por medidas com percentil e condição de carga; 1 por distinguir tempo até primeiro conteúdo e resposta completa ou justificar por que apenas um deles importa.

## Analisar

### 10. Comparação arquitetural

Compare geração direta, documentos completos no contexto e contexto por recuperação para o caso Horizonte. Construa uma matriz com atualização, proveniência, autorização, latência, custo, complexidade operacional e evidências disponíveis. Identifique uma incógnita que poderia inverter sua escolha.

**Rubrica (0–4 pontos):** 1 ponto por critérios definidos; 1 por consequências específicas, sem declarar vencedor universal; 1 por usar as evidências e reconhecer suas limitações; 1 por uma incógnita testável ligada à decisão.

## Avaliar

### 11. Contestação da ADR

A equipe propõe aceitar a ADR preliminar deste módulo porque “RAG é o padrão de mercado”. Avalie a proposta. Defenda aceitar, rejeitar ou manter como experimento e estabeleça condições de revisão.

**Rubrica (0–4 pontos):** 1 ponto por julgamento explícito; 1 por relacioná-lo a direcionadores; 1 por separar evidência existente de hipótese; 1 por critérios mensuráveis e gatilhos que poderiam mudar o julgamento.

## Criar

### 12. Leitura arquitetural mínima

Projete uma arquitetura de referência para um assistente que resume atas fornecidas pelo usuário e, opcionalmente, consulta um diretório para normalizar nomes. O sistema não pode enviar mensagens nem manter memória após 24 horas. Produza um diagrama e uma ficha de decisão.

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

**Rubrica (0–5 pontos):** 1 ponto por escopo e stakeholders; 1 por separação coerente entre responsabilidades; 1 por dados, retenção e autorização; 1 por falhas e cenário verificável; 1 por diagrama consistente e experimento capaz de refutar a hipótese.

Concluída a prática, faça a [síntese e autoavaliação](sintese-e-referencias.md).
