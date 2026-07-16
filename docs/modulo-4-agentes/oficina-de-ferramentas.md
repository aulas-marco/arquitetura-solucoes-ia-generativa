# Oficina de ferramentas — workflow, ferramenta e aprovação

**Objetivo Bloom:** Aplicar e Analisar.

Esta oficina separa consulta, intenção e efeito em um fluxo pequeno e inspecionável. A prática simula uma ação em dados de treinamento; ela não conecta CRM, estoque, pedidos ou qualquer sistema corporativo real.

## Decisão arquitetural em foco

Disponibilizar uma ferramenta ao modelo não autoriza sua execução. A **atividade guiada** torna visíveis o contrato da ferramenta, a autorização delegada, a aprovação humana e o retorno autoritativo que fecha um efeito. Consulte o [Guia de ferramentas e plataformas](../referencia/guia-de-ferramentas.md): a ferramenta é uma hipótese de implementação, não uma substituição para política e controle.

## Roteiros equivalentes de acesso

### Essencial, sem cartão

Use um diagrama, uma tabela de estado ou arquivo de configuração local para descrever o workflow e executar a simulação passo a passo. A “ferramenta” de consulta pode ser uma busca no conjunto JSON ou na tabela sintética abaixo; a ação apenas atualiza um estado de simulação. A rota não depende de cartão, conta, chave de API ou integração externa e é suficiente para a evidência obrigatória.

### Institucional

Se houver autorização prévia, use um ambiente institucional de automação para reproduzir o mesmo fluxo com dados sintéticos e endpoint simulado. Não conecte sistemas corporativos nem use credenciais reais. A rota institucional não acrescenta pontos; ela só torna observável o mesmo contrato em outro ambiente.

### Comercial ou avançada

Opcionalmente, modele o fluxo em uma plataforma comercial de automação ou orquestração, usando exclusivamente dados e ações simulados. Declare conta, chave, cobrança, retenção e limites antes de executar. A rota comercial ou avançada não acrescenta pontos e nunca justifica acesso a um sistema real.

## Atividade guiada

A atividade obrigatória é a rota **Essencial, sem cartão** (ou uma execução local equivalente); ela não depende de cartão. Use os dados sintéticos abaixo e desenhe ou configure a sequência de estados.

**Dados sintéticos — Troca Boreal (ambiente de treinamento):**

```json
{
  "pedido": {"id": "PED-104", "cliente": "C-88", "status": "entregue", "versao": 4},
  "estoque": {"SKU-21": {"disponivel": true, "versao": 9}},
  "politica": {"troca_em_dias": 30, "aprovacao_humana": true}
}
```

**Solicitação simulada:** “Quero trocar `PED-104` pelo item `SKU-21`.”

1. Registre a **intenção** proposta: consultar pedido e estoque; propor a reserva simulada. Defina o contrato de consulta (entradas, resultado tipado e nenhum efeito).
2. Execute a consulta nos dados sintéticos e verifique a política. Identifique a identidade de treinamento `C-88` e a **autorização** necessária para propor a ação; não trate o texto da solicitação como autorização de escrita.
3. Gere uma chave de **idempotência**, por exemplo `TROCA-PED-104-1`, e guarde uma intenção `reserva_pendente` com versão esperada do pedido e do estoque. Simule uma segunda tentativa com a mesma chave e mostre que ela não cria uma nova reserva.
4. Produza uma tela, registro ou linha de aprovação explícita: aprovador, decisão, data simulada e escopo. Sem aprovação, a condição de parada é `aguardando_aprovacao`; nenhum efeito é aplicado.
5. Após a aprovação, execute somente a ação simulada `reservar(SKU-21)`. Retorne um **resultado autoritativo** tipado, por exemplo `RES-501`, e persista o estado `reservado`. Se a confirmação não retornar, pare em `outcome_unknown` e consulte o registro simulado pela chave de idempotência antes de repetir.

A decisão arquitetural a discutir é: **em que fronteira o workflow deixa de planejar e passa a produzir efeito, e quem deve aprová-lo?** A evidência é o trace que relaciona proposta, autorização, aprovação e resultado. A atividade não autoriza chamadas a sistemas externos, mesmo quando uma ferramenta comercial estiver disponível.

## Evidência a entregar

Entregue o diagrama, configuração ou tabela de trace e uma conclusão de até cinco linhas. A evidência da atividade deve declarar que utilizou dados sintéticos, a rota escolhida e qualquer instalação, limite, consumo local ou custo potencial.

| Etapa | Registro exigido | Evidência produzida |
|---|---|---|
| Intenção | consulta e ação proposta |  |
| Autorização | identidade, política e escopo |  |
| Idempotência | chave e tratamento de repetição |  |
| Aprovação | aprovador, decisão e condição de espera |  |
| Efeito simulado | ação, versão esperada e resultado autoritativo |  |
| Parada | concluído, aguardando aprovação ou `outcome_unknown` |  |

Explique qual condição impede a ação, como evitaria duplicação e por que o resultado autoritativo não pode ser substituído por uma mensagem do modelo.

## Segurança e custo

A decisão arquitetural é controlar efeitos, não demonstrar autonomia máxima. Mantenha dados, identidades, pedidos, estoque, aprovações e resultados inteiramente sintéticos; não registre chaves, tokens, URLs privadas, credenciais ou capturas de sistemas reais.

Um executor local pode consumir CPU, memória, disco e energia; plataformas institucionais ou comerciais podem impor conta, retenção, limites e cobrança. Registre esses limites na evidência e exclua configurações locais de teste quando não forem mais necessárias. Se a ferramenta falhar, preserve o diagrama e a execução simulada: a atividade continua possível sem cartão e sem efeito externo.
