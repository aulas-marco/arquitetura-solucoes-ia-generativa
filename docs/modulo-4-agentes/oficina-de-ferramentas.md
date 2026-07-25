# Oficina de ferramentas — workflow, aprovação e efeito simulado

**Objetivo Bloom:** Aplicar e Analisar.

Esta oficina executa um workflow local que separa intenção, aprovação e efeito. Nenhuma chamada alcança CRM, estoque, pedidos ou qualquer sistema externo.

## Ferramenta

**LangGraph** é uma biblioteca open source para definir grafos de estado. O grafo Boreal desta prática tem três resultados explícitos: `aguardando_aprovacao`, `reservado` e `outcome_unknown`.

**Decisão arquitetural em foco:** em que fronteira uma intenção deixa de ser texto proposto e passa a produzir um efeito que exige autorização?

## Pré-requisitos

- Python 3.10 ou superior e terminal.
- Uma pasta descartável e somente os dados sintéticos do laboratório.
- O arquivo `troca_boreal.py` baixado na etapa seguinte.

## Instalação

### macOS

```bash
python3 --version
mkdir oficina-m4
cd oficina-m4
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install langgraph langchain-ollama
```

### Linux

No terminal Linux, execute:

```bash
python3 --version
mkdir oficina-m4
cd oficina-m4
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install langgraph langchain-ollama
```

### Windows

No PowerShell, execute:

```powershell
python --version
mkdir oficina-m4
cd oficina-m4
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install langgraph langchain-ollama
```

> **Ao retomar a prática:** se você fechar o terminal, volte para `oficina-m4` e reative o ambiente: no macOS/Linux, `source .venv/bin/activate`; no Windows/PowerShell, `.venv\Scripts\Activate.ps1`. Com o ambiente ativo, `python` funciona nos três sistemas.

## Preparação do laboratório

Baixe [troca_boreal.py](../assets/labs/modulo-4/troca_boreal.py) para a pasta `oficina-m4`. O arquivo contém um pedido fictício `PED-104`, uma chave de idempotência `TROCA-PED-104-1` e uma reserva simulada `RES-501`.

```bash
ls troca_boreal.py
```

O script é o workflow inteiro: cada nó devolve um estado tipado e o grafo escolhe entre aguardar aprovação ou reservar. Não há ferramenta externa escondida.

## Execução

Primeiro execute sem aprovação:

```bash
python troca_boreal.py --aprovado false
```

Depois execute com aprovação e, por fim, repita a mesma intenção:

```bash
python troca_boreal.py --aprovado true
python troca_boreal.py --aprovado true --repetir
```

## Receita principal

O script percorre o grafo completo e imprime o estado após o nó de aprovação. O resultado `RES-501` é uma confirmação simulada e tipada; ele não é uma frase produzida pelo modelo.

Leia as linhas `ESTADO`, `CHAVE`, `RESULTADO` e `TRACE` de cada execução. Sem aprovação, o estado esperado é `aguardando_aprovacao` e o resultado é “nenhum efeito”. Com aprovação, o estado é `reservado` e o resultado é `RES-501`. Na repetição, o trace declara que não foi criada uma segunda reserva.

## Resultado esperado

Você terá três traces comparáveis: parada segura, efeito simulado aprovado e repetição idempotente. A prática mostra o fluxo de controle, não prova que a autorização de uma organização real está correta.

## Interpretação

Altere apenas o argumento `--aprovado` ou `--repetir`; não modifique a chave de idempotência. Compare o ponto em que o workflow para, o resultado autoritativo e a evidência de repetição. Se uma confirmação tivesse sido interrompida após a intenção, o estado correto seria `outcome_unknown`: a arquitetura deveria consultar o registro pela chave antes de tentar novamente.

## Roteiro sugerido para aula

### Experimento A — intenção sem efeito (Essencial em aula)

**Objetivo**

Distinguir proposta e autorização.

**Pré-requisito**

Script instalado.

**Execute**

Use `--aprovado false`.

**Observe**

Parada em `aguardando_aprovacao`.

**Compare**

Pedido em linguagem natural e decisão de escrita.

**Questões exploratórias:**

