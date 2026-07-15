# Exercícios: operar e escalar com controle

Use o portfólio do estudo de caso quando não houver outro contexto. Nos níveis iniciais, tente antes de abrir a resposta. Nos níveis superiores, entregue artefatos verificáveis; nomes de ferramentas sem decisão, limite ou proprietário não recebem pontuação integral.

## Recordar

### 1. O que é um ativo comportamental?

<details>
<summary>Resposta comentada</summary>

É qualquer artefato cuja mudança pode alterar resposta, decisão, custo, latência, acesso ou efeito. Inclui modelo e parâmetros, prompt, política, corpus, snapshot do índice, embedding, recuperação, ferramenta, memória, avaliador, conjunto de referência, orquestração e dependências. Versionar apenas código não reconstrói o comportamento de uma solução generativa.

</details>

### 2. O que diferencia fallback de rollback?

<details>
<summary>Resposta comentada</summary>

Fallback usa uma alternativa durante uma falha ou condição, como outro modelo ou busca sem geração. Rollback restaura um manifesto anterior conhecido. Fallback deve preservar classe de dados e guardrails; rollback precisa manter compatibilidade entre todos os ativos. Efeitos externos já realizados podem exigir reconciliação ou compensação, não apenas rollback.

</details>

### 3. Quais são os quatro planos de métricas?

<details>
<summary>Resposta comentada</summary>

Produto, modelo, operação e negócio. Eles conectam jornada e resultado, qualidade comportamental, saúde técnica e valor organizacional. Nenhum plano substitui os outros: disponibilidade não prova utilidade, e satisfação não revela uma violação rara de segurança.

</details>

### 4. O que distingue showback de chargeback?

<details>
<summary>Resposta comentada</summary>

Showback mostra consumo e custo atribuído às unidades, sem transferência contábil. Chargeback transfere o custo. Showback ajuda a validar medição e ensinar comportamento. Chargeback exige tags confiáveis, regra transparente para custos comuns e contestação; aplicado cedo, pode incentivar subnotificação ou uso fora da plataforma.

</details>

## Compreender

### 5. Por que reprodutibilidade não significa sempre obter o mesmo texto?

<details>
<summary>Resposta comentada</summary>

Inferência pode variar por amostragem, hardware, concorrência ou atualização invisível do provedor. A reprodução operacional reconstrói configuração, entradas, versões e decisões suficientes para comparar critérios e distribuições. Seeds e parâmetros são registrados quando existem; repetições e intervalos tratam variância quando identidade bit a bit não é possível.

</details>

### 6. Por que um fallback saudável não pode ser apenas o modelo mais disponível?

<details>
<summary>Resposta comentada</summary>

O modelo alternativo precisa ser permitido para a classe de dados, região, finalidade, ferramentas e qualidade exigidas. Trocar automaticamente para um modelo público pode remover fundamentação ou enviar dados restritos a um fornecedor não aprovado. Quando não há alternativa semanticamente compatível, a resposta correta é degradar capacidade e comunicar o limite.

</details>

### 7. Como plataforma compartilhada pode aumentar e reduzir risco ao mesmo tempo?

<details>
<summary>Resposta comentada</summary>

Ela reduz credenciais dispersas, controles divergentes e telemetria incompatível. Entretanto concentra dependência: uma falha no gateway ou guardrail comum alcança vários produtos; abstrações podem ocultar diferenças entre fornecedores; política genérica pode ser aplicada fora do contexto. Contratos, isolamento, rollout gradual, extensão governada e propriedade de produto equilibram o trade-off.

</details>

## Aplicar

### 8. Manifesto e portão de regressão

O RAG de políticas trocará modelo de embedding, chunking e prompt no mesmo release. Crie um manifesto com versões de todos os ativos comportamentais, compatibilidades, evidências, proprietário e rota de retorno. Depois especifique um **portão de regressão** com verificações determinísticas, avaliação por componente e ponta a ponta, fatias, casos adversariais, limiares de bloqueio e trade-offs revisáveis. Inclua como testar se o rollback restaura índice, prompt e modelo compatíveis.

**Rubrica (10 pontos).** 2 pontos por inventário completo e imutável; 2 por compatibilidade e reprodução; 2 por cobertura multidimensional e por fatia; 2 por critérios de bloqueio separados de metas; 2 por rollback ensaiável. Uma lista sem versão de corpus, avaliador ou conjunto recebe no máximo 6 pontos.

### 9. Trace e SLO com privacidade

Desenhe o trace de uma consulta que recupera documentos, chama um modelo e pode abrir rascunho de solicitação. Para cada span, declare identificadores, versões, tempos, decisão de política e conteúdo que não será coletado. Defina dois SLOs: um de resposta útil e outro de ação sem duplicidade. Especifique janela, população elegível, indicador, meta, fonte, atraso, alerta, runbook e comportamento diante de evento intolerável.

**Rubrica (10 pontos).** 2 pontos por causalidade entre prompt, contexto, recuperação, ferramenta e resposta; 2 por versões e política; 2 por minimização, segregação e retenção; 2 por SLOs mensuráveis e centrados no usuário; 2 por alertas acionáveis. Guardar todas as conversas “para observabilidade” zera o item de privacidade.

## Analisar

### 10. Diagnóstico de rollout composto

