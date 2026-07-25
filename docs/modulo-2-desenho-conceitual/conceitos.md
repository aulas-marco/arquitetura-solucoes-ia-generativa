# O que é o desenho conceitual?

O desenho conceitual é o momento em que a arquitetura de software e a IA generativa se fundem para transformar uma ideia em um **sistema governado e operável**. Nesta etapa, o arquiteto não busca apenas "fazer a IA funcionar", mas sim garantir que o modelo seja um **componente integrado** que respeite os fundamentos de APIs, dados e sistemas distribuídos.

## O racional da conversão: oportunidade versus requisito

O cerne deste módulo é a capacidade de **converter oportunidades em requisitos e escolhas justificadas**. Sob a lente do arquiteto, uma oportunidade de negócio (ex: "automatizar o suporte") só se torna um desenho conceitual quando o **racional arquitetural** define como o comportamento probabilístico da IA será controlado.

- **Decisões explícitas:** cada escolha no desenho conceitual deve ser **explícita e verificável**, evitando que a solução seja uma "caixa preta".
- **Análise de trade-offs:** o arquiteto compara consequências sobre as características priorizadas; monólito modular e serviços distribuídos são estilos possíveis, enquanto gateway e chassi são capacidades compartilhadas que podem ou não ser necessárias.

## A IA como componente de um sistema maior

Um arquiteto de soluções entende que o modelo de linguagem não é a solução completa, mas um **componente dentro de uma arquitetura de backend**. O desenho conceitual deve prever como esse componente se conecta a:

- **Conhecimento:** como os dados corporativos serão acessados de forma segura.
- **Integrações:** como as APIs existentes servirão de contexto ou ferramentas para a IA.
- **Controles:** quais são os limites de autonomia e segurança impostos ao sistema.

## Atributos de qualidade no contexto generativo

Diferente de sistemas determinísticos, o desenho conceitual para IA exige que o arquiteto defina **critérios de aceitação para comportamentos probabilísticos**. Isso significa que os atributos de qualidade clássicos (performance, segurança, escalabilidade) devem ser estendidos para incluir a **confiabilidade e a observabilidade das respostas**.

- O arquiteto utiliza o **vocabulário e padrões** da disciplina para tomar decisões que possam ser defendidas perante stakeholders técnicos e de negócio.

Características arquiteturais não são uma lista de desejos. Segurança, privacidade, proveniência, latência, custo, confiabilidade, observabilidade e modificabilidade competem entre si. A equipe precisa limitar as prioritárias, declarar a tensão aceita e definir medida, responsável e momento de revisão; a arquitetura adequada é a menos ruim para esse contexto, não a que maximiza uma característica isolada.

## O processo de decisão e o uso de ADRs

Seguindo o princípio de um **processo mínimo de arquitetura**, o desenho conceitual deve ser documentado através de **ADRs (Architecture Decision Records)**. No contexto do Módulo 2, isso garante que:

- O contexto da decisão (a oportunidade original) esteja claro.
- As alternativas técnicas consideradas (diferentes modelos ou abordagens de integração) sejam registradas.
- As **consequências e evidências sintéticas** de que a decisão foi a correta estejam acessíveis para revisão futura.

## Preparação para a progressão de decisões

Este módulo estabelece a fundação para as etapas subsequentes da solução: **RAG, Agentes e Confiança**. Sem um desenho conceitual sólido, focado em requisitos técnicos e não apenas em "promessas", a solução corre o risco de falhar em produção por falta de **sustentabilidade e escala**.

## Critérios de adequação da IA generativa

IA generativa tende a ser candidata quando a tarefa exige interpretar linguagem ou conteúdo não estruturado, sintetizar múltiplas evidências, produzir uma representação adaptada a um contexto ou lidar com variedade que tornaria regras explícitas frágeis. A candidatura fica mais forte quando uma saída aproximada pode ser avaliada, corrigida ou contida antes de produzir dano.

Use cinco perguntas:

1. **Variabilidade útil:** há muitas formas aceitáveis de saída, ou existe uma única resposta calculável?
2. **Dados e contexto:** existem exemplos, evidências e permissões suficientes para orientar e avaliar o comportamento?
3. **Tolerância ao erro:** uma saída imperfeita pode ser detectada e revisada antes do efeito?
4. **Critério de qualidade:** especialistas conseguem julgar casos representativos com concordância aceitável?
5. **Vantagem comparativa:** a capacidade generativa supera uma alternativa convencional em valor total, não só em demonstração?

