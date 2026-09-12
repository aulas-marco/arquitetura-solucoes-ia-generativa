# Vibe coding, assistência e SDD

*Vibe coding*, assistência de codificação e desenvolvimento guiado por especificação diferem pelo artefato que governa a mudança, e não pelo quanto cada um usa o modelo.

Esta é a primeira página do módulo depois da abertura. Ela pressupõe o [vocabulário mínimo](index.md#vocabulario-minimo) e nada além do Módulo 4: um agente com ferramentas, contratos e portões de autorização.

## Do agente que age ao agente que constrói software

O agente que constrói software é um caso especialmente instrutivo de autonomia. Suas ferramentas — ler arquivos, editar código, executar comandos, criar branches e propor commits — produzem efeitos duráveis. Uma alteração pode compilar e ainda violar uma regra de negócio, enfraquecer segurança, introduzir acoplamento ou resolver um problema diferente daquele que motivou o trabalho. Portanto, a pergunta arquitetural permanece a mesma: **qual liberdade o modelo recebe, qual contrato orienta suas escolhas e que evidência autoriza o próximo passo?**

O uso de IA no desenvolvimento não começa com geração de código. Começa com a transformação de uma intenção incompleta em um conjunto de decisões verificáveis. É nesse ponto que o **desenvolvimento guiado por especificação**, ou SDD (*Specification-Driven Development*), se conecta ao tema do módulo: a especificação funciona como estado autoritativo do objetivo, enquanto agentes especializados ajudam a descobrir, formalizar, planejar, implementar e revisar.

## Vibe coding, assistência e SDD

Três modos de trabalho costumam ser confundidos:

| Modo | Artefato que governa | Como a qualidade é julgada | Risco dominante |
|---|---|---|---|
| *Vibe coding* | conversa corrente e resultado aparente | “parece funcionar” | intenção implícita, regressão e dívida invisível |
| assistência de codificação | ticket, código existente e revisão do desenvolvedor | testes e revisão após gerar | contexto fragmentado e decisões não registradas |
| SDD | constitution, spec, plano, tarefas, testes e gates versionados | rastreabilidade entre intenção, implementação e evidência | custo de especificar sem aprender ou manter artefatos vivos |

*Vibe coding* é útil para exploração descartável: provar uma interação, experimentar uma API ou descobrir uma pergunta de design. Ele se torna perigoso quando o protótipo atravessa silenciosamente a fronteira para produto. A conversa contém decisões que não aparecem no repositório; o código incorpora suposições que ninguém aprovou; o teste confirma apenas o que foi implementado; e uma nova sessão não possui o contexto que orientou a anterior.

Assistência de codificação é mais disciplinada. A pessoa mantém o desenho e usa o modelo para completar funções, explicar código, gerar testes ou revisar um diff. Isso pode produzir excelente engenharia, mas não constitui SDD por si: a especificação ainda pode ser um ticket curto e descartável, sem critérios suficientes para orientar mais de um agente ou reconstruir por que o sistema ficou daquela forma.

### A definição estrita importa

Andrej Karpathy cunhou a expressão *vibe coding* em fevereiro de 2025 para descrever uma forma de programar em que a pessoa “se entrega às sensações” e quase esquece que o código existe. O ciclo é essencialmente conversacional: pedir, executar, observar, copiar erros de volta para o modelo e aceitar mudanças sem necessariamente inspecionar sua implementação. O próprio exemplo de Karpathy tratava de projetos de fim de semana e reconhecia o caráter descartável do resultado (Karpathy, 2025).

Usar IA para programar não é, por si só, vibe coding. Um engenheiro pode delegar a escrita de código a um agente e ainda assim revisar o diff, exigir testes, verificar propriedades de segurança e manter registro das decisões. Simon Willison propõe reservar o termo para software construído com um modelo de linguagem sem revisão do código gerado, um uso deliberadamente distinto da programação profissional assistida por IA (Willison, 2025).

A diferença entre os três modos, portanto, não está em quanto código a IA escreve. Está em onde a intenção é registrada, quem responde pela validação e qual evidência autoriza a mudança a avançar.

Nenhum dos modos é moralmente superior. O anti-padrão é mudar silenciosamente a classe do ativo: um protótipo passa a atender usuários, acumula dados e recebe integrações, mas continua sendo mantido como se ainda fosse descartável. Quando isso acontece, a dívida não é apenas de código. É uma **dívida de intenção**, um sistema que contém decisões que ninguém consegue distinguir de acidentes de implementação.

SDD muda a relação entre os artefatos. Em vez de tratar a especificação como andaime abandonado quando o código começa, trata-a como expressão versionada da intenção. O código é uma implementação possível daquela intenção, condicionada por arquitetura, plataforma e momento. Essa inversão não significa que prosa esteja sempre certa ou que código possa ser regenerado sem custo. Significa que uma mudança relevante deve começar por tornar explícito **o que mudou na intenção**, e que plano, testes e implementação precisam mostrar sua relação com essa mudança.

> **Decisão arquitetural:** use SDD quando a tarefa contém decisões, riscos ou coordenação suficientes para justificar um contrato durável. Para um experimento descartável, registre a pergunta e o resultado; não simule uma burocracia completa.

## Por que escalar agentes desloca o gargalo

Agentes reduzem o custo marginal de produzir uma primeira versão de código. Esse ganho é real, mas não significa que o sistema de entrega inteiro se tornou mais rápido. Requisitos, revisão, integração, testes, segurança, implantação e operação continuam formando uma cadeia. Aumentar a vazão de uma etapa pode apenas deslocar o gargalo para a etapa seguinte.

Ao apresentar o SPDD, o time de tecnologia interna da Thoughtworks descreve quatro fricções recorrentes:

- requisitos ambíguos viram código mais depressa
- revisores recebem maior volume de mudança
- inconsistências aparecem na integração e nos testes
- o risco de produção fica mais difícil de avaliar quando o volume cresce

A metáfora usada pelos autores é a de colocar o motor de uma Ferrari numa estrada ruim. A potência local não determina o horário de chegada (Zhang & Xia, 2026).

Esse deslocamento acontece por mecanismos concretos:

- **Amplificação da ambiguidade.** Um requisito incompleto não bloqueia o agente. Ele preenche lacunas com suposições plausíveis, e plausibilidade não é equivalência com a regra de negócio.
- **Assimetria entre geração e revisão.** Produzir cem linhas pode levar segundos. Compreender suas implicações, dependências e casos de falha continua exigindo atenção humana e execução de verificações.
- **Perda de contexto entre etapas.** A intenção discutida no chat não acompanha necessariamente o pull request, o teste, o incidente ou a manutenção futura.
- **Convergência local e incoerência global.** Cada alteração pode parecer razoável isoladamente e, ainda assim, introduzir múltiplas formas de resolver o mesmo problema, violar uma decisão arquitetural ou duplicar uma regra.
- **Automação da confiança indevida.** Um relatório gerado pelo mesmo agente que produziu a mudança pode confirmar a coerência interna de uma premissa errada. Revisar código contra uma especificação ajuda apenas se alguém também revisar a especificação contra a necessidade real.

O objetivo de uma abordagem estruturada não é tornar o modelo infalível. É transformar parte dessa incerteza em pontos de decisão observáveis: o que precisa ser esclarecido, quem aprova, o que será testado e quais divergências impedem a conclusão.

## Máquinas probabilísticas pedem procedimentos reproduzíveis

Modelos de linguagem produzem saídas condicionadas ao prompt, ao contexto, à versão do modelo, às ferramentas disponíveis e aos parâmetros de execução. Mesmo quando a configuração reduz a aleatoriedade, não há garantia geral de que a mesma solicitação produzirá uma implementação idêntica em outro momento ou ambiente.

Isso não significa que software gerado por IA seja inevitavelmente instável. Significa que a reprodutibilidade precisa vir menos da expectativa de repetir exatamente a geração e mais da capacidade de repetir o **procedimento de validação**.

Um procedimento robusto preserva cinco coisas:

1. a intenção que motivou a mudança.
2. os limites explícitos do que não deve ser alterado.
3. as decisões técnicas e os trade-offs aceitos.
4. os critérios observáveis que distinguem sucesso de falha.
5. as evidências que demonstram que a implementação atual satisfaz esses critérios.

Uma boa especificação, portanto, não é a mais longa. É a que reduz interpretações relevantes e permite contestação. “Adicionar segurança ao login” é uma intenção. Já “bloquear novas autenticações por quinze minutos após cinco falhas associadas à conta, sem bloquear o fluxo de recuperação de senha” contém comportamento verificável. Ainda faltam decisões (concorrência, distribuição, privacidade, desbloqueio e ataques de negação de serviço), mas agora é possível enxergar as lacunas. Esse mesmo caso é percorrido pelas quatro abordagens no [fluxo SDD](fluxo.md#quatro-abordagens-para-o-mesmo-padrao).

## A spec como artefato central e vivo

Uma boa spec não é uma descrição longa. É uma fronteira de decisão. Ela deve permitir que pessoas diferentes respondam, sem ler a mente do autor:

- qual problema vale resolver e para quem;
- qual comportamento observável caracteriza sucesso;
- o que está explicitamente fora do escopo;
- quais termos têm significado específico no domínio;
- quais regras não podem ser violadas;
- quais atributos de qualidade alteram a solução;
- quais incertezas permanecem abertas;
- qual evidência permitirá aceitar ou rejeitar a entrega.

“Adicionar exportação” não é uma spec. Ainda faltam ator, finalidade, formato, volume, autorização, tratamento de dados sensíveis, tempo aceitável, falhas e resultado observável. “Construir exportação CSV para gestores baixarem até 50 mil registros autorizados em menos de 30 segundos, sem expor colunas restritas” começa a formar uma especificação porque restringe interpretações e permite derivar decisões e testes.

A spec é **viva** quando uma descoberta altera o artefato apropriado. Se o domínio revela que relatórios fechados não podem ser regenerados, a regra entra na spec. Se o banco escolhido não sustenta o volume, a decisão e suas consequências entram no plano ou ADR; isso não deve ser escondido como detalhe do código. Se um incidente mostra que o controle de autorização falhou, a correção não termina no patch: requisito, cenário adversarial e teste de regressão passam a governar trabalhos futuros.

Ela é **executável em sentido amplo** quando consegue produzir ou verificar outros artefatos: cenários tornam-se testes; entidades orientam modelo de dados; contratos orientam APIs; atributos de qualidade geram experimentos; regras de segurança produzem casos negativos; tarefas carregam critérios de conclusão. Executável não quer dizer que toda prosa se transforme mecanicamente em código nem que o modelo seja um compilador infalível. A transformação continua sujeita a interpretação, ferramentas e revisão.

<a id="constitution-principios-antes-da-feature"></a>

## Constituição (*constitution*): princípios antes da funcionalidade

O [Spec Kit](https://github.com/github/spec-kit) começa pela **constituição** — em inglês *constitution*, e é assim que o comando aparece na ferramenta. É um arquivo versionado no repositório, geralmente `constitution.md`, com os princípios que toda mudança precisa respeitar. Ela existe para que decisões que valem para o projeto inteiro não precisem ser repetidas em cada pedido ao agente, e para impedir que ele trate convenção fundamental como preferência local.

A comparação que ajuda: a especificação diz o que **esta** mudança deve fazer; a constituição diz o que **nenhuma** mudança pode violar. Uma vale por uma funcionalidade, a outra vale até ser explicitamente alterada.

Uma constituição útil contém regras capazes de bloquear ou redirecionar um plano:

- interfaces públicas exigem compatibilidade ou estratégia de migração;
- toda escrita material precisa de autorização no servidor;
- comportamento novo começa por um teste que falha pelo motivo esperado;
- dependências adicionais exigem justificativa;
- dados pessoais não entram em logs;
- módulos expõem interfaces pequenas e testáveis;
- documentação e ADRs mudam junto com o contrato que descrevem;
- a esteira deve permanecer verde a cada fatia integrável.

### Um exemplo completo

Uma constituição de verdade cabe em uma página. Esta é a de um serviço de pedidos fictício, com cinco princípios e a consequência de cada um:

```markdown
# Constituição — serviço de pedidos Boreal
Versão 1.2 · alterada em 12/03/2026 · dono: arquitetura

1. Toda transição de estado de pedido é explícita e testada.
   Consequência: mudança que introduz estado novo sem teste de transição é
   bloqueada no portão de entrega.

2. Comportamento novo começa por um teste que falha pelo motivo esperado.
   Consequência: pull request cujo primeiro commit já contém implementação
   é devolvido, mesmo que os testes passem no final.

3. Nenhum dado pessoal entra em log, mensagem de erro ou telemetria.
   Consequência: o revisor de segurança pode barrar a entrega sozinho,
   sem discussão de prioridade.

4. Dependência nova exige justificativa escrita e um responsável nomeado.
   Consequência: sem as duas coisas, o plano não passa do portão de
   arquitetura.

5. Interface pública só muda com compatibilidade ou plano de migração.
   Consequência: quebrar contrato sem plano é exceção que exige decisão
   do dono do produto, registrada na própria especificação.
```

Repare no que cada linha faz. O princípio nomeia a regra; a consequência nomeia **quem barra o quê**. Sem a segunda metade, o agente lê a regra como conselho.

Princípios vagos não governam. “Escreva código limpo”, “priorize segurança” e “use boas práticas” não dizem o que fazer diante de um conflito, e por isso nunca rejeitam nada. O teste é direto: se você não consegue imaginar uma mudança plausível que o princípio barraria, ele é decoração. Quando um requisito viola um princípio, o plano registra a exceção e pede decisão humana em vez de seguir em silêncio.

A constituição também não deve congelar o projeto. Mudá-la é possível, mas exige uma decisão de alcance maior que uma feature. A alteração pode tornar specs e implementações anteriores não conformes; por isso tem versão, justificativa, impacto e plano de adoção. Em termos arquiteturais, ela opera como política do sistema de desenvolvimento.

## O que “SDD” pode significar

*Spec-Driven Development* ainda não designa uma prática única e estabilizada. A expressão reúne fluxos com diferentes níveis de compromisso entre especificação e código. A taxonomia proposta por Birgitta Böckeler ajuda a evitar que ferramentas distintas pareçam equivalentes apenas porque todas produzem arquivos Markdown (Böckeler, 2025):

1. **Spec-first.** A especificação melhora a primeira geração, mas pode ser arquivada ou abandonada depois. O código volta a ser a fonte operacional de verdade.
2. **Spec-anchored.** Especificação e código evoluem juntos. Cada mudança parte do estado documentado e deve reconciliar os dois lados antes de terminar.
3. **Spec-as-source.** A especificação é o artefato primário editável, e o código é uma projeção regenerável dela. Essa é a forma mais ambiciosa, e também a mais difícil, porque a especificação teria de expressar detalhe suficiente para reproduzir o comportamento sem depender de decisões escondidas no código.

Este módulo opera entre *spec-first* e *spec-anchored*. As quatro abordagens comparadas no [fluxo SDD](fluxo.md#quatro-abordagens-para-o-mesmo-padrao) se distribuem nessa mesma faixa.

A taxonomia leva a uma distinção que evita confundir instalação com adoção:

- **método** é o conjunto de decisões sobre como o trabalho deve avançar.
- **artefato** é o registro durável de intenção, design, tarefas ou evidências.
- **ferramenta** instala comandos, modelos e automações que ajudam o agente a seguir o método.
- **governança** define quem aprova, quais portões são obrigatórios e o que acontece quando um portão falha.

Instalar uma ferramenta não cria governança automaticamente. Um agente pode preencher todos os modelos e ainda produzir uma especificação vaga. Da mesma forma, um time pode praticar SDD com arquivos simples, desde que trate a especificação como um contrato revisável e mantenha a disciplina de atualizá-la.

## Cinco perguntas para escolher o modo de trabalho

A escolha deve ser feita por mudança, não por preferência pessoal nem por um mandato uniforme para toda a organização. Cinco perguntas oferecem uma primeira triagem, e antecipam a classificação S/M/L da [Decisão 1](decisoes.md#decisao-1-escolher-a-profundidade-proporcional):

1. **Reversibilidade.** Se a decisão estiver errada, é possível descartar o resultado sem migração de dados, indisponibilidade, quebra de contrato ou retrabalho amplo?
2. **Tempo de vida esperado.** O código será usado por horas, por um ciclo de campanha ou por vários anos?
3. **Número de futuros mantenedores.** A conversa original estará acessível e compreensível para todas as pessoas que precisarão alterar o sistema?
4. **Criticidade da regra de negócio.** O comportamento envolve dinheiro, identidade, autorização, privacidade, segurança, obrigações regulatórias ou exceções difíceis de reconstruir?
5. **Familiaridade com o sistema existente.** A mudança ocorre num projeto novo ou num sistema maduro, com dependências, convenções e restrições que não estão todas documentadas?

As perguntas ficam mais úteis quando se traduzem em consequências operacionais:

| Sinal observado | O que precisa aumentar no processo |
|---|---|
| mudança difícil de reverter | revisão prévia da solução, estratégia de migração e plano de rollback |
| vida útil longa | registro durável das decisões e mecanismo de atualização da especificação |
| muitos times consumidores | contratos explícitos, compatibilidade, responsáveis e comunicação de mudança |
| regra crítica | critérios de aceitação verificáveis, cenários de borda e evidência de teste |
| código legado ou pouco conhecido | exploração do repositório, análise de impacto e validação por alguém com conhecimento do domínio |

Uma resposta “alta” não obriga a adotar a ferramenta mais pesada. Ela obriga a cobrir o risco correspondente. Uma alteração irreversível em um serviço pequeno pode pedir um plano de migração rigoroso, mas não necessariamente uma constitution de projeto. Uma mudança trivial em um sistema regulado pode reutilizar salvaguardas já codificadas e seguir um caminho abreviado.

Por isso, “peso do processo” não deve ser medido pelo número de arquivos ou comandos. O custo relevante é a soma de três esforços: produzir o artefato, revisá-lo com atenção e mantê-lo coerente com o sistema. Se o time gera documentos que ninguém usa para decidir, o processo adiciona custo sem reduzir risco.
