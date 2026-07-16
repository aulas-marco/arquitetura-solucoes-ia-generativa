# Desenho — oficinas exploratórias com roteiro docente

## Objetivo

Transformar as seis oficinas em laboratórios compostos por experimentos independentes e permitir que o professor escolha o que executar em cada encontro.

## Padrão da página do aluno

Cada oficina terá um roteiro sugerido e experimentos numerados. Todo experimento contém: objetivo, pré-requisito, execute, observe, compare e questões exploratórias. Os experimentos são classificados como essencial em aula, exploração em dupla ou extensão.

## Material do professor

Criar orientações locais em `material-professor/`, não publicadas: duração, sequência recomendada, escolhas de execução, respostas esperadas, riscos de infraestrutura e alternativas quando a ferramenta local falhar.

## Módulo 1

Acrescentar Experimento D, por API local do Ollama. Com o mesmo corpus e pergunta, executar duas requisições `curl` para `http://localhost:11434/api/generate`: temperatura `0.1` e `0.9`. Comparar variação, fundamentação e limite; explicar que temperatura altera diversidade, não factualidade.

## Módulos 2–6

Dividir as receitas existentes em experimentos selecionáveis: adaptadores/contratos; RAG local; workflow e aprovação; testes de confiança; gateway/telemetria. Cada módulo recebe questões exploratórias conectadas a arquitetura, qualidade e risco.

## Critérios de aceite

1. Professor consegue selecionar experimentos sem reescrever a oficina.
2. Alunos distinguem execução obrigatória, exploração e extensão.
3. M1 executa e compara temperaturas reais por API local.
4. Material do professor permanece fora do site público.
5. Todas as rotas obrigatórias continuam locais, sintéticas e sem credenciais.
