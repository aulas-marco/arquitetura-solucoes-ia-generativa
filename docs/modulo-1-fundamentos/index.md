# Módulo 1 — Fundamentos de sistemas com IA generativa

> **Pergunta-guia:** O que muda quando parte do sistema produz comportamento probabilístico?

Um modelo generativo acrescenta ao software uma capacidade de interpretação e produção cuja saída não é determinada apenas por regras explícitas. Respostas semelhantes podem variar, fluência pode ocultar erro e uma mudança de modelo, prompt ou contexto pode alterar o comportamento sem modificar o código da aplicação. A arquitetura passa a delimitar, medir e governar um espaço de comportamentos.

Isso não torna toda chamada a modelo uma decisão arquitetural. A escolha se torna **arquiteturalmente significativa** quando altera estruturas fundamentais, características prioritárias, dependências, responsabilidades ou custo de mudança. O sistema — software, modelos, dados, pessoas, políticas, fornecedores e efeitos — continua sendo a unidade principal de julgamento.

Este módulo constrói o vocabulário comum do curso. Primeiro separa modelo, aplicação e sistema sociotécnico. Depois mostra a superfície que determina o comportamento e distingue geração, decisão, autorização e efeito. Por fim, compara formas de compor geração com conhecimento, ferramentas, controles e operação.

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

| Página | Questão central | Resultado esperado |
|---|---|---|
| **1. Abertura** | Qual vocabulário sustenta o curso? | Um mapa das perguntas que serão aprofundadas. |
| **2. [Conceitos](conceitos.md)** | O que determina o comportamento do sistema? | Unidades de análise, superfície comportamental e formas de verificação. |
| **3. [Padrões e decisões](padroes-e-decisoes.md)** | Que composições acrescentam quais responsabilidades? | Panorama, mapa de responsabilidades e ficha de decisão inicial. |
| **4. [Exemplo arquitetural](exemplo-arquitetural.md)** | Como aplicar o mapa a um incremento? | Atendimento Horizonte com escopo, fluxo, falhas e evidências. |
| **5. [Estudo de caso](estudo-de-caso.md)** | Como comparar uma direção sem antecipar a solução? | Recomendação equilibrada entre conhecimento, efeito, confiança e operação. |
| **6. [Oficina de ferramentas](oficina-de-ferramentas.md)** | O que uma execução local permite observar? | Evidência limitada sobre contexto, variabilidade e configuração. |
| **7. [Exercícios](exercicios.md)** | Consigo aplicar o vocabulário a outro sistema? | Evidências nos seis níveis da Taxonomia de Bloom. |
| **8. [Síntese e referências](sintese-e-referencias.md)** | O que deve permanecer para os próximos módulos? | Checklist transversal, autoavaliação e fontes. |

## Como este módulo prepara os demais

| Continuação | Pergunta preparada aqui |
|---|---|
| [Módulo 2 — Desenho conceitual](../modulo-2-desenho-conceitual/index.md) | Que problema, RAS, visões, táticas e evidências justificam uma direção? |
| [Módulo 3 — RAG](../modulo-3-rag/index.md) | Como uma fonte externa se torna evidência atualizada, autorizada e recuperável? |
| [Módulo 4 — Agentes](../modulo-4-agentes/index.md) | Quando o modelo pode escolher passos ou propor ações, e quem governa o efeito? |
| [Módulo 5 — Confiança](../modulo-5-confianca/index.md) | Que riscos, controles e avaliações tornam o uso aceitável para uma finalidade? |
| [Módulo 6 — Operação](../modulo-6-operacao/index.md) | Como preservar propriedades quando modelos, prompts, fontes, ferramentas e políticas mudam? |

## O caso que nos acompanhará

Uma organização quer apoiar atendimento interno. Algumas solicitações pedem reformulação de texto; outras dependem de políticas atualizadas; poucas permitem consultar um sistema corporativo, sem escrita automática. As fontes têm níveis de acesso, versões e responsáveis diferentes.

A primeira intuição é “conectar um modelo”. A leitura arquitetural separa quatro perguntas: que saída pode ser gerada, que evidência precisa sustentá-la, quem decide, e que efeito — se houver — pode ser autorizado. O caso permitirá comparar alternativas sem pressupor RAG ou agente.

## Como estudar

Ao encontrar um componente, pergunte qual responsabilidade ele assume, que falha contém e que nova dependência introduz. Ao encontrar uma medida, pergunte se ela avalia código, comportamento ou propriedade arquitetural. Ao encontrar uma escolha, pergunte que evidência poderia restringi-la ou revertê-la.

O objetivo não é eliminar incerteza. É localizá-la e atribuir a ela uma forma de aprendizagem, contenção ou decisão.

**Próxima página:** [Conceitos fundamentais](conceitos.md).
