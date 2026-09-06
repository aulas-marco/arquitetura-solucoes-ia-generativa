# Ferramentas e tool calling

Uma ferramenta é uma capacidade exposta por interface controlada. O que o modelo produz é uma solicitação, e o contrato decide se ela vira chamada.

## Uso de ferramentas e saídas estruturadas

Uma **ferramenta** é uma capacidade exposta ao modelo por uma interface controlada. Pode consultar CRM, calcular frete ou solicitar alteração de pedido. O modelo não deveria montar SQL livre, escolher credenciais nem chamar diretamente qualquer endpoint. Ele produz uma **solicitação de ferramenta**; o orquestrador valida esquema, política, identidade, orçamento e estado antes de executar.

Uma **saída estruturada** restringe a forma, por exemplo a um objeto com `tool_name`, `arguments` e `justification_code`. Esquema válido reduz ambiguidade sintática, mas não garante semântica, autorização ou segurança. `quantidade: 1000` pode ser inteiro válido e ainda violar política. O estudo [Toolformer](https://proceedings.neurips.cc/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html) é uma fonte primária sobre modelos aprendendo a usar ferramentas; em produção corporativa, capacidade de seleção precisa ser cercada por contratos e execução mediada.

## Comece pelo contrato de ferramenta

Um **contrato de ferramenta** transforma uma capacidade corporativa em operação estreita, validável e auditável. “Acesso ao sistema de pedidos” é amplo demais. Prefira operações como `consultar_pedido`, `reservar_item` e `solicitar_cancelamento`, cada uma com efeito e política próprios.

O contrato mínimo declara:

| Campo | Pergunta que responde |
|---|---|
| nome, versão e finalidade | que capacidade está sendo invocada e por quê? |
| classe de efeito | é leitura, proposta, escrita reversível ou efeito irreversível? |
| esquema de entrada | tipos, obrigatoriedade, limites, enumerações e identificadores aceitos? |
| esquema de saída | dados, proveniência, versão do recurso e indicador de conclusão? |
| erros tipados | inválido, não autorizado, conflito, não encontrado, transitório ou definitivo? |
| identidade e autorização | quem age em nome de quem, com quais escopos e política? |
| idempotência e concorrência | qual chave evita duplicação e qual versão/precondição evita sobrescrita? |
| timeout e retry | quando desistir e quais erros permitem nova tentativa? |
| dados e auditoria | quais campos são sensíveis, mascarados, retidos e correlacionados? |
| compensação | como desfazer ou neutralizar o efeito, e quando isso é impossível? |

Descrições para o modelo incluem uso e não uso, mas o executor aplica as regras. O [Model Context Protocol](https://modelcontextprotocol.io/specification/2025-11-25) oferece uma especificação oficial de interoperabilidade entre aplicações e servidores que expõem contexto e ferramentas. Um protocolo padroniza comunicação; não decide política corporativa, semântica de transação ou adequação da ferramenta.

## Reduzir o espaço de decisão antes de trocar o modelo

Quando um agente erra a escolha de ferramenta, a reação usual é ampliar o catálogo ou trocar por um modelo maior. As duas movimentações são caras e frequentemente pioram o resultado. A ordem de investigação que este curso recomenda vai na direção oposta, do mais barato para o mais caro:

1. **remover ferramentas**, consolidando as que compartilham fronteira, até que uma pessoa da equipe consiga dizer sem hesitar qual ferramenta cabe em cada situação;
2. **descrever** as que restaram, com contrato, pré-condição e efeito, em vez de expor nomes parecidos sem definição;
3. **restringir o contexto** ao recorte necessário para a etapa corrente, carregando definições sob demanda;
4. **acrescentar verificação** determinística antes do efeito, com o motivo da recusa devolvido ao modelo;
5. só então **avaliar troca de modelo**, com o mesmo conjunto de casos e o mesmo arnês.

A justificativa está em [Mais ferramentas não significa menos erro](arnes.md#mais-ferramentas-nao-significa-menos-erro) e o efeito de cada passo é mensurável: a [oficina deste módulo](oficina-de-ferramentas.md#extensao-ablacao-de-arnes) executa exatamente essa sequência com o mesmo modelo local e mede a diferença.

A regra tem um limite que precisa ficar explícito. Remover ferramenta não é remover capacidade do sistema; é mover capacidade para fora do espaço de decisão do modelo. A operação que a Vercel fez foi substituir dezesseis ferramentas por uma capacidade mais geral, com isolamento, e não simplesmente amputar funções do produto. Uma remoção que deixe uma jornada sem caminho não melhorou nada, apenas empurrou o problema para o atendimento humano sem registrar a decisão.

## APIs, mensageria, eventos e adaptadores

Use **API síncrona** quando o agente precisa do resultado para escolher o próximo passo e a dependência responde dentro do orçamento. O contrato deve definir timeout menor que o prazo total, erros e correlação. Não mantenha uma interação bloqueada indefinidamente.

Use **mensageria** para comandos assíncronos, filas de trabalho e absorção de picos. O envio aceito não significa efeito concluído. Estado precisa distinguir `solicitado`, `aceito`, `processando`, `concluído` e `falhou`; uma resposta posterior correlaciona `execution_id` e `command_id`.

Use **eventos** para comunicar fatos ocorridos — `ReservaExpirada`, não “talvez reserve”. Consumidores assumem entrega pelo menos uma vez, ordenação limitada e evolução de esquema. Deduplicação é responsabilidade do consumidor. Evento não deve carregar dado sensível além do necessário.

Um **adaptador** protege o domínio de protocolos legados, campos instáveis e códigos opacos. Traduz contrato canônico para SOAP, arquivo, terminal ou API antiga; normaliza erros; aplica timeout; correlaciona chamadas; e impede que peculiaridades do legado entrem no prompt. Quando o legado não oferece idempotência, o adaptador pode usar registro transacional próprio, consulta de reconciliação e chave de negócio — ou classificar a ação como não repetível e exigir intervenção.
