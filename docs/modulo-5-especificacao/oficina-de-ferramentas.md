# Oficina de ferramentas — mini-fluxo com Spec Kit

**Objetivo Bloom:** Aplicar e Analisar.

Esta oficina transforma uma solicitação curta em artefatos verificáveis. O objetivo não é decorar comandos, e sim observar como cada etapa reduz uma incerteza diferente.

<a id="extensao-mini-fluxo-spec-kit"></a>

## Ferramenta

O **Spec Kit** é um conjunto de comandos open source, mantido pelo GitHub, que instala num repositório os *templates* e os passos do fluxo guiado por especificação: `constitution`, `specify`, `clarify`, `plan`, `tasks`, `analyze`, `implement` e `verify`. Ele não gera software sozinho: cada comando é executado por um agente de codificação já instalado na sua máquina, e o que o Spec Kit acrescenta são os artefatos e a ordem em que eles aparecem.

**Decisão arquitetural em foco:** qual profundidade de especificação uma mudança merece, e qual portão pode barrá-la antes que o código exista?

## Pré-requisitos

- Um agente de codificação com modelo de fronteira: GitHub Copilot, Claude Code ou Codex CLI. A subseção de instalação explica por que um modelo local pequeno não sustenta este fluxo.
- `git` e `uv` disponíveis no terminal.
- Uma pasta descartável. Nenhum dado real, credencial ou repositório de cliente entra neste laboratório.

## Cenário sintético

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

## Resultado de aprendizagem

Ao final, você deverá distinguir:

