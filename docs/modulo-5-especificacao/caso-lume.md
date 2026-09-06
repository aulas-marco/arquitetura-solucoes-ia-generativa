# Caso contínuo: Banco Lume — a mudança governada

**Caso contínuo — Banco Lume.** [← Módulo 4: Autonomia](../modulo-4-agentes/caso-lume.md) · [Módulo 6: Confiança →](../modulo-6-confianca/caso-lume.md)

O Banco Lume chegou até aqui com um workflow assistivo com RAG e **sem agente** em produção: a decisão do [Módulo 4](../modulo-4-agentes/caso-lume.md) foi manter o fluxo determinístico, porque a sequência de consulta continua enumerável. A pergunta deste módulo é outra e independe daquela: como o próprio time do Lume conduz uma mudança no software que sustenta esse workflow.

## A demanda

A área de contestações pede que o rascunho gerado passe a citar a cláusula do contrato, e não apenas a política interna. Uma frase, e três regras escondidas dentro dela: o contrato tem versões por data de adesão, nem todo cliente tem cláusula equivalente, e a citação errada de cláusula é risco jurídico, não defeito de usabilidade.

## Constitution do repositório

O Lume já operava sob regras de engenharia não escritas. Ao adotar o fluxo, elas viraram cinco princípios com poder de rejeitar:

1. nenhuma resposta ao analista pode citar fonte sem identificador de versão;
2. mudança que toque cláusula contratual exige revisão do jurídico antes do merge, não depois;
3. teste antes de comportamento novo, sem exceção para correção urgente;
4. nenhuma consulta a contrato ocorre fora do filtro de autorização por cliente;
5. o que não puder ser verificado por comando não entra como critério de aceite.

O princípio 2 é o que distingue o Lume: ele insere um aprovador que não é de engenharia dentro do Gate 3.

## Profundidade escolhida

Fluxo completo, com uma exceção declarada: a etapa de comparação de alternativas foi dispensada, porque só existe uma fonte contratual autoritativa. A dispensa está registrada como decisão, não como esquecimento — a diferença aparece quando alguém, daqui a um ano, perguntar por que não houve avaliação de alternativas.

## O que o gate reteve

No Gate 1, a spec afirmava “citar a cláusula aplicável”. O jurídico apontou que *aplicável* depende da data de adesão, e que dois clientes com o mesmo produto podem ter cláusulas diferentes. A ambiguidade virou fato registrado, e o critério de aceite passou a exigir data de adesão no filtro de recuperação. Sem esse gate, o agente teria implementado a leitura literal e o teste teria passado.

## Continuidade

A [Cooperativa Aurora](caso-aurora.md) conduz a mesma etapa com escolha oposta de profundidade. No [Módulo 6](../modulo-6-confianca/caso-lume.md), a decisão de citar cláusula contratual reaparece como superfície de risco: fonte nova, autorização nova, consequência jurídica nova.
