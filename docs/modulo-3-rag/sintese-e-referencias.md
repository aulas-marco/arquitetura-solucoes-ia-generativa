# Síntese e referências

## RAG é um sistema, não um banco vetorial

Antes de liberar uma solução, verifique:

- fontes têm dono, autoridade, classificação, vigência e SLO de atualização;
- aquisição processa inclusão, alteração, exclusão e reconciliação;
- extração e normalização preservam estrutura e tornam falhas visíveis;
- chunking foi comparado com perguntas reais e mantém localização e vizinhança;
- metadados de autorização vêm de autoridade confiável;
- embeddings, índices, extratores e corpus pertencem a um pacote versionado;
- busca lexical, vetorial, híbrida ou estruturada foi escolhida por evidência;
- transformação de consulta preserva entidades, negação e temporalidade;
- autorização limita o universo antes de conteúdo chegar a ranking, cache ou modelo;
- reranking demonstra ganho no orçamento de latência e recebe só candidatos permitidos;
- contexto remove duplicatas, preserva autoridade e separa evidência de instrução;
- cada afirmação material pode apontar para fonte, versão e trecho que a sustentam;
- falta, conflito, expiração e bloqueio produzem resposta parcial ou abstenção explícita;
- métricas distinguem conhecimento, recuperação, contexto, geração, sistema e produto;
- falhas têm detecção, contenção, recuperação e estado preservado;
- traces permitem reconstrução sem copiar dados sensíveis desnecessários;
- toda complexidade adicional possui hipótese, evidência e gatilho de remoção.

## Autoavaliação

1. Consigo desenhar os pipelines offline e online sem omitir exclusão e autorização?
2. Sei explicar quando lexical vence vetorial e quando híbrido compensa?
3. Consigo medir Recall@k, Precision@k e qualidade de citação separadamente?
4. Sei impedir que reranker, cache e abertura de fonte atravessem permissões?
5. Consigo distinguir “não existe”, “não encontrei” e “não está disponível para você”?
6. Sei escolher entre RAG básico, hierárquico, adaptativo, corretivo, multisource e estruturado?

Se duas respostas forem “ainda não”, retome [Conceitos](conceitos.md), [Padrões e decisões](padroes-e-decisoes.md) e os exercícios 8, 10 e 12.

## Fundamentação pedagógica

O trabalho original de [Lewis et al.](https://proceedings.neurips.cc/paper/2020/hash/6b493230-Abstract.html) introduz a combinação de memória paramétrica e recuperada. [Dense Passage Retrieval](https://aclanthology.org/2020.emnlp-main.550/) e [Sentence-BERT](https://aclanthology.org/D19-1410/) fundamentam recuperação densa e embeddings. [RAGAs](https://aclanthology.org/2024.eacl-demo.16/) oferece uma abordagem primária de avaliação de recuperação e geração. O perfil oficial [NIST AI RMF para GenAI](https://doi.org/10.6028/NIST.AI.600-1) e o [OWASP Top 10 para aplicações com LLM](https://genai.owasp.org/llm-top-10/) orientam risco e segurança.

Os capítulos locais *Requirements and Architecture for AI Pipelines* (`avila-ahmad-chapter-5-local`) e *Architecting a Generative AI System — A Case Study* (`avila-ahmad-chapter-7-local`) sustentam o raciocínio de pipeline e integração. Todas as fontes constam no [registro editorial](../referencia/fontes.yml) e na [Bibliografia consolidada](../referencia/bibliografia.md).

## Conexão com o próximo módulo

RAG recupera conhecimento; não concede autonomia. O [Módulo 4 — Agentes](../sobre/plano-da-disciplina.md#modulo-4) acrescentará escolha de ferramentas, estado e trajetórias. Evidência autorizada, contratos, orçamento, observabilidade e degradação segura continuarão válidos quando o sistema passar de responder a agir.

Volte ao [mapa de aprendizagem](../comecar/mapa-de-aprendizagem.md) ou avance para o [Módulo 4](../sobre/plano-da-disciplina.md#modulo-4).
