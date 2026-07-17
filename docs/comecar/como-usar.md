# Como usar este site-livro

Este material pode ser lido em sequência, consultado durante uma decisão arquitetural ou usado como apoio aos encontros. As páginas priorizam conceitos e critérios duráveis; produtos aparecem apenas quando ajudam a concretizar uma ideia.

## Sequência recomendada

1. Leia [Sobre a disciplina](sobre-a-disciplina.md) e o [Mapa de aprendizagem](mapa-de-aprendizagem.md).
2. Percorra os seis módulos na ordem. Cada um pressupõe o vocabulário e as decisões construídos antes.
3. Em cada módulo, comece por conceitos, avance para padrões e decisões, examine o exemplo e então enfrente o estudo de caso.
4. Resolva os exercícios após a leitura. Use a [Taxonomia de Bloom](taxonomia-de-bloom.md) para reconhecer o tipo de raciocínio solicitado.
5. Consulte o [Glossário](../referencia/glossario.md), o [Catálogo de padrões](../referencia/catalogo-de-padroes.md), os [Atributos de qualidade](../referencia/atributos-de-qualidade.md) e o [Template de ADR](../referencia/template-adr.md) sempre que precisar comparar ou registrar escolhas.

## Oficinas de ferramentas sem barreira financeira

Cada módulo tem uma oficina prática com uma ferramenta local open source. O roteiro informa pré-requisitos, instalação, arquivos sintéticos, comandos, resultado esperado, variação controlada, entrega e limpeza. A evidência é a execução e sua interpretação arquitetural; nunca use dados reais, credenciais ou segredos.

Use somente prompts, corpus, traces e configurações sintéticos. Não envie, registre ou versione dados pessoais, documentos corporativos, credenciais, chaves, tokens, URLs privadas ou qualquer outro dado sensível. O [Guia de ferramentas e plataformas](../referencia/guia-de-ferramentas.md) ajuda a escolher uma rota, e a oficina continua possível pela rota essencial quando uma plataforma externa falhar ou não estiver disponível.

## Espinha de aprendizagem

Em qualquer página, use quatro movimentos para transformar leitura em decisão arquitetural:

1. **Conceito:** nomeie o fenômeno e delimite o que ele significa no sistema.
2. **Decisão:** compare alternativas e explicite o trade-off assumido.
3. **Evidência:** declare como a hipótese será testada, observada ou revista.
4. **Aplicação:** use o raciocínio no caso, respeitando contexto, risco e restrições.

## No GitHub ou no MkDocs

No GitHub, abra `docs/index.md` para iniciar e siga os links entre arquivos Markdown. Essa forma é conveniente para leitura direta, histórico de mudanças e comentários em revisão.

No site MkDocs, use as abas e o menu lateral para navegar, a busca para localizar termos e o sumário da página para saltar entre seções. Os links **anterior** e **próximo** preservam o percurso didático.

## Respostas, casos e feedback

As questões de recordar e compreender trazem respostas públicas em blocos expansíveis. Elas servem para autocorreção imediata, não para substituir sua tentativa inicial. Atividades de aplicar, analisar, avaliar e criar apresentam critérios de avaliação; a resposta depende do contexto e deve explicitar pressupostos, alternativas e evidências.

Nos níveis avançados, leia primeiro a situação e identifique seu papel. Em seguida, reúna os insumos indicados, siga os passos de condução e confira se a entrega responde ao formato pedido. Os percentuais mostram o peso relativo de cada critério; não são uma lista de pontos a acumular. Use a coluna “o que evidencia atendimento adequado” para revisar clareza, evidência, limites e consequências antes de enviar.

Os estudos de caso são independentes. Leia primeiro o contexto, registre dúvidas e restrições, produza sua proposta e só depois compare com os padrões do módulo. Quando houver feedback do professor, ele poderá incluir exemplos adicionais, comentários sobre a defesa e referências às decisões discutidas em aula.

## Acessibilidade e estudo ativo

Diagramas essenciais são acompanhados por descrição textual e imagens possuem texto alternativo. Tabelas não substituem a explicação principal. Use zoom, modo de alto contraste e navegação por teclado do navegador conforme necessário. Se um recurso visual não estiver acessível, a descrição adjacente deve permitir acompanhar o argumento.

Para estudar ativamente, transforme títulos em perguntas, tente explicar cada padrão com suas próprias palavras e registre decisões usando o [Template de ADR](../referencia/template-adr.md). O objetivo não é memorizar uma arquitetura pronta, mas aprender a construir uma justificativa verificável.
