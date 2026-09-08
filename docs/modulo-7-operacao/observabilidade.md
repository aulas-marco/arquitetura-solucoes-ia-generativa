# Observabilidade e métricas

Observar uma solução generativa exige relacionar as fases de uma solicitação, escolher o que registrar sem acumular dados sensíveis e transformar sinais em decisões. Uma métrica só é operacionalmente útil quando declara **o evento contado, o denominador, a janela, as exclusões, as fatias, a fonte e a ação possível**.

Esta página separa quatro planos que não devem ser confundidos:

- **produto:** o usuário conseguiu realizar a tarefa?;
- **modelo:** a resposta ou decisão atingiu o critério de qualidade?;
- **operação:** o serviço respondeu dentro dos limites técnicos?;
- **negócio:** o resultado justificou custo e risco assumidos?

Uma única medida raramente responde às quatro perguntas. Latência menor não prova tarefa concluída; resposta aceita não prova factualidade; mais uso não prova valor.

## Rastreamento: reconstruir a composição {#trace-reconstruir-a-composicao}

Um **rastreamento distribuído** (*distributed trace*) conecta a solicitação às etapas de **instrução**, **contexto**, **recuperação**, **ferramenta** e **resposta**. Cada segmento (*span*) registra tempo, resultado, versão, política aplicada e relação causal.

Por padrão, o span de recuperação registra classificação, tamanho, identificador controlado ou hash e metadados de recuperação: índice, filtros de autorização, quantidade, latência e identificadores controlados dos documentos. A consulta derivada em texto bruto só pode aparecer em amostra explicitamente autorizada, segregada e com retenção limitada; não pertence à telemetria operacional padrão. O span de ferramenta registra contrato, operação, decisão de política, idempotência e estado; o de resposta registra validações e rota de entrega.

