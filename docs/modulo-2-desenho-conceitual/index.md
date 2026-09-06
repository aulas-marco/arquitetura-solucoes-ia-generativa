# Módulo 2 — Do problema ao Documento de Arquitetura de Software

> **Pergunta-guia:** Como evitar construir a solução de IA certa para o problema errado?

Uma equipe pode selecionar um modelo competente, implementar controles rigorosos e ainda fracassar: basta otimizar uma capacidade que não resolve a necessidade real, automatizar uma decisão que deveria continuar humana ou introduzir IA generativa onde regras convencionais seriam mais previsíveis. Antes de componentes e produtos, a arquitetura precisa estabelecer propósito, fronteiras, responsabilidades e evidências de sucesso.

Este módulo transforma uma oportunidade ambígua em um **Documento de Arquitetura de Software**, nome adotado pelo curso para o conjunto curto de entradas, visões, análises, decisões e evidências que permite iniciar — ou recusar — uma solução. O percurso é sempre o mesmo: oportunidade, hipótese de valor, atividades humanas, CONOPS, fronteiras, requisitos significativos, visões, táticas, alternativas, experimento e ADR. Só depois compararemos soluções; prompt, RAG, fine-tuning, workflows e agentes são respostas possíveis, não o ponto de partida.

Desenho conceitual é a etapa que define **o que vale a pena resolver, sob quais limites e com que evidência** antes de escolher modelos, padrões ou fornecedores. Seu resultado não é um diagrama de tecnologia. É uma descrição arquitetural suficiente para comparar direções e tornar decisões revisáveis.

## Antes de começar

Você deve dominar o vocabulário do [Módulo 1 — Fundamentos](../modulo-1-fundamentos/index.md): modelo, aplicação de IA, sistema sociotécnico, componentes determinísticos e probabilísticos, contexto, RAG, ferramentas, workflows, agentes, avaliação e trade-offs. Também retomaremos o [Catálogo de atributos de qualidade](../referencia/atributos-de-qualidade.md) e o [Template de ADR](../referencia/template-adr.md).

Não é necessário conhecer um provedor, modelo ou framework específico. As decisões deste módulo são deliberadamente independentes de fornecedor e devem continuar úteis quando produtos, preços e capacidades mudarem.

**Tempo estimado de leitura:** 60–90 minutos, sem contar o estudo de caso e os exercícios de projeto.

## Objetivos de aprendizagem

Ao concluir o módulo, você deverá ser capaz de:

1. **Compreender** uma oportunidade como hipótese de valor e expressá-la por meio de stakeholders, fronteiras, cenários e modos operacionais.
2. **Aplicar** critérios de adequação e rejeição para decidir se IA generativa participa da solução e qual responsabilidade permanece humana.
3. **Analisar** objetivos e requisitos para identificar RAS, cenários de qualidade, táticas, sensibilidades, trade-offs e riscos.
4. **Avaliar** alternativas por capacidade adicionada, responsabilidade criada, visões afetadas, evidência mínima e condição de rejeição.
5. **Criar** um Documento de Arquitetura de Software rastreável, com visões de contexto, responsabilidades, interação, informação e implantação, regras de correspondência, ADRs e proveniência.

## Roteiro do módulo

| Etapa | Página | Foco |
|---|---|---|
| 1 | [Abertura](index.md) | contrato de aprendizagem do módulo |
| 2 | [Descrever o sistema antes da solução](descricao-arquitetural.md) | documento de arquitetura, cinco visões mínimas e correspondências |
| 3 | [Oportunidade e adequação](adequacao-da-ia.md) | critérios de adequação e os casos em que a resposta é recusar |
| 4 | [CONOPS, fronteiras e stakeholders](conops-e-fronteiras.md) | CONOPS, fora de escopo, stakeholders, modos operacionais e papel humano |
| 5 | [Requisitos significativos e táticas](requisitos-e-taticas.md) | do atributo ao RAS, táticas e critério de aceitação probabilístico |
| 6 | [Comparar alternativas e registrar a decisão](alternativas-e-registro.md) | menor capacidade suficiente, ADR e verificação de correspondência |
| 7 | [Exemplo arquitetural](exemplo-arquitetural.md) | — |
| 8 | [Exercícios](exercicios.md) | — |
| 9 | [Oficina de ferramentas](oficina-de-ferramentas.md) | — |
| 10 | [Estudo de caso](estudo-de-caso.md) | — |
| 11 | [Síntese e referências](sintese-e-referencias.md) | — |

## Caso condutor: Banco Lume

O Banco Lume pretende apoiar analistas que tratam contestações de transações. Hoje eles consultam políticas, dados cadastrais e histórico em sistemas legados, registram uma recomendação e encaminham o caso a um supervisor. A direção pede “um agente que resolva tudo”; Risco exige revisão humana antes de qualquer decisão; Privacidade restringe o trânsito de dados pessoais; Operações informa que parte dos sistemas fica indisponível durante janelas de manutenção.

O objetivo não será confirmar a preferência inicial. Investigaremos se a melhor composição é automação convencional, copiloto com contexto fornecido, RAG ou agente com ferramentas — e se alguma capacidade generativa deve ser rejeitada. A Cooperativa Aurora, mais adiante, será o **caso de transferência**: aplica o mesmo método em outro domínio sem copiar a solução do Banco Lume.

## Um princípio de trabalho

Leia cada seta nos dois sentidos: **objetivo → cenário → requisito significativo → alternativa → evidência**; depois pergunte qual necessidade justifica cada componente, permissão e dependência. Para toda evidência, registre origem, autoridade, versão, transformação e uso. Sem resposta, há lacuna de rastreabilidade ou proveniência.

O [NIST AI RMF Generative AI Profile](https://doi.org/10.6028/NIST.AI.600-1) reforça que riscos e impactos devem ser compreendidos no contexto de uso, e não inferidos apenas das capacidades gerais de um modelo. Esse princípio orientará o módulo: arquitetura é uma disciplina de escolha contextual, não um catálogo de caixas.

**Próxima página:** [Descrever o sistema antes da solução](descricao-arquitetural.md).