Um canary reduz custo por chamada em 25% e p95 em 15%. Ao mesmo tempo, tarefas concluídas caem 6%, tokens por tarefa sobem, fundamentação piora apenas em português, erros do gateway permanecem estáveis e uma ferramenta dobra chamadas após timeout. O avaliador automático declara melhora geral. Analise hipóteses separadas para roteamento, modelo, recuperação, ferramenta, avaliador e experiência. Relacione métricas de produto, modelo, operação e negócio; indique traces e experimentos que refutariam cada hipótese; decida pausar, reverter, degradar ou ampliar.

**Rubrica (12 pontos).** 3 pontos por decomposição causal; 2 por relacionar métricas sem tratá-las como equivalentes; 2 pela qualidade da análise por fatia e do avaliador; 2 pela análise de efeitos sob incerteza; 2 por experimentos refutáveis; 1 por decisão coerente com as evidências.

## Avaliar

### 11. Plataforma comum ou autonomia local?

A plataforma propõe gateway, prompt registry, RAG, ferramentas e guardrails comuns. Atendimento quer capacidade específica de streaming; Jurídico exige índice fisicamente isolado; Compras precisa de executor transacional; FinOps quer chargeback imediato. Produza parecer com capacidades que devem ser comuns, específicas ou adiadas. Avalie reuso versus acoplamento, ponto único de falha, portabilidade, estratégia multimodelo, identidade, tenancy, política, equipes, cotas e modelo econômico. Registre ao menos três ADRs e gatilhos de revisão.

**Rubrica (12 pontos).** 2 pontos por contexto e critérios; 2 por fronteiras coerentes; 2 por riscos de concentração e contenção; 2 por autonomia governada e portabilidade graduada; 2 por responsabilidades e FinOps; 2 por ADRs com consequências e gatilhos. “Centralizar tudo” ou “cada time escolhe tudo” sem análise recebe no máximo 5 pontos.

## Criar

### 12. Capstone — arquitetura e plano operacional da organização

Crie a arquitetura-alvo e um plano incremental para a organização que possui copiloto, RAG e agente isolados, componentes duplicados, fornecedores incompatíveis, rastreabilidade pobre e custo crescente. A entrega deve ser autocontida e conter:

1. **contexto:** atores, jornadas, sistemas existentes, classes de dados, efeitos, restrições, pressupostos e usos proibidos;
2. **atributos de qualidade:** ao menos oito cenários no formato fonte, estímulo, ambiente, artefato, resposta e medida, incluindo qualidade, fundamentação, latência, custo, privacidade, segurança, confiabilidade e observabilidade;
3. **componentes:** produtos, model gateway, registros, RAG, ferramentas, guardrails, catálogo, identidade, tenancy, política, telemetria, avaliação, fornecedores e sistemas corporativos, com responsabilidades;
4. **fluxos:** consulta fundamentada, ação aprovada, ingestão, promoção, canary, fallback, rollback, degradação e incidente; forneça diagrama e equivalente textual;
5. ao menos quatro **ADRs** sobre fronteira da plataforma, portabilidade ou multimodelo, isolamento e modelo econômico, com alternativas, consequências e gatilhos;
6. **guardrails:** controles por entrada, contexto, recuperação, ferramenta, saída e aprovação, declarando limite, proprietário, modo de falha e teste;
7. **avaliação:** conjunto de referência, fatias, casos adversariais, rubricas, instrumentos, calibração humana, testes por componente e ponta a ponta, portões e critérios de canary;
8. **operações:** manifesto, ambientes, SLOs, traces, logs com preservação de privacidade, alertas, runbooks, plantão, quotas, showback ou chargeback e resposta a incidente;
9. **riscos residuais:** probabilidade, impacto, afetados, controles, autoridade de aceitação, prazo e gatilho de revisão;
10. três **experimentos:** hipótese refutável, baseline, variável, população, duração, métricas dos quatro planos, guardrails, critério de parada e decisão possível;
11. roadmap de três incrementos que preserve valor e contenção antes da migração total.

Mostre as **fronteiras de propriedade** entre equipe de plataforma, equipes de produto, segurança e privacidade, operação, FinOps, domínios e dono do processo. Para cada falha — fornecedor, índice, gateway, guardrail, executor e telemetria — declare raio de impacto e contenção. Para o gateway, inclua réplicas em domínios de falha, health failover, condições de bypass com controles equivalentes e degradação por produto quando não houver caminho seguro. Nenhuma opção pode usar “humano no loop”, “monitoramento” ou “multimodelo” como garantia sem mecanismo.

**Rubrica (24 pontos).** 3 pontos por contexto e qualidade mensurável; 3 por arquitetura, componentes e contratos; 3 por fluxos completos e equivalentes textuais; 2 por ADRs e trade-offs; 3 por guardrails e autoridade; 3 por avaliação e portões; 3 por operações, recuperação e privacidade; 2 por riscos residuais; 2 por experimentos e roadmap. Sem identidade propagada, teste negativo de tenancy, rollback do manifesto ou modo seguro para ação, a entrega recebe no máximo 14 pontos.

## Orientação para revisão entre pares

Faça uma trilha vertical: escolha uma mudança de corpus e siga versão, avaliação, promoção, trace, SLO, incidente e aprendizagem. Depois faça uma trilha horizontal: escolha uma ação e siga usuário, identidade, gateway, política, ferramenta, aprovação, sistema e auditoria. Procure saltos de responsabilidade, fallback que reduz segurança, métrica sem decisão e risco sem autoridade.

Feche o curso com a [Síntese e referências](sintese-e-referencias.md).
