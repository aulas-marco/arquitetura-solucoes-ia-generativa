# Guia de ferramentas e plataformas

## Como ler este guia

Uma ferramenta é uma hipótese de implementação, não uma recomendação automática. Antes de adotá-la, registre a decisão, o contrato, o dado enviado, o custo, a forma de saída e o caminho de remoção.

As condições abaixo foram verificadas em **16 de julho de 2026** nas fontes oficiais indicadas. Elas podem mudar; não trate uma rota sem cobrança hoje como gratuidade permanente.

## Regra de acesso justo

Nenhuma atividade obrigatória depende de cartão de crédito. A rota essencial, sem cartão, é suficiente para produzir a evidência e receber a nota máxima. A disponibilidade de planos gratuitos muda: confira a fonte oficial e a data de verificação indicada em cada oficina.

Use apenas dados sintéticos nas atividades. Não cole credenciais, chaves, dados pessoais, dados institucionais ou segredos em prompts, arquivos de configuração, capturas ou repositórios.

## Categorias e critérios

| Categoria | Decisão que apoia | Critérios | Risco de abstração |
|---|---|---|---|
| AIaaS e SDK | consumo de inferência | dados, região, custo, limite, portabilidade | contrato do provedor vira contrato do produto |
| Framework de RAG/orquestração | contexto e fluxo | rastreabilidade, avaliação, extensibilidade | ocultar recuperação e prompt |
| Executor local | privacidade e autonomia | capacidade, operação, modelo, licença | custo operacional subestimado |
| Gateway | controle compartilhado | identidade, quota, política, failover | gargalo e menor denominador comum |

## Opções pesquisadas e matriz de acesso

