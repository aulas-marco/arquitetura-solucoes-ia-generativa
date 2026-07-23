# Síntese e referências

## O argumento do módulo

Operar sistemas generativos é controlar uma composição que muda. Pacote comportamental, avaliação contínua, entrega gradual, observabilidade e recuperação tornam premissas, versões, limites e responsáveis visíveis. A plataforma escala capacidades comuns sem absorver a responsabilidade dos domínios; maturidade significa conter falhas e transformar evidência em mudança verificável.

## A progressão dos seis módulos

- O **Módulo 1** separou capacidade probabilística de controle determinístico e situou o modelo dentro de um sistema.
- O **Módulo 2** partiu do problema, dos stakeholders, dos atributos de qualidade e das decisões registradas.
- O **Módulo 3** organizou conhecimento em ingestão e consulta, com proveniência, vigência e autorização.
- O **Módulo 4** distinguiu workflow, agente, ferramenta e efeito, mantendo autoridade fora do texto gerado.
- O **Módulo 5** conectou ameaças, guardrails, avaliação multidimensional, governança e risco residual.
- O **Módulo 6** coloca tudo no tempo: versões, promoção, observação, recuperação, plataforma, equipes e economia.

O capstone é um argumento rastreável do contexto à operação: propósito, qualidade, fluxo, falhas, autoridade, evidência, degradação e experimentos pendentes.

## Checklist de prontidão para produção

- [ ] Contexto, público, finalidade, usos proibidos e dono do processo estão registrados.
- [ ] Atributos de qualidade têm cenários, medidas, população e janela.
- [ ] Modelos, prompts, políticas, corpus, índices, ferramentas, avaliadores e dependências têm versões relacionadas por manifesto.
- [ ] Desenvolvimento, homologação e produção segregam identidades, dados, segredos, índices, quotas e telemetria.
- [ ] O replay evita repetir efeitos e respeita finalidade e retenção.
- [ ] Conjunto de referência cobre fatias comuns, raras, adversariais e de recusa.
- [ ] Portões separam eventos intoleráveis de metas negociáveis e registram exceções.
- [ ] Canary tem coorte, duração, volume, critérios de avanço e autoridade de interrupção.
- [ ] Traces ligam prompt, contexto, recuperação, ferramenta e resposta às versões e decisões.
- [ ] Logs com conteúdo são exceção; minimização, acesso, segregação, retenção e descarte foram testados.
- [ ] Métricas de produto, modelo, operação e negócio sustentam decisões explícitas.
- [ ] SLOs representam serviço útil; eventos críticos não são compensados por médias.
- [ ] Roteamento e fallback preservam classe de dados, política e qualidade mínima.
- [ ] Rollback do manifesto, degradação e reconciliação de efeitos foram ensaiados.
- [ ] Alertas possuem proprietário, runbook, acesso a evidência e caminho de comunicação.
- [ ] Resposta a incidente delimita impacto, contém, recupera e atualiza testes e riscos.
- [ ] Gateway e serviços comuns possuem SLO, isolamento, extensão governada e modo de falha.
- [ ] Catálogo reconcilia modelos aprovados com tráfego real.
- [ ] Identidade e tenancy têm testes negativos ponta a ponta.
- [ ] Cotas protegem cargas críticas; showback ou chargeback possui atribuição contestável.
- [ ] Equipes de plataforma, produto, operação, segurança, privacidade, FinOps e domínio conhecem seus limites.
- [ ] Riscos residuais têm autoridade, prazo, gatilho e experimento quando falta evidência.

## Fontes oficiais e primárias

### Operação, observabilidade e entrega

