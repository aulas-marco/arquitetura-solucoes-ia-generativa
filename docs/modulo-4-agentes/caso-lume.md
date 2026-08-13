# Caso contínuo: Banco Lume — autonomia

**Caso contínuo — Banco Lume.** [← Módulo 3: RAG](../modulo-3-rag/caso-lume.md) · [Módulo 5: Confiança e avaliação →](../modulo-5-confianca/caso-lume.md)

O [Módulo 2](../modulo-2-desenho-conceitual/caso-lume.md) decidiu manter o Banco Lume sem agente. O [Módulo 3](../modulo-3-rag/caso-lume.md) deu a ele seu próprio caminho de conhecimento (RAG). Este módulo reavalia autonomia com a evidência acumulada até aqui — e o Lume **não** chega à mesma conclusão da [Cooperativa Aurora](caso-aurora.md), tratada em sua própria página.

## Os critérios do ADR-001 continuam não atendidos

O ADR-001 do Módulo 2 previa reavaliar autonomia de agente somente "se uma atividade adicional demonstrar, em casos representativos, sequência não enumerável, benefício mensurável acima do workflow, autoridade clara por ferramenta e recuperação proporcional diante de falha". Depois da adoção de RAG no Módulo 3, a sequência do Lume continua a mesma: montar contexto, recuperar política vigente, gerar rascunho, validar suporte, recomendar, aprovar. Nenhum caso do modo sombra exigiu consultar fontes em ordem diferente da já prevista, e nenhuma evidência mostrou benefício mensurável de escolher a sequência dinamicamente.

**Decisão:** o Banco Lume permanece em **A1 — informar** na [matriz de autonomia](padroes-e-decisoes.md#matriz-de-autonomia): o modelo gera o rascunho, sem ferramenta de efeito e sem escolher a ordem de consulta; o orquestrador decide a sequência, não o modelo. Isto não é uma lacuna do desenho — é a leitura correta da evidência: **nem todo sistema evolui para agente**. Reavaliar exigiria uma nova atividade com sequência genuinamente não enumerável, ainda inexistente no escopo do Lume.

## Execução local

**Objetivo.** Observar em código o que distingue **A1 — informar** (Lume) de **A2 — recomendar** (Aurora) na [matriz de autonomia](padroes-e-decisoes.md#matriz-de-autonomia): aqui o orquestrador decide a sequência e o modelo não escolhe ferramenta, ordem nem parada — ver também [quatro formas de controle operacional](conceitos.md#quatro-formas-de-controle-operacional).

**Pré-requisitos.** Python 3.11+, o mesmo padrão de venv das oficinas anteriores.

**Instalação.**

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install langgraph
```

**Execução.**

```bash
python docs/assets/labs/modulo-4/agente_lume_aurora.py --caso lume
```

**Resultado esperado.** O script imprime a sequência fixa de duas etapas (montar contexto → gerar rascunho); o `TRACE` confirma que nenhuma delas escolhe ferramenta — o orquestrador decide a ordem, não o modelo. Ao contrário do [caso Aurora](caso-aurora.md), aqui não existe orçamento de chamadas nem lista de ferramentas candidatas: são sempre as mesmas duas funções, na mesma ordem, em toda execução.

**Perguntas exploratórias.**

1. Rode o script e compare o `TRACE` com o do caso Aurora (`--caso aurora`). Em qual dos dois o modelo participa de alguma escolha — de ferramenta, ordem ou parada?
2. Se alguém propusesse deixar o modelo escolher a ordem entre "montar contexto" e "gerar rascunho", isso mudaria o nível de autonomia do Lume? Por quê, segundo o [critério de entrada](conceitos.md#o-criterio-de-entrada) para agentes?
3. Que evidência do ADR-001 (Módulo 2) continua justificando manter o Lume em A1 mesmo depois do RAG do Módulo 3?

**Entrega de evidência.** Registre a saída de uma execução (rascunho e trace completo) e aponte, no trace, em qual ponto estaria a "escolha" do modelo caso o Lume evoluísse para A2 — essa evidência alimenta o exercício [Autonomia orçada em execução real](exercicios.md#13-autonomia-orcada-em-execucao-real).

**Limpeza.** `deactivate` e remover o diretório `.venv`. Nenhum dado real deve substituir os identificadores sintéticos do script.

---

**Continua:** [Módulo 5 — confiança e avaliação](../modulo-5-confianca/caso-lume.md)
