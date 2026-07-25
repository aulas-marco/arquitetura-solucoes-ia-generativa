# Síntese e referências

O produto do módulo é um dossiê conceitual revisável — convenção didática deste curso — que mantém entradas, vistas, análise, decisões e evidências ligadas antes da implementação detalhada.

## Doze ideias essenciais

1. **Oportunidade vem antes da solução.** Um problema observável e um resultado desejado preservam alternativas que a frase “usar IA” elimina.
2. **Valor e capacidade são hipóteses diferentes.** Qualidade do modelo pode ser necessária sem produzir melhoria no sistema sociotécnico.
3. **GenAI também pode ser rejeitada.** Regra, cálculo, consulta, template ou mudança de processo vencem quando entregam valor com menos risco e variabilidade.
4. **CONOPS torna o uso concreto.** Atores, informação, efeitos, modos, exceções e evidências revelam responsabilidades que um diagrama de chat esconde.
5. **Revisão humana precisa ser projetada.** Competência, tempo, autoridade, evidência e possibilidade de discordar diferenciam controle de aprovação ritual.
6. **Objetivos têm camadas.** Negócio, produto, dados e IA precisam se conectar sem que uma métrica intermediária substitua o resultado.
7. **Probabilístico não significa imensurável.** População, amostra, critérios de avaliação, limiar, incerteza, falha intolerável e ação produzem aceitação honesta.
8. **Vista, cenário e ADR têm funções distintas.** Vistas representam a arquitetura; cenários especificam respostas de qualidade; ADRs preservam decisões e racional.
9. **Informação e implantação fazem parte do desenho.** Ciclo de vida, região, identidade, rede, retenção e provedor alteram privacidade, operação e risco.
10. **Táticas realizam atributos de qualidade.** Mecanismos as concretizam; padrões e estilos organizam estruturas; nenhum desses elementos substitui a análise.
11. **Sensibilidades e trade-offs revelam risco.** Uma escolha deve registrar características beneficiadas, prejudicadas e evidência necessária.
12. **Rastreabilidade e proveniência funcionam nos dois sentidos.** Todo mecanismo deve apontar para um RAS e para elementos das vistas; toda prioridade deve chegar a uma evidência cuja origem, autoridade, versão, transformação e uso possam ser explicados.

## Checklist de desenho conceitual

Antes de aprovar o início da construção, verifique:

- problema, população, baseline, resultado e contramétricas estão explícitos;
- hipótese de valor não foi confundida com benchmark ou demonstração de modelo;
- critérios de adequação e rejeição de GenAI foram aplicados por atividade;
- stakeholders, impactos, fronteiras e fora de escopo estão registrados;
- CONOPS cobre modos normal, degradado, bloqueado, manutenção e incidente conforme o risco;
- responsabilidades humanas usam verbos e incluem autoridade para discordar;
- objetivos de negócio, produto, dados e IA não se contradizem;
- características prioritárias declaram tensão aceita, medida e responsável;
- requisitos arquiteturalmente significativos têm origem, prioridade, cenário e método de verificação;
- pontos de vista declaram preocupação, público, convenção e informação excluída;
- vistas de contexto, responsabilidades, interação, informação e implantação cobrem o sistema;
- correspondências entre participantes, passos, dados, alocações, fronteiras e controles foram verificadas;
- restrições confirmadas estão separadas de preferências e pressupostos;
- critérios probabilísticos cobrem segmentos críticos e falhas intoleráveis;
- proveniência registra origem, autorização, versão, transformação e uso de evidências materiais;
- alternativas convencionais foram comparadas antes de opções generativas mais complexas;
- cada RAS chega a táticas, mecanismos, elementos das vistas e evidência;
- tática, mecanismo, padrão, estilo e ADR não são usados como sinônimos;
- composições registram sensibilidades, trade-offs e riscos residuais;
- vistas e diagramas possuem equivalentes textuais;
- falhas especificam detecção, contenção, recuperação e estado preservado;
- ADRs registram evidências, risco residual e gatilhos mensuráveis;
- existe experimento barato que pode refutar a hipótese de maior risco.

## Autoavaliação

Sem consultar as páginas, responda:

1. Consigo reformular “queremos um agente” como oportunidade sem pressupor solução?
2. Sei dar um exemplo de capacidade que funciona, mas não produz valor no processo?
3. Consigo escrever um CONOPS que inclua modo degradado e efeito proibido?
4. Sei distinguir requisito significativo, restrição, preferência e pressuposto?
5. Consigo transformar “a resposta deve ser boa” em critério probabilístico verificável?
6. Sei explicar por que prompt, RAG e fine-tuning respondem a problemas diferentes?
7. Consigo justificar workflow ou agente pela variabilidade útil do plano?
8. Sei comparar modelo hospedado e autogerido pelo custo total e risco residual?
9. Consigo localizar a responsabilidade humana antes de qualquer efeito crítico?
10. Sei distinguir preocupação, ponto de vista, vista, modelo, cenário e ADR?
11. Consigo verificar correspondências entre interação, responsabilidades, informação e implantação?
12. Sei percorrer objetivo → RAS → tática → mecanismo → vista → evidência e voltar?

