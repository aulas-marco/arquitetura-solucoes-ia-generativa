# Enunciados explícitos para exercícios de arquitetura de IA

## Objetivo

Revisar os exercícios dos seis módulos para que um arquiteto de software que ainda está construindo repertório em IA consiga executar cada instrução sem adivinhar o significado do artefato, sua localização no material ou o formato da entrega.

## Problema observado

Os exercícios preservam desafios de Aplicar, Analisar, Avaliar e Criar, mas algumas instruções usam termos como “fronteira”, “baseline”, “trace”, “SLO”, “ADR” e “critério” como se o aluno já soubesse onde encontrá-los e como representá-los. Isso torna o enunciado hermético: a dificuldade passa a ser decifrar a instrução, e não tomar a decisão arquitetural.

## Decisão editorial

Cada exercício avançado manterá a estrutura existente e receberá explicações locais, próximas do ponto de uso:

1. **O que é:** definição breve do objeto pedido, em linguagem de arquitetura de soluções.
2. **Onde encontrar:** link para o conceito, exemplo, template ou saída de oficina que serve de referência.
3. **Como produzir:** procedimento numerado, com ações observáveis e ordem de execução.
4. **Como verificar:** teste de completude ou pergunta de revisão antes da entrega.

Os quatro blocos não precisam aparecer com esses títulos em cada linha. Quando vários passos usam o mesmo objeto, uma subseção “Como ler o enunciado” poderá concentrar as definições e links. O procedimento específico continuará junto da atividade para evitar que o aluno precise reconstruir a tarefa a partir de páginas distantes.

## Exemplo de aplicação

Instrução hermética:

> Desenhe duas fronteiras: uma entre extração e regra de negócio, e outra entre proposta e efeito financeiro.

Versão explícita:

> **O que é uma fronteira:** é a separação entre responsabilidades e efeitos. **Onde olhar:** consulte o diagrama de componentes do [exemplo arquitetural](../../modulo-1-fundamentos/exemplo-arquitetural.md) e a distinção entre comportamento determinístico e probabilístico em [Conceitos](../../modulo-1-fundamentos/conceitos.md). **Como fazer:** desenhe uma caixa “Extração do recibo”, uma caixa “Regra de limite” e uma caixa “Lançamento financeiro”; ligue as caixas e escreva em cada seta o dado transferido e quem valida a saída. Repita com “Proposta de despesa” e “Lançamento aprovado”. **Como verificar:** a proposta apenas sugere; o lançamento altera o sistema financeiro e exige autorização explícita.

## Escopo

- Revisar os seis arquivos `docs/modulo-*/exercicios.md`.
- Priorizar Aplicar, Analisar, Avaliar e Criar, sem remover perguntas de Recordar e Compreender.
- Explicar cada artefato ou termo operacional que aparece como entrada, ação ou entrega.
- Referenciar conceitos, exemplos, oficinas, glossário e templates já existentes antes de criar material duplicado.
- Manter os critérios de avaliação percentuais e a política de não publicar respostas canônicas para os níveis avançados.
- Não trocar as ferramentas locais das oficinas nem alterar a sequência de Bloom.

## Critérios de aceitação

- Cada atividade avançada declara o contexto, o papel do aluno, os insumos e a entrega.
- Cada instrução que pede desenho, tabela, cálculo, trace, cenário, ADR, métrica, teste, fronteira, fluxo ou decisão explica o objeto, aponta uma referência e descreve como verificar o resultado.
- Termos essenciais de IA e arquitetura têm link para uma definição acessível na primeira ocorrência relevante.
- O aluno consegue identificar arquivos, seções, campos ou caixas que precisa usar sem depender de conhecimento implícito.
- A suíte de testes, o validador de conteúdo e o build estrito do MkDocs continuam aprovados.

## Fora de escopo

- Não produzir gabaritos para as atividades avançadas.
- Não reduzir o desafio cognitivo de Bloom a perguntas de memorização.
- Não exigir ferramentas pagas ou dados reais.
- Não reescrever conceitos inteiros quando um link contextualizado e uma definição curta forem suficientes.
