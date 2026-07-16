# Relatório — Task 1: contrato testável de letramento aplicado

## Escopo executado

- Criado `tests/test_applied_literacy.py` com o contrato das seis oficinas, incluindo as três rotas de acesso, níveis conservadores de Bloom, atividade, evidência, segurança/custo e a exigência de acesso sem cartão.
- Incluído no mesmo contrato o guia compartilhado e o projeto final: política de equidade, trabalho em grupo, duas opções, evidências e ausência de benefício por ferramenta paga.
- Atualizado `tests/test_pedagogical_shell.py` para exigir oito páginas para os módulos 4–6 e o link explícito da oficina em todos os módulos.
- Nenhum conteúdo didático, índice de conteúdo, validador ou página de curso foi alterado.

## Commits

- `aa68f0a test: define applied tool literacy contract`

## Testes e verificações

| Comando | Resultado |
|---|---|
| `python -m unittest tests.test_applied_literacy.AppliedLiteracyTest.test_every_module_has_an_accessible_tool_workshop -v` | Falhou como esperado com `FileNotFoundError` para `docs/modulo-1-fundamentos/oficina-de-ferramentas.md`. |
| `python -m unittest tests.test_applied_literacy tests.test_pedagogical_shell -v` | Falhou somente em novas exigências ainda não implementadas: oficinas/guia compartilhado ausentes e links das oficinas ausentes; as quatro verificações preexistentes de `test_pedagogical_shell` passaram. |
| `git diff --check` | Passou, sem erro de whitespace. |

## Auto-revisão

- O teste usa `MODULES` como fonte única dos seis módulos e preserva `PAGES` para as sete páginas existentes, somando explicitamente a oficina como a oitava.
- A rota essencial exige literalmente `não depende de cartão` em cada oficina, garantindo que toda atividade obrigatória tenha alternativa sem cartão.
- As verificações de Bloom permitem somente `Compreender`, `Aplicar` ou `Analisar` e rejeitam `Avaliar` e `Criar` na declaração de Bloom da oficina.

## Preocupações

- A suíte conjunta está propositalmente vermelha até as tarefas de conteúdo criarem as seis oficinas, `docs/referencia/guia-de-ferramentas.md`, `docs/sobre/projeto-final.md` e os links nos índices.
- Não há preocupação de regressão nas verificações pedagógicas já existentes: elas foram executadas na mesma descoberta e passaram.

## Correção pós-revisão

- Fortalecido apenas `tests/test_applied_literacy.py`: cada seção operacional precisa ter conteúdo não vazio; a atividade obrigatória deve declarar a rota essencial sem cartão; as rotas institucional e comercial devem declarar que não acrescentam pontos; a declaração Bloom agora aceita exclusivamente Compreender, Aplicar e Analisar; e as seções de atividade, evidência e segurança/custo precisam conectar explicitamente decisão arquitetural, atividade, evidência e segurança/custo.

| Comando | Resultado |
|---|---|
| `python -m unittest tests.test_applied_literacy -v` | Falhou como esperado antes da criação do conteúdo: oficinas e guia compartilhado ainda inexistentes (`FileNotFoundError`). O teste ampliado foi descoberto e executado. |
| `python -m unittest tests.test_applied_literacy tests.test_pedagogical_shell -v` | Falhou como esperado apenas nas oficinas/guia ainda ausentes e nos links/mapas de oficina ainda não criados; as cinco verificações preexistentes do shell pedagógico passaram. |
| Verificação isolada da expressão Bloom e `git diff --check` | A expressão aceitou `Compreender`, `Aplicar` e `Analisar`, rejeitou `Lembrar` e `Criar`; sem erro de whitespace. |

## Correção da re-revisão

- A extração de seção agora termina no próximo heading de mesmo nível ou superior. Assim, cada rota `###` é avaliada sem absorver conteúdo das demais rotas ou da próxima seção `##`.
- `## Decisão arquitetural em foco` agora precisa ter conteúdo útil não vazio e mencionar explicitamente a `atividade guiada` dentro da própria seção; menções em outras seções não satisfazem o contrato.
- Incluído teste de regressão para a fronteira de headings `###` e `##`.

| Comando | Resultado |
|---|---|
| `python -m unittest tests.test_applied_literacy.AppliedLiteracyTest.test_section_stops_at_a_heading_of_the_same_or_higher_level -v` | Passou: 1 teste. |
| `python -m unittest tests.test_applied_literacy tests.test_pedagogical_shell -v` | Falhou como esperado no estado atual do worktree: 2 erros por oficinas/guia inexistentes e 9 falhas por links/mapas de oficina ainda ausentes; a nova regressão de fronteira de seção passou e as verificações preexistentes restantes passaram. |
| `git diff --check` | Passou, sem erro de whitespace. |
