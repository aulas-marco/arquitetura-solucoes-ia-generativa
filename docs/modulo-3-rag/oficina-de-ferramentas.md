# Oficina de ferramentas — observar um RAG fundamentado

**Objetivo Bloom:** Aplicar e Analisar.

Esta oficina torna inspecionável o caminho entre uma pergunta, uma evidência recuperada e uma resposta. Ela usa um corpus de treinamento pequeno; não mede a qualidade geral de um modelo, índice ou fornecedor.

## Decisão arquitetural em foco

Um sistema RAG precisa distinguir uma resposta fluente de uma resposta sustentada por fonte elegível. A **atividade guiada** compara essas condições e explicita onde a arquitetura deve registrar versão, trecho e citação. Consulte o [Guia de ferramentas e plataformas](../referencia/guia-de-ferramentas.md) antes de escolher uma rota: as categorias orientam a decisão, não prescrevem um produto.

## Roteiros equivalentes de acesso

### Essencial, sem cartão

Faça a recuperação manual estruturada com o corpus desta página, uma tabela ou arquivos locais; alternativamente, use um recuperador local que aceite documentos sintéticos. Separe os trechos, atribua identificadores e selecione evidências antes de redigir a resposta. A rota não depende de cartão, conta, chave de API nem chamada remota e é suficiente para a evidência obrigatória.

### Institucional

Use um ambiente de busca, laboratório ou conector institucional somente se ele já estiver autorizado e disponível. Carregue apenas o corpus sintético desta página, registre a política de acesso aplicada e produza a mesma evidência. A rota institucional não acrescenta pontos; apenas muda o ambiente de observação.

### Comercial ou avançada

Opcionalmente, repita a prática em um serviço gerenciado de RAG ou conector comercial autorizado. Declare conta, chave, possível cobrança, retenção e quais dados seriam enviados; não use dados reais. A rota comercial ou avançada não acrescenta pontos e não é necessária para comparar a decisão arquitetural.

## Atividade guiada

A atividade obrigatória é a rota **Essencial, sem cartão** (ou a execução local equivalente); ela não depende de cartão. Trabalhe com o corpus sintético abaixo.

**Corpus sintético — Base de atendimento Boreal (versão de treinamento 2026-07):**

| ID e versão | Trecho |
|---|---|
| `POL-17:v3` | Reembolso de compra regular pode ser solicitado em até 15 dias corridos da compra. O atendente deve citar a política aplicada. |
| `POL-17:v3` | Em campanha especial identificada no pedido, o prazo de reembolso é de 7 dias corridos. Sem a data ou o tipo de compra, o caso deve ser encaminhado para revisão humana. |
| `ENV-04:v1` | Pedidos de estorno são registrados no portal; a confirmação depende da validação do pedido elegível. |

**Perguntas de referência:**

1. “Qual é o prazo para solicitar reembolso em uma compra regular?”
2. “O que devo responder se não sei a data nem se a compra foi promocional?”

1. Registre uma resposta inicial a cada pergunta **sem evidência recuperada**. Ela pode ser uma hipótese, mas não deve inventar uma fonte.
2. Simule a ingestão: conserve ID, versão e conteúdo de cada trecho; explique como uma mudança de versão seria reconhecida.
3. Para cada pergunta, recupere manualmente os trechos candidatos, anote o critério de seleção e aplique o trecho à resposta. Uma ferramenta local pode executar esta etapa, mas deve mostrar os identificadores recuperados.
4. Redija a resposta **com evidência**, citando `POL-17:v3` ou recusando-se a concluir quando a evidência exigir revisão humana. Compare recuperação, citação e resposta com a versão sem evidência.
5. Inspecione uma falha plausível: por exemplo, recuperar apenas o primeiro trecho de `POL-17:v3` para a segunda pergunta. Formule uma hipótese de correção em ingestão, metadado, consulta, filtro, ranking ou montagem de contexto.

A decisão arquitetural a discutir é: **como a ingestão, a recuperação e a citação permitem saber se uma resposta está fundamentada na fonte autorizada?** Não acrescente fatos externos ao corpus.

## Evidência a entregar

Entregue a tabela preenchida e uma conclusão de até cinco linhas. A evidência da atividade inclui segurança e custo: informe a rota escolhida, declare que o corpus é sintético e registre qualquer instalação, limite, consumo local ou custo potencial percebido.

| Pergunta | Resposta sem evidência | Trecho recuperado e proveniência | Resposta com evidência e citação | Falha observada | Hipótese de correção |
|---|---|---|---|---|---|
| Prazo regular |  |  |  |  |  |
| Dados insuficientes |  |  |  |  |  |

Na conclusão, diferencie uma resposta que pode ser apresentada ao usuário daquela que deve abster-se e encaminhar revisão. Uma única execução não prova qualidade de produção: ela apenas localiza uma hipótese verificável sobre o pipeline.

## Segurança e custo

A decisão arquitetural não é escolher a ferramenta “mais inteligente”, mas preservar proveniência, autorização e possibilidade de revisão. Use somente o corpus sintético; não carregue políticas, contratos, credenciais, dados pessoais ou documentos institucionais em conectores, capturas ou repositórios.

Uma ferramenta local pode consumir CPU, memória, disco e energia; um conector institucional ou comercial pode impor conta, retenção, limites ou cobrança. Registre esses limites na evidência e remova o corpus ou configuração local ao terminar. Se qualquer rota externa falhar, retorne à recuperação manual estruturada: a atividade e a evidência continuam possíveis sem cartão.
