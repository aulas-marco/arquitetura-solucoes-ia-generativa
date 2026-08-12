# Coesão arquitetural do Módulo 6 — desenho

**Data:** 2026-07-25  
**Status:** aprovado para implementação

## Objetivo

Consolidar a operação de sistemas generativos como disciplina de características arquiteturais priorizadas, fronteiras de responsabilidade, fitness functions e decisões explícitas de plataforma.

## Alterações

1. Inserir matriz de disponibilidade, segurança, privacidade, confiabilidade, latência, custo, auditabilidade e modificabilidade, com prioridade, tensão, medida e responsável.
2. Consolidar fitness functions para manifesto, trace, bypass, fallback, rollback e ensaio de recuperação.
3. Distinguir mecanismos comuns de plataforma das decisões que permanecem com produto e domínio.
4. Tornar explícita a decisão entre capacidade hospedada, autogerida e composta.
5. Propagar os critérios para exemplo, estudo de caso, oficina, exercícios e síntese.

## Limites

- Preservar o modelo de plataforma como caminho preferencial, não centralização obrigatória.
- Não apresentar SLO, gateway, fallback ou multimodelo como garantias universais.
- Manter as decisões independentes de fornecedor e o foco em risco residual.

## Verificação

Executar validação de conteúdo, suíte Python e build estrito do MkDocs.
