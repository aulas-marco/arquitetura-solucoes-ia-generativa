# Oficina de ferramentas — comportamento de modelo e contexto

**Objetivo Bloom:** Compreender e Aplicar.

Esta oficina torna observável uma decisão estudada no módulo: que efeito o contexto fornecido e um parâmetro de geração podem ter no comportamento de uma resposta. Ela não mede a capacidade geral de nenhum modelo, produto ou provedor.

## Decisão arquitetural em foco

Ao escolher entre geração direta e uma resposta com contexto, a equipe precisa declarar que evidência envia ao modelo, qual limite de uso aceita e como observará a diferença. A **atividade guiada** produz uma comparação curta: ela não substitui uma avaliação representativa do produto.

Consulte o [Guia de ferramentas e plataformas](../referencia/guia-de-ferramentas.md) antes de escolher uma rota. As rotas usam categorias do guia; disponibilidade, limites e condições podem mudar.

## Roteiros equivalentes de acesso

### Essencial, sem cartão

Use uma interface de playground/assistente disponível sem cartão ou um executor local, se o seu equipamento o comportar. Caso a interface peça uma conta, siga somente as condições públicas aplicáveis à sua região; não use cartão, chave nem crédito. Se não houver execução disponível, faça a mesma comparação como análise manual dos três pedidos e registre o comportamento esperado e os limites. Esta rota não depende de cartão e é suficiente para a evidência obrigatória.

### Institucional

Use uma interface, laboratório ou ambiente institucional apenas se ele já tiver sido disponibilizado e autorizado. Não envie material da instituição: mantenha o prompt e o corpus sintéticos desta página. A rota institucional não acrescenta pontos; ela somente muda o ambiente em que a mesma evidência é produzida.

### Comercial ou avançada

Opcionalmente, use um assistente comercial ou uma API autorizada para repetir o procedimento, declarando que há potencial de cobrança, limites e envio de dados ao provedor. Chave própria, créditos e assinatura não são exigidos. A rota comercial ou avançada não acrescenta pontos e não deve ser usada como comparação de desempenho entre planos.

## Atividade guiada

A atividade obrigatória é a rota **Essencial, sem cartão** (ou sua análise manual equivalente); ela não depende de cartão. Trabalhe individualmente ou em dupla, com o texto sintético abaixo.

**Prompt comum:** `Qual é o prazo para solicitar reembolso? Responda em uma frase e informe a fonte quando ela estiver disponível.`

**Corpus sintético — Política Aurora de reembolso (versão de treinamento):**

> Solicitações de reembolso devem ser abertas em até 15 dias corridos após a compra. Para compras feitas durante campanhas especiais, o prazo é de 7 dias corridos. O atendimento deve indicar qual regra usou e pedir revisão humana se a data da compra não estiver disponível.

1. Envie apenas o prompt comum e registre a resposta **sem contexto**. Não acrescente fatos externos.
2. Envie o mesmo prompt seguido do corpus sintético e registre a resposta **com contexto**. Verifique se ela cita a regra de 15 dias, a exceção de 7 dias ou a ausência de data como limite.
3. Repita o segundo pedido, mudando somente um parâmetro controlável da ferramenta — por exemplo, a temperatura, quando a interface o expuser. Se ele não estiver exposto, mantenha o pedido idêntico e registre que a variação não é observável nessa rota. Não altere simultaneamente prompt, corpus ou modelo.
4. Compare as três saídas. Marque onde há resposta útil, fundamentação no corpus, latência percebida e um limite ou incerteza que exigiria revisão humana.

Não use dados pessoais, documentos institucionais, credenciais, chaves ou capturas que revelem contas. A decisão arquitetural a discutir é: **quando uma resposta deve depender de contexto fornecido e qual evidência precisa acompanhá-la?**

## Evidência a entregar

Entregue a tabela da atividade e uma conclusão de até cinco linhas. A evidência da atividade deve incluir segurança e custo: declare que usou apenas material sintético, a rota escolhida e qualquer limite ou custo potencial percebido.

| Condição | Qualidade para a pergunta | Fundamentação no corpus | Latência percebida | Limite ou incerteza observada |
|---|---|---|---|---|
| Sem contexto |  |  |  |  |
| Com contexto |  |  |  |  |
| Com contexto + parâmetro controlado |  |  |  |  |

Na conclusão, diga qual condição você aceitaria apenas como rascunho e qual exigiria fonte, revisão humana ou novo teste. Os resultados desta pequena amostra não provam qualidade geral, nem autorizam uma decisão de produção sem casos representativos.

## Segurança e custo

A decisão arquitetural não é “qual ferramenta venceu”, mas qual fronteira de dado, evidência e operação é aceitável para a atividade. Use somente o corpus acima; remova quaisquer registros locais ao terminar e nunca versione respostas que contenham dados reais.

Para a atividade, instalação local pode consumir CPU, memória, disco e energia; uma interface ou API pode impor conta, limites, retenção ou custo potencial. Registre esses limites na evidência, mesmo quando não houve cobrança. Se uma rota falhar, volte à rota essencial de análise manual: ela preserva a comparação e não depende de acesso pago.
