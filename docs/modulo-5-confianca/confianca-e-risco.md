# Confiança e risco

Confiança é expectativa justificada num contexto definido, não selo do modelo. Daí saem as quatro famílias de risco e a noção de risco residual com dono.

## Confiança é uma relação, não uma característica absoluta

**Confiança sistêmica** é a expectativa justificada de que uma solução, em um contexto definido, produzirá resultados aceitáveis, limitará danos previsíveis e permitirá detectar, explicar e corrigir desvios. Ela depende da composição entre modelo, dados, recuperação, prompts, código, ferramentas, identidade, políticas, interfaces, pessoas, fornecedores e operação. Um modelo pode sugerir títulos, mas não decidir elegibilidade.

“Justificada” exige evidência. Demonstrações escolhidas pela equipe, ausência de incidentes conhecidos ou reputação do fornecedor são sinais fracos. Evidências melhores incluem cenários de risco, testes reproduzíveis, conjunto de referência representativo, resultados por dimensão, revisão independente, traces minimizados, incidentes, limites de uso e decisão formal sobre risco residual. Ainda assim, evidência reduz incerteza; não prova ausência de falhas futuras.

O [AI Risk Management Framework 1.0 do NIST](https://doi.org/10.6028/NIST.AI.100-1) organiza a gestão de risco em Govern, Map, Measure e Manage; seu [perfil de IA generativa](https://doi.org/10.6028/NIST.AI.600-1) aplica essa visão aos riscos generativos. Ambos orientam raciocínio, não certificam sistemas; limiares pertencem ao contexto organizacional.

## Quatro famílias de risco que se reforçam

**Risco técnico** nasce de propriedades ou falhas da solução: resposta falsa, recuperação inadequada, injeção de prompt, permissão incorreta, indisponibilidade, modelo alterado, filtro contornado ou trace incompleto. A causa pode estar longe do efeito. Uma configuração de indexação pode trazer a política errada; um documento malicioso pode induzir uma chamada; um fallback pode remover a fundamentação.

**Risco operacional** envolve processo, pessoas e capacidade de sustentar o controle: alertas sem responsável, fila de aprovação saturada, conjunto de testes desatualizado, credencial não rotacionada, incidente sem procedimento, mudança urgente fora do pipeline ou fornecedor indisponível. Um desenho seguro no papel deixa de ser confiável se a organização não consegue operá-lo.

**Risco legal** envolve obrigações aplicáveis a dados, relações de trabalho, propriedade intelectual, discriminação, contratos, registros e prestação de contas. A arquitetura não interpreta sozinha a lei. Ela deve permitir que especialistas traduzam obrigações em finalidade, base autorizativa, acesso, retenção, contestação, evidência e restrição de uso. Um filtro de dados pessoais não torna automaticamente o tratamento lícito.

**Risco reputacional** é a perda de confiança de empregados, clientes, parceiros ou sociedade. Pode decorrer de uma falha técnica, mas também de expectativa mal administrada: interface que aparenta autoridade, resposta sem fonte, automação opaca ou comunicação tardia de incidente. Reputação não é apenas “imagem”; afeta adoção, cooperação e legitimidade do serviço.

As famílias não formam silos. Um vazamento técnico pode gerar investigação legal, interrupção operacional e dano reputacional. Por isso o registro de risco deve relacionar causa, ativo, parte afetada, cenário, probabilidade, impacto, controles, proprietário e risco residual.

## Do perigo ao risco residual

Um **ativo** é algo que precisa ser protegido ou preservado: dado pessoal, segredo, integridade de uma política, identidade, orçamento, disponibilidade, decisão humana ou confiança do empregado. Uma **ameaça** é uma causa potencial de incidente; uma **vulnerabilidade** é a condição explorável; um **evento** é a materialização; um **impacto** é a consequência para pessoas e organização.

O **risco inerente** é avaliado antes dos controles. O **risco residual** permanece depois que controles e condições operacionais são considerados. Controles podem reduzir probabilidade, limitar impacto, aumentar detecção ou facilitar recuperação. Nenhum número elimina a necessidade de justificar premissas. “Baixo” precisa dizer para quem, em qual período e sob qual exposição.

> **Risco arquitetural:** Aceitar risco residual é decisão de negócio e governança, não preferência do desenvolvedor. O proprietário precisa ter autoridade, compreender incerteza, registrar prazo e definir gatilhos de revisão. Risco acima do apetite requer reduzir escopo, acrescentar controle, transferir parte do risco, suspender ou não lançar. A aceitação expira quando mudam modelo, fontes, ferramentas, público, finalidade, ameaça ou obrigação.

## Modele ativos, atores e fronteiras antes de escolher produtos

Um modelo de ameaças começa no fluxo concreto. Liste usuários legítimos, atacantes externos, autores de documentos, administradores, fornecedores e serviços comprometidos. Marque ativos, entradas controláveis, fronteiras de confiança, mudanças de privilégio e efeitos. Para cada cenário, descreva precondição, percurso, impacto, prevenção, detecção, resposta e risco residual. Uma lista genérica de riscos ajuda a descobrir cenários, mas não substitui esse mapa.

O [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/) é orientação comunitária de segurança e um vocabulário útil, não prova de conformidade. O [perfil SSDF para IA generativa do NIST](https://doi.org/10.6028/NIST.SP.800-218A) estende práticas de desenvolvimento seguro a modelos e componentes generativos. Nenhum documento conhece, sozinho, as permissões, impactos e atacantes do seu sistema.
