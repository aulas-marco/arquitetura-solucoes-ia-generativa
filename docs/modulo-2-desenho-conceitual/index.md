# Módulo 2 — Desenho conceitual e decisões arquiteturais

> **Pergunta-guia:** Como evitar construir a solução de IA certa para o problema errado?

Uma equipe pode selecionar um modelo competente, implementar controles rigorosos e ainda fracassar: basta otimizar uma capacidade que não resolve a necessidade real, automatizar uma decisão que deveria continuar humana ou introduzir IA generativa onde regras convencionais seriam mais previsíveis. Antes de componentes e produtos, a arquitetura precisa estabelecer propósito, fronteiras, responsabilidades e evidências de sucesso.

Este módulo transforma uma oportunidade ambígua em desenho defensável. Partiremos da hipótese de valor e do CONOPS, identificaremos stakeholders e cenários, separaremos objetivos e criaremos critérios probabilísticos. Só depois compararemos soluções: **prompt, RAG, fine-tuning, workflows e agentes são respostas possíveis; não definem o problema**.

## Antes de começar

Você deve dominar o vocabulário do [Módulo 1 — Fundamentos](../modulo-1-fundamentos/index.md): modelo, aplicação de IA, sistema sociotécnico, componentes determinísticos e probabilísticos, contexto, RAG, ferramentas, workflows, agentes, avaliação e trade-offs. Também retomaremos o [Catálogo de atributos de qualidade](../referencia/atributos-de-qualidade.md) e o [Template de ADR](../referencia/template-adr.md).

Não é necessário conhecer um provedor, modelo ou framework específico. As decisões deste módulo são deliberadamente independentes de fornecedor e devem continuar úteis quando produtos, preços e capacidades mudarem.

**Tempo estimado de leitura:** 75–105 minutos, sem contar o estudo de caso e os exercícios de projeto.

## Objetivos de aprendizagem

Ao concluir o módulo, você deverá ser capaz de:

1. **Compreender** uma oportunidade como hipótese de valor e expressá-la por meio de stakeholders, fronteiras, cenários e modos operacionais.
2. **Aplicar** critérios de adequação e rejeição para decidir se IA generativa participa da solução e qual responsabilidade permanece humana.
3. **Analisar** objetivos e requisitos para identificar requisitos arquiteturalmente significativos, restrições e critérios probabilísticos de aceitação.
4. **Avaliar** alternativas como prompt, RAG, fine-tuning, workflow, agente, modelo único ou múltiplos modelos, hospedagem gerenciada ou autogerida e construir, comprar ou compor.
5. **Criar** um desenho conceitual rastreável, com vistas, cenários de falha, ADRs, evidências e gatilhos de revisão.

## Roteiro do módulo

| Página | Questão central | Resultado esperado |
|---|---|---|
| **1. Abertura** | Qual é o contrato de aprendizagem? | Uma sequência que parte do problema, não da tecnologia. |
| **2. [Conceitos](conceitos.md)** | Que problema, valor e sistema estamos definindo? | Oportunidade, CONOPS, limites, stakeholders, modos e responsabilidade humana. |
| **3. [Padrões e decisões](padroes-e-decisoes.md)** | Como requisitos orientam alternativas? | Requisitos significativos, critérios de aceitação e paisagem de decisões. |
| **4. [Exemplo arquitetural](exemplo-arquitetural.md)** | Como a rastreabilidade aparece em vistas e ADRs? | Um copiloto financeiro derivado do objetivo até componentes e falhas. |
| **5. [Estudo de caso](estudo-de-caso.md)** | Que direção faz sentido sob dados sensíveis e legado? | Comparação disciplinada de quatro desenhos candidatos. |
| **6. [Exercícios](exercicios.md)** | Consigo produzir e defender um desenho conceitual? | Evidências nos seis níveis da Taxonomia de Bloom. |
| **7. [Síntese e referências](sintese-e-referencias.md)** | Como preservar decisões e preparar o próximo passo? | Checklist de rastreabilidade e ponte para RAG. |

## O caso que nos acompanhará

O Banco Lume pretende apoiar analistas que tratam contestações de transações. Hoje eles consultam políticas, dados cadastrais e histórico em sistemas legados, registram uma recomendação e encaminham o caso a um supervisor. A direção pede “um agente que resolva tudo”; Risco exige revisão humana antes de qualquer decisão; Privacidade restringe o trânsito de dados pessoais; Operações informa que parte dos sistemas fica indisponível durante janelas de manutenção.

O objetivo não será confirmar a preferência inicial. Investigaremos se a melhor composição é automação convencional, copiloto com contexto fornecido, RAG ou agente com ferramentas — e se alguma capacidade generativa deve ser rejeitada. O caso aparece apenas depois de construirmos os conceitos e o método de decisão, para não transformar particularidades de um exemplo em regra universal.

## Um princípio de trabalho

Leia cada seta nos dois sentidos: **objetivo → cenário → requisito significativo → mecanismo → evidência**; depois pergunte qual necessidade justifica cada componente, permissão e dependência. Sem resposta, há lacuna de rastreabilidade.

O [NIST AI RMF Generative AI Profile](https://doi.org/10.6028/NIST.AI.600-1) reforça que riscos e impactos devem ser compreendidos no contexto de uso, e não inferidos apenas das capacidades gerais de um modelo. Esse princípio orientará o módulo: arquitetura é uma disciplina de escolha contextual, não um catálogo de caixas.

**Próxima página:** [Oportunidade, CONOPS e fronteiras](conceitos.md).
