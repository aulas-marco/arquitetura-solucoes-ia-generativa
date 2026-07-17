# Exercícios: operar e escalar com controle

Use o portfólio do caso. Artefato exige decisão, limite e proprietário.

## Recordar

### 1. O que é um ativo comportamental?

<details>
<summary>Resposta comentada</summary>

É qualquer artefato cuja mudança altera resposta, decisão, custo, latência, acesso ou efeito: modelo, prompt, política, corpus, índice, embedding, ferramenta, memória, avaliador, orquestração e dependências. Versionar só código não reconstrói comportamento.

</details>

### 2. O que diferencia fallback de rollback?

<details>
<summary>Resposta comentada</summary>

Fallback usa alternativa durante falha; rollback restaura manifesto anterior. Fallback preserva classe de dados e guardrails; rollback mantém ativos compatíveis. Efeitos externos podem exigir compensação.

</details>

### 3. Quais são os quatro planos de métricas?

<details>
<summary>Resposta comentada</summary>

Produto, modelo, operação e negócio conectam jornada, comportamento, saúde técnica e valor. Disponibilidade não prova utilidade; satisfação não revela violação rara.

</details>

### 4. O que distingue showback de chargeback?

<details>
<summary>Resposta comentada</summary>

Showback mostra consumo sem transferência contábil; chargeback transfere custo. Chargeback exige tags, regra para custos comuns e contestação.

</details>

## Compreender

### 5. Por que reprodutibilidade não significa sempre obter o mesmo texto?

<details>
<summary>Resposta comentada</summary>

Inferência varia por amostragem, hardware, concorrência ou provedor. Reprodução reconstrói configuração, entradas, versões e decisões; registre seeds quando existirem e use repetições para tratar variância.

</details>

### 6. Por que um fallback saudável não pode ser apenas o modelo mais disponível?

<details>
<summary>Resposta comentada</summary>

O alternativo deve ser permitido para classe de dados, região, finalidade, ferramentas e qualidade. Modelo público pode remover fundamentação ou expor dados; sem alternativa compatível, degrade e comunique o limite.

</details>

### 7. Como plataforma compartilhada pode aumentar e reduzir risco ao mesmo tempo?

<details>
<summary>Resposta comentada</summary>

Ela reduz credenciais dispersas e telemetria incompatível, mas concentra dependência: falha no gateway alcança produtos e abstração oculta diferenças. Contratos, isolamento, rollout e propriedade equilibram o trade-off.

</details>

## Aplicar

### 8. Manifesto e portão de regressão

