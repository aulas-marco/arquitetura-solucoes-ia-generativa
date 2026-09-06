# Plataforma corporativa

O que vale padronizar para várias equipes, o que precisa continuar no domínio e o que uma plataforma comum não decide por ninguém.

## Model gateway como fronteira comum

Um **model gateway** centraliza autenticação, autorização, roteamento, limites, normalização de APIs, registro de versões, medição, redaction e políticas transversais. Ele reduz credenciais espalhadas e cria um ponto consistente de controle. Também pode virar gargalo, ponto único de falha e interface pelo menor denominador comum.

O gateway não deve interpretar regra profunda do domínio nem ocultar capacidades importantes. Réplicas ativas ou em espera ocupam **domínios de falha** distintos; uma entrada com health check faz failover entre regiões. Catálogo, política e configuração assinada precisam estar disponíveis na réplica, e o ensaio deve incluir perda regional e dependências comuns. Circuit breaker por rota e quotas por produto limitam o **raio de impacto**.

Bypass é contingência limitada, não acesso direto improvisado ao provedor. Só existe quando previamente autorizado e testado, por **prazo curto**, com proprietário e desligamento, e preserva **controles equivalentes** de identidade, quotas, política, guardrails e telemetria. Se isso não for seguro, cada produto degrada: o copiloto informa indisponibilidade ou encaminha; o RAG oferece **busca oficial** sem geração; o agente **suspende escrita** e mantém apenas consulta permitida. Assim, falha do gateway não se converte em remoção coletiva de controles.

## Serviços compartilhados, com fronteiras explícitas

Um **serviço compartilhado de prompts** oferece registro imutável, templates tipados, variáveis autorizadas, revisão, experimentos e promoção. Ele não deve permitir que qualquer produto edite um prompt global sem análise de impacto.

Um **serviço compartilhado de RAG** pode prover ingestão, parsing, embeddings, índices, recuperação e proveniência. Tenancy, classificação, filtro de autorização e snapshot precisam atravessar a interface. Uma única coleção com filtro opcional é um risco estrutural. Domínios preservam curadoria, regras de vigência e qualidade de fonte.

Um **serviço compartilhado de ferramentas** mantém catálogo, contratos, identidade delegada, política externa, idempotência, budgets e auditoria. A descrição consumida pelo modelo é interface de descoberta, não autorização. Adaptadores isolam APIs corporativas, mas não convertem uma operação irreversível em segura.

Um **serviço compartilhado de guardrails** entrega detectores, políticas, validação e decisão. Ele versiona configuração e mede falsos positivos por idioma e produto. Guardrail transversal cobre regras comuns; produto permanece responsável por dano e exceções do contexto. Dependência indisponível deve ter comportamento fail-closed ou degradação definido por rota.

Serviços comuns promovem **reuso**, mas aumentam **acoplamento** operacional e semântico. Extraia apenas capacidades com vários consumidores, contrato relativamente estável e equipe mantenedora. Duplicação temporária pode ser mais barata que uma abstração prematura; duplicação de identidade, auditoria ou controle de custo costuma ser mais perigosa.

## Mecanismos de plataforma e decisões de domínio

Gateway, catálogo, telemetria, avaliação, identidade técnica e guardrails comuns oferecem **mecanismos**: aplicam contratos, registram evidência e limitam caminhos. Eles não decidem finalidade, qualidade suficiente, regra de negócio, exceção contextual ou aceitação de risco residual. Produto e domínio continuam responsáveis por essas decisões; Segurança, Privacidade e Operação mantêm autoridades próprias. Essa divisão evita que uma plataforma comum se torne uma camada central que concentra tecnologia e autoridade indevidamente.

## Catálogo, identidade, tenancy e política

O **catálogo de modelos** registra fornecedor, revisão, capacidades, modalidades, regiões, classes de dados permitidas, contexto, limites, custo, avaliação, riscos, status e data de revisão. “Aprovado” sempre tem finalidade e condições. Catálogo sem reconciliação com tráfego real vira planilha; o gateway deve apontar uso não catalogado.

**Identidade** liga pessoa, serviço e workload à solicitação. A plataforma autentica e propaga contexto mínimo; o produto decide finalidade; o executor revalida autorização no recurso. Não coloque segredo no prompt. Para agentes, identidade delegada tem escopo, prazo e audiência menores que os do usuário ou da plataforma.

