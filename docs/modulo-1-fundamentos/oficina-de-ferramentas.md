# Oficina de ferramentas — comportamento de modelo e contexto

**Objetivo Bloom:** Compreender e Aplicar.

**Ferramenta:** Ollama — executor local de modelos open source.
**Você vai observar:** como o contexto fornecido altera uma resposta gerada.
**Tempo estimado:** 35 minutos.
**Resultado esperado:** uma tabela com três respostas comparáveis e uma conclusão arquitetural curta.

Este é um laboratório local: não requer conta, cartão, chave ou API. Use somente o material sintético desta página; não cole dados pessoais, documentos institucionais ou conteúdo de clientes.

## Passos do laboratório

1. **Instale e confira o Ollama.** Baixe o instalador oficial para [macOS](https://ollama.com/download), [Windows](https://ollama.com/download) ou [Linux](https://ollama.com/download). Conclua a instalação indicada para seu sistema e abra um terminal. Em seguida, execute:

   ```bash
   ollama --version
   ```

   **O que observar:** o terminal mostra a versão instalada. O Ollama é um executor local: ele baixa e executa no seu equipamento os pesos de um [modelo](conceitos.md#modelo-aplicacao-e-sistema-sociotecnico), isto é, o artefato treinado que recebe entradas e produz saídas.

2. **Baixe o modelo da atividade.** Execute o comando abaixo uma vez; o download depende da sua conexão e do espaço em disco disponível.

   ```bash
   ollama pull llama3.2:3b
   ```

   **O que observar:** o Ollama informa o progresso e conclui o download de `llama3.2:3b`. Os pesos ficam armazenados localmente. Esta escolha permite fazer a [inferência](conceitos.md#treinamento-adaptacao-e-inferencia) — a execução de um modelo treinado para gerar uma saída — sem enviar o corpus a um serviço externo.

3. **Abra uma sessão local.** Inicie o chat com o modelo:

   ```bash
   ollama run llama3.2:3b
   ```

   **O que observar:** aparece um cursor para digitar mensagens. Uma sessão mantém a conversa enquanto o comando está aberto. Cada mensagem é um [prompt](conceitos.md#prompts-mensagens-e-parametros): instruções e dados que orientam a geração.

4. **Experimento A — responda sem corpus.** No cursor aberto no passo anterior, copie e envie exatamente o texto abaixo. Depois copie a resposta para a linha **Sem corpus** da tabela.

   ```text
   Qual é o prazo para solicitar reembolso? Responda em uma frase e informe a fonte quando ela estiver disponível.
   ```

   **O que observar:** o modelo pode declarar incerteza, sugerir um prazo sem fonte ou inventar uma regra. Sem uma política fornecida, ele só dispõe do que foi aprendido antes do uso; isso não prova que a resposta vale para a Política Aurora.

5. **Experimento B — acrescente o corpus sintético.** Um [corpus](conceitos.md#tokens-contexto-e-janela-de-contexto) é um conjunto de textos usado como material de trabalho; neste laboratório, ele é a Política Aurora fictícia. Copie e envie todo o bloco a seguir na mesma sessão. O corpus entra como [contexto](conceitos.md#tokens-contexto-e-janela-de-contexto), isto é, informação disponibilizada ao modelo durante esta execução.

   ```text
   Use somente a Política Aurora abaixo para responder à pergunta. Se a política não permitir uma resposta, diga que é necessária revisão humana.

   Política Aurora de reembolso (versão de treinamento):
   Solicitações de reembolso devem ser abertas em até 15 dias corridos após a compra. Para compras feitas durante campanhas especiais, o prazo é de 7 dias corridos. O atendimento deve indicar qual regra usou e pedir revisão humana se a data da compra não estiver disponível.

   Pergunta: Qual é o prazo para solicitar reembolso? Responda em uma frase e informe a fonte quando ela estiver disponível.
   ```

   **O que observar:** a resposta deve mencionar 15 dias para compra regular, 7 dias para campanha especial ou a necessidade de revisão quando a data não estiver disponível. Registre-a na linha **Com corpus** e identifique a [fundamentação](../referencia/glossario.md#fundamentacao-grounding): o apoio da resposta no texto fornecido, com a Política Aurora como fonte.

6. **Experimento C — repita com uma variável controlada.** Saia da sessão atual com `Ctrl+C`, abra uma nova sessão e envie novamente o bloco do experimento B. Registre a resposta na linha **Com corpus — repetição**.

   ```bash
   ollama run llama3.2:3b
   ```

   **O que observar:** mantenha modelo, pergunta e corpus iguais; a nova sessão é a única **variável de controle** alterada. Compare as duas respostas com corpus. Uma [variação](conceitos.md#conhecimento-parametrico-variabilidade-e-alucinacao) pode ocorrer entre execuções, mas não é uma medida de qualidade por si só. A interação de linha de comando usada aqui não expõe temperatura; não declare que modificou esse parâmetro.

   Preencha a tabela após cada execução:

   | Condição | Resposta (resumo ou transcrição curta) | Fundamentação e fonte | Limite ou incerteza observada |
   |---|---|---|---|
   | Sem corpus |  |  |  |
   | Com corpus |  |  |  |
   | Com corpus — repetição |  |  |  |

7. **Compare as evidências e responda à decisão arquitetural.** Uma [alucinação](conceitos.md#conhecimento-parametrico-variabilidade-e-alucinacao) é uma afirmação plausível que não é sustentada pelos fatos, pelo contexto ou pelas evidências disponíveis. Com base na tabela, responda em até cinco linhas:

   - Qual resposta você aceitaria apenas como rascunho e por quê?
   - Que trecho da Política Aurora torna a resposta com corpus verificável?
   - Em que situação a falta da data de compra exige fonte ou revisão humana, em vez de uma resposta automática?

   **O que observar:** a decisão não é “qual resposta venceu”, mas quando a arquitetura deve fornecer contexto, preservar sua fonte e encaminhar limites para revisão humana.

8. **Encerre e limpe o ambiente.** Interrompa qualquer sessão aberta com `Ctrl+C`. Se não for usar o modelo novamente, remova-o e apague as anotações locais que não deseja manter:

   ```bash
   ollama rm llama3.2:3b
   ```

   **O que observar:** o Ollama confirma a remoção do modelo local. Se a instalação, o download ou a capacidade da máquina impedir a execução, peça ao professor as três saídas sintéticas de referência, preencha a mesma tabela e declare a limitação encontrada. Essa contingência preserva o objetivo do laboratório, mas não transforma as saídas em prova de qualidade geral.

## Evidência a entregar

Entregue a tabela preenchida e as respostas às três perguntas arquiteturais. Declare que utilizou apenas o corpus sintético, a versão exibida por `ollama --version` e qualquer limitação percebida (tempo, memória, disco ou variação entre saídas).

Os três resultados são uma amostra de aprendizado, não uma avaliação representativa para produção. Uma decisão real também precisa de casos representativos, critérios de aceitação, evidência de fonte e revisão proporcional ao risco.
