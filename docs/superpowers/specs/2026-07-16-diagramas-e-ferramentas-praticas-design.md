# Desenho — diagramas arquiteturais e ferramentas práticas

**Data:** 16 de julho de 2026  
**Status:** aprovado para revisão do documento

## Objetivo

Substituir a leitura excessivamente abstrata do exemplo arquitetural do Módulo 1 por duas representações complementares e tornar o letramento de ferramentas concreto ao longo dos conceitos e das oficinas da disciplina.

## Diagramas do Módulo 1

### Diagrama de componentes

Substituir o primeiro diagrama Mermaid por uma ilustração didática gerada por IA, em português e com estilo acadêmico. A ilustração mostra componentes, fronteiras e dependências de uma solução de consulta documental:

- canal do usuário, aplicação/API e orquestrador como caminho principal;
- conhecimento autorizado e gateway/modelo como dependências explícitas do orquestrador;
- ferramentas corporativas como caminho condicional com retorno tipado;
- infraestrutura/operação sustentando os componentes;
- uma faixa transversal para segurança, governança, avaliação e observabilidade;
- setas que expressem direção de dependência e de dados, sem conexão direta do modelo a sistemas corporativos.

O texto alternativo e o equivalente textual permanecem obrigatórios. A imagem não usa marcas, logotipos ou fornecedores.

### Diagrama de sequência

Substituir o segundo fluxo por um Mermaid `sequenceDiagram` que descreve o caminho crítico online: usuário, aplicação, orquestrador, política/autorização, recuperação, gateway, modelo e validação. O diagrama deve tornar visíveis: autenticação antes de recuperação, retorno de evidências autorizadas, montagem de prompt/contexto, resposta do modelo, validação/citações e devolução ao usuário. Caminhos de ferramenta ou de degradação aparecem somente como ramos opcionais, sem ofuscar a sequência principal.

O fluxo offline de ingestão é distinguido textualmente do caminho online e não aparece como chamada síncrona na sequência.

## Exemplos de ferramentas nos conceitos

Cada módulo recebe dois níveis de aterramento:

1. exemplos inseridos no ponto conceitual em que a categoria aparece;
2. caixa final `## Ferramentas no mercado`, com quando usar, pré-requisito, limite e link para o Guia de ferramentas.

As ferramentas são exemplos de categorias, nunca prescrição de fornecedor. Condições de acesso e instalação são verificadas em documentação oficial na data de implementação e registradas nas fontes do curso.

| Módulo | Conceito | Exemplos concretos |
|---|---|---|
| 1 | modelo local, AIaaS e playground | Ollama, LM Studio, ChatGPT, API OpenAI |
| 2 | SDK, adaptador e portabilidade | OpenAI SDK, LiteLLM, Docker Model Runner |
| 3 | RAG e recuperação vetorial | LangChain, LlamaIndex, Chroma, Qdrant |
| 4 | workflow e agentes | n8n, LangGraph, AutoGen |
| 5 | avaliação, observabilidade e guardrails | Langfuse, Phoenix, Guardrails AI |
| 6 | gateway, telemetria e custo | LiteLLM Proxy, OpenTelemetry, Langfuse |

## Oficinas executáveis

Cada oficina passa a ter uma receita principal em ambiente local ou sem cartão, composta por: objetivo, software/versão, pré-requisitos, instalação, comando ou configuração mínima, entrada sintética, resultado esperado, evidência a entregar, limpeza e limites.

| Módulo | Receita principal | Resultado mínimo |
|---|---|---|
| 1 | Ollama com modelo local pequeno | comparar resposta sem/com contexto usando corpus sintético |
| 2 | LiteLLM ou OpenAI SDK com fixture local | exercitar adaptador e matriz de decisão sem chamar API paga |
| 3 | LangChain + Chroma local | indexar corpus sintético, recuperar trechos e citar fonte |
| 4 | n8n local | executar workflow sintético com aprovação antes de efeito simulado |
| 5 | Phoenix ou Langfuse auto-hospedado | registrar casos adversariais e decisão de tratamento |
| 6 | LiteLLM Proxy diante do Ollama local | observar roteamento, quotas e métricas sintéticas |

Uma rota alternativa institucional e uma rota comercial continuam disponíveis, mas não acrescentam pontos. Toda receita obrigatória pode ser cumprida sem cartão, sem credencial de provedor e sem dados reais. Se a máquina do estudante não comportar a execução local, a oficina oferece artefato sintético e roteiro de inspeção equivalente, identificado como plano de contingência e não como substituto silencioso.

## Mudanças previstas

- Gerar e adicionar uma nova imagem em `docs/assets/images/` para o diagrama de componentes do Módulo 1.
- Atualizar `docs/modulo-1-fundamentos/exemplo-arquitetural.md` com imagem, equivalente textual e sequência Mermaid.
- Atualizar conceitos e oficinas dos seis módulos.
- Expandir `docs/referencia/guia-de-ferramentas.md`, `docs/referencia/fontes.yml` e testes editoriais para nomes de ferramentas, receitas e fontes oficiais.
- Preservar a política de equidade, a independência de fornecedor, os limites de palavras e a construção estrita MkDocs.

## Critérios de aceite

1. A página do Módulo 1 possui uma imagem acessível de componentes e um Mermaid `sequenceDiagram` legível, sem confundir dependência e sequência.
2. Cada página de conceitos contém exemplos nomeados no texto e uma seção `Ferramentas no mercado` com limites e link para o guia.
3. Cada oficina oferece uma receita principal reproduzível com comando/configuração, entrada sintética, resultado esperado e limpeza.
4. Nenhuma receita obrigatória requer cartão, chave de API, conta corporativa ou dado real.
5. Links e pré-requisitos de ferramentas são sustentados por fontes oficiais registradas.
6. Testes, validador editorial e `mkdocs build --strict` passam.
