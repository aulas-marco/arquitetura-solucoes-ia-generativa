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
- fallback determinístico preserva identidade, estado e verdade sobre o resultado;
- agente único é o padrão inicial; múltiplos agentes exigem fronteira ou benefício medido;
- traces permitem reconstrução sem reter segredos e dados pessoais desnecessários;
- caminhos de sucesso, negação, repetição e compensação têm testes próprios.

## Autoavaliação

1. Consigo localizar quem escolhe transições e quem executa efeitos?
2. Sei escrever um contrato que permita negar, deduplicar e compensar uma ferramenta?
3. Consigo explicar por que timeout e falha não são sinônimos?
4. Sei preservar identidade do usuário sem expor credenciais ao modelo?
5. Consigo classificar autonomia por ação e definir intervenção humana proporcional?
6. Sei defender agente único, múltiplos agentes ou workflow com métricas capazes de inverter a decisão?

Se duas respostas forem “ainda não”, retome [Conceitos](conceitos.md), [Padrões e decisões](padroes-e-decisoes.md) e os exercícios 8, 10 e 12.

## Fundamentação

[ReAct](https://openreview.net/forum?id=WE_vluYUL-X) é pesquisa primária sobre a combinação de raciocínio e ação. [Toolformer](https://proceedings.neurips.cc/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html) examina aprendizagem de uso de ferramentas. A [especificação do Model Context Protocol](https://modelcontextprotocol.io/specification/2025-11-25) documenta um protocolo aberto para integrar aplicações, contexto e ferramentas; interoperabilidade não substitui autorização e semântica corporativa.

O [perfil do NIST para IA generativa](https://doi.org/10.6028/NIST.AI.600-1), o [perfil SSDF do NIST](https://doi.org/10.6028/NIST.SP.800-218A) e o [OWASP Top 10 para aplicações com LLM](https://genai.owasp.org/llm-top-10/) orientam risco, desenvolvimento seguro e ameaças. As [convenções de OpenTelemetry para IA generativa](https://github.com/open-telemetry/semantic-conventions-genai) apoiam vocabulário de observabilidade. O capítulo local *Architecting a Generative AI System — A Case Study* (`avila-ahmad-chapter-7-local`) fornece o material do livro sobre integração e estudo de caso. Todas as fontes estão no [registro editorial](../referencia/fontes.yml) e na [Bibliografia consolidada](../referencia/bibliografia.md).

## Materiais adicionais sobre SDD

O [GitHub Spec Kit](https://github.com/github/spec-kit) é o fio operacional desta disciplina: constitution, specification, plan, tasks, implementação e verificação deixam decisões e critérios de aceite visíveis. As [skills de engenharia de Matt Pocock](https://github.com/mattpocock/skills/tree/main/docs/engineering) oferecem uma variação disciplinada, com *vertical slices*, testes nas interfaces públicas e revisão separada por aderência à spec e padrões do repositório.

[Kiro Specs](https://kiro.dev/docs/specs/), [BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) e [Tessl](https://tessl.io) mostram escolhas diferentes de ambiente, papéis e persistência da especificação. O [OpenAI Model Spec](https://github.com/openai/model_spec) ajuda a discutir regras verificáveis, enquanto a palestra [The New Code](https://www.youtube.com/watch?v=8rABwKRsec4) provoca a tratar especificação como competência de engenharia. São comparações: não substituem o fluxo principal do Spec Kit.

## Conexão com o próximo módulo

Controles de ferramenta reduzem risco, mas não demonstram que o sistema é seguro, justo ou adequado para todas as populações. O [Módulo 5 — Confiança, segurança, avaliação e governança](../sobre/plano-da-disciplina.md#modulo-5) aprofundará ameaças, privacidade, guardrails, avaliação e evidências de governança. A matriz de autonomia e o contrato de ferramenta tornam-se entradas: cada nível precisa de casos adversariais, critérios de aceitação e monitoramento proporcional ao efeito.

Volte ao [mapa de aprendizagem](../comecar/mapa-de-aprendizagem.md) ou avance para o [Módulo 5](../sobre/plano-da-disciplina.md#modulo-5).
