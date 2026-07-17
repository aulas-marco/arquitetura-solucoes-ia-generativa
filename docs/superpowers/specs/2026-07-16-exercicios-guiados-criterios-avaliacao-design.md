# Exercícios guiados e critérios de avaliação — desenho

**Data:** 2026-07-16  
**Status:** aprovado para especificação e revisão docente

## Objetivo

Tornar as atividades de níveis Aplicar, Analisar, Avaliar e Criar acessíveis a arquitetos de software que ainda estão construindo repertório em IA generativa. O material deve conduzir a investigação e a tomada de decisão sem entregar uma resposta pronta. Em paralelo, substituir a linguagem de avaliação baseada em “rubrica” e pontos por critérios claros com pesos percentuais.

## Público e princípio pedagógico

Os estudantes já conhecem fundamentos de arquitetura de software, mas podem não saber como transformar evidência sobre modelos, dados, recuperação, agentes, risco ou operação em decisão arquitetural. Cada atividade avançada deve reduzir a ambiguidade inicial, explicitar os artefatos de partida e tornar visível o caminho de raciocínio esperado. A complexidade fica na análise e na justificativa, não em adivinhar o formato da entrega.

## Escopo

### Exercícios dos seis módulos

Reestruturar as questões de Aplicar, Analisar, Avaliar e Criar nas seis páginas `docs/modulo-*/exercicios.md`. Cada questão passará a conter, nesta ordem:

1. **Situação:** contexto sintético e limitado, ligado ao tema do módulo.
2. **Seu papel:** responsabilidade do aluno como arquiteto em início de atuação com IA.
3. **Insumos disponíveis:** páginas do módulo, oficina, corpus, trace, tabela ou cenário que pode ser usado.
4. **Como conduzir:** de três a cinco passos progressivos; observar, separar fatos de hipóteses, organizar evidências, comparar alternativas e justificar a decisão.
5. **Entrega esperada:** artefato, formato e limite proporcional de escopo.
6. **Critérios de avaliação:** tabela com pesos em percentuais que totalizam 100%, descrição observável do que será avaliado e, quando necessário, um limite de aceitabilidade.

Questões de Recordar e Compreender mantêm o formato atual de autocorreção. As questões avançadas não terão gabarito público nem solução canônica.

### Projeto final

Renomear a seção `Rubrica` em `docs/sobre/projeto-final.md` para `Critérios de avaliação`. Converter a coluna de pontos para percentuais, mantendo os seis aspectos avaliados e total de 100%. Ampliar a descrição de cada critério para indicar evidência mínima, qualidade esperada e erro frequente a evitar.

### Linguagem de avaliação em conteúdo publicado

Substituir “rubrica” e suas flexões em conteúdo destinado ao aluno por vocabulário adequado ao contexto:

| Uso atual | Substituição | Uso pretendido |
|---|---|---|
| rubrica de atividade | critérios de avaliação | correção de exercícios e projeto |
| rubrica humana | critérios qualitativos de avaliação humana | julgamento humano de respostas de IA |
| rubrica aplicada por modelo | critérios de avaliação aplicados por modelo | avaliação assistida por modelo |
| métrica ou rubrica | métrica ou critério qualitativo | critério de aceitação de comportamento |

Documentos internos em `docs/superpowers/` não serão alterados, pois registram decisões anteriores e não são conteúdo pedagógico publicado.

## Formato de critérios

Os critérios usam percentuais exclusivamente como peso relativo para orientar a atenção do estudante; não definem cálculo obrigatório de nota. Cada tabela deve:

- totalizar 100%;
- usar no máximo cinco critérios nas questões Aplicar e Analisar, e no máximo seis em Avaliar e Criar;
- nomear um resultado observável, não uma palavra genérica como “qualidade”; e
- explicar o que evidencia atendimento adequado, com vocabulário de arquitetura.

Exemplo de estrutura, sem resposta do exercício:

| Critério | Peso | O que evidencia atendimento adequado |
|---|---:|---|
| Evidência usada | 30% | Diferencia fatos fornecidos, suposições e lacunas. |
| Decisão arquitetural | 35% | Conecta uma alternativa a requisitos, riscos e consequências. |
| Verificação | 35% | Define medida, limite e condição que levaria à revisão da decisão. |

## Progressão por Bloom

- **Aplicar:** executar um procedimento já apresentado e registrar o efeito em um cenário delimitado.
- **Analisar:** separar componentes, relações, causas possíveis e evidências insuficientes antes de explicar uma falha ou trade-off.
- **Avaliar:** emitir recomendação condicionada, comparar alternativas com critérios e definir o que poderia reverter a decisão.
- **Criar:** compor uma proposta coerente a partir dos elementos anteriores, delimitando escopo, responsabilidades, testes e evolução.

As instruções devem iniciar pelo menor passo útil. Termos como “investigação refutável”, “fatia” ou “direcionador” serão definidos no próprio enunciado ou ligados a uma página que os explica antes de serem exigidos.

## Verificação

Atualizar testes de conteúdo para garantir que as seis páginas de exercícios:

- não contenham o rótulo `Rubrica` nem expressões de pontuação;
- tenham critérios percentuais nas atividades avançadas; e
- contenham os seis blocos de condução previstos.

Executar a suíte de testes, o validador de conteúdo e o build estrito do MkDocs.

## Limites

- Não criar respostas-modelo para Aplicar, Analisar, Avaliar e Criar.
- Não alterar a quantidade de exercícios, os temas dos módulos ou a política de respostas públicas dos níveis iniciais.
- Não mudar termos em documentos internos de histórico e planejamento.
