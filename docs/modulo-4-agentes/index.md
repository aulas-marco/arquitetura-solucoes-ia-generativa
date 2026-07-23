# Agentes e integração com sistemas corporativos

## Pergunta orientadora

> **Quando permitir que o modelo escolha e execute ações?**

Responder bem não autoriza agir. Um modelo pode redigir uma mensagem convincente e, ainda assim, escolher a ferramenta errada, repetir um pedido, usar parâmetros fora da política ou prosseguir quando deveria interromper. Ao conectar geração a CRM, estoque, pagamentos ou pedidos, a arquitetura passa a governar efeitos sobre pessoas e sistemas. A questão deixa de ser apenas “a resposta parece correta?” e passa a incluir “quem autorizou a ação, com qual identidade, dentro de quais limites e como recuperamos uma falha?”.

Este módulo estuda essa passagem sem tratar “agente” como sinônimo de chatbot sofisticado. Um **chatbot** sustenta uma conversa; um **copiloto** ajuda uma pessoa a decidir ou produzir; um **workflow determinístico** tem sequência e transições definidas pela aplicação; um **agente** delega ao modelo a escolha de próximos passos ou ferramentas dentro de fronteiras explícitas. Uma solução pode combinar os quatro, e o rótulo da interface não determina onde está o controle.

**Tempo estimado de leitura:** 60–90 minutos, sem contar o estudo de caso e os exercícios de projeto.

## O que você aprenderá

Ao final, você deverá conseguir:

1. distinguir geração, decisão e ação em uma trajetória;
2. justificar quando a variabilidade do plano cria valor suficiente para aceitar autonomia;
3. especificar ferramentas por contratos validáveis, não por descrições vagas;
4. separar contexto, estado de execução, memória de trabalho e memória persistente;
5. escolher APIs, mensagens, eventos e adaptadores conforme consistência e acoplamento;
6. preservar identidade, autorização delegada, idempotência e auditoria em cada ação;
7. aplicar timeout, retry, circuit breaker e compensação sem duplicar efeitos;
8. classificar autonomia por ação e risco, com aprovação humana e fallback;
9. comparar agente único e múltiplos agentes por evidência operacional.

## Fio aplicado: desenvolvimento guiado por especificação

O caso mais concreto de autonomia com ferramentas é o agente que constrói software. Ele lê o repositório, propõe um plano, altera arquivos, executa testes e interpreta resultados. Portanto, concentra em pequena escala quase todos os problemas deste módulo: delegação, contratos, estado, memória, efeitos colaterais, observabilidade, revisão humana e recuperação de falhas. **Specification-Driven Development (SDD)** não entra como tópico lateral. Ele funciona como a espinha dorsal aplicada para estudar como uma intenção humana atravessa um sistema de agentes até se tornar software verificável.

O **Spec Kit** conduz o percurso comum: `constitution → specify → clarify → plan → tasks → analyze → implement → verify`. A sequência não transforma comandos em método infalível. Ela torna explícitas perguntas que o “prompt e torça” costuma esconder: quais princípios são inegociáveis? O que deve acontecer para o usuário? Quais ambiguidades permanecem? Que arquitetura suporta os atributos de qualidade? Como fatiar trabalho que possa ser integrado e validado? Que evidência demonstra aderência à intenção e aos padrões do repositório?

A especificação será tratada como artefato vivo e versionado. Ela descreve comportamento observável, critérios de aceite, limites, riscos e questões em aberto. O plano técnico traduz essa intenção para componentes, contratos e decisões. As tarefas formam fatias verticais pequenas, e não uma lista de camadas desconectadas. A implementação começa por testes nas interfaces públicas. A revisão ocorre em dois eixos: **aderência à spec** e **qualidade segundo os padrões de engenharia**. Três gates humanos preservam responsabilidade antes do plano, antes da execução e antes da integração.

Essa escolha dá unidade ao módulo sem reduzir SDD ao Spec Kit. O fluxo de Matt Pocock — `grill-with-docs → to-spec → to-tickets → implement → code-review` — ajuda a aprofundar clarificação, fatiamento vertical, módulos profundos e revisão em duas passagens. Kiro, BMAD, Tessl e outros materiais aparecem no apêndice como variações comparáveis. A turma pratica um fio condutor comum e, ao mesmo tempo, aprende a separar os princípios duráveis da sintaxe de uma ferramenta.

O percurso produz evidências concretas:

| Parte do módulo | Pergunta de SDD | Evidência produzida |
|---|---|---|
| [Conceitos](conceitos.md#do-agente-que-age-ao-agente-que-constroi-software) | por que a spec precisa governar agentes de codificação? | vocabulário, fluxo completo e ledger epistemológico |
| [Padrões e decisões](padroes-e-decisoes.md#padrao-desenvolvimento-guiado-por-especificacao) | como preservar intenção e qualidade durante a transformação? | critérios, fatias verticais, seams, gates e ADRs |
| [Exemplo arquitetural](exemplo-arquitetural.md#pipeline-sdd-com-gates-humanos) | como os artefatos se conectam numa mudança real? | constitution, spec, plano, contratos, tarefas, testes e revisão |
| [Oficina](oficina-de-ferramentas.md#extensao-mini-fluxo-spec-kit) | como operar o ciclo com segurança? | mini-iniciativa executada com Spec Kit |
| [Exercícios](exercicios.md) | como criticar e adaptar o método? | análise de consistência e proposta completa |
| [Síntese](sintese-e-referencias.md#sintese-do-fio-sdd) | o que permanece quando a ferramenta muda? | checklists, limites e apêndice comparativo |

Ao terminar, você não deverá apenas repetir etapas. Deverá saber calibrar profundidade ao risco, interromper o agente quando a evidência é insuficiente, reconhecer uma spec ornamental e explicar por que aprovação humana não compensa critérios vagos. A pessoa arquiteta preserva a responsabilidade pela intenção, pelos atributos de qualidade e pelos gates; o agente amplia capacidade de exploração e execução dentro desses limites.

## Pré-requisitos e princípio de continuidade

Retomaremos a [sequência de decisão](../modulo-2-desenho-conceitual/padroes-e-decisoes.md#uma-sequencia-de-decisao): gerar, acessar conhecimento, agir e só então conceder autonomia. Também reutilizaremos autorização, proveniência e suficiência do [Módulo 3](../modulo-3-rag/index.md). Uma evidência recuperada não concede permissão de escrita; uma ferramenta disponível não precisa ser oferecida ao modelo; uma saída estruturada válida não prova que a ação é apropriada.

Os atributos de [Autonomia](../referencia/atributos-de-qualidade.md#autonomia), [Confiabilidade](../referencia/atributos-de-qualidade.md#confiabilidade), [Segurança](../referencia/atributos-de-qualidade.md#seguranca) e [Observabilidade](../referencia/atributos-de-qualidade.md#observabilidade) serão tratados como cenários mensuráveis. A tese do módulo é simples: **autonomia deve ser orçada e observável**. “Orçada” significa limitada por escopo, ações, etapas, tempo, custo e risco. “Observável” significa reconstruir propostas, decisões de política, aprovações, chamadas, resultados e compensações sem registrar segredos desnecessários.

## Mapa do módulo

| Etapa | Página | Foco |
|---|---|---|
| 1 | [Abertura](index.md) | contrato de aprendizagem e limites de autonomia |
| 2 | [Conceitos](conceitos.md) | agente, planejamento, estado, memória, topologias e SDD |
| 3 | [Padrões e decisões](padroes-e-decisoes.md) | ferramentas, SDD, identidade, resiliência e intervenção humana |
| 4 | [Exemplo arquitetural](exemplo-arquitetural.md) | sucesso, repetição, compensação, pipeline SDD e squad híbrida |
| 5 | [Estudo de caso](estudo-de-caso.md) | solicitações com CRM, estoque, pedidos e política |
| 6 | [Oficina de ferramentas](oficina-de-ferramentas.md) | uma evidência breve, comparável e segura |
| 7 | [Exercícios](exercicios.md) | autonomia, trace, crítica e projeto |
| 8 | [Síntese e referências](sintese-e-referencias.md) | checklist, autoavaliação e fontes |

## Um teste inicial

Considere: “se o cliente pedir troca, consulte pedido e estoque; reserve o item; solicite confirmação; cancele a reserva anterior; atualize o CRM”. A sequência parece conhecida, mas exceções variam: item substituto, política por canal, estoque concorrente e aprovação para diferença de valor. Isso não prova que um agente seja necessário. Primeiro enumere decisões, efeitos e falhas. Depois compare um workflow com ramificações a um agente limitado. A escolha depende do valor da adaptação e da capacidade de controlar trajetórias, não da novidade da tecnologia.

Comece pela linguagem precisa em [Conceitos](conceitos.md).
