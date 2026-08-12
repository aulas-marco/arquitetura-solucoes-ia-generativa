# Coesão arquitetural do Módulo 4 — desenho

**Data:** 2026-07-25  
**Status:** aprovado para especificação e revisão docente

## Objetivo

Tornar as decisões de autonomia do Módulo 4 explicitamente orientadas por características arquiteturais, trade-offs, modularidade, governança contínua e responsabilidade operacional.

## Alterações

1. Inserir matriz de autonomia, segurança, confiabilidade, auditabilidade, latência, custo e modificabilidade com prioridade, tensão, medida e responsável.
2. Adicionar fitness functions para política válida, idempotência, aprovação imutável, prevenção de repetição e compensação pendente.
3. Explicitar responsabilidades e dependências proibidas entre planejador, executor, política, estado, aprovação, catálogo e telemetria.
4. Aplicar hospedado versus autogerido e construir, comprar ou compor a orquestração, estado, identidade, observabilidade e ferramentas.
5. Ajustar títulos para formulações diretas, sem alterar o conteúdo técnico ou o escopo do módulo.

## Limites

- Modificar apenas `docs/modulo-4-agentes/conceitos.md` e `docs/modulo-4-agentes/padroes-e-decisoes.md`.
- Preservar a matriz de autonomia, o conteúdo de SDD e a independência de fornecedor.
- Não apresentar agente como padrão universal.

## Verificação

Executar validação de conteúdo, suíte Python e build estrito do MkDocs.
