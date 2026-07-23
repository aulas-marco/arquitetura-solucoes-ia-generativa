# Padrões e decisões: integração, autonomia e recuperação

## Comece pelo contrato de ferramenta

Um **contrato de ferramenta** transforma uma capacidade corporativa em operação estreita, validável e auditável. “Acesso ao sistema de pedidos” é amplo demais. Prefira operações como `consultar_pedido`, `reservar_item` e `solicitar_cancelamento`, cada uma com efeito e política próprios.

O contrato mínimo declara:

| Campo | Pergunta que responde |
|---|---|
| nome, versão e finalidade | que capacidade está sendo invocada e por quê? |
| classe de efeito | é leitura, proposta, escrita reversível ou efeito irreversível? |
| esquema de entrada | tipos, obrigatoriedade, limites, enumerações e identificadores aceitos? |
| esquema de saída | dados, proveniência, versão do recurso e indicador de conclusão? |
| erros tipados | inválido, não autorizado, conflito, não encontrado, transitório ou definitivo? |
| identidade e autorização | quem age em nome de quem, com quais escopos e política? |
| idempotência e concorrência | qual chave evita duplicação e qual versão/precondição evita sobrescrita? |
| timeout e retry | quando desistir e quais erros permitem nova tentativa? |
| dados e auditoria | quais campos são sensíveis, mascarados, retidos e correlacionados? |
| compensação | como desfazer ou neutralizar o efeito, e quando isso é impossível? |

