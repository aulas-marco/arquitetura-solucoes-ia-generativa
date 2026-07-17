# Padrões e decisões: ameaças, guardrails e governança

## Modele ativos, atores e fronteiras antes de escolher produtos

Um modelo de ameaças começa no fluxo concreto. Liste usuários legítimos, atacantes externos, autores de documentos, administradores, fornecedores e serviços comprometidos. Marque ativos, entradas controláveis, fronteiras de confiança, mudanças de privilégio e efeitos. Para cada cenário, descreva precondição, percurso, impacto, prevenção, detecção, resposta e risco residual. Uma lista genérica de riscos ajuda a descobrir cenários, mas não substitui esse mapa.

O [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/) é orientação comunitária de segurança e um vocabulário útil, não prova de conformidade. O [perfil SSDF para IA generativa do NIST](https://doi.org/10.6028/NIST.SP.800-218A) estende práticas de desenvolvimento seguro a modelos e componentes generativos. Nenhum documento conhece, sozinho, as permissões, impactos e atacantes do seu sistema.

## Ameaças recorrentes em RAG e agentes

### Instruções adversariais

Na **injeção direta de prompt**, o usuário escreve instruções para substituir política, revelar contexto, alterar formato ou induzir uma ferramenta. Delimitadores, hierarquia de mensagens, classificadores e exemplos de recusa reduzem ataques conhecidos. Eles não garantem que um modelo probabilístico obedecerá sempre, nem corrigem uma ferramenta excessivamente autorizada.

Na **injeção indireta de prompt**, a instrução vem de documento, página, e-mail, resultado de ferramenta ou memória. O usuário pode nem saber que a carga existe. Marcar conteúdo como dado, separar instrução de evidência, remover formatos ativos e restringir ferramentas reduz exposição. Contudo, como o modelo interpreta texto e instrução no mesmo mecanismo, isolamento textual é imperfeito. A barreira decisiva para efeitos continua fora do modelo: autorização, validação de parâmetros e aprovação proporcional ao risco.

**Conteúdo recuperado não confiável** amplia o problema. Uma fonte pode ser autorizada e ainda estar desatualizada, adulterada ou semanticamente errada. Assinatura, origem, revisão editorial, classificação, data de vigência, filtros de autorização e citação aumentam integridade e rastreabilidade. Não provam que a afirmação é verdadeira; fontes conflitantes exigem regra de precedência, abstenção ou revisão humana.

### Exposição e efeitos indevidos

**Vazamento de contexto** ocorre quando instruções internas, histórico, trechos de outros usuários ou metadados são reproduzidos. **Vazamento de segredo** envolve tokens, chaves, senhas ou credenciais. Minimizar o contexto, segregar tenants, impedir segredos no prompt, usar referências opacas, aplicar prevenção de perda de dados e testar extração reduzem a superfície. Um filtro de saída não recupera um segredo já enviado ao fornecedor e pode falhar diante de codificação ou fragmentação.

**Uso indevido de ferramenta** inclui escolher operação errada, trocar o recurso, elevar parâmetros, repetir efeitos ou contornar política por uma ferramenta equivalente. Catálogo mínimo, contrato estreito, identidade delegada, decisão de política no executor, idempotência, limite de taxa e confirmação reduzem dano. Esquema válido garante forma, não legitimidade; descrição “use com cuidado” não é controle de acesso.

### Estado, custo e dependências

Na **manipulação de memória**, conteúdo de conversa ou ferramenta se torna fato persistente, preferência ou instrução sem validação. Separe estado autoritativo, memória de trabalho e memória persistente; registre origem, finalidade, escopo, confiança, versão e expiração; exija confirmação para promoção. Essas medidas não tornam uma memória verdadeira. Fatos críticos devem ser reconciliados com a fonte oficial antes do uso.

A **negação de serviço econômica** explora prompts longos, recuperação ampla, loops de agentes, ferramentas caras ou geração repetida para consumir tokens, chamadas e tempo. Cotas por identidade e tarefa, limite de contexto, orçamento de etapas, cache seguro, timeout, rate limiting e circuit breaker contêm custo. Limites muito baixos também negam serviço a usos legítimos; calibre por classe e monitore falsos bloqueios. Orçamento impede gasto ilimitado, mas não garante que o gasto permitido produza valor.

O risco de **cadeia de fornecedores** inclui mudança de modelo, dependência, biblioteca, dataset, imagem de container, API, subprocessador ou política contratual. Inventário, versões fixadas quando possível, avaliação de fornecedor, assinatura e procedência de artefatos, testes de regressão, canary, alternativa de saída e cláusulas de notificação reduzem surpresa. Um selo ou questionário não observa toda a cadeia; dependências transitivas e mudanças do serviço continuam exigindo monitoramento.

## Guardrails em profundidade

Guardrail é uma barreira técnica, processual ou humana que previne, detecta, limita ou ajuda a recuperar um desvio. Distribua-os onde a informação muda de confiança ou privilégio.

| Camada | Controles possíveis | O que reduzem | O que não garantem |
|---|---|---|---|
| **camada de entrada** | autenticação, limite de tamanho e taxa, normalização, detecção de dados sensíveis e padrões adversariais | abuso óbvio, carga excessiva, parte das injeções diretas | intenção legítima, ausência de ataque novo ou segurança das etapas seguintes |
| **camada de contexto** | instruções versionadas, separação entre política e dados, contexto mínimo, referências opacas, segregação por execução | confusão entre fontes, exposição desnecessária e contaminação cruzada | obediência perfeita do modelo ou correção do conteúdo |
| **camada de recuperação** | filtro de autorização antes do conteúdo, proveniência, classificação, vigência, integridade, diversidade e limiar de suficiência | acesso indevido, fonte obsoleta ou contexto insuficiente | verdade da fonte ou resistência completa à injeção indireta |
| **camada de ferramenta** | catálogo mínimo, esquema, política externa, credencial fora do prompt, idempotência, orçamento e sandbox | abuso de privilégio, parâmetros inválidos, repetição e parte dos efeitos | adequação semântica da ação ou reversibilidade do mundo real |
| **camada de saída** | validação de esquema, vínculo afirmação–evidência, política de conteúdo, mascaramento e abstenção | formato inválido, afirmações sem apoio detectável e parte dos vazamentos | factualidade universal, ausência de conteúdo codificado ou reparação de exposição anterior |
| **camada de aprovação humana** | fila por risco, resumo de evidências, diferenças, prazo, dupla aprovação e escalonamento | ações sensíveis sem autoridade e casos ambíguos | decisão correta se houver fadiga, viés, informação manipulada ou aprovação automática |

O padrão **guardrails em profundidade** evita depender de uma barreira. Independência importa: três classificadores treinados com dados e modelo semelhantes podem falhar juntos. Cada camada precisa de modo seguro de falha. Se o filtro está indisponível, o sistema bloqueia, degrada para conteúdo público ou segue sem proteção? A escolha deve refletir o impacto, não apenas disponibilidade.

Filtros também criam dano por falso positivo. Registre motivo de bloqueio, ofereça contestação adequada e meça desempenho por idioma e grupo. Guardrail invisível e sem telemetria vira segurança teatral: aparece no diagrama, mas ninguém sabe se está ativo, eficaz ou contornável.

## Privacidade por ciclo de vida

**Minimização** começa na finalidade: quais campos são necessários para responder, avaliar, auditar e operar? Reduza coleta, contexto, saída e log separadamente. Pseudonimização diminui associação direta, mas não torna dados automaticamente anônimos nem elimina obrigação de proteção.

**Retenção** define prazo e evento de descarte por classe: conversa, trace, amostra de avaliação, memória, índice e backup. “Guardar para melhorar o modelo” é finalidade vaga. Documente necessidade, acesso, expiração, exclusão e exceções de preservação. Verifique o descarte também em cache, índice e fornecedor.

**Segregação** aplica isolamento lógico ou físico por tenant, sensibilidade, ambiente e função. Índice separado pode reduzir erro de configuração; filtro de autorização permite flexibilidade. Ambos precisam de testes negativos. Criptografia protege dados em trânsito ou repouso conforme sua aplicação, mas não impede que um processo legitimamente autorizado envie o dado errado ao modelo.

Dados de produção em avaliação exigem o mesmo rigor. Prefira casos sintéticos ou desidentificados quando preservarem o fenômeno. Quando amostras reais forem necessárias, use seleção autorizada, acesso restrito, prazo curto e rastreabilidade. Não copie conversas indiscriminadamente para planilhas de avaliação.

## Governança que acompanha mudanças

Um **catálogo** registra caso de uso, finalidade, públicos, proprietário, criticidade, modelos, fontes, ferramentas, fornecedores, classes de dados, controles, métricas e status. Catálogo sem reconciliação com o ambiente vira inventário histórico; automatize referências a implantações e revise divergências.

**Versionamento** precisa abranger o pacote comportamental: modelo, parâmetros, prompt, política, corpus, pipeline de indexação, avaliadores, critérios de avaliação, ferramentas e dependências. Uma versão permite reproduzir a configuração, não necessariamente repetir a mesma saída probabilística. Preserve sementes quando suportadas, entradas e faixas de variação.

**Auditoria** registra quem aprovou finalidade, mudança, acesso, exceção e risco residual, além das decisões de execução relevantes. Log imutável ajuda a detectar alteração; não comprova que o evento registrado foi correto. Proteja a própria trilha, separe funções e teste consultas de investigação.

A **política de uso** declara usuários, finalidades, dados, ações, proibições, revisão humana, comunicação de limites, escalonamento e consequências de desvio. Publique-a na interface e transforme itens executáveis em política técnica. Texto sozinho depende de adesão; controle técnico sozinho não cobre julgamento e contexto social.

O [ISO/IEC 42001:2023](https://www.iso.org/standard/42001) especifica requisitos para um sistema de gestão de IA quando uma organização escolhe adotá-lo ou buscar conformidade. Ele não prescreve uma arquitetura única nem certifica cada resposta. O NIST AI RMF permanece voluntário. Neste curso, catálogo, pacote de versões e portões de avaliação são recomendações arquiteturais para materializar governança; não devem ser apresentados como cláusulas literais desses documentos.

## Critério de decisão

Para cada controle, registre: cenário tratado, camada, proprietário, configuração, evidência de teste, cobertura conhecida, falsos positivos, dependências, modo de falha e risco residual. Evite afirmar “bloqueia prompt injection”. Prefira: “reduziu esta família de ataques de 62% para 9% no conjunto v4, ainda falhou em conteúdo codificado e, por isso, escrita permanece mediada por política e aprovação”. Essa linguagem sustenta decisão e aprendizagem.

Veja os controles aplicados a um fluxo real em [Exemplo arquitetural](exemplo-arquitetural.md).
