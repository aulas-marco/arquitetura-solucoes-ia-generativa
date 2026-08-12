# Coesão arquitetural do Módulo 3 — desenho

**Data:** 2026-07-25  
**Status:** aprovado para especificação e revisão docente

## Objetivo

Reforçar as páginas de conceitos e padrões de RAG como decisões arquiteturais contextuais, mensuráveis e evolutivas.

## Alterações

1. Corrigir a formulação de RAG básico: o padrão pode preservar proveniência, mas não a garante.
2. Inserir matriz de características prioritárias, tensões aceitas, medidas e responsáveis para recuperação.
3. Distinguir estratégias de recuperação e composição de estilos arquiteturais completos.
4. Explicitar responsabilidades e acoplamentos entre política, recuperador, montador de contexto, ranking, validação e adaptadores.
5. Aplicar hospedado versus autogerido e construir, comprar ou compor a índice, embeddings, reranking e observabilidade.
6. Nomear fitness functions para autorização, atualização, qualidade de recuperação e promoção de versões.

## Limites

- Modificar apenas `docs/modulo-3-rag/conceitos.md` e `docs/modulo-3-rag/padroes-e-decisoes.md`.
- Preservar os dois pipelines, os padrões existentes e a orientação independente de fornecedor.
- Não transformar estratégias de RAG em receita universal.

## Verificação

Executar `python scripts/validate_content.py --all`, `python -m pytest -q` e `mkdocs build --strict`.
