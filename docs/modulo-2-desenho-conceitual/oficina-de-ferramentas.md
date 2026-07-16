# Oficina de ferramentas — estabilizar o contrato de consumo

**Objetivo Bloom:** Aplicar e Analisar.

Esta oficina cria um gateway local para tornar uma fronteira de consumo visível. O aluno envia uma requisição estável para a aplicação e escolhe o modelo no manifesto do gateway, sem alterar o cliente.

## Ferramenta

**LiteLLM Proxy** é um gateway open source que recebe uma interface compatível com APIs de chat e encaminha a solicitação para o modelo configurado. Nesta prática, ele encaminha para o **Ollama**, que executa o modelo localmente.

**Decisão arquitetural em foco:** qual contrato a aplicação deve consumir para preservar portabilidade, observação e possibilidade de troca do destino de inferência?

## Pré-requisitos

- Python 3.10 ou superior e um terminal.
- Ollama instalado e espaço para o modelo `llama3.2:3b`.
- Portas locais `11434` (Ollama) e `4000` (gateway) disponíveis.
- Uma pasta descartável para o laboratório e somente a solicitação sintética fornecida abaixo.

## Instalação

Primeiro confirme o interpretador disponível. Você precisa de Python 3.10 ou superior.

### macOS

Baixe o Ollama em [ollama.com/download](https://ollama.com/download). No Terminal, confirme Python e crie o ambiente:

```bash
python3 --version
mkdir oficina-m2
cd oficina-m2
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install 'litellm[proxy]'
ollama pull llama3.2:3b
```

Homebrew pode instalar utilitários complementares, mas não é necessário para esta prática.

### Linux

Instale o Ollama pelo procedimento atualizado em [ollama.com/download](https://ollama.com/download), adequado à sua distribuição. Depois, no terminal Linux, execute os mesmos comandos POSIX:

```bash
python3 --version
mkdir oficina-m2
cd oficina-m2
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install 'litellm[proxy]'
ollama pull llama3.2:3b
```

Não é necessário usar um gerenciador específico como `apt` ou `dnf`.

### Windows

Baixe o Ollama em [ollama.com/download](https://ollama.com/download). Abra o PowerShell e execute:

```powershell
python --version
mkdir oficina-m2
cd oficina-m2
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install 'litellm[proxy]'
ollama pull llama3.2:3b
```

Se o PowerShell bloquear a ativação, registre a mensagem e peça apoio ao professor ou ao suporte do computador; não altere políticas de segurança sem orientação.

> **Ao retomar a prática:** se você fechar o terminal, volte para `oficina-m2` e reative o ambiente antes de executar os comandos seguintes: no macOS/Linux, `source .venv/bin/activate`; no Windows/PowerShell, `.venv\Scripts\Activate.ps1`.

## Preparação do laboratório

Baixe e salve os dois arquivos na pasta `oficina-m2`:

- [litellm_config.yaml](../assets/labs/modulo-2/litellm_config.yaml) — o manifesto do gateway. `boreal-local` é o alias que a aplicação verá; `ollama/llama3.2:3b` é o destino local inicial.
- [request.json](../assets/labs/modulo-2/request.json) — a solicitação de chat sintética. O cliente usa o alias, não o nome físico do modelo.

Confirme que os dois arquivos estão presentes:

```bash
ls litellm_config.yaml request.json
```

## Execução

Abra **dois terminais** na pasta `oficina-m2`. No primeiro, inicie o gateway:

```bash
# macOS/Linux
source .venv/bin/activate
litellm --config litellm_config.yaml --port 4000
```

No Windows/PowerShell, use:

```powershell
.venv\Scripts\Activate.ps1
litellm --config litellm_config.yaml --port 4000
```

No segundo, envie a requisição pelo contrato do gateway:

```bash
curl http://localhost:4000/v1/chat/completions \
  -H 'Content-Type: application/json' \
  --data @request.json
```

## Receita principal

A requisição é entregue a `localhost:4000`, não diretamente ao Ollama. Observe no JSON de resposta a mensagem em `choices[0].message.content`. O manifesto é a fronteira explícita entre a aplicação e a capacidade de inferência.

Se `litellm` informar que a porta 4000 já está em uso, encerre o processo que a usa ou escolha outra porta e atualize o endereço do `curl`. Se o Ollama não responder, execute `ollama list` e confira se `llama3.2:3b` aparece na lista.

## Resultado esperado

Você deve receber uma resposta JSON do alias `boreal-local`. Registre três evidências: o arquivo de manifesto, a requisição JSON e a resposta. A prática prova que há um contrato de consumo observável; não mede qualidade geral, latência de produção ou adequação de um modelo ao domínio.

## Interpretação

Abra `litellm_config.yaml` e troque **somente** esta linha por um modelo que você já tenha baixado no Ollama, por exemplo `ollama/qwen2.5:3b`:

```yaml
model: ollama/qwen2.5:3b
```

Mantenha `model_name: boreal-local` e `request.json` inalterados. Reinicie o proxy e repita o mesmo `curl`. Esta é uma **troca controlada**: a única variável é o destino do manifesto. Compare a resposta e anote o que o cliente não precisou modificar.

## Roteiro sugerido para aula

### Experimento A — contrato pelo gateway (Essencial em aula)

**Objetivo**

Identificar o contrato consumido pela aplicação.

**Pré-requisito**

Proxy iniciado.

**Execute**

Envie `request.json`.

**Observe**

Alias, mensagens e resposta JSON.

**Compare**

Chamada para `localhost:4000` versus chamada direta ao modelo.

**Questões exploratórias:**

- Qual campo do contrato deve permanecer estável para o cliente?
- Onde a arquitetura deve registrar modelo e versão efetivamente usados?
- Que atributo de qualidade melhora quando o ponto de consumo é explícito?

### Experimento B — troca controlada do destino (Exploração em dupla)

**Objetivo**

Separar contrato público e modelo configurado.

**Pré-requisito**

Um segundo modelo já baixado.

**Execute**

Altere apenas o destino no manifesto.

**Observe**

A mesma requisição passa pelo mesmo alias.

**Compare**

Manifesto anterior, manifesto alterado e respostas.

**Questões exploratórias:**

- Qual alteração exigiria novo teste de regressão antes de produção?
- Que decisão reduz acoplamento entre produto e fornecedor/modelo?
- Que informação não pode faltar no log para reproduzir uma saída?

### Experimento C — mini-ADR reversível (Extensão)

**Objetivo**

Registrar uma escolha verificável.

**Pré-requisito**

Resultados de A e B.

**Execute**

Complete a mini-ADR.

**Observe**

Evidência disponível e limite não medido.

**Compare**

Manter o modelo atual, trocar o destino ou chamar o modelo diretamente.

**Questões exploratórias:**

- Que gatilho faria a equipe revisar essa fronteira?
- Como latência e observabilidade entram na decisão sem serem inferidas de uma chamada?
- Que risco aparece se o alias não for versionado no manifesto?

## Evidência a entregar

Entregue a tabela e uma mini-ADR de até 250 palavras.

| Item | Evidência observada | Limite da observação |
|---|---|---|
| Alias consumido |  |  |
| Modelo configurado |  |  |
| Entrada enviada |  |  |
| Resposta recebida |  |  |
| Troca controlada |  |  |

```markdown
### Mini-ADR — fronteira de consumo

- **Hipótese:**
- **Escolha provisória:**
- **Alternativa considerada:**
- **Evidência do laboratório:**
- **Gatilho de revisão:**
```

## Limpeza e contingência

Encerre o proxy com `Ctrl+C`, saia do ambiente com `deactivate` e remova a pasta `oficina-m2` se não precisar mais da evidência. Para liberar o espaço do modelo, use `ollama rm llama3.2:3b` somente se ele não será usado nas próximas oficinas.

Se a instalação falhar, registre a mensagem de erro, verifique `python --version`, `ollama --version` e as portas indicadas. A contingência é corrigir o ambiente local com o professor; não substitua a execução por uma resposta inventada ou por dados reais.
