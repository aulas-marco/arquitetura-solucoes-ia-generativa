# Oficinas locais e executáveis — desenho

**Data:** 2026-07-16  
**Status:** aprovado para especificação; aguardando revisão do documento antes do plano de implementação.

## Objetivo

Transformar as seis oficinas da disciplina em laboratórios práticos, reproduzíveis e executáveis com ferramentas locais e open source. Cada estudante deve conseguir identificar a ferramenta, instalá-la, preparar os arquivos de entrada, executar comandos, inspecionar resultados e responder a questões alinhadas à taxonomia de Bloom.

O material não deve condicionar a atividade a conta, cartão, cobrança, serviço comercial ou chamada remota. Referências a esses temas serão removidas das oficinas e dos exercícios. A análise manual poderá permanecer apenas como contingência explícita para uma falha local de instalação, nunca como rota principal.

## Padrão editorial e didático

Toda oficina seguirá, na mesma ordem, esta estrutura:

1. **Objetivo de aprendizagem e decisão arquitetural:** explica o que será aprendido e qual decisão de arquitetura a prática torna observável.
2. **Ferramenta:** apresenta nome, finalidade, licença/abertura e o papel da ferramenta no laboratório.
3. **Pré-requisitos:** sistema, versões, espaço em disco, serviço local já necessário e dados sintéticos autorizados.
4. **Instalação:** comandos copiados e executados em uma pasta de laboratório, incluindo alternativa de ativação no Windows quando aplicável.
5. **Preparação:** arquivos e conteúdo completos, com nome, localização e significado de cada artefato.
6. **Execução:** comandos sequenciais, sem lacunas como “crie um script” ou “adicione o corpus” sem instrução concreta.
7. **Resultado esperado:** saída observável, como resposta, IDs recuperados, trace, avaliação ou arquivo gerado.
8. **Interpretação e variações:** o que comparar, qual variável alterar e quais conclusões não podem ser tiradas de uma única execução.
9. **Entrega e questões exploratórias:** evidências, critérios e perguntas conservadoras de Bloom para a aula; extensões ficam claramente separadas.
10. **Limpeza e contingência:** como parar processos, remover artefatos e continuar a aprendizagem caso a instalação local falhe.

Todos os dados continuam sintéticos. Cada laboratório indicará explicitamente os arquivos que devem ser apagados e a proibição de inserir dados pessoais, institucionais, credenciais ou documentos reais.

## Ferramentas e experiências por módulo

| Módulo | Ferramenta local/open source | Experiência executável | Evidência central |
|---|---|---|---|
| 1. Fundamentos | Ollama | Executar modelo local e variar temperatura pela API local | Respostas comparáveis e registro de parâmetros |
| 2. Desenho conceitual | LiteLLM Proxy + Ollama | Subir um gateway local, enviar solicitação por contrato estável e alterar o modelo no manifesto | Requisição, resposta, manifesto e mini-ADR |
| 3. RAG | LangChain + Chroma + Ollama | Criar corpus Boreal em arquivos, ingerir, recuperar trechos e responder com citação | IDs, versões, trechos e resposta fundamentada |
| 4. Agentes | LangGraph + Ollama | Executar grafo local com estado, ferramenta simulada e limite de autonomia | Histórico de estados e decisão de parada |
| 5. Confiança | DeepEval + Ollama | Avaliar casos sintéticos e inspecionar resultado de cada critério | Relatório de avaliação, falhas e hipótese de correção |
| 6. Operação | OpenTelemetry + LiteLLM Proxy + Ollama | Gerar uma solicitação local, observar trace/telemetria e analisar latência e erro | Trace, métricas locais e parecer operacional |

Quando uma biblioteca admitir diferentes versões ou o projeto mudar de APIs, o material fixará comandos compatíveis e verificará a execução durante a atualização do site.

## Reconstrução do Módulo 2

A oficina deixa de ser uma inspeção de fixture. O estudante criará uma pasta de laboratório, instalará LiteLLM, confirmará que Ollama e um modelo local estão disponíveis e salvará um manifesto `litellm_config.yaml`. O manifesto declarará um alias público e um destino local `ollama/<modelo>`.

Em seguida, iniciará o proxy, enviará uma requisição HTTP compatível com o contrato de chat e observará a resposta recebida pelo gateway. A variação pedirá que troque o modelo configurado sem alterar a requisição do cliente. O arquivo JSON de exemplo permanecerá apenas como contrato de entrada/saída explicado e reutilizado pelo comando, nunca como uma fixture isolada.

A mini-ADR continuará sendo a entrega, mas será sustentada pela observação de: contrato exposto, manifesto, fronteira do gateway, modelo selecionado e resultado da troca controlada.

## Reconstrução do Módulo 3

A oficina fornecerá os arquivos completos `politica-reembolso.txt`, `politica-campanha.txt` e `portal-estorno.txt`, contendo o corpus Boreal com IDs e versões. O estudante instalará LangChain, Chroma e a integração local de Ollama, criará o ambiente virtual e executará um script fornecido integralmente.

O script realizará ingestão em `chroma-boreal`, fará uma pergunta, imprimirá os metadados e textos recuperados e pedirá ao modelo local que responda somente com base nos trechos selecionados. Uma segunda pergunta demonstrará a necessidade de abstenção/revisão humana quando a informação estiver incompleta.

Uma variação controlada removerá ou filtrará um documento para mostrar a diferença entre falha de recuperação e resposta sem sustentação. A evidência exigirá a transcrição dos IDs/versões e a comparação entre as duas execuções.

## Aplicação global de linguagem

Em todas as oficinas e exercícios públicos:

- Remover menções a cartão, crédito, cobrança, rota comercial, rota institucional e “sem cartão”.
- Substituir classificações de acesso por instruções diretas da prática local.
- Manter custos operacionais locais somente quando forem relevantes para a decisão arquitetural (CPU, memória, disco e energia), sem transformar isso em requisito de acesso.
- Mencionar fornecedores ou serviços externos somente em material conceitual quando ajudarem a situar o ecossistema, e nunca como requisito ou alternativa da atividade.

## Critérios de aceitação

- Cada oficina nomeia uma ferramenta open source e possui comandos que podem ser executados localmente.
- Nenhuma oficina ou exercício público menciona cartão, crédito, cobrança, rota comercial/institucional ou “sem cartão”.
- M2 permite observar o mesmo contrato passando por LiteLLM e uma troca de modelo no manifesto.
- M3 oferece corpus em arquivos, script completo, ingestão, recuperação visível, resposta fundamentada e caso de abstenção.
- As seis oficinas têm pré-requisitos, instalação, preparação, execução, resultado esperado, variação, entrega, limpeza e contingência.
- Conteúdo e validações do MkDocs continuam passando antes da publicação.

## Limites de escopo

O trabalho não implantará infraestrutura de produção, não distribuirá modelos, não configurará serviços pagos e não usará dados reais. O foco é o letramento técnico e arquitetural em um ambiente local e descartável.
