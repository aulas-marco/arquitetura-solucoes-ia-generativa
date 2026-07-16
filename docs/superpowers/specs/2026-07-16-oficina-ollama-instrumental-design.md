# Desenho — Oficina instrumental com Ollama

**Data:** 16 de julho de 2026  
**Status:** aprovado para revisão do documento

## Objetivo

Reescrever a Oficina de ferramentas do Módulo 1 como um laboratório linear e executável com Ollama, eliminando a abertura abstrata sobre rotas de acesso e permitindo que um aluno iniciante observe, passo a passo, o efeito do contexto sobre uma resposta gerada.

## Experiência do aluno

A página abre com um contrato curto:

- **Ferramenta:** Ollama — executor local de modelos.
- **Você vai observar:** como o contexto altera uma resposta.
- **Tempo estimado:** 35 minutos.
- **Resultado:** uma tabela com três respostas comparáveis e uma conclusão arquitetural.

O percurso é linear. Cada etapa contém: ação, comando ou texto exato para copiar, resultado que o aluno deve enxergar e uma explicação curta de conceitos novos.

## Roteiro de laboratório

1. Baixar e instalar Ollama usando links oficiais para macOS, Windows e Linux; verificar `ollama --version`.
2. Baixar `llama3.2:3b` por `ollama pull llama3.2:3b`; explicar modelo, pesos, armazenamento e execução local.
3. Abrir chat local com `ollama run llama3.2:3b`; explicar prompt, inferência e sessão.
4. Executar Experimento A: pergunta definida sem corpus; copiar a resposta para a tabela.
5. Executar Experimento B: a mesma pergunta com corpus sintético; copiar a resposta para a tabela.
6. Executar Experimento C: repetir a condição B em nova sessão; registrar semelhanças, diferenças e variável de controle. A ferramenta de linha de comando não expõe temperatura nessa interação; não fingir que um parâmetro foi modificado.
7. Comparar qualidade, fundamentação, fonte e limite percebido; responder perguntas curtas que ligam observação e decisão arquitetural.
8. Encerrar com `Ctrl+C`, remover opcionalmente o modelo e apagar registros locais.

## Conceitos ligados ao momento de uso

No primeiro uso, cada termo recebe definição curta e hiperlink interno para o tópico conceitual correspondente:

- modelo local, prompt e inferência;
- corpus e contexto;
- fundamentação e fonte;
- variabilidade, variável de controle e alucinação.

O texto não exige que o estudante saia da oficina para entender o passo; o link serve para aprofundamento.

## Contingência

O fim da página apresenta uma única contingência: se a instalação ou a capacidade da máquina impedir a execução, o aluno usa as três saídas sintéticas fornecidas pelo professor, preenche a mesma tabela e declara a limitação. A contingência não aparece antes da receita principal e não pede conta, cartão, chave ou API.

## Critérios de aceite

1. A abertura identifica Ollama como ferramenta open source e não usa a expressão “Essencial, sem cartão”.
2. Os oito passos possuem comandos/textos copiáveis e resultado observável.
3. Cada conceito novo recebe explicação breve e link interno válido.
4. O corpus é sintético e aparece em um bloco copiável.
5. A comparação final contém três condições e perguntas arquiteturais curtas.
6. A contingência fica no final e não muda o objetivo nem o entregável.
7. Testes, validador editorial e build estrito passam.
