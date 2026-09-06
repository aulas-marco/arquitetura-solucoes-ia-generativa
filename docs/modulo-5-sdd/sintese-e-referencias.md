# Síntese e referências

## Materiais adicionais sobre SDD

O [GitHub Spec Kit](https://github.com/github/spec-kit) é o fio operacional desta disciplina: constitution, specification, plan, tasks, implementação e verificação deixam decisões e critérios de aceite visíveis. As [skills de engenharia de Matt Pocock](https://github.com/mattpocock/skills/tree/main/docs/engineering) oferecem uma variação disciplinada, com *vertical slices*, testes nas interfaces públicas e revisão separada por aderência à spec e padrões do repositório.

[Kiro Specs](https://kiro.dev/docs/specs/), [BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) e [Tessl](https://tessl.io) mostram escolhas diferentes de ambiente, papéis e persistência da especificação. O [OpenAI Model Spec](https://github.com/openai/model_spec) ajuda a discutir regras verificáveis, enquanto a palestra [The New Code](https://www.youtube.com/watch?v=8rABwKRsec4) provoca a tratar especificação como competência de engenharia. São comparações: não substituem o fluxo principal do Spec Kit.

## Síntese do fio SDD

SDD não é “pedir ao modelo para escrever uma spec antes do código”. É desenhar um sistema de desenvolvimento no qual intenção, decisões, tarefas, implementação e evidência permaneçam relacionadas. A especificação assume centralidade porque reduz interpretações silenciosas e oferece um contrato versionado; não porque linguagem natural seja mais precisa que código por natureza.

A progressão completa é:

1. **Constitution:** princípios de alcance organizacional restringem todos os trabalhos.
2. **Specify:** problema, atores, regras, qualidade, segurança e fora de escopo tornam a intenção revisável.
3. **Clarify:** perguntas de alto impacto separam fatos, hipóteses, desconhecidos e decisões.
4. **Plan:** arquitetura, contratos, dados, ADRs, migração e testes traduzem intenção em abordagem.
5. **Tasks:** fatias verticais e dependências tornam trabalho executável e demonstrável.
6. **Analyze:** cobertura e consistência são avaliadas antes do custo de implementação.
7. **Implement:** agentes executam decisões aprovadas em ciclos test-first.
8. **Verify:** aderência à spec e qualidade técnica são revisadas separadamente.
9. **Operate:** métricas, incidentes e aprendizagem de produção atualizam requisitos e experimentos.

O fluxo não é linear no sentido de waterfall. Um protótipo pode revelar que uma hipótese não se sustenta e devolver o trabalho à spec ou ao plano. O que muda é a disciplina: a descoberta atualiza o artefato que governa a próxima transformação. A equipe não continua implementando com base numa decisão que só existe em conversa.

## O papel do arquiteto

Em SDD, o arquiteto deixa de ser apenas autor de diagramas e revisor tardio. Ele ajuda a projetar o próprio sistema de produção de software:

- escolhe seams estáveis e limites de módulos;
- traduz atributos de qualidade em cenários e experimentos;
- registra alternativas e consequências em ADRs;
- identifica blast radius e estratégia de migração;
- define quais decisões podem ser delegadas;
- posiciona portões (*gates*) e evidências;
- impede que automação amplie autoridade;
- conecta telemetria e incidentes à evolução da spec.

Ser “dono da spec” não significa escrever toda a prosa. Significa responder pela coerência entre intenção, arquitetura e evidência técnica. Produto continua responsável por valor, regra e prioridade; segurança e operação mantêm suas autoridades; agentes produzem rascunhos, pesquisa, código e análises.

## Checklist antes de implementar

- [ ] A constitution possui princípios verificáveis, não slogans.
- [ ] O problema e o público estão delimitados.
- [ ] Termos de domínio possuem significado compartilhado.
- [ ] Fatos, hipóteses e desconhecidos estão separados.
- [ ] Requisitos descrevem comportamento, não tecnologia acidental.
- [ ] Critérios cobrem sucesso, negação, conflito, falha e casos extremos relevantes.
- [ ] Atributos de qualidade têm medida, ambiente e volume.
- [ ] Segurança e privacidade aparecem antes do código.
- [ ] Fora de escopo evita expansão plausível.
- [ ] O plano leu o sistema existente e preserva interfaces estáveis.
- [ ] ADRs registram decisões significativas.
- [ ] Seams de teste correspondem às interfaces de uso.
- [ ] Tarefas são fatias demonstráveis com bloqueadores.
- [ ] Cada requisito prioritário possui tarefa e teste planejado.
- [ ] Gates identificam pessoa, versão, evidência e consequência.
- [ ] Fitness functions têm limiar, responsável e consequência diante da falha.

## Checklist antes do merge

- [ ] Testes foram observados falhando pelo motivo esperado antes da implementação.
- [ ] A suíte relevante e as verificações globais estão verdes.
- [ ] Critérios de aceite possuem evidência rastreável.
- [ ] Revisão de Spec não encontrou requisito ausente ou expansão de escopo (*scope creep*).
- [ ] Revisão de Standards avaliou arquitetura, código e testes.
- [ ] Segurança revisou superfícies e casos negativos.
- [ ] Migração, rollback e operação estão definidos.
- [ ] Riscos residuais possuem dono, prazo e gatilho.
- [ ] Spec, plano, tarefas, ADRs e documentação refletem o comportamento entregue.
- [ ] Nenhuma decisão humana foi sobrescrita por regeneração automática.

## Perguntas críticas para qualquer proposta de SDD

1. Qual artefato é autoritativo quando conversa, spec e código divergem?
2. Quem pode aprovar mudança de requisito, arquitetura e risco?
3. Como o método torna desconhecidos visíveis?
4. Que transformação cada agente realiza e quais ferramentas recebe?
5. Onde a implementação deve pausar em vez de inferir?
6. Quais tarefas são realmente independentes?
7. Que teste observa a mesma interface usada pelo consumidor?
8. Como provar aderência à spec sem confundir com qualidade de código?
9. O que acontece quando produção contradiz uma premissa?
10. Qual parte do processo pode ser removida para uma tarefa simples sem perder controle?

Se a resposta for apenas “o agente segue os documentos”, ainda falta arquitetura. É preciso definir autoridade, estado, contratos, gates, falhas e evidência como em qualquer outro sistema agêntico.

## Comparação das abordagens

| Abordagem | Ênfase útil | Cuidado arquitetural |
|---|---|---|
| Spec Kit | fluxo reproduzível e artefatos conectados | comandos e templates evoluem; fixe versão |
| Matt Pocock | perguntas, fatias verticais, deep modules, TDD e revisão dual | skills pressupõem disciplina e integração com tracker |
| Kiro | requisitos, design e tasks próximos ao IDE; EARS | experiência da ferramenta não substitui governança externa |
| BMAD-METHOD | papéis e histórias para coordenar agentes | multiplicar personas pode aumentar handoffs |
| Tessl | spec residente e reutilização por registro | avaliar portabilidade e dependência da plataforma |
| Model Spec | regras comportamentais verificáveis por avaliações | especificação de modelo não equivale a spec de produto |

O objetivo do apêndice é oferecer vocabulário comparativo. A turma pratica Spec Kit para observar um fluxo comum; deve conseguir substituir a ferramenta e preservar princípios.

## Limites honestos

SDD exige investimento. Specs podem envelhecer, agentes podem gerar coerência aparente e gates podem virar cerimônia. Não há garantia de que regenerar código seja mais barato que mantê-lo. Sistemas brownfield possuem decisões históricas que não cabem num documento novo. Requisitos sociais e organizacionais continuam ambíguos mesmo com templates.

Por isso, maturidade não é “usar todos os comandos”. É escolher profundidade proporcional, medir retrabalho e defeitos, revisar artefatos como código e abandonar partes do processo que não produzem decisão ou evidência. A principal defesa contra burocracia é a mesma contra geração irresponsável: cada artefato deve ter consumidor, função e critério de qualidade.