| Categoria | Rota essencial sem cartão | Institucional | Comercial ou avançada | Pré-requisitos | Fonte e data de verificação |
|---|---|---|---|---|---|
| Playground/assistente — ChatGPT | ChatGPT Free: conta pode ser necessária conforme região; navegador, sem instalação, chave ou cartão para a rota. Os limites variam. | ChatGPT Edu/Business, se a instituição já disponibilizar conta. | Plus/Pro: assinatura opcional; não acrescenta pontos. | Essencial: navegador e, quando exigido, conta; sem chave. Pode haver limite de uso. | [FAQ do plano Free](https://help.openai.com/en/articles/9275245-using-chatgpt-s-free-tier), [FAQ geral](https://help.openai.com/en/articles/12677804-what-is-chatgpt-faq) — verificado em 16 jul. 2026. |
| Executor local — Ollama | Executar um modelo local pequeno ou apenas registrar a decisão de capacidade. Sem conta, chave ou cartão; requer instalação e espaço/CPU/RAM locais. | Laboratório institucional com máquina gerenciada, se houver. | Infraestrutura com GPU ou modelo maior é opcional e não acrescenta pontos. | Instalar Ollama e baixar modelo; custo potencial de hardware, energia e armazenamento, mesmo sem cobrança de serviço. | [Quickstart do Ollama](https://docs.ollama.com/quickstart), [requisitos no macOS](https://docs.ollama.com/macos) — verificado em 16 jul. 2026. |
| SDK de provedor / AIaaS — OpenAI SDK | Validar o contrato do adaptador com fixture local sintética, sem chamada remota, conta, chave ou cartão. Isso produz evidência de contrato, não inferência. | Chave disponibilizada pela instituição, se houver política e autorização. | Chave própria e créditos de API; opcional e sem vantagem. | Para chamada real: instalar SDK, criar conta e chave; há custo potencial de créditos/faturamento. Nunca registrar chave no projeto. | [Quickstart da API OpenAI](https://platform.openai.com/docs/quickstart/make-your-first-api-request) — verificado em 16 jul. 2026. |
| Framework de RAG/orquestração — LangChain | Instalar LangChain e executar fluxo com documentos, recuperador e resposta sintéticos/mocks locais; sem conta, chave ou cartão. | Serviço de avaliação/observabilidade institucional, se autorizado. | Integrações com provedores pagos são opcionais e não acrescentam pontos. | Python 3.10+ e instalação do pacote; uma chamada a modelo externo exigirá a credencial e as condições do provedor. | [Instalação do LangChain](https://docs.langchain.com/oss/python/langchain/install) — verificado em 16 jul. 2026. |
| Automação de agentes — n8n | Fluxo local com gatilho manual e nós que transformam JSON sintético; sem conta, chave ou cartão para esse fluxo. | n8n gerenciado pela instituição, se houver acesso concedido. | n8n Cloud ou integrações externas são opcionais e não acrescentam pontos. | Instalação local (por exemplo, Docker ou npm); cada integração externa pode exigir conta/credencial e gerar custo. | [Documentação de hospedagem do n8n](https://docs.n8n.io/hosting/) — verificado em 16 jul. 2026. |
| Observabilidade/avaliação — Langfuse | Registrar manualmente um traço e critérios sobre entradas/saídas sintéticas, ou auto-hospedar Langfuse localmente; sem cartão e sem chave de provedor para a evidência mínima. | Instância da instituição, somente com autorização e dados sintéticos. | Cloud/Enterprise e recursos licenciados são opcionais e não acrescentam pontos. | Auto-hospedagem requer Docker e serviços de armazenamento; pode exigir conta local e consome disco/CPU. Custos de infraestrutura continuam possíveis. | [Auto-hospedagem Langfuse](https://langfuse.com/self-hosting), [implantação com Docker Compose](https://langfuse.com/self-hosting/deployment/docker-compose) — verificado em 16 jul. 2026. |
| Gateway — LiteLLM Proxy | Instalar o proxy e apontá-lo para Ollama local, com prompt/saída sintéticos; sem conta, chave ou cartão. | Gateway institucional, se a equipe responsável autorizar o uso. | Provedores remotos, balanceamento corporativo e observabilidade comercial são opcionais e não acrescentam pontos. | Instalar `litellm[proxy]`; para provedor remoto, a respectiva chave e condições são necessárias. Um gateway não elimina custos do provedor. | [Quickstart do LiteLLM Proxy](https://docs.litellm.ai/docs/proxy/quick_start) — verificado em 16 jul. 2026. |

## Matriz de seleção

| Pergunta de decisão | Evidência mínima na rota essencial | Sinal para considerar rota institucional ou avançada |
|---|---|---|
| O dado pode sair do dispositivo? | classificação do dado sintético e fronteira de envio | política institucional, região ou contrato exigido |
| O contrato do modelo é portátil? | interface de entrada/saída e fixture de resposta | necessidade de múltiplos provedores ou failover |
| O fluxo recupera contexto de modo rastreável? | corpus sintético, consulta, trechos recuperados e resposta | escala, conectores ou avaliação gerenciada |
| O agente pode agir com segurança? | simulação sem efeitos externos, limites e aprovação humana | integração autorizada com sistemas reais |
| Como avaliar e operar? | caso de teste sintético, métrica definida e log redigido | retenção, RBAC, SSO, auditoria ou suporte contratado |

## Checklist de segurança e remoção

- [ ] O conjunto de dados, prompts, respostas e capturas é sintético e não contém dados pessoais, institucionais ou segredos.
- [ ] Não há chave, token, senha, URL privada ou arquivo `.env` versionado; credenciais nunca são solicitadas para a rota essencial.
- [ ] O grupo declara o provedor, a região quando aplicável, o dado enviado, os limites, o custo potencial e quem pode acessar a saída.
- [ ] A atividade pode ser reproduzida sem cartão por fixture, mock, executor local ou fluxo manual equivalente.
- [ ] O grupo registra como desligar a ferramenta, revogar acessos, apagar dados sintéticos e remover dependências.
- [ ] Uma opção institucional ou comercial é documentada como comparação, nunca como pré-requisito ou vantagem avaliativa.
