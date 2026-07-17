# Estudo de caso: liberar ou não o assistente de RH

## A proposta

Uma organização com 12 mil empregados quer reduzir dúvidas repetitivas sobre férias, benefícios e trabalho híbrido. A primeira proposta conecta um modelo a todo o portal de RH e ao sistema de pessoas, armazena conversas por dois anos “para melhoria” e permite que o assistente abra solicitações. A demonstração responde bem a dez perguntas preparadas. A direção pede lançamento em quatro semanas.

A equipe de arquitetura interrompe a discussão sobre fornecedor e reformula o caso de uso. A primeira versão explicará políticas, consultará o saldo do próprio usuário e criará um rascunho de encaminhamento. Não fará escrita no sistema de pessoas. O público inicial será um grupo voluntário de duas unidades. Haverá **conteúdo público**, **conteúdo restrito** a gestores e **dados pessoais** acessíveis apenas ao titular e a profissionais autorizados. Saúde, assédio, discriminação, medida disciplinar, conflito normativo ou contestação de elegibilidade exigem **escalonamento obrigatório**.

Essa redução não torna o produto seguro; torna ativos, efeitos e evidências mais delimitáveis. A demonstração vira apenas uma observação inicial, incapaz de representar ataques, variação de políticas, permissões ou uso real.

## Decisões de risco e governança

O registro de riscos destaca quatro cenários. Primeiro, um documento restrito pode aparecer para empregado comum por metadado errado. O controle é classificação na origem, filtro de autorização antes da recuperação e teste negativo por perfil. Segundo, um documento pode conter injeção indireta. O controle combina revisão de ingestão, tratamento como dado e executor sem escrita; o risco residual permanece porque o modelo ainda interpreta texto adversarial. Terceiro, uma conversa sobre saúde pode entrar em log amplo. O controle minimiza trace, mascara campos e retém conteúdo completo apenas em amostra autorizada por prazo curto. Quarto, um avaliador automático pode aprovar resposta discriminatória ou inútil. O controle é aplicação de critérios humanos calibrados, análise por fatias e canal de contestação.

Responsabilidades ficam nomeadas. RH é proprietário da finalidade, das políticas, das categorias de escalonamento e da aceitação de risco residual. Segurança lidera o modelo de ameaças; privacidade define classes, acesso e retenção; a plataforma mantém identidade, gateway e versões; produto mede experiência; operação responde a alertas; jurídico interpreta obrigações aplicáveis; autores respondem pela vigência do conteúdo. O fornecedor responde ao contrato e ao serviço contratado, não à decisão trabalhista da organização.

O catálogo registra caso e dependências. Mudança de modelo, prompt, política, corpus, ferramenta, avaliador ou público dispara regressão. Conversas completas ficam fora da memória persistente. O trace conserva identificadores, versões, fontes, decisões, métricas e categoria de escalonamento, não texto integral por conveniência.

## Quadro multidimensional de qualidade

A equipe rejeita “acurácia de 90%” como requisito único. Define as dimensões para a tarefa:

| Dimensão | Pergunta de avaliação | Evidência e exemplo de critério |
|---|---|---|
| **factualidade** | as afirmações correspondem à política vigente e ao dado autoritativo? | revisão de afirmações factuais; erro material bloqueia o caso |
| **relevância** | a resposta aborda a intenção sem distrair ou expor informação extra? | critérios de 1 a 4 e análise por categoria de pergunta |
| **fundamentação** | afirmações normativas estão apoiadas em trechos autorizados e suficientes? | cobertura de afirmações por citação e inspeção de entailment por amostra |
| **segurança** | a resposta preserva acesso, dados, política e escalonamento? | casos negativos; vazamento ou ausência de encaminhamento obrigatório é portão crítico |
| **utilidade** | o empregado sabe o que pode fazer, inclusive em recusa? | critérios humanos com próximo passo, clareza e adequação do limite |
| **latência** | o tempo é aceitável por rota comum e escalonada? | percentis 50, 95 e 99, incluindo recuperação e validações |
| **custo** | o consumo por resposta e por resolução cabe no orçamento? | média, percentil 95 e custo de casos adversariais, não só tokens do modelo |

