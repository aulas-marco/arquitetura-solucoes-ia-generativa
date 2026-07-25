# Módulo 2 — Do problema ao dossiê conceitual

> **Pergunta-guia:** Como evitar construir a solução de IA certa para o problema errado?

Uma equipe pode selecionar um modelo competente, implementar controles rigorosos e ainda fracassar: basta otimizar uma capacidade que não resolve a necessidade real, automatizar uma decisão que deveria continuar humana ou introduzir IA generativa onde regras convencionais seriam mais previsíveis. Antes de componentes e produtos, a arquitetura precisa estabelecer propósito, fronteiras, responsabilidades e evidências de sucesso.

Este módulo transforma uma oportunidade ambígua em um **dossiê conceitual**, nome adotado pelo curso para o conjunto curto de entradas, vistas, análises, decisões e evidências que permite iniciar — ou recusar — uma solução. O percurso é sempre o mesmo: oportunidade, hipótese de valor, atividades humanas, CONOPS, fronteiras, requisitos significativos, vistas, táticas, alternativas, experimento e ADR. Só depois compararemos soluções; prompt, RAG, fine-tuning, workflows e agentes são respostas possíveis, não o ponto de partida.

## Antes de começar

Você deve dominar o vocabulário do [Módulo 1 — Fundamentos](../modulo-1-fundamentos/index.md): modelo, aplicação de IA, sistema sociotécnico, componentes determinísticos e probabilísticos, contexto, RAG, ferramentas, workflows, agentes, avaliação e trade-offs. Também retomaremos o [Catálogo de atributos de qualidade](../referencia/atributos-de-qualidade.md) e o [Template de ADR](../referencia/template-adr.md).

Não é necessário conhecer um provedor, modelo ou framework específico. As decisões deste módulo são deliberadamente independentes de fornecedor e devem continuar úteis quando produtos, preços e capacidades mudarem.

**Tempo estimado de leitura:** 60–90 minutos, sem contar o estudo de caso e os exercícios de projeto.

## Objetivos de aprendizagem

Ao concluir o módulo, você deverá ser capaz de:

1. **Compreender** uma oportunidade como hipótese de valor e expressá-la por meio de stakeholders, fronteiras, cenários e modos operacionais.
2. **Aplicar** critérios de adequação e rejeição para decidir se IA generativa participa da solução e qual responsabilidade permanece humana.
3. **Analisar** objetivos e requisitos para identificar RAS, cenários de qualidade, táticas, sensibilidades, trade-offs e riscos.
4. **Avaliar** alternativas por capacidade adicionada, responsabilidade criada, vistas afetadas, evidência mínima e condição de rejeição.
5. **Criar** um dossiê conceitual rastreável, com vistas de contexto, responsabilidades, interação, informação e implantação, regras de correspondência, ADRs e proveniência.

## Roteiro do módulo

| Página | Questão central | Resultado esperado |
|---|---|---|
| **1. Abertura** | Qual é o contrato de aprendizagem? | Uma sequência que parte do problema, não da tecnologia. |
| **2. [Conceitos](conceitos.md)** | Que descrição precisamos antes de escolher solução? | Entradas, vistas, análise, decisão, evidência e vocabulário preciso. |
| **3. [Padrões e decisões](padroes-e-decisoes.md)** | Como RAS orientam alternativas? | Táticas, mecanismos, correspondências, trade-offs, experimentos e ADRs. |
| **4. [Exemplo arquitetural](exemplo-arquitetural.md)** | Como a rastreabilidade aparece nas cinco vistas? | Um copiloto financeiro derivado do objetivo até riscos, estruturas e evidências. |
| **5. [Estudo de caso](estudo-de-caso.md)** | Que direção faz sentido sob dados sensíveis e legado? | Comparação disciplinada de quatro desenhos candidatos. |
| **6. [Oficina de ferramentas](oficina-de-ferramentas.md)** | Como uma ferramenta torna visível a decisão estudada? | Uma evidência breve, comparável e segura. |
| **7. [Exercícios](exercicios.md)** | Consigo produzir e defender um desenho conceitual? | Evidências nos seis níveis da Taxonomia de Bloom. |
| **8. [Síntese e referências](sintese-e-referencias.md)** | Como preservar decisões e preparar o próximo passo? | Checklist de rastreabilidade e ponte para RAG. |

## Caso condutor: Banco Lume

O Banco Lume pretende apoiar analistas que tratam contestações de transações. Hoje eles consultam políticas, dados cadastrais e histórico em sistemas legados, registram uma recomendação e encaminham o caso a um supervisor. A direção pede “um agente que resolva tudo”; Risco exige revisão humana antes de qualquer decisão; Privacidade restringe o trânsito de dados pessoais; Operações informa que parte dos sistemas fica indisponível durante janelas de manutenção.

O objetivo não será confirmar a preferência inicial. Investigaremos se a melhor composição é automação convencional, copiloto com contexto fornecido, RAG ou agente com ferramentas — e se alguma capacidade generativa deve ser rejeitada. A Cooperativa Aurora, mais adiante, será o **caso de transferência**: aplica o mesmo método em outro domínio sem copiar a solução do Banco Lume.

## Um princípio de trabalho

Leia cada seta nos dois sentidos: **objetivo → cenário → requisito significativo → alternativa → evidência**; depois pergunte qual necessidade justifica cada componente, permissão e dependência. Para toda evidência, registre origem, autoridade, versão, transformação e uso. Sem resposta, há lacuna de rastreabilidade ou proveniência.

O [NIST AI RMF Generative AI Profile](https://doi.org/10.6028/NIST.AI.600-1) reforça que riscos e impactos devem ser compreendidos no contexto de uso, e não inferidos apenas das capacidades gerais de um modelo. Esse princípio orientará o módulo: arquitetura é uma disciplina de escolha contextual, não um catálogo de caixas.

**Próxima página:** [Oportunidade, CONOPS e fronteiras](conceitos.md).
