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

A Contafácil é uma fintech fictícia de gestão de despesas corporativas. Hoje um analista recebe a foto de um recibo, digita valor, moeda e categoria à mão e só então o lançamento segue para aprovação. A diretoria quer um assistente que leia a foto e proponha o lançamento, mas duas regras não podem mudar: nenhum valor entra no sistema financeiro sem checagem contra a política de limite vigente, e nenhum lançamento é efetivado sem aprovação de uma pessoa autorizada.

**Exemplo de recibo:** foto de um recibo de locadora de veículos, valor R$ 187,40, categoria “transporte”. A política de viagem define limite diário de R$ 250 para essa categoria — o valor está dentro do limite, mas o sistema só pode confirmar isso depois de extrair o valor corretamente.

**Seu papel**

Você é o arquiteto responsável por separar o que pode variar linguisticamente do que precisa obedecer a uma regra verificável.

**Insumos disponíveis**

Use os conceitos de [modelo, aplicação e sistema sociotécnico](conceitos.md#modelo-aplicacao-e-sistema-sociotecnico), o [panorama de padrões](padroes-e-decisoes.md#panorama-das-abordagens) e o caso Contafácil descrito acima. Não é necessário instalar uma ferramenta.

**Como conduzir**

1. Classifique autenticação, extração, verificação de limite, redação e gravação como predominantemente determinísticas ou probabilísticas.
2. Desenhe um diagrama de componentes com quatro caixas nomeadas: **Extração do recibo**, **Regra de limite**, **Proposta de despesa** e **Lançamento financeiro**. A primeira fronteira fica entre “Extração do recibo” e “Regra de limite”; a segunda fica entre “Proposta de despesa” e “Lançamento financeiro”.
3. Rotule cada seta com o dado que atravessa a fronteira: imagem e campos extraídos (ex.: R$ 187,40, “transporte”); valor, moeda e política vigente; proposta com justificativa; comando de lançamento com identificador do aprovador. A última seta só existe depois de autorização explícita.
4. Usando o exemplo do recibo, defina uma validação que compare o valor extraído com o recibo e encaminhe qualquer divergência para revisão. Registre quem pode corrigir o campo e quem pode autorizar o efeito financeiro.

**Entrega esperada**

Entregue três itens: (1) a tabela de classificação com as cinco atividades — autenticação, extração, verificação de limite, redação e gravação; (2) o diagrama de componentes com as quatro caixas e as duas fronteiras rotuladas (passos 2 e 3); (3) o fluxo curto de validação da extração para o exemplo do recibo (passo 4).

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Classificação (item 1) | 25% | Separa geração de texto e percepção de regra, sem tratar todo o sistema como “IA”. |
| Diagrama e fronteiras (item 2) | 30% | Localiza, no diagrama, onde a saída probabilística deixa de ser autoridade. |
| Validação (item 3) | 25% | Propõe comparação, limiar e revisão para o exemplo do recibo. |
| Justificativa | 20% | Liga cada escolha a risco, responsabilidade e evidência observável. |

**Como verificar antes de entregar:** confirme que os três itens foram entregues; que as quatro caixas do diagrama aparecem com esses nomes; que as duas fronteiras estão desenhadas; que cada seta tem dado e responsável; e que “Lançamento financeiro” exige autorização registrada. Verifique também se uma divergência de extração não vira lançamento automático.

### 9. Cenário de qualidade

**O que é:** um cenário de qualidade transforma uma expectativa como “responder rápido” em evento, condição e medida observáveis, permitindo repetir a avaliação.

**Onde encontrar:** consulte o [Catálogo de atributos de qualidade](../referencia/atributos-de-qualidade.md) — o próprio cenário de **Latência** já está totalmente preenchido lá e serve de modelo de formato. Não copie os valores dele: o caso abaixo tem canal, população e limite próprios.

**Situação**

O Redator é um assistente documental embutido no chat interno da empresa Malbec Jurídico, hoje usado por cerca de 500 consultas por dia. Ele transmite a resposta token a token enquanto gera, como texto sendo digitado. Nas últimas semanas, usuários reclamaram que “a tela fica travada por 6 a 9 segundos antes de aparecer qualquer coisa”. A liderança pediu à equipe uma definição de “rápido” que possa ser medida, não apenas prometida.

**Seu papel**

Você é o arquiteto que transforma a palavra “rápido” em um cenário que outra pessoa consegue medir.

**Insumos disponíveis**

Consulte o [Catálogo de atributos de qualidade](../referencia/atributos-de-qualidade.md), identifique fonte, estímulo, ambiente, artefato, resposta e medida, e observe como o cenário de **Latência** já publicado usa p95 para dois momentos distintos (primeiro conteúdo e resposta completa).

**Como conduzir**

1. Escolha uma jornada do Redator, como “um analista pergunta sobre uma cláusula de contrato”, e declare quem inicia o estímulo.
2. Preencha as seis partes do cenário para essa jornada, sem usar “baixa latência” como medida final.
3. Escolha percentil, população (todos os usuários? só os do plano mais lento?) e janela de observação.
4. Decida se o Redator precisa medir tempo até o primeiro conteúdo, resposta completa ou os dois, e justifique com base na reclamação relatada.

**Entrega esperada**

Entregue um cenário em seis linhas e uma ficha de medição com população, percentil, janela e decisão para quando o limite falhar.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Cenário completo | 25% | Identifica as seis partes com um evento observável e um artefato específico do Redator. |
| Medição | 35% | Define percentil, população e janela que permitam repetir a medida. |
| Escolha de tempos | 25% | Distingue primeiro conteúdo de resposta completa ou explica por que um deles basta. |
| Ação | 15% | Define o que a equipe fará quando o limite não for atendido. |

**Como verificar antes de entregar:** confira se fonte, estímulo, ambiente, artefato, resposta e medida estão identificados; se a medida tem população, percentil e janela; e se há uma ação definida para o caso de falha.

### 10. Evidência do laboratório de comportamento

**O que é:** organizar os resultados de um laboratório empírico segundo os três tipos de verificação evita tratar uma execução isolada — ou cinco — como prova de qualidade geral.

**Onde encontrar:** use a tabela preenchida e as respostas às questões exploratórias do [Resultado esperado](oficina-de-ferramentas.md#resultado-esperado) da oficina de ferramentas — os cinco registros das condições Sem corpus, Com corpus, Com corpus — repetição, Temperatura 0.1 e Temperatura 0.9 — junto com os [três tipos de verificação](conceitos.md#tres-tipos-de-verificacao) e as definições de [variabilidade e alucinação](conceitos.md#conhecimento-parametrico-variabilidade-e-alucinacao).

**Situação**

Você concluiu a oficina de ferramentas com o Ollama e a Política Aurora de reembolso sintética. Um colega, vendo apenas a resposta do Experimento B (com corpus), conclui: “deu certo, já podemos confiar nesse modelo para responder sobre reembolso”. Seu papel é usar sua própria tabela preenchida para mostrar por que essas cinco execuções não sustentam essa conclusão sem qualificar o tipo de evidência.

**Seu papel**

Você é o arquiteto que precisa transformar observações de bancada em evidência classificada, apta — ou não — a entrar numa ficha de decisão.

**Insumos disponíveis**

Sua tabela preenchida do [Resultado esperado](oficina-de-ferramentas.md#resultado-esperado), com as cinco condições e as respostas às questões exploratórias de cada experimento; a tabela de [três tipos de verificação](conceitos.md#tres-tipos-de-verificacao) em Conceitos; as definições de [variabilidade e alucinação](conceitos.md#conhecimento-parametrico-variabilidade-e-alucinacao).

**Como conduzir**

1. Para cada uma das cinco condições da sua tabela, classifique o que ela permitiria verificar — teste de software, avaliação comportamental ou nenhum dos dois — e justifique em uma frase.
2. Compare a resposta **Com corpus** e a resposta **Com corpus — repetição**: aponte uma diferença que seria apenas de redação e uma diferença (real ou hipotética, se as duas respostas foram idênticas) que mudaria uma decisão de atendimento.
3. Compare **Temperatura 0.1** e **Temperatura 0.9**: a maior diversidade observada acompanhou perda de fundamentação na Política Aurora? Cite o trecho da resposta que sustenta sua conclusão.
4. Em até quatro frases, explique por que a afirmação do colega (“já podemos confiar”) ignora o tamanho da amostra e o tipo de verificação disponível, e proponha um próximo experimento (por exemplo, um conjunto maior de perguntas estratificadas) que reduziria essa lacuna.

**Entrega esperada**

Entregue a classificação das cinco condições (passo 1), a comparação de repetição e de temperatura (passos 2 e 3) e o parecer de até quatro frases sobre a afirmação do colega, com o próximo experimento proposto (passo 4).

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Classificação das condições | 30% | Associa cada uma das cinco condições a um tipo de verificação (ou a nenhum), com justificativa coerente com a tabela de Conceitos. |
| Comparação de repetição e temperatura | 35% | Distingue variação de redação de variação que afeta decisão; liga diversidade a fundamentação, não a factualidade. |
| Parecer sobre a afirmação do colega | 35% | Explica por que amostra pequena e verificação limitada não sustentam confiança geral; propõe um próximo experimento concreto e mensurável. |

**Como verificar antes de entregar:** confira que as cinco condições foram classificadas; que a comparação cita ao menos um trecho da sua própria tabela; que o parecer nomeia o tipo de verificação ausente e propõe um experimento seguinte mensurável.

## Analisar

### 11. Comparação das quatro decisões

**O que é:** separar produção, conhecimento, efeito e operação evita que “usar um modelo” esconda decisões independentes.

**Onde encontrar:** use o [exemplo arquitetural](exemplo-arquitetural.md), os [padrões e decisões](padroes-e-decisoes.md#panorama-das-abordagens) e as definições de atualização, proveniência e autorização em [conceitos](conceitos.md#o-novo-contrato-arquitetural).

**Situação**

No [caso Horizonte](exemplo-arquitetural.md), o piloto atende perguntas sobre vinte políticas de viagem com dono e vigência confirmados; em um teste com 30 perguntas, 24 foram respondidas de forma aceitável usando documentos escolhidos manualmente. As políticas mudam de versão com frequência, algumas perguntas exigem citar a fonte, e poucos casos poderiam abrir um chamado depois de confirmação humana. Depois de ver o piloto funcionar, a liderança pediu à equipe: “por que não fazemos logo um agente completo, que decide sozinho e já abre o chamado quando tiver certeza?”. Seu trabalho é comparar alternativas para as quatro decisões sem deixar essa preferência decidir por você.

**Exemplo parcial (linha “Produção”):** alternativa convencional = manter a busca atual, com o analista lendo o documento inteiro; alternativa generativa = manter a redação automática já testada no piloto; evidência disponível = 24 de 30 respostas aceitáveis. Complete as três linhas restantes seguindo esse mesmo padrão.

**Seu papel**

Você é o arquiteto que conduz uma decisão inicial e precisa mostrar quais consequências ainda não foram medidas.

**Insumos disponíveis**

Use o [exemplo arquitetural](exemplo-arquitetural.md), os padrões deste módulo e as definições de atualização, proveniência e autorização em [conceitos](conceitos.md).

**Como conduzir**

1. Crie linhas para produção, conhecimento, efeito e operação; comece pela linha “Produção” já iniciada acima.
2. Em cada linha, compare ao menos uma alternativa convencional e uma generativa, registrando capacidade, responsabilidade e evidência disponível.
3. Separe fatos (como o 24 de 30) de hipóteses (como “um agente completo reduziria mais tempo”).
4. Para a linha “Efeito”, formule a incógnita que poderia inverter a direção — por exemplo, se abrir chamado sozinho preservaria a taxa de acerto observada no piloto.

**Entrega esperada**

Entregue a matriz das quatro decisões e uma recomendação incremental para a incógnita da linha “Efeito”.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Decisões separadas | 25% | Não confunde produção, conhecimento, efeito e operação. |
| Evidências e limites | 35% | Distingue dado fornecido (como o 24 de 30), hipótese e lacuna de medição. |
| Decisão provisória | 40% | Recomenda uma opção condicionada ao contexto para a incógnita de “Efeito”, sem declarar vencedor universal. |

**Como verificar antes de entregar:** confira que cada decisão possui alternativa convencional, responsabilidade e evidência; que fato e hipótese estão separados; e que a incógnita de “Efeito” está formulada de forma testável.

## Avaliar

### 12. Contestação da ficha de decisão

**O que é:** contestar uma ficha inicial significa verificar se ela contém problema, responsabilidades, alternativas e evidência suficientes para seguir ao desenho conceitual.

**Onde encontrar:** leia a [Ficha de decisão inicial](padroes-e-decisoes.md#ficha-de-decisao-inicial) — reproduzida abaixo com os dados do caso Horizonte — e o [catálogo de atributos de qualidade](../referencia/atributos-de-qualidade.md). Se você já fez o exercício 11, reaproveite sua matriz das quatro decisões.

**Situação**

A ficha de decisão do caso Horizonte já registra: *situação* — analistas gastam tempo localizando políticas e explicando-as; *prioridades* — fundamentação e privacidade antes de cobertura, p95 abaixo de oito segundos; *evidência* — 24 de 30 perguntas aceitáveis com documentos escolhidos manualmente. Mesmo com esses dados na mesa, um membro da equipe argumenta em uma reunião: “RAG e agente são o padrão de mercado, vamos direto para lá”. A frase não cita nenhum dado da ficha.

**Seu papel**

Você é o revisor arquitetural. Seu trabalho é testar a afirmação “é o padrão de mercado” contra a ficha e dizer o que precisa acontecer antes de uma adoção.

**Insumos disponíveis**

Leia a [Ficha de decisão inicial](padroes-e-decisoes.md#ficha-de-decisao-inicial) e o [catálogo de atributos de qualidade](../referencia/atributos-de-qualidade.md). Use os dados do caso Horizonte reproduzidos acima.

**Como conduzir**

1. Escreva o julgamento inicial: aceitar, rejeitar ou manter como experimento a proposta de ir direto para RAG e agente.
2. Aponte dois dados da ficha (por exemplo, o 24 de 30 e o p95 de oito segundos) que a frase “padrão de mercado” ignora.
3. Defina um limite e um gatilho que fariam você rever o julgamento — por exemplo, uma taxa de suporte abaixo de 80% em teste piloto.

**Entrega esperada**

Entregue um parecer de até 200 palavras citando os dois dados da ficha e o gatilho de revisão.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Julgamento | 30% | Toma uma posição explícita (aceitar, rejeitar ou experimentar). |
| Evidência da ficha | 40% | Cita ao menos dois dados concretos da ficha, não a tendência de mercado. |
| Gatilho de revisão | 30% | Define um limite e uma condição que fariam a decisão ser revista. |

**Como verificar antes de entregar:** confira se o parecer declara aceitar, rejeitar ou experimentar; se cita pelo menos dois dados da ficha (não “padrão de mercado”); e se o gatilho de revisão é mensurável.

## Criar

### 13. Leitura arquitetural mínima

**O que é:** uma leitura arquitetural mínima é um desenho pequeno, mas completo o suficiente para mostrar propósito, responsabilidades, fronteiras e evidências de qualidade. Este exercício reúne, em um único caso, os elementos praticados nos exercícios 8, 9, 11 e 12.

**Onde encontrar:** use os [conceitos](conceitos.md), a [ficha de decisão](padroes-e-decisoes.md#ficha-de-decisao-inicial), o [mapa de responsabilidades](padroes-e-decisoes.md#mapa-de-responsabilidades) e o [exemplo Horizonte](exemplo-arquitetural.md).

**Situação**

A Registra é uma equipe fictícia de secretaria executiva. Ela quer um assistente que resuma atas de reunião coladas pelo próprio usuário — por exemplo, um trecho como “presentes: Ana, Bruno e o fornecedor externo; decidido adiar a integração para o próximo trimestre”. Opcionalmente, o assistente pode consultar um diretório interno (nomes e cargos, sem dados de contato) apenas para corrigir a grafia de nomes citados na ata. Por exigência de privacidade da equipe jurídica, o assistente **não pode enviar mensagens** a ninguém e deve **apagar a memória da conversa após 24 horas** — ele só ajuda a redigir o resumo; não distribui nada.

**Seu papel**

Você é o arquiteto que precisa compor um desenho mínimo, deixando claro onde existe inferência, onde existe regra e quem responde por cada efeito.

**Insumos disponíveis**

Use os [conceitos do módulo 1](conceitos.md#o-novo-contrato-arquitetural), o [panorama de padrões](padroes-e-decisoes.md#panorama-das-abordagens), a [ficha inicial](padroes-e-decisoes.md#ficha-de-decisao-inicial) e o mapa de exemplo. O diretório e as atas são fictícios; não use dados reais.

**Como conduzir**

1. Preencha propósito, fora de escopo, stakeholders e duas preocupações (privacidade e correção de nomes, por exemplo); classifique os componentes do fluxo — leitura da ata, consulta ao diretório, redação do resumo — como determinísticos ou probabilísticos.
2. Separe geração, decisão, autorização e efeito para o fluxo de resumo; desenhe o fluxo principal com o exemplo de ata acima.
3. Classifique o que o assistente usa como conhecimento (diretório), contexto (ata colada) e memória (nenhuma além de 24 horas).
4. Escreva um cenário de qualidade mensurável e uma forma de verificação (um teste de software **ou** uma avaliação comportamental) para a falha mais provável: o assistente citar um nome incorreto do diretório.

**Entrega esperada**

Entregue a ficha abaixo preenchida e um diagrama de componentes acompanhado do equivalente textual.

**Template do entregável**

```text
Propósito e fora de escopo:
Stakeholders e duas preocupações:
Componentes determinísticos e probabilístico(s):
Geração — decisão — autorização — efeito:
Fluxo principal (use o exemplo de ata):
Conhecimento — contexto — memória usados:
Falha mais provável — consequência — contenção:
Cenário de qualidade mensurável:
Verificação (teste ou avaliação):
Diagrama:
```

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Escopo e responsabilidades | 25% | Define stakeholders, fora de escopo, classifica os componentes do fluxo como determinísticos ou probabilísticos e separa geração, decisão, autorização e efeito. |
| Informação usada | 25% | Separa conhecimento (diretório), contexto (ata) e memória (24 horas), sem confundir os três. |
| Falha e qualidade | 25% | Liga a falha mais provável a consequência, contenção e um cenário mensurável. |
| Diagrama e texto | 25% | Mantém componentes e fluxo consistentes entre o diagrama e o equivalente textual. |

**Como verificar antes de entregar:** confira o equivalente textual, a classificação determinístico/probabilístico dos três componentes, os quatro verbos de responsabilidade, a separação entre conhecimento, contexto e memória, e se a falha de nome incorreto tem contenção definida.

Concluída a prática, faça a [síntese e autoavaliação](sintese-e-referencias.md).
