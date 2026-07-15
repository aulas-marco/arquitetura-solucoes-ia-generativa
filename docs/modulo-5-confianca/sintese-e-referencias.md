# Síntese e referências

## O argumento do módulo

Confiabilidade não reside no modelo isolado. Ela emerge, de forma imperfeita e contextual, da composição entre finalidade, dados, recuperação, geração, ferramentas, políticas, pessoas, fornecedores e operação. Demonstrá-la exige ligar cenários de risco a controles e evidências, declarar limitações e obter uma decisão autorizada sobre o risco residual.

## Síntese dos princípios

- **Confiança é suficiente para um contexto, nunca universal.** Uma configuração aprovada para explicar política pública não herda autorização para consultar ou alterar dados pessoais.
- **Responsabilidade compartilhada exige responsáveis distintos.** Um fornecedor não assume a decisão de uso nem os controles locais.
- **Autorizado não significa confiável.** Usuário autorizado, documento permitido e ferramenta disponível ainda podem estar errados, comprometidos ou fora de finalidade.
- **Guardrails funcionam em profundidade.** As seis camadas cobrem falhas diferentes; independência e modo seguro de falha importam mais que quantidade.
- **Privacidade é ciclo de vida.** Minimização, segregação, retenção e descarte alcançam contexto, trace, índice, avaliação, memória, cache, backup e fornecedor.
- **Qualidade é multidimensional.** Factualidade, relevância, fundamentação, segurança, utilidade, latência e custo precisam de critérios próprios e análise por fatias.
- **Avaliação não é garantia.** Conjuntos e avaliadores amostram comportamentos sob hipóteses. Casos adversariais, canary, monitoramento e resposta cobrem parte do que a avaliação offline não prevê.
- **Governança precisa ser executável.** Catálogo, pacote de versões, portões, exceções, auditoria e rollback conectam decisão a mudança real.

## O que vem dos referenciais e o que é recomendação do curso

| Fonte | Natureza e contribuição | Limite de interpretação | Recomendação adotada neste curso |
|---|---|---|---|
| NIST AI RMF 1.0 | framework voluntário que organiza gestão de risco em Govern, Map, Measure e Manage | não certifica uma solução nem define limiar local | manter registro contextual de riscos, evidências, proprietários e revisão |
| NIST Generative AI Profile | perfil complementar com riscos e ações para IA generativa | ações precisam ser selecionadas e adaptadas; não formam checklist de garantia | relacionar falhas de RAG e agentes a controles, avaliação e resposta |
| NIST SP 800-218A | perfil de práticas de desenvolvimento seguro para IA generativa e modelos de uso dual | desenvolvimento seguro não garante comportamento seguro em todo uso | inventariar cadeia, versionar pacote e bloquear mudança sem regressão proporcional |
| OWASP Top 10 for LLM Applications | orientação comunitária para classes relevantes de vulnerabilidade | “cobrir o Top 10” não prova segurança nem conformidade jurídica | transformar cada classe aplicável em cenário específico do fluxo e teste adversarial |
| ISO/IEC 42001:2023 | requisitos de sistema de gestão de IA para organizações que adotam o padrão ou buscam conformidade | não prescreve arquitetura única nem atesta cada saída do sistema | usar catálogo, papéis e portões como mecanismos arquiteturais, sem alegar que são texto literal da norma |
| pesquisas de avaliação | métodos e resultados originais sobre avaliação holística, RAG e avaliadores baseados em modelos | desempenho de pesquisa não valida automaticamente o domínio de RH | combinar instrumentos, calibrar com humanos e reportar limitações e fatias |

Essa distinção evita dois erros. O primeiro é transformar orientação voluntária em obrigação jurídica universal. O segundo é citar um framework enquanto controles essenciais existem apenas no slide. Requisitos normativos aplicáveis devem ser interpretados por profissionais competentes e rastreados à sua fonte; recomendações arquiteturais precisam de justificativa e evidência próprias.

## Fontes oficiais e primárias

### Risco, governança e segurança

- [Artificial Intelligence Risk Management Framework (AI RMF 1.0), NIST AI 100-1](https://doi.org/10.6028/NIST.AI.100-1). Framework institucional de gestão de riscos.
- [Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile, NIST AI 600-1](https://doi.org/10.6028/NIST.AI.600-1). Perfil oficial para IA generativa.
- [Secure Software Development Practices for Generative AI and Dual-Use Foundation Models, NIST SP 800-218A](https://doi.org/10.6028/NIST.SP.800-218A). Perfil de desenvolvimento seguro.
- [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/). Classes de vulnerabilidade do projeto OWASP GenAI Security.
- [ISO/IEC 42001:2023 — Artificial intelligence management system](https://www.iso.org/standard/42001). Página canônica do padrão internacional de sistema de gestão de IA.

### Avaliação e arquitetura generativa

- [Holistic Evaluation of Language Models](https://arxiv.org/abs/2211.09110), de Percy Liang et al. Pesquisa original que explicita cenários, métricas e transparência na avaliação de modelos.
- [RAGAs: Automated Evaluation of Retrieval Augmented Generation](https://aclanthology.org/2024.eacl-demo.16/), de Shahul Es et al. Artigo original sobre avaliação automatizada de componentes de RAG.
- [G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment](https://aclanthology.org/2023.emnlp-main.153/), de Yang Liu et al. Pesquisa original sobre uso de modelo na avaliação de geração.
- [On the Opportunities and Risks of Foundation Models](https://arxiv.org/abs/2108.07258), de Rishi Bommasani et al. Relatório institucional sobre capacidades, impactos e riscos sistêmicos de foundation models.
- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://proceedings.neurips.cc/paper/2020/hash/6b493230-Abstract.html), de Patrick Lewis et al. Artigo original do desenho de RAG retomado na avaliação por componente.

## Checklist de saída

Antes de chamar uma solução de “pronta”, confirme contexto e usos proibidos; dados e ferramentas mínimos; ameaças por fronteira; testes negativos; escalonamento; casos adversariais; resultados por dimensão e fatia; limites; versões; responsáveis; risco residual; canary, rollback e resposta a incidente.

Sem evidência para item crítico, reduza escopo, produza-a ou não libere. No [Módulo 6](../sobre/plano-da-disciplina.md#modulo-6), a arquitetura vira prática operacional: LLMOps, observabilidade, SLOs, mudanças e plataforma.