O estudo [HELM](https://arxiv.org/abs/2211.09110) sustenta uma visão holística e transparente de cenários, métricas e modelos. A equipe usa o princípio de pluralidade, não copia um benchmark como se representasse RH local. Uma média ponderada serve para comparação exploratória, mas segurança e escalonamento mantêm portões separados: pontuação alta em utilidade não compensa um vazamento.

## Três tipos de avaliação, três limites

**Verificações determinísticas** examinam esquema, autorização, identificador do titular, existência e vigência de citação, categorias de escalonamento, campos proibidos, tamanho, tempo e custo. Elas são rápidas e reproduzíveis. Não determinam por si se uma explicação ambígua é útil nem se uma citação realmente sustenta a nuance da afirmação.

**Critérios humanos** definem níveis observáveis. Para utilidade: 1 é enganosa ou sem próximo passo; 2 é parcialmente útil, mas omite limite importante; 3 resolve com limite e próximo passo; 4 resolve de forma clara, proporcional e apoiada. Dois avaliadores julgam uma amostra, discutem divergências e refinam exemplos. Humanos trazem contexto, mas sofrem fadiga, viés, diferença de conhecimento e pressão por concordar.

A **avaliação assistida por modelo** aplica critérios de avaliação em escala e produz justificativa referenciada à resposta e às evidências. Use versão identificada, temperatura controlada quando disponível, exemplos, ordem alternada e calibração periódica. Ela não substitui critérios humanos nem se torna independente só porque usa outro modelo. O **viés do avaliador** pode favorecer respostas longas, estilo específico ou famílias semelhantes; monitore discordância por fatia e envie casos de baixa confiança para pessoas.

## Conjuntos, componentes e regressão

O **conjunto de referência** contém 480 casos selecionados por intenções e riscos: perguntas comuns, ambiguidades, políticas conflitantes, ausência de evidência, dados pessoais, perfis sem permissão e escalonamentos. Cada item registra entrada, identidade sintética, versão das fontes, evidências aceitáveis, resposta ou comportamento esperado, dimensões e severidade. Há divisão entre desenvolvimento e portão; autores de mudanças não veem todos os casos do portão.

Os **casos adversariais** incluem injeções diretas e indiretas, Unicode e codificação, pedido de dado de terceiro, prompt longo, repetição, documento contaminado, fonte vencida, fonte ausente, conflito de jurisdição e tentativa de evitar encaminhamento. Eles evoluem com incidentes e testes, mas não recebem conversa de produção sem curadoria e autorização.

A **avaliação por componente** mede recuperação e geração separadamente. Na recuperação, a equipe observa autorização, cobertura de evidência, precisão do contexto, vigência e ranking. O artigo original [RAGAs](https://aclanthology.org/2024.eacl-demo.16/) apresenta avaliação automatizada de sistemas RAG; suas métricas são instrumentos com hipóteses, não garantias. Na geração, mede vínculo entre afirmações e contexto, recusa e segurança. Na ferramenta, verifica identidade e contrato.

A **avaliação ponta a ponta** executa a mesma interface do empregado, incluindo identidade, filtros, latência, fallback e escalonamento. Ela captura composição e experiência, mas localiza causas com menos precisão. Por isso ambas são necessárias: componente diagnostica; ponta a ponta decide se a jornada integrada atende.

Toda alteração executa **regressão** no conjunto fixo e em casos novos, comparando configuração candidata e base. A equipe examina ganhos e perdas por dimensão e fatia; não aceita “melhorou a média”. Aprovação offline libera canary de 5% com conteúdo público e consulta pessoal limitada, orçamento, alertas e rollback. Somente após estabilidade e revisão de amostras o alcance aumenta.

## Julgamento final

A proposta original não é liberada: escrita, corpus amplo e retenção vaga excedem a evidência. A versão reduzida entra em piloto; o dono de RH aceita por 60 dias resposta incorreta não crítica e falsa recusa como riscos residuais. Vazamento, acesso cruzado, falta de escalonamento obrigatório ou mudança não avaliada interrompem o piloto.

A decisão é temporal. “Aprovado” significa aprovado para esta configuração, público, finalidade, período e capacidade de resposta — não certificado para qualquer uso. Agora aplique o raciocínio nos [Exercícios](exercicios.md).
