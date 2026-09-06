# Módulo 1 — Fundamentos de sistemas com IA generativa

> **Pergunta-guia:** O que muda quando parte do sistema produz comportamento probabilístico?

Um modelo generativo acrescenta ao software uma capacidade de interpretação e produção cuja saída não é determinada apenas por regras explícitas. Respostas semelhantes podem variar, fluência pode ocultar erro e uma mudança de modelo, prompt ou contexto pode alterar o comportamento sem modificar o código da aplicação. A arquitetura passa a delimitar, medir e governar um espaço de comportamentos.

Isso não torna toda chamada a modelo uma decisão arquitetural. A escolha se torna **arquiteturalmente significativa** quando altera estruturas fundamentais, características prioritárias, dependências, responsabilidades ou custo de mudança. O sistema — software, modelos, dados, pessoas, políticas, fornecedores e efeitos — continua sendo a unidade principal de julgamento.

Este módulo constrói o vocabulário comum do curso. Primeiro separa modelo, aplicação e sistema sociotécnico. Depois mostra a superfície que determina o comportamento e distingue geração, decisão, autorização e efeito. Por fim, compara formas de compor geração com conhecimento, ferramentas, controles e operação.

Arquitetar uma solução com IA generativa não começa pela escolha do modelo. Começa pela definição do resultado que o sistema deve produzir, das condições em que esse resultado é aceitável e das responsabilidades que não podem ser delegadas à geração probabilística.

O trabalho do arquiteto é transformar uma capacidade ampla — interpretar, resumir, redigir, classificar ou propor passos — em comportamento útil dentro de limites conhecidos. Para isso, ele precisa:

- delimitar onde a geração participa e onde permanecem regras, decisões humanas e operações determinísticas;
- identificar os elementos que alteram o comportamento, mesmo quando o código da aplicação não muda;
- relacionar riscos e atributos de qualidade a mecanismos de contenção, medição e recuperação;
- distribuir responsabilidades entre software, modelos, dados, pessoas, políticas e fornecedores;
- definir que evidências permitem adotar, promover, restringir ou abandonar uma composição.

Essas tarefas mudam a pergunta inicial. Em vez de “qual modelo usar?”, a análise procura saber **que comportamento o sistema deve sustentar, quem responde por cada parte e como verificar se os limites continuam válidos**.

## Um mapa para orientar a leitura

A figura a seguir apresenta os elementos que participam do comportamento generativo. Ela não representa uma arquitetura pronta nem uma sequência obrigatória. Serve para localizar três questões que atravessam esta página:

1. o que pertence ao modelo e o que pertence ao sistema;
2. quais elementos tornam a saída variável;
3. quais controles e evidências precisam acompanhar essa variabilidade.

![Mapa do comportamento generativo: entrada e contexto atravessam prompt, tokens e parâmetros até um modelo fundacional e uma saída variável; conhecimento paramétrico, avaliação, segurança e observabilidade circundam esse comportamento probabilístico](../assets/images/m01-mapa-comportamento-generativo.png "Mapa do comportamento generativo")
*Figura — A saída do modelo é apenas uma parte do comportamento do sistema; avaliação, segurança e observabilidade pertencem à composição desde o início.*

## Antes de começar

Você deve reconhecer componente, interface, dependência, fluxo de dados, requisito funcional, atributo de qualidade e trade-off. Não é necessário conhecer aprendizado de máquina, estatística ou a matemática dos transformadores. Consulte o [Glossário](../referencia/glossario.md) e o [Catálogo de atributos de qualidade](../referencia/atributos-de-qualidade.md) quando precisar de uma definição controlada ou de um cenário mensurável.

**Tempo estimado de leitura:** 60–90 minutos, sem contar a oficina e os exercícios.

## Objetivos de aprendizagem

Ao concluir o módulo, você deverá ser capaz de:

