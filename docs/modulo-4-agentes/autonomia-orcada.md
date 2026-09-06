# Níveis de autonomia

Autonomia não é propriedade binária nem virtude: é uma concessão por ação, com orçamento, aprovação e caminho de volta.

## Características e tensões da autonomia

| Característica | Prioridade | Tensão aceita | Medida e responsável |
|---|---|---|---|
| Segurança e autorização | Não negociável | validação adicional aumenta latência | ação material sem política válida: zero; Segurança |
| Confiabilidade | Alta | idempotência e compensação aumentam estado | efeitos duplicados e compensações pendentes; Operações |
| Auditabilidade | Alta | trace retém metadados técnicos | execução reconstruível por versão; Auditoria |
| Latência e custo | Importante | orçamento pode limitar autonomia | p95, chamadas e custo por execução; Produto e plataforma |
| Modificabilidade | Importante | adaptadores e contratos acrescentam componentes | troca localizada e teste de contrato; Arquitetura |

Autonomia adequada é a que atende essas prioridades no cenário, não a que maximiza o número de ferramentas ou etapas escolhidas pelo modelo.

## Matriz de autonomia

Autonomia é atribuída por **ação e cenário**, não por produto inteiro. Os níveis abaixo não são uma escada obrigatória:

| Nível | Escolha do modelo | Efeito | Controle humano | Exemplo |
|---|---|---|---|---|
| A0 — sem autonomia | nenhuma | regra executa fluxo conhecido | responsável define processo | cálculo e consulta determinística |
| A1 — informar | gera resposta, sem ferramenta de efeito | nenhum | usuário interpreta | chatbot de políticas |
| A2 — recomendar | escolhe proposta ou ferramenta de leitura | pessoa executa | revisão antes de qualquer efeito | copiloto sugere troca |
| A3 — agir reversivelmente | escolhe leitura e escrita de baixo risco | reversível e limitada | aviso/contestação; amostra depois | criar reserva temporária |
| A4 — agir com aprovação | propõe ação material e aguarda | efeito após aprovação antes da ação | aprovador recebe evidência, parâmetros e prazo | cancelar pedido elegível |
| A5 — autonomia limitada | escolhe sequência e ações aprovadas por classe | efeitos dentro de limites estreitos | monitoramento e revisão humana depois da ação | ajuste operacional de baixo valor |

**Aprovação humana antes da ação** precisa ocorrer sobre objeto imutável: ferramenta, parâmetros, evidência, consequência, prazo e chave. Alterar parâmetros invalida aprovação. Aprovar “faça o necessário” não é controle.

**Revisão humana depois da ação** detecta desvio, corrige política e permite recurso; não retroativamente autoriza dano. Só serve quando o efeito é aceitável, reversível ou de baixo risco. Amostragem, alertas e prazo de contestação devem ser definidos. Ação crítica continua exigindo aprovação prévia, como pede o cenário de [Autonomia](../referencia/atributos-de-qualidade.md#autonomia).

## Orçamentos, interrupção e fallback

Um agente recebe **orçamento de etapas**, **orçamento de tempo** e **orçamento de custo**, além de limites de tokens, chamadas e ações de efeito. O contador é externo ao modelo e inclui retries, handoffs e compensações. Limites diferentes podem valer por classe de tarefa. Ao se aproximar do teto, o sistema resume estado, evita nova ação material e escolhe conclusão parcial, solicitação de dado, pausa ou escalonamento.

O fallback para **workflow determinístico** é uma rota projetada: por exemplo, coletar pedido e motivo, validar regras conhecidas e abrir tarefa humana. Não entregue silenciosamente a mesma ação a um modelo mais barato ou ferramenta alternativa com política diferente. Fallback preserva identidade, estado, idempotência e informação clara sobre o que não foi concluído.

## Fitness functions para autonomia

Fitness functions verificam continuamente se a autonomia permanece dentro do contrato:

- toda ação material possui decisão de política válida, identidade delegada e chave de idempotência;
- aprovação referencia ferramenta, parâmetros, evidência, prazo e versão de estado imutáveis;
- repetição da mesma ferramenta com argumentos canônicos e estado idêntico interrompe a trajetória;
- execução em `compensation_pending` permanece aberta e alerta Operações até reconciliação;
- trace contém versões de política, ferramenta, estado e resultado, sem conteúdo sensível além da retenção permitida.

Falha em uma dessas verificações bloqueia promoção de versão, reduz autonomia ou encaminha o caso para workflow humano, conforme risco.

## Plataforma e obtenção de capacidade

Orquestração, estado, identidade, telemetria e catálogo de ferramentas podem ser hospedados, autogeridos ou compostos. Serviço hospedado acelera capacidade, mas cria fronteira de fornecedor para dados, disponibilidade, versões e portabilidade; operação autogerida amplia controle e assume escala, atualização, segurança e plantão. **Construir** faz sentido para políticas ou contratos diferenciadores; **comprar** acelera capacidade padronizada; **compor** permite combinar identidade corporativa, executor próprio e observabilidade compartilhada. Compare custo total, risco residual e evidência de saída antes de delegar uma responsabilidade operacional.

## Ferramentas no mercado

Compare contratos no [Guia de ferramentas](../referencia/guia-de-ferramentas.md).

| Ferramenta | Quando ajuda | Pré-requisito | Limite arquitetural |
|---|---|---|---|
| n8n | Desenhar workflow. | Ambiente, credenciais e dados sintéticos. | Não autoriza ações ou garante idempotência. |
| LangGraph | Modelar estado e retomada. | Schema, limites e ferramentas. | Não substitui política externa. |
| AutoGen | Testar papéis de agentes. | Protocolo, orçamento e catálogo mínimo. | Mais agentes não são aprovação. |

Com essa base, a pergunta passa de “o que é um agente” para “o que precisa existir em volta dele”: [Engenharia de arnês](arnes.md).
