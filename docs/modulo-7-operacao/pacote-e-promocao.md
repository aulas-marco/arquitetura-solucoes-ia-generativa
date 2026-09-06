# Versionamento e promoção

A unidade de mudança excede a versão do código. O que se promove entre ambientes é um pacote de artefatos que, juntos, determinam comportamento.

## O objeto operado é um pacote comportamental

Em IA generativa, a unidade de mudança excede a versão do código. Chamaremos de **ativo comportamental** qualquer artefato cuja alteração possa mudar resposta, decisão, custo, latência, acesso ou efeito: modelo e revisão do provedor; parâmetros de inferência; prompt e exemplos; política e guardrails; corpus, permissões e snapshot do índice; modelo de embedding e estratégia de recuperação; esquemas e versões de ferramentas; memória; código de orquestração; critérios de avaliação, avaliadores e conjuntos de referência; dependências e configuração de infraestrutura.

A lista é a mesma [superfície comportamental](../modulo-1-fundamentos/superficie-comportamental.md#de-onde-emerge-o-comportamento) do Módulo 1 e o mesmo [arnês (*harness*)](../modulo-4-agentes/arnes.md) do Módulo 4, agora sob a lente da operação. O que interessa aqui não é o que determina o comportamento nem o que a engenharia controla, e sim o que precisa de versão, manifesto e portão para ser promovido.

O manifesto de uma liberação registra versões, proprietário, finalidade, evidências, aprovação e compatibilidade. “Versão 2 do chatbot” não basta se ela não permite descobrir qual índice, modelo e política estavam ativos. Hashes ajudam a verificar integridade, mas precisam de metadados compreensíveis. Para provedores sem revisão fixável, registre identificador, região, data, parâmetros e testes sentinela: a variação é risco explícito.

## Ambientes e promoção

**Desenvolvimento** favorece velocidade e diagnóstico. Usa dados sintéticos ou minimizados, modelos econômicos quando adequados e credenciais sem efeito real. Ainda precisa reproduzir contratos essenciais: schemas, filtros de autorização e limites não podem existir apenas em produção.

**Homologação** aproxima topologia, identidade, políticas, cotas e dependências da produção. Executa conjunto de referência, testes adversariais, carga, recuperação e simulações de falha. Dados reais só entram com finalidade, minimização e acesso aprovados. A homologação não prova que produção será igual; ela reduz diferenças conhecidas e torna diferenças restantes visíveis.

**Produção** atende usuários e efeitos reais com acesso mínimo, telemetria, SLOs, alertas, runbooks e mudança controlada. Ambientes devem separar identidades, segredos, índices, quotas e trilhas. Copiar conversas ou credenciais de produção para desenvolvimento destrói a fronteira. Configuração comum pode ser promovida como artefato; segredo e dado sensível são fornecidos pelo ambiente.

A promoção segue o mesmo manifesto entre ambientes. Exceções emergenciais ficam registradas e depois reconciliadas com a fonte versionada. Se alguém “corrige o prompt direto” no console do fornecedor, cria divergência impossível de reproduzir e uma mudança fora dos portões.

## Reprodutibilidade sem promessa impossível

**Reprodutibilidade** significa reconstruir configuração, entradas, decisões observáveis e condições suficientes para comparar o comportamento. Ela não promete texto idêntico: amostragem, paralelismo, hardware e mudanças invisíveis do provedor podem gerar variação. Quando houver seed e inferência determinística, registre-as; quando não houver, execute repetições e compare distribuições, critérios e intervalos.

Um registro mínimo por execução liga `release_id`, modelo, parâmetros, prompt, política, snapshot de recuperação, contratos de ferramenta, identidade autorizada pseudonimizada, decisões de roteamento e resultado. O replay deve evitar repetir efeitos: ferramentas de escrita são substituídas por simuladores ou respostas capturadas, e dados que não podem ser retidos são representados por evidência mínima. Reproduzir não autoriza reprocessar dados para outra finalidade.

## Portões antes da exposição

Um **portão de regressão** compara o candidato com critérios e baseline versionados. Testes determinísticos cobrem schemas, autorização, citações, budgets e invariantes de ferramenta. Avaliação probabilística usa repetições, fatias e intervalos. Segurança inclui casos adversariais. Desempenho e custo são medidos com carga representativa. O portão registra pacote, conjunto, avaliador, resultado, exceção, aprovador e validade.

Portões não devem congelar melhoria. Um limiar absoluto protege o mínimo; um limite de não regressão impede piora relevante; uma revisão explícita trata trade-offs, como pequena perda de latência para grande ganho de segurança. Flakiness não é motivo para ignorar teste: separe variação esperada de infraestrutura instável e estime incerteza.

**Canary** expõe o candidato a uma fração delimitada de tráfego, usuários, tenants ou casos. A coorte precisa representar o risco e evitar pessoas vulneráveis sem consentimento ou proteção. Antes do início, defina duração, volume mínimo, métricas, limiares, autoridade para pausar e versão de retorno. Compare por fatia e mantenha atribuição: sem `release_id` no trace, misturam-se resultados. Atingir um critério de parada sempre interrompe a exposição, mas só abre incidente se houver impacto, guardrail crítico ou severidade definida; hipótese de produto rejeitada segue para diagnóstico normal.

Shadow traffic pode executar o candidato sem mostrar a saída nem realizar efeitos. É útil para latência e comparação, mas ainda processa dados e incorre em custo; ferramentas devem ser simuladas. A/B testa uma hipótese de produto quando ambas as variantes já são aceitáveis. Não se usa experimento para descobrir se uma variante viola um guardrail crítico.
