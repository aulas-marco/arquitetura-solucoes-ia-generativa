# Estudo de caso: atendimento interno com conhecimento e ação limitada

O caso aplica o vocabulário do módulo sem pressupor RAG, agente ou plataforma. O objetivo é decidir que hipóteses merecem o desenho conceitual do Módulo 2.

## Como usar este estudo de caso

Leia a situação, os stakeholders, as restrições e as evidências iniciais uma única vez, de forma contínua — sem tentar resolver nada ainda. Depois, resolva os [exercícios guiados](#exercicios-guiados) na ordem em que aparecem: cada um indica exatamente qual seção de [Conceitos](conceitos.md) ou [Padrões e decisões](padroes-e-decisoes.md) consultar antes de responder, e usa o que você produziu no exercício anterior. Se travar num exercício, releia só a seção indicada — o objetivo não é lembrar o módulo inteiro de cor, mas praticar a consulta ao vocabulário certo no momento certo. O último exercício pede a leitura de uma a duas páginas que reúne tudo; os anteriores existem para que ela não precise ser escrita do zero.

## Situação

A empresa Horizonte possui políticas de pessoas, compras e viagens. Analistas gastam tempo localizando a versão vigente, explicando texto normativo e, em alguns casos, abrindo chamado para o dono da política. A liderança pede “um agente que responda e resolva tudo”.

### Stakeholders

- analistas querem reduzir busca e transcrição;
- pessoas colaboradoras querem orientação compreensível e contestável;
- donos das políticas respondem por vigência e conflitos;
- Segurança e Privacidade exigem isolamento e finalidade;
- Operações precisa implantar, observar e recuperar com equipe pequena;
- Auditoria precisa reconstruir fontes, versões, aprovações e efeitos.

## Restrições conhecidas

O acervo contém 420 documentos e 11 mil páginas. Trinta documentos são restritos à liderança; 65 possuem anexos com dados pessoais que não podem virar conhecimento do assistente. Trinta e cinco documentos mudam por mês; doze não têm dono confirmado.

O piloto terá 150 usuários, equipe de três pessoas e oito semanas. Pode orientar, resumir e propor abertura de chamado. Não pode decidir direito, alterar cadastro, aprovar pagamento ou enviar comunicação externa. Chamado só é criado depois de confirmação do analista e por API idempotente.

O p95 desejado é oito segundos para orientação sem ação. Pergunta sensível sem evidência suficiente deve ser encaminhada. Logs não podem conservar documento completo nem texto pessoal sem finalidade aprovada.

## Evidências iniciais

| Observação | Resultado |
|---|---:|
| perguntas respondidas por analistas com acesso | 27/30 |
| respostas aceitáveis sem documentos corporativos | 9/30 |
| respostas aceitáveis com três documentos escolhidos manualmente | 24/30 |
| perguntas dependentes de versão vigente | 11/30 |
| fontes parcialmente contraditórias | 4/30 |
| chamados abertos por falta de dono ou conflito | 6/30 |

A amostra não demonstra a solução. Seleção manual favorece contexto fornecido; ainda faltam perguntas sem resposta, perfis distintos, falhas de dependência, custo, latência e carga de revisão.

## Quatro decisões a separar

### 1. Produção

Regras e templates atendem respostas estáveis. Geração pode reformular políticas e preparar rascunhos. A equipe precisa comparar utilidade, erro material e esforço de revisão.

### 2. Conhecimento

Busca convencional, contexto selecionado e recuperação são alternativas. O problema central é localizar versão autorizada e preservar evidência; embeddings são apenas um mecanismo possível.

### 3. Efeito

O primeiro incremento pode não ter ferramenta. Se abrir chamado agregar valor, o modelo produz proposta estruturada; aplicação valida contrato e política; analista confirma; executor idempotente cria o registro.

### 4. Operação e confiança

Hospedagem, retenção, trace, fallback e mudança de modelo permanecem decisões próprias. Um controle não prova o sistema inteiro. O piloto precisa de critérios de bloqueio para vazamento e de metas para utilidade, latência e custo.

## Exercícios guiados

Cada exercício tem um objetivo específico, indica o que consultar antes de responder e pede um resultado curto — uma tabela, uma lista ou poucas frases. Guarde as respostas: o Exercício 9 pede que você as reúna numa única leitura.

### Exercício 1 — Situação e quatro responsabilidades

**Consulte:** [Geração, decisão, autorização e efeito](conceitos.md#geracao-decisao-autorizacao-e-efeito).

**Tarefa:** em três a cinco frases, descreva a situação da Horizonte e o resultado que o piloto deveria produzir. Depois, monte uma tabela de quatro linhas — Geração, Decisão, Autorização, Efeito — preenchendo, para cada responsabilidade, quem ou o que a exerce hoje na Horizonte (mesmo que ainda de forma manual).

### Exercício 2 — Quatro decisões e alternativas

**Consulte:** [Quatro decisões a separar](#quatro-decisoes-a-separar) (nesta página) e [Panorama das abordagens](padroes-e-decisoes.md#panorama-das-abordagens).

**Tarefa:** para cada uma das quatro decisões — produção, conhecimento, efeito, operação —, escolha uma alternativa candidata do panorama de abordagens e escreva uma frase justificando por que ela é uma candidata plausível para o primeiro incremento, sem ainda decidir a composição final. Não escolha a mesma abordagem para as quatro linhas: o objetivo é perceber que são decisões independentes.

### Exercício 3 — O que atravessa o sistema

**Consulte:** [Que informação atravessa o sistema](conceitos.md#que-informacao-atravessa-o-sistema), especialmente a tabela de [artefatos com ciclos de vida diferentes](conceitos.md#artefatos-com-ciclos-de-vida-diferentes).

**Tarefa:** olhando a situação da Horizonte, dê um exemplo concreto de cada artefato — conhecimento, contexto, estado, memória, evidência, trace — usando dados do próprio caso (por exemplo: qual documento é conhecimento? o que vira contexto numa pergunta específica? o que não deveria virar memória?).

### Exercício 4 — Duas características em tensão

**Consulte:** [Atributos de qualidade, trade-offs e significância](conceitos.md#atributos-de-qualidade-trade-offs-e-significancia) e o [catálogo de atributos de qualidade](../referencia/atributos-de-qualidade.md).

**Tarefa:** escolha duas características do catálogo que competem entre si nesta situação (por exemplo, duas entre Privacidade, Fundamentação, Latência e Custo). Escreva um cenário mensurável para uma delas, no formato Fonte/Estímulo/Ambiente/Artefato/Resposta/Medida usado no catálogo.

### Exercício 5 — Três riscos e contenções

**Consulte:** [Anti-padrão: uma caixa probabilística para tudo](padroes-e-decisoes.md#anti-padrao-uma-caixa-probabilistica-para-tudo).

**Tarefa:** liste três riscos concretos da situação da Horizonte — pelo menos um de acesso indevido a documento restrito e um de efeito repetido (chamado duplicado) — e, para cada um, uma frase descrevendo a contenção (o que impede ou limita o dano).

### Exercício 6 — Classifique a evidência

**Consulte:** [Três tipos de verificação](conceitos.md#tres-tipos-de-verificacao).

**Tarefa:** releia a tabela de [Evidências iniciais](#evidencias-iniciais) (nesta página) e classifique cada linha da tabela como teste de software, avaliação comportamental ou verificação arquitetural — ou explique por que a amostra atual não permite classificar aquela linha em nenhum dos três.

### Exercício 7 — Uma fitness function candidata

**Consulte:** a definição de *fitness function* na mesma seção do Exercício 6, [Três tipos de verificação](conceitos.md#tres-tipos-de-verificacao).

**Tarefa:** escreva uma fitness function candidata para o piloto da Horizonte — uma frase no formato "se [condição observável], então [ação automática antes da promoção]".

### Exercício 8 — Ficha de decisão inicial

**Consulte:** [Ficha de decisão inicial](padroes-e-decisoes.md#ficha-de-decisao-inicial) — preencha os mesmos oito campos do exemplo resumido ali, mas para a Horizonte.

**Tarefa:** preencha a ficha completa (Situação, Responsabilidades, Características prioritárias, Alternativas, Consequências, Evidência existente, Incógnita decisiva, Próximo experimento) usando os dados e restrições descritos nesta página.

### Exercício 9 — Síntese: a leitura de uma a duas páginas

**Consulte:** suas respostas dos Exercícios 1 a 8.

**Tarefa:** reúna os oito exercícios numa única leitura corrida de uma a duas páginas, terminando com uma recomendação explícita: avançar, restringir, experimentar ou rejeitar. Uma recomendação sólida pode começar sem ação, comparar busca e contexto com recuperação num corpus piloto e deixar ferramenta para outro incremento; também pode rejeitar geração em tarefas cuja resposta já deriva de regra estável.

## Perguntas para ir além

Depois de concluir os nove exercícios, se quiser aprofundar antes de seguir para o Módulo 2:

- O problema é localizar evidência, explicar conteúdo, produzir efeito ou uma combinação?
- Que atividade não deveria usar modelo?
- Qual dado tem finalidade para contexto, mas não para trace ou memória?
- Que mudança de configuração exigiria nova avaliação?
- Que resultado faria abandonar a alternativa preferida?

O caso prepara o [Módulo 2](../modulo-2-desenho-conceitual/index.md): transformar essas perguntas em RAS, vistas, táticas, riscos, evidências e decisões.

Agora consolide o vocabulário nos [exercícios](exercicios.md).
