# Coesão arquitetural do Módulo 2 — desenho

**Data:** 2026-07-25
**Status:** aprovado para especificação e revisão docente

## Objetivo

Tornar o Módulo 2 explicitamente aderente à lente de arquitetura de Richards e Ford: decisões contextuais, características arquiteturais priorizadas, trade-offs, responsabilidades de componentes, governança por evidência e evolução reversível.

## Alterações

1. Alinhar `index.md` e `padroes-e-decisoes.md`: incluir novamente as decisões hospedado versus autogerido e construir, comprar ou compor, ou removê-las da promessa didática. A opção escolhida é incluí-las, pois já constam dos objetivos e do caso.
2. Reorganizar a progressão de decisão como perguntas arquiteturais: gerar, fundamentar com conhecimento externo, agir, conceder autonomia, definir fronteiras de plataforma e produzir evidência. Cada pergunta apresentará direcionadores, alternativas, consequências e gatilhos de revisão.
3. Inserir uma matriz concisa de características arquiteturais: prioridade, tensão aceita, medida e responsável, usando segurança, privacidade, proveniência, latência, custo, confiabilidade e modificabilidade.
4. Explicitar responsabilidades, coesão e acoplamento entre orquestrador, adaptadores, gateway, montador de contexto e validação; relacionar mudanças locais aos limites de componente.
5. Tratar gateway e chassi como alternativas condicionadas, incluindo custos de centralização, acoplamento, fila de evolução e ponto de falha.
6. Corrigir a taxonomia de estilos e capacidades de plataforma: monólito modular, serviços distribuídos e capacidades compartilhadas não serão apresentados como opções equivalentes.

## Limites

- Preservar os cenários, o exemplo Banco Lume e a estrutura de exercícios.
- Alterar apenas conteúdo necessário para coerência: `index.md`, `conceitos.md`, `padroes-e-decisoes.md`, `exemplo-arquitetural.md`, `estudo-de-caso.md`, `exercicios.md` e `sintese-e-referencias.md`.
- Não apresentar estilo, padrão ou produto como solução universal.

## Verificação

- Executar o validador de conteúdo, a suíte Python e o build estrito do MkDocs.
- Revisar que cada decisão nova apresenta ao menos um trade-off, uma consequência e uma evidência ou gatilho de revisão.