- Que dado do estado mostra que nenhuma reserva ocorreu?
- Por que um modelo não deve decidir a aprovação por conta própria?
- Onde a identidade e a política entrariam em um sistema real?

### Experimento B — aprovação e idempotência (Exploração em dupla)

**Objetivo**

Observar uma escrita simulada e sua repetição.

**Pré-requisito**

Experimento A.

**Execute**

Use `--aprovado true` e depois `--repetir`.

**Observe**

`RES-501` e trace de repetição.

**Compare**

Primeira execução e segunda execução.

**Questões exploratórias:**

- Quem deve criar e guardar a chave de idempotência?
- Que falha uma chave duplicada evita?
- Por que a resposta do modelo não substitui o resultado autoritativo?

### Experimento C — resultado desconhecido (Extensão)

**Objetivo**

Planejar recuperação após confirmação ausente.

**Pré-requisito**

Traces anteriores.

**Execute**

Descreva a interrupção entre intenção e confirmação.

**Observe**

O limite entre repetir e reconciliar.

**Compare**

Retry cego, consulta por chave e escalonamento.

**Questões exploratórias:**

- Que componente deve persistir `outcome_unknown`?
- Qual dado é necessário para reconciliação?
- Quando a revisão humana é um controle obrigatório?

## Evidência a entregar

Entregue as três saídas ou uma tabela equivalente e uma conclusão de até cinco linhas.

| Execução | Estado | Chave | Resultado | O que a arquitetura comprovou? |
|---|---|---|---|---|
| Sem aprovação |  |  |  |  |
| Com aprovação |  |  |  |  |
| Repetição |  |  |  |  |

Explique qual condição impede a reserva, como a repetição é contida e como você trataria `outcome_unknown`. Registre também uma fitness function verificável — por exemplo, a mesma intenção com a mesma chave não pode produzir dois efeitos — e quem responde por seu alerta.

## Limpeza e contingência

Saia do ambiente com `deactivate` e apague a pasta `oficina-m4` quando terminar. Se houver erro, confira `python --version`, a ativação do ambiente e `python -m pip show langgraph`. Registre a mensagem e corrija a instalação local antes de continuar; não conecte o exercício a sistemas reais.

## Extensão — mini-fluxo Spec Kit

Esta segunda parte transforma uma solicitação curta em artefatos verificáveis. O objetivo não é aprender comandos por memorização, mas observar como cada etapa reduz uma incerteza diferente.

### Cenário sintético

A empresa fictícia Boreal possui um serviço pequeno que classifica o estado de pedidos. A nova demanda chega assim:

> “Permita marcar um pedido como aguardando confirmação do cliente.”

O repositório de laboratório não contém dados reais, credenciais ou integração externa. A feature altera apenas uma máquina de estados sintética.

Regras que o PO confirma:

- somente pedidos `em_separacao` podem mudar para `aguardando_confirmacao`;
- pedidos `despachados` ou `cancelados` são rejeitados;
- a transição registra ator, instante e motivo;
- repetir a mesma solicitação não cria segundo evento;
- a confirmação expira em 48 horas;
- envio de mensagem ao cliente está fora do escopo.

### Resultado de aprendizagem

Ao final, você deverá distinguir:

- requisito de decisão técnica;
- fato de hipótese;
- história de usuário de tarefa;
- critério de aceite de teste interno;
- gate humano de aprovação automática;
- evidência de atividade de evidência de conformidade.

### Preparar o ambiente do Spec Kit

A documentação oficial evolui. Consulte a versão fixada pela turma e não instale diretamente a versão mais recente num repositório corporativo sem revisão.

Com `uv` disponível:

```bash
uv tool install specify-cli
specify --help
mkdir boreal-sdd
cd boreal-sdd
git init
specify init . --integration copilot
```

Se a integração usada no seu ambiente for outra, escolha-a durante `specify init` ou siga a opção indicada pelo docente. Algumas integrações expõem comandos `/speckit.*`; outras usam skills equivalentes. Os artefatos são o objeto da aula, não a sintaxe exata da interface.

### Passo 0 — escrever uma constitution pequena

Execute no agente compatível:

```text
/speckit.constitution
O projeto Boreal deve:
1. manter transições de estado explícitas;
2. escrever teste antes de comportamento novo;
3. preservar idempotência de comandos;
4. registrar auditoria sem dados pessoais;
5. rejeitar mudanças fora do escopo da feature.
```

