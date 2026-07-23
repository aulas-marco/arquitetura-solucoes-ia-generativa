# Catálogo de padrões arquiteturais

Padrões nomeiam soluções recorrentes e suas consequências. Use-os para ampliar alternativas e comunicar decisões; não os trate como componentes obrigatórios. Cada aplicação ainda precisa ser justificada por requisitos, riscos e evidências do contexto.

## Geração

### Geração direta com prompt versionado

**Contexto.** Tarefa de baixo risco depende principalmente das capacidades do modelo e das informações fornecidas pelo usuário.  
**Problema.** A equipe precisa entregar geração útil sem introduzir componentes de conhecimento ou autonomia desnecessários.  
**Solução.** Encapsular instruções, exemplos e parâmetros em uma versão testável; chamar o modelo e registrar configuração e resultado.  
**Consequências.** Reduz complexidade e latência, mas mantém dependência do conhecimento paramétrico e exige avaliação de variabilidade e alucinação.  
**Módulos relacionados.** [1 — Fundamentos](../sobre/plano-da-disciplina.md#modulo-1) e [2 — Desenho conceitual](../sobre/plano-da-disciplina.md#modulo-2).

### Saída estruturada por contrato

**Contexto.** A resposta será consumida por software ou usada para orientar uma ação posterior.  
**Problema.** Texto livre é ambíguo e pode quebrar integrações ou introduzir parâmetros inválidos.  
**Solução.** Definir esquema, restringir a geração e validar tipos, limites e regras antes do consumo.  
**Consequências.** Aumenta previsibilidade e testabilidade, mas não garante correção semântica; falhas de validação precisam de retry limitado ou fallback.  
**Módulos relacionados.** [2 — Desenho conceitual](../sobre/plano-da-disciplina.md#modulo-2) e [4 — Agentes](../sobre/plano-da-disciplina.md#modulo-4).

### Seleção de modelo por tarefa

**Contexto.** O portfólio possui tarefas com diferentes exigências de qualidade, latência, custo, modalidade e risco.  
**Problema.** Um único modelo impõe custo excessivo ou capacidade insuficiente a parte das solicitações.  
**Solução.** Classificar a tarefa por sinais observáveis e rotear para perfis de modelo aprovados, com políticas e avaliação por rota.  
**Consequências.** Otimiza recursos e reduz dependência, mas adiciona classificadores, matriz de compatibilidade e mais combinações para testar.  
**Módulos relacionados.** [2 — Desenho conceitual](../sobre/plano-da-disciplina.md#modulo-2) e [6 — Operação](../sobre/plano-da-disciplina.md#modulo-6).

### Degradação segura da geração

**Contexto.** O modelo principal pode falhar, degradar ou ultrapassar orçamento sem que toda a experiência possa parar.  
**Problema.** Repetições ilimitadas aumentam custo e latência, enquanto uma falha abrupta pode induzir o usuário ao erro.  
**Solução.** Definir timeout e critérios de degradação para modelo alternativo, resposta parcial, template determinístico ou encaminhamento humano.  
**Consequências.** Melhora resiliência e controle de custo, mas cada caminho precisa preservar requisitos mínimos e ser testado separadamente.  
**Módulos relacionados.** [4 — Agentes](../sobre/plano-da-disciplina.md#modulo-4) e [6 — Operação](../sobre/plano-da-disciplina.md#modulo-6).

## Conhecimento

### RAG básico com dois fluxos

**Contexto.** Respostas dependem de conteúdo atualizável e controlado que não deve ficar apenas nos parâmetros do modelo.  
**Problema.** É necessário atualizar conhecimento e rastrear fontes sem retreinar o modelo.  
**Solução.** Separar fluxo offline de ingestão e indexação do fluxo online de consulta, recuperação, contexto e geração.  
**Consequências.** Melhora atualidade e proveniência, mas introduz qualidade de recuperação, sincronização e operação do índice como responsabilidades.  
**Módulos relacionados.** [3 — RAG](../sobre/plano-da-disciplina.md#modulo-3) e [5 — Confiança](../sobre/plano-da-disciplina.md#modulo-5).

### Recuperação híbrida com reranking

**Contexto.** O corpus combina termos exatos, siglas e relações semânticas que uma única estratégia não recupera bem.  
**Problema.** Aumentar cobertura traz candidatos ruidosos e pode piorar o contexto final.  
**Solução.** Unir busca lexical e vetorial, normalizar os escores e aplicar reranking a um conjunto limitado de candidatos.  
**Consequências.** Pode elevar precisão e cobertura, ao custo de mais latência, parâmetros, infraestrutura e avaliação por etapa.  
**Módulos relacionados.** [3 — RAG](../sobre/plano-da-disciplina.md#modulo-3) e [5 — Confiança](../sobre/plano-da-disciplina.md#modulo-5).

### Recuperação consciente de autorização

**Contexto.** Fontes possuem permissões por usuário, grupo, organização ou classificação.  
**Problema.** Filtrar apenas depois da busca pode revelar metadados, ocupar o conjunto de candidatos ou contaminar o contexto.  
**Solução.** Propagar identidade e políticas até a recuperação, aplicar filtros antes do acesso ao conteúdo e auditar a decisão.  
**Consequências.** Reduz vazamento entre tenants, mas acopla atualização de permissões ao índice e exige testes de negação e revogação.  
**Módulos relacionados.** [3 — RAG](../sobre/plano-da-disciplina.md#modulo-3), [5 — Confiança](../sobre/plano-da-disciplina.md#modulo-5) e [6 — Operação](../sobre/plano-da-disciplina.md#modulo-6).

### Resposta apoiada em evidências

**Contexto.** O usuário precisa distinguir afirmações sustentadas de inferências ou ausência de conhecimento.  
**Problema.** O modelo pode preencher lacunas e produzir uma resposta fluente mesmo quando a recuperação é insuficiente.  
**Solução.** Entregar trechos com identificadores, exigir vínculo entre afirmação e fonte e recusar ou encaminhar quando a evidência não atingir o critério.  
**Consequências.** Aumenta verificabilidade, mas pode reduzir cobertura aparente e depende de limiares calibrados e fontes de boa qualidade.  
**Módulos relacionados.** [3 — RAG](../sobre/plano-da-disciplina.md#modulo-3) e [5 — Confiança](../sobre/plano-da-disciplina.md#modulo-5).

## Orquestração

### Workflow determinístico com etapas generativas

**Contexto.** O processo é conhecido e auditável, mas algumas etapas exigem interpretação ou geração.  
**Problema.** Delegar o fluxo inteiro ao modelo criaria autonomia sem benefício correspondente.  
**Solução.** Manter ordem, transições e erros sob controle determinístico e usar o modelo apenas em etapas delimitadas por contratos.  
**Consequências.** Facilita testes e auditoria, mas oferece menos adaptação a tarefas abertas e requer modelagem explícita das exceções.  
**Módulos relacionados.** [2 — Desenho conceitual](../sobre/plano-da-disciplina.md#modulo-2) e [4 — Agentes](../sobre/plano-da-disciplina.md#modulo-4).

### Uso controlado de ferramentas

**Contexto.** O sistema precisa consultar dados ou executar funções além da geração de texto.  
**Problema.** A escolha e os parâmetros produzidos pelo modelo podem ser inválidos, indevidos ou perigosos.  
**Solução.** Expor catálogo mínimo com esquemas, validar autorização e parâmetros e separar proposta de ferramenta de sua execução.  
**Consequências.** Amplia capacidade mantendo uma fronteira verificável, mas cada ferramenta aumenta superfície de ataque, integração e testes.  
**Módulos relacionados.** [4 — Agentes](../sobre/plano-da-disciplina.md#modulo-4) e [5 — Confiança](../sobre/plano-da-disciplina.md#modulo-5).

### Desenvolvimento guiado por especificação

**Contexto.** Agentes de codificação podem alterar muitos artefatos com rapidez.  
**Problema.** Pedido informal não oferece critério estável para teste, revisão ou aceite.  
**Solução.** Usar constitution, spec, plan, tasks, implementação e verificação como sequência de artefatos, com gates humanos.  
**Consequências.** Aumenta preparo e rastreabilidade, mas reduz interpretação silenciosa e facilita revisão por aderência à spec.  
**Módulos relacionados.** [4 — Agentes](../sobre/plano-da-disciplina.md#modulo-4) e [6 — Operação](../sobre/plano-da-disciplina.md#modulo-6).

### Aprovação humana por risco

**Contexto.** Algumas ações têm impacto financeiro, jurídico, operacional ou pessoal incompatível com autonomia total.  
**Problema.** Aprovar tudo destrói eficiência; aprovar nada concentra risco no modelo e na integração.  
**Solução.** Classificar ações por risco e exigir confirmação ou aprovação com contexto suficiente acima de limites definidos.  
**Consequências.** Preserva responsabilidade humana nos pontos críticos, mas cria filas, metas de atendimento e necessidade de uma interface de decisão clara.  
**Módulos relacionados.** [4 — Agentes](../sobre/plano-da-disciplina.md#modulo-4) e [5 — Confiança](../sobre/plano-da-disciplina.md#modulo-5).

### Agente com orçamento limitado

**Contexto.** A tarefa aberta justifica escolher dinamicamente ferramentas e próximos passos.  
**Problema.** Um agente pode entrar em ciclos, acumular custo ou ampliar seus efeitos sem progresso mensurável.  
**Solução.** Definir orçamento de etapas, tempo, tokens, custo e ações; interromper em limites e oferecer retomada, fallback ou escalonamento.  
**Consequências.** Contém falhas e custo, mas pode encerrar tarefas válidas; os limites precisam de telemetria e calibração por classe de tarefa.  
**Módulos relacionados.** [4 — Agentes](../sobre/plano-da-disciplina.md#modulo-4), [5 — Confiança](../sobre/plano-da-disciplina.md#modulo-5) e [6 — Operação](../sobre/plano-da-disciplina.md#modulo-6).

## Confiança

### Guardrails em profundidade

**Contexto.** Entradas, fontes, modelos e ferramentas possuem falhas diferentes e nenhuma barreira é suficiente sozinha.  
**Problema.** Um controle isolado cria confiança excessiva e deixa caminhos alternativos sem proteção.  
**Solução.** Distribuir controles em entrada, recuperação, contexto, ferramentas, saída e aprovação, com degradação segura.  
**Consequências.** Reduz dependência de um único mecanismo, mas pode aumentar latência e falsos positivos e requer observação do efeito combinado.  
**Módulos relacionados.** [5 — Confiança](../sobre/plano-da-disciplina.md#modulo-5) e [6 — Operação](../sobre/plano-da-disciplina.md#modulo-6).

### Isolamento entre instrução e conteúdo

**Contexto.** O sistema processa documentos, páginas ou mensagens que podem conter comandos não confiáveis.  
**Problema.** O modelo pode interpretar conteúdo recuperado como instrução e ignorar a política do sistema.  
**Solução.** Marcar fronteiras, minimizar contexto, tratar fontes como dados e impedir que definam ferramentas, credenciais ou políticas.  
**Consequências.** Diminui exposição à injeção indireta, mas não elimina a necessidade de autorização, validação de ações e testes adversariais.  
**Módulos relacionados.** [3 — RAG](../sobre/plano-da-disciplina.md#modulo-3), [4 — Agentes](../sobre/plano-da-disciplina.md#modulo-4) e [5 — Confiança](../sobre/plano-da-disciplina.md#modulo-5).

### Validação de saída em camadas

**Contexto.** Uma saída pode conter formato inválido, dado sensível, conteúdo proibido ou afirmação sem suporte.  
**Problema.** Uma única verificação não cobre propriedades sintáticas, semânticas e de política.  
**Solução.** Aplicar esquema e regras determinísticas, verificações de política e, quando necessário, avaliação especializada antes de entregar ou agir.  
**Consequências.** Aumenta segurança e consistência, mas adiciona custo e pode bloquear conteúdo legítimo; falhas devem ter tratamento explícito.  
**Módulos relacionados.** [4 — Agentes](../sobre/plano-da-disciplina.md#modulo-4) e [5 — Confiança](../sobre/plano-da-disciplina.md#modulo-5).

### Pirâmide de avaliação

**Contexto.** Qualidade possui dimensões distintas e avaliações humanas completas são caras e lentas.  
**Problema.** Uma métrica única ou avaliador único produz uma visão parcial e pode ocultar regressões críticas.  
**Solução.** Combinar verificações determinísticas amplas, métricas por componente, avaliadores automatizados calibrados e amostras humanas focadas.  
**Consequências.** Equilibra velocidade e profundidade, mas exige conjuntos representativos, calibração contínua e rastreamento das limitações do avaliador.  
**Módulos relacionados.** [2 — Desenho conceitual](../sobre/plano-da-disciplina.md#modulo-2) e [5 — Confiança](../sobre/plano-da-disciplina.md#modulo-5).

## Operações

### Gateway corporativo de modelos

**Contexto.** Várias equipes consomem modelos com contratos, políticas e telemetria diferentes.  
**Problema.** Integrações diretas duplicam controles, reduzem portabilidade e dificultam compreender consumo e risco.  
**Solução.** Centralizar autenticação, roteamento, cotas, políticas e telemetria em um gateway com interface estável.  
**Consequências.** Padroniza controles e negociação, mas pode se tornar gargalo ou ponto único de falha e precisa preservar capacidades específicas justificadas.  
**Módulos relacionados.** [6 — Operação](../sobre/plano-da-disciplina.md#modulo-6).

### Pacote de versões reproduzível

**Contexto.** O comportamento depende da combinação de modelo, prompt, dados, índice, ferramenta e política.  
**Problema.** Versionar apenas código impede reproduzir uma resposta ou atribuir uma regressão.  
**Solução.** Registrar uma versão de implantação que referencia todas as configurações e artefatos efetivamente usados.  
**Consequências.** Melhora auditoria, comparação e rollback, mas requer disciplina de catálogo e compatibilidade entre artefatos.  
**Módulos relacionados.** [5 — Confiança](../sobre/plano-da-disciplina.md#modulo-5) e [6 — Operação](../sobre/plano-da-disciplina.md#modulo-6).

### Avaliação contínua antes e depois da entrega

**Contexto.** Mudanças em modelos, prompts, dados e fontes podem alterar comportamento sem mudança no código.  
**Problema.** Testes apenas antes da primeira liberação não detectam regressão de fornecedor ou deriva do domínio.  
**Solução.** Executar regressão offline em cada mudança e monitorar amostras e indicadores online com critérios de canary e rollback.  
**Consequências.** Reduz tempo de detecção e risco de mudança, mas exige conjuntos mantidos, limites operacionais e governança de dados de produção.  
**Módulos relacionados.** [5 — Confiança](../sobre/plano-da-disciplina.md#modulo-5) e [6 — Operação](../sobre/plano-da-disciplina.md#modulo-6).

### Trace de ponta a ponta com privacidade

**Contexto.** Uma resposta emerge de recuperação, modelos, controles e ferramentas distribuídos.  
**Problema.** Logs isolados não permitem reconstruir qualidade, latência, custo ou causa de uma ação, e podem expor dados sensíveis.  
**Solução.** Correlacionar etapas e versões em um trace, registrar métricas necessárias e aplicar minimização, mascaramento, acesso e retenção.  
**Consequências.** Acelera investigação e medição, mas adiciona custo de telemetria e requer equilíbrio explícito entre utilidade e privacidade.  
**Módulos relacionados.** [5 — Confiança](../sobre/plano-da-disciplina.md#modulo-5) e [6 — Operação](../sobre/plano-da-disciplina.md#modulo-6).
