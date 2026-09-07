# Exercícios: operar e escalar com controle

Use o caso. Artefato exige decisão, limite e proprietário.

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

### 5. Quais são os quatro portões de um laço autônomo?

Um laço que roda sem pessoa presente atravessa portões específicos, além dos que qualquer pacote comportamental precisa cumprir.

Nomeie os quatro e diga o que cada um verifica.

<details>
<summary>Ver resposta</summary>

Portão de critério: a condição de parada existe, é executável por comando determinístico, está versionada e discrimina, ou seja, existe caso conhecido em que ela reprova. Portão de orçamento: há dois tetos independentes, de iterações e de custo, cada um com dono e com comportamento definido no esgotamento, que não pode ser encerrar em silêncio. Portão de isolamento: o laço executa com identidade própria, escopo reduzido, credenciais de prazo curto e sem alcance a produção ou dado real enquanto o efeito não estiver classificado. Portão de interrupção: existe desligamento acessível fora do processo, documentado em runbook, testado e conhecido por quem está de plantão.
</details>

## Compreender

### 6. Reprodutibilidade e variação de saída

<details>
<summary>Resposta comentada</summary>

Inferência varia por amostragem, hardware, concorrência ou provedor. Reprodução reconstrói configuração, entradas, versões e decisões; registre seeds quando existirem e use repetições para tratar variância.

</details>

### 7. O que qualifica um fallback como saudável

<details>
<summary>Resposta comentada</summary>

O alternativo deve ser permitido para classe de dados, região, finalidade, ferramentas e qualidade. Modelo público pode remover fundamentação ou expor dados; sem alternativa compatível, degrade e comunique o limite.

</details>

### 8. Plataforma compartilhada: risco que sobe e risco que desce

<details>
<summary>Resposta comentada</summary>

Ela reduz credenciais dispersas e telemetria incompatível, mas concentra dependência: falha no gateway alcança produtos e abstração oculta diferenças. Contratos, isolamento, rollout e propriedade equilibram o trade-off.

</details>

## Aplicar

### 9. Manifesto e portão de regressão

