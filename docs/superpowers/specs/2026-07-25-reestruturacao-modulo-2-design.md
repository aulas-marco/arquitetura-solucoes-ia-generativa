# Reestruturação pedagógica do Módulo 2 — desenho

**Data:** 2026-07-25
**Status:** aprovado para implementação e ampliado após revisão arquitetural

## Objetivo

Transformar o Módulo 2 na fundação de decisão do curso: partir de uma oportunidade e produzir um dossiê conceitual rastreável antes de escolher padrões, modelos ou fornecedores.

## Princípios de desenho

1. O fio pedagógico é: oportunidade → hipótese de valor → atividades e responsabilidades → CONOPS e fronteiras → RAS → alternativas → evidência e ADR.
2. Banco Lume é o caso condutor; Cooperativa Aurora é explicitamente um caso de transferência, sem ambiguidade.
3. RAG, fine-tuning, workflows, agentes, gateways, multimodelo e hospedagem aparecem como famílias de decisão com capacidade, responsabilidade e evidência mínima; o detalhamento pertence aos módulos 3–6.
4. O dossiê conceitual é construído progressivamente em conceitos, decisões, exemplo, caso, oficina, exercícios e síntese.
5. A linguagem privilegia situações, responsabilidades e decisões observáveis; elimina metáforas e rótulos de padrão sem função pedagógica.
6. A taxonomia separa entradas da análise, descrição arquitetural, análise de trade-offs, registros de decisão e evidências.
7. Ponto de vista define as convenções de representação; vista representa o sistema segundo essas convenções; modelos compõem vistas; ADR registra uma decisão e cenário de qualidade especifica um requisito.
8. As vistas mínimas cobrem contexto, responsabilidades, interação, informação e implantação. Regras de correspondência tornam contradições entre elas verificáveis.
9. RAS são realizados por táticas. Mecanismos concretizam táticas; padrões e estilos organizam estruturas recorrentes; ADRs preservam o racional da escolha.
10. A análise usa uma árvore de utilidade reduzida para registrar prioridade, sensibilidade, trade-off, risco e evidência sem transformar o módulo em uma apresentação completa do ATAM.

## Escopo

- Reescrever `index.md`, `conceitos.md`, `padroes-e-decisoes.md`, `exemplo-arquitetural.md`, `estudo-de-caso.md`, `oficina-de-ferramentas.md`, `exercicios.md` e `sintese-e-referencias.md` do Módulo 2.
- Preservar fontes, imagem existente, exercícios em seis níveis de Bloom e independência de fornecedor.
- Não antecipar a implementação detalhada de RAG, agentes, confiança ou LLMOps.
- Declarar “dossiê conceitual” como convenção didática do curso, não como termo normativo.
- Fazer exemplo, caso, oficina e exercícios produzirem ou verificarem as mesmas correspondências ensinadas em conceitos e padrões.

## Verificação

Executar validação de conteúdo, suíte Python e build estrito do MkDocs.
