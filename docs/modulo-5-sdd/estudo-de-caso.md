# Estudo de caso: profundidade proporcional numa base legada

Caso curto, para cerca de 30 minutos de discussão em grupo com o material do módulo aberto. O dossiê fornece a situação e as restrições; a decisão de quanto processo aplicar fica por conta do grupo.

## Objetivo

Decidir **quanta especificação uma mudança merece**, e por quê. A tentação em SDD é aplicar as oito etapas a tudo, o que transforma método em cerimônia; a tentação oposta é dispensá-las sempre, o que devolve a intenção para a conversa. A discussão é de arquitetura: onde está o risco, qual artefato o contém e qual portão (*gate*) o autoriza.

## Como trabalhar em grupo

Grupos de três a cinco pessoas. Leia o dossiê uma vez, sem decidir nada, e depois trabalhe as cinco perguntas na ordem. Cada resposta precisa nomear o artefato que passa a existir e quem o aprova. O que o dossiê não permite decidir vira **incógnita**, com o experimento que a resolveria.

## Dossiê

A Boreal opera há nove anos um serviço de pedidos em produção. O código tem cobertura de testes irregular, três integrações síncronas com sistemas de parceiros e uma máquina de estados de pedido que ninguém documentou por inteiro — o conhecimento está distribuído entre quatro pessoas, duas das quais saíram no último ano.

A empresa adotou um agente de codificação há dois meses. O ganho foi real em tarefas pequenas e o incômodo também: duas mudanças passaram na revisão e quebraram regra de negócio em produção, porque o revisor não sabia que a regra existia.

Quatro demandas chegam na mesma semana:

| # | Demanda | O que se sabe |
|---|---|---|
| D1 | Corrigir o rótulo “Aguardando pagto.” para “Aguardando pagamento” em três telas | Texto puro, sem regra associada |
| D2 | Permitir que o cliente cancele um pedido até a separação começar | Existe regra de cancelamento no código, não escrita em lugar nenhum |
| D3 | Trocar o parceiro de frete da região Sul | Contrato de integração diferente do atual, prazos e exceções distintos |
| D4 | Provar à auditoria que nenhum pedido despachado foi cancelado nos últimos 12 meses | Não existe evento de auditoria específico; a informação está espalhada em logs |

A liderança quer uma regra clara: “quando usamos SDD e quando não usamos”.

## Perguntas

### 1. Profundidade por demanda

Classifique D1 a D4 em três faixas — sem spec, spec curta, fluxo completo — e nomeie o critério que separa as faixas. O critério precisa ser aplicável por outra pessoa sem consultar o grupo.

### 2. O que a base legada muda

D2 depende de uma regra que só existe no código. Decida se o primeiro artefato é uma spec da regra desejada ou uma descrição da regra vigente, e diga qual erro cada escolha evita.

### 3. Onde ficam os gates

Para a demanda que você classificou como fluxo completo, posicione os três portões (*gates*) e diga o que cada um pode bloquear. Um gate que nunca bloqueou nada em seis meses é um sinal de quê?

### 4. A demanda que não é de software

D4 pede evidência sobre o passado, não comportamento novo. Decida se ela entra no mesmo fluxo, e o que muda no conjunto de artefatos quando o entregável é uma prova e não uma funcionalidade.

### 5. O incidente que motivou tudo

Duas mudanças quebraram regra de negócio porque o revisor não sabia da regra. Diga qual etapa do fluxo teria contido cada uma, e se a contenção viria do artefato ou do gate. Se a resposta for “nenhuma”, nomeie o controle que faltaria.

## Entrega esperada

Uma página com a tabela das quatro demandas classificadas, o critério de faixa, os gates posicionados para uma delas e as incógnitas registradas com o experimento correspondente. A regra que a liderança pediu deve caber em duas frases.
