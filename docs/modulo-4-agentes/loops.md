# Loops agênticos

Quem aciona o arnês (*harness*), quantas vezes, e o que precisa estar verificável antes de entregar mais uma coisa à máquina.

## Quatro níveis de loop

O arnês responde à pergunta "o que cerca o modelo". Falta a pergunta seguinte: **quem aciona o arnês, e quantas vezes**. É o que a engenharia de loop trata.

O ciclo básico já está descrito nas seções anteriores, e a Anthropic o formula em quatro tempos em [Building agents with the Claude Agent SDK](https://claude.com/blog/building-agents-with-the-claude-agent-sdk): **reunir contexto, agir, verificar o trabalho, repetir**. Cada rodada de uma conversa com um agente já é uma execução desse ciclo. A pergunta de engenharia é quanto dele fica com a pessoa e quanto passa para o sistema.

A Anthropic organiza a resposta em [Getting started with loops](https://claude.com/blog/getting-started-with-loops) como uma escada de quatro degraus. A escada se lê assim: **a cada degrau você entrega uma coisa a mais para a máquina**, e o que você entrega é exatamente o que precisa ter tornado verificável antes de subir.

| Nível | O que dispara | O que você entrega | Como o loop para | Exemplo |
|---|---|---|---|---|
| 1 — por rodada | seu *prompt* | a verificação | o agente julga que terminou ou precisa de contexto | pedir uma alteração, o agente edita, testa e responde |
| 2 — por objetivo | seu *prompt*, uma vez | a condição de parada | o objetivo é atingido ou o teto de rodadas é alcançado | "rode até a suíte de testes passar" |
| 3 — por tempo | um intervalo ou agendamento | o gatilho | você cancela ou o trabalho termina | a cada cinco minutos, verificar a fila e tratar o que chegou |
| 4 — proativo | um evento, sem pessoa presente | o próprio *prompt* | cada tarefa encerra ao atingir seu objetivo; a rotina roda até ser desligada | triagem contínua de erros reportados |

A diferença entre o nível 1 e o nível 2 é a mais importante e a menos percebida. No nível 1, o agente para quando **acha** que terminou. No nível 2, ele para quando um critério objetivo é satisfeito. Trocar julgamento por critério é o que permite tirar a pessoa da frente sem trocar supervisão por esperança.

### De uma piada a uma disciplina

A técnica que popularizou o nível 2 é deliberadamente simples. Em [Ralph Wiggum as a "software engineer"](https://ghuntley.com/ralph/), de 14 de julho de 2025, Geoffrey Huntley publicou um laço de uma linha:

```bash
while :; do cat PROMPT.md | claude-code ; done
```

O nome homenageia o personagem menos brilhante dos Simpsons, e a descrição do autor é honesta: a técnica é "deterministicamente ruim num mundo indeterminado". Ela funciona porque o estado não vive na conversa, vive nos arquivos e no histórico do repositório: cada iteração começa com contexto limpo e enxerga o que a anterior deixou no disco. Huntley é explícito sobre a condição que sustenta o laço, e que ele chama de contrapressão obrigatória: testes, análise estática e portões de validação que rejeitam código ruim. Sem isso, o laço apenas repete.

Um ano depois, a mesma ideia aparece como mecanismo de produto. A Anthropic distribui um [plugin oficial Ralph Wiggum](https://github.com/anthropics/claude-code/blob/main/plugins/ralph-wiggum/README.md) que implementa o laço dentro da própria sessão: um *hook* de encerramento bloqueia a saída e reinjeta o mesmo *prompt*. A documentação do plugin traz dois avisos que valem como princípio de projeto, muito além da ferramenta. O primeiro: a frase de conclusão é comparada por igualdade exata de texto, portanto não distingue "terminei com sucesso" de "terminei bloqueado", e o mecanismo de segurança primário passa a ser o **limite de iterações**. O segundo é a lista de casos em que não se deve usar laço: tarefas que exigem julgamento humano, operações de uma vez só, tarefas sem critério de sucesso claro e depuração em produção.

O que esse par ensina é direto. O nível 2 é uma decisão de projeto sobre autoridade e orçamento, com as mesmas perguntas de qualquer sistema agêntico: qual é a condição de parada, quem responde por ela, qual é o teto de consumo e o que acontece quando o teto é atingido sem sucesso.

### O gargalo é o verificador

O componente com maior retorno documentado é a verificação. Boris Cherny, criador do Claude Code, afirma que [dar ao modelo uma forma de verificar o próprio trabalho](https://x.com/bcherny/status/2007179861115511237) multiplica por dois ou três a qualidade do resultado final, e que essa é provavelmente a coisa mais importante a fazer. O que conta como verificação muda com o domínio: rodar um comando, executar uma suíte de testes, abrir a interface e conferir o resultado. A Anthropic descreve três famílias no Agent SDK: realimentação por regras, que é a mais forte porque diz qual regra falhou e por quê; realimentação visual; e um segundo modelo como avaliador, útil para critérios difusos e sujeito às limitações que o Módulo 6 detalha.

Daí sai o critério para subir a escada, e ele é restritivo de propósito. **Só é candidata ao nível 2 uma tarefa cujo critério de sucesso seja inteiramente objetivo**: testes que passam, compilação que conclui, análise estática que zera, indicador que atinge um limiar. Sem esse critério, um laço desassistido queima orçamento sem nunca poder terminar. E o pior desfecho é o falso positivo: o sistema declara conclusão e ninguém confere.

Existe uma consequência prática agradável para quem já pratica desenvolvimento guiado por testes. Testes escritos antes da implementação não são só verificação: são a condição de parada de um laço de nível 2. Quem já os escreve primeiro tem o pré-requisito pronto. A mesma observação vale para o fluxo guiado por especificação da segunda metade deste módulo, e é por isso que ele aparece aqui: um processo com constitution, spec, plano, tarefas e portões é, em vocabulário de arnês, o arnês de um agente que escreve software. A operação desses laços fora da sessão de trabalho, com orçamento, isolamento, interrupção e trilha, é assunto do [Módulo 7](../sobre/plano-da-disciplina.md#modulo-7).

## Escolher o nível de loop e a condição de parada

A [escada de quatro níveis](loops.md#quatro-niveis-de-loop) é uma decisão arquitetural, não uma preferência de fluxo de trabalho. Cada degrau transfere uma responsabilidade da pessoa para o sistema, e cada transferência exige um controle correspondente no arnês antes de ser feita. A tabela abaixo é o critério de subida.

| Nível | Pré-requisito inegociável | Controle que precisa existir antes | Evidência exigida |
|---|---|---|---|
| 1 — por rodada | nenhum além dos contratos de ferramenta | catálogo mínimo e validação de saída | trace da rodada com decisão de política |
| 2 — por objetivo | critério de sucesso inteiramente objetivo e versionado | teto de iterações e orçamento de custo, com comportamento definido ao esgotar | condição de parada declarada antes da execução, e qual delas encerrou |
| 3 — por tempo | idempotência sob execução repetida e ausência de pessoa no momento do disparo | identidade própria do gatilho, escopo reduzido e desligamento acessível | registro de cada disparo, inclusive dos que não produziram efeito |
| 4 — proativo | classificação prévia do que o sistema pode iniciar sem provocação | catálogo de eventos autorizados e limite por janela | trilha ligando evento, decisão de iniciar e efeito |

Três regras atravessam a tabela.

**A condição de parada é artefato versionado, não parâmetro de execução.** Ela pertence ao mesmo pacote que prompt, política e contrato de ferramenta. Mudar a condição de parada muda o comportamento do sistema tanto quanto trocar o modelo, e deve seguir o mesmo caminho de revisão.

**O orçamento é o mecanismo de segurança primário, não a condição de parada.** A documentação do plugin oficial de laço da Anthropic diz isso de forma direta: a frase de conclusão é comparada por igualdade exata e não distingue sucesso de bloqueio, portanto o limite de iterações é a rede. Um laço sem teto de iterações e sem teto de custo é um incidente esperando data. Prefira dois tetos independentes, porque iterações baratas e iterações caras não são intercambiáveis.

**Esgotar o orçamento é um desfecho legítimo e precisa de tratamento definido.** Ao atingir o teto sem sucesso, o sistema deve registrar o que tentou, o que bloqueou o progresso e qual é o estado atual, e encaminhar para uma pessoa. O que não pode acontecer é o laço encerrar em silêncio deixando um artefato parcial que parece pronto.

Existe um teste rápido para decidir se uma tarefa é candidata a laço, e ele se aplica antes de qualquer discussão de ferramenta: se ninguém consegue escrever, em uma frase, o comando que decide se o trabalho terminou, a tarefa está no nível 1 e permanece nele. Reformular a tarefa até que esse comando exista é trabalho de arquitetura, não preparação para a automação.

### Quando não usar laço

Recusar autonomia iterativa é uma decisão tão registrável quanto concedê-la. Não use laço quando o critério de sucesso depende de julgamento humano ou de negociação; quando a operação é de uma vez só e não se beneficia de refinamento; quando o efeito é irreversível e não existe compensação proporcional; quando a falha só aparece em produção e o diagnóstico exige contexto que o agente não tem. Nesses casos, a resposta arquitetural é a mesma da [matriz de autonomia](autonomia-orcada.md#matriz-de-autonomia): copiloto com aprovação explícita, não laço desassistido.

### Fitness functions de um laço

- toda execução do laço registra a condição de parada declarada, a que efetivamente encerrou e o consumo acumulado;
- nenhum laço em ambiente com efeito real roda sem teto de iterações e teto de custo, ambos com dono;
- uma parada por esgotamento de orçamento gera registro com o motivo do bloqueio e destinatário humano;
- duas iterações consecutivas com o mesmo resultado de verificação acionam diversificação ou interrupção, não repetição;
- a condição de parada tem versão e revisão, e uma mudança nela invalida a evidência de execuções anteriores.
