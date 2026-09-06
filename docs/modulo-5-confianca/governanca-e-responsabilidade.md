# Governança e responsabilidade

Quem responde por cada parte de um sistema composto, como a governança acompanha mudanças e quando a decisão sai da engenharia.

## Responsabilidade compartilhada, papéis identificáveis

**Responsabilidade compartilhada** descreve dependências entre participantes; não permite que todos sejam genericamente responsáveis e ninguém responda. Uma matriz mínima diferencia:

| Papel | Responsabilidade principal | Não pode presumir |
|---|---|---|
| fornecedor de modelo ou serviço | documentar interface, mudanças, compromissos e controles contratados | que o cliente usará o serviço em finalidade adequada |
| plataforma de IA | identidade, gateway, versões, telemetria, limites e integrações comuns | que um controle comum conhece toda regra do domínio |
| equipe de produto | contexto de uso, experiência, testes ponta a ponta e fallback | que desempenho de benchmark representa seus usuários |
| segurança e privacidade | ameaças, requisitos, revisão, incidentes e tratamento de dados | que revisão pontual mantém o sistema seguro após mudanças |
| dono do processo | política, autoridade, impacto, escalonamento e risco residual | que a equipe técnica pode aceitar risco em seu nome |
| operação | saúde, alertas, resposta e evidências | que toda resposta plausível é correta |
| usuário e aprovador | usar dentro da finalidade e revisar com informação suficiente | que a interface ou o modelo substituem responsabilidade institucional |

Contratos com fornecedores definem disponibilidade, uso de dados, localização, subprocessadores, notificação, portabilidade e encerramento. Porém contrato não impede tecnicamente uma injeção nem valida a política de RH. Controles técnicos, operacionais e contratuais se complementam.

## Fronteiras de responsabilidade

A **recuperação** seleciona evidência autorizada, mas não decide regra de domínio; o **guardrail** detecta ou limita um desvio, mas não aceita risco residual; a **política de domínio** determina uso permitido; a **avaliação** produz evidência, mas não aprova lançamento; o **dono do processo** aceita ou rejeita o risco com apoio de segurança, privacidade e operação; e a **observabilidade** registra evidência minimizada, sem se tornar memória ou retenção irrestrita. Essas fronteiras permitem alterar um modelo, avaliador ou fornecedor sem transferir autoridade a eles.

Separar responsabilidades acrescenta integração e operação. A fronteira se justifica quando protege ativo, isola privilégio, permite ciclo de mudança próprio ou torna uma característica arquitetural verificável.

## Governança que acompanha mudanças

Um **catálogo** registra caso de uso, finalidade, públicos, proprietário, criticidade, modelos, fontes, ferramentas, fornecedores, classes de dados, controles, métricas e status. Catálogo sem reconciliação com o ambiente vira inventário histórico; automatize referências a implantações e revise divergências.

**Versionamento** precisa abranger o pacote comportamental: modelo, parâmetros, prompt, política, corpus, pipeline de indexação, avaliadores, critérios de avaliação, ferramentas e dependências. Uma versão permite reproduzir a configuração, não necessariamente repetir a mesma saída probabilística. Preserve sementes quando suportadas, entradas e faixas de variação.

**Auditoria** registra quem aprovou finalidade, mudança, acesso, exceção e risco residual, além das decisões de execução relevantes. Log imutável ajuda a detectar alteração; não comprova que o evento registrado foi correto. Proteja a própria trilha, separe funções e teste consultas de investigação.

A **política de uso** declara usuários, finalidades, dados, ações, proibições, revisão humana, comunicação de limites, escalonamento e consequências de desvio. Publique-a na interface e transforme itens executáveis em política técnica. Texto sozinho depende de adesão; controle técnico sozinho não cobre julgamento e contexto social.

O [ISO/IEC 42001:2023](https://www.iso.org/standard/42001) especifica requisitos para um sistema de gestão de IA quando uma organização escolhe adotá-lo ou buscar conformidade. Ele não prescreve uma arquitetura única nem certifica cada resposta. O NIST AI RMF permanece voluntário. Neste curso, catálogo, pacote de versões e portões de avaliação são recomendações arquiteturais para materializar governança; não devem ser apresentados como cláusulas literais desses documentos.

## Plataforma e obtenção de capacidade

Telemetria, gateway, avaliação, armazenamento de traces e guardrails podem ser hospedados, autogeridos ou compostos. Serviço hospedado acelera capacidade, mas desloca fronteiras de dados, versões, disponibilidade, portabilidade e resposta a incidente; operação autogerida amplia controle e assume escala, atualização, segurança e plantão. **Construir** é justificável para política de domínio, regras diferenciadoras ou integração que concentra risco; **comprar** atende capacidade padronizada; **compor** permite combinar identidade corporativa, controles próprios e observabilidade compartilhada. Compare custo total, risco residual, evidência de saída e responsabilidades contratuais antes de delegar uma capacidade de confiança.

## Critério de decisão

Para cada controle, registre: cenário tratado, camada, proprietário, configuração, evidência de teste, cobertura conhecida, falsos positivos, dependências, modo de falha e risco residual. Evite afirmar “bloqueia prompt injection”. Prefira: “reduziu esta família de ataques de 62% para 9% no conjunto v4, ainda falhou em conteúdo codificado e, por isso, escrita permanece mediada por política e aprovação”. Essa linguagem sustenta decisão e aprendizagem.

Veja os controles aplicados a um fluxo real em [Exemplo arquitetural](exemplo-arquitetural.md).
