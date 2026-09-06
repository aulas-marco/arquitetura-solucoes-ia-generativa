# Rastreabilidade e privacidade

Reconstruir uma execução sem transformar telemetria em vigilância, e tratar minimização, retenção e segregação como decisões de arquitetura.

## Rastreabilidade sem vigilância indiscriminada

**Rastreabilidade** é a capacidade de reconstruir a cadeia relevante: solicitação e identidade autorizada; versões de prompt, modelo, política, índice e ferramentas; documentos recuperados e suas permissões; decisões determinísticas; aprovações; saída entregue; latência, custo e incidentes. Ela sustenta depuração, avaliação, contestação e responsabilização.

Rastrear não significa guardar tudo. Prompts completos, documentos e respostas podem conter dados pessoais ou segredos. Prefira identificadores, hashes, categorias, decisões, métricas e amostras controladas; masque campos; segregue telemetria; limite acesso; defina retenção e descarte verificável. Quando conteúdo completo for necessário para investigação, trate-o como exceção autorizada. Uma trilha que vaza o que deveria proteger é uma nova vulnerabilidade.

Rastreabilidade também não equivale a explicação causal do modelo. O sistema pode registrar evidências apresentadas, passos observáveis e regras acionadas. Texto gerado como “raciocínio” não prova o mecanismo interno nem deve ser usado como justificativa suficiente para uma decisão sensível.

**Langfuse** e **Phoenix** observam traços; **Guardrails AI** valida entradas ou saídas. Risco, regras de domínio e bloqueios continuam no sistema.

## Privacidade por ciclo de vida

**Minimização** começa na finalidade: quais campos são necessários para responder, avaliar, auditar e operar? Reduza coleta, contexto, saída e log separadamente. Pseudonimização diminui associação direta, mas não torna dados automaticamente anônimos nem elimina obrigação de proteção.

**Retenção** define prazo e evento de descarte por classe: conversa, trace, amostra de avaliação, memória, índice e backup. “Guardar para melhorar o modelo” é finalidade vaga. Documente necessidade, acesso, expiração, exclusão e exceções de preservação. Verifique o descarte também em cache, índice e fornecedor.

**Segregação** aplica isolamento lógico ou físico por tenant, sensibilidade, ambiente e função. Índice separado pode reduzir erro de configuração; filtro de autorização permite flexibilidade. Ambos precisam de testes negativos. Criptografia protege dados em trânsito ou repouso conforme sua aplicação, mas não impede que um processo legitimamente autorizado envie o dado errado ao modelo.

Dados de produção em avaliação exigem o mesmo rigor. Prefira casos sintéticos ou desidentificados quando preservarem o fenômeno. Quando amostras reais forem necessárias, use seleção autorizada, acesso restrito, prazo curto e rastreabilidade. Não copie conversas indiscriminadamente para planilhas de avaliação.
