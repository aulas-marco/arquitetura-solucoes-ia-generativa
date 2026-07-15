# Padrões e decisões: liberar, recuperar e escalar

## Portões antes da exposição

Um **portão de regressão** compara o candidato com critérios e baseline versionados. Testes determinísticos cobrem schemas, autorização, citações, budgets e invariantes de ferramenta. Avaliação probabilística usa repetições, fatias e intervalos. Segurança inclui casos adversariais. Desempenho e custo são medidos com carga representativa. O portão registra pacote, conjunto, avaliador, resultado, exceção, aprovador e validade.

Portões não devem congelar melhoria. Um limiar absoluto protege o mínimo; um limite de não regressão impede piora relevante; uma revisão explícita trata trade-offs, como pequena perda de latência para grande ganho de segurança. Flakiness não é motivo para ignorar teste: separe variação esperada de infraestrutura instável e estime incerteza.

**Canary** expõe o candidato a uma fração delimitada de tráfego, usuários, tenants ou casos. A coorte precisa representar o risco e evitar pessoas vulneráveis sem consentimento ou proteção. Antes do início, defina duração, volume mínimo, métricas, limiares, autoridade para pausar e versão de retorno. Compare por fatia e mantenha atribuição: sem `release_id` no trace, misturam-se resultados. Atingir um critério de parada sempre interrompe a exposição, mas só abre incidente se houver impacto, guardrail crítico ou severidade definida; hipótese de produto rejeitada segue para diagnóstico normal.

Shadow traffic pode executar o candidato sem mostrar a saída nem realizar efeitos. É útil para latência e comparação, mas ainda processa dados e incorre em custo; ferramentas devem ser simuladas. A/B testa uma hipótese de produto quando ambas as variantes já são aceitáveis. Não se usa experimento para descobrir se uma variante viola um guardrail crítico.

## Roteamento, fallback e degradação

**Roteamento** escolhe modelo ou fluxo por classe de dado, risco, idioma, capacidade, latência, custo, região e saúde. A regra é determinística e versionada. Um classificador probabilístico pode fornecer sinal, mas decisões sensíveis recebem confirmação ou rota conservadora. A estratégia deve evitar loops e respeitar afinidade quando estado não é portável.

**Fallback** substitui uma dependência ou abordagem. Pode trocar modelo, usar busca sem geração, servir conteúdo aprovado, criar rascunho offline ou encaminhar a uma pessoa. Compatibilidade sintática não basta: o fallback deve manter identidade, política, classificação de dados, requisito de fundamentação e limites de ferramenta. Um modelo alternativo não aprovado para dados pessoais não é fallback válido para essa rota.

**Degradação** reduz capacidade de forma declarada. Se a recuperação falha, uma aplicação baseada em política não deve improvisar: informa indisponibilidade e oferece fonte oficial ou canal humano. Se a ferramenta de escrita está indisponível, mantém consulta e rascunho, mas não confirma ação. Se o guardrail crítico falha, bloqueia a rota afetada. A interface comunica o que não ocorreu.

**Rollback** restaura um manifesto conhecido: código, modelo/rota, prompt, política, índice e contratos compatíveis. Reverter apenas o prompt pode deixar o índice incompatível. Migrações de memória e efeitos externos exigem forward recovery, compensação ou reconciliação; não se “desfaz” um e-mail enviado com deployment anterior. Mantenha janela de compatibilidade e teste o procedimento.

## Incidente generativo

**Resposta a incidente** preserva a sequência: detectar, triar, conter, comunicar, erradicar, recuperar e aprender. Quando a classificação alcança impacto, guardrail crítico ou limiar de severidade, abre-se um identificador e congelam-se evidências minimizadas. A triagem delimita release, tenants, dados, ferramentas, período e possível efeito. Contenção pode desabilitar operação, remover fonte, reduzir tráfego, revogar credencial, fixar modelo ou encaminhar ao humano. Segurança, privacidade, jurídico e dono do processo participam conforme impacto.

Depois, reconstruir traces não autoriza expor conteúdo a todos. A recuperação valida o pacote e amplia gradualmente. O post-incident review evita caça a culpados e produz causas técnicas e organizacionais, riscos atualizados, testes de regressão, mudanças de runbook e responsáveis com prazo. Casos reais alimentam avaliação apenas após tratamento de dados e revisão para não perpetuar conteúdo malicioso.