**Ativo comportamental** muda resposta, decisão, custo, latência, acesso ou efeito; **manifesto** registra versões; **portão** bloqueia promoção (**o que é** cada um?). Consulte [pacote comportamental](conceitos.md#o-objeto-operado-e-um-pacote-comportamental).

**Situação**

O RAG de políticas trocará modelo de embedding, chunking e prompt no mesmo release. Uma falha de compatibilidade pode parecer uma regressão do modelo, mas pode ter nascido no corpus, no índice ou no avaliador.

**Seu papel**

Você torna a mudança reproduzível e decide quando bloquear.

**Insumos disponíveis**

Consulte o [manifesto da oficina](oficina-de-ferramentas.md), o conjunto de referência e os [padrões](padroes-e-decisoes.md).

**Como conduzir**

1. Liste versões, dependências, compatibilidades, evidências, proprietário e rota de retorno.
2. Separe verificações determinísticas, avaliação por componente, ponta a ponta, fatias e casos adversariais.
3. Defina limiares de bloqueio diferentes de metas de melhoria.
4. Descreva um ensaio que confirme que rollback restaura índice, prompt e modelo compatíveis.

**Entrega esperada**

Entregue manifesto, portão de regressão e roteiro de ensaio do rollback.

**Como verificar**

Confira versões, proprietários e compatibilidade do manifesto em homologação.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Inventário | 20% | Versiona todos os ativos comportamentais e seus responsáveis. |
| Compatibilidade | 20% | Explica dependências e como reproduzir a configuração. |
| Cobertura | 20% | Inclui dimensões, fatias e casos adversariais. |
| Bloqueio | 20% | Separa limites de segurança de metas de melhoria. |
| Rollback | 20% | Define ensaio que verifica restauração compatível. |

### 9. Trace e SLO com privacidade

**Span** é etapa observável do trace; **SLO** é meta de indicador numa janela (**o que é** cada um?). Consulte [trace](conceitos.md#trace-reconstruir-a-composicao).

**Situação**

Uma consulta recupera documentos, chama um modelo e pode abrir um rascunho de solicitação. O trace precisa permitir diagnóstico sem guardar a pergunta completa ou dados pessoais desnecessários.

**Seu papel**

Você conecta causalidade, privacidade e ação operacional.

**Insumos disponíveis**

Consulte o [script de telemetria](oficina-de-ferramentas.md), trace, SLO e o [catálogo](../referencia/atributos-de-qualidade.md).

**Como conduzir**

1. Para cada span, escolha identificadores, versões, tempos, política e conteúdo que será minimizado.
2. Defina um SLO de resposta útil e outro de ação sem duplicidade.
3. Preencha janela, população, indicador, meta, fonte, atraso, alerta e runbook.
4. Diga o que acontece quando um evento intolerável é detectado.

**Entrega esperada**

Entregue um esquema de trace e duas fichas de SLO com ação de alerta e política de retenção.

**Como verificar**

Confira trace minimizado e todos os campos do SLO, inclusive runbook.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Causalidade | 20% | Relaciona prompt, contexto, recuperação, ferramenta e resposta. |
| Versões e política | 20% | Registra configuração e decisão de acesso necessárias. |
| Privacidade | 20% | Minimiza, segrega e retém dados com finalidade explícita. |
| SLOs | 20% | Define indicadores mensuráveis centrados no usuário. |
| Alertas | 20% | Liga sinal a proprietário, runbook e ação. |

## Analisar

### 10. Diagnóstico de rollout composto

**Canary** expõe versão a parcela; **fallback** usa alternativa; **rollback** restaura manifesto (**o que é** ação segura?). Leia [entrega](conceitos.md#avaliacao-continua-e-entrega-controlada).

**Situação**

Um canary reduz custo por chamada em 25% e p95 em 15%, mas tarefas concluídas caem 6%, tokens por tarefa sobem, fundamentação piora em português e uma ferramenta dobra chamadas após timeout. O avaliador automático declara melhora geral.

**Seu papel**

Você separa economia técnica de valor e decide pausar, reverter, degradar ou ampliar.

**Insumos disponíveis**

Consulte os quatro planos, o [trace da oficina](oficina-de-ferramentas.md) e os conceitos de canary, fallback e rollback.

**Como conduzir**

1. Organize sinais por produto, modelo, operação e negócio.
2. Separe hipóteses de roteamento, modelo, recuperação, ferramenta, avaliador e experiência.
3. Indique trace, amostra ou experimento que refutaria cada hipótese.
4. Decida uma ação provisória e registre o limite que a faria mudar.

**Entrega esperada**

Entregue tabela hipótese → evidência → teste → ação e parecer de rollout de até 400 palavras.

**Como verificar**

Confira quatro planos, teste refutador e limite de interrupção.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Decomposição causal | 25% | Não trata variação média como causa única. |
| Métricas relacionadas | 20% | Conecta planos sem considerá-los equivalentes. |
| Fatias e avaliador | 20% | Considera idioma, tarefa e limites do avaliador. |
| Experimentos | 20% | Define testes capazes de refutar hipóteses. |
| Decisão | 15% | Liga evidência a pausa, reversão, degradação ou ampliação. |

## Avaliar

### 11. Plataforma comum ou autonomia local?

**Fronteira de propriedade** diz quem decide, mantém, alerta e aceita risco; **ADR** registra contexto e decisão (**o que é** responsabilidade?). Consulte [promoção](conceitos.md#ambientes-e-promocao).

**Situação**

A plataforma propõe gateway, registro de prompts, RAG, ferramentas e guardrails comuns. Atendimento quer streaming específico; Jurídico exige índice isolado; Compras precisa de executor transacional; FinOps quer atribuição de custo imediata.

**Seu papel**

Você decide o que é plataforma comum, específico ou adiado.

**Insumos disponíveis**

Consulte o [caso](estudo-de-caso.md) e os [padrões](padroes-e-decisoes.md).

**Como conduzir**

1. Separe capacidades comuns, específicas e adiadas com uma razão verificável.
2. Compare reuso, acoplamento, concentração de falha e portabilidade.
3. Explicite responsabilidades de plataforma, produto, segurança, operação e FinOps.
4. Registre três ADRs e um gatilho de revisão para cada decisão relevante.

**Entrega esperada**

Entregue parecer com matriz de responsabilidades, três ADRs resumidas e gatilhos.

**Como verificar**

Confira decisão, consequência, gatilho e responsabilidades em cada ADR.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Contexto e critérios | 15% | Liga decisões às necessidades dos quatro domínios. |
| Fronteiras | 20% | Define o que é comum, específico ou adiado. |
| Concentração e contenção | 20% | Trata ponto único de falha e controles equivalentes. |
| Autonomia e portabilidade | 15% | Preserva evolução sem permitir escolhas sem governança. |
| Responsabilidades e FinOps | 15% | Nomeia proprietário, cotas e modelo econômico. |
| ADRs e gatilhos | 15% | Registra consequências e condição de revisão. |

## Criar

### 12. Capstone — arquitetura e plano operacional da organização

**Situação**

Uma organização tem copiloto, RAG e agente isolados, duplicação, fornecedores incompatíveis, pouca rastreabilidade e custo crescente. Proponha arquitetura operável, mensurável e reversível.

Aqui, **o que é** arquitetura operável? Mudança, evidência, decisão e recuperação têm dono e limite.

**Seu papel**

Você fecha fronteiras de propriedade, contratos operacionais e decisões de liberação.

**Insumos disponíveis**

Use [pacote comportamental](conceitos.md#o-objeto-operado-e-um-pacote-comportamental), [trace](conceitos.md#trace-reconstruir-a-composicao), [SLO](conceitos.md#slo-para-servico-util) e [exemplo](exemplo-arquitetural.md).

**Como conduzir**

1. Delimite contexto, dados, jornadas, efeitos permitidos e usos proibidos.
2. Desenhe componentes e fluxos com propriedade e evidência.
3. Monte manifesto, critérios, portões, canary, fallback, rollback, SLOs, traces, alertas e runbooks.
4. Siga mudança de corpus até incidente e ação de usuário até auditoria; declare contenção e decisão para cada falha.

Crie a arquitetura-alvo e um plano incremental para a organização que possui copiloto, RAG e agente isolados, componentes duplicados, fornecedores incompatíveis, rastreabilidade pobre e custo crescente. A entrega deve ser autocontida e conter:

1. **contexto:** atores, jornadas, sistemas existentes, classes de dados, efeitos, restrições, pressupostos e usos proibidos;
2. **atributos de qualidade:** ao menos oito cenários no formato fonte, estímulo, ambiente, artefato, resposta e medida, incluindo qualidade, fundamentação, latência, custo, privacidade, segurança, confiabilidade e observabilidade;
3. **componentes:** produtos, model gateway, registros, RAG, ferramentas, guardrails, catálogo, identidade, tenancy, política, telemetria, avaliação, fornecedores e sistemas corporativos, com responsabilidades;
4. **fluxos:** consulta fundamentada, ação aprovada, ingestão, promoção, canary, fallback, rollback, degradação e incidente; forneça diagrama e equivalente textual;
5. ao menos quatro **ADRs** sobre fronteira da plataforma, portabilidade ou multimodelo, isolamento e modelo econômico, com alternativas, consequências e gatilhos;
6. **guardrails:** controles por entrada, contexto, recuperação, ferramenta, saída e aprovação, declarando limite, proprietário, modo de falha e teste;
7. **avaliação:** conjunto de referência, fatias, casos adversariais, critérios, instrumentos, calibração humana, testes por componente e ponta a ponta, portões e critérios de canary;
8. **operações:** manifesto, ambientes, SLOs, traces, logs com preservação de privacidade, alertas, runbooks, plantão, quotas, showback ou chargeback e resposta a incidente;
9. **riscos residuais:** probabilidade, impacto, afetados, controles, autoridade de aceitação, prazo e gatilho de revisão;
10. três **experimentos:** hipótese refutável, baseline, variável, população, duração, métricas dos quatro planos, guardrails, critério de parada e decisão possível;
11. roadmap de três incrementos que preserve valor e contenção antes da migração total.

Mostre as **fronteiras de propriedade** entre equipe de plataforma, equipes de produto, segurança e privacidade, operação, FinOps, domínios e dono do processo. Para cada falha — fornecedor, índice, gateway, guardrail, executor e telemetria — declare raio de impacto e contenção. Para o gateway, inclua réplicas em domínios de falha, health failover, condições de bypass com controles equivalentes e degradação por produto quando não houver caminho seguro. Nenhuma opção pode usar “humano no loop”, “monitoramento” ou “multimodelo” como garantia sem mecanismo.

**Entrega esperada**

Entregue pacote com contexto, diagramas, manifesto, ADRs, critérios, portões, SLOs, traces, runbooks, riscos, experimentos e roadmap.

**Como verificar**

- Percorra uma mudança de corpus completa: versão, avaliação, promoção, trace, SLO, incidente e aprendizado.
- Percorra uma ação de usuário completa: identidade, gateway, política, ferramenta, aprovação, sistema externo e auditoria.
- Confira que cada SLO possui indicador, janela, meta, fonte, proprietário e runbook; que cada ADR possui alternativa e gatilho; e que cada risco residual possui autoridade e prazo.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Contexto e qualidade | 12% | Delimita atores, jornadas, restrições e cenários mensuráveis. |
| Arquitetura e contratos | 12% | Define componentes, fronteiras, responsabilidades e interfaces. |
| Fluxos e ADRs | 12% | Fecha fluxos, equivalentes textuais, alternativas e consequências. |
| Guardrails e autoridade | 12% | Define controles, limites, proprietários e modo de falha. |
| Avaliação e portões | 12% | Usa fatias, casos, critérios, canary e condição de bloqueio. |
| Operação e recuperação | 12% | Inclui SLOs, traces, alertas, rollback e degradação. |
| Privacidade e riscos residuais | 10% | Declara minimização, afetados, autoridade e gatilho. |
| Experimentos e roadmap | 10% | Define hipóteses refutáveis e incrementos reversíveis. |
| Propriedade e comunicação | 8% | Torna responsabilidades e decisões compreensíveis para os envolvidos. |

## Orientação para revisão entre pares

Faça uma trilha vertical da mudança de corpus ao incidente e outra horizontal da ação do usuário à auditoria. Procure saltos de responsabilidade, fallback que reduz segurança, métrica sem decisão e risco sem autoridade.