Se mais de duas respostas forem “ainda não”, retome [Conceitos](conceitos.md), reconstrua a análise em [Padrões e decisões](padroes-e-decisoes.md) e refaça os exercícios 8, 10 e 12.

## Fundamentação pedagógica

A sequência dialoga com três capítulos locais de Avila e Ahmad: *The Case for Architecture* (`avila-ahmad-chapter-2-local`) trata consequências e risco; *Software Engineering and Architecture* (`avila-ahmad-chapter-3-local`) liga intenção, estrutura e verificabilidade; *Conceptual Design for AI Systems* (`avila-ahmad-chapter-4-local`) organiza oportunidade e requisitos antes do detalhamento. Esta é uma síntese original adaptada ao curso.

Fontes primárias e oficiais complementam a base com riscos, desenvolvimento seguro, avaliação e RAG. Elas oferecem métodos, não arquitetura pronta para os casos.

## Conexão com o próximo módulo

O desenho conceitual do Módulo 2 termina quando sabemos **por que** uma fonte externa é necessária, **que evidência** deve ser recuperada, **quem pode vê-la**, **como medir suporte** e **quando recusar**. O [Módulo 3 — RAG](../sobre/plano-da-disciplina.md#modulo-3) detalhará os dois fluxos que implementam essa decisão: ingestão e consulta. Segmentação, índices, recuperação híbrida e reranking só devem aparecer depois que atualização, proveniência, autorização e cobertura justificarem a complexidade.

## Referências citadas no módulo

Somente as fontes abaixo sustentaram afirmações deste módulo. Todas constam na [Bibliografia consolidada](../referencia/bibliografia.md) e no registro editorial.

- Avila, R. D.; Ahmad, I. (2025). *The Case for Architecture*. Material local fornecido pelo professor. (`avila-ahmad-chapter-2-local`)
- Avila, R. D.; Ahmad, I. (2025). *Software Engineering and Architecture*. Material local fornecido pelo professor. (`avila-ahmad-chapter-3-local`)
- Avila, R. D.; Ahmad, I. (2025). *Conceptual Design for AI Systems*. Material local fornecido pelo professor. (`avila-ahmad-chapter-4-local`)
- Bommasani, R. et al. (2021). [*On the Opportunities and Risks of Foundation Models*](https://arxiv.org/abs/2108.07258). Riscos e oportunidades dependentes do contexto e da composição.
- Lewis, P. et al. (2020). [*Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*](https://proceedings.neurips.cc/paper/2020/hash/6b493230-Abstract.html). Trabalho original de RAG.
- National Institute of Standards and Technology (2024). [*Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*](https://doi.org/10.6028/NIST.AI.600-1). Perfil oficial de riscos de IA generativa.
- National Institute of Standards and Technology (2024). [*Secure Software Development Practices for Generative AI and Dual-Use Foundation Models*](https://doi.org/10.6028/NIST.SP.800-218A). Perfil oficial de desenvolvimento seguro.
- Liang, P. et al. (2023). [*Holistic Evaluation of Language Models*](https://arxiv.org/abs/2211.09110). Avaliação multidimensional de modelos de linguagem.
- Liu, Y. et al. (2023). [*G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment*](https://aclanthology.org/2023.emnlp-main.153/). Técnica primária de avaliação de geração com modelos.
- ISO/IEC/IEEE (2022). [*ISO/IEC/IEEE 42010:2022 — Architecture description*](https://www.iso.org/standard/74393.html). Estrutura conceitual para preocupações, pontos de vista, vistas, tipos de modelo e correspondências.
- Software Engineering Institute. [*Modifiability Tactics*](https://www.sei.cmu.edu/library/modifiability-tactics/). Definição e uso de táticas como decisões dirigidas a atributos de qualidade.
- Brown, S. [*C4 model*](https://c4model.com/). Abstrações hierárquicas e diagramas complementares de contexto, estrutura, dinâmica e implantação.
- arc42. [*Introduction and Goals*](https://docs.arc42.org/section-1/) e [*Architecture Decisions*](https://docs.arc42.org/section-9/). Priorização de objetivos de qualidade e registro de decisões arquiteturalmente significativas.

Continue pelo [Módulo 3](../sobre/plano-da-disciplina.md#modulo-3) ou volte ao [mapa de aprendizagem](../comecar/mapa-de-aprendizagem.md).