Abra a constitution gerada. Verifique se as frases produzem consequência. “Código deve ter qualidade” é vago; “comportamento novo começa por teste que falha” pode bloquear uma implementação.

**Gate 0 — princípios**

Responda:

- Que plano seria rejeitado por cada princípio?
- Algum princípio prescreve tecnologia sem necessidade?
- Há conflito entre simplicidade e auditoria?

Edite o documento até conseguir responder. Registre o commit:

```bash
git add .
git commit -m "docs: establish Boreal development principles"
```

### Passo 1 — gerar a specification

Execute:

```text
/speckit.specify
Adicionar o estado aguardando confirmação do cliente ao serviço Boreal.
Somente pedidos em separação podem entrar nesse estado. A transição
registra ator, instante e motivo, é idempotente e expira em 48 horas.
Não enviar mensagens e não conectar sistemas externos.
```

Leia `spec.md` antes de aceitar. Procure:

- problema e ator;
- história prioritária;
- requisitos funcionais;
- critérios de aceite;
- casos extremos;
- fora de escopo;
- marcadores de incerteza.

O agente pode ter inventado detalhes: formato do identificador, fuso horário, política de reativação ou papel autorizado. Marque-os como desconhecidos. Não deixe plausibilidade virar requisito.

### Passo 2 — clarificar uma pergunta por vez

Use `/speckit.clarify` ou conduza manualmente:

1. Quem pode solicitar a transição?
2. O que acontece quando 48 horas terminam?
3. Repetição usa qual identidade lógica?
4. Motivo é texto livre ou código?
5. Como o consumidor observa rejeição?

Para o laboratório, adote:

- papel `atendimento`;
- expiração retorna pedido a `em_separacao`;
- chave de idempotência é obrigatória;
- motivo é enumeração `cliente_ausente | divergencia_endereco | confirmacao_item`;
- rejeições são erros tipados.

Atualize a spec com as respostas. Crie um pequeno ledger:

| Item | Estado | Evidência |
|---|---|---|
| expiração em 48 h | fato decidido | aprovação do PO no laboratório |
| volume de pedidos | desconhecido | não altera a feature local |
| envio de mensagem | fora de escopo | solicitação original |
| armazenamento definitivo | decisão de plano | ainda aberta |

### Gate 1 — intenção

Troque a spec com outra pessoa. Ela deve conseguir responder:

- qual comportamento será construído;
- quais transições são válidas e inválidas;
- como reconhecer idempotência;
- o que ocorre após 48 horas;
- o que não será implementado.

Se duas interpretações forem possíveis, volte à clarificação. Só então marque a versão aprovada:

```bash
git add specs .specify
git commit -m "docs: specify pending customer confirmation"
```

### Passo 3 — planejar a arquitetura

Execute:

```text
/speckit.plan
Usar Python 3.12, biblioteca padrão e unittest. Representar a máquina
de estados como módulo de domínio com interface pública pequena.
Persistência do laboratório é em memória. Expor uma CLI JSON para
demonstrar transições, sem API ou banco de dados.
```

O plano deve mostrar:

- arquivos criados e responsabilidades;
- seam pública da máquina de estados;
- representação de pedido, comando e evento;
- erros tipados;
- estratégia de idempotência;
- relógio controlável para testar 48 horas;
- ordem teste → implementação;
- ausência de integração externa.

Uma interface possível:

```python
def request_customer_confirmation(
    order: Order,
    command: ConfirmationCommand,
    now: datetime,
) -> TransitionResult:
    ...
```

O plano não deve criar framework, banco, fila ou servidor “para futuro”. A persistência em memória é uma restrição deliberada do laboratório.

### Passo 4 — verificar a constitution

Antes de tarefas, confronte plano e princípios:

| Princípio | Evidência no plano |
|---|---|
| transições explícitas | tabela de estados e erros |
| teste primeiro | ordem das tarefas |
| idempotência | command key e evento único |
| auditoria mínima | ator, instante, código de motivo |
| fora de escopo | nenhuma mensagem ou integração |

Se alguma célula estiver vazia, o plano não está pronto.

