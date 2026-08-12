# Fundação transversal do Módulo 1 — desenho

**Data:** 2026-07-25
**Status:** aprovado para implementação

## Objetivo

Reorientar o Módulo 1 como vocabulário comum dos módulos 2–6, equilibrando desenho conceitual, conhecimento, autonomia, confiança e operação sem antecipar o detalhamento de cada tema.

## Princípios

1. Modelo, aplicação e sistema sociotécnico permanecem as unidades de análise.
2. A superfície comportamental reúne modelo, parâmetros, prompt, contexto, fontes, ferramentas, políticas, estado, memória e implantação.
3. Geração, decisão, autorização e efeito são responsabilidades distintas.
4. Conhecimento, contexto, estado, memória, evidência e trace têm ciclos de vida próprios.
5. Teste de software, avaliação comportamental e verificação arquitetural respondem a perguntas diferentes; fitness functions introduzem a verificação contínua.
6. O panorama de abordagens orienta o curso, mas RAG deixa de dominar exemplo, decisão e caso.
7. A anatomia da solução é um mapa de responsabilidades dentro de “Padrões e decisões”, não um estilo em oito camadas nem uma nova categoria de página.
8. Afirmações absolutas sobre decisão arquitetural, prompt, embedding, contexto e conhecimento paramétrico serão substituídas por definições proporcionais.

## Estrutura pedagógica

- `index.md` explicita o mapa Módulo 1 → módulos 2–6.
- `conceitos.md` apresenta a superfície comportamental, os limites do modelo e os três tipos de verificação por meio de uma progressão narrativa, sem funcionar como glossário de termos independentes.
- `padroes-e-decisoes.md` compara famílias de composição, contém o mapa de responsabilidades e substitui a ADR detalhada por uma ficha de decisão inicial.
- `exemplo-arquitetural.md` aplica o mapa ao atendimento Horizonte, com escopo, fluxo, falhas e evidências.
- `estudo-de-caso.md` exige decisão equilibrada sobre conhecimento, efeito, confiança e operação.
- `oficina-de-ferramentas.md` continua observando contexto e variabilidade, mas relaciona a evidência ao pacote comportamental.
- `exercicios.md` aplica o vocabulário transversal e prepara explicitamente os módulos seguintes.
- `sintese-e-referencias.md` consolida o mapa do curso e remove repetições.

### Progressão narrativa de `conceitos.md`

A página será organizada em cinco movimentos. Cada movimento parte de uma pergunta arquitetural, incorpora os termos necessários para respondê-la e prepara o movimento seguinte:

1. **O que muda no sistema:** relaciona comportamento determinístico e probabilístico às unidades modelo, aplicação e sistema sociotécnico.
2. **De onde emerge o comportamento:** reúne modelo fundacional, treinamento, inferência, prompt, parâmetros, tokens, contexto e conhecimento paramétrico dentro da superfície comportamental.
3. **Que informação atravessa o sistema:** distingue conhecimento, contexto, embeddings, evidência, estado, memória e trace pelos respectivos usos e ciclos de vida.
4. **Como distribuir responsabilidade:** conecta atributos de qualidade e significância arquitetural à separação entre geração, decisão, autorização e efeito; multimodalidade aparece como variação que amplia dados, interfaces e riscos.
5. **Como verificar e governar:** diferencia teste de software, avaliação comportamental e verificação arquitetural; apresenta fitness functions como continuidade da evidência.

Os títulos técnicos poderão permanecer como subtítulos quando ajudarem a consulta posterior, mas não interromperão o argumento principal. Cada movimento terminará com uma consequência arquitetural ou uma pergunta que introduza o seguinte.

O mapa visual será apresentado depois da finalidade do arquiteto e interpretado como orientação de leitura, não como arquitetura de referência. Nomes de produtos permanecerão na oficina e no guia de ferramentas.

## Limites

- Preservar oito páginas, seis níveis de Bloom, laboratório local e independência de fornecedor.
- Não ensinar visões, táticas ou ADRs em profundidade; essa responsabilidade permanece no Módulo 2.
- Não detalhar pipelines de RAG, trajetórias de agentes, modelagem de ameaças ou LLMOps.
- Preservar imagens úteis, alterando títulos e interpretação quando a classificação atual induzir erro.

## Verificação

- Testes específicos devem impedir o retorno da taxonomia de “oito camadas”, das afirmações absolutas corrigidas e da predominância de RAG.
- A ordem das seções deve seguir os cinco movimentos e preservar as âncoras usadas por links internos.
- A página deve definir todos os termos existentes sem criar uma lista de definições desconectadas.
- A transição final deve explicar como o contrato arquitetural prepara padrões e decisões e os módulos 2–6.
- Executar validação editorial, suíte Python e build estrito do MkDocs.
