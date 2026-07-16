# Relatório — Task 2

## Resultado

Foram criadas as páginas canônicas de guia de ferramentas e projeto final, e ambas foram incluídas na navegação. A rota essencial é reproduzível sem cartão, usa dados sintéticos e não requer credenciais; alternativas institucionais e comerciais são comparativas e não dão vantagem avaliativa.

## Fontes oficiais consultadas

Todas verificadas em 16 de julho de 2026:

- OpenAI, [ChatGPT Free Tier FAQ](https://help.openai.com/en/articles/9275245-using-chatgpt-s-free-tier) e [What is ChatGPT: FAQ](https://help.openai.com/en/articles/12677804-what-is-chatgpt-faq).
- Ollama, [Quickstart](https://docs.ollama.com/quickstart) e [macOS requirements](https://docs.ollama.com/macos).
- OpenAI, [Developer quickstart — API](https://developers.openai.com/api/docs/quickstart).
- LangChain, [Install LangChain](https://docs.langchain.com/oss/python/langchain/install).
- n8n, [Hosting documentation](https://docs.n8n.io/hosting/).
- Langfuse, [Self-host Langfuse](https://langfuse.com/self-hosting) e [Docker Compose deployment](https://langfuse.com/self-hosting/deployment/docker-compose).
- LiteLLM, [Proxy CLI quick start](https://docs.litellm.ai/docs/proxy/quick_start).

## Arquivos

- `docs/referencia/guia-de-ferramentas.md`
- `docs/sobre/projeto-final.md`
- `mkdocs.yml`

## Commit

`20a7fcb docs: add accessible tool guide and group project`

## Teste executado

`python -m unittest tests.test_applied_literacy.AppliedLiteracyTest.test_shared_guide_and_group_project_preserve_equity -v` — PASS (1 teste).

## Correção de fonte

A URL anterior do quickstart da API OpenAI retornava HTTP 404. Em 16 de julho de 2026, foi substituída por [Developer quickstart — API](https://developers.openai.com/api/docs/quickstart), que retornou HTTP 200 e documenta o SDK, a chave de API e a adição de créditos. O teste da Task 2 foi executado novamente após a correção: PASS (1 teste).

## Auto-revisão

Verificados os requisitos literais: as sete categorias têm opções e fonte/data; as condições de instalação, conta, chave, cartão e custo potencial aparecem na matriz; a rubrica totaliza 100; o parágrafo literal de equidade foi preservado; e `git diff --check` não reportou erros.