Alertas precisam de ação. “Qualidade média caiu 1%” sem janela, fatia ou runbook gera fadiga. Prefira sinais compostos: aumento de abstenção numa rota após mudança de índice; custo por tarefa concluída acima do orçamento; ferramenta com duplicidade; divergência entre feedback e avaliador. Métricas sentinela detectam mudança do fornecedor mesmo sem release interno.

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

## Catálogo, identidade, tenancy e política

O **catálogo de modelos** registra fornecedor, revisão, capacidades, modalidades, regiões, classes de dados permitidas, contexto, limites, custo, avaliação, riscos, status e data de revisão. “Aprovado” sempre tem finalidade e condições. Catálogo sem reconciliação com tráfego real vira planilha; o gateway deve apontar uso não catalogado.

**Identidade** liga pessoa, serviço e workload à solicitação. A plataforma autentica e propaga contexto mínimo; o produto decide finalidade; o executor revalida autorização no recurso. Não coloque segredo no prompt. Para agentes, identidade delegada tem escopo, prazo e audiência menores que os do usuário ou da plataforma.

**Tenancy** isola configurações, dados, índices, quotas, chaves, telemetria e administração. O nível — lógico, por recurso ou físico — segue criticidade e obrigação. Testes negativos provam que um tenant não recupera, observa nem cobra o outro. Um `tenant_id` no log não corrige índice compartilhado sem filtro obrigatório.

**Política** como código torna regras executáveis e versionadas: modelos permitidos por classe, ferramentas por papel, retenção, regiões, budgets e aprovação. Decisões registram política e motivo. Regras precisam de dono e fluxo de exceção; uma engine central não interpreta automaticamente legitimidade ou nuance jurídica.

## Portabilidade e estratégia multimodelo

**Portabilidade** é graduada. Normalizar mensagens e respostas facilita troca; prompts, tool calling, embeddings, filtros, contexto, segurança e observabilidade continuam específicos. Defina quais capacidades precisam ser portáveis, tempo objetivo de saída, formato de exportação, testes de equivalência e custo aceitável. A abstração total pode impedir usar uma capacidade que cria valor.

Uma **estratégia multimodelo** pode buscar resiliência, adequação por tarefa, soberania ou negociação econômica. Cada modelo adicional multiplica avaliação, contrato, competência e modos de falha. “Temos dois fornecedores” não garante continuidade se ambos dependem da mesma região ou se o índice só funciona com um embedding. Modele dependências comuns e ensaie failover.

Registre ADR: contexto, alternativas, critérios, decisão, consequências e gatilhos de revisão. Evite escolher multimodelo por medo abstrato. Um único modelo com rota de saída testada pode ser melhor que três modelos mal avaliados.

## Modelo operacional da plataforma

A **equipe de plataforma** trata a capacidade como produto interno: gateway, contratos, catálogo, identidade técnica, telemetria, paved road, documentação, suporte, SLOs e evolução. Cada **equipe de produto** mantém jornada, dados do domínio, prompts específicos, avaliação ponta a ponta, risco residual e resultado de negócio. Segurança e privacidade definem requisitos e supervisionam risco; operações coordena confiabilidade e incidentes; FinOps fornece critérios econômicos; fornecedores respondem por compromissos contratados.

**Cotas** limitam tokens, requisições, concorrência, ferramentas e gasto por tenant, produto e classe. Devem reservar capacidade crítica e prever aumento aprovado. **Showback** mostra consumo e custo atribuído sem transferir contabilmente; educa e revela desperdício. **Chargeback** transfere custo à unidade consumidora e pode melhorar responsabilidade, mas incentiva subnotificação ou soluções paralelas se a regra parecer opaca. Comece com showback confiável, vincule custo a resultado e adote chargeback apenas com tags, contestação e tratamento de custos compartilhados.

Custos não se resumem ao token: incluem recuperação, armazenamento, observabilidade, avaliação, guardrails, pessoas, incidentes e capacidade ociosa. Otimizar centavos por chamada enquanto aumenta retrabalho é uma falsa economia.

Veja a composição desses padrões em [Exemplo arquitetural](exemplo-arquitetural.md).
