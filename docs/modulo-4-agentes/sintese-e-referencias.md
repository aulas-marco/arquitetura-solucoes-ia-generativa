# Síntese e referências

## Autonomia deve ser orçada e observável

Antes de liberar um sistema que age, verifique:

- chatbot, copiloto, workflow e agente estão diferenciados por controle e efeito;
- autonomia só existe onde a variabilidade do plano cria valor mensurável;
- cada ferramenta possui finalidade, efeito, esquemas, erros, identidade, política, idempotência, timeout, retry, auditoria, versão e compensação;
- o catálogo oferecido ao modelo contém somente capacidades necessárias;
- saídas estruturadas são validadas semanticamente antes da execução;
- credenciais permanecem fora do modelo e a autorização delegada é mínima e revalidada;
- estado autoritativo é separado de memória de trabalho, memória persistente e contexto;
- idempotência e precondições evitam duplicação e escrita concorrente;
- timeout de escrita leva à reconciliação antes de retry;
- circuit breaker não pode ser contornado pelo agente;
- compensações são idempotentes, autorizadas, observadas e reconhecem efeitos irreversíveis;
- níveis de autonomia são atribuídos por ação, risco e reversibilidade;
- aprovação prévia vincula objeto imutável; revisão posterior não substitui consentimento;
- orçamento limita etapas, tempo, custo, tokens, handoffs, tentativas e ações;
- prioridades de segurança, confiabilidade, auditabilidade, latência, custo e modificabilidade declaram tensões e responsáveis;
- fitness functions verificam autorização, idempotência, aprovação imutável, compensação e reconstrução do trace;
- fallback determinístico preserva identidade, estado e verdade sobre o resultado;
- agente único é o padrão inicial; múltiplos agentes exigem fronteira ou benefício medido;
- traces permitem reconstrução sem reter segredos e dados pessoais desnecessários;
- caminhos de sucesso, negação, repetição e compensação têm testes próprios.
- o arnês foi projetado como um todo, e cada componente tem dono: prompt de sistema, ferramentas, contexto, verificação, memória, sandbox e hooks;
- o catálogo passou pelo teste da ambiguidade: uma pessoa da equipe diz sem hesitar qual ferramenta cabe em cada situação;
- a redução do número de etapas foi considerada antes de aumentar a confiabilidade de cada uma;
- o nível de loop está declarado, e o que foi entregue à máquina em cada degrau tem controle correspondente no arnês;
- a condição de parada é objetiva, executável, versionada e conhecidamente capaz de reprovar;
- há teto de iterações e teto de custo independentes, com dono e comportamento definido no esgotamento;
- nenhum laço tem permissão de escrita sobre o artefato que define seu próprio critério de sucesso.

## Autoavaliação

1. Consigo localizar quem escolhe transições e quem executa efeitos?
2. Sei escrever um contrato que permita negar, deduplicar e compensar uma ferramenta?
3. Consigo explicar por que timeout e falha não são sinônimos?
4. Sei preservar identidade do usuário sem expor credenciais ao modelo?
5. Consigo classificar autonomia por ação e definir intervenção humana proporcional?
6. Sei defender agente único, múltiplos agentes ou workflow com métricas capazes de inverter a decisão?
7. Consigo atribuir responsabilidades entre planejador, executor, política, estado e aprovação, sem conceder autoridade ao modelo?
8. Sei nomear os componentes do arnês e dizer qual deles atacaria diante de um tipo específico de falha?
9. Consigo calcular o efeito do erro composto numa trajetória e usar o resultado para limitar o número de etapas?
10. Sei dizer se uma tarefa pode subir para o nível 2 de loop, e escrever o comando que decide seu término?

Se duas respostas forem “ainda não”, retome os [temas do módulo](index.md) e os exercícios de SDD em [Exercícios](exercicios.md).

## Fundamentação

