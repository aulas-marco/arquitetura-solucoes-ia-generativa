# Conceitos: da oportunidade ao conceito de operações

![Mapa da oportunidade ao CONOPS: uma oportunidade é testada por hipóteses de valor e capacidade, passa por uma decisão de adequação da IA e se converte em CONOPS, partes interessadas, modos operacionais, responsabilidade humano–IA e requisitos significativos; a rejeição da IA é uma saída válida](../assets/images/m02-mapa-da-oportunidade-ao-conops.png "Mapa da oportunidade ao CONOPS")

*Figura — A decisão arquitetural começa antes do modelo: uma oportunidade só merece solução depois que seu valor, sua capacidade e seu modo de operação podem ser defendidos.*

O desenho conceitual descreve **o que o sistema será no contexto de uso**, antes de comprometer a solução com produtos. Ele conecta intenção, experiência, informação, responsabilidades humanas e capacidades técnicas com precisão suficiente para revelar decisões e riscos.

## Oportunidade não é solução

Uma oportunidade combina uma situação observada, um grupo afetado e uma melhoria desejada. “Adotar IA generativa no atendimento” não é oportunidade; já pressupõe tecnologia. Uma formulação melhor seria: “analistas gastam 35% do tempo localizando políticas e consolidando evidências, o que aumenta o prazo e a inconsistência das contestações”. Essa formulação aceita respostas diferentes: melhorar busca, redesenhar processo, criar regras, oferecer um copiloto ou não mudar o software.

Resultado atual mensurado, resultado desejado e hipótese causal evitam a solução prematura.

Uma métrica de atividade, como número de respostas geradas, não demonstra valor. Tempo de ciclo, retrabalho, conformidade, taxa de resolução e compreensão do usuário estão mais próximos do resultado. Mesmo assim, precisam de contramétricas: reduzir tempo elevando decisões incorretas não é sucesso.

## Hipótese de valor e hipótese de capacidade

A **hipótese de valor** afirma que uma mudança no sistema sociotécnico melhora um resultado relevante. A **hipótese de capacidade** afirma que um mecanismo consegue executar uma tarefa sob condições definidas. Confundi-las produz provas de conceito impressionantes e produtos inúteis.

No Banco Lume:

> Se analistas receberem um resumo rastreável de evidências e políticas aplicáveis, poderão preparar contestações em menos tempo sem elevar correções do supervisor.

Essa é a hipótese de valor. “Um modelo resume dez documentos com nota média 4/5” é uma hipótese de capacidade. Ela pode ser necessária, mas não prova que o fluxo reduz tempo, que a evidência chega correta ou que as pessoas confiam nela na medida adequada.

Uma boa ficha registra problema, resultado, baseline, intervenção, evidência refutável e dono da decisão. Pergunte sempre o que não pode piorar e quem decide interromper.

## Critérios de adequação da IA generativa

IA generativa tende a ser candidata quando a tarefa exige interpretar linguagem ou conteúdo não estruturado, sintetizar múltiplas evidências, produzir uma representação adaptada a um contexto ou lidar com variedade que tornaria regras explícitas frágeis. A candidatura fica mais forte quando uma saída aproximada pode ser avaliada, corrigida ou contida antes de produzir dano.

Use cinco perguntas:

1. **Variabilidade útil:** há muitas formas aceitáveis de saída, ou existe uma única resposta calculável?
2. **Dados e contexto:** existem exemplos, evidências e permissões suficientes para orientar e avaliar o comportamento?
3. **Tolerância ao erro:** uma saída imperfeita pode ser detectada e revisada antes do efeito?
4. **Critério de qualidade:** especialistas conseguem julgar casos representativos com concordância aceitável?
5. **Vantagem comparativa:** a capacidade generativa supera uma alternativa convencional em valor total, não só em demonstração?

A resposta “sim” não autoriza automação. Ela apenas justifica um experimento controlado. Modelos fundacionais apresentam capacidades amplas, mas também riscos dependentes de composição e contexto, como discute o relatório primário [On the Opportunities and Risks of Foundation Models](https://arxiv.org/abs/2108.07258). A unidade de decisão permanece o sistema, não o modelo isolado.

## Quando rejeitar IA generativa

Rejeite GenAI quando:

- a saída correta deriva de regra estável, cálculo ou consulta estruturada;
- qualquer variação é defeito e não existe contenção antes do efeito;
- não há dados legalmente utilizáveis ou exemplos representativos para avaliação;
- o requisito exige explicação causal ou garantia formal que a geração não fornece;
- latência, custo, residência, retenção ou conectividade tornam a solução inviável;
- a tarefa automatizada remove uma responsabilidade humana irrenunciável;
- uma busca, formulário, regra ou melhoria de processo produz valor equivalente com menos risco.

Se política, valor, prazo e categoria determinam exatamente um reembolso, regras devem decidir. Um modelo pode explicar ou extrair campos, mantendo decisão e efeito determinísticos.

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

## Stakeholders e preocupações

“Usuário” é uma categoria insuficiente. Analista, cliente afetado, supervisor, dono da política, encarregado de dados, Segurança, Operações, auditoria, fornecedor e equipe de manutenção enxergam riscos diferentes. Uma matriz de preocupações torna tensões visíveis:

| Stakeholder | Resultado desejado | Preocupação arquitetural |
|---|---|---|
| Analista | preparar caso com menos busca manual | utilidade, latência, fontes compreensíveis |
| Supervisor | revisar decisões consistentes | destaque de incerteza, histórico e comparação |
| Cliente | tratamento justo e tempestivo | contestabilidade, privacidade, ausência de dano |
| Dono da política | aplicar versão vigente | atualização, semântica e resolução de conflitos |
| Segurança e Privacidade | limitar exposição e abuso | minimização, autorização, retenção e auditoria |
| Operações | manter serviço recuperável | dependências, fallback, observabilidade e custo |
| Auditoria | reconstruir decisão | identidade, versões, evidências e ações humanas |

Treinamento, processo, papéis e contestação também respondem a preocupações do sistema sociotécnico.

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

## Do conceito ao requisito

Ao final do desenho conceitual inicial, a equipe deve conseguir declarar: oportunidade, hipótese de valor, critérios de adequação, fora de escopo, stakeholders, cenários, modos, fronteiras e divisão de responsabilidade. A próxima etapa não é escolher um modelo; é transformar esses elementos em objetivos, requisitos significativos e critérios de aceitação que permitam comparar alternativas.

**Próxima página:** [Requisitos e padrões de decisão](padroes-e-decisoes.md).
