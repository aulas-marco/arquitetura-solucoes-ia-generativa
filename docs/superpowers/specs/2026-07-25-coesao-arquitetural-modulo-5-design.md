# Coesão arquitetural do Módulo 5 — desenho

**Data:** 2026-07-25  
**Status:** aprovado para implementação

## Objetivo

Explicitar como confiança sistêmica é governada por características arquiteturais priorizadas, fronteiras de responsabilidade, fitness functions e decisões de plataforma, sem reduzir risco a um controle, métrica ou fornecedor.

## Alterações

1. Inserir matriz de segurança, privacidade, auditabilidade, confiabilidade, utilidade, latência, custo e modificabilidade, com prioridade, tensão, medida e responsável.
2. Adicionar fitness functions para autorização, versões avaliadas, escalonamento obrigatório, rastreabilidade minimizada e mudança de dependência.
3. Delimitar responsabilidades entre recuperação, guardrails, política de domínio, avaliação, aprovação de liberação e observabilidade.
4. Completar a decisão de serviços hospedados, componentes autogeridos e composição de capacidades de confiança.
5. Propagar os critérios para exemplo, caso, oficina, exercícios e síntese.

## Limites

- Preservar os referenciais NIST, OWASP e ISO como orientação, sem alegar certificação.
- Não tratar guardrails, avaliação ou fornecedor como garantias universais.
- Manter a progressão pedagógica e os cenários existentes.

## Verificação

Executar validação de conteúdo, suíte Python e build estrito do MkDocs.
