# Confiança, segurança, avaliação e governança

![Quatro riscos alimentam risco inerente; controles em camadas produzem risco residual, rastreabilidade, papéis e avaliação](../assets/images/m05-mapa-confianca-sistemica.png "Mapa da confiança sistêmica")

*Figura — Confiança combina riscos, controles, responsabilidades e evidências.*

## Pergunta orientadora

> **Como demonstrar que uma solução generativa é suficientemente confiável para seu contexto?**

Confiança começa com contexto delimitado, pessoas afetadas, eventos indesejados, responsabilidades e critérios observáveis. Um assistente de RH pode responder corretamente sobre férias e ainda ser inadequado se revelar salário, obedecer a instruções escondidas, reter dados sem prazo ou impedir escalonamento. Qualidade da frase é apenas parte da confiança do sistema.

Neste módulo, **confiável** não significa infalível. Significa que os riscos relevantes foram identificados; que atributos como fundamentação, segurança, latência e custo têm critérios proporcionais ao uso; que controles independentes reduzem probabilidade ou impacto; que o risco residual foi aceito por quem tem autoridade; e que existem evidências para revisar a decisão. A pergunta correta não é “este modelo é seguro?”, mas “esta configuração, integrada a estas fontes e ferramentas, operada por estas pessoas, é suficientemente controlada para este público e esta finalidade?”.

**Tempo estimado de leitura:** 60–90 minutos, sem contar o estudo de caso e os exercícios de projeto.

## O que você aprenderá

Ao final, você deverá conseguir:

1. explicar confiança como propriedade sistêmica e contextual, não como selo do modelo;
2. relacionar riscos técnicos, operacionais, legais e reputacionais aos afetados e às responsabilidades;
3. modelar injeção de prompt, vazamento, abuso de ferramentas, memória contaminada, consumo econômico e cadeia de fornecedores;
4. distribuir guardrails entre entrada, contexto, recuperação, ferramenta, saída e aprovação humana;
5. especificar minimização, retenção, segregação, catálogo, versionamento, auditoria e política de uso;
6. decompor qualidade em factualidade, relevância, fundamentação, segurança, utilidade, latência e custo;
7. combinar verificações determinísticas, critérios humanos e avaliação assistida por modelo sem confundir uma delas com verdade;
8. construir conjuntos de referência e casos adversariais para componentes e fluxos ponta a ponta;
9. julgar risco residual e defender uma arquitetura de confiança com evidências.
10. priorizar características arquiteturais, declarar tensões, atribuir responsáveis e definir fitness functions para controles críticos.

## Continuidade com RAG, agentes e atributos de qualidade

O [Módulo 3](../modulo-3-rag/index.md) separou ingestão e consulta, propagou autorização até a recuperação e tratou conteúdo recuperado como evidência. Aqui acrescentamos uma hipótese hostil: a fonte autorizada também pode estar comprometida, conter instruções maliciosas ou induzir a resposta a revelar outro dado. Autorização responde “quem pode ler”; não prova integridade, veracidade ou segurança do texto.

O [Módulo 4](../modulo-4-agentes/index.md) separou geração, decisão e ação. Aqui examinamos como um atacante ou uma falha pode atravessar essas fronteiras. Saída estruturada não garante intenção correta; aprovação humana não é barreira se o aprovador recebe contexto enganoso; uma ferramenta com escopo estreito ainda pode causar dano quando repetida ou usada sobre o recurso errado.

Os cenários de [atributos de qualidade](../referencia/atributos-de-qualidade.md) transformam palavras amplas em estímulo, ambiente, resposta e medida. Segurança, privacidade, explicabilidade, confiabilidade e autonomia interagem: aumentar filtragem pode reduzir utilidade; registrar mais conteúdo pode ajudar auditoria e ferir minimização; usar um avaliador adicional pode elevar custo e reproduzir o viés do modelo avaliado. Arquitetura torna essas tensões explícitas.

## Quatro compromissos do módulo

Primeiro, **nenhum controle isolado é prova de segurança**. Classificador de entrada, prompt de sistema, filtro de saída e aprovação humana cobrem falhas diferentes e todos têm falsos negativos, falsos positivos ou caminhos de contorno.

Segundo, **avaliação é multidimensional**. Uma média de qualidade pode esconder vazamento raro e grave. Dimensões críticas usam critérios de bloqueio; dimensões otimizáveis usam metas e comparação. O conjunto deve representar casos comuns, difíceis, adversariais e de recusa apropriada.

Terceiro, **governança produz decisões e evidências**, não apenas documentos. Proprietários, versões, autorizações, exceções, retenção e auditoria precisam aparecer no fluxo de mudança e operação.

Quarto, **responsabilidade é compartilhada, mas não diluída**. Fornecedor, plataforma, equipe de produto, segurança, dados, jurídico, operação, dono do processo e usuários têm parcelas distintas. “O modelo decidiu” nunca é um proprietário aceitável.

## Mapa do módulo

| Etapa | Página | Foco |
|---|---|---|
| 1 | [Abertura](index.md) | contrato de confiança contextual |
| 2 | [Confiança sistêmica e risco](confianca-e-risco.md) | confiança sistêmica, quatro famílias de risco e risco residual |
| 3 | [Ameaças e guardrails](ameacas-e-guardrails.md) | ameaças em RAG e agentes, defesa em camadas e o que ela não garante |
| 4 | [Rastreabilidade e privacidade](rastreabilidade-e-privacidade.md) | escopo mínimo de trace e privacidade por ciclo de vida |
| 5 | [Qualidade multidimensional e medição](qualidade-e-medicao.md) | sete dimensões, duas camadas de medição e tensões prioritárias |
| 6 | [Governança e responsabilidade](governanca-e-responsabilidade.md) | papéis identificáveis, governança de mudança e critério de decisão |
| 7 | [Exemplo arquitetural](exemplo-arquitetural.md) | modelo de ameaças e pipeline de avaliação |
| 8 | [Estudo de caso](estudo-de-caso.md) | RH, escalonamento e critérios de liberação |
| 9 | [Oficina de ferramentas](oficina-de-ferramentas.md) | avaliação, guardrails e experiência recuperável |
| 10 | [Exercícios](exercicios.md) | ameaças, controles, risco residual e projeto |
| 11 | [Síntese e referências](sintese-e-referencias.md) | checklist, autoavaliação e fontes |

Comece por [Confiança sistêmica e risco](confianca-e-risco.md): antes de escolher controles, precisamos definir o que deve ser confiável, para quem e mediante quais evidências. A [Oficina de ferramentas](oficina-de-ferramentas.md) permite testar essas decisões com casos sintéticos em um laboratório local.
