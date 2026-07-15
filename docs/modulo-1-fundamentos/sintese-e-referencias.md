# Síntese e referências

## Dez ideias essenciais

1. **O modelo não é o sistema.** Qualidade e risco emergem da composição com dados, software, pessoas, políticas e operação.
2. **Probabilístico não significa sem controle.** Regras, contratos, autorização e validações determinísticas delimitam a geração.
3. **Avaliar comportamento complementa testar código.** Conjuntos representativos e critérios mensuráveis cobrem a variabilidade que asserções exatas não capturam.
4. **Contexto é uma decisão arquitetural.** Seleção, ordem, autorização, proveniência e orçamento importam tanto quanto a capacidade da janela.
5. **Conhecimento paramétrico tem limites.** Ele não garante atualização sob demanda, cobertura nem fonte granular.
6. **Fluência não é factualidade.** Alucinação precisa ser contida com escopo, evidência, validação e comunicação de limites.
7. **Cada abordagem acrescenta responsabilidades.** RAG traz recuperação; ferramentas trazem efeitos; agentes trazem autonomia; fine-tuning traz ciclo de modelo adaptado.
8. **A solução mais complexa não é a mais madura.** Padrões devem responder a cenários e evidências, não a tendências.
9. **Capacidades transversais atravessam o fluxo.** Segurança, governança, avaliação e observabilidade não são uma caixa no fim do diagrama.
10. **Decisões são hipóteses revisáveis.** Uma ADR registra contexto, consequências, evidências e gatilhos, não uma certeza permanente.

## Checklist do arquiteto

Antes de aprovar um desenho inicial, verifique:

- o propósito, usuários afetados e decisões fora de escopo estão explícitos;
- modelo, aplicação e sistema sociotécnico não foram confundidos;
- componentes probabilísticos estão separados de regras e efeitos críticos;
- fontes de contexto, autorização, retenção e proveniência estão identificadas;
- modelo e forma de hospedagem foram tratados como dimensões de decisão;
- caminho crítico, orçamento de tokens, latência e custo podem ser medidos;
- falhas de modelo, conhecimento e integrações possuem degradação segura;
- saídas e chamadas de ferramentas passam por contratos proporcionais ao risco;
- versões de modelo, prompt, dados, políticas e avaliações podem ser correlacionadas;
- a alternativa escolhida possui evidência, critério de aceitação e gatilho de revisão.

## Autoavaliação

Responda sem consultar o texto e marque onde precisa voltar:

1. Consigo explicar a uma pessoa não técnica por que uma resposta variável não é necessariamente um defeito?
2. Consigo dar um exemplo em que o modelo é adequado para interpretar, mas inadequado para decidir?
3. Sei distinguir treinamento, fine-tuning e inferência e suas consequências operacionais?
4. Consigo explicar o que tokens e janela de contexto limitam — e o que não garantem?
5. Sei comparar contexto fornecido e RAG sem assumir que um sempre vence?
6. Consigo apontar o novo risco criado quando um modelo recebe uma ferramenta?
7. Sei percorrer as oito camadas e localizar autorização, evidência, falha e telemetria?
8. Consigo escrever uma ADR preliminar que declare o que ainda não sabemos?

Se você respondeu “ainda não” a mais de duas, retome [Conceitos](conceitos.md) e [Padrões e decisões](padroes-e-decisoes.md), depois refaça os itens 8 a 10 dos [Exercícios](exercicios.md).

## Conexão com o próximo módulo

Este módulo ensinou a **ler** uma solução. O [Módulo 2 — Desenho conceitual e decisões arquiteturais](../sobre/plano-da-disciplina.md#modulo-2) ensinará a **escolher**: transformar oportunidade em requisitos arquiteturalmente significativos, cenários de qualidade, alternativas e experimentos. A pergunta muda de “que componentes existem?” para “que decisão atende este contexto e como podemos demonstrá-la?”.

## Referências citadas no módulo

Somente as fontes abaixo foram usadas para sustentar afirmações deste módulo. O registro editorial completo está na [Bibliografia consolidada](../referencia/bibliografia.md).

- Vaswani, A. et al. (2017). [*Attention Is All You Need*](https://proceedings.neurips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html). Introdução da arquitetura Transformer.
- Brown, T. B. et al. (2020). [*Language Models are Few-Shot Learners*](https://proceedings.neurips.cc/paper_files/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html). Evidência primária de adaptação de modelos de linguagem por contexto e exemplos.
- Bommasani, R. et al. (2021). [*On the Opportunities and Risks of Foundation Models*](https://arxiv.org/abs/2108.07258). Formulação e análise do paradigma de modelos fundacionais.
- Sculley, D. et al. (2015). [*Hidden Technical Debt in Machine Learning Systems*](https://proceedings.neurips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html). Dependências e dívida técnica além do código em sistemas de aprendizado de máquina.
- Lewis, P. et al. (2020). [*Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*](https://proceedings.neurips.cc/paper/2020/hash/6b493230-Abstract.html). Trabalho original de geração aumentada por recuperação.
- National Institute of Standards and Technology (2023). [*Artificial Intelligence Risk Management Framework (AI RMF 1.0)*](https://doi.org/10.6028/NIST.AI.100-1). Estrutura institucional para gestão de riscos de sistemas de IA ao longo do ciclo de vida.

Continue pelo [Módulo 2](../sobre/plano-da-disciplina.md#modulo-2) ou volte ao [mapa de aprendizagem](../comecar/mapa-de-aprendizagem.md).
