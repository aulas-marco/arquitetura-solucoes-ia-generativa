# Requisitos significativos e táticas

Da característica de qualidade ao requisito arquiteturalmente significativo, e daí à tática que o realiza e ao critério que o aceita quando a saída é probabilística.

## Atributos de qualidade e RAS no contexto generativo

Diferente de sistemas determinísticos, o desenho conceitual para IA exige que o arquiteto defina **critérios de aceitação para comportamentos probabilísticos**. Isso significa que os atributos de qualidade clássicos (performance, segurança, escalabilidade) devem ser estendidos para incluir a **confiabilidade e a observabilidade das respostas**.

Características arquiteturais não são uma lista de desejos. Segurança, privacidade, proveniência, latência, custo, confiabilidade, observabilidade e modificabilidade competem entre si. A equipe precisa limitar as prioritárias, declarar a tensão aceita e definir medida, responsável e momento de revisão; a arquitetura adequada é a menos ruim para esse contexto, não a que maximiza uma característica isolada.

Um **requisito arquiteturalmente significativo (RAS)** é um requisito cuja satisfação influencia estruturas fundamentais, atravessa responsabilidades, cria dependência relevante, protege uma característica prioritária ou torna mudanças posteriores caras. Um cenário de qualidade bem formado — fonte, estímulo, ambiente, artefato, resposta e medida — ajuda a expressá-lo sem adjetivos vagos.

### Da característica à estrutura

Uma **tática arquitetural** é uma decisão de desenho dirigida à resposta de um atributo de qualidade. Ela é mais específica que uma intenção e menos concreta que sua implementação. Os termos próximos têm funções diferentes:

| Elemento | Função | Exemplo |
|---|---|---|
| Cenário de qualidade ou RAS | declara a resposta exigida | preservar a edição quando a inferência exceder dois segundos |
| Tática | controla a resposta ao atributo | timeout e preservação de estado |
| Mecanismo | realiza a tática neste sistema | limite no adaptador e rascunho persistido |
| Padrão | organiza uma solução recorrente | circuit breaker ou workflow com aprovação |
| Estilo arquitetural | impõe uma organização ampla a componentes e conectores | monólito modular ou serviços distribuídos |
| ADR | registra por que a combinação foi escolhida | adotar timeout de dois segundos e fluxo manual |

Uma tática não é necessariamente um componente. “Abstenção” pode exigir validação, interface e workflow; “proveniência” atravessa coleta, transformação, geração e auditoria. Um padrão pode combinar várias táticas, e o mesmo mecanismo pode participar de mais de uma.

### Composição e tensão entre táticas

Táticas raramente atuam sozinhas. A análise deve registrar efeitos colaterais:

| Tática ou combinação | Benefício pretendido | Tensão criada |
|---|---|---|
| cache seguro | reduz latência e custo | pode servir conteúdo desatualizado e amplia retenção |
| fallback de modelo | melhora disponibilidade | pode alterar qualidade, residência ou política de dados |
| trace detalhado | melhora diagnóstico e auditoria | pode expor conteúdo e elevar armazenamento |
| minimização antes da inferência | reduz exposição | pode remover contexto necessário à qualidade |
| revisão humana obrigatória | contém efeitos inadequados | aumenta tempo e pode virar aprovação ritual |

Não se escolhe uma tática por seu benefício isolado. A equipe avalia a resposta produzida, as características prejudicadas e o risco residual.

## 2. Identificar o que exige arquitetura

Objetivos de negócio, produto, dados e IA mostram resultados desejados. Alguns deles exigem somente trabalho local; outros mudam fronteiras, responsabilidades, interfaces ou opções futuras. Estes são os **requisitos arquiteturalmente significativos (RAS)**.

Um RAS costuma atravessar componentes, proteger uma característica sob condição relevante, impor obrigação ou dependência externa, ou tornar uma mudança posterior cara. Para cada um, descreva fonte, estímulo, ambiente, artefato, resposta e medida; acrescente prioridade, responsável e verificação.

![Fluxo do objetivo ao requisito arquiteturalmente significativo, à estrutura, fronteiras, evidência e ADR](../assets/images/m02-direcionador-estrutura.png)

*Figura — Uma preocupação se torna arquitetura quando exige uma escolha estrutural e uma forma de verificar sua consequência.*

Exemplo: “nenhum dado pessoal cru atravessa a inferência” exige táticas de minimização, mascaramento e autorização por finalidade; essas táticas levam a uma fronteira de dados, uma responsabilidade de seleção de contexto, um fluxo de informação e testes de campos proibidos. A consequência é latência e manutenção adicionais; a decisão só faz sentido porque privacidade é prioritária.

## 3. Realizar RAS com táticas arquiteturais

Uma **tática arquitetural** é uma resposta recorrente que realiza um atributo de qualidade ou atende um RAS. Ela não é o cenário, o stakeholder, o componente ou a ADR. Esses elementos ajudam a descobrir, aplicar ou justificar a tática.

