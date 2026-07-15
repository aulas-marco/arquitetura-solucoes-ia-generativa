# Catálogo de atributos de qualidade

Um atributo só orienta arquitetura quando é expresso como cenário verificável. Para cada qualidade, registre **fonte**, **estímulo**, **ambiente**, **artefato**, **resposta** e **medida**; ajuste valores e condições ao risco do seu caso.

## Qualidade

- **Fonte:** usuário autorizado.
- **Estímulo:** envia uma pergunta representativa do domínio.
- **Ambiente:** operação normal, com versões aprovadas de modelo e prompt.
- **Artefato:** fluxo de geração de resposta.
- **Resposta:** produz conteúdo relevante, correto para a tarefa e coerente com as instruções.
- **Medida:** ao menos 90% dos casos críticos atingem nota mínima 4/5 na rubrica aprovada.

## Fundamentação (grounding)

- **Fonte:** usuário consultando conhecimento controlado.
- **Estímulo:** solicita uma afirmação que depende de fonte corporativa.
- **Ambiente:** índice atualizado e fontes disponíveis.
- **Artefato:** recuperação, montagem de contexto e geração.
- **Resposta:** limita a resposta às evidências recuperadas, indica fontes e declara insuficiência quando necessário.
- **Medida:** pelo menos 95% das afirmações verificáveis possuem suporte correto; nenhuma resposta é inventada nos casos sem evidência do conjunto crítico.

## Latência

- **Fonte:** usuário interativo.
- **Estímulo:** envia uma solicitação válida.
- **Ambiente:** carga normal e dependências saudáveis.
- **Artefato:** caminho online completo.
- **Resposta:** confirma o recebimento e inicia a entrega sem bloquear a interface.
- **Medida:** p95 do primeiro conteúdo abaixo de 2 s e p95 da resposta completa abaixo de 8 s.

## Custo

- **Fonte:** uso agregado de uma unidade de negócio.
- **Estímulo:** volume mensal alcança a faixa planejada.
- **Ambiente:** mix esperado de tarefas e modelos.
- **Artefato:** solução e serviços compartilhados.
- **Resposta:** roteia tarefas, aplica cotas e registra consumo por responsável.
- **Medida:** custo médio por interação dentro do orçamento e desvio mensal menor que 10% sem alerta.

## Privacidade

- **Fonte:** usuário ou sistema contendo dado pessoal.
- **Estímulo:** envia informação além da finalidade autorizada.
- **Ambiente:** operação normal ou suporte.
- **Artefato:** entrada, contexto, memória, logs e fornecedor de modelo.
- **Resposta:** minimiza, mascara, impede retenção indevida e registra a política aplicada.
- **Medida:** 100% dos campos classificados recebem o tratamento definido; exclusões são concluídas no prazo acordado.

## Segurança

- **Fonte:** conteúdo externo malicioso.
- **Estímulo:** tenta alterar instruções, extrair segredo ou acionar ferramenta sem autorização.
- **Ambiente:** sessão autenticada com recuperação e ferramentas habilitadas.
- **Artefato:** orquestrador, contexto e catálogo de ferramentas.
- **Resposta:** isola instruções não confiáveis, nega a ação, preserva segredos e produz evento auditável.
- **Medida:** nenhum cenário crítico do conjunto adversarial executa ação proibida; detecção e registro ocorrem em até 5 s.

## Confiabilidade

- **Fonte:** falha de modelo ou dependência.
- **Estímulo:** serviço primário retorna erro, timeout ou degradação.
- **Ambiente:** produção sob carga normal.
- **Artefato:** gateway, orquestração e experiência do usuário.
- **Resposta:** aplica timeout, retry seguro ou fallback; informa limites sem duplicar ações.
- **Medida:** disponibilidade mensal de 99,9% para o caminho essencial e zero duplicação em operações idempotentes testadas.

## Observabilidade

- **Fonte:** operador ou rotina de detecção.
- **Estímulo:** investiga uma resposta de baixa qualidade ou ação incorreta.
- **Ambiente:** produção, respeitando políticas de privacidade.
- **Artefato:** traces, métricas, logs e versões de configuração.
- **Resposta:** correlaciona solicitação, recuperação, modelo, ferramentas, guardrails e resultado.
- **Medida:** 95% dos casos amostrados são reconstruídos em menos de 15 min sem expor dado não autorizado.

## Explicabilidade

- **Fonte:** usuário, auditor ou responsável pela decisão.
- **Estímulo:** solicita a base de uma recomendação.
- **Ambiente:** após uma resposta ou ação relevante.
- **Artefato:** saída, evidências e registro de decisão do sistema.
- **Resposta:** apresenta fatores, fontes e limites compreensíveis, sem alegar acesso a raciocínio interno do modelo.
- **Medida:** 90% dos avaliadores identificam corretamente evidência e limite em teste de compreensão.

## Manutenibilidade

- **Fonte:** equipe de plataforma.
- **Estímulo:** substitui modelo, prompt ou política aprovada.
- **Ambiente:** pipeline de entrega com suíte de avaliação disponível.
- **Artefato:** adaptadores, configurações e testes.
- **Resposta:** executa regressão, compara resultados e permite rollback independente.
- **Medida:** mudança de modelo sem alterar consumidores em até um dia útil; restauração em até 30 min.

## Autonomia

- **Fonte:** agente diante de uma tarefa composta.
- **Estímulo:** propõe uma ação acima do limite de risco, custo ou escopo.
- **Ambiente:** execução com identidade delegada.
- **Artefato:** políticas, planejador e ferramentas.
- **Resposta:** interrompe, solicita aprovação humana ou recua para workflow determinístico.
- **Medida:** 100% das ações classificadas como críticas exigem aprovação; nenhuma ultrapassa orçamento de etapas e custo.

## Como usar o catálogo

Priorize poucos cenários arquiteturalmente significativos. Medidas numéricas acima são exemplos completos, não metas universais. Registre a justificativa para cada limiar, associe mecanismos de arquitetura e mantenha evidências de teste ou monitoramento.