- requisito de decisão técnica;
- [fato de hipótese](fluxo.md#3-clarify-que-ambiguidades-mudariam-a-solucao);
- história de usuário de tarefa;
- critério de aceite de teste interno;
- [gate humano](fluxo.md#tres-gates-dois-papeis-humanos) de aprovação automática;
- evidência de atividade de evidência de conformidade.

## Instalação

A documentação oficial evolui. Consulte a versão fixada pela turma e não instale diretamente a versão mais recente num repositório corporativo sem revisão.

### macOS

```bash
uv tool install specify-cli
specify --help
mkdir boreal-sdd
cd boreal-sdd
git init
```

### Linux

```bash
uv tool install specify-cli
specify --help
mkdir boreal-sdd
cd boreal-sdd
git init
```

### Windows

No PowerShell:

```powershell
uv tool install specify-cli
specify --help
mkdir boreal-sdd
cd boreal-sdd
git init
```

Escolha a integração conforme o agente disponível na sua máquina:

```bash
specify init . --integration copilot   # GitHub Copilot
specify init . --integration claude    # Claude Code
specify init . --integration codex     # Codex CLI (OpenAI)
```

Use só um dos três comandos acima. Se a integração usada no seu ambiente for outra, escolha-a durante `specify init` ou siga a opção indicada pelo docente. O próprio `specify init` imprime, em "Next Steps", o nome exato de cada comando ou skill instalado para a integração escolhida — use essa lista como referência, pois o formato muda entre versões e integrações (por exemplo, `/speckit-constitution` com hífen na integração `copilot` desta prática, em vez do `/speckit.constitution` com ponto usado abaixo como notação genérica). Os artefatos são o objeto da aula, não a sintaxe exata da interface.

**Limitação testada: modelos locais pequenos não sustentam este fluxo.** Um agente de codificação apontado para um modelo Llama local via Ollama (testado nesta oficina com `llama3.2:3b`, `llama3.1:8b` e `qwen2.5-coder:7b`, este último recomendado pela própria documentação do Goose para uso agêntico) não completou o primeiro comando (`/speckit.constitution`) em nenhum dos três casos. Em vez de editar o arquivo de verdade, o agente travou, pediu esclarecimento ao usuário ou, no caso mais enganoso, devolveu um relatório de sucesso completo (versão, justificativa, mensagem de *commit* sugerida) sem que o arquivo no disco tivesse mudado uma linha. Use Copilot, Claude Code ou Codex CLI, como acima: é a integração com modelos de fronteira que este exercício pressupõe.

## Preparação do laboratório

O repositório de laboratório não contém dados reais, credenciais ou integração externa. A *feature* altera apenas uma máquina de estados sintética, descrita no cenário acima.

## Execução

Cada comando roda dentro de `boreal-sdd`, no agente de codificação escolhido. O laboratório não tem script para executar: o artefato produzido em cada passo é o resultado.

## Receita principal

Percorra os passos 0 a 8 na ordem, parando nos três portões. Em uma aula curta, execute até o Gate 1 em conjunto e deixe os passos 3 a 8 para o trabalho assíncrono.

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

Abra a [constitution](modos-de-trabalho.md#constitution-principios-antes-da-feature) gerada. Verifique se as frases produzem consequência. “Código deve ter qualidade” é vago; “comportamento novo começa por teste que falha” pode bloquear uma implementação.

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

Leia [`spec.md`](modos-de-trabalho.md#a-spec-como-artefato-central-e-vivo) antes de aceitar. Procure:

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

Atualize a spec com as respostas. Crie um pequeno [ledger](fluxo.md#3-clarify-que-ambiguidades-mudariam-a-solucao):

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

O [plano](fluxo.md#4-plan-como-a-arquitetura-realizara-a-intencao) deve mostrar:

- arquivos criados e responsabilidades;
- [seam](fluxo.md#deep-modules-e-testes-pelas-seams) pública da máquina de estados;
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

Essa divisão é horizontal e posterga evidência. Reescreva tarefas como [fatias demonstráveis](decisoes.md#decisao-4-fatiar-verticalmente).

### Passo 6 — analisar consistência

Use [`/speckit.analyze`](fluxo.md#6-analyze-os-artefatos-contam-a-mesma-historia) quando disponível ou preencha:

| Requisito | Plano | Tarefa | Teste previsto |
|---|---|---|---|
| origem em separação | regra de domínio | T1/T2 | válido e inválido |
| auditoria | evento | T2 | campos mínimos |
| idempotência | command key | T3 | repetição |
| expiração | relógio injetado | T4 | antes/depois de 48 h |
| sem mensagem | fora de escopo | nenhuma | busca por integração ausente |

Um requisito sem tarefa é lacuna. Uma tarefa sem requisito pode ser infraestrutura necessária ou scope creep; peça justificativa.

### Passo 7 — implementar uma fatia

Execute somente a primeira tarefa com [`/speckit.implement`](fluxo.md#7-implement-executar-decisoes-nao-reinventa-las) ou equivalente. Antes de aceitar código, observe:

1. teste criado;
2. teste falha porque o comportamento não existe;
3. implementação mínima;
4. teste passa;
5. regressão permanece verde;
6. diff não introduz trabalho de tarefas futuras.

Registre a saída red e green. Se o agente criar teste e código juntos, reverta a implementação da fatia, execute o teste para confirmar a falha e reintroduza o código. O laboratório avalia evidência, não velocidade.

### Passo 8 — revisão em dois eixos

Faça duas leituras independentes, seguindo a [revisão em dois eixos](decisoes.md#decisao-6-usar-revisao-em-dois-eixos).

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

## Resultado esperado

Ao final, existem oito arquivos versionados no repositório: constitution, spec, plano, tarefas, matriz de cobertura, evidência de teste e as duas revisões. Eles demonstram o encadeamento entre intenção e evidência; não demonstram que a *feature* está pronta para produção.

## Interpretação

Leia os artefatos em duas camadas. Primeiro, confira o encadeamento mecânico: todo requisito da spec aparece no plano, numa tarefa e num teste. Depois, avalie o que cada portão reteve. Um fluxo em que nenhum portão barrou nada é um fluxo que documentou uma decisão já tomada, e o custo dele não se justifica.

## Roteiro sugerido para aula

### Experimento A — a ambiguidade que vira código

**Objetivo**

Observar uma ambiguidade da demanda original ser capturada na clarificação em vez de virar implementação silenciosa.

**Pré-requisito**

Passos 0 a 2 concluídos, com a spec e as perguntas de clarificação no repositório.

**Execute**

Antes de responder às perguntas de clarificação, peça ao agente que implemente a *feature* direto a partir da spec do Passo 1, numa branch descartável.

**Observe**

Que decisão o agente tomou sozinho no lugar de cada pergunta em aberto, e se ela aparece em algum lugar além do código.

**Compare**

A branch descartável e a spec clarificada do Passo 2. A diferença entre as duas é o valor mensurável da etapa de clarificação nesta demanda.

**Questões exploratórias:**

- Qual das decisões implícitas seria cara de reverter depois de três meses em produção?
- Que portão teria barrado a implementação direta, e o que ele exigiria como evidência?
- Numa correção de rótulo, esse mesmo experimento produziria diferença? O que isso diz sobre profundidade proporcional?


### Experimento B — o portão que não barra nada

**Objetivo**

Distinguir um portão que decide de um portão que carimba, medindo o que cada um rejeita.

**Pré-requisito**

Constitution do Passo 0 escrita e Gate 1 já percorrido uma vez.

**Execute**

Reescreva a constitution trocando os cinco princípios por versões genéricas — “o código deve ter qualidade”, “decisões devem ser documentadas” — e refaça os passos 1 e 2 com ela.

**Observe**

Quantas propostas do agente a constitution genérica rejeita, e quantas a original rejeitava.

**Compare**

As duas execuções do Gate 1. Um princípio que nenhuma mudança plausível violaria não é princípio: é declaração de intenção.

**Questões exploratórias:**

- Como você escreveria um princípio que rejeita algo sem transformar o repositório em burocracia?
- Um portão que nunca barrou nada em seis meses está calibrado ou está ausente?
- Que evidência distinguiria as duas hipóteses acima?

### Experimento C — profundidade proporcional

**Objetivo**

Medir o custo do fluxo completo aplicado a uma mudança que não o merece.

**Pré-requisito**

Ambiente instalado e o fluxo percorrido ao menos até o Passo 3.

**Execute**

Aplique os oito passos a uma demanda trivial: corrigir um rótulo de interface, sem regra de negócio associada.

**Observe**

Quanto tempo cada artefato consome e qual deles não produziu nenhuma decisão.

**Compare**

O conjunto de artefatos desta execução com o da demanda original. A diferença é o que a [Decisão 1](decisoes.md#decisao-1-escolher-a-profundidade-proporcional) chama de profundidade proporcional.

**Questões exploratórias:**

- Que critério, escrito em uma frase, separaria as duas demandas antes de começar?
- Qual artefato você manteria mesmo na demanda trivial, e por quê?
- Quem decide a profundidade quando a pessoa que implementa e a que aprova discordam?

## Evidência a entregar

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

## Alternativa demonstrativa sem CLI

Se o CLI não estiver disponível, crie manualmente os oito arquivos acima. Use os mesmos templates e gates. O método não depende da instalação. O docente pode fornecer artefatos incompletos para a turma identificar lacunas e produzir a matriz de cobertura.

## Limpeza e contingência

Verifique que nenhum dado real ou token entrou no diretório:

```bash
git status --short
git grep -n -i "token\\|password\\|secret" || true
```

Saia do diretório e mova `boreal-sdd` para a lixeira. Se quiser preservar evidência, mantenha apenas o arquivo compactado entregue, sem ambiente virtual, caches ou credenciais.

## Ferramentas adicionais

O laboratório usou o Spec Kit para tornar o fluxo observável. O mercado tem outras formalizações do mesmo raciocínio, comparadas no [apêndice da síntese](sintese-e-referencias.md#comparacao-das-abordagens). Investigação livre, fora do escopo avaliado desta oficina.

| Ferramenta | Site | Propósito |
|---|---|---|
| Spec Kit | [github.com/github/spec-kit](https://github.com/github/spec-kit) | Fluxo de referência desta oficina, mantido pelo GitHub |
| Kiro | [kiro.dev/docs/specs](https://kiro.dev/docs/specs/) | Requisitos, design e tarefas próximos ao IDE, com EARS |
| BMAD-METHOD | [github.com/bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | Papéis e histórias para coordenar vários agentes |
| Tessl | [tessl.io](https://tessl.io) | Spec residente e reuso por registro |
