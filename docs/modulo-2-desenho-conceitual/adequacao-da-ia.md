# Quando usar IA generativa

Antes de desenhar, decidir se a capacidade generativa cabe no problema, e reconhecer os casos em que a resposta correta é recusar.

## A IA como componente de um sistema maior

Um modelo de linguagem participa de um sistema que também contém dados, integrações, controles e pessoas. O desenho conceitual deve prever como essa capacidade se conecta a:

- **Conhecimento:** como os dados corporativos serão acessados de forma segura.
- **Integrações:** como as APIs existentes servirão de contexto ou ferramentas para a IA.
- **Controles:** quais são os limites de autonomia e segurança impostos ao sistema.

## Critérios de adequação da IA generativa

IA generativa costuma ser candidata quando a tarefa exige interpretar linguagem ou conteúdo não estruturado, sintetizar múltiplas evidências, produzir uma representação adaptada a um contexto ou lidar com variedade que tornaria regras explícitas frágeis. A candidatura fica mais forte quando uma saída aproximada pode ser avaliada, corrigida ou contida antes de produzir dano.

Use cinco perguntas:

1. **Variabilidade útil:** há muitas formas aceitáveis de saída, ou existe uma única resposta calculável?
2. **Dados e contexto:** existem exemplos, evidências e permissões suficientes para orientar e avaliar o comportamento?
3. **Tolerância ao erro:** uma saída imperfeita pode ser detectada e revisada antes do efeito?
4. **Critério de qualidade:** especialistas conseguem julgar casos representativos com concordância aceitável?
5. **Vantagem comparativa:** a capacidade generativa supera uma alternativa convencional em valor total, não só em demonstração?

A resposta “sim” não autoriza automação. Ela apenas justifica um experimento controlado. Modelos fundacionais apresentam capacidades amplas, mas também riscos dependentes de composição e contexto, como discute o relatório primário [On the Opportunities and Risks of Foundation Models](https://arxiv.org/abs/2108.07258). A unidade de decisão permanece o sistema, não o modelo isolado.

## Quando rejeitar IA generativa

Rejeite GenAI quando:

- a saída correta deriva de regra estável, cálculo ou consulta estruturada;
- qualquer variação é defeito e não existe contenção antes do efeito;
- não há dados legalmente utilizáveis ou exemplos representativos para avaliação;
- o requisito exige explicação causal ou garantia formal que a geração não fornece;
- latência, custo, residência, retenção ou conectividade tornam a solução inviável;
- a tarefa automatizada remove uma responsabilidade humana irrenunciável;
- uma busca, formulário, regra ou melhoria de processo produz valor equivalente com menos risco.

Se política, valor, prazo e categoria determinam exatamente um reembolso, regras devem decidir. Um modelo pode explicar ou extrair campos, mantendo decisão e efeito determinísticos.
