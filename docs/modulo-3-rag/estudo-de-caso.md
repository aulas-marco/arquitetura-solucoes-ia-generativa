# Estudo de caso: políticas e contratos com acesso individual

A Aurora Serviços quer um assistente para colaboradores consultarem políticas internas e contratos de clientes. Hoje, especialistas respondem perguntas repetidas, verificam vigência em três repositórios e enviam links manualmente. A organização exige **permissões por usuário**, **citações** de fonte, **atualização** rápida e **abstenção** explícita. O assistente informa e compara; não aprova exceções, altera contratos nem substitui parecer jurídico.

## Cenários que dirigem a arquitetura

1. Uma política geral pode ser vista por toda a empresa; uma política regional depende da unidade.
2. Um contrato só pode ser consultado pela equipe do cliente e por funções autorizadas.
3. A pergunta pode combinar regra geral e cláusula específica, com autoridades diferentes.
4. Uma política revogada deve deixar de aparecer em até quinze minutos; revogação de acesso, em até dois.
5. Se fonte obrigatória estiver ausente, ilegível, expirada ou conflitante, o sistema deve limitar a resposta e encaminhar.
6. A interface deve abrir a versão e a cláusula citadas, repetindo a autorização no clique.

## Decisão incremental

Uma busca vetorial única foi rejeitada: códigos de contrato e cláusulas favorecem busca lexical, enquanto perguntas em linguagem natural favorecem semântica. Também não resolveria autorização e temporalidade.

O primeiro incremento usa RAG híbrido com dois domínios separados: políticas e contratos. Cada domínio tem conector, regras de chunking e metadados próprios. Políticas são divididas por seção, preservando título, exceções e vigência; contratos seguem cláusulas e subcláusulas, com relação pai–filho. Índices lexical e vetorial produzem candidatos, e um reranker limitado reordena somente conteúdo autorizado.

O motor de políticas deriva tenant, unidade, carteira de clientes, papel e finalidade da identidade corporativa. Isolamento por cliente reduz a superfície; filtros por atributo refinam o conjunto. Falha de política nega a consulta. O cache inclui decisão de acesso, versão e domínio.

Para perguntas mistas, um roteador determinístico identifica se ambos os domínios são necessários. O montador mantém cada evidência com autoridade e data. Contrato específico prevalece apenas quando uma regra jurídica aprovada declara essa relação; similaridade não decide precedência. Conflito não resolvido aparece ao usuário.

## Fluxos e critérios

Publicações disparam ingestão por evento; reconciliação horária detecta eventos perdidos. Extração inválida entra em quarentena. Uma versão candidata passa por perguntas de regressão, testes de exclusão e verificação de metadados antes da promoção atômica. O manifesto preserva fonte, versão, extrator, chunking, embedding e índices.

Na consulta, a transformação extrai cliente, número, região e data sem aceitar atributos de acesso fornecidos no texto. Recuperação híbrida recebe o predicado obrigatório. A suficiência exige fonte aplicável, vigência, cobertura das partes da pergunta e ausência de conflito não resolvido. A geração associa afirmações materiais a chunks; um validador verifica suporte e completude de citações.

Três respostas são possíveis:

- resposta apoiada, com citações próximas das afirmações;
- resposta parcial, declarando qual parte não possui suporte;
- abstenção: “As fontes disponíveis para sua consulta não sustentam uma resposta. Encaminhe ao responsável indicado.”

A mensagem não revela se existe contrato fora das permissões do usuário.

## Avaliação e operação

O conjunto de teste cruza perguntas respondíveis, sem resposta, temporalidade, conflito e grupos de acesso. Mede Recall@5 de evidências, precisão no contexto, correção e completude de citações, fidelidade, abstenção correta e indevida. Testes adversariais tentam recuperar contrato por nome, reformulação e cache após revogação. Qualquer conteúdo proibido materializado reprova a versão, independentemente da média.

Operações acompanha atraso de política e revogação, falha de extração, latência por etapa, fallback, custo e reconstrução do trace. Se reranking falhar, o ranking híbrido só é aceito para perguntas gerais que ainda atinjam suficiência; contratos de alto risco levam à abstenção. Se um repositório cair, o assistente não apresenta cópia antiga como atual.

## Gatilhos de evolução

RAG hierárquico será testado se cláusulas isoladas perderem definições. RAG corretivo, com uma reformulação, só entra se falhas recuperáveis forem frequentes e a intenção permanecer estável. Consulta estruturada será adicionada para datas e status operacionais, em vez de indexar snapshots. Cada evolução precisa superar a arquitetura atual no conjunto estratificado sem violar latência, custo ou autorização.

O caso demonstra o princípio central: índice, modelo e prompt são substituíveis; identidade, proveniência, atualização, suficiência e avaliação definem se a resposta é confiável no sistema.

**Próxima página:** [Exercícios](exercicios.md).
