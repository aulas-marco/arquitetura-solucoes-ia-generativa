# Oficina de ferramentas — comportamento de modelo e contexto

**Objetivo Bloom:** Compreender e Aplicar.

**Ferramenta:** Ollama — executor local de modelos open source.
**Você vai observar:** como contexto e temperatura alteram uma resposta gerada.
**Tempo estimado:** 35 minutos.
**Resultado esperado:** uma tabela de respostas comparáveis e uma conclusão arquitetural curta.

Este laboratório local não requer conta, cartão, chave ou API externa. Use somente material sintético; não cole dados pessoais, institucionais ou de clientes.

## Antes de começar: o problema e o documento de treinamento

Você integra a equipe de atendimento da **empresa fictícia Aurora**. Uma pessoa pergunta qual é o prazo para pedir reembolso. A **Política Aurora** é sintética para treinamento.

Um **[corpus](conceitos.md#tokens-contexto-e-janela-de-contexto)** é o conjunto de documentos que um sistema pode consultar; aqui, o corpus tem apenas a Política Aurora. O **[contexto](conceitos.md#tokens-contexto-e-janela-de-contexto)** é a parte do corpus enviada ao modelo junto da pergunta. A **[fundamentação](../referencia/glossario.md#fundamentacao-grounding)** é o apoio da resposta nesse documento.

## Preparação local

Baixe o instalador oficial para [macOS](https://ollama.com/download), [Windows](https://ollama.com/download) ou [Linux](https://ollama.com/download), abra um terminal e execute:

```bash
ollama --version
ollama pull llama3.2:3b
```

**Observe:** o terminal mostra a versão e o progresso do download. O Ollama executa localmente os pesos de um [modelo](conceitos.md#modelo-aplicacao-e-sistema-sociotecnico), permitindo a [inferência](conceitos.md#treinamento-adaptacao-e-inferencia) sem enviar o corpus a um serviço externo.

## Roteiro sugerido para aula

- **Essencial em aula:** Experimentos A e B, para distinguir resposta sem fonte de resposta fundamentada.
- **Exploração em dupla:** Experimento C, para observar a variação entre execuções controladas.
- **Extensão:** Experimento D, para comparar duas temperaturas pela API local do Ollama.

## Experimento A — responda sem corpus

**Classificação:** Essencial em aula.

**Objetivo:** identificar o limite de uma resposta sem documento de referência.

**Pré-requisito:** conclusão da preparação local.

**Execute:** inicie uma sessão e envie exatamente o [prompt](conceitos.md#prompts-mensagens-e-parametros) abaixo.

```bash
ollama run llama3.2:3b
```

```text
Qual é o prazo para solicitar reembolso? Responda em uma frase e informe a fonte quando ela estiver disponível.
```

**Observe:** o modelo pode declarar incerteza, sugerir um prazo sem fonte ou inventar uma regra. Sem a Política Aurora, ele só dispõe do que foi aprendido antes do uso; isso não prova que a resposta vale para a empresa fictícia.

**Compare:** registre a saída na linha **Sem corpus** da tabela e compare-a com o Experimento B.

**Questões exploratórias:**

- Qual afirmação da resposta pode ser verificada sem uma fonte fornecida?
- Em qual risco de atendimento uma resposta plausível, mas sem fonte, deixa de ser aceitável?
- Que decisão arquitetural impediria apresentar essa saída como política da Aurora?

## Experimento B — responda com o documento de treinamento

**Classificação:** Essencial em aula.

**Objetivo:** observar como contexto sintético e fonte tornam uma resposta verificável.

**Pré-requisito:** Experimento A concluído; mantenha a sessão do Ollama aberta.

**Execute:** copie o bloco inteiro abaixo para o cursor do Ollama e pressione `Enter` uma vez.

```text
Use somente a Política Aurora abaixo para responder à pergunta. Se a política não permitir uma resposta, diga que é necessária revisão humana.

Política Aurora de reembolso (versão de treinamento):
Solicitações de reembolso devem ser abertas em até 15 dias corridos após a compra. Para compras feitas durante campanhas especiais, o prazo é de 7 dias corridos. O atendimento deve indicar qual regra usou e pedir revisão humana se a data da compra não estiver disponível.

Pergunta: Qual é o prazo para solicitar reembolso? Responda em uma frase e informe a fonte quando ela estiver disponível.
```

**Observe:** a resposta deve mencionar 15 dias para compra regular, 7 dias para campanha especial ou a necessidade de revisão quando a data não estiver disponível. Registre “Política Aurora” como fonte.

**Compare:** compare esta saída com a do Experimento A: há uma regra citável e um limite explícito quando a data da compra não está disponível?

**Questões exploratórias:**

- Qual trecho da Política Aurora fundamenta cada prazo citado?
- Qual atributo de qualidade melhora quando a resposta preserva sua fonte?
- Em que caso a arquitetura deve encaminhar a pessoa para revisão humana?

## Experimento C — repita com uma variável controlada

**Classificação:** Exploração em dupla.

**Objetivo:** observar a [variação](conceitos.md#conhecimento-parametrico-variabilidade-e-alucinacao) entre execuções com o mesmo contexto.

**Pré-requisito:** Experimento B concluído e sua resposta registrada.

**Execute:** interrompa a sessão com `Ctrl+C`, abra uma nova sessão e envie novamente, sem alterar, o bloco completo do Experimento B.

```bash
ollama run llama3.2:3b
```

**Observe:** mantenha modelo, pergunta e corpus iguais; a nova sessão é a única variável alterada. A variação pode ocorrer entre execuções, mas não é uma medida de qualidade por si só.

**Compare:** registre a saída em **Com corpus — repetição** e compare formulação, fonte e encaminhamento para revisão humana com a primeira resposta com corpus.

**Questões exploratórias:**

- Quais diferenças são apenas de redação e quais mudam uma decisão de atendimento?
- Que critério de aceitação verificaria a fundamentação nas duas execuções?
- Qual risco aparece se um teste avalia apenas uma execução do modelo?

## Experimento D — compare temperaturas pela API local

**Classificação:** Extensão.

**Objetivo:** comparar a diversidade de respostas quando apenas a temperatura muda.

**Pré-requisito:** o modelo `llama3.2:3b` foi baixado e o serviço local do Ollama está em execução.

**Execute:** rode os dois comandos abaixo. Eles usam o mesmo modelo, prompt e corpus sintético; muda somente `options.temperature`. Cada resposta vem no campo JSON `response`.

```bash
curl -s http://localhost:11434/api/generate \
  -d '{
    "model": "llama3.2:3b",
    "prompt": "Use somente a Política Aurora abaixo para responder à pergunta. Se a política não permitir uma resposta, diga que é necessária revisão humana.\n\nPolítica Aurora de reembolso (versão de treinamento):\nSolicitações de reembolso devem ser abertas em até 15 dias corridos após a compra. Para compras feitas durante campanhas especiais, o prazo é de 7 dias corridos. O atendimento deve indicar qual regra usou e pedir revisão humana se a data da compra não estiver disponível.\n\nPergunta: Qual é o prazo para solicitar reembolso? Responda em uma frase e informe a fonte quando ela estiver disponível.",
    "stream": false,
    "options": {"temperature": 0.1}
  }'
```

```bash
curl -s http://localhost:11434/api/generate \
  -d '{
    "model": "llama3.2:3b",
    "prompt": "Use somente a Política Aurora abaixo para responder à pergunta. Se a política não permitir uma resposta, diga que é necessária revisão humana.\n\nPolítica Aurora de reembolso (versão de treinamento):\nSolicitações de reembolso devem ser abertas em até 15 dias corridos após a compra. Para compras feitas durante campanhas especiais, o prazo é de 7 dias corridos. O atendimento deve indicar qual regra usou e pedir revisão humana se a data da compra não estiver disponível.\n\nPergunta: Qual é o prazo para solicitar reembolso? Responda em uma frase e informe a fonte quando ela estiver disponível.",
    "stream": false,
    "options": {"temperature": 0.9}
  }'
```

**Observe:** [temperatura](conceitos.md#prompts-mensagens-e-parametros) menor tende a tornar a escolha de palavras mais repetível; temperatura maior tende a aumentar a diversidade. Temperatura não prova factualidade, nem substitui contexto, fonte ou revisão humana.

**Compare:** registre as duas saídas nas linhas de temperatura da tabela. Compare diversidade de formulação, fundamentação na Política Aurora e correção dos prazos e do limite de revisão humana.

**Questões exploratórias:**

- A temperatura `0.9` aumentou a diversidade sem perder fundamentação? Mostre o trecho que sustenta sua avaliação.
- Se as duas respostas citam a política, como você verificaria a correção dos prazos e da condição de revisão humana?
- Em um atendimento de maior risco, qual temperatura escolheria e que controle adicional usaria para não confundir diversidade com factualidade?

## Registro e decisão arquitetural

Preencha a tabela após cada execução:

| Condição | Resposta (resumo ou transcrição curta) | Fundamentação e fonte | Limite ou incerteza observada |
|---|---|---|---|
| Sem corpus |  |  |  |
| Com corpus |  |  |  |
| Com corpus — repetição |  |  |  |
| Temperatura 0.1 |  |  |  |
| Temperatura 0.9 |  |  |  |

Uma [alucinação](conceitos.md#conhecimento-parametrico-variabilidade-e-alucinacao) é uma afirmação plausível que não é sustentada pelos fatos, pelo contexto ou pelas evidências disponíveis. Em até cinco linhas, responda:

- Qual resposta você aceitaria apenas como rascunho e por quê?
- Que trecho da Política Aurora torna a resposta com corpus verificável?
- Quando a falta da data de compra exige fonte ou revisão humana, em vez de uma resposta automática?

**Observe:** a decisão não é “qual resposta venceu”, mas quando a arquitetura deve fornecer contexto, preservar sua fonte e encaminhar limites para revisão humana.

## Encerramento e evidência a entregar

Interrompa qualquer sessão aberta com `Ctrl+C`. Se não for usar o modelo novamente, remova-o:

```bash
ollama rm llama3.2:3b
```

Entregue a tabela preenchida e as respostas às questões exploratórias. Declare o corpus sintético, a versão exibida por `ollama --version` e qualquer limitação percebida (tempo, memória, disco ou variação entre saídas).

Se a instalação, o download ou a capacidade da máquina impedir a execução, peça ao professor saídas sintéticas de referência, preencha a mesma tabela e declare a limitação. Essas saídas preservam o objetivo do laboratório, mas não transformam a amostra em prova de qualidade geral: uma decisão real também precisa de casos representativos, critérios de aceitação, evidência de fonte e revisão proporcional ao risco.