[ReAct](https://openreview.net/forum?id=WE_vluYUL-X) é pesquisa primária sobre a combinação de raciocínio e ação. [Toolformer](https://proceedings.neurips.cc/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html) examina aprendizagem de uso de ferramentas. A [especificação do Model Context Protocol](https://modelcontextprotocol.io/specification/2025-11-25) documenta um protocolo aberto para integrar aplicações, contexto e ferramentas; interoperabilidade não substitui autorização e semântica corporativa.

O [perfil do NIST para IA generativa](https://doi.org/10.6028/NIST.AI.600-1), o [perfil SSDF do NIST](https://doi.org/10.6028/NIST.SP.800-218A) e o [OWASP Top 10 para aplicações com LLM](https://genai.owasp.org/llm-top-10/) orientam risco, desenvolvimento seguro e ameaças. As [convenções de OpenTelemetry para IA generativa](https://github.com/open-telemetry/semantic-conventions-genai) apoiam vocabulário de observabilidade. O capítulo local *Architecting a Generative AI System — A Case Study* (`avila-ahmad-chapter-7-local`) fornece o material do livro sobre integração e estudo de caso.

Sobre arnês e loops, o material do módulo se apoia em documentação de fornecedor e em relatos de engenharia, que são as fontes primárias disponíveis para uma prática que ainda não tem literatura revisada por pares. A Anthropic documenta o ciclo de quatro tempos em [Building agents with the Claude Agent SDK](https://claude.com/blog/building-agents-with-the-claude-agent-sdk), a escada de níveis em [Getting started with loops](https://claude.com/blog/getting-started-with-loops), o erro composto e a distinção entre workflow e agente em [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents), a curadoria de contexto em [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), o desenho de catálogo em [Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents) e [Code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp), a separação entre guiar e impor em [Steering Claude Code](https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more) e o laço com teto de iterações no [plugin Ralph Wiggum](https://github.com/anthropics/claude-code/blob/main/plugins/ralph-wiggum/README.md). O termo arnês vem de [The Anatomy of an Agent Harness](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness), de Vivek Trivedy, com a leitura complementar de [Agent Harness Engineering](https://addyosmani.com/blog/agent-harness-engineering/), de Addy Osmani; o laço em sua forma mínima vem de [Ralph Wiggum as a "software engineer"](https://ghuntley.com/ralph/), de Geoffrey Huntley. Os dois relatos de campo usados no texto são a [remoção de 80% das ferramentas](https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools) publicada pela Vercel e a estimativa de ganho por verificação de [Boris Cherny](https://x.com/bcherny/status/2007179861115511237). Trate números de benchmark e ganhos relatados como indicação de direção: eles vêm de contextos que você não controla e não foram replicados de forma independente.

Todas as fontes estão no [registro editorial](../referencia/fontes.yml) e na [Bibliografia consolidada](../referencia/bibliografia.md).

## Conexão com o próximo módulo

O agente que constrói software é o caso de autonomia com efeito mais durável, e ganha módulo próprio: o [Módulo 5 — Desenvolvimento guiado por especificação](../modulo-5-especificacao/index.md) percorre constitution, spec, plano, tarefas e portões humanos com o mesmo vocabulário de contrato, estado e autoridade construído aqui.

Controles de ferramenta reduzem risco, mas não demonstram que o sistema é seguro, justo ou adequado para todas as populações. O [Módulo 6 — Confiança, segurança, avaliação e governança](../sobre/plano-da-disciplina.md#modulo-6) aprofundará ameaças, privacidade, guardrails, avaliação e evidências de governança. A matriz de autonomia e o contrato de ferramenta tornam-se entradas: cada nível precisa de casos adversariais, critérios de aceitação e monitoramento proporcional ao efeito.

Volte ao [mapa de aprendizagem](../comecar/mapa-de-aprendizagem.md) ou avance para o [Módulo 6](../sobre/plano-da-disciplina.md#modulo-6).
