# Exercícios: construir evidência de confiança

Use o assistente de RH quando não houver outro contexto. Nos níveis iniciais, consulte a resposta após tentar. Nos superiores, entregue os artefatos e revise-os pela rubrica.

## Recordar

### 1. O que distingue confiança sistêmica de confiança no modelo?

<details>
<summary>Resposta comentada</summary>

Confiança sistêmica é uma expectativa justificada sobre a solução no contexto de uso. Inclui modelo, dados, recuperação, ferramentas, identidade, políticas, pessoas, fornecedores e operação. Avaliar apenas o modelo ignora falhas de composição, como acesso indevido, fonte contaminada ou aprovação humana sem informação.

</details>

### 2. Defina risco inerente e risco residual.

<details>
<summary>Resposta comentada</summary>

Risco inerente é avaliado antes de considerar controles. Risco residual é o que permanece após controles e condições operacionais. Controle pode reduzir probabilidade, impacto, tempo de detecção ou recuperação, mas não transforma automaticamente risco em zero. A aceitação do residual cabe a um proprietário com autoridade.

</details>

### 3. Quais são as seis camadas de guardrails usadas neste módulo?

<details>
<summary>Resposta comentada</summary>

Entrada, contexto, recuperação, ferramenta, saída e aprovação humana. Elas cobrem modos de falha diferentes. A ordem não implica que a última camada seja infalível: aprovação pode falhar por fadiga, viés ou contexto enganoso.

</details>

### 4. Quais dimensões compõem o prisma de avaliação?

<details>
<summary>Resposta comentada</summary>

Factualidade, relevância, fundamentação, segurança, utilidade, latência e custo. Dimensões críticas podem ser portões; dimensões negociáveis podem ter metas. Uma média única não deve compensar um evento intolerável.

</details>

## Compreender

### 5. Por que separar instrução e conteúdo recuperado ajuda, mas não elimina injeção indireta?

<details>
<summary>Resposta comentada</summary>

Marcação de fronteiras, contexto mínimo e tratamento da fonte como dado tornam a intenção arquitetural mais clara e reduzem algumas confusões. Porém o modelo continua processando linguagem de instrução e conteúdo com o mesmo mecanismo, e ataques novos podem atravessar a separação. Por isso autorização e execução de ferramentas permanecem fora do modelo, com catálogo mínimo, política, validação e aprovação por risco.

</details>

### 6. Por que rastreabilidade e minimização não são objetivos opostos?

<details>
<summary>Resposta comentada</summary>

Rastreabilidade requer reconstruir versões, fontes, decisões, aprovações e resultados relevantes; não exige guardar todo conteúdo indefinidamente. Identificadores, hashes, categorias, métricas e amostras controladas podem fornecer evidência com menos exposição. Quando o texto completo for necessário, acesso, finalidade e prazo devem ser explícitos.

</details>

### 7. Compare verificações determinísticas, rubricas humanas e avaliação assistida por modelo.

<details>
<summary>Resposta comentada</summary>

Verificações determinísticas são reproduzíveis para propriedades codificáveis, mas não capturam toda nuance. Rubricas humanas trazem contexto, mas têm custo, fadiga e divergência. Avaliação assistida por modelo amplia escala, porém introduz variância, viés e correlação. A combinação calibrada produz evidência mais diversa; nenhuma é padrão-ouro universal.

</details>

## Aplicar

### 8. Identificação de ameaças em uma nova integração

O assistente de RH passará a ler anexos enviados por empregados e a criar um rascunho de chamado. Para cinco ameaças — incluindo ao menos injeção indireta, vazamento e consumo econômico — produza uma tabela com: ativo, ator, precondição, percurso, impacto, sinal de detecção e risco inerente. Diferencie “anexo autorizado para o usuário” de “anexo confiável como instrução”.

**Rubrica (10 pontos).** 2 pontos por ativos e atores específicos; 2 por precondições e percursos plausíveis; 2 por impactos sobre pessoas e organização; 2 por sinais observáveis; 2 por distinguir autorização de integridade. Respostas que apenas copiam nomes do OWASP sem conectá-los ao fluxo recebem no máximo 4 pontos.

### 9. Mapeamento de controles por camada

Escolha três ameaças do exercício anterior e monte uma matriz com controles nas camadas de entrada, contexto, recuperação, ferramenta, saída e aprovação humana. Para cada controle, declare o que ele reduz, o que não garante, proprietário, modo de falha e evidência de teste. Inclua ao menos uma degradação segura quando um guardrail estiver indisponível.