**Tenancy** isola configurações, dados, índices, quotas, chaves, telemetria e administração. O nível — lógico, por recurso ou físico — segue criticidade e obrigação. Testes negativos provam que um tenant não recupera, observa nem cobra o outro. Um `tenant_id` no log não corrige índice compartilhado sem filtro obrigatório.

**Política** como código torna regras executáveis e versionadas: modelos permitidos por classe, ferramentas por papel, retenção, regiões, budgets e aprovação. Decisões registram política e motivo. Regras precisam de dono e fluxo de exceção; uma engine central não interpreta automaticamente legitimidade ou nuance jurídica.

## Portabilidade e estratégia multimodelo

**Portabilidade** é graduada. Normalizar mensagens e respostas facilita troca; prompts, tool calling, embeddings, filtros, contexto, segurança e observabilidade continuam específicos. Defina quais capacidades precisam ser portáveis, tempo objetivo de saída, formato de exportação, testes de equivalência e custo aceitável. A abstração total pode impedir usar uma capacidade que cria valor.

Uma **estratégia multimodelo** pode buscar resiliência, adequação por tarefa, soberania ou negociação econômica. Cada modelo adicional multiplica avaliação, contrato, competência e modos de falha. “Temos dois fornecedores” não garante continuidade se ambos dependem da mesma região ou se o índice só funciona com um embedding. Modele dependências comuns e ensaie failover.

Registre ADR: contexto, alternativas, critérios, decisão, consequências e gatilhos de revisão. Evite escolher multimodelo por medo abstrato. Um único modelo com rota de saída testada pode ser melhor que três modelos mal avaliados.

## Obtenção de capacidade de plataforma

Gateway, telemetria, avaliação, armazenamento de traces e execução podem ser hospedados, autogeridos ou compostos. Serviço hospedado acelera capacidade, mas cria fronteiras de dados, versões, disponibilidade, portabilidade e resposta a incidente; operação autogerida amplia controle e assume escala, atualização, segurança e plantão. **Construir** se justifica para política, integração ou contrato que diferencia o domínio; **comprar** atende capacidade padronizada; **compor** combina serviços especializados com identidade, política e evidência corporativas. Compare custo total, tempo objetivo de saída, dependências comuns, evidência de recuperação e responsabilidades contratuais antes de delegar uma capacidade.

## Modelo operacional da plataforma

A **equipe de plataforma** trata a capacidade como produto interno: gateway, contratos, catálogo, identidade técnica, telemetria, paved road, documentação, suporte, SLOs e evolução. Cada **equipe de produto** mantém jornada, dados do domínio, prompts específicos, avaliação ponta a ponta, risco residual e resultado de negócio. Segurança e privacidade definem requisitos e supervisionam risco; operações coordena confiabilidade e incidentes; FinOps fornece critérios econômicos; fornecedores respondem por compromissos contratados.

**Cotas** limitam tokens, requisições, concorrência, ferramentas e gasto por tenant, produto e classe. Devem reservar capacidade crítica e prever aumento aprovado. **Showback** mostra consumo e custo atribuído sem transferir contabilmente; educa e revela desperdício. **Chargeback** transfere custo à unidade consumidora e pode melhorar responsabilidade, mas incentiva subnotificação ou soluções paralelas se a regra parecer opaca. Comece com showback confiável, vincule custo a resultado e adote chargeback apenas com tags, contestação e tratamento de custos compartilhados.

Custos não se resumem ao token: incluem recuperação, armazenamento, observabilidade, avaliação, guardrails, pessoas, incidentes e capacidade ociosa. Otimizar centavos por chamada enquanto aumenta retrabalho é uma falsa economia.

Veja a composição desses padrões em [Exemplo arquitetural](exemplo-arquitetural.md).

## Ferramentas no mercado

Veja comparações no [Guia de ferramentas](../referencia/guia-de-ferramentas.md).

| Ferramenta | Quando ajuda | Pré-requisito | Limite arquitetural |
|---|---|---|---|
| LiteLLM Proxy | Centralizar rotas e limites. | Provedores, identidade, segredos e fallback. | Não remove custo ou valida produto. |
| OpenTelemetry | Correlacionar sinais. | Convenções, coletor e retenção. | Não substitui investigação. |
| Langfuse | Acompanhar liberação. | Instrumentação e acesso controlado. | Não define SLO ou incidente. |