Descrições para o modelo incluem uso e não uso, mas o executor aplica as regras. O [Model Context Protocol](https://modelcontextprotocol.io/specification/2025-11-25) oferece uma especificação oficial de interoperabilidade entre aplicações e servidores que expõem contexto e ferramentas. Um protocolo padroniza comunicação; não decide política corporativa, semântica de transação ou adequação da ferramenta.

## APIs, mensageria, eventos e adaptadores

Use **API síncrona** quando o agente precisa do resultado para escolher o próximo passo e a dependência responde dentro do orçamento. O contrato deve definir timeout menor que o prazo total, erros e correlação. Não mantenha uma interação bloqueada indefinidamente.

Use **mensageria** para comandos assíncronos, filas de trabalho e absorção de picos. O envio aceito não significa efeito concluído. Estado precisa distinguir `solicitado`, `aceito`, `processando`, `concluído` e `falhou`; uma resposta posterior correlaciona `execution_id` e `command_id`.

Use **eventos** para comunicar fatos ocorridos — `ReservaExpirada`, não “talvez reserve”. Consumidores assumem entrega pelo menos uma vez, ordenação limitada e evolução de esquema. Deduplicação é responsabilidade do consumidor. Evento não deve carregar dado sensível além do necessário.

Um **adaptador** protege o domínio de protocolos legados, campos instáveis e códigos opacos. Traduz contrato canônico para SOAP, arquivo, terminal ou API antiga; normaliza erros; aplica timeout; correlaciona chamadas; e impede que peculiaridades do legado entrem no prompt. Quando o legado não oferece idempotência, o adaptador pode usar registro transacional próprio, consulta de reconciliação e chave de negócio — ou classificar a ação como não repetível e exigir intervenção.

## Identidade do usuário e autorização delegada

A ação precisa preservar **identidade do usuário**, aplicação, executor e aprovador. Evite uma conta técnica onipotente apresentada ao modelo. Na **autorização delegada**, a aplicação recebe autoridade limitada para agir em nome do usuário, com escopos reduzidos, recurso, finalidade e duração. Tokens e segredos ficam no executor, nunca no contexto do modelo.

Em cada chamada:

1. autentique usuário e serviço;
2. derive um token delegado de curta duração ou decisão equivalente;
3. reduza escopo à ferramenta e ao recurso;
4. avalie política com identidade, risco, parâmetros, estado e consentimento;
5. execute usando credencial fora do prompt;
6. registre ator, sujeito, delegador, aprovador, política e resultado.

Revalide na execução, não apenas quando o plano foi criado. Uma permissão pode ser revogada durante espera por aprovação. Delegação não transfere responsabilidade para o modelo; torna a cadeia explícita e revogável.

## Idempotência, concorrência e prevenção de repetição

**Idempotência** faz repetições equivalentes produzirem um único efeito lógico. O orquestrador gera uma chave estável a partir da execução e da intenção de ação, persiste-a antes da chamada e reutiliza-a em retry. O sistema de destino armazena chave e resultado. Não crie nova chave a cada tentativa.

Idempotência não resolve tudo. Para atualizar um pedido, envie a versão observada (`if-match` ou precondição) para detectar concorrência. Para impedir loops, registre uma assinatura de ferramenta, argumentos canônicos e versão de estado. Se a mesma chamada já concluiu, devolva o resultado persistido; se está em andamento, aguarde ou reconcilie; se falhou definitivamente, não repita por reformulação textual.

## Timeout, retry e circuit breaker

Todo limite local deve caber no **orçamento de tempo** da execução. Um **timeout** encerra a espera, não prova que o destino não executou. Após timeout de escrita, consulte por chave de idempotência antes de tentar novamente.

**Retry** é apropriado para falhas transitórias e operações idempotentes, com número limitado, backoff e jitter. Erro de validação, autorização, conflito de negócio ou saldo insuficiente é definitivo até mudança de estado; repetir consome custo e pode amplificar incidente.

O **circuit breaker** abre após padrão de falhas, evita pressão sobre uma dependência degradada e testa recuperação de forma controlada. Quando aberto, o agente não procura um endpoint equivalente para contornar a proteção. Ele usa fallback aprovado, pausa ou encaminha.

## Consistência, transações e compensação

Uma trajetória entre CRM, estoque e pedidos raramente participa de transação ACID única. Modele uma saga: cada efeito local confirma e produz estado durável; falhas posteriores acionam **compensação** na ordem apropriada. Liberar uma reserva pode compensar a criação da reserva. Não é “rollback” perfeito: uma mensagem enviada ou produto despachado pode ser irreversível. Nesses casos, compense por neutralização, correção ou processo humano e registre efeito residual.

Defina precondição e compensação antes de oferecer uma ferramenta de escrita. A compensação tem contrato, autorização, idempotência, timeout e observabilidade próprios. Se ela falhar, a execução entra em `compensation_pending`, alerta operações e não é marcada como resolvida.

## Auditoria e observabilidade

**Auditoria** preserva evidência de responsabilidade; **observabilidade** ajuda a entender comportamento e saúde. Um trace correlaciona solicitação, versões de modelo/prompt/política, catálogo oferecido, saída estruturada, validações, decisão de autorização, aprovação, chamada, tentativas, resultado, custo e compensação. Registre parâmetros minimizados ou hashes quando o conteúdo for sensível.

As [convenções semânticas de IA generativa do OpenTelemetry](https://github.com/open-telemetry/semantic-conventions-genai) são uma referência oficial para telemetria. Padronizar nomes não autoriza copiar prompts e dados pessoais. Retenção, acesso e mascaramento continuam sob política.

## Matriz de autonomia

Autonomia é atribuída por **ação e cenário**, não por produto inteiro. Os níveis abaixo não são uma escada obrigatória:

| Nível | Escolha do modelo | Efeito | Controle humano | Exemplo |
|---|---|---|---|---|
| A0 — sem autonomia | nenhuma | regra executa fluxo conhecido | responsável define processo | cálculo e consulta determinística |
| A1 — informar | gera resposta, sem ferramenta de efeito | nenhum | usuário interpreta | chatbot de políticas |
| A2 — recomendar | escolhe proposta ou ferramenta de leitura | pessoa executa | revisão antes de qualquer efeito | copiloto sugere troca |
| A3 — agir reversivelmente | escolhe leitura e escrita de baixo risco | reversível e limitada | aviso/contestação; amostra depois | criar reserva temporária |
| A4 — agir com aprovação | propõe ação material e aguarda | efeito após aprovação antes da ação | aprovador recebe evidência, parâmetros e prazo | cancelar pedido elegível |
| A5 — autonomia limitada | escolhe sequência e ações aprovadas por classe | efeitos dentro de limites estreitos | monitoramento e revisão humana depois da ação | ajuste operacional de baixo valor |

**Aprovação humana antes da ação** precisa ocorrer sobre objeto imutável: ferramenta, parâmetros, evidência, consequência, prazo e chave. Alterar parâmetros invalida aprovação. Aprovar “faça o necessário” não é controle.

**Revisão humana depois da ação** detecta desvio, corrige política e permite recurso; não retroativamente autoriza dano. Só serve quando o efeito é aceitável, reversível ou de baixo risco. Amostragem, alertas e prazo de contestação devem ser definidos. Ação crítica continua exigindo aprovação prévia, como pede o cenário de [Autonomia](../referencia/atributos-de-qualidade.md#autonomia).

## Orçamentos, interrupção e fallback

Um agente recebe **orçamento de etapas**, **orçamento de tempo** e **orçamento de custo**, além de limites de tokens, chamadas e ações de efeito. O contador é externo ao modelo e inclui retries, handoffs e compensações. Limites diferentes podem valer por classe de tarefa. Ao se aproximar do teto, o sistema resume estado, evita nova ação material e escolhe conclusão parcial, solicitação de dado, pausa ou escalonamento.

O fallback para **workflow determinístico** é uma rota projetada: por exemplo, coletar pedido e motivo, validar regras conhecidas e abrir tarefa humana. Não entregue silenciosamente a mesma ação a um modelo mais barato ou ferramenta alternativa com política diferente. Fallback preserva identidade, estado, idempotência e informação clara sobre o que não foi concluído.

## Agente único versus múltiplos agentes

Comece com agente único e ferramentas estreitas. Adote múltiplos agentes apenas se um experimento demonstrar benefício de especialização, isolamento de contexto/autoridade ou paralelismo. Compare taxa de conclusão, ações indevidas, handoffs, latência, custo e capacidade de reconstruir traces. Um supervisor não elimina falha: precisa de contrato de delegação, orçamento global, regra de consenso e autoridade para interromper. Nunca permita que subagentes ampliem escopo, criem credenciais ou deleguem indefinidamente.

Esses mecanismos aparecem juntos no [Exemplo arquitetural](exemplo-arquitetural.md).

## Padrão — Desenvolvimento guiado por especificação

**Contexto.** Um agente de codificação pode alterar múltiplos artefatos e executar ferramentas rapidamente.

**Problema.** Pedidos vagos transformam implementação em interpretação silenciosa; testes podem passar sem atender à necessidade original.

**Solução.** Manter constitution, spec, plan e tasks como contratos explícitos. Implementar em fatias verificáveis, testar nas interfaces acordadas e revisar separadamente padrões do repositório e aderência à spec.

**Consequências.** Há mais preparação e gates, mas decisões, critérios de aceite e riscos permanecem auditáveis. O modelo ganha autonomia limitada para implementar; não ganha autoridade para redefinir o objetivo.

> **Decisão arquitetural:** posicione gates humanos após a specification, após verify e antes da liberação. Um gate deve receber artefatos imutáveis, evidência de testes e o diff correspondente.

## Decisão 1 — escolher a profundidade proporcional

O método deve acompanhar risco e incerteza. Aplicar o mesmo pacote documental a toda alteração transforma SDD em fila de aprovação; aplicar somente a mudanças grandes permite que riscos pequenos e frequentes se acumulem.

Use três classes:

| Classe | Situação | Contrato mínimo |
|---|---|---|
| S — localizada | comportamento conhecido, baixo blast radius, reversível | problema, teste de regressão, diff e revisão |
| M — feature | novo comportamento, mais de um componente ou decisão | spec, critérios, plano, fatias, testes e gates 1/3 |
| L — iniciativa | múltiplos domínios, migração, risco material ou vários times | constitution aplicável, spec, arquitetura, ADRs, plano, grafo de tarefas e três gates |

Classifique pelo maior risco, não pelo número de linhas. Uma mudança curta em autorização pode ser classe L; uma migração mecânica extensa pode ser classe M com estratégia *expand–contract*. Registre o motivo da classificação para que a simplificação seja uma decisão, não omissão.

> **Decisão arquitetural:** adote classe M como padrão para comportamento novo. Reduza para S ou eleve para L por critérios explícitos de risco, reversibilidade, coordenação e evidência.

## Decisão 2 — separar “o quê” de “como”

Misturar tecnologia na spec torna a intenção instável. “Usuário baixa CSV” pode ser requisito; “endpoint FastAPI usa Celery e S3” pertence ao plano. A separação permite:

- comparar arquiteturas sem reescrever o problema;
- mudar tecnologia preservando critérios;
- revisar produto e arquitetura por autoridades diferentes;
- gerar mais de um plano a partir da mesma intenção;
- localizar onde ocorreu uma decisão incorreta.

Há exceções: uma restrição tecnológica pode ser requisito quando vem do ambiente — “deve operar desconectado”, “deve usar a identidade corporativa”, “não pode transferir dados para fora do país”. Nesse caso, registre a restrição e sua fonte na spec; o plano decide como atendê-la.

Use este teste: se a tecnologia fosse substituída por outra equivalente, a necessidade do usuário continuaria a mesma? Se sim, mantenha-a fora da especificação funcional.

## Decisão 3 — formular critérios antes de tarefas

Tarefas derivadas de requisitos sem critérios de aceite viram atividades, não compromissos de comportamento. Antes de fatiar, escreva exemplos observáveis:

```gherkin
Cenário: exportação expira
  Dado que uma exportação foi criada há mais de 24 horas
  Quando o solicitante usa o link original
  Então o sistema nega o download
  E permite solicitar uma nova exportação
  E registra o motivo sem persistir o conteúdo exportado
```

Esse cenário cria trabalho em autorização, UX, expiração, auditoria e teste. Sem ele, “implementar expiração” pode significar apagar um arquivo, esconder um botão ou invalidar um token, cada opção com consequências diferentes.

Critérios não devem prescrever asserts internos. Devem descrever comportamento e propriedades relevantes. Para atributos de qualidade, use cenários:

```text
Fonte: gestor autenticado
Estímulo: solicita 50 mil registros autorizados
Ambiente: horário de pico
Resposta: sistema aceita, processa e disponibiliza arquivo
Medida: 95% concluídos em até 30 s; nenhuma linha fora do escopo
```

> **Decisão arquitetural:** nenhuma tarefa de implementação é considerada pronta sem critério observável e método de verificação associado.

## Decisão 4 — fatiar verticalmente

Uma fatia vertical entrega uma trajetória estreita de ponta a ponta. Para exportação:

1. solicitar exportação vazia e observar estado pendente;
2. gerar arquivo com um tipo de registro autorizado;
3. adicionar processamento assíncrono e consulta de estado;
4. adicionar expiração e nova solicitação;
5. ampliar volume e medir SLO.

Cada fatia possui comportamento demonstrável e mantém a suíte verde. Uma decomposição horizontal — tabela, repositório, serviço, API, interface — só demonstra valor depois de integrar tudo. Também aumenta a probabilidade de agentes implementarem suposições incompatíveis em paralelo.

Tarefas paralelas devem ter:

- arquivos ou componentes com baixa sobreposição;
- contratos já aprovados;
- resultados integráveis independentemente;
- bloqueadores explícitos;
- responsável pelo fechamento da integração.

Quando uma alteração ampla não pode ser fatiada sem quebrar consumidores, use **expand–contract**:

1. **expandir:** adicionar nova interface ao lado da antiga;
2. **migrar:** mover consumidores em lotes verificáveis;
3. **contrair:** remover a forma antiga quando não houver uso.

Esse padrão preserva integração contínua e reduz branches longas.

## Decisão 5 — escolher seams duráveis

Antes de gerar testes, identifique as interfaces pelas quais consumidores observam comportamento. Prefira poucas seams de alta alavancagem.

| Seam | Boa para | Evite |
|---|---|---|
| comando CLI | transformação ou operação reproduzível | testar cada função privada chamada |
| endpoint/contrato HTTP | autorização, validação e resposta | acoplar teste ao framework sem necessidade |
| evento publicado | integração assíncrona e esquema | afirmar ordem interna de métodos |
| função pública de domínio | regra determinística | mockar o próprio comportamento testado |
| adaptador | tradução de dependência externa | chamar serviço real em toda suíte |

Uma seam profunda permite trocar implementação mantendo contrato. Uma seam rasa expõe muitos detalhes e multiplica testes frágeis. O plano deve registrar assinatura, invariantes, tipos de erro e dados sensíveis de cada interface.

> **Decisão arquitetural:** teste comportamento na seam mais alta que permaneça rápida, determinística e diagnóstica; use testes internos apenas para propriedades que não podem ser observadas adequadamente por ela.

## Decisão 6 — usar revisão em dois eixos

Revisão de **Spec** pergunta:

- todas as histórias prioritárias foram atendidas?
- critérios possuem evidência?
- regras e fora de escopo foram respeitados?
- alguma decisão de produto foi inventada durante implementação?
- riscos e desconhecidos foram resolvidos ou continuam visíveis?

Revisão de **Standards** pergunta:

- a implementação segue convenções e arquitetura do repositório?
- interfaces e nomes expressam o domínio?
- há duplicação, acoplamento ou dependência injustificada?
- testes observam comportamento e sobrevivem a refatoração?
- segurança, privacidade e operação estão adequadas?

Os relatórios permanecem separados. Um “passa” em Standards não compensa requisito ausente; um “passa” em Spec não compensa vulnerabilidade crítica. Quando possível, use contextos de revisão independentes para reduzir ancoragem na solução do implementador.

Achados devem citar evidência: requisito, princípio, trecho de diff ou padrão do repositório. “Não gostei” não é finding; “o requisito FR-07 exige autorização por unidade, mas o endpoint filtra apenas por usuário” é.

## Decisão 7 — tratar segurança como parte da transformação

Segurança não é revisão posterior. A spec identifica ativos, atores, dados e usos proibidos; o plano define trust boundaries, identidade, autorização, proteção e observabilidade; tarefas carregam testes negativos; verificação compara o diff às ameaças.

Checklist mínimo:

- autenticação e autorização no servidor;
- princípio de menor privilégio;
- validação e normalização de entrada;
- dados pessoais minimizados em armazenamento e logs;
- segredos fora de prompts e repositório;
- dependências e imagens examinadas;
- ações materiais auditadas;
- falha segura e recuperação;
- abuso, automação e limites de taxa considerados;
- risco residual com dono e prazo.

Um agente de segurança pode aumentar cobertura, mas não aceita risco. Achado crítico bloqueia o gate até correção ou aceitação formal por autoridade competente.

## Decisão 8 — manter os artefatos coerentes

Artefatos vivos exigem regras de mudança:

| Mudança descoberta | Atualizar |
|---|---|
| necessidade ou regra | spec e critérios |
| restrição organizacional | constitution ou spec, conforme alcance |
| escolha técnica relevante | plano e ADR |
| nova dependência entre trabalhos | tasks |
| bug de comportamento | critério e teste de regressão |
| incidente ou métrica de produção | requisito de qualidade, risco e experimento |

Antes do merge, execute uma análise de cobertura:

```text
requisito → cenário → decisão/plano → tarefa → teste → evidência
```

Relações não precisam estar num sistema sofisticado. Identificadores estáveis e links bastam para começar. O importante é conseguir navegar em ambas as direções: “que código implementa FR-07?” e “por que esta validação existe?”.

Evite atualizar specs por regeneração cega. A alteração deve aparecer como diff revisável. Texto aprovado por pessoa não pode ser sobrescrito porque um novo template produziu formulação diferente.

## ADR — onde colocar os gates do fluxo SDD

**Contexto.** Gates demais criam espera; gates tardios deixam decisões caras chegarem ao final.

**Opções consideradas.**

1. **Somente revisão final:** menor interrupção, mas requisitos e arquitetura incorretos são descobertos depois do código.
2. **Gate em toda etapa:** alta supervisão, mas filas e aprovações mecânicas reduzem fluxo.
3. **Três gates por mudança material:** intenção, arquitetura e entrega; etapas internas continuam dentro da autonomia aprovada.

**Decisão.** Usar três gates para classe L; gate de intenção e entrega para classe M; revisão final para classe S. Um gate é pulado apenas com motivo registrado.

**Consequências.** Decisões de maior custo são validadas antes; o time precisa manter critérios de entrada/saída claros e tempo de resposta dos responsáveis.

**Gatilho de revisão.** Se tempo em fila superar tempo de trabalho ou se defeitos escaparem apesar dos gates, revisar granularidade, autoridade e qualidade dos artefatos.

## ADR — Spec Kit como fio operacional, não como metodologia exclusiva

**Contexto.** A disciplina precisa de um fluxo reproduzível, mas ferramentas e integrações mudam.

**Opções consideradas.**

1. Ensinar princípios sem ferramenta: durável, porém abstrato para a oficina.
2. Tratar Spec Kit como padrão universal: concreto, porém cria acoplamento e confunde ferramenta com método.
3. Usar Spec Kit como implementação de referência e comparar variações.

**Decisão.** Adotar a terceira opção. Constitution, spec, plan, tasks e implement fornecem uma trajetória observável. Matt Pocock aprofunda *vertical slices*, deep modules, TDD e revisão em dois eixos; Kiro, BMAD e Tessl mostram outras escolhas de ambiente e artefatos.

**Consequências.** O aluno pratica comandos concretos e consegue transferir princípios. Materiais devem fixar versões e distinguir recurso atual de conceito durável.

**Gatilho de revisão.** Mudança incompatível nos comandos, templates ou licença; surgimento de alternativa que ofereça melhor acesso e evidência para a turma.
