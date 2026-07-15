# Estudo de caso: assistente interno de documentos

Este caso é independente do exemplo anterior: você receberá dados suficientes para elaborar uma leitura arquitetural sem pressupor uma implementação de RAG. O objetivo não é desenhar todos os componentes, mas comparar três direções e explicitar o que ainda precisa ser provado.

## Situação

A empresa Horizonte possui políticas de pessoas, compras e viagens em um repositório interno. Analistas de atendimento gastam tempo localizando a versão vigente e traduzindo texto normativo em orientação prática. A liderança propõe um assistente que responda em português e mostre de onde veio a informação.

### Stakeholders

- **Analistas de atendimento:** querem resposta rápida e um caminho para abrir o documento original.
- **Pessoas colaboradoras:** precisam de orientação compreensível, sem que o assistente se apresente como decisão oficial.
- **Donos das políticas:** respondem por aprovação, vigência e resolução de conflitos entre fontes.
- **Segurança e privacidade:** exigem isolamento entre perfis e minimização de conteúdo em logs e fornecedores.
- **Operações de TI:** precisam implantar, observar, reverter e suportar a solução com uma equipe pequena.
- **Auditoria:** quer reconstruir quais fontes e versões sustentaram uma resposta crítica.

## Restrições conhecidas

O acervo contém 420 documentos e 11 mil páginas. Trinta documentos são restritos à liderança; 65 contêm dados pessoais em anexos que não devem ser usados como conhecimento. O restante é interno geral ou segmentado por área. Em média, 35 documentos recebem nova versão por mês. Há arquivos duplicados e doze políticas sem dono confirmado.

O piloto terá 150 usuários e orçamento para uma equipe de três pessoas durante oito semanas. A solução pode apenas orientar e indicar fontes: não aprovará reembolsos, não alterará cadastros e não enviará mensagens em nome do usuário. O p95 desejado para resposta completa é oito segundos. Perguntas sensíveis sem evidência suficiente devem ser encaminhadas ao atendimento humano.

## Evidências iniciais

Um teste exploratório usou 30 perguntas reais anonimizadas:

| Observação | Resultado inicial |
|---|---:|
| Perguntas respondidas corretamente por analistas com acesso ao repositório | 27/30 |
| Respostas aceitáveis de um modelo sem documentos corporativos | 9/30 |
| Respostas aceitáveis com até três documentos escolhidos manualmente no contexto | 24/30 |
| Casos em que o documento inteiro continha anexo ou seção não pertinente | 18/30 |
| Perguntas cuja resposta dependia da versão vigente | 11/30 |
| Perguntas com fontes parcialmente contraditórias | 4/30 |

Esses números são amostra, não conclusão. A seleção manual favorece a alternativa de contexto: um sistema real ainda teria de localizar documentos. Também faltam perguntas sem resposta, testes entre perfis, medição de custo e latência e critérios consistentes para julgar fundamentação.

## Três desenhos candidatos

### A. Modelo direto

O canal envia a pergunta e uma instrução versionada ao modelo. A aplicação valida a saída e informa que se trata de orientação geral.

**Força:** menor tempo de implementação e boa linha de base. **Limite decisivo:** o conhecimento paramétrico não contém as políticas privadas vigentes nem permite indicar a versão consultada. O resultado de 9/30 é compatível com respostas gerais, mas insuficiente para o propósito. Esta alternativa poderia permanecer apenas para reformular texto fornecido pelo próprio usuário, não para responder sobre o acervo.

### B. Documentos completos no contexto

A aplicação seleciona um conjunto de documentos e os envia integralmente com a pergunta. Não há índice de trechos.

**Força:** para poucos documentos conhecidos, preserva conteúdo e reduz infraestrutura. **Questão oculta:** quem fará a seleção? Enviar os 420 arquivos é inviável; pedir que o usuário escolha contradiz a promessa de assistência. Documentos completos aumentam tokens, latência e exposição de anexos. Ainda seria necessário controlar versão e autorização antes de montar o contexto.

Esta opção pode ser apropriada para um primeiro recorte, por exemplo três políticas públicas de viagem sem anexos, desde que a seleção seja determinística. Não é uma resposta geral ao acervo.

### C. Contexto baseado em recuperação

Um fluxo prepara fontes aprovadas com metadados e unidades menores. Na pergunta, a aplicação propaga identidade, recupera candidatos autorizados e envia ao modelo apenas trechos e identificadores pertinentes.

**Força:** torna seleção, atualização e proveniência responsabilidades explícitas. **Custo:** adiciona ingestão, segmentação, índice, sincronização de permissões e falhas de recuperação. Uma resposta pode ser ruim porque a evidência não foi encontrada ou porque foi mal utilizada; as duas etapas precisam de avaliação separada.

O desenho é promissor para escala e atualização, mas ainda é uma hipótese. O piloto deve começar com corpus limpo e perguntas representativas, não com todos os documentos e uma confiança presumida.

## Trabalho de arquitetura solicitado

Produza uma leitura de uma a duas páginas, não um projeto detalhado de RAG. Seu entregável deve conter:

1. **Recomendação:** escolha uma direção para o piloto e delimite o que fica fora dele.
2. **Diagrama simples:** mostre canal, aplicação, seleção de contexto, modelo, fontes e capacidades transversais; identifique fronteiras de autorização.
3. **Dois cenários de qualidade:** um de fundamentação e um entre latência, privacidade ou segurança, no formato fonte–estímulo–ambiente–artefato–resposta–medida.
4. **Riscos e contenções:** relacione pelo menos três pares; inclua ausência de evidência e acesso indevido.
5. **Hipóteses a testar:** defina conjunto de perguntas, métricas e critérios de decisão.
6. **Questões abertas:** indique donos de política, documentos contraditórios, retenção e mecanismo de encaminhamento.

Uma recomendação sólida pode selecionar C para um corpus piloto e usar B como linha de base comparativa. Também pode rejeitar o lançamento até que fontes sem dono sejam resolvidas. O que não é aceitável é escolher pela popularidade do padrão sem relacioná-lo às restrições e evidências.

## Pistas para a discussão

- O problema é geração de texto, localização de evidência ou ambos?
- Em que ponto a identidade do usuário precisa ser conhecida?
- Como diferenciar “não encontrei” de “o modelo não soube usar o trecho”?
- Que dados do trace são indispensáveis e quais criariam risco de privacidade?
- Qual resultado faria a equipe abandonar a alternativa escolhida?

O caso prepara a competência central do curso: decisões proporcionais ao contexto, sustentadas por evidência e revisáveis. Agora consolide o vocabulário nos [exercícios](exercicios.md).