A resposta “sim” não autoriza automação. Ela apenas justifica um experimento controlado. Modelos fundacionais apresentam capacidades amplas, mas também riscos dependentes de composição e contexto, como discute o relatório primário [On the Opportunities and Risks of Foundation Models](https://arxiv.org/abs/2108.07258). A unidade de decisão permanece o sistema, não o modelo isolado.

## Quando rejeitar IA generativa

Rejeite GenAI quando:

- a saída correta deriva de regra estável, cálculo ou consulta estruturada;
- qualquer variação é defeito e não existe contenção antes do efeito;
- não há dados legalmente utilizáveis ou exemplos representativos para avaliação;
- o requisito exige explicação causal ou garantia formal que a geração não fornece;
- latência, custo, residência, retenção ou conectividade tornam a solução inviável;
- a tarefa automatizada remove uma responsabilidade humana irrenunciável;
- uma busca, formulário, regra ou melhoria de processo produz valor equivalente com menos risco.

Se política, valor, prazo e categoria determinam exatamente um reembolso, regras devem decidir. Um modelo pode explicar ou extrair campos, mantendo decisão e efeito determinísticos.

## CONOPS: o sistema em operação

O **Concept of Operations (CONOPS)** descreve como o sistema será usado sob condições normais e excepcionais. É mais amplo que uma jornada e menos detalhado que uma arquitetura de componentes. Responde:

- quem inicia, supervisiona, recebe e contesta resultados;
- que informação entra, de onde vem e sob qual autoridade;
- quais atividades continuam humanas;
- quais modos de operação existem;
- quais efeitos são permitidos e proibidos;
- como o sistema degrada, interrompe e recupera;
- que evidências ficam disponíveis para usuário, operação e auditoria.

### Cenário operacional essencial

Um cenário não é apenas “usuário faz pergunta”. Escreva ator, objetivo, precondições, estímulo, colaboração, resultado, exceções e evidência. Exemplo:

> Um analista autenticado abre uma contestação já classificada. O sistema reúne apenas dados autorizados do caso e políticas vigentes, propõe um resumo com referências e destaca lacunas. O analista confere evidências, corrige a proposta e registra recomendação. Um supervisor aprova ou devolve. Se uma fonte essencial estiver indisponível ou o suporte for insuficiente, o sistema não recomenda; preserva o trabalho e orienta a consulta manual.

Essa narrativa revela necessidades que “chat com LLM” oculta: identidade, autorização por dado, vigência, proveniência, estado de trabalho, revisão, segregação de função e degradação segura.

## Fronteiras e fora de escopo

Fronteira define responsabilidade, não apenas rede. Marque:

- **fronteira organizacional:** quem é responsável por processo, dado, modelo e operação;
- **fronteira de confiança:** onde conteúdo, identidade ou instrução muda de nível de confiança;
- **fronteira de dados:** onde informação é coletada, derivada, persistida, registrada ou enviada;
- **fronteira de decisão:** onde uma recomendação passa a produzir consequência;
- **fronteira de fornecedor:** onde políticas de retenção, treinamento, localização e suporte deixam de ser controladas diretamente.

O fora de escopo evita expectativas perigosas. No Banco Lume: não aprovar, alterar cadastro, enviar comunicações, aprender com correções individuais ou tratar categorias não avaliadas. Cada exclusão precisa aparecer em interface, autorização e testes.

### Proveniência

**Proveniência** é a cadeia verificável que permite explicar uma evidência: **de onde veio**, **sob qual autoridade foi acessada**, **qual versão e vigência possuía**, **quais transformações ou seleções sofreu** e **onde foi usada na resposta ou decisão**. Não é apenas uma URL ou citação. Em um sistema generativo, ela liga fonte, identidade, finalidade, transformação, trecho recuperado, versão de política, modelo e saída. Essa cadeia permite contestar uma recomendação, revogar uma fonte e investigar uma resposta sem conservar conteúdo além do necessário.

Um **adaptador** separa contrato e fornecedor: **OpenAI SDK** e **LiteLLM** consomem modelos; **Docker Model Runner** apoia execução local. Nenhum define finalidade, dado ou autorização.

## Stakeholders e preocupações

“Usuário” é uma categoria insuficiente. Analista, cliente afetado, supervisor, dono da política, encarregado de dados, Segurança, Operações, auditoria, fornecedor e equipe de manutenção enxergam riscos diferentes. Uma matriz de preocupações torna tensões visíveis:

| Stakeholder             | Resultado desejado                   | Preocupação arquitetural                        |
| ----------------------- | ------------------------------------ | ----------------------------------------------- |
| Analista                | preparar caso com menos busca manual | utilidade, latência, fontes compreensíveis      |
| Supervisor              | revisar decisões consistentes        | destaque de incerteza, histórico e comparação   |
| Cliente                 | tratamento justo e tempestivo        | contestabilidade, privacidade, ausência de dano |
| Dono da política        | aplicar versão vigente               | atualização, semântica e resolução de conflitos |
| Segurança e Privacidade | limitar exposição e abuso            | minimização, autorização, retenção e auditoria  |
| Operações               | manter serviço recuperável           | dependências, fallback, observabilidade e custo |
| Auditoria               | reconstruir decisão                  | identidade, versões, evidências e ações humanas |

Treinamento, processo, papéis e contestação também respondem a preocupações do sistema sociotécnico.

## Modularidade e fronteiras de componente

Componentes devem ter responsabilidade coesa e dependências deliberadas. O **orquestrador** coordena o caso, mas não deve conhecer peculiaridades de cada legado; **adaptadores** isolam contratos, versões e falhas de fornecedor; o **montador de contexto** seleciona evidências; o **gateway** aplica controles transversais; a **validação** verifica saída e suporte. Essa separação reduz acoplamento: trocar um fornecedor ou uma fonte deve afetar seu adaptador, não reescrever a política de autorização nem o workflow humano. Separar sem motivo também cria chamadas, latência e operação adicionais; a fronteira só se justifica por mudança independente, risco ou atributo de qualidade.

## Modos operacionais

Defina modos e transições além do caminho feliz:

1. **normal:** dependências saudáveis, escopo válido e evidência suficiente;
2. **baixa confiança:** proposta parcial, lacunas e revisão reforçada;
3. **degradado:** dependência indisponível e trabalho manual acessível;
4. **bloqueado:** dado, finalidade ou ação não autorizada;
5. **manutenção ou incidente:** mudança controlada, contenção e recuperação.

Para cada transição, especifique gatilho, estado preservado, pessoa informada e critério de retorno. Retry indiscriminado não é estratégia de recuperação: pode elevar custo, amplificar carga e repetir efeitos.

## Responsabilidade humano–IA

“Human in the loop” não explica quem decide. Separe responsabilidades por verbo:

- o sistema **localiza**, **extrai**, **resume**, **sinaliza** e **propõe**;
- o analista **verifica**, **complementa**, **justifica** e **recomenda**;
- o supervisor **aprova**, **devolve** ou **escala**;
- o dono da política **define** interpretação oficial;
- Operações **monitora**, **contém** e **restaura**.

Revisão só controla quando há competência, tempo, autoridade, evidências e interface para discordar. Um clique após recomendação sem fontes é ritual. Registre correções sem tratá-las automaticamente como rótulos e permita recusa.

## Do conceito ao requisito

Ao final do desenho conceitual inicial, a equipe deve conseguir declarar: oportunidade, hipótese de valor, critérios de adequação, fora de escopo, stakeholders, cenários, modos, fronteiras e divisão de responsabilidade. A próxima etapa não é escolher um modelo; é transformar esses elementos em objetivos, requisitos significativos e critérios de aceitação que permitam comparar alternativas.

## Ferramentas no mercado

São exemplos; consulte o [Guia de ferramentas](../referencia/guia-de-ferramentas.md).

| Ferramenta          | Quando ajuda             | Pré-requisito                               | Limite arquitetural                      |
| ------------------- | ------------------------ | ------------------------------------------- | ---------------------------------------- |
| OpenAI SDK          | Adaptar contrato de API. | Credencial real ou fixture.                 | Não define política.                     |
| LiteLLM             | Normalizar endpoints.    | Modelos, credenciais e falhas configurados. | Não elimina diferenças entre provedores. |
| Docker Model Runner | Prototipar modelo local. | Docker, modelo e recursos.                  | Não substitui critérios ou operação.     |

**Próxima página:** [Requisitos e padrões de decisão](padroes-e-decisoes.md).