1. **Compreender** por que modelo, aplicação e sistema sociotécnico são unidades de análise diferentes.
2. **Compreender** as fronteiras entre componentes determinísticos e probabilísticos.
3. **Aplicar** tokens, contexto, prompts, embeddings, inferência e multimodalidade à leitura de uma solução.
4. **Analisar** a superfície comportamental formada por modelo, parâmetros, prompt, contexto, fontes, ferramentas, políticas, estado, memória e implantação.
5. **Analisar** a separação entre geração, decisão, autorização e efeito.
6. **Avaliar** geração direta, contexto fornecido, RAG, ferramentas, workflows, agentes e fine-tuning pelas responsabilidades que acrescentam.
7. **Distinguir** teste de software, avaliação comportamental e verificação arquitetural.

## Roteiro do módulo

| Etapa | Página | Foco |
|---|---|---|
| 1 | [Abertura](index.md) | contrato de aprendizagem do módulo |
| 2 | [Determinístico e probabilístico](mudanca-probabilistica.md) | determinístico e probabilístico; modelo, aplicação e sistema sociotécnico |
| 3 | [Superfície comportamental](superficie-comportamental.md) | superfície de comportamento: tokens, janela, prompt, parâmetros e alucinação |
| 4 | [Artefatos e embeddings](artefatos-do-sistema.md) | conhecimento, contexto, estado, memória, evidência e trace |
| 5 | [Geração, decisão e efeito](responsabilidade-e-efeito.md) | geração, decisão, autorização e efeito; mapa de responsabilidades |
| 6 | [Padrões de solução](escolha-da-abordagem.md) | sete abordagens, quatro decisões ortogonais e a ficha inicial |
| 7 | [Verificação e governança](verificacao-e-governanca.md) | três tipos de verificação e o contrato arquitetural que passa a valer |
| 8 | [Exemplo arquitetural](exemplo-arquitetural.md) | — |
| 9 | [Estudo de caso](estudo-de-caso.md) | — |
| 10 | [Oficina de ferramentas](oficina-de-ferramentas.md) | — |
| 11 | [Exercícios](exercicios.md) | — |
| 12 | [Síntese e referências](sintese-e-referencias.md) | — |

## Como este módulo prepara os demais

| Continuação | Pergunta preparada aqui |
|---|---|
| [Módulo 2 — Desenho conceitual](../modulo-2-desenho-conceitual/index.md) | Que problema, RAS, visões, táticas e evidências justificam uma direção? |
| [Módulo 3 — RAG](../modulo-3-rag/index.md) | Como uma fonte externa se torna evidência atualizada, autorizada e recuperável? |
| [Módulo 4 — Agentes](../modulo-4-agentes/index.md) | Quando o modelo pode escolher passos ou propor ações, e quem governa o efeito? |
| [Módulo 5 — SDD](../modulo-5-sdd/index.md) | Como uma intenção humana atravessa um sistema de agentes até virar software verificável? |
| [Módulo 6 — Confiança](../modulo-6-confianca/index.md) | Que riscos, controles e avaliações tornam o uso aceitável para uma finalidade? |
| [Módulo 7 — Operação](../modulo-7-operacao/index.md) | Como preservar propriedades quando modelos, prompts, fontes, ferramentas e políticas mudam? |

## O caso que nos acompanhará

Uma organização quer apoiar atendimento interno. Algumas solicitações pedem reformulação de texto; outras dependem de políticas atualizadas; poucas permitem consultar um sistema corporativo, sem escrita automática. As fontes têm níveis de acesso, versões e responsáveis diferentes.

A primeira intuição é “conectar um modelo”. A leitura arquitetural separa quatro perguntas: que saída pode ser gerada, que evidência precisa sustentá-la, quem decide, e que efeito — se houver — pode ser autorizado. O caso permitirá comparar alternativas sem pressupor RAG ou agente.

## Como estudar

Ao encontrar um componente, pergunte qual responsabilidade ele assume, que falha contém e que nova dependência introduz. Ao encontrar uma medida, pergunte se ela avalia código, comportamento ou propriedade arquitetural. Ao encontrar uma escolha, pergunte que evidência poderia restringi-la ou revertê-la.

O objetivo não é eliminar incerteza. É localizá-la e atribuir a ela uma forma de aprendizagem, contenção ou decisão.

**Próxima página:** [Determinístico e probabilístico](mudanca-probabilistica.md).
