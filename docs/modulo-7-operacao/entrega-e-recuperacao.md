# Entrega e recuperação

Transformar evidência em exposição gradual, e ter definido de antemão o que acontece quando a exposição dá errado.

## Avaliação contínua e entrega controlada

**Avaliação contínua** reutiliza o framework do Módulo 6 ao longo do ciclo. Antes da integração, testes locais verificam schemas e regras determinísticas. No pull request, um subconjunto rápido detecta regressões conhecidas. Na homologação, o conjunto completo mede factualidade, relevância, fundamentação, segurança, utilidade, latência e custo por fatia. Em produção, canary e amostragem detectam mudança de distribuição, novas intenções e falhas de componentes. Periodicamente, casos de incidentes e feedback autorizado voltam ao conjunto.

Um resultado não passa apenas porque a média subiu. Critérios intoleráveis — vazamento, ação sem autorização, ausência de escalonamento obrigatório — bloqueiam. Métricas negociáveis usam faixa, orçamento e comparação com a versão vigente. Mudança no avaliador também é versão comportamental: deve ser calibrada contra julgamento humano e não pode redefinir retroativamente o sucesso sem explicação.

**Entrega controlada** transforma evidência em exposição gradual. O pacote aprovado entra em canary para uma parcela delimitada, com critérios de continuação e interrupção definidos antes. Só então amplia. Liberação e mudança de configuração compartilham trilha. A velocidade sustentável vem de automatizar evidências repetíveis, não de dispensar decisão.

## Roteamento, fallback e degradação

**Roteamento** escolhe modelo ou fluxo por classe de dado, risco, idioma, capacidade, latência, custo, região e saúde. A regra é determinística e versionada. Um classificador probabilístico pode fornecer sinal, mas decisões sensíveis recebem confirmação ou rota conservadora. A estratégia deve evitar loops e respeitar afinidade quando estado não é portável.

**Fallback** substitui uma dependência ou abordagem. Pode trocar modelo, usar busca sem geração, servir conteúdo aprovado, criar rascunho offline ou encaminhar a uma pessoa. Compatibilidade sintática não basta: o fallback deve manter identidade, política, classificação de dados, requisito de fundamentação e limites de ferramenta. Um modelo alternativo não aprovado para dados pessoais não é fallback válido para essa rota.

**Degradação** reduz capacidade de forma declarada. Se a recuperação falha, uma aplicação baseada em política não deve improvisar: informa indisponibilidade e oferece fonte oficial ou canal humano. Se a ferramenta de escrita está indisponível, mantém consulta e rascunho, mas não confirma ação. Se o guardrail crítico falha, bloqueia a rota afetada. A interface comunica o que não ocorreu.

**Rollback** restaura um manifesto conhecido: código, modelo/rota, prompt, política, índice e contratos compatíveis. Reverter apenas o prompt pode deixar o índice incompatível. Migrações de memória e efeitos externos exigem forward recovery, compensação ou reconciliação; não se “desfaz” um e-mail enviado com deployment anterior. Mantenha janela de compatibilidade e teste o procedimento.

## Incidente generativo

**Resposta a incidente** preserva a sequência: detectar, triar, conter, comunicar, erradicar, recuperar e aprender. Quando a classificação alcança impacto, guardrail crítico ou limiar de severidade, abre-se um identificador e congelam-se evidências minimizadas. A triagem delimita release, tenants, dados, ferramentas, período e possível efeito. Contenção pode desabilitar operação, remover fonte, reduzir tráfego, revogar credencial, fixar modelo ou encaminhar ao humano. Segurança, privacidade, jurídico e dono do processo participam conforme impacto.

Depois, reconstruir traces não autoriza expor conteúdo a todos. A recuperação valida o pacote e amplia gradualmente. O post-incident review evita caça a culpados e produz causas técnicas e organizacionais, riscos atualizados, testes de regressão, mudanças de runbook e responsáveis com prazo. Casos reais alimentam avaliação apenas após tratamento de dados e revisão para não perpetuar conteúdo malicioso.

Alertas precisam de ação. “Qualidade média caiu 1%” sem janela, fatia ou runbook gera fadiga. Prefira sinais compostos: aumento de abstenção numa rota após mudança de índice; custo por tarefa concluída acima do orçamento; ferramenta com duplicidade; divergência entre feedback e avaliador. Métricas sentinela detectam mudança do fornecedor mesmo sem release interno.

## Fitness functions operacionais

Fitness functions verificam continuamente se a operação mantém o contrato arquitetural:

- toda execução crítica contém `release_id`, rota, versão de política e resultado no trace minimizado;
- promoção exige manifesto completo, regressão compatível e autoridade registrada para exceção;
- bypass do gateway preserva controles equivalentes, prazo, escopo e proprietário, ou a rota degrada;
- fallback para dado restrito usa somente modelo, região e capacidade catalogados e avaliados para a classe;
- rollback, failover e recuperação de efeitos são ensaiados na janela definida, com resultado e responsáveis registrados.

Falha em uma dessas verificações interrompe promoção, reduz exposição, ativa degradação ou abre incidente conforme impacto. A fitness function não substitui julgamento de risco; ela torna verificável a condição operacional que não pode ser violada.

## Prioridades e tensões operacionais

| Característica | Prioridade | Tensão aceita | Medida e responsável |
|---|---|---|---|
| Segurança, privacidade e autorização | Não negociável | bloqueio e segregação podem reduzir disponibilidade | acesso indevido ou ação sem política: zero; Segurança e Privacidade |
| Confiabilidade e recuperação | Alta | redundância, ensaios e reconciliação aumentam custo e operação | recuperação dentro da janela e efeitos duplicados: zero; Operação e Plataforma |
| Auditabilidade | Alta | traces preservam metadados sob retenção limitada | execução crítica reconstruível por `release_id`; Auditoria e Operação |
| Latência, custo e utilidade | Importante | orçamento e degradação podem encaminhar ou limitar jornadas | p95, custo por resultado e abandono por rota; Produto e FinOps |
| Modificabilidade e portabilidade | Importante | adaptadores, contratos e regressão elevam complexidade | mudança localizada e ensaio de saída; Arquitetura e Plataforma |

Operação sustentável atende a essas prioridades no cenário. Não maximiza simultaneamente disponibilidade, autonomia, coleta de telemetria, velocidade de mudança e opcionalidade.
