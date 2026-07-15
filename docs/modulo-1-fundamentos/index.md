# Módulo 1 — Fundamentos de sistemas com IA generativa

> **Pergunta-guia:** O que muda quando parte do sistema deixa de ser determinística?

Arquitetar uma solução generativa não é apenas acrescentar uma API de modelo a um software convencional. O modelo introduz uma forma probabilística de produzir resultados: duas execuções semelhantes podem variar, uma resposta fluente pode estar errada e uma mudança de contexto pode alterar o comportamento sem que o código da aplicação tenha mudado. Isso desloca parte do trabalho arquitetural de “garantir uma saída por regra” para “delimitar, medir e governar um espaço de comportamentos”.

Este módulo constrói o vocabulário necessário para fazer essa leitura. Primeiro separaremos modelo, aplicação e sistema sociotécnico; depois reconheceremos as propriedades técnicas que influenciam contexto, custo, qualidade e risco. Só então veremos padrões de solução e aplicaremos o raciocínio a um assistente interno de documentos.

## Antes de começar

Você deve reconhecer noções básicas de arquitetura de software: componente, interface, dependência, fluxo de dados, requisito funcional, atributo de qualidade e trade-off. Não é necessário conhecer aprendizado de máquina, estatística ou a matemática dos transformadores. Quando um termo controlado aparecer, consulte o [Glossário](../referencia/glossario.md); para transformar uma qualidade desejada em cenário verificável, use o [Catálogo de atributos de qualidade](../referencia/atributos-de-qualidade.md).

**Tempo estimado de leitura:** 60–90 minutos, sem contar os exercícios de projeto.

## Objetivos de aprendizagem

Ao concluir o módulo, você deverá ser capaz de:

1. **Compreender** e explicar por que modelo generativo, aplicação de IA e sistema de IA são unidades de análise diferentes.
2. **Compreender** e distinguir componentes determinísticos e probabilísticos, relacionando variabilidade, alucinação e conhecimento paramétrico.
3. **Aplicar** o vocabulário de tokens, contexto, prompts, embeddings, inferência e multimodalidade à leitura de uma solução.
4. **Analisar** o que geração direta, contexto fornecido, RAG, ferramentas, workflows, agentes e fine-tuning acrescentam à arquitetura.
5. **Analisar** uma arquitetura em camadas e antecipar consequências para qualidade, latência, custo, privacidade, segurança e operação.

## Roteiro do módulo

| Página | Questão central | Resultado esperado |
|---|---|---|
| **1. Abertura** | O que vamos aprender e em qual ordem? | Um contrato de aprendizagem comum. |
| **2. [Conceitos](conceitos.md)** | Que propriedades técnicas mudam nossas decisões? | Um vocabulário para ler sistemas generativos. |
| **3. [Padrões e decisões](padroes-e-decisoes.md)** | Que alternativas existem e o que cada uma adiciona? | Um panorama comparável e uma ADR preliminar. |
| **4. [Exemplo arquitetural](exemplo-arquitetural.md)** | Como os componentes colaboram no caminho de uma resposta? | Uma leitura em oito camadas, com falhas e qualidades. |
| **5. [Estudo de caso](estudo-de-caso.md)** | Como escolher uma direção para um assistente documental? | Uma recomendação sustentada por restrições e evidências. |
| **6. [Exercícios](exercicios.md)** | Consigo recordar, aplicar e defender os conceitos? | Evidências de aprendizagem nos seis níveis de Bloom. |
| **7. [Síntese e referências](sintese-e-referencias.md)** | O que deve permanecer depois da leitura? | Checklist, autoavaliação e fontes efetivamente usadas. |

## O caso que nos acompanhará

Uma organização quer um **assistente interno de documentos**. Pessoas de atendimento precisam perguntar “qual é o prazo para reembolso?” ou “que aprovação esta contratação exige?” e receber uma resposta útil. Os documentos mudam, têm níveis distintos de acesso e às vezes se contradizem. A primeira intuição é conectar um modelo e escrever um bom prompt. A pergunta arquitetural é mais exigente: **de onde virá a evidência, como a autorização será preservada e como saberemos que a resposta é aceitável?**

Ao longo do módulo, compararemos três direções: usar apenas o modelo; enviar documentos inteiros a cada pergunta; ou recuperar trechos pertinentes antes de gerar. Não construiremos ainda um RAG completo. O objetivo é aprender a enxergar responsabilidades, fronteiras e consequências antes de escolher tecnologias.

## Como estudar

Percorra as páginas na ordem. Conceitos precedem padrões porque nomes de soluções sem um modelo mental viram receitas. Ao encontrar uma afirmação arquitetural, pergunte: “qual requisito ou evidência justifica isto?” Ao encontrar uma camada, pergunte: “qual falha ela contém e qual nova dependência ela introduz?”. Use os blocos de resposta apenas depois de formular sua própria explicação.

O módulo não promete eliminar incerteza. Ele ensina a transformá-la em decisões explícitas, cenários verificáveis, testes e mecanismos de contenção. Essa mudança de postura é o fundamento do restante da disciplina.

**Próxima página:** [Conceitos fundamentais](conceitos.md).
