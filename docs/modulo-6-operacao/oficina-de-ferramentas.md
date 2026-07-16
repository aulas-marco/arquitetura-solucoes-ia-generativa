# Oficina de ferramentas — operar uma capacidade compartilhada

**Objetivo Bloom:** Analisar.

Esta oficina usa sinais sintéticos para decidir como uma capacidade generativa compartilhada deve proteger produtos diferentes. Ela não acessa produção, não configura gateway real e não infere causalidade a partir de um único trace.

## Decisão arquitetural em foco

Gateway, quotas, roteamento e SLOs são controles de plataforma que precisam ser traduzidos em responsabilidade por produto e ações recuperáveis. A **atividade guiada** relaciona métricas a uma hipótese operacional, em vez de tratar dashboard ou fornecedor como decisão arquitetural. Consulte o [Guia de ferramentas e plataformas](../referencia/guia-de-ferramentas.md) ao escolher uma rota: a observação deve manter dados minimizados e limites explícitos.

## Roteiros equivalentes de acesso

### Essencial, sem cartão

Analise os traces e métricas sintéticas desta página em uma tabela, planilha ou arquivo local. Formule o parecer operacional sem conectar serviço algum. Esta rota não depende de cartão, conta, chave de API, credencial ou chamada remota e produz toda a evidência obrigatória.

### Institucional

Se existir acesso previamente autorizado, observe um dashboard ou gateway institucional sem executar mudança e sem copiar conteúdo sensível. Compare apenas os sinais necessários com os artefatos sintéticos e registre a mesma recomendação. A rota institucional não acrescenta pontos; ela apenas oferece outro ambiente de observação.

### Comercial ou avançada

Opcionalmente, use dashboard, gateway ou plataforma comercial autorizada para visualizar os mesmos indicadores sintéticos. Declare conta, retenção, custo, limite e qualquer dado que deixaria a fronteira local. A rota comercial ou avançada não acrescenta pontos e não é necessária para o parecer operacional.

## Atividade guiada

A atividade obrigatória é a rota **Essencial, sem cartão**; ela não depende de cartão. Considere o recorte sintético de 15 minutos da capacidade compartilhada Boreal.

| Produto | Trace/indicador sintético | Qualidade | Custo por solicitação | p95 de latência | Falhas | Uso no período |
|---|---|---:|---:|---:|---:|---:|
| Copiloto de suporte | `tr-201`, recuperação versionada | 0,91 | R$ 0,08 | 1,8 s | 0,4% | 1.200 |
| Resumo interno | `tr-202`, contexto acima do alvo | 0,86 | R$ 0,42 | 3,9 s | 0,8% | 430 |
| Assistente de pedidos | `tr-203`, timeout no provedor | 0,93 | R$ 0,11 | 7,4 s | 5,6% | 860 |
| Laboratório | `tr-204`, picos de tentativas | 0,72 | R$ 0,61 | 2,2 s | 1,1% | 2.900 |

**Hipóteses de trabalho:** o SLO do Assistente de pedidos é p95 até 4 s e falha abaixo de 2%; o Resumo interno tem orçamento de R$ 0,25 por solicitação; o Laboratório não pode consumir mais de 20% da quota diária da capacidade; respostas com qualidade abaixo de 0,80 não seguem para ação.

1. Identifique uma hipótese para cada sinal preocupante. Diferencie sintoma, métrica, limiar e possível causa; os dados não provam a causa sozinhos.
2. Recomende uma configuração de **gateway**, **quota** e **roteamento** para os quatro produtos. Inclua ao menos uma prioridade por produto, uma proteção contra explosão de custo e uma regra de preservação de qualidade.
3. Defina um SLO ou orçamento operacional com métrica, limiar e proprietário. Para um desvio, escolha uma ação de recuperação: fallback aprovado, redução de contexto, fila, rollback, degradação segura ou escalonamento de incidente.
4. Registre que trace ou amostra adicional, com metadados minimizados, seria necessário para confirmar a hipótese antes de mudar produção.

A decisão arquitetural em discussão é: **como uma plataforma compartilhada aplica controles comuns sem apagar o dono, o objetivo e a recuperação de cada produto?** A evidência é um parecer operacional, não a configuração efetiva de um gateway.

## Evidência a entregar

Entregue o parecer operacional da atividade e declare que os dados são sintéticos, a rota escolhida e qualquer instalação, limite, consumo local ou custo potencial. Cada recomendação deve ter hipótese, métrica, limiar, proprietário e ação.

| Produto ou capacidade | Hipótese | Métrica e limiar | Proprietário | Gateway, quota ou roteamento recomendado | Ação de recuperação |
|---|---|---|---|---|---|
| Copiloto de suporte |  |  |  |  |  |
| Resumo interno |  |  |  |  |  |
| Assistente de pedidos |  |  |  |  |  |
| Laboratório |  |  |  |  |  |

Conclua em até cinco linhas qual decisão deve ser reversível primeiro e qual condição transforma uma parada segura em incidente. Explique como a quota evita que a conveniência de um produto prejudique os demais.

## Segurança e custo

A decisão arquitetural é controlar uma capacidade compartilhada com observabilidade proporcional, não maximizar chamadas ou centralizar responsabilidade. Use somente os traces e métricas sintéticas; não exponha identificadores reais, prompts, respostas, URLs privadas, topologias, tokens, credenciais ou dados de telemetria de produção.

Uma planilha ou ferramenta local pode consumir CPU, memória, disco e energia; dashboards e gateways institucionais ou comerciais podem reter dados, impor limites e gerar cobrança. Registre essas condições na evidência da atividade. Se um dashboard não estiver disponível, use a tabela sintética e produza o mesmo parecer: a rota essencial continua possível sem cartão e sem alteração externa.