**Rubrica (10 pontos).** 2 pontos pela cobertura das seis camadas; 2 pela relação causal entre ameaça e controle; 2 por limites precisos; 2 por propriedade e modo de falha; 2 por testes e degradação. A frase “a IA detecta ataques” sem mecanismo e evidência não pontua como controle.

## Analisar

### 10. Diagnóstico de uma regressão composta

Após trocar modelo e reindexar políticas, a factualidade média sobe de 3,2 para 3,5 em 4, mas a recuperação de documentos vigentes cai de 96% para 91%; perguntas de gestores melhoram, perguntas de terceirizados pioram; dois de 80 casos obrigatórios deixam de escalar; latência p95 aumenta 40%; e o avaliador automático quase nunca discorda do novo modelo. Analise por que a média não sustenta liberação. Separe hipóteses de recuperação, geração, avaliador e composição. Proponha investigações que possam refutar cada hipótese e indique quais portões interrompem o rollout.

**Rubrica (12 pontos).** 3 pontos por decomposição causal; 2 por análise de fatias; 2 pela coerência entre severidade, evidência e decisão de liberação; 2 pela crítica ao avaliador; 2 por experimentos refutáveis; 1 por conclusão explícita. Confundir correlação com causa reduz a nota em até 3 pontos.

## Avaliar

### 11. Julgamento de risco residual

Um piloto encontrou zero vazamentos em 2 mil casos, 99% de escalonamento obrigatório, custo dentro do orçamento e 8% de falsas recusas. Um vazamento teria alto impacto; uma falsa recusa leva ao canal humano em até um dia. Segurança propõe ampliar para toda a empresa com monitoramento; RH quer corrigir primeiro o 1% de falhas de escalonamento. Produza um parecer de uma página que recomende aceitar, reduzir, transferir, suspender ou combinar tratamentos. Declare incerteza amostral, pessoas afetadas, apetite de risco, controles compensatórios, autoridade para aceitar, prazo e gatilhos de revisão.

**Rubrica (12 pontos).** 2 pontos por distinguir ausência observada de risco zero; 2 por severidade e afetados; 2 por avaliar separadamente falha de escalonamento e falsa recusa; 2 por tratamento proporcional; 2 por autoridade, prazo e gatilhos; 2 por conclusão coerente com as evidências. Uma recomendação sem explicitar risco residual recebe no máximo 6 pontos.

## Criar

### 12. Arquitetura de confiança e rubrica de avaliação

Crie uma arquitetura de confiança para um assistente que atende empregados e gestores, usa políticas públicas e restritas, consulta dados pessoais e encaminha casos sensíveis. Entregue:

1. diagrama com atores, ativos, fronteiras, identidade, recuperação, modelo, ferramenta de leitura, validação, aprovação e telemetria;
2. cinco cenários de ameaça, incluindo cadeia de fornecedores e manipulação de memória;
3. controles em profundidade com limitações e modo seguro de falha;
4. governança de minimização, retenção, segregação, catálogo, versões, auditoria e política de uso;
5. uma **rubrica de avaliação** de quatro níveis para factualidade, fundamentação, segurança e utilidade;
6. conjunto de referência com fatias comuns, raras, adversariais e de recusa;
7. pipeline de avaliação por componente e ponta a ponta, com verificações determinísticas, avaliador assistido por modelo e amostra humana;
8. portões de liberação, canary, rollback e regra de aceitação do risco residual.

Inclua um equivalente textual do diagrama. Justifique cada decisão por cenário e atributo de qualidade. Não use “criptografia”, “filtro” ou “humano no loop” como garantia genérica: diga onde atua, qual falha reduz e qual permanece.

**Rubrica (20 pontos).** 3 pontos por modelo de ameaças e fronteiras; 3 por identidade e segregação; 3 por defesas independentes e seus limites; 2 por privacidade no ciclo de vida; 2 por governança e responsabilidades; 3 por desenho multidimensional da avaliação; 2 por portões, canary e rollback; 2 por clareza, rastreabilidade e coerência entre diagrama e texto. Uma solução sem escalonamento obrigatório ou sem teste negativo de autorização recebe no máximo 12 pontos.

## Orientação para revisão entre pares

Ao revisar, procure “impede”, “garante” e “100% seguro”. Peça evidência, universo testado e modo de falha. Verifique ainda quem mantém, responde ao alerta, aceita o risco e pode desligar. A revisão revela premissas ocultas pelo diagrama.

Feche o módulo com a [Síntese e referências](sintese-e-referencias.md).
