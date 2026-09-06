# Decisões e limites do SDD

As oito decisões que calibram profundidade, fatiamento, seams e revisão, os dois ADRs que registram a escolha, e os casos em que o método vira cerimônia.

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
| função pública de domínio | regra determinística | simular o próprio comportamento testado |
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

## Quando SDD falha

SDD não corrige automaticamente entendimento ruim. Ele pode produzir **documentação em escala** sem produzir conhecimento. Os principais antipadrões são:

- **spec teatral:** documento extenso que não contém decisões nem critérios testáveis;
- **falsa precisão:** números e regras inventados pelo modelo para preencher lacunas;
- **waterfall regenerado:** tentar completar tudo antes de qualquer experimento;
- **artefatos divergentes:** spec, plano, tarefas e código evoluem separadamente;
- **aprovação automática:** o mesmo agente produz e “aprova” todos os artefatos;
- **task slicing horizontal:** tarefas por camada sem resultado demonstrável;
- **testes espelho:** testes copiam a implementação e não expressam intenção;
- **constitution ornamental:** princípios sem consequência sobre o plano;
- **regeneração destrutiva:** atualizar artefatos sobrescreve decisões humanas sem diff revisável;
- **contexto excessivo:** despejar todo o repositório no agente em vez de oferecer interfaces e fontes relevantes.

Também há tarefas em que o custo não compensa: correção óbvia e localizada com teste de regressão; atualização mecânica de dependência; protótipo descartável; exploração cuja finalidade é descobrir se uma abordagem é possível. Nesses casos, use um contrato menor: problema, limite, teste e evidência.

## Como medir adoção sem medir burocracia

Contar specs criadas incentiva produção de arquivos. Métricas melhores observam efeito:

| Pergunta | Indicador possível |
|---|---|
| intenção ficou clara antes do código? | percentual de implementações iniciadas após aceite versionado |
| tarefas carregavam trajetórias completas? | percentual de fatias demonstráveis sem esperar outras camadas |
| testes nasceram dos critérios? | cobertura de critérios por cenários, não apenas linhas |
| implementação respeitou a spec? | desvios encontrados na revisão de aderência |
| segurança entrou cedo? | riscos críticos descobertos antes e depois da implementação |
| artefatos permaneceram vivos? | mudanças de comportamento acompanhadas por atualização de spec/teste |
| o método melhorou fluxo? | tempo de clarificação, retrabalho, lead time e defeitos escapados |

Velocidade de geração isolada é uma métrica perigosa. Se o agente produz mais código e aumenta retrabalho, o sistema local ficou rápido e o fluxo global piorou.

## O que permanece humano

SDD desloca trabalho, não elimina responsabilidade. Pessoas continuam responsáveis por:

- escolher problemas que merecem investimento;
- ouvir usuários e reconhecer conflito de interesses;
- aceitar risco e consequências;
- decidir trade-offs arquiteturais;
- identificar quando a linguagem não representa o domínio;
- julgar suficiência de evidência;
- responder por efeitos em produção.

Agentes ampliam pesquisa, comparação, consistência, geração e revisão. Eles são particularmente úteis para manter relações entre muitos artefatos. Mas não possuem mandato organizacional. A spec não é central porque foi escrita em linguagem natural; é central porque pessoas autorizadas a adotaram como contrato e mantêm mecanismos para testá-la.