- [OpenTelemetry Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/). Especificação oficial para nomes e atributos de telemetria. Convenções evoluem; fixe a versão adotada.
- [OpenTelemetry GenAI Semantic Conventions](https://github.com/open-telemetry/semantic-conventions-genai). Projeto oficial de convenções para IA generativa. É **prática viva**, não contrato eternamente estável; valide maturidade e privacidade de cada campo.
- [Service Level Objectives, Google SRE Book](https://sre.google/sre-book/service-level-objectives/). Capítulo institucional sobre indicadores, objetivos e foco no usuário.
- [DORA's Software Delivery Performance Metrics](https://dora.dev/guides/dora-metrics/). Orientação institucional atual sobre desempenho de entrega. Suas métricas observam capacidade de entrega; não substituem qualidade generativa, risco ou valor de negócio.
- [Hidden Technical Debt in Machine Learning Systems](https://proceedings.neurips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html), de D. Sculley et al. Artigo primário sobre dependências e dívida sistêmica em ML.

### Risco, desenvolvimento e interoperabilidade

- [NIST AI Risk Management Framework 1.0](https://doi.org/10.6028/NIST.AI.100-1) e [Generative AI Profile](https://doi.org/10.6028/NIST.AI.600-1). Referenciais institucionais para governar, mapear, medir e gerenciar risco; não prescrevem esta plataforma.
- [NIST SP 800-218A](https://doi.org/10.6028/NIST.SP.800-218A). Perfil institucional de desenvolvimento seguro para IA generativa e modelos de uso dual.
- [Model Context Protocol Specification](https://modelcontextprotocol.io/specification/2025-11-25). Especificação oficial de interoperabilidade de contexto e ferramentas. Compatibilidade de protocolo não concede autorização nem garante segurança semântica.
- [ISO/IEC 42001:2023](https://www.iso.org/standard/42001). Padrão internacional para sistema de gestão de IA; não define uma arquitetura tecnológica única.

## O que é referência e o que é prática viva

Fontes oficiais fornecem vocabulário dentro de seu escopo. A arquitetura proposta é síntese pedagógica; limiares e retenção pertencem ao contexto.

**Prática viva** é uma convenção ou abordagem ainda sujeita a rápida mudança, como schemas GenAI de telemetria, capacidades de gateways e estratégias de avaliação assistida por modelo. Registre versão e data, teste migração e revise evidência. “Padrão de mercado” sem contrato, estabilidade ou fonte não é decisão arquitetural.

Use o [Mapa de aprendizagem](../comecar/mapa-de-aprendizagem.md) para percorrer novamente contexto, arquitetura, conhecimento, ação, confiança e operação em um sistema real.

## Tendências e futuro da arquitetura com GenAI

Prever produtos vencedores é uma base frágil para arquitetura. O fechamento do curso usa outra pergunta: **que direção pode alterar decisões, riscos ou experimentos, e quais capacidades continuam necessárias independentemente do fornecedor?** Tendências são tratadas como hipóteses com evidência e horizonte, não como lista de novidades.

### Contexto longo muda o limite, não elimina arquitetura de contexto

Janelas maiores permitem analisar documentos extensos, históricos e conjuntos de código que antes exigiam segmentação agressiva. Isso reduz algumas perdas locais, mas não transforma contexto em memória autoritativa nem torna todo conteúdo relevante.

Mesmo com milhões de tokens, permanecem decisões:

- que fontes podem ser usadas por identidade e finalidade;
- qual versão e vigência valem;
- como ordenar evidências contraditórias;
- quanto custa e demora processar o contexto;
- como minimizar dados pessoais;
- como medir se informação crítica foi utilizada;
- quando recuperar seletivamente é superior a enviar tudo.

O sinal arquitetural não é apenas o tamanho anunciado da janela. É a combinação de qualidade em posições distantes, custo por trajetória, latência, controles de acesso e resultado em tarefas reais. Um experimento deve comparar contexto amplo, recuperação seletiva e abordagem híbrida com o mesmo conjunto de casos.

O que permanece: proveniência, autorização, seleção, versionamento, avaliação e observabilidade.

### Multimodalidade amplia superfícies e seams

Texto, imagem, áudio, vídeo e interfaces tornam-se entradas e saídas de uma mesma trajetória. Isso permite inspeção visual, assistência por voz, análise documental e geração de artefatos ricos. Também amplia superfície de ataque e avaliação.

Uma imagem pode carregar instrução adversarial; áudio pode conter dados biométricos; vídeo exige segmentação temporal; OCR introduz erro antes do modelo; uma resposta visual pode parecer correta e ainda distorcer escala ou omitir categoria. A arquitetura precisa rastrear transformações: arquivo original, extração, recorte, modelo, saída e revisão.

Perguntas de desenho:

1. Qual modalidade é autoritativa em caso de divergência?
2. Que pré-processamento altera significado?
3. Como consentimento e retenção variam por modalidade?
4. Que fallback existe para acessibilidade?
5. Como avaliar conteúdo e apresentação separadamente?
6. Que ferramentas podem produzir efeitos a partir de uma interpretação visual?

O sinal é desempenho verificável em uma jornada multimodal relevante, com erros e populações conhecidos. Demo impressionante sem conjunto de avaliação é hype.

O que permanece: contratos por etapa, acessibilidade, minimização, avaliação por componente e responsabilidade pela saída composta.

### Modelos abertos, fechados, locais e especializados

A fronteira não é simplesmente aberto versus hospedado. Há pesos disponíveis com licença restritiva, modelos pequenos especializados, APIs proprietárias, execução local, serviço gerenciado e arranjos híbridos. A escolha distribui responsabilidades:

| Dimensão | Hospedado | Aberto/autogerido |
|---|---|---|
| atualização | fornecedor controla ritmo | organização escolhe versão |
| operação | abstraída parcialmente | capacidade, runtime e otimização internos |
| dados | contrato e controles do serviço | controle maior, responsabilidade integral |
| customização | recursos oferecidos | amplo ajuste, com custo e risco |
| portabilidade | depende de API e semântica | depende de runtime, hardware e licença |
| evidência | documentação e testes próprios | testes próprios e transparência possível |

Modelos pequenos podem deslocar tarefas de classificação, extração ou roteamento para borda e reduzir custo. Modelos maiores podem permanecer em trajetórias complexas. Isso reforça arquitetura multimodelo, mas roteamento acrescenta outra decisão probabilística. É necessário medir erro de roteamento, qualidade mínima, fallback e custo total.

O sinal não é benchmark geral. É uma fronteira custo–qualidade–latência–risco melhor para tarefas e volumes da organização.

O que permanece: abstração suficiente para portabilidade, acesso a capacidades específicas quando justificadas, catálogo versionado e avaliação comparável.

### Agentes passam de conversa a trajetórias operacionais

Agentes tendem a executar trabalhos mais longos, usar computadores, coordenar ferramentas e retomar estado. O desafio muda de “o modelo chama uma função?” para “o sistema mantém uma trajetória segura através de horas, falhas e mudanças externas?”.

Isso exige:

- estado durável separado do contexto;
- checkpoints e retomada;
- identidade e credenciais por ferramenta;
- orçamento global e por fase;
- precondições revalidadas;
- idempotência e reconciliação;
- supervisão por risco;
- testes de trajetória e modos degradados;
- telemetria que reconstrua escolhas observáveis.

Mais autonomia aumenta o valor de ambientes isolados, permissões temporárias e execução reversível. Um agente que opera navegador ou terminal não deve herdar todas as credenciais da pessoa. Catálogos de ferramentas e políticas precisam ser mínimos por tarefa.

O sinal é taxa de conclusão com erros contidos, custo, intervenção e recuperação medidos. “Funcionou numa gravação” não caracteriza confiabilidade operacional.

O que permanece: autoridade fora do modelo, contratos estreitos, estados explícitos e responsabilidade humana.

### Desenvolvimento agêntico e SDD

O SDD do Módulo 4 é uma tendência porque modelos tornam especificações transformáveis em planos, testes e código. A unidade de trabalho pode migrar de “escrever função” para “governar a transformação de intenção em implementação”.

Possíveis efeitos:

- specs e ADRs ganham papel operacional;
- tarefas tornam-se pacotes de contexto para agentes;
- revisão separa aderência à intenção de qualidade técnica;
- testes e avaliações funcionam como gates executáveis;
- agentes especializados trabalham em fronteiras paralelas;
- produção retroalimenta requisitos e experimentos;
- repositórios são desenhados para navegabilidade por pessoas e agentes.

Isso não torna código descartável. Sistemas existentes carregam dados, migrações, contratos e história. Regenerar sem preservar compatibilidade pode destruir valor. A tendência relevante é elevar o nível de intenção mantendo disciplina de engenharia.

O sinal é redução de retrabalho e defeitos, maior rastreabilidade e lead time sustentável. Volume de código gerado ou quantidade de agentes não são medidas suficientes.

O que permanece: linguagem de domínio, modularidade, testes duráveis, revisão, configuração, migração e operação.

### Plataformas corporativas tornam IA uma capacidade governada

À medida que produtos proliferam, cada equipe não deve reconstruir identidade, gateway, telemetria, avaliação, guardrails e catálogo. Plataformas internas tendem a oferecer capacidades comuns:

- gateway e roteamento de modelos;
- identidade, tenancy, quotas e políticas;
- registro de prompts, specs e avaliadores;
- serviços de RAG e ferramentas;
- observabilidade e custos;
- ambientes de experimentação;
- catálogo de modelos e usos aprovados;
- esteiras de avaliação e promoção.

O risco é criar uma plataforma central que absorve decisões do domínio, padroniza cedo demais ou vira gargalo. O produto continua responsável por finalidade, dados, qualidade e experiência. A plataforma oferece mecanismos e evidência.

O sinal é redução mensurável de duplicação e tempo de adoção sem aumento de incidentes ou bloqueio de capacidades justificadas.

O que permanece: fronteiras de propriedade, contratos, SLOs, extensão governada e modos de falha.

### Regulação e governança tornam evidência parte da arquitetura

Leis e padrões evoluem por jurisdição, setor e impacto. Arquitetura não deve tentar adivinhar um texto regulatório futuro, mas pode construir capacidade de responder:

- inventário de sistemas, modelos, dados e responsáveis;
- finalidade e usos proibidos;
- avaliação de risco e impacto;
- proveniência e versionamento;
- supervisão e contestação;
- incidentes, mudanças e exceções;
- evidência de testes e decisões;
- retenção, acesso e descarte.

Governança emergente favorece sistemas que conseguem explicar processo e autoridade, não raciocínio interno completo do modelo. Traces, ADRs, specs, avaliações e registros de aprovação compõem evidência.

O sinal é requisito aplicável com prazo, autoridade e consequência. “A regulação vai proibir” sem fonte ou análise contextual é hype.

O que permanece: gestão de risco, privacidade, segurança, accountability e documentação verificável.

### Interfaces generativas e confiança calibrada

Interfaces podem migrar de menus estáticos para composição dinâmica, conversação e ações sugeridas. O risco é confundir fluidez com autoridade. Usuários precisam entender:

- quando conteúdo é gerado;
- que fonte e data sustentam a resposta;
- que ação será executada;
- quais campos foram inferidos;
- como corrigir, desfazer ou escalar;
- quando o sistema não possui evidência suficiente.

Personalização pode melhorar relevância e ampliar manipulação ou filtragem indevida. Memória persistente requer consentimento, correção e exclusão. Interfaces adaptativas precisam manter acessibilidade e previsibilidade em tarefas críticas.

O sinal é melhora em tarefa, confiança calibrada e recuperação de erro, não preferência estética numa demonstração.

O que permanece: design centrado em pessoas, divulgação de limites, confirmação proporcional e recurso.

### Arquitetura para substituição e opcionalidade

Mudanças rápidas valorizam **opcionalidade**, mas abstração universal pode esconder capacidades e criar menor denominador comum. Uma estratégia equilibrada:

1. isola contratos voláteis em adaptadores;
2. mantém semântica do domínio fora do SDK;
3. versiona prompts, modelos e políticas;
4. possui conjunto de avaliação portátil;
5. permite capacidades específicas por extensão explícita;
6. testa migração e fallback antes da necessidade;
7. registra custo de saída e dados que precisam ser movidos.

Portabilidade não significa troca instantânea. Significa compreender dependências, possuir evidência comparável e reduzir decisões irreversíveis sem benefício.

### Um radar baseado em decisão

Avalie tendências com uma ficha comum:

| Campo | Pergunta |
|---|---|
| alegação | que capacidade está sendo prometida? |
| fonte | é documentação, benchmark, estudo, demo ou opinião? |
| maturidade | pesquisa, preview, produto ou prática operacional? |
| decisão afetada | muda componente, contrato, risco ou operação? |
| evidência local | que experimento reproduz a alegação no nosso contexto? |
| custo de opção | quanto custa preparar sem adotar? |
| gatilho | que resultado autoriza adoção, espera ou abandono? |
| horizonte | agora, 6–18 meses ou exploração longa? |

O radar evita dois extremos: perseguir toda novidade e ignorar mudanças até virarem urgência.

### Sinal, hype e permanência

Considere **sinal** quando há mecanismo compreensível, evidência reproduzível, impacto sobre uma decisão e trajetória de maturidade. Trate como **hype** quando a alegação depende de demonstração selecionada, linguagem absoluta, benchmark sem contexto ou promessa de eliminar controles.

Pergunte sempre:

1. Que problema antigo esta tendência resolve?
2. Que risco novo introduz?
3. Qual suposição arquitetural ela invalida?
4. Qual evidência precisamos antes de mudar?
5. Que investimento reversível preserva opção?
6. O que continua necessário se a tendência não se confirmar?

O futuro muda ferramentas e fronteiras econômicas. O trabalho do arquiteto permanece reconhecer contexto, explicitar trade-offs, desenhar limites, produzir evidência e manter opções. A competência durável não é prever qual modelo vencerá, mas construir sistemas capazes de aprender e mudar sem perder controle.

## Autoavaliação

1. Consigo reproduzir o pacote comportamental promovido?
2. Ligo cada métrica a hipótese, decisão e responsável?
3. Distingo parada segura de experimento e incidente real?
4. Projeto fallback e rollback que preservam controles essenciais?
5. Delimito capacidades comuns, autonomia local e raio de impacto?
