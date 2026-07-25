# Estudo de caso: atendimento interno com conhecimento e ação limitada

O caso aplica o vocabulário do módulo sem pressupor RAG, agente ou plataforma. O objetivo é decidir que hipóteses merecem o desenho conceitual do Módulo 2.

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

## Trabalho de arquitetura solicitado

Produza uma leitura de uma a duas páginas com:

1. situação, resultado esperado e responsabilidades de geração, decisão, autorização e efeito;
2. alternativas para produção, conhecimento, efeito e operação;
3. separação entre conhecimento, contexto, estado, memória, evidência e trace;
4. duas características em tensão e um cenário mensurável;
5. três riscos e contenções, incluindo acesso indevido e efeito repetido;
6. classificação de evidências em teste de software, avaliação comportamental e verificação arquitetural;
7. uma fitness function candidata;
8. ficha de decisão inicial com incógnita decisiva e experimento;
9. recomendação: avançar, restringir, experimentar ou rejeitar.

Uma recomendação sólida pode começar sem ação, comparar busca e contexto com recuperação num corpus piloto e deixar ferramenta para outro incremento. Também pode rejeitar geração em tarefas cuja resposta deriva de regra estável.

## Pistas para discussão

- O problema é localizar evidência, explicar conteúdo, produzir efeito ou uma combinação?
- Que atividade não deveria usar modelo?
- Qual dado tem finalidade para contexto, mas não para trace ou memória?
- Que mudança de configuração exigiria nova avaliação?
- Que resultado faria abandonar a alternativa preferida?

O caso prepara o [Módulo 2](../modulo-2-desenho-conceitual/index.md): transformar essas perguntas em RAS, vistas, táticas, riscos, evidências e decisões.

Agora consolide o vocabulário nos [exercícios](exercicios.md).
