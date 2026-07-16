# Oficina de ferramentas — avaliar decisões de confiança

**Objetivo Bloom:** Analisar.

Esta oficina executa uma avaliação local de cinco casos sintéticos. Ela transforma “parece seguro” em casos, respostas, critério e relatório inspecionável.

## Ferramenta

**DeepEval** é um framework open source para avaliar aplicações de IA. Nesta prática ele usa um juiz **Ollama** local para avaliar se a resposta observada se aproxima da decisão esperada: bloquear, corrigir ou escalar.

**Decisão arquitetural em foco:** como uma equipe registra comportamento esperado, falha observada e hipótese de correção sem reduzir confiança a uma única pontuação?

## Pré-requisitos

- Python 3.10 ou superior, terminal e Ollama instalado.
- Modelo `llama3.2:3b` já baixado com `ollama pull llama3.2:3b`.
- Uma pasta descartável. Os cinco casos fornecidos são sintéticos e não devem ser misturados a conversas reais.

## Instalação

### macOS

Baixe o Ollama em [ollama.com/download](https://ollama.com/download). No Terminal, execute:

```bash
python3 --version
mkdir oficina-m5
cd oficina-m5
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install deepeval
ollama pull llama3.2:3b
```

### Linux

Instale o Ollama pelo procedimento oficial em [ollama.com/download](https://ollama.com/download). No terminal Linux, execute:

```bash
python3 --version
mkdir oficina-m5
cd oficina-m5
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install deepeval
ollama pull llama3.2:3b
```

### Windows

Baixe o Ollama em [ollama.com/download](https://ollama.com/download). No PowerShell, execute:

```powershell
python --version
mkdir oficina-m5
cd oficina-m5
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install deepeval
ollama pull llama3.2:3b
```

> **Ao retomar a prática:** se você fechar o terminal, volte para `oficina-m5` e reative o ambiente: no macOS/Linux, `source .venv/bin/activate`; no Windows/PowerShell, `.venv\Scripts\Activate.ps1`. Com o ambiente ativo, `python` funciona nos três sistemas.

## Preparação do laboratório

Baixe os dois arquivos para a pasta `oficina-m5`:

- [casos_confianca.json](../assets/labs/modulo-5/casos_confianca.json) — entradas e decisões esperadas.
- [avaliar_confianca.py](../assets/labs/modulo-5/avaliar_confianca.py) — gera respostas locais, aplica a métrica e grava o relatório.

Confira os nomes antes de executar:

```bash
ls casos_confianca.json avaliar_confianca.py
```

Cada caso possui um identificador, uma entrada sintética e uma decisão esperada. A decisão esperada é a referência de avaliação; ela não é enviada como instrução ao usuário final.

## Execução

Com o Ollama em execução, rode:

```bash
python avaliar_confianca.py
```

## Receita principal

O script produz `relatorio-confianca.json` e imprime uma linha por caso. Cada item contém: caso, decisão esperada, resposta observada, pontuação e justificativa do avaliador. Abra o relatório:

```bash
python -m json.tool relatorio-confianca.json
```

## Resultado esperado

Você deve encontrar cinco resultados (`C-01` a `C-05`). Casos de injeção e tentativa de burlar identidade devem tender a bloqueio; pedido ambíguo deve pedir contexto; contestação deve escalar para um caminho humano. Uma pontuação não substitui a leitura da resposta e da justificativa.

## Interpretação

Escolha um único caso no JSON e altere somente `decisao_esperada`, por exemplo de `escalar` para `bloquear`. Execute novamente e compare o relatório. A variável controlada é a regra esperada; a resposta do modelo pode variar mesmo com temperatura baixa. Pergunte se a nova regra melhora segurança, experiência e recuperação — não trate a pontuação como veredito automático.

## Roteiro sugerido para aula

### Experimento A — caso adversarial (Essencial em aula)

**Objetivo**

Verificar uma decisão de bloqueio.

**Pré-requisito**

Relatório gerado.

**Execute**

Leia `C-01` e `C-03`.

**Observe**

Resposta, pontuação e justificativa.

**Compare**

Bloquear com explicação e bloquear sem próximo passo.

**Questões exploratórias:**

- Que parte da resposta pode expor informação protegida?
- Qual controle deve existir antes da geração?
- Como uma recusa preserva a dignidade da pessoa usuária?

### Experimento B — regra e avaliador (Exploração em dupla)

**Objetivo**

Distinguir comportamento observado de referência.

**Pré-requisito**

Caso alterado.

**Execute**

Mude uma decisão esperada e rode novamente.

**Observe**

Diferença do relatório.

**Compare**

Regra original e regra alterada.

**Questões exploratórias:**

- Quem aprova uma regra esperada antes de ela virar portão de qualidade?
- Que viés pode surgir se o mesmo modelo responde e julga?
- Que amostra humana ajudaria a calibrar a métrica?

### Experimento C — priorização de correção (Extensão)

**Objetivo**

Escolher uma hipótese de melhoria.

**Pré-requisito**

Dois relatórios.

**Execute**

Selecione uma falha.

**Observe**

Decisão, justificativa e impacto.

**Compare**

Corrigir prompt, contexto, guardrail ou UX.

**Questões exploratórias:**

- Qual falha deve bloquear uma entrega?
- Que evidência adicional evitaria falso bloqueio?
- Como versionar a regra e o conjunto de casos?

## Evidência a entregar

Entregue `relatorio-confianca.json` ou a tabela preenchida e uma conclusão de até cinco linhas.

| Caso | Decisão esperada | Resultado observado | Justificativa | Hipótese de correção |
|---|---|---|---|---|
| C-01 |  |  |  |  |
| C-02 |  |  |  |  |
| C-03 |  |  |  |  |
| C-04 |  |  |  |  |
| C-05 |  |  |  |  |

Indique uma falha que exigiria bloqueio, uma que exigiria melhoria de experiência e uma que precisaria de revisão humana.

## Limpeza e contingência

Saia do ambiente com `deactivate`. Apague `relatorio-confianca.json` se não quiser preservar a evidência local. Se o script falhar, confira `ollama list`, `python -m pip show deepeval` e a existência dos dois arquivos. Registre o erro e corrija o ambiente local com apoio do professor antes de prosseguir.
