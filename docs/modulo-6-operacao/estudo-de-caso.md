# Estudo de caso: de protótipos isolados a capacidade corporativa

## O portfólio fragmentado

Uma empresa de serviços cresceu por provas de conceito. Atendimento criou um **copiloto** em um provedor; Jurídico construiu um **RAG** em outro; Compras conectou um **agente** ao ERP. Há **componentes duplicados** para prompts, extração, filtros e telemetria. Os **fornecedores incompatíveis** usam schemas, regiões e contratos diferentes. Cada equipe chama “versão” a uma coisa. A rastreabilidade é pobre: não se sabe qual índice produziu uma resposta reclamada. O custo sobe, mas faturas não chegam ao produto ou resultado.

A diretoria pede uma plataforma única em três meses. Arquitetura recusa duas simplificações: não substituirá tudo por um modelo, nem criará uma camada que esconda toda diferença entre fornecedores. Primeiro, delimita contexto e risco de cada produto. Copiloto apenas sugere; RAG explica norma vigente; agente prepara pedido e só executa após política e aprovação. Uma mesma disponibilidade não implica o mesmo modo de degradação.

## Baseline e atributos

Durante quatro semanas, equipes inventariam ativos, fluxos, classes de dados, identidades, fornecedores, métricas e incidentes. O baseline revela 17 prompts ativos sem proprietário, quatro índices com ACL divergente, duas credenciais amplas, custo por resposta sem custo por tarefa e zero teste de rollback completo.

Os atributos aprovados são: isolamento de tenant e ação autorizada como bloqueios; 95% de fundamentação nível 3 ou 4 para RAG; p95 abaixo de 8 segundos; recuperação de consulta pública em 15 minutos; custo por caso resolvido dentro do orçamento; e trace capaz de relacionar release, fonte, política e ferramenta em 99,5% das execuções elegíveis. O dono do processo, não a plataforma, aceita o risco residual.

## Incrementos e ADRs

O primeiro incremento instala identidade, gateway de medição e manifesto comum sem migrar modelos. Isso produz showback e inventário de tráfego. ADR-01 aceita normalização limitada a autenticação, mensagens, erros e medição; capacidades específicas ficam em adaptadores tipados. A consequência é alguma complexidade no produto, revisada se o custo de manutenção superar o benefício.

O segundo incremento extrai catálogo de modelos, registro de prompts, política e telemetria. ADR-02 mantém índices restritos separados porque o impacto de cruzamento supera a economia. O RAG migra primeiro, com conjunto de referência e canary. O copiloto adota o gateway sem reescrever a jornada. O agente só migra após executor compartilhado oferecer identidade delegada, idempotência, reconciliação e aprovação vinculada à intenção.

ADR-03 escolhe estratégia multimodelo apenas para consulta pública. Testes mostram que o segundo modelo mantém fundamentação, mas falha em JSON de ferramentas; portanto não é fallback do agente. ADR-04 adota showback por seis meses. Chargeback depende de tags acima de 98%, regra para custos comuns e canal de contestação.

## Guardrails, avaliação e operação

Guardrails comuns tratam tamanho, dados sensíveis, modelos permitidos, budgets e saída. Produtos acrescentam regras de domínio: vigência e citação no RAG; efeito e aprovação no agente. A avaliação combina testes determinísticos, rubricas humanas calibradas e avaliador assistido por modelo. Casos são segmentados por tenant, idioma, fonte e rota. Mudança de prompt, corpus, ferramenta ou modelo percorre o mesmo portão.

Traces registram metadados minimizados; conteúdo completo fica em amostra segregada com prazo. SLOs ligam disponibilidade a resposta útil. Alertas têm runbook e proprietário. Canary começa em tenants voluntários; rollback referencia o manifesto inteiro. Se recuperação falhar, RAG mostra busca oficial; se política ou executor falhar, agente não escreve. Incidentes atualizam risco, avaliação e arquitetura.

## Incidente e aprendizagem

No canary, custo cai 18%, mas perguntas longas acionam fallback público mesmo para documentos restritos. Nenhum vazamento é observado, porém o desenho permitiria classe incompatível. A equipe interrompe rollout, desabilita o fallback, corrige a decisão de política antes do roteamento e cria teste que exige preservação de classe. A ausência de dano observado não reduz a severidade do risco residual.

Depois de doze semanas, dois produtos usam a base comum. O agente permanece parcialmente isolado, decisão consciente, não fracasso. O próximo **experimento** compara busca sem geração e modelo alternativo em indisponibilidade pública; outro mede se cache por versão reduz custo sem servir política vencida. Cada experimento tem hipótese, população, métricas, guardrails e critério de parada.

## Resultado e riscos residuais

A organização ganha comparabilidade, rota de recuperação e custo atribuível. Ainda restam lock-in em embeddings, mudança invisível de fornecedor, cobertura limitada de idiomas, dependência do gateway e capacidade de plantão. Esses **riscos residuais** têm proprietários, prazos e gatilhos: ensaio trimestral de saída, sentinelas diárias, ampliação de amostras, teste regional e revisão de SLO.

O caso demonstra que escala não é quantidade de componentes centralizados. É consistência seletiva: controles transversais comuns, autonomia de produto onde o contexto diverge e contratos que tornam a composição observável. A questão final não é “temos uma plataforma?”, mas “conseguimos mudar, conter e aprender sem perder responsabilidade?”.

## Entrega requerida para este caso final

Antes de comparar sua proposta com a trajetória descrita, produza um dossiê que contenha: **contexto** e usos proibidos; **atributos de qualidade** mensuráveis; **componentes** e proprietários; **fluxos** normais, degradados e de incidente; ao menos três **ADRs**; **guardrails** com limites; avaliação offline e em produção; plano de **operações** com SLOs, traces, promoção e recuperação; **riscos residuais** com autoridade; e **experimentos** com hipóteses refutáveis. Relacione cada item: um atributo precisa aparecer no fluxo, ser protegido ou observado por componente, orientar ADR e deixar evidência operacional. Se um experimento puder violar um bloqueio crítico, ele não é admissível.

Pratique essas decisões em [Exercícios](exercicios.md).
