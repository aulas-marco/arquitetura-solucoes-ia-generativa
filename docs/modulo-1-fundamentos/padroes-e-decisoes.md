# Padrões e decisões

Os conceitos anteriores descrevem propriedades; padrões organizam respostas recorrentes a elas. Eles não formam uma escada obrigatória. A solução mais simples que satisfaz cenários de qualidade e risco costuma ser preferível, e padrões podem ser combinados. Use o [Catálogo de padrões arquiteturais](../referencia/catalogo-de-padroes.md) para a formulação completa dos padrões que serão aprofundados adiante.

## Panorama das abordagens

| Abordagem | O que acrescenta | Quando ajuda | Nova responsabilidade arquitetural |
|---|---|---|---|
| **Geração direta** | Prompt versionado, chamada ao modelo e tratamento da saída | Tarefas de baixo risco apoiadas no pedido do usuário ou na capacidade geral do modelo | Avaliar variabilidade, qualidade e custo por modelo/prompt |
| **Contexto fornecido** | Conteúdo selecionado enviado junto à solicitação | Poucos materiais conhecidos e estáveis cabem no contexto | Selecionar, autorizar, versionar e montar o contexto |
| **RAG** | Ingestão, índice, recuperação e evidências antes da geração | Conhecimento amplo, mutável ou que exige proveniência | Operar dois fluxos e avaliar recuperação separada da geração |
| **Uso de ferramentas** | Contratos para consultar ou agir em sistemas externos | O modelo precisa de dado atual ou de uma capacidade executável | Validar autorização, parâmetros, efeitos e idempotência |
| **Workflow com LLM** | Ordem determinística com etapas generativas delimitadas | Processo conhecido contém interpretação ou redação | Modelar estado, exceções, retries e contratos entre etapas |
| **Agente** | Escolha dinâmica de próximos passos e ferramentas | Caminho não pode ser totalmente antecipado e o ganho justifica autonomia | Limitar orçamento, permissões, memória e aprovação humana |
| **Fine-tuning** | Alteração dos parâmetros para comportamento especializado | Padrão recorrente de estilo, formato ou tarefa não resolvido por contexto | Curar dados, avaliar versões, implantar e reverter o modelo adaptado |

### Geração direta

Na geração direta, a aplicação monta instruções e entrada, chama o modelo e entrega ou transforma a saída. É uma boa linha de base para redação, ideação e reformulação sem conhecimento privado crítico. A arquitetura continua precisando de versão de prompt e modelo, timeout, observação de tokens e avaliação. “Direta” significa poucos componentes, não ausência de engenharia.

### Contexto fornecido

Em vez de depender apenas dos parâmetros, a aplicação inclui material relevante na chamada. Para comparar duas cláusulas que o próprio usuário anexou, isso pode bastar. O contexto precisa respeitar autorização e limite de tamanho, preservar separação entre instruções e conteúdo e informar ao modelo como lidar com divergências. Quando a seleção manual deixa de escalar, surge a necessidade de recuperação.

### RAG