**O que é:** **ativo comportamental** muda resposta, custo, acesso ou efeito; **manifesto** registra versões; **portão** bloqueia promoção. Consulte [pacote comportamental](pacote-e-promocao.md#o-objeto-operado-e-um-pacote-comportamental).

**Situação**

O RAG de políticas trocará modelo de embedding, chunking e prompt no mesmo release. Uma falha de compatibilidade pode parecer uma regressão do modelo, mas pode ter nascido no corpus, no índice ou no avaliador.

**Seu papel**

Você torna a mudança reproduzível e decide quando bloquear.

**Insumos disponíveis**

Use [manifesto](oficina-de-ferramentas.md#preparacao-do-laboratorio), [conjunto de referência](oficina-de-ferramentas.md#preparacao-do-laboratorio) e os [portões antes da exposição](pacote-e-promocao.md#portoes-antes-da-exposicao).

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

### 10. Trace e SLO com privacidade

**O que é:** **span** é etapa do trace; **SLO** é meta de indicador numa janela. Consulte [trace](observabilidade.md#trace-reconstruir-a-composicao) e [SLO](observabilidade.md#slo-para-servico-util).

**Situação**

Uma consulta recupera documentos, chama um modelo e pode abrir um rascunho de solicitação. O trace precisa permitir diagnóstico sem guardar a pergunta completa ou dados pessoais desnecessários.

**Seu papel**

Você conecta causalidade, privacidade e ação operacional.

**Insumos disponíveis**

Use [script de telemetria](oficina-de-ferramentas.md#receita-principal), [trace](observabilidade.md#trace-reconstruir-a-composicao), [SLO, indicador e janela](observabilidade.md#slo-para-servico-util), [incidente e runbook](entrega-e-recuperacao.md#incidente-generativo) e [catálogo](../referencia/atributos-de-qualidade.md).

**Laboratório.** Comece pelo trace que você mesmo produziu na [oficina](oficina-de-ferramentas.md#receita-principal): rode o script, guarde a saída dos spans `entrada`, `modelo` e `saida` com o `trace_id` e a duração, e trabalhe sobre esses três spans reais em vez de um esquema imaginado. O que o script emite hoje é o piso; o exercício é decidir o que falta e o que sobra.

**Como conduzir**

1. Compare os atributos que o script emite com os que a página de [trace](observabilidade.md#trace-reconstruir-a-composicao) exige. Aponte o que falta para diagnóstico e o que já é conteúdo demais.
2. Acrescente o span de recuperação e o de ferramenta, que a oficina local não produz, e para cada span escolha identificadores, versões, tempos, política e conteúdo que será minimizado.
3. Defina um SLO de resposta útil e outro de ação sem duplicidade.
4. Preencha janela, população, indicador, meta, fonte, atraso, alerta e runbook.
5. Diga o que acontece quando um evento intolerável é detectado.

**Entrega esperada**

Entregue a saída dos três spans da sua execução, o esquema de trace estendido e duas fichas de SLO com alerta e retenção.

**Como verificar**

Confira o [trace minimizado](observabilidade.md#trace-reconstruir-a-composicao), o indicador e a janela do [SLO](observabilidade.md#slo-para-servico-util), além do [runbook de incidente](entrega-e-recuperacao.md#incidente-generativo).

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Causalidade | 20% | Relaciona prompt, contexto, recuperação, ferramenta e resposta. |
| Versões e política | 20% | Registra configuração e decisão de acesso necessárias. |
| Privacidade | 20% | Minimiza, segrega e retém dados com finalidade explícita. |
| SLOs | 20% | Define indicadores mensuráveis centrados no usuário. |
| Alertas | 20% | Liga sinal a proprietário, runbook e ação. |

### 11. Telemetria comparada: Lume e Aurora

**O que é:** **trace** reconstrói a composição da chamada; **showback** e **chargeback** atribuem custo de formas diferentes. Consulte [trace](observabilidade.md#trace-reconstruir-a-composicao) e [modelo operacional da plataforma](plataforma-corporativa.md#modelo-operacional-da-plataforma).

**Situação**

O Lume mantém showback sem chargeback; a Aurora antecipa chargeback porque sua chamada de ferramenta a sistemas legados é mais atribuível que consulta a índice. Antes de validar essa diferença em produção, a equipe quer uma primeira evidência local, comparando o trace dos dois produtos sob a mesma plataforma.

**Seu papel**

Você produz a evidência comparativa que sustenta — ou não — a diferença de tratamento de custo entre os dois produtos.

**Insumos disponíveis**

Use o [script de telemetria do caso](caso-lume.md#mini-execucao-telemetria), o [ADR de showback do Lume](caso-lume.md#adr-lume-canary-por-agencia-sem-chargeback), o [ADR de chargeback antecipado da Aurora](caso-aurora.md#adr-aurora-escrita-suspensa-em-canary-chargeback-antecipado) e os [quatro planos de métricas](observabilidade.md#quatro-planos-de-metricas).

**Como conduzir**

1. Execute `telemetria_lume_aurora.py --caso lume` e `--caso aurora`, três repetições cada, registrando `TRACE_ID`, `DURACAO_MS` e o atributo `boreal.etapa` do span `conhecimento`.
2. Separe, para cada produto, o que a duração observada mede (consulta ao índice; consulta ao índice mais chamada de ferramenta, na operação real) do que ela não mede (custo real por token ou por chamada de ferramenta).
3. Compare a variação entre as três repetições de cada caso antes de tratar qualquer diferença isolada como conclusiva.
4. Ligue a evidência coletada a cada ADR: ela reforça, é neutra ou contradiz a decisão de showback do Lume e de chargeback antecipado da Aurora?

**Entrega esperada**

Entregue a tabela com três repetições por produto (`TRACE_ID`, `DURACAO_MS`, `boreal.etapa`) e um parecer de até 200 palavras ligando a evidência aos dois ADRs.

**Como verificar**

Confira repetição suficiente para distinguir variação de sinal, e a ligação explícita entre trace e ADR de cada produto.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Execução e registro | 25% | Roda os dois casos com repetições e registra `trace_id`, duração e etapa. |
| Composição da medida | 25% | Distingue o que a duração mede do que ela não prova sobre custo. |
| Variação | 20% | Não trata uma única execução como suficiente. |
| Ligação ao ADR | 30% | Conecta a evidência à decisão de showback do Lume e chargeback da Aurora. |

## Analisar

### 12. Diagnóstico de rollout composto

**O que é:** **canary** expõe versão; **fallback** usa alternativa; **rollback** restaura manifesto. Leia [entrega](entrega-e-recuperacao.md#avaliacao-continua-e-entrega-controlada) e [roteamento/fallback](entrega-e-recuperacao.md#roteamento-fallback-e-degradacao).

**Situação**

Um canary reduz custo por chamada em 25% e p95 em 15%, mas tarefas concluídas caem 6%, tokens por tarefa sobem, fundamentação piora em português e uma ferramenta dobra chamadas após timeout. O avaliador automático declara melhora geral.

**Seu papel**

Você separa economia técnica de valor e decide pausar, reverter, degradar ou ampliar.

**Insumos disponíveis**

Consulte os [quatro planos de métricas](observabilidade.md#quatro-planos-de-metricas), o [trace da oficina](oficina-de-ferramentas.md#receita-principal) e [canary, fallback e rollback](entrega-e-recuperacao.md#avaliacao-continua-e-entrega-controlada).

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

### 13. Promoção de degrau de um laço em operação

**Laboratório.** Antes de julgar o caso, produza a sua própria distribuição. Rode o [laço objetivado](oficina-de-ferramentas.md#extensao-loop-objetivado-com-orcamento) três vezes com condição de parada objetiva e uma vez com `--parada modelo`, e anote `PARADA`, `ITERACOES`, `TOKENS_TOTAIS` e `VERDADE_FINAL` de cada execução. Quatro execuções não formam uma distribuição, e é justamente essa insuficiência que o exercício usa: com quatro pontos, você já consegue dizer que a mediana não dimensiona um teto, e é essa a leitura que o caso abaixo exige.

```bash
python loop_objetivado.py
python loop_objetivado.py
python loop_objetivado.py
python loop_objetivado.py --parada modelo
```

**Situação:** um laço de nível 2 fecha, há oito semanas, chamados de baixa complexidade a partir de um roteiro determinístico. Os números da janela: 412 execuções, 78% terminando em `meta_atingida`, 22% em `orcamento_esgotado`, custo por objetivo concluído estável, mediana de três iterações e percentil 95 de sete. Duas execuções encerraram com sucesso declarado e reabertura do chamado pelo cliente em menos de 24 horas. A equipe propõe subir para o nível 3, com disparo a cada quinze minutos, e aumentar o teto de iterações de oito para vinte para reduzir a fatia de esgotamento.

**Como conduzir**

1. Confronte a execução `--parada modelo` do seu laboratório com as duas reaberturas do caso e diga que modo de falha as três compartilham.
2. Classifique as duas reaberturas: falha do modelo, falha do verificador ou falha do critério de sucesso, com a evidência que sustentaria cada leitura.
3. Avalie a proposta de aumentar o teto de iterações à luz da fatia de 22% e do percentil 95 observado. Use a dispersão das suas três execuções objetivas para argumentar por que um teto dimensionado pela mediana produz a fatia de esgotamento que a equipe quer eliminar.
4. Liste os controles que precisam existir antes da subida para o nível 3, e diga qual deles ainda não está evidenciado pelos números apresentados.
5. Defina os sinais que autorizariam a promoção e os que exigiriam rebaixamento imediato ao nível anterior.
6. Indique quem responde por cada teto, pelo desligamento e pela aceitação do risco residual.

**Entrega esperada:** as quatro linhas de execução do laboratório e um parecer de até uma página com decisão sobre a promoção, condições associadas e os limiares que disparam rebaixamento.

**Critérios de avaliação**

| Critério | Peso | Evidência |
|---|---:|---|
| Medição | 15% | Entrega as quatro execuções e usa a variação entre elas no argumento. |
| Diagnóstico | 25% | Separa falha de verificador de falha de critério e nomeia a evidência que distinguiria as duas. |
| Orçamento | 15% | Trata aumento de teto como hipótese a testar, não como correção da fatia de esgotamento. |
| Pré-requisitos do degrau | 25% | Exige idempotência, identidade própria e desligamento antes do disparo automático. |
| Reversibilidade | 10% | Define rebaixamento como ação operacional normal, com limiar. |
| Autoridade | 10% | Nomeia dono de cada teto e do risco residual. |

## Avaliar

### 14. Plataforma comum ou autonomia local?

**O que é:** **fronteira de propriedade** diz quem decide e aceita risco; **ADR** registra contexto e decisão. Consulte [promoção](pacote-e-promocao.md#ambientes-e-promocao) e [incrementos e ADRs](estudo-de-caso.md#incrementos-e-adrs).

**Situação**

A plataforma propõe gateway, registro de prompts, RAG, ferramentas e guardrails comuns. Atendimento quer streaming específico; Jurídico exige índice isolado; Compras precisa de executor transacional; FinOps quer atribuição de custo imediata.

**Seu papel**

Você decide o que é plataforma comum, específico ou adiado.

**Insumos disponíveis**

Consulte o [caso](estudo-de-caso.md) e a [plataforma corporativa](plataforma-corporativa.md).

**Como conduzir**

1. Separe capacidades comuns, específicas e adiadas com uma razão verificável.
2. Compare reuso, acoplamento, concentração de falha e portabilidade.
3. Explicite responsabilidades de plataforma, produto, segurança, operação e FinOps.
4. Compare hospedado, autogerido e composto para uma capacidade compartilhada.
5. Registre três ADRs, uma fitness function e um gatilho de revisão para cada decisão relevante.

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
| ADRs, fitness functions e gatilhos | 15% | Registra consequências, verificação contínua e condição de revisão. |

## Criar

### 15. Capstone — arquitetura e plano operacional da organização

**Situação**

Uma organização tem copiloto, RAG e agente isolados, duplicação, fornecedores incompatíveis, pouca rastreabilidade e custo crescente. Proponha arquitetura operável e reversível.

**O que é:** arquitetura operável é aquela em que mudança, decisão e recuperação têm dono.

**Seu papel**

Você fecha fronteiras de propriedade, contratos operacionais e decisões de liberação.

**Insumos disponíveis**

Use [pacote comportamental](pacote-e-promocao.md#o-objeto-operado-e-um-pacote-comportamental), [trace](observabilidade.md#trace-reconstruir-a-composicao), [SLO](observabilidade.md#slo-para-servico-util) e [exemplo](exemplo-arquitetural.md).

**Como conduzir**

**Campos:** ator = participante; proprietário = responsável; evidência = registro; portão = bloqueio; baseline = medida inicial; variável = mudança; parada = limite.

Fases e checkpoints:

1. **Fase 1 — Contexto:** preencha `atores | jornadas | dados | efeitos | restrições`. **Checkpoint:** usos proibidos.
2. **Fase 2 — Contratos:** preencha `componente | interface | proprietário | evidência`. **Checkpoint:** fluxos e fronteiras.
3. **Fase 3 — Entrega:** preencha `manifesto | critério | portão | canary | rollback | fitness function`. **Checkpoint:** promoção reversível.
4. **Fase 4 — Operação:** preencha `span | SLO | indicador | janela | alerta | runbook`. Declare prioridade e tensão entre segurança, privacidade, confiabilidade, latência, custo, auditabilidade e modificabilidade. **Checkpoint:** incidente reproduzível.
5. **Fase 5 — Evolução:** preencha `hipótese | baseline | variável | parada | decisão`. **Checkpoint:** roadmap incremental.

Preencha os onze artefatos:

Links: [referência](oficina-de-ferramentas.md#preparacao-do-laboratorio), [fatias](entrega-e-recuperacao.md#avaliacao-continua-e-entrega-controlada) e [quatro planos](observabilidade.md#quatro-planos-de-metricas).

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
12. fitness functions para manifesto, trace, bypass, fallback e ensaio de recuperação, com responsável e reação à falha.

Mostre propriedade, impacto e contenção de cada falha. No gateway, inclua réplicas, failover, bypass e degradação; não trate “humano no loop”, “monitoramento” ou “multimodelo” como garantia.

**Entrega esperada**

Entregue pacote com contexto, diagramas, manifesto, ADRs, critérios, portões, SLOs, traces, runbooks, riscos, experimentos e roadmap.

**Como verificar**

- Percorra uma mudança de corpus completa: versão, avaliação, promoção, trace, SLO, incidente e aprendizado.
- Percorra uma ação de usuário completa: identidade, gateway, política, ferramenta, aprovação, sistema externo e auditoria.
- Confira que cada fitness function possui limiar, responsável e reação diante da falha.
- Confira que cada SLO possui indicador, janela, meta, fonte, proprietário e runbook; que cada ADR possui alternativa e gatilho; e que cada risco residual possui autoridade e prazo.

**Critérios de avaliação**

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Contexto e qualidade | 12% | Delimita atores, jornadas, restrições e cenários mensuráveis. |
| Arquitetura e contratos | 12% | Define componentes, fronteiras, responsabilidades e interfaces. |
| Fluxos e ADRs | 12% | Fecha fluxos, equivalentes textuais, alternativas e consequências. |
| Guardrails e autoridade | 12% | Define controles, limites, proprietários e modo de falha. |
| Avaliação, portões e fitness functions | 12% | Usa fatias, casos, critérios, canary e condição verificável de bloqueio. |
| Operação e recuperação | 12% | Inclui SLOs, traces, alertas, rollback e degradação. |
| Privacidade e riscos residuais | 10% | Declara minimização, afetados, autoridade e gatilho. |
| Experimentos e roadmap | 10% | Define hipóteses refutáveis e incrementos reversíveis. |
| Propriedade e comunicação | 8% | Torna responsabilidades e decisões compreensíveis para os envolvidos. |

## Orientação para revisão entre pares

Faça uma trilha vertical da mudança de corpus ao incidente e outra horizontal da ação do usuário à auditoria. Procure saltos de responsabilidade, fallback que reduz segurança, métrica sem decisão e risco sem autoridade.

Feche o módulo com a [Síntese e referências](sintese-e-referencias.md).
