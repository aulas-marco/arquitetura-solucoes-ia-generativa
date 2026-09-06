# Citações e abstenção

O que entra na janela, como a resposta aponta para a evidência que a sustenta e o que o sistema faz quando a evidência não basta.

## Montagem de contexto

O montador de contexto organiza evidências dentro de um orçamento e precisa:

- reservar orçamento para instruções, pergunta e resposta;
- preservar título, versão, vigência, seção e identificador de citação;
- agrupar chunks vizinhos quando a unidade recuperada depende do entorno;
- remover duplicatas e versões superadas;
- equilibrar relevância e diversidade de fontes;
- sinalizar autoridade e conflitos, sem inventar precedência;
- separar claramente evidência de instrução;
- limitar dados à finalidade da consulta.

Ordenação pode influenciar a atenção do modelo. Avalie casos em que a evidência principal está no início, meio e fim. Compressão de contexto pode resumir candidatos antes da geração, porém cria uma transformação que também precisa preservar suporte e proveniência.

Conteúdo recuperado é entrada não confiável. Um documento pode conter frases como “ignore as instruções anteriores”. Isolamento estrutural, rotulagem, minimização de ferramentas e validação posterior reduzem risco de injeção indireta. O [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) é orientação de segurança registrada para tratar essa superfície; conteúdo nunca recebe autoridade para mudar política ou executar ação.

## Citações e suporte

Uma citação útil liga uma afirmação material a um trecho que realmente a sustenta. O pipeline deve produzir identificadores estáveis, e a interface deve permitir abrir fonte, versão e localização dentro da autorização vigente.

Valide ao menos:

- **correção:** a fonte citada implica a afirmação;
- **completude:** afirmações verificáveis importantes possuem citação;
- **qualidade da fonte:** a origem é adequada e vigente;
- **atribuição:** a citação está próxima da afirmação correspondente;
- **acessibilidade:** o usuário consegue consultar o material citado.

Mostrar três links no rodapé não demonstra suporte. Uma resposta pode citar fonte relevante ao tema, mas não à proposição. Citação também não transforma opinião, inferência ou política conflitante em fato; essas categorias devem ser rotuladas.

## Evidência insuficiente e abstenção

**Evidência insuficiente** ocorre quando falta cobertura, os resultados são fracos, há conflito não resolvido, uma fonte exigida está indisponível, a pergunta está fora do escopo ou a autorização remove todo suporte. O sistema precisa distinguir “não existe”, “não foi encontrado” e “você não pode acessar”. A mensagem não deve revelar a existência de documento confidencial.

O controle de suficiência combina sinais: presença de fonte obrigatória, limiar calibrado, cobertura das partes da pergunta, vigência, diversidade, conflito e verificações de suporte. Escores de similaridade variam por coleção e consulta; não use um valor universal.

Respostas seguras incluem:

- pedir dado essencial que falta;
- responder parcialmente e nomear o limite;
- indicar canal oficial ou revisão humana;
- declarar que as fontes disponíveis não sustentam a resposta;
- bloquear quando a finalidade ou identidade não autoriza.

Avalie **abstenção correta** e **abstenção indevida**. Recusar sempre é seguro, mas inútil; responder sempre é fluente, mas arriscado.

## Proveniência de ponta a ponta

Proveniência é a cadeia que permite reconstruir origem e transformação. No mínimo, cada evidência deve ligar:

`fonte → versão → localização → aquisição → extração → chunk → metadados → representação → índice → consulta → contexto → citação`.

Também é preciso versionar política de acesso, transformador de consulta, modelo de embedding, algoritmo de fusão, reranker, template de contexto, prompt e modelo gerador. Um trace completo pode registrar identificadores, hashes, versões, tempos e decisões, em lugar do conteúdo integral, conforme retenção e privacidade.

RAG preserva essa cadeia quando o pipeline registra origem, autoridade, versão, transformação e uso verificáveis. Índice vetorial, citação na interface e trace precisam compor esse registro, cada qual com sua responsabilidade.

## Atualidade, consistência e temporalidade

“Atual” precisa de medida. Uma política publicada às 10h pode ter SLO de disponibilidade até 10h15; uma exclusão por incidente pode exigir propagação em dois minutos. Defina atraso máximo por fonte, comportamento durante reindexação e regra para consultas no intervalo. Índices azul–verde, manifestos e troca atômica evitam misturar versões incompatíveis.

Vigência difere de data de ingestão. A consulta “qual política valia em janeiro?” requer recuperação temporal, enquanto “qual vale agora?” deve excluir versões expiradas. Conflitos entre fontes não devem ser resolvidos por similaridade: autoridade, jurisdição e precedência pertencem à governança do conhecimento.
