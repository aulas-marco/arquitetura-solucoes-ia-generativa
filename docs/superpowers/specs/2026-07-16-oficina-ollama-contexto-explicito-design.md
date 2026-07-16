# Desenho — contexto explícito na Oficina Ollama

**Data:** 16 de julho de 2026  
**Status:** aprovado para revisão do documento

## Objetivo

Eliminar instruções implícitas da Oficina 1, situando o cenário fictício Aurora e guiando literalmente cada ação do estudante para usar um corpus como contexto no Ollama.

## Abertura pelo problema

Antes de instalar qualquer ferramenta, a oficina apresenta o cenário:

> Você integra a equipe de atendimento da empresa fictícia Aurora. Uma pessoa pergunta qual é o prazo para pedir reembolso. Você receberá um único documento interno fictício e observará o que acontece quando o modelo responde sem e com esse documento.

A Política Aurora é apresentada como um documento fictício de treinamento. O texto explica que **corpus** é o conjunto de documentos que um sistema pode consultar e que, nesta prática, o corpus tem um único documento. **Contexto** é a parte desse corpus enviada ao modelo junto da pergunta.

## Instrução operacional

Cada execução informa, na ordem:

1. onde a ação acontece: navegador, Terminal ou cursor `>>>` do Ollama;
2. o que copiar, em bloco único e delimitado;
3. como colar: `Cmd+V` no macOS ou `Ctrl+Shift+V` em Windows/Linux;
4. que tecla pressionar: `Enter` uma vez;
5. o que esperar: resposta, cursor ou mensagem de erro;
6. o que registrar: resposta, fonte, limite ou falha na tabela.

O Experimento B não diz “acrescente o corpus”. Ele manda copiar o bloco completo, colá-lo diretamente após aparecer o cursor `>>>`, pressionar Enter e aguardar a resposta. O bloco contém instrução, Política Aurora e pergunta; nenhum trecho fica para o aluno montar.

## Critérios de aceite

1. O texto situa Aurora e Política Aurora como empresa e documento fictícios antes de usar o termo corpus.
2. Corpus e contexto recebem definição simples e link interno.
3. Os experimentos A, B e C informam local, ação de copiar/colar, tecla, resultado esperado e registro.
4. A prática não contém a frase “acrescente o corpus”.
5. A Política Aurora e a pergunta aparecem em bloco único copiável no Experimento B.
