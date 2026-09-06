# Superfície comportamental

O comportamento observável não sai do modelo sozinho: ele emerge de uma superfície que a arquitetura escolhe e pode alterar.

<a id="de-onde-emerge-o-comportamento"></a>

## Superfície comportamental

O comportamento observado resulta da configuração inteira usada em uma execução:

```text
modelo e versão
+ parâmetros de geração
+ prompt e exemplos
+ contexto e fontes
+ recuperação
+ ferramentas disponíveis
+ políticas e guardrails
+ estado e memória
+ configuração de implantação
```

Essa combinação é a **superfície comportamental**. Uma alteração em qualquer elemento pode mudar qualidade, custo, latência, segurança ou efeito sem modificar o código da aplicação. Por isso, avaliar apenas o modelo oferece evidência insuficiente para aceitar o sistema.

Guarde o nome, porque o curso volta a esse mesmo inventário sob outras duas lentes. No [Módulo 4](../modulo-4-agentes/arnes.md), a lista reaparece sem a primeira linha: tudo o que cerca o modelo, e que a engenharia pode reconstruir sem trocar de fornecedor, recebe o nome de **arnês** — arnês é a superfície comportamental menos o modelo. No [Módulo 7](../modulo-7-operacao/pacote-e-promocao.md), cada item da lista passa a ser um **ativo comportamental**, algo que precisa de versão, manifesto e portão para ser promovido. Três perguntas diferentes sobre o mesmo território: por que a saída é esta, o que eu controlo e o que eu preciso versionar.

## Modelos fundacionais e LLMs

Um **modelo fundacional** é treinado em dados amplos e pode ser adaptado a várias tarefas. Um **grande modelo de linguagem (LLM)** trabalha com padrões de linguagem em larga escala; nem todo modelo fundacional é textual e nem todo modelo útil precisa ser grande.

LLMs contemporâneos usam arquiteturas como Transformer, apresentadas em [*Attention Is All You Need*](https://proceedings.neurips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html). Para o desenho da solução, interessa que o modelo processa representações no contexto disponível. Ele não consulta automaticamente fontes corporativas, preserva permissões ou verifica cada afirmação.

Pesos podem ser abertos ou proprietários; a execução pode ocorrer como serviço, em ambiente dedicado ou sob gestão própria. Essas escolhas afetam residência de dados, elasticidade, telemetria, atualização, portabilidade, custo e responsabilidade operacional.

## Treinamento, adaptação e inferência

No **treinamento**, dados e um objetivo de otimização ajustam parâmetros. Na **inferência**, uma versão treinada processa entradas e produz saídas. Latência, disponibilidade e custo por interação aparecem no caminho de inferência.

**Fine-tuning** adapta parâmetros com dados específicos e pode melhorar formato, estilo ou comportamento recorrente. Fatos que exigem atualização, exclusão e proveniência granular precisam de fontes administráveis. A escolha entre fine-tuning, prompt, exemplos, contexto e regras depende do tipo de mudança que o sistema deverá absorver.

## Tokens, contexto e janela de contexto

Um **token** é uma unidade de processamento do modelo. Serviços usam tokens para limites e cobrança, mas sua relação com caracteres, preço e capacidade varia. Essas diferenças tornam custo e latência propriedades a medir, não valores dedutíveis apenas pelo tamanho do texto.

O **contexto** reúne o que a aplicação disponibiliza ao modelo numa execução: instruções, pedido, exemplos, trechos, resultados de ferramentas e estado permitido. A **janela de contexto** limita a entrada e a saída processadas na chamada. Um documento caber nessa janela não demonstra atualização, autorização, localização ou uso correto.

## Prompts, mensagens e parâmetros

Um **prompt** orienta a geração e pode combinar política do sistema, pedido do usuário, exemplos, contexto e especificação de saída. Quando participa de comportamento relevante, precisa de versão e avaliação. Seu contrato inclui entradas, saída esperada, modelo compatível, parâmetros, políticas, validação e tratamento de falha.

Parâmetros como **temperatura** influenciam a distribuição de saída. Temperatura menor pode reduzir diversidade, mas não garante verdade. Da mesma forma, inserir conteúdo no prompt não o converte em instrução confiável; origem, finalidade e autorização continuam pertencendo ao sistema.

## Conhecimento paramétrico, variabilidade e alucinação

**Conhecimento paramétrico** é conteúdo implicitamente representado nos parâmetros de uma versão do modelo. Ele não oferece atualização sob demanda, proveniência granular ou garantia de cobertura. Uma troca de versão também pode alterar o que aparece nas respostas.

**Variabilidade** é a mudança possível entre saídas ou versões. Pode contribuir para ideação e comprometer processos que exigem repetibilidade. **Alucinação** é conteúdo plausível sem sustentação adequada nos fatos, no contexto ou nas evidências disponíveis. Escopo, evidências, abstenção, validação, revisão e avaliação tratam dimensões diferentes desse problema.

Conhecer a superfície explica onde o comportamento pode mudar. Ainda é preciso distinguir a informação que atravessa esses elementos e a finalidade de cada registro.
