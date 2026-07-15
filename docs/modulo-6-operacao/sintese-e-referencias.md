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

## Autoavaliação

1. Consigo reproduzir o pacote comportamental promovido?
2. Ligo cada métrica a hipótese, decisão e responsável?
3. Distingo parada segura de experimento e incidente real?
4. Projeto fallback e rollback que preservam controles essenciais?
5. Delimito capacidades comuns, autonomia local e raio de impacto?
