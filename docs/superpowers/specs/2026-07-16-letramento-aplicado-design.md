# Desenho — letramento aplicado em Arquitetura de Soluções com IA Generativa

**Data:** 16 de julho de 2026  
**Status:** aprovado para revisão do documento

## Objetivo

Reequilibrar a disciplina de 24 horas para preservar a fundamentação arquitetural e, ao mesmo tempo, desenvolver letramento prático em ferramentas de IA generativa. Ferramentas materializam decisões e permitem produzir evidências; não substituem a análise arquitetural nem passam a ser o eixo da disciplina.

## Princípios de desenho

1. **Conceito antes da ferramenta.** Cada oficina parte de uma decisão, atributo de qualidade ou risco estudado no encontro.
2. **Independência de fornecedor.** O material descreve categorias, critérios e contratos; nomes de produtos aparecem como opções intercambiáveis.
3. **Acesso equitativo.** Toda atividade obrigatória terá um caminho viável sem cartão de crédito, conta corporativa ou consumo pago.
4. **Aprofundamento opcional.** Alternativas comerciais podem ser usadas por quem já possui acesso ou deseja experimentar recursos avançados, sem vantagem de avaliação.
5. **Evidência acima de demonstração.** O aluno registra hipótese, configuração, resultado, limite e implicação arquitetural.
6. **Ferramentas com Bloom conservador.** Nas aulas, atividades instrumentais priorizam lembrar, compreender, aplicar e analisar. Avaliar e criar ficam reservados para a integração progressiva e, sobretudo, para o projeto final.

## Estrutura por encontro

Cada encontro preserva a sequência conceituar → exemplificar → comparar → aplicar no caso → refletir. A oficina aplicada ocupa de 35 a 45 minutos, substituindo parte do experimento orientado e produz um artefato curto.

| Encontro | Decisão arquitetural | Oficina e artefato | Bloom predominante |
|---|---|---|---|
| 1. Fundamentos | comportamento de modelo, prompt, contexto e parâmetros | executar experimento controlado em playground ou ambiente local; registrar variação de qualidade, custo e latência | compreender, aplicar |
| 2. Desenho conceitual | serviço gerenciado, modelo aberto/autogerido, SDK e orquestração | preencher matriz de seleção e criar uma chamada mínima ou configuração equivalente | aplicar, analisar |
| 3. RAG | ingestão, recuperação, citação e avaliação | observar pipeline de RAG com corpus pequeno; comparar recuperação e resposta fundamentada | aplicar, analisar |
| 4. Agentes | workflow, ferramentas, aprovação e autonomia | configurar fluxo com uma ferramenta de consulta e autorização explícita; identificar fronteiras de efeito | aplicar, analisar |
| 5. Confiança | UX conversacional, segurança, guardrails e avaliação | executar casos adversariais e revisar saídas, recusas, escalonamento e evidências | analisar, avaliar |
| 6. Operação | gateway, LLMOps, custo, portfólio e evolução | ler traces e métricas de cenário; propor roteamento, SLO e controle de custo | analisar, avaliar |

## Política de opções de ferramenta

Cada oficina apresentará uma tabela com três rotas equivalentes:

| Rota | Uso | Regra didática |
|---|---|---|
| **Essencial, sem cartão** | ambiente local, sandbox gratuito, conta gratuita ou artefato previamente fornecido | é sempre suficiente para cumprir a atividade e obter nota máxima |
| **Institucional** | ambiente disponibilizado pela PUC ou empregador, quando existir | opcional; a turma não depende dele |
| **Comercial ou avançada** | serviço pago, API com crédito ou ferramenta licenciada | opcional; o aluno documenta limites e custo, mas não recebe vantagem por pagar |

O material deixará claro se uma opção requer instalação, conta, chave de API, cartão de crédito ou gasto. Não serão versionadas chaves, credenciais, dados pessoais ou documentos corporativos. Cada prática terá alternativa com corpus sintético e instruções para interromper consumo/custo.

## Novos conteúdos explícitos

Além de atualizar as páginas existentes, serão adicionadas seções didáticas e exercícios para:

- AI-as-a-Service, IA como commodity, gateways e portabilidade;
- categorias de SDK, bibliotecas e frameworks, incluindo critérios de seleção e riscos de abstração;
- UX para chatbots e copilotos: divulgação de limites, recuperação, escalonamento, acessibilidade e confiança calibrada;
- uso de GenAI no ciclo de desenvolvimento: requisitos, implementação, testes, revisão e qualidade de software;
- otimização de infraestrutura e FinOps: cache, roteamento, orçamento, capacidade, custo e qualidade;
- gestão de portfólio e conformidade: intake, priorização, catálogo, exceções e evidências;
- tendências e futuro: mudanças emergentes avaliadas por impacto arquitetural, não por popularidade.

## Projeto final em grupo

Grupos projetam uma solução para um caso realista ou trazido pela organização, explorando de forma comparativa ferramentas e plataformas. A entrega deve conter:

1. hipótese de valor, requisitos, restrições e atributos de qualidade;
2. arquitetura e ADRs que expliquem alternativas descartadas;
3. matriz comparativa de ao menos duas opções de ferramenta/plataforma, incluindo uma rota sem cartão quando aplicável;
4. protótipo, experimento reproduzível ou avaliação baseada em artefatos fornecidos;
5. conjunto de evidências: qualidade, segurança, UX, custo, operação e limites;
6. estratégia de governança, evolução e decisão de adoção.

A avaliação privilegia a qualidade da justificativa, da evidência e do reconhecimento de limites. Uso de ferramenta paga não acrescenta pontos.

## Mudanças previstas no site

- Revisar o plano de disciplina, objetivos, programação e rubricas.
- Acrescentar a cada módulo uma página ou seção de oficina, com pré-requisitos, rotas de acesso, exercício e evidência esperada.
- Ampliar os conteúdos conceituais relevantes e a navegação do MkDocs.
- Criar páginas de apoio para catálogo de ferramentas, matriz de seleção e guia do projeto final.
- Manter testes de conteúdo, referências e construção estrita do site.

## Critérios de aceite

1. As seis oficinas são coerentes com o tema conceitual de seu encontro e têm objetivos Bloom explícitos.
2. Todas as atividades obrigatórias possuem uma rota declarada sem cartão de crédito.
3. Opções comerciais são apresentadas como alternativas, com transparência de pré-requisitos e custo.
4. O projeto final exige comparação de ferramentas e evidência arquitetural, sem premiar gasto financeiro.
5. A ementa ampliada cobre explicitamente plataformas/bibliotecas, UX, SDLC, AIaaS/gateway, infraestrutura/portfólio e tendências.
