# Módulo 3 — RAG e sistemas de conhecimento

> **Pergunta-guia:** Como conectar um modelo a conhecimento verificável e atualizável?

Um modelo de linguagem pode escrever com fluência sobre temas que apareceram em seu treinamento, mas não funciona como arquivo corporativo. Seus parâmetros não oferecem consulta confiável à versão vigente de uma política, não preservam por si mesmos a permissão de cada leitor e não permitem reconstruir qual cláusula sustentou uma afirmação. Quando uma resposta depende de conhecimento controlado, a arquitetura precisa criar um caminho explícito entre pergunta, evidência autorizada e geração.

**Retrieval-Augmented Generation (RAG)** é uma família de arquiteturas que recupera informação externa no momento da consulta e a oferece ao modelo como contexto. Essa definição parece simples, porém a solução completa tem dois fluxos, múltiplas fronteiras e critérios próprios de qualidade. O fluxo de ingestão transforma fontes em unidades pesquisáveis, versionadas e autorizáveis. O fluxo de consulta interpreta a necessidade, recupera candidatos, aplica políticas, organiza evidências, gera e valida uma resposta. Se qualquer elo falhar, a resposta pode ser fluente e ainda assim estar errada, desatualizada ou proibida.

Por isso, este módulo adota uma tese: **RAG é um sistema de conhecimento, não um tutorial de banco vetorial**. Um índice vetorial pode participar da recuperação, mas não resolve aquisição, extração, atualização, proveniência, busca lexical, autorização, reranking, composição de contexto, citação, recusa e avaliação ponta a ponta.

## Antes de começar

Retomaremos o [Módulo 2 — Desenho conceitual](../modulo-2-desenho-conceitual/index.md): oportunidade, CONOPS, requisitos arquiteturalmente significativos, critérios probabilísticos e rastreabilidade. Também usaremos o [Glossário](../referencia/glossario.md), o [Catálogo de padrões](../referencia/catalogo-de-padroes.md) e os cenários de [atributos de qualidade](../referencia/atributos-de-qualidade.md).

Não é necessário conhecer um produto de busca, um provedor de modelos ou uma biblioteca específica. Falaremos em repositório de origem, processador, índice lexical, índice vetorial, motor de políticas, reranker, montador de contexto e serviço de inferência. Esses papéis podem ser implementados de várias maneiras sem alterar as decisões essenciais.

**Tempo estimado de leitura:** 85–115 minutos, sem contar o estudo de caso e os exercícios de projeto.

## Objetivos de aprendizagem

Ao concluir o módulo, você deverá ser capaz de:

1. **Compreender** a diferença entre conhecimento paramétrico, fonte de verdade, evidência recuperada e resposta gerada.
2. **Aplicar** decisões de aquisição, extração, normalização, segmentação, metadados, embeddings, indexação, atualização e proveniência.
3. **Analisar** recuperação lexical, vetorial e híbrida; filtros de autorização; reranking; montagem de contexto; citação e evidência insuficiente.
4. **Avaliar** padrões básico, híbrido, hierárquico, adaptativo, corretivo, multisource e orientado a dados estruturados.
5. **Criar** uma arquitetura RAG completa, com fluxos offline e online, fronteiras de confiança, métricas, recuperação e degradação segura.

## Roteiro do módulo

| Página | Questão central | Resultado esperado |
|---|---|---|
| **1. Abertura** | O que torna conhecimento verificável e atualizável? | Um contrato de aprendizagem centrado no sistema. |
| **2. [Conceitos](conceitos.md)** | Como separar conhecimento, recuperação e geração? | Vocabulário e os dois pipelines completos. |
| **3. [Padrões e decisões](padroes-e-decisoes.md)** | Qual mecanismo responde a cada necessidade? | Decisões de recuperação, autorização, evidência e variantes de RAG. |
| **4. [Exemplo arquitetural](exemplo-arquitetural.md)** | Como os dois fluxos cooperam em execução? | Diagramas, sequência, responsabilidades, falhas e métricas. |
| **5. [Estudo de caso](estudo-de-caso.md)** | Como atender políticas e contratos com permissões individuais? | Uma decisão incremental com citações, atualização rápida e abstenção. |
| **6. [Exercícios](exercicios.md)** | Consigo medir, diagnosticar e projetar RAG? | Evidências nos seis níveis da Taxonomia de Bloom. |
| **7. [Síntese e referências](sintese-e-referencias.md)** | O que precisa existir além do índice? | Checklist sistêmico, autoavaliação e fontes. |

## A unidade de raciocínio: pergunta → evidência → resposta

Para cada afirmação importante, a arquitetura deve conseguir responder:

1. qual identidade e finalidade iniciaram a consulta;
2. quais fontes e versões estavam elegíveis naquele instante;
3. como candidatos foram recuperados, filtrados e ordenados;
4. quais trechos entraram no contexto e sob quais identificadores;
5. qual configuração de prompt e modelo produziu a saída;
6. quais verificações aprovaram, limitaram ou recusaram a resposta.

Essa cadeia não garante verdade universal. Ela torna o comportamento inspecionável e permite medir onde ocorreu uma falha. O trabalho original de [Lewis et al. sobre RAG](https://proceedings.neurips.cc/paper/2020/hash/6b493230-Abstract.html) combina memória paramétrica e memória não paramétrica recuperada. Em arquitetura corporativa, ampliamos a ideia para incluir ciclo de vida do conhecimento, políticas de acesso, operação e responsabilização.

## Uma regra para o restante do módulo

Não otimize geração antes de localizar a causa. Uma resposta ruim pode decorrer de fonte ausente, extração incorreta, chunk sem contexto, metadado inválido, consulta mal transformada, filtro excessivo, ranking fraco, contexto conflitante, instrução inadequada ou geração sem suporte. Avaliar apenas a resposta final esconde o componente que precisa mudar.

Primeiro construiremos o vocabulário e os dois fluxos. Depois compararemos decisões e padrões. Só então aplicaremos o método ao assistente corporativo de políticas e contratos. Essa ordem evita transformar uma escolha particular de índice em uma regra para todos os sistemas.

**Próxima página:** [Conhecimento externo e os dois pipelines](conceitos.md).
