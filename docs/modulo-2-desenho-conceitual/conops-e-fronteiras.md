# CONOPS, fronteiras e stakeholders

O sistema descrito em operação, com o que está dentro e fora de escopo, quem se preocupa com o quê e onde a pessoa entra.

## CONOPS: o sistema em operação

O **Concept of Operations (CONOPS)** descreve como o sistema será usado sob condições normais e excepcionais. É mais amplo que uma jornada e menos detalhado que uma arquitetura de componentes. Responde:

- quem inicia, supervisiona, recebe e contesta resultados;
- que informação entra, de onde vem e sob qual autoridade;
- quais atividades continuam humanas;
- quais modos de operação existem;
- quais efeitos são permitidos e proibidos;
- como o sistema degrada, interrompe e recupera;
- que evidências ficam disponíveis para usuário, operação e auditoria.

### Cenário operacional essencial

Um cenário não é apenas “usuário faz pergunta”. Escreva ator, objetivo, precondições, estímulo, colaboração, resultado, exceções e evidência. Exemplo:

> Um analista autenticado abre uma contestação já classificada. O sistema reúne apenas dados autorizados do caso e políticas vigentes, propõe um resumo com referências e destaca lacunas. O analista confere evidências, corrige a proposta e registra recomendação. Um supervisor aprova ou devolve. Se uma fonte essencial estiver indisponível ou o suporte for insuficiente, o sistema não recomenda; preserva o trabalho e orienta a consulta manual.

Essa narrativa revela necessidades que “chat com LLM” oculta: identidade, autorização por dado, vigência, proveniência, estado de trabalho, revisão, segregação de função e degradação segura.

## Fronteiras e fora de escopo

Fronteira define responsabilidade, não apenas rede. Marque:

- **fronteira organizacional:** quem é responsável por processo, dado, modelo e operação;
- **fronteira de confiança:** onde conteúdo, identidade ou instrução muda de nível de confiança;
- **fronteira de dados:** onde informação é coletada, derivada, persistida, registrada ou enviada;
- **fronteira de decisão:** onde uma recomendação passa a produzir consequência;
- **fronteira de fornecedor:** onde políticas de retenção, treinamento, localização e suporte deixam de ser controladas diretamente.

O fora de escopo evita expectativas perigosas. No Banco Lume: não aprovar, alterar cadastro, enviar comunicações, aprender com correções individuais ou tratar categorias não avaliadas. Cada exclusão precisa aparecer em interface, autorização e testes.

### Proveniência

**Proveniência** é a cadeia verificável que permite explicar uma evidência: **de onde veio**, **sob qual autoridade foi acessada**, **qual versão e vigência possuía**, **quais transformações ou seleções sofreu** e **onde foi usada na resposta ou decisão**. Não é apenas uma URL ou citação. Em um sistema generativo, ela liga fonte, identidade, finalidade, transformação, trecho recuperado, versão de política, modelo e saída. Essa cadeia permite contestar uma recomendação, revogar uma fonte e investigar uma resposta sem conservar conteúdo além do necessário.

Um **adaptador** separa contrato e fornecedor: **OpenAI SDK** e **LiteLLM** consomem modelos; **Docker Model Runner** apoia execução local. Nenhum define finalidade, dado ou autorização.

## Stakeholders e preocupações

“Usuário” é uma categoria insuficiente. Analista, cliente afetado, supervisor, dono da política, encarregado de dados, Segurança, Operações, auditoria, fornecedor e equipe de manutenção enxergam riscos diferentes. Uma matriz de preocupações torna tensões visíveis:

| Stakeholder             | Resultado desejado                   | Preocupação arquitetural                        |
| ----------------------- | ------------------------------------ | ----------------------------------------------- |
| Analista                | preparar caso com menos busca manual | utilidade, latência, fontes compreensíveis      |
| Supervisor              | revisar decisões consistentes        | destaque de incerteza, histórico e comparação   |
| Cliente                 | tratamento justo e tempestivo        | contestabilidade, privacidade, ausência de dano |
| Dono da política        | aplicar versão vigente               | atualização, semântica e resolução de conflitos |
| Segurança e Privacidade | limitar exposição e abuso            | minimização, autorização, retenção e auditoria  |
| Operações               | manter serviço recuperável           | dependências, fallback, observabilidade e custo |
| Auditoria               | reconstruir decisão                  | identidade, versões, evidências e ações humanas |

Treinamento, processo, papéis e contestação também respondem a preocupações do sistema sociotécnico.

## Modularidade e fronteiras de componente

Componentes devem ter responsabilidade coesa e dependências deliberadas. O **orquestrador** coordena o caso, mas não deve conhecer peculiaridades de cada legado; **adaptadores** isolam contratos, versões e falhas de fornecedor; o **montador de contexto** seleciona evidências; o **gateway** aplica controles transversais; a **validação** verifica saída e suporte. Essa separação reduz acoplamento: trocar um fornecedor ou uma fonte deve afetar seu adaptador, não reescrever a política de autorização nem o workflow humano. Separar sem motivo também cria chamadas, latência e operação adicionais; a fronteira só se justifica por mudança independente, risco ou atributo de qualidade.

## Modos operacionais

Defina modos e transições além do caminho feliz:

1. **normal:** dependências saudáveis, escopo válido e evidência suficiente;
2. **baixa confiança:** proposta parcial, lacunas e revisão reforçada;
3. **degradado:** dependência indisponível e trabalho manual acessível;
4. **bloqueado:** dado, finalidade ou ação não autorizada;
5. **manutenção ou incidente:** mudança controlada, contenção e recuperação.

Para cada transição, especifique gatilho, estado preservado, pessoa informada e critério de retorno. Retry indiscriminado não é estratégia de recuperação: pode elevar custo, amplificar carga e repetir efeitos.

## Responsabilidade humano–IA

“Human in the loop” não explica quem decide. Separe responsabilidades por verbo:

- o sistema **localiza**, **extrai**, **resume**, **sinaliza** e **propõe**;
- o analista **verifica**, **complementa**, **justifica** e **recomenda**;
- o supervisor **aprova**, **devolve** ou **escala**;
- o dono da política **define** interpretação oficial;
- Operações **monitora**, **contém** e **restaura**.

Revisão só controla quando há competência, tempo, autoridade, evidências e interface para discordar. Um clique após recomendação sem fontes é ritual. Registre correções sem tratá-las automaticamente como rótulos e permita recusa.
