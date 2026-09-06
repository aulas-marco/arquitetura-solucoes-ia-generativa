# Verificar e governar

O que substitui o teste determinístico quando a saída varia, e o contrato arquitetural que passa a valer a partir daí.

## Como verificar e governar

As zonas da composição pedem formas de verificação diferentes. Contratos e regras permitem asserções exatas. Saídas generativas exigem observação sobre conjuntos de casos. Propriedades como latência, isolamento e recuperação dependem do sistema em condições representativas.

### Três tipos de verificação

| Tipo | O que verifica | Exemplo |
|---|---|---|
| **Teste de software** | comportamento determinístico de contratos, regras e componentes | campo proibido é rejeitado; transação duplicada não é aplicada |
| **Avaliação comportamental** | distribuição de qualidade sobre uma população de casos | cobertura, fundamentação e recusa em conjunto representativo |
| **Verificação arquitetural** | característica sistêmica ao longo da evolução | p95, isolamento entre perfis, custo por jornada, recuperação de falha |

Uma **fitness function** é uma verificação automatizada e contínua de uma característica arquitetural. Ela pode impedir promoção quando latência, vazamento, fundamentação ou compatibilidade sai do limite. O mecanismo não substitui julgamento humano nem transforma uma métrica intermediária em objetivo de negócio.

### O novo contrato arquitetural

Sistemas generativos combinam zonas testadas por asserção e zonas avaliadas por amostragem. A arquitetura define fronteiras, responsabilidades, medidas e recuperação. O modelo oferece interpretação e geração; o sistema preserva identidade, finalidade, autorização, evidência e efeito.

Esse contrato organiza a continuidade do curso:

- o [Módulo 2](../modulo-2-desenho-conceitual/index.md) transforma oportunidade em descrição e decisão;
- o [Módulo 3](../modulo-3-rag/index.md) governa conhecimento externo;
- o [Módulo 4](../modulo-4-agentes/index.md) governa autonomia e efeitos;
- o [Módulo 5](../modulo-5-confianca/index.md) distribui controles e avaliação;
- o [Módulo 6](../modulo-6-operacao/index.md) governa mudança e operação da superfície comportamental.

Esses critérios são o que a [escolha da abordagem](escolha-da-abordagem.md) precisa sustentar, e reaparecem no [exemplo arquitetural](exemplo-arquitetural.md) como evidência exigida.

## Ponte para confiança e operação

Qualquer alternativa precisa responder a duas perguntas transversais. O [Módulo 5](../modulo-5-confianca/index.md) perguntará quais riscos, controles e avaliações tornam o uso aceitável. O [Módulo 6](../modulo-6-operacao/index.md) perguntará quais versões, fitness functions, rollouts e modos degradados preservam essa aceitação no tempo.

**Próxima página:** [Exemplo arquitetural — atendimento Horizonte](exemplo-arquitetural.md).
