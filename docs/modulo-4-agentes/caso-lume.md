# Caso contínuo: Banco Lume — autonomia

**Caso contínuo — Banco Lume.** [← Módulo 3: RAG](../modulo-3-rag/caso-lume.md) · [Módulo 5: Confiança e avaliação →](../modulo-5-confianca/caso-lume.md)

O [Módulo 2](../modulo-2-desenho-conceitual/caso-lume.md) decidiu manter o Banco Lume sem agente. O [Módulo 3](../modulo-3-rag/caso-lume.md) deu a ele seu próprio caminho de conhecimento (RAG). Este módulo reavalia autonomia com a evidência acumulada até aqui — e o Lume **não** chega à mesma conclusão da [Cooperativa Aurora](caso-aurora.md), tratada em sua própria página.

## Os critérios do ADR-001 continuam não atendidos

O ADR-001 do Módulo 2 previa reavaliar autonomia de agente somente "se uma atividade adicional demonstrar, em casos representativos, sequência não enumerável, benefício mensurável acima do workflow, autoridade clara por ferramenta e recuperação proporcional diante de falha". Depois da adoção de RAG no Módulo 3, a sequência do Lume continua a mesma: montar contexto, recuperar política vigente, gerar rascunho, validar suporte, recomendar, aprovar. Nenhum caso do modo sombra exigiu consultar fontes em ordem diferente da já prevista, e nenhuma evidência mostrou benefício mensurável de escolher a sequência dinamicamente.

**Decisão:** o Banco Lume permanece em **A1 — informar** na [matriz de autonomia](padroes-e-decisoes.md#matriz-de-autonomia): o modelo gera o rascunho, sem ferramenta de efeito e sem escolher a ordem de consulta; o orquestrador decide a sequência, não o modelo. Isto não é uma lacuna do desenho — é a leitura correta da evidência: **nem todo sistema evolui para agente**. Reavaliar exigiria uma nova atividade com sequência genuinamente não enumerável, ainda inexistente no escopo do Lume.

## Execução local

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

**Resultado esperado.** O script imprime a sequência fixa (contexto → rascunho → validação), sem decisão de ferramenta — o orquestrador segue a mesma ordem em toda execução, ao contrário do que se vê no [caso Aurora](caso-aurora.md).

**Limpeza.** `deactivate` e remover o diretório `.venv`. Nenhum dado real deve substituir os identificadores sintéticos do script.

---

**Continua:** [Módulo 5 — confiança e avaliação](../modulo-5-confianca/caso-lume.md)