As [convenções semânticas do OpenTelemetry](https://opentelemetry.io/docs/specs/semconv/) oferecem um vocabulário oficial em evolução. As [convenções específicas de IA generativa](https://github.com/open-telemetry/semantic-conventions-genai) definem atributos para operação, modelo e consumo. Como ainda evoluem, a organização deve:

1. fixar a versão adotada;
2. mapear a convenção externa para um esquema interno estável;
3. testar migrações de nomes e unidades;
4. documentar campos opcionais habilitados;
5. impedir que cardinalidade e conteúdo sensível vazem para métricas.

**LiteLLM Proxy** concentra rotas; **OpenTelemetry** transporta telemetria. Ambos exigem identidade, minimização e retenção; um portal de modelos (*model gateway*) não substitui controle de domínio.

O rastreamento não deve guardar cadeia de pensamento privada como explicação. Registre entradas autorizadas, evidências, decisões externas e saídas necessárias. Justificativas de política vêm de regras auditáveis; texto do modelo sobre seu “raciocínio” não é prova causal.

## Antes de calcular: contrato da métrica

Cada métrica deve possuir uma ficha versionada:

- **nome e finalidade:** pergunta respondida e decisão apoiada;
- **evento elegível:** o que entra no denominador e quais exclusões são permitidas;
- **fórmula:** numerador, denominador, unidade, agregação e tratamento de valores ausentes;
- **janela:** intervalo móvel ou calendário e atraso de consolidação;
- **dimensões:** produto, jornada, idioma, cliente organizacional, versão, modelo e classe de risco;
- **fonte:** evento, rastreamento, avaliação, pesquisa ou sistema transacional autoritativo;
- **qualidade do dado:** cobertura, atraso, duplicidade, erro de classificação e retenção;
- **limites:** o que a medida não demonstra e quais fatores de confusão permanecem;
- **responsável e ação:** quem interpreta e qual decisão pode tomar.

Para uma taxa, use em geral `eventos que atendem ao critério / eventos elegíveis × 100`. O denominador é parte da definição: mudar “todas as solicitações” para “solicitações respondidas” muda a pergunta e pode esconder falhas.

Para distribuições de duração, custo ou consumo, reporte percentis, não apenas média. O percentil 95 (`p95`) é o menor valor que contém 95% das observações ordenadas na janela. Ele descreve cauda, mas não identifica causa; preserve o rastreamento para diagnóstico. O [livro de SRE do Google](https://sre.google/sre-book/service-level-objectives/) mostra por que médias podem ocultar degradação de cauda.

## Quatro planos de métricas

Métricas formam uma cadeia de hipóteses, não um placar único:

| Plano | Pergunta dominante | Decisão possível |
|---|---|---|
| **produto** | a jornada terminou com resultado útil? | corrigir experiência, escopo ou fluxo |
| **modelo** | a saída cumpriu critérios de qualidade e segurança? | trocar instrução, modelo, contexto ou avaliador |
| **operação** | o serviço respeitou capacidade, tempo, custo e confiabilidade? | escalar, conter, rotear, degradar ou reverter |
| **negócio** | o resultado produziu valor líquido e risco aceitável? | ampliar, redesenhar ou encerrar o caso |

Correlação não prova causa. Mais unidades de processamento (*tokens*) podem acompanhar melhor resolução porque casos difíceis são longos. Um experimento controlado, com métricas de proteção equivalentes, é necessário para estimar contribuição causal. “Dez mil respostas” mede atividade, não valor.

## Métricas de produto

As métricas de produto usam a jornada como unidade. Antes de calculá-las, defina o início, o fim, o prazo e o evento autoritativo de cada tarefa.

### Conclusão de tarefa

**O que mede.** Proporção de tarefas elegíveis que atingem um estado de sucesso verificável dentro da janela definida.

**Cálculo.** `tarefas com evento de sucesso / tarefas iniciadas elegíveis × 100`.

**Considerações.** O evento deve vir do sistema de negócio sempre que possível: pedido registrado, chamado encerrado sem reabertura, formulário aceito. “O modelo disse que concluiu” não é evidência suficiente. Separe conclusão autônoma, conclusão com intervenção e conclusão posteriormente desfeita.

### Abandono

**O que mede.** Proporção de jornadas iniciadas que não alcançam o próximo passo obrigatório ou o desfecho esperado dentro do prazo.

**Cálculo.** `(jornadas iniciadas − jornadas que alcançaram o marco) / jornadas iniciadas × 100`.

**Considerações.** Expiração de sessão, troca de canal e retomada posterior podem parecer abandono. Defina janela e identidade da jornada antes de contar. A [documentação oficial do Google Analytics](https://support.google.com/analytics/answer/13128171) ilustra o cálculo por transição de funil; a organização deve adaptar os eventos à sua jornada, não copiar a taxonomia de comércio eletrônico.

### Reconsulta

**O que mede.** Frequência com que o usuário reformula ou repete a mesma intenção após uma resposta.

**Cálculo.** `tarefas com nova consulta semanticamente equivalente em Δt / tarefas respondidas × 100`.

**Considerações.** Reconsulta pode indicar incompreensão, dado novo ou aprofundamento legítimo. A equivalência de intenção precisa de regra auditável — taxonomia humana, classificador validado ou amostra revisada — e deve ser segmentada por tipo de tarefa. Não use similaridade textual bruta como verdade.

### Aceitação

**O que mede.** Proporção de sugestões que provocam uma ação explícita de aceitar, aplicar ou inserir.

**Cálculo.** `sugestões aceitas / sugestões exibidas e elegíveis × 100`.

**Considerações.** Clique não prova correção, e ausência de clique não prova rejeição. Diferencie aceitação total, edição antes do uso, desfazer e aceitação automática. Compare também o resultado posterior, pois uma sugestão aceita pode gerar retrabalho.

### Escalonamento

**O que mede.** Proporção de jornadas transferidas para pessoa, processo especializado ou canal de maior autoridade.

**Cálculo.** `jornadas escalonadas / jornadas elegíveis × 100`.

**Considerações.** Escalonamento alto pode indicar baixa capacidade; baixo pode indicar automação indevida. Separe escalonamento solicitado pelo usuário, acionado por política, provocado por baixa confiança e ocorrido após falha. A [ISO 18295-1](https://www.iso.org/standard/64739.html) fornece um quadro de requisitos e indicadores para centros de contato, mas os limiares continuam dependentes do contexto.

### Feedback do usuário

**O que mede.** Julgamento explícito sobre uma interação ou jornada, por escala, categoria ou texto.

**Cálculo.** Para escala: `soma das notas válidas / número de respostas válidas`; para aprovação binária: `avaliações positivas / avaliações válidas × 100`. Sempre reporte também taxa de resposta: `respondentes / pessoas convidadas × 100`.

**Considerações.** Feedback sofre viés de seleção, extremos e formulação da pergunta. Não misture escalas ou versões de questionário. O [American Customer Satisfaction Index](https://theacsi.org/wp-content/uploads/2024/05/24jun-telecom-study-FINAL.pdf) ilustra uma metodologia que combina amostragem e modelo de satisfação; uma média informal de “curtidas” não é equivalente a esse índice.

## Métricas de modelo

Métricas de modelo avaliam saídas contra critérios. As [práticas de avaliações da OpenAI](https://developers.openai.com/api/docs/guides/evals) recomendam formalizar critérios, dados e avaliadores; o [perfil de IA generativa do NIST](https://doi.org/10.6028/NIST.AI.600-1) enquadra medição como parte da gestão de risco ao longo do ciclo de vida.

Para métricas julgadas por pessoas ou por outro modelo, registre:

- critérios e exemplos de cada nível;
- população, método de amostragem e tamanho da amostra;
- versão do avaliador e configuração;
- revisão humana de calibração;
- concordância entre avaliadores;
- intervalo de confiança e fatias críticas.

### Factualidade

**O que mede.** Proporção de afirmações verificáveis sustentadas pelo estado do mundo ou por uma fonte autoritativa definida.

**Cálculo.** `afirmações verificáveis corretas / afirmações verificáveis avaliadas × 100`. Outra opção é a taxa por resposta: `respostas sem erro factual / respostas avaliadas × 100`; não misture as duas unidades.

**Considerações.** Decompor resposta em afirmações é parte do protocolo. Declare tratamento de afirmações não verificáveis, informação desatualizada e divergência entre fontes. Um avaliador automático deve ser calibrado contra amostra humana e não pode avaliar com conhecimento menos atual que a fonte exigida.

### Fundamentação

**O que mede.** Quanto das afirmações relevantes pode ser inferido das evidências fornecidas ao sistema, independentemente de ser verdadeiro no mundo.

**Cálculo.** `afirmações relevantes apoiadas pelas evidências / afirmações relevantes avaliadas × 100`, ou média de critérios ordinais versionados.

**Considerações.** Factualidade e fundamentação são diferentes: uma frase pode ser verdadeira, mas não estar apoiada no contexto recuperado. Verifique também se a citação aponta para o trecho correto e se o usuário tinha autorização para essa evidência.

### Recusa adequada

**O que mede.** Capacidade de recusar quando deve e responder quando pode.

**Cálculo.** Mantenha duas taxas: `recusas corretas / casos que exigem recusa × 100` e `respostas corretas / casos permitidos × 100`. Na linguagem de classificação, correspondem à sensibilidade da recusa e à especificidade; uma única “taxa de recusa” oculta o compromisso entre ambas.

**Considerações.** O conjunto precisa conter casos permitidos, proibidos e ambíguos por fatia. Recusa excessiva prejudica utilidade; recusa insuficiente amplia risco. Pese severidade, não apenas quantidade.

### Aderência ao esquema

**O que mede.** Proporção de saídas estruturadas que validam contra contrato sintático e regras semânticas.

**Cálculo.** `saídas válidas sem reparo / saídas estruturadas elegíveis × 100`. Reporte separadamente `saídas válidas após reparo / saídas elegíveis × 100`.

**Considerações.** JSON bem formado pode violar regra de negócio. Valide tipos, campos obrigatórios, enumerações, limites e referências. Reparos mascaram falhas do modelo e acrescentam latência; registre sua taxa e versão.

### Segurança por fatia

**O que mede.** Frequência e severidade de violações de política em grupos de casos relevantes: idioma, domínio, classe de dado, perfil de usuário ou tipo de ataque.

**Cálculo.** `casos com violação / casos avaliados na fatia × 100`, acompanhado por severidade e limite superior do intervalo de confiança.

**Considerações.** Média global pode esconder uma fatia rara e crítica. Conjuntos adversariais não representam prevalência de produção, mas testam resistência. O [NIST AI 600-1](https://doi.org/10.6028/NIST.AI.600-1) recomenda medir e gerir riscos específicos de IA generativa; não converta riscos incompatíveis em uma nota única.

## Métricas de operação

O [capítulo de monitoramento do Google SRE](https://sre.google/sre-book/monitoring-distributed-systems/) organiza operação em latência, tráfego, erros e saturação. Para IA generativa, acrescente consumo e custo, mantendo distinção entre chamada de modelo, trajetória completa e resultado útil.

### Disponibilidade útil

**O que mede.** Proporção de solicitações elegíveis que recebem um desfecho tecnicamente válido e útil segundo o contrato do produto.

**Cálculo.** `solicitações bem-sucedidas / solicitações elegíveis × 100`.

**Considerações.** HTTP 200 não basta: resposta sem fonte obrigatória, ferramenta duplicada ou saída inválida é falha implícita. Declare exclusões, como tráfego sintético e solicitações rejeitadas antes da admissão. Separe indisponibilidade do provedor, da aplicação e do domínio.

### Latência total e tempo até o primeiro token

**O que mede.** Latência total mede do recebimento ao desfecho; **tempo até o primeiro token** (*time to first token*, TTFT) mede até o início perceptível da resposta transmitida.

**Cálculo.** Por requisição: `t_fim − t_início` e `t_primeiro_token − t_início`. Agregue em histogramas e reporte `p50`, `p95` e `p99` por rota e resultado.

**Considerações.** Separe sucesso e erro: erro rápido não melhora experiência. Em agentes, meça também recuperação, inferência, ferramentas e fila. O OpenTelemetry recomenda histogramas de duração e convenção de nome `{operação}.duration`; consulte as [regras oficiais de nomenclatura](https://opentelemetry.io/docs/specs/semconv/general/naming/).

### Consumo de tokens

**O que mede.** Unidades processadas na entrada e produzidas na saída por chamada, tarefa ou resultado.

**Cálculo.** `tokens_totais = tokens_entrada + tokens_saída`; para eficiência, `tokens_totais / tarefas concluídas`. Registre separadamente itens recuperados do cache quando o provedor os diferencia.

**Considerações.** Tokenização varia entre modelos; não compare contagens como se fossem caracteres. Raciocínio interno faturável, cache e multimodalidade podem ter regras próprias. As [convenções GenAI do OpenTelemetry](https://github.com/open-telemetry/semantic-conventions-genai) definem atributos de entrada e saída e orientam usar os totais fornecidos pelo provedor quando disponíveis.

### Taxa de erros

**O que mede.** Proporção de operações que falham explicitamente, implicitamente ou por violar o objetivo de serviço.

**Cálculo.** `operações com erro / operações elegíveis × 100`, por classe: transporte, limite, provedor, validação, política, ferramenta, tempo excedido e conteúdo incorreto.

**Considerações.** Uma única taxa mistura causas e severidades. Conte repetição final e tentativas intermediárias separadamente. O Google SRE inclui erros explícitos, implícitos e por política entre os [quatro sinais dourados](https://sre.google/sre-book/monitoring-distributed-systems/).

### Saturação

**O que mede.** Quão próximo o recurso limitante está da capacidade segura.

**Cálculo.** `uso observado / capacidade segura × 100`, aplicado ao recurso dominante: concorrência, cota do provedor, conexões, memória, CPU ou trabalhadores de fila.

**Considerações.** Capacidade segura pode ser inferior a 100% físico. Identifique o primeiro recurso que degrada latência ou erros e valide o limite por ensaio de carga. Saturação é previsão de esgotamento, não só leitura instantânea.

### Fila

**O que mede.** Trabalho aguardando execução e tempo gasto antes do processamento.

**Cálculo.** Registre `comprimento_da_fila` como calibre e `tempo_de_espera = t_início_processamento − t_entrada_fila` como distribuição. Compare taxa de chegada `λ` e taxa de serviço `μ`.

**Considerações.** Fila absorve rajadas, mas pode esconder sobrecarga e consumir todo o orçamento de latência. Separe por prioridade e idade. O capítulo do Google SRE sobre [falhas em cascata](https://sre.google/sre-book/addressing-cascading-failures/) mostra que filas longas aumentam latência e que rejeição antecipada pode ser mais segura.

### Novas tentativas

**O que mede.** Amplificação criada por repetição de chamadas após falha ou tempo excedido.

**Cálculo.** `tentativas totais / operações lógicas` produz o fator de amplificação; `operações com ao menos uma nova tentativa / operações lógicas × 100` produz a taxa de repetição.

**Considerações.** Meça no nível lógico para não chamar cada tentativa de nova solicitação. Registre motivo, atraso, limite e sucesso posterior. Repetição sem idempotência pode duplicar efeitos; sem recuo (*backoff*) e aleatoriedade, pode agravar saturação.

### Custo

**O que mede.** Despesa atribuível à chamada, tarefa, produto ou resultado, incluindo componentes compartilhados relevantes.

**Cálculo.** Uma aproximação por chamada é `tokens_entrada × preço_entrada + tokens_saída × preço_saída + chamadas_de_ferramenta + recuperação + infraestrutura`. Para decisão: `custo total elegível / resultados concluídos`.

**Considerações.** Preços variam por modelo, região, cache, lote e data; versione a tabela usada. Custo por chamada favorece respostas curtas que podem não resolver a tarefa. Inclua repetição, avaliação, armazenamento, observabilidade e operação humana quando material.

## Métricas de negócio

Métricas de negócio exigem fonte transacional, janela de maturação e, quando a pergunta for causal, um contrafactual. Não atribua toda mudança observada ao sistema generativo.

### Tempo poupado validado

**O que mede.** Diferença de esforço humano para resultados equivalentes.

**Cálculo.** `tempo mediano do grupo comparável sem assistência − tempo mediano com assistência`, multiplicado pelo volume apenas quando população e período forem compatíveis.

**Considerações.** Inclua revisão, correção e retrabalho. Autorrelato pode complementar, não substituir, eventos observados. Mudanças de complexidade, treinamento e seleção de participantes exigem grupo de comparação ou desenho quase experimental.

### Resolução

**O que mede.** Proporção de casos cujo problema foi efetivamente resolvido segundo regra do domínio.

**Cálculo.** `casos resolvidos sem reabertura em Δt / casos elegíveis × 100`.

**Considerações.** Defina resolução no sistema autoritativo e uma janela de reabertura. Separe resolução no primeiro contato, transferência e resolução posterior. A [ISO 18295-1](https://www.iso.org/standard/64739.html) contextualiza indicadores de desempenho para centros de contato.

### Receita incremental

**O que mede.** Receita adicional atribuível à intervenção em comparação com um contrafactual.

**Cálculo.** Em experimento: `(receita média por unidade no tratamento − receita média por unidade no controle) × unidades tratadas`.

**Considerações.** Receita observada depois da implantação não é automaticamente incremental. Controle sazonalidade, preço, campanhas e seleção. Verifique também margem, cancelamento e métricas de proteção; aumentar conversão com recomendações inadequadas não é ganho sustentável.

### Perda evitada

**O que mede.** Valor esperado de eventos adversos prevenidos.

**Cálculo.** `Σ[(probabilidade_base − probabilidade_residual) × impacto financeiro] − custo do controle`.

**Considerações.** É uma estimativa, não receita realizada. Registre origem das probabilidades, incerteza, severidade e dependências. Não agregue eventos incompatíveis sem explicitar pesos. Faça análise de sensibilidade.

### Satisfação

**O que mede.** Percepção declarada do usuário sobre a jornada ou serviço.

**Cálculo.** Use média de escala ou proporção de respostas favoráveis, sempre com taxa de resposta, distribuição e intervalo de confiança. Não chame qualquer nota de NPS ou ACSI sem seguir a metodologia correspondente.

**Considerações.** Satisfação pode subir enquanto correção cai. Controle formulação, momento da pesquisa, canal, não resposta e repetição por pessoa. A metodologia do [ACSI](https://theacsi.org/wp-content/uploads/2024/05/24jun-telecom-study-FINAL.pdf) demonstra que um índice formal exige amostragem e modelagem explícitas.

### Risco observado e exposição ao risco

**O que mede.** Frequência e impacto de eventos adversos, quase-incidentes e violações de limite.

**Cálculo.** Para frequência: `eventos adversos / unidades de exposição`; para perda esperada: `Σ(probabilidade × impacto)`. Reporte separadamente eventos intoleráveis, mesmo quando raros.

**Considerações.** Ausência observada não prova risco zero, especialmente em baixa frequência. Use limite superior de confiança, cenários adversariais e indicadores antecedentes. O [NIST AI RMF](https://doi.org/10.6028/NIST.AI.100-1) organiza a prática em governar, mapear, medir e gerir; risco residual requer autoridade explícita.

### Custo por resultado

**O que mede.** Eficiência econômica ponta a ponta para produzir o desfecho de negócio definido.

**Cálculo.** `(modelo + recuperação + ferramentas + infraestrutura + avaliação + operação humana + retrabalho) / resultados válidos`.

**Considerações.** Use o mesmo conceito de resultado no numerador operacional e no denominador de negócio. Diferencie custo marginal e custo total. Uma solução barata por chamada pode ser cara por resolução se exigir muitas tentativas ou revisão humana.

## Logs com preservação de privacidade

**Logs com preservação de privacidade** aplicam minimização antes da coleta. Por padrão, registre:

- identificadores pseudonimizados;
- tamanhos, tempos e versões;
- categorias e decisões de política;
- hashes controlados;
- métricas e códigos de resultado.

Mascare campos sensíveis antes do coletor; separe telemetria operacional de conteúdo para avaliação; criptografe e controle acesso; defina retenção por classe; audite consultas; descarte também exportações e cópias de segurança.

Amostras de instrução ou resposta exigem base, finalidade, seleção, acesso e prazo explícitos. A amostragem (*sampling*) deve ser estratificada para não esconder grupos raros, mas nenhum objetivo analítico justifica coleta indiscriminada. Hashes de texto previsível podem permitir reidentificação; use técnicas e chaves adequadas ao risco. Em incidente, acesso excepcional tem aprovação e trilha.

## SLO para serviço útil

Um **objetivo de nível de serviço** (*service level objective*, SLO) define uma meta sobre um **indicador de nível de serviço** (*service level indicator*, SLI) em uma janela. O [capítulo oficial de SLOs do Google SRE](https://sre.google/sre-book/service-level-objectives/) orienta escolher poucos indicadores relevantes ao usuário; o [SRE Workbook](https://sre.google/workbook/implementing-slos/) detalha a implementação.

Para IA generativa, disponibilidade HTTP é necessária, porém insuficiente. Uma resposta 200 sem fonte obrigatória ou uma ação duplicada não é sucesso.

### Exemplo calculado

Considere o SLO: “99% das consultas elegíveis em 28 dias recebem resposta validada em até 8 segundos”.

1. **Eventos elegíveis:** 120.000 consultas admitidas; tráfego sintético e solicitações rejeitadas por política ficam fora.
2. **Eventos bons:** 118.500 terminaram em até 8 segundos com esquema válido e fonte quando obrigatória.
3. **SLI:** `118.500 / 120.000 × 100 = 98,75%`.
4. **Meta:** 99%; logo, o SLO não foi atendido.
5. **Orçamento de erro:** `120.000 × (1 − 0,99) = 1.200` eventos não bons permitidos.
6. **Consumo:** `120.000 − 118.500 = 1.500`; foram consumidos 125% do orçamento, excedendo-o em 300 eventos.

Outros exemplos úteis:

- “99,9% das ações confirmadas não produzem duplicidade”;
- “95% das respostas amostradas sobre políticas vigentes atingem fundamentação 3 ou 4”;
- “95% das tarefas elegíveis começam a transmitir resposta em até 1,5 segundo”.

O primeiro pode ser observado continuamente; o segundo depende de amostragem e julgamento, portanto deve declarar atraso e incerteza. O orçamento de erro orienta ritmo de mudança, mas não compra permissão para eventos intoleráveis. Vazamento de dado sensível ou ação fora de autoridade aciona incidente mesmo se a média do SLO estiver dentro da meta. SLO, métrica de proteção e risco residual são instrumentos complementares.

## Como montar um painel que leve a decisões

Um painel mínimo não deve colocar todas as métricas no mesmo nível. Organize-o por pergunta:

1. **o usuário está conseguindo?** conclusão, abandono, reconsulta e escalonamento;
2. **a saída está correta e segura?** factualidade, fundamentação, recusa e violações por fatia;
3. **o serviço está saudável?** disponibilidade útil, p95, TTFT, erros, fila, saturação e custo;
4. **o caso continua justificável?** resolução, tempo poupado, risco e custo por resultado.

Cada visualização deve mostrar versão da liberação, janela, população, fatias críticas e mudança conhecida. Alertas precisam indicar responsável e ação. Uma variação sem hipótese, limiar ou procedimento operacional (*runbook*) pertence à análise, não ao plantão.
