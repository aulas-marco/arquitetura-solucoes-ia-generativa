# Caso contínuo: Cooperativa Aurora — spec curta e evidência cedo

**Caso contínuo — Cooperativa Aurora.** [← Módulo 4: Autonomia](../modulo-4-agentes/caso-aurora.md) · [Módulo 6: Confiança →](../modulo-6-confianca/caso-aurora.md)

A Aurora chegou a este ponto com um agente de ferramentas somente de leitura e orçamento de passos, decidido no [ADR-Aurora-003](../modulo-4-agentes/caso-aurora.md). O time de tecnologia tem quatro pessoas e nenhuma dedicada a arquitetura. Essa restrição é o dado principal deste módulo: o mesmo método aplicado com a profundidade do Banco Lume consumiria a capacidade inteira do time.

## A demanda

O atendimento pede que o dossiê gerado pelo agente inclua o histórico de parcelamento do cooperado. O dado existe, está autorizado e já é lido por outra tela.

## Profundidade escolhida

Spec curta, sem plano formal e sem tarefas fatiadas. O critério que a Aurora adotou tem uma linha: **fluxo completo quando a mudança cria efeito externo, altera autorização ou toca regra que ninguém sabe recitar de cabeça; spec curta no resto.** Esta demanda não cria efeito, não altera autorização e a regra de parcelamento está escrita na política que o RAG já indexa.

A spec curta tem quatro campos: o que o usuário passa a ver, o que não muda, dois critérios de aceite verificáveis por comando e uma pergunta em aberto. Cabe em meia página e leva vinte minutos.

## O gate que a Aurora manteve

Dos três gates, a Aurora manteve **um**: revisão humana antes do merge, com o mesmo revisor cumprindo os dois eixos, aderência à spec e padrões de engenharia. Os gates 1 e 2 viraram uma conversa de dez minutos registrada na própria spec.

Essa é uma redução legítima e tem preço declarado: com um único gate, um erro de intenção só aparece quando o código já existe. A Aurora aceita o preço porque o custo de refazer meia página de spec e uma fatia pequena é baixo. Se a mesma redução fosse aplicada à mudança de cláusula contratual do [Banco Lume](caso-lume.md), o erro de intenção chegaria ao jurídico depois do merge.

## O que as duas organizações provam juntas

O mesmo método, o mesmo material teórico e duas profundidades diferentes, ambas defensáveis. O que torna cada uma defensável não é o número de etapas cumpridas: é o critério escrito que decide a profundidade e o registro do que foi dispensado.

## Continuidade

No [Módulo 6](../modulo-6-confianca/caso-aurora.md), o histórico de parcelamento entra como dado pessoal adicional no contexto do agente, e a spec curta desta página passa a ser a evidência de que a inclusão foi uma decisão registrada.
