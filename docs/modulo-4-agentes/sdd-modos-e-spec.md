# Modos de trabalho e a spec viva

Vibe coding, assistência de codificação e desenvolvimento guiado por especificação diferem pelo artefato que governa a mudança, não pelo grau de uso do modelo.

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

SDD muda a relação entre os artefatos. Em vez de tratar a especificação como andaime abandonado quando o código começa, trata-a como expressão versionada da intenção. O código é uma implementação possível daquela intenção, condicionada por arquitetura, plataforma e momento. Essa inversão não significa que prosa esteja sempre certa ou que código possa ser regenerado sem custo. Significa que uma mudança relevante deve começar por tornar explícito **o que mudou na intenção**, e que plano, testes e implementação precisam mostrar sua relação com essa mudança.

> **Decisão arquitetural:** use SDD quando a tarefa contém decisões, riscos ou coordenação suficientes para justificar um contrato durável. Para um experimento descartável, registre a pergunta e o resultado; não simule uma burocracia completa.

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

## Constitution: princípios antes da feature

O [Spec Kit](https://github.com/github/spec-kit) começa pela **constitution**, um conjunto versionado de princípios que todas as features devem respeitar. Ela reduz a necessidade de repetir decisões organizacionais em cada prompt e impede que o agente trate convenções fundamentais como preferências locais.

Uma constitution útil contém regras capazes de bloquear ou redirecionar um plano:

- interfaces públicas exigem compatibilidade ou estratégia de migração;
- toda escrita material precisa de autorização no servidor;
- comportamento novo começa por um teste que falha pelo motivo esperado;
- dependências adicionais exigem justificativa;
- dados pessoais não entram em logs;
- módulos expõem interfaces pequenas e testáveis;
- documentação e ADRs mudam junto com o contrato que descrevem;
- a esteira deve permanecer verde a cada fatia integrável.

Princípios vagos — “escreva código limpo”, “priorize segurança”, “use boas práticas” — não governam. Eles não definem o que o agente deve fazer diante de um trade-off. Uma constitution precisa declarar consequências: se um requisito viola um princípio, o plano registra a exceção e pede decisão humana; não prossegue silenciosamente.

A constitution também não deve congelar o projeto. Mudá-la é possível, mas exige uma decisão de alcance maior que uma feature. A alteração pode tornar specs e implementações anteriores não conformes; por isso tem versão, justificativa, impacto e plano de adoção. Em termos arquiteturais, ela opera como política do sistema de desenvolvimento.