| Intenção | RAS típico | Táticas | Estrutura que pode aplicá-las |
|---|---|---|---|
| Segurança e privacidade | dado sensível não atravessa inferência sem necessidade | minimização, mascaramento, autorização por finalidade, segregação | política de acesso, montador de contexto, adaptador de inferência |
| Fundamentação | afirmação material precisa de suporte | seleção de evidência, vínculo afirmação–fonte, abstenção, vigência | contexto, validação e interface de revisão |
| Confiabilidade | falha não perde trabalho nem confirma efeito | timeout, preservação de estado, idempotência, fallback, degradação, compensação e reconciliação | orquestrador, adaptadores e workflow |
| Modificabilidade | troca de fornecedor não reescreve o fluxo | encapsulamento, contrato estável, adaptador, configuração versionada | interface de capacidade e adaptadores |
| Observabilidade | decisão crítica precisa ser reconstruível | proveniência, correlação, trace, registro de versão, métricas e auditoria | telemetria, log de decisão e repositório de evidência |
| Custo e latência | uso precisa caber no orçamento e no tempo do caso | orçamento, limite de contexto, quota, cache seguro, rate limiting e rota proporcional | gateway, roteador e política de execução |

O Módulo 2 usa essas táticas para comparar direções. Os módulos 3 a 6 aprofundam suas realizações em conhecimento, autonomia, confiança e operação.

Tática, mecanismo, padrão e estilo não são sinônimos. A tática descreve a resposta pretendida; o mecanismo a concretiza neste sistema; um padrão organiza uma composição recorrente de elementos; um estilo restringe a organização geral de componentes e conectores. A ADR registra por que uma dessas combinações foi escolhida.

> **Decisão arquitetural:** selecione táticas a partir dos RAS prioritários, concretize-as em mecanismos identificáveis nas visões e registre em ADR somente as escolhas que alteram estrutura, fronteira, dependência ou responsabilidade.

### Analisar composições, não itens isolados

Uma combinação pode ajudar uma característica e prejudicar outra. Antes de decidir, complete esta leitura:

| Escolha candidata | Resposta desejada | Sensibilidade | Trade-off | Evidência necessária |
|---|---|---|---|---|
| cache de evidências | reduzir latência | validade do conteúdo e chave de autorização | desempenho × atualização e privacidade | teste de expiração, isolamento e revogação |
| fallback de modelo | manter disponibilidade | compatibilidade de contrato e categoria | disponibilidade × qualidade, residência e custo | regressão por categoria e simulação de falha |
| trace de geração | reconstruir falhas | conteúdo e nível de detalhe capturado | auditabilidade × minimização e retenção | inspeção de campos e teste de expurgo |
| revisão obrigatória | conter efeito inadequado | tempo e informação disponíveis ao revisor | segurança × latência e carga humana | estudo de concordância, correção e tempo |

O **ponto de sensibilidade** indica o parâmetro que mais altera a resposta. O **ponto de trade-off** indica uma decisão que afeta características concorrentes. Ambos devem aparecer no risco e na evidência, não apenas na conversa da equipe.

### Priorizar com uma árvore de utilidade reduzida

Para cada um dos três a cinco cenários de qualidade prioritários, registre:

```text
objetivo → característica → cenário → prioridade
        → tática e mecanismo → sensibilidade → trade-off
        → risco ou premissa → experimento
```

Prioridade combina importância para o negócio e dificuldade ou risco arquitetural. A árvore não calcula a decisão; ela impede que uma preferência técnica receba o mesmo peso de uma obrigação ou que dez características sejam declaradas igualmente críticas.

## Critérios de aceitação para comportamento probabilístico

<a id="como-medir-a-aderencia-criterios-probabilisticos-de-aceitacao"></a>

Uma capacidade probabilística precisa de população, amostra, critério, limiar, incerteza, falha intolerável e ação. Exemplo: em 400 contestações estratificadas, ao menos 90% dos resumos atingem cobertura 4/5; nenhum caso crítico expõe outro cliente; abaixo do limite, a categoria fica fora do escopo.

Avaliação automatizada pode ampliar cobertura, mas exige calibração humana, versão e registro de limitações. A evidência não encerra a decisão: ela define se o próximo passo é ampliar, restringir, corrigir ou abandonar.

Continue no [Exemplo arquitetural — Banco Lume](exemplo-arquitetural.md), onde o mesmo raciocínio aparece em modelos, RAS, alternativas e ADRs.

## Do conceito ao requisito

Ao final do desenho conceitual inicial, a equipe deve conseguir declarar: oportunidade, hipótese de valor, critérios de adequação, fora de escopo, stakeholders, cenários, modos, fronteiras e divisão de responsabilidade. A próxima etapa não é escolher um modelo; é transformar esses elementos em objetivos, requisitos significativos e critérios de aceitação que permitam comparar alternativas.
