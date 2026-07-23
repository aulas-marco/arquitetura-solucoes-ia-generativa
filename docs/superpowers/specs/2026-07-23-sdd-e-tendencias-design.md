# Desenho — SDD e tendências na arquitetura de soluções com IA generativa

**Data:** 23 de julho de 2026  
**Status:** aprovado para revisão do documento

## Objetivo

Fechar as lacunas de ementa sobre GenAI no desenvolvimento de software e tendências da arquitetura, preservando os seis módulos, 24 horas, oito páginas por módulo e as três Unidades de gravação. Os dois temas precisam integrar a arquitetura curricular, e não aparecer como complementos isolados.

## Arquitetura curricular

O percurso passa a explicitar a espinha: **fundamentos → desenho → RAG → agentes e SDD → confiança → operação e tendências**.

- No Módulo 4, SDD é a aplicação central de agentes com ferramentas: transforma autonomia, contratos, testes e gates humanos em um caso concreto de construção de software.
- No Módulo 6, tendências conclui a disciplina: retoma operação, governança, portabilidade, avaliação e estratégia multimodelo como capacidades duráveis para interpretar mudanças em modelos, agentes, plataformas e regulação.
- O plano da disciplina, a matriz de alinhamento, o glossário, o catálogo de padrões e o projeto final registram essa continuidade. O projeto final pode usar SDD como método de execução da entrega.

## SDD no Módulo 4

O GitHub Spec Kit é o fio condutor operacional. O aluno conhece o fluxo `constitution → specification → plan → tasks → implement → verify`, com o arquiteto responsável pela especificação, pelos critérios de aceite e pelos gates de revisão. A oficina usa o fluxo `/speckit.specify → /speckit.plan → /speckit.tasks → /speckit.implement` em uma feature sintética, com alternativa demonstrativa para ambientes sem o CLI.

O conteúdo distribui-se pelas páginas existentes do módulo:

| Página | Papel do SDD |
|---|---|
| Conceitos | comparar vibe coding e desenvolvimento guiado por especificação; explicar a spec como artefato durável |
| Padrões e decisões | apresentar o padrão Desenvolvimento guiado por especificação e localizar gates humanos |
| Exemplo arquitetural | diagramar em Mermaid o pipeline SDD e a squad híbrida de dois papéis humanos e cinco agentes |
| Oficina | executar o mini-fluxo Spec Kit com dados sintéticos, verificação e limpeza |
| Exercícios | praticar SDD nos seis níveis de Bloom, sem gabarito nos níveis superiores |
| Síntese | conectar SDD aos limites de autonomia, confiança e operação |

Kiro, BMAD-METHOD, Tessl, OpenAI Model Spec e a palestra de Sean Grove entram como variações, contrastes ou fundamentos conceituais breves. Um apêndice de materiais adicionais concentra a relação ampliada, impedindo que essas referências concorram com o Spec Kit na narrativa principal.

## Tendências no Módulo 6

A seção final de `sintese-e-referencias.md` aborda contexto longo, multimodalidade, modelos abertos versus hospedados, desenvolvimento agêntico, plataformas corporativas de IA, regulação e governança emergentes. Ela separa sinais de hype e explicita o que permanece no trabalho do arquiteto: decisões de qualidade, evidências, limites, portabilidade e governança.

## Contratos técnicos preservados e ajustados

Permanecem inalterados: navegação e títulos-âncora, tokens e componentes visuais, acessibilidade, Mermaid 11, portabilidade do MkDocs, publicação e ausência de segredos.

O validador continua contando palavras e imagens para fins informativos, mas deixa de rejeitar conteúdo por orçamento e deixa de exigir ou limitar um conjunto fixo de PNGs. Toda imagem referenciada continua exigindo arquivo existente e alt-text não vazio. Os novos diagramas usam Mermaid; nenhum PNG é criado.

## Referências e apêndice

As URLs externas novas são registradas em `fontes.yml` e refletidas na bibliografia, conforme a regra já validada pelo projeto. O apêndice contém os materiais adicionais e suas descrições curtas: GitHub Spec Kit e documentação, anúncio GitHub, Microsoft for Developers, Kiro, BMAD-METHOD, Tessl, OpenAI Model Spec e a palestra “The New Code”.

## Critérios de aceite

1. A espinha curricular explicita SDD no Módulo 4 e tendências no fechamento do Módulo 6, inclusive no plano da disciplina e na matriz de alinhamento.
2. O Spec Kit conduz o conteúdo e a oficina de SDD; as demais fontes aparecem como variações e no apêndice.
3. Não há sétimo módulo, alteração da carga de 24 horas ou renomeação de encontros.
4. Diagramas novos são Mermaid e não há PNG novo.
5. A contagem de palavras e imagens permanece informativa; não existem mais travas de orçamento ou conjunto fixo de imagens.
6. `python -m unittest discover -s tests -v`, `python scripts/validate_content.py --all` e `mkdocs build --strict` terminam sem erro.