**Retrieval-Augmented Generation** separa conhecimento externo dos parâmetros: um fluxo prepara e indexa fontes; outro recupera evidências para a pergunta e as fornece à geração. O trabalho original de [Lewis et al.](https://proceedings.neurips.cc/paper/2020/hash/6b493230-Abstract.html) estabeleceu a combinação de memória paramétrica e não paramétrica para tarefas intensivas em conhecimento. Em arquitetura corporativa, RAG acrescenta atualização e proveniência possíveis, mas também segmentação, permissões, índice, sincronização, ranking e avaliação por etapa. O [Módulo 3](../sobre/plano-da-disciplina.md#modulo-3) tratará esse desenho em profundidade.

### Uso de ferramentas

Uma ferramenta expõe ao sistema uma consulta ou ação por contrato: buscar saldo, calcular frete, criar chamado. O modelo pode propor a chamada; um componente determinístico deve validar esquema, identidade, autorização e política antes da execução. Ferramentas ampliam capacidade e superfície de ataque. Operações com efeito exigem idempotência, limites e, conforme o risco, aprovação humana.

### Workflows com LLM

Um workflow mantém sequência e transições explícitas: receber documento, extrair campos, validar, encaminhar exceção e redigir resposta. O modelo atua onde interpretação é útil; o processo não depende dele para inventar a próxima etapa. Essa abordagem é adequada quando o caminho é conhecido e auditabilidade importa.

### Agentes

Um agente usa um modelo para escolher próximos passos e ferramentas em busca de um objetivo dentro de limites. Ele se justifica quando tarefas abertas demandam adaptação que um workflow fixo não oferece. Autonomia é uma decisão graduada, não um interruptor. Orçamento de etapas, ferramentas mínimas, identidade delegada, memória controlada, critérios de parada e aprovação por risco devem fazer parte do desenho. O [Módulo 4](../sobre/plano-da-disciplina.md#modulo-4) aprofundará esses limites.

### Fine-tuning

Fine-tuning altera comportamento paramétrico. Pode reduzir exemplos longos no prompt ou melhorar consistência em uma tarefa especializada. Não substitui controles da aplicação nem é um banco de dados atualizável. Antes de adotá-lo, compare uma linha de base com prompt, exemplos e contexto; registre o ganho observado e o custo de dados, avaliação, hospedagem e regressão.

## Anti-padrão: “LLM conectado diretamente a toda necessidade”

O anti-padrão aparece quando a mesma chamada ao modelo recebe documentos, decide autorização, calcula regras, consulta sistemas, escolhe ações e produz o texto final. Sua aparente simplicidade esconde contratos distintos dentro de uma caixa probabilística.

Os sintomas incluem prompt crescente, credenciais amplas, dificuldade de reproduzir falhas, retries que repetem ações, resposta sem fonte e testes baseados em poucos exemplos felizes. Uma mudança de modelo passa a afetar todas as responsabilidades ao mesmo tempo.

A correção não é criar microsserviços para cada frase. É separar responsabilidades onde há qualidade ou risco diferente: regras explícitas permanecem determinísticas; conhecimento ganha fonte e proveniência; ações passam por contrato e autorização; geração recebe escopo; observabilidade correlaciona o caminho. A fronteira deve ser proporcional ao caso.

## ADR preliminar — contexto para o assistente documental

### Status

Proposta para experimento em 14 de julho de 2026.

### Contexto

O atendimento interno precisa responder perguntas sobre 420 documentos corporativos. Cerca de 8% mudam por mês, há quatro níveis de acesso e respostas sobre compras e pessoas devem indicar a fonte. O piloto atenderá 150 usuários. Não existe ainda conjunto de avaliação representativo nem medição de latência em produção.

### Direcionadores da decisão

- Fundamentação: afirmações sobre políticas devem apontar evidência autorizada.
- Privacidade e segurança: nenhum conteúdo pode atravessar níveis de acesso.
- Atualização: uma versão aprovada deve aparecer no assistente no mesmo dia útil.
- Latência: p95 preliminar de resposta completa inferior a oito segundos.
- Manutenibilidade: trocar modelo ou regra de recuperação sem alterar o canal.

### Opções consideradas

1. **Geração direta com conhecimento paramétrico.** Menor complexidade, porém não atende atualização, acesso e proveniência.
2. **Documentos inteiros no contexto.** Viável para um subconjunto pequeno, mas seleção, custo e conflito de versões pioram com o corpus.
3. **RAG básico com autorização antes da recuperação.** Acrescenta ingestão e índice, mas separa fontes, seleção e geração e permite citar trechos.
4. **Fine-tuning com os documentos.** Pode ajustar comportamento, mas não oferece exclusão, atualização e proveniência compatíveis.

### Decisão

Executar um piloto da opção 3. O fluxo offline registrará fonte, versão, vigência e nível de acesso antes da indexação. O fluxo online propagará identidade, filtrará candidatos autorizados, fornecerá trechos com identificadores e instruirá o modelo a declarar insuficiência. O canal acessará a solução por uma API, sem integração direta ao fornecedor do modelo.

### Consequências

Ganhamos uma hipótese verificável para atualização e fundamentação, além de fronteiras para substituir componentes. Assumimos pipeline de ingestão, índice, sincronização de permissões e mais latência. Persistem riscos de recuperação incompleta, documento contraditório e resposta que extrapola a evidência. O piloto não autoriza decisões automáticas nem escrita em sistemas corporativos.

### Evidências

Ainda não há evidência suficiente para aceitar a decisão. O experimento usará 80 perguntas representativas, incluindo 20 sem resposta e 20 com restrição de acesso. Medirá presença de fonte relevante nos cinco primeiros candidatos, suporte das afirmações, recusas corretas, vazamento entre perfis, p95 e custo por interação. A adoção dependerá de limiares aprovados com as áreas responsáveis.

### Gatilhos de revisão

- qualquer vazamento de conteúdo restrito;
- menos de 90% das perguntas respondíveis com evidência relevante recuperada;
- resposta sem suporte em mais de 5% das afirmações críticas;
- p95 acima de oito segundos ou custo mensal projetado acima do orçamento;
- corpus pequeno e estável tornar o contexto integral comprovadamente mais simples e equivalente.

Esta ADR é preliminar porque explicita hipóteses, não certezas. Use o [template de ADR](../referencia/template-adr.md) para registrar decisões do seu caso.

**Próxima página:** [Exemplo arquitetural em oito camadas](exemplo-arquitetural.md).