### Gate 2 — arquitetura

Peça que outra pessoa faça duas perguntas:

1. A interface permite testar comportamento sem conhecer implementação?
2. Há componente ou dependência que não deriva da spec?

Registre ajustes e aprovação do plano.

### Passo 5 — derivar tarefas verticais

Execute:

```text
/speckit.tasks
```

Avalie o resultado. Uma decomposição adequada pode ser:

1. rejeitar estado de origem inválido pela interface pública;
2. aceitar transição válida e emitir evento auditável;
3. deduplicar repetição pela chave;
4. expirar após 48 horas com relógio controlado;
5. expor a trajetória pela CLI JSON.

Cada tarefa contém teste, implementação mínima, comando de verificação e arquivos. Evite:

```text
T1 criar todos os modelos
T2 criar todas as regras
T3 criar todos os testes
T4 criar a CLI
```

Essa divisão é horizontal e posterga evidência. Reescreva tarefas como fatias demonstráveis.

### Passo 6 — analisar consistência

Use `/speckit.analyze` quando disponível ou preencha:

| Requisito | Plano | Tarefa | Teste previsto |
|---|---|---|---|
| origem em separação | regra de domínio | T1/T2 | válido e inválido |
| auditoria | evento | T2 | campos mínimos |
| idempotência | command key | T3 | repetição |
| expiração | relógio injetado | T4 | antes/depois de 48 h |
| sem mensagem | fora de escopo | nenhuma | busca por integração ausente |

Um requisito sem tarefa é lacuna. Uma tarefa sem requisito pode ser infraestrutura necessária ou scope creep; peça justificativa.

### Passo 7 — implementar uma fatia

Execute somente a primeira tarefa com `/speckit.implement` ou equivalente. Antes de aceitar código, observe:

1. teste criado;
2. teste falha porque o comportamento não existe;
3. implementação mínima;
4. teste passa;
5. regressão permanece verde;
6. diff não introduz trabalho de tarefas futuras.

Registre a saída red e green. Se o agente criar teste e código juntos, reverta a implementação da fatia, execute o teste para confirmar a falha e reintroduza o código. O laboratório avalia evidência, não velocidade.

### Passo 8 — revisão em dois eixos

Faça duas leituras independentes.

**Revisão de Spec**

- origem inválida é rejeitada?
- erro é observável?
- nenhuma mensagem é enviada?
- a fatia atende somente o critério escolhido?

**Revisão de Standards**

- nomes usam linguagem do domínio?
- seam pública é pequena?
- teste depende apenas do contrato?
- código possui duplicação ou abstração prematura?

Não una os resultados numa nota única. Liste achados por eixo.

### Gate 3 — entrega

Para a feature completa, o gate recebe:

- constitution usada;
- spec aprovada;
- plano e matriz de cobertura;
- tarefas concluídas;
- saídas red/green;
- suíte completa;
- dois relatórios de revisão;
- diff;
- limitações do laboratório.

Nenhum desses itens isolado prova conclusão. Juntos, permitem reconstruir a transformação.

### Evidência a entregar

Entregue uma pasta ou arquivo compactado com:

```text
constitution.md
spec.md
plan.md
tasks.md
coverage-matrix.md
test-evidence.txt
review-spec.md
review-standards.md
```

Inclua uma reflexão de até 300 palavras:

1. Qual ambiguidade teria virado código sem clarificação?
2. Qual decisão permaneceu humana?
3. Onde a tarefa vertical reduziu risco?
4. Que parte do processo seria excessiva numa correção trivial?

### Alternativa demonstrativa sem CLI

Se o CLI não estiver disponível, crie manualmente os oito arquivos acima. Use os mesmos templates e gates. O método não depende da instalação. O docente pode fornecer artefatos incompletos para a turma identificar lacunas e produzir a matriz de cobertura.

### Limpeza do laboratório

Verifique que nenhum dado real ou token entrou no diretório:

```bash
git status --short
git grep -n -i "token\\|password\\|secret" || true
```

Saia do diretório e mova `boreal-sdd` para a lixeira. Se quiser preservar evidência, mantenha apenas o arquivo compactado entregue, sem ambiente virtual, caches ou credenciais.
