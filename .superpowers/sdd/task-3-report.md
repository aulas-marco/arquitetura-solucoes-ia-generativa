# Task 3 — módulos 3 e 4

## Status

Concluído. As atividades avançadas de RAG e agentes agora explicam os artefatos pedidos no enunciado, apontam para conceitos, padrões, exemplo e oficina local, e terminam com uma checklist de verificação.

## Alterações

- Módulo 3: definições operacionais de chunk, conjunto de referência, `Recall@5`, `Precision@5`, chunking, proveniência, autorização antecipada, cache, citação, padrões RAG, `p95`, suficiência, abstenção e rollback; fórmulas com numerador/denominador e fonte da referência; tabelas e checklists para as quatro atividades avançadas.
- Módulo 4: definições de contrato de ferramenta, idempotência, A0–A5, aprovação, trace, timeout, estado desconhecido, agente único/multiagente/workflow e agente controlado; campos a registrar, fronteiras de execução e checklists para seleção, autonomia, diagnóstico, crítica e criação.
- Mantidos Bloom, percentuais de critérios de avaliação, respostas públicas apenas em Recordar/Compreender e restrição a dados sintéticos/local.

## Commits

- `df1cde4` — `docs: clarify retrieval and agent exercises`
- `7c80abc` — `docs: keep retrieval exercises within budget`

## Testes

- `python -m unittest tests.test_module_three tests.test_module_four -v`: 17 testes, OK.
- `python scripts/validate_content.py --all`: OK (48 páginas, 20 imagens, 36 exercícios).
- A suíte completa ainda acusa falhas nos contratos editoriais dos módulos 5 e 6, que estão sendo tratados nas outras tarefas; não há falhas nos testes específicos dos módulos 3 e 4.

## Concerns

Nenhuma mudança de código ou ferramenta foi necessária. O limite de palavras do módulo 3 foi respeitado após condensação das novas orientações.

## Revisão pós-feedback

- Removidos valores canônicos de `Recall@5`/`Precision@5`; o aluno preenche fórmulas e numeradores. Incluído template de tabela com cinco posições.
- Corrigida a inconsistência de chunking: a atividade agora entrega quatro estratégias.
- Nomeados os três arquivos `.txt` (`portal-estorno.txt`, `politica-campanha.txt`, `politica-reembolso.txt`) e `rag_local.py`.
- A escala de autonomia agora aponta para a âncora da matriz e descreve A0, A1, A2, A3, A4 e A5 explicitamente.
- O diagnóstico de agentes separa a observação externa de duas reservas do que o trace realmente comprova.
- M3 ficou com 9.918 palavras no validador, deixando margem abaixo do teto de 10.000.
- M3/M4 #12 definem ADR como registro de decisão arquitetural e listam seus campos; M4 #8 aponta para a âncora de saída estruturada.
- Adicionada regressão que rejeita valores numéricos calculados nos enunciados avançados de recuperação.

### Teste de cobertura pós-feedback

`python scripts/validate_content.py --module modulo-3-rag`: OK (9.918 palavras).

`python -m unittest tests.test_module_three tests.test_module_four tests.test_pedagogical_shell.PublicExerciseAnswerPolicyTest.test_advanced_retrieval_exercises_do_not_reveal_metric_values -v`: 18 testes, OK.

O contrato amplo `test_advanced_exercises_explain_artifacts_and_procedure` continua apontando apenas as oito lacunas já existentes nos módulos 5 e 6; nenhum caso dos módulos 3 ou 4 falhou. A validação completa permanece OK.
