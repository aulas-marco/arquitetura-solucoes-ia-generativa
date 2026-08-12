# Síntese e referências

## Doze ideias essenciais

1. **O modelo não é o sistema.** Resultado e risco emergem da composição com software, dados, pessoas, políticas, fornecedores e operação.
2. **Probabilístico não significa sem controle.** Regras, contratos, autorização e validações delimitam geração e efeito.
3. **Nem toda chamada é uma decisão arquitetural.** Significância depende de estrutura, características prioritárias, dependências, responsabilidades e custo de mudança.
4. **A superfície comportamental é composta.** Modelo, parâmetros, prompt, contexto, fontes, ferramentas, políticas, estado, memória e implantação influenciam a saída.
5. **Geração, decisão, autorização e efeito são responsabilidades diferentes.** Um modelo pode propor sem receber autoridade ou credencial.
6. **Conhecimento, contexto, estado, memória, evidência e trace possuem ciclos de vida próprios.**
7. **Prompt participa do contrato; não é o contrato inteiro.** Entrada, saída, modelo, políticas, validação e falha também importam.
8. **Embedding é representação.** Recuperação ainda exige fontes, índices, metadados, filtros, ranking, autorização e avaliação.
9. **Teste, avaliação e verificação arquitetural respondem a perguntas distintas.** Fitness functions preservam características ao longo da evolução.
10. **Cada abordagem acrescenta responsabilidades.** RAG traz recuperação; ferramentas trazem efeitos; agentes trazem autonomia; fine-tuning traz ciclo de modelo adaptado.
11. **A alternativa mais complexa não é a mais madura.** A composição adequada é proporcional ao problema, risco e evidência.
12. **Mudança faz parte do sistema.** Alterar qualquer elemento da superfície comportamental pode exigir regressão, promoção controlada e retorno seguro.

## Checklist transversal

Antes de levar uma hipótese ao desenho conceitual, verifique:

- propósito, pessoas afetadas e efeitos fora de escopo estão explícitos;
- modelo, aplicação e sistema sociotécnico não foram confundidos;
- geração, decisão, autorização e efeito têm responsáveis;
- conhecimento, contexto, estado, memória, evidência e trace não foram fundidos;
- componentes determinísticos protegem regras e efeitos críticos;
- superfície comportamental e versões relevantes podem ser identificadas;
- finalidade, autorização, retenção e descarte acompanham os dados;
- produção, conhecimento, efeito e operação foram tratados como decisões independentes;
- alternativa convencional foi comparada à generativa;
- falhas têm contenção, degradação ou retorno seguro;
- teste de software, avaliação comportamental e verificação arquitetural foram diferenciados;
- hipótese, evidência existente, incógnita decisiva e próximo experimento estão registrados.

## Autoavaliação

1. Consigo explicar por que duas respostas diferentes podem ser aceitáveis e uma resposta estável pode estar errada?
2. Sei distinguir modelo, aplicação e sistema sociotécnico?
3. Consigo enumerar a superfície comportamental de uma execução?
4. Sei separar geração, decisão, autorização e efeito?
5. Consigo distinguir conhecimento, contexto, estado, memória, evidência e trace?
6. Sei explicar o que tokens, janela, prompt, temperatura e embedding permitem — e o que não garantem?
7. Consigo comparar produção, conhecimento, efeito e operação sem escolher tudo de uma vez?
8. Sei diferenciar teste de software, avaliação comportamental e fitness function?
9. Consigo localizar responsabilidades no mapa e explicar uma degradação segura?
10. Sei escrever uma ficha inicial com incógnita e experimento capaz de inverter uma direção?

Se mais de duas respostas forem “ainda não”, retome [Conceitos](conceitos.md), o [mapa de responsabilidades](padroes-e-decisoes.md#mapa-de-responsabilidades), o [exemplo Horizonte](exemplo-arquitetural.md) e os exercícios 8, 10 e 12.

## Conexão com os próximos módulos

- O [Módulo 2](../modulo-2-desenho-conceitual/index.md) transforma a ficha inicial em RAS, visões, táticas, riscos, evidências e ADRs.
- O [Módulo 3](../modulo-3-rag/index.md) detalha fontes, ingestão, recuperação, autorização, proveniência e fundamentação.
- O [Módulo 4](../modulo-4-agentes/index.md) detalha ferramentas, estado, memória, autonomia, efeitos e recuperação.
- O [Módulo 5](../modulo-5-confianca/index.md) detalha ameaças, guardrails, avaliação e aceitação de risco residual.
- O [Módulo 6](../modulo-6-operacao/index.md) detalha versões, fitness functions, observabilidade, rollout, rollback e plataformas.

## Referências citadas no módulo

- Richards, M. e Ford, N. (2020). [*Fundamentals of Software Architecture — An Engineering Approach*](https://www.oreilly.com/library/view/fundamentals-of-software-architecture/9781492043454/). Trade-offs, características arquiteturais e evolução.
- Vaswani, A. et al. (2017). [*Attention Is All You Need*](https://proceedings.neurips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html). Base técnica de arquiteturas Transformer.
- Brown, T. B. et al. (2020). [*Language Models are Few-Shot Learners*](https://proceedings.neurips.cc/paper_files/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html). Adaptação por instruções, contexto e exemplos.
- Bommasani, R. et al. (2021). [*On the Opportunities and Risks of Foundation Models*](https://arxiv.org/abs/2108.07258). Modelo fundacional como base de aplicações e riscos derivados.
- Sculley, D. et al. (2015). [*Hidden Technical Debt in Machine Learning Systems*](https://proceedings.neurips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html). Dependências de dados, configuração e processos.
- Lewis, P. et al. (2020). [*Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*](https://proceedings.neurips.cc/paper/2020/hash/6b493230-Abstract.html). Combinação de memória paramétrica e informação recuperada.
- National Institute of Standards and Technology (2023). [*Artificial Intelligence Risk Management Framework (AI RMF 1.0)*](https://doi.org/10.6028/NIST.AI.100-1). Gestão de riscos de sistemas de IA ao longo do ciclo de vida.

Continue pelo [Módulo 2](../modulo-2-desenho-conceitual/index.md) ou volte ao [mapa de aprendizagem](../comecar/mapa-de-aprendizagem.md).
