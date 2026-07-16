# Letramento Aplicado em Ferramentas Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Atualizar o site-livro para combinar fundamentos arquiteturais com oficinas de ferramentas acessíveis e um projeto final comparativo em grupo.

**Architecture:** O conteúdo conceitual existente permanece como espinha dorsal. Cada módulo receberá uma página de oficina que conecta uma decisão arquitetural a uma prática curta, com três rotas de acesso equivalentes; referências compartilhadas concentrarão o catálogo de ferramentas e o projeto final, evitando repetir orientação operacional e política de acesso.

**Tech Stack:** Markdown, MkDocs Material, Python `unittest`, validador editorial em `scripts/validate_content.py`.

## Global Constraints

- Toda atividade obrigatória deve possuir rota essencial sem cartão de crédito, conta corporativa ou consumo pago.
- Rota institucional e rota comercial são opcionais e nunca atribuem vantagem de avaliação.
- Cada oficina declara instalação, conta, chave de API, cartão e custo antes da execução.
- Nenhuma chave, credencial, dado pessoal ou documento corporativo é versionado; usar corpus sintético quando necessário.
- Ferramentas são apresentadas por categoria e critério de decisão, sem dependência de fornecedor.
- As oficinas usam objetivos Bloom de lembrar, compreender, aplicar e analisar; avaliação e criação integradoras pertencem ao projeto final.
- Produtos e condições de gratuidade exigem pesquisa em documentação oficial na data da implementação; o texto deve registrar data de verificação, sem prometer que planos gratuitos são permanentes.
- A validação final obrigatória é `python -m unittest discover -s tests -v`, `python scripts/validate_content.py --all` e `mkdocs build --strict`.

---

## Estrutura de arquivos

| Arquivo | Responsabilidade |
|---|---|
| `docs/comecar/como-usar.md` | Explicar como preparar, escolher e registrar uma rota de oficina sem depender de gasto. |
| `docs/comecar/taxonomia-de-bloom.md` | Delimitar objetivos Bloom das oficinas e do projeto final. |
| `docs/modulo-{1..6}-*/oficina-de-ferramentas.md` | Uma prática independente por módulo: decisão, alternativas, rotas, atividade, evidência, segurança e extensão opcional. |
| `docs/referencia/guia-de-ferramentas.md` | Catálogo por categoria, critérios, matriz e transparência de acesso/custo. |
| `docs/sobre/projeto-final.md` | Enunciado, entregas, rubrica e regras do projeto comparativo em grupo. |
| `docs/sobre/plano-da-disciplina.md` | Ementa, programação, avaliação e oficinas atualizadas. |
| `docs/comecar/sobre-a-disciplina.md`, `docs/comecar/mapa-de-aprendizagem.md`, `docs/index.md`, `README.md` | Posicionamento público, percurso e instruções de uso atualizados. |
| `mkdocs.yml` | Navegação das sete páginas existentes mais a oficina em cada módulo; novas referências e página do projeto. |
| `tests/test_applied_literacy.py` | Contrato editorial das oficinas, rotas, Bloom, catálogo e projeto final. |
| `tests/test_pedagogical_shell.py` | Ajuste das expectativas para a oitava página de cada módulo. |

## Task 1: Criar o contrato testável de letramento aplicado

**Files:**
- Create: `tests/test_applied_literacy.py`
- Modify: `tests/test_pedagogical_shell.py`

**Interfaces:**
- Consumes: `scripts.validate_content.MODULES` e `scripts.validate_content.PAGES`.
- Produces: testes que exigem uma oficina por módulo, a política de três rotas, Bloom conservador, guia e projeto final.

- [ ] **Step 1: Escrever o teste de contrato das seis oficinas**

```python
from pathlib import Path
import re
import unittest

from scripts.validate_content import MODULES


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OFFICE = "oficina-de-ferramentas.md"


class AppliedLiteracyTest(unittest.TestCase):
    def test_every_module_has_an_accessible_tool_workshop(self):
        required = (
            "## Decisão arquitetural em foco",
            "## Roteiros equivalentes de acesso",
            "Essencial, sem cartão",
            "Institucional",
            "Comercial ou avançada",
            "## Atividade guiada",
            "## Evidência a entregar",
            "## Segurança e custo",
        )
        for slug in MODULES:
            text = (DOCS / slug / OFFICE).read_text(encoding="utf-8")
            with self.subTest(module=slug):
                for marker in required:
                    self.assertIn(marker, text)
                self.assertRegex(text, r"Bloom[^\n]*(Compreender|Aplicar|Analisar)")
                self.assertNotRegex(text, r"Bloom[^\n]*(Avaliar|Criar)")
                self.assertIn("não depende de cartão", text.casefold())
```

- [ ] **Step 2: Executar o teste para confirmar a falha inicial**

Run: `python -m unittest tests.test_applied_literacy.AppliedLiteracyTest.test_every_module_has_an_accessible_tool_workshop -v`  
Expected: FAIL com `FileNotFoundError` para `oficina-de-ferramentas.md`.

- [ ] **Step 3: Acrescentar os testes para o guia e o projeto final**

```python
    def test_shared_guide_and_group_project_preserve_equity(self):
        guide = (DOCS / "referencia" / "guia-de-ferramentas.md").read_text(encoding="utf-8").casefold()
        project = (DOCS / "sobre" / "projeto-final.md").read_text(encoding="utf-8").casefold()

        for term in ("sem cartão", "institucional", "comercial", "sdk", "framework", "gateway", "aiaas"):
            self.assertIn(term, guide)
        for term in ("grupo", "duas opções", "evidências", "uso de ferramenta paga não acrescenta pontos"):
            self.assertIn(term, project)
```

- [ ] **Step 4: Atualizar o contrato de navegação pedagógica**

Em `tests/test_pedagogical_shell.py`, substitua a expectativa de sete páginas por oito e exija o link da oficina em cada `index.md`:

```python
    def test_every_module_links_to_the_applied_workshop(self):
        for slug in MODULES:
            text = (DOCS / slug / "index.md").read_text(encoding="utf-8")
            with self.subTest(module=slug):
                self.assertIn("[Oficina de ferramentas](oficina-de-ferramentas.md)", text)
```

- [ ] **Step 5: Executar os testes novos e confirmar a falha**

Run: `python -m unittest tests.test_applied_literacy tests.test_pedagogical_shell -v`  
Expected: FAIL apenas por páginas e links ainda ausentes; os testes existentes continuam sendo descobertos.

- [ ] **Step 6: Fazer o commit do contrato editorial**

```bash
git add tests/test_applied_literacy.py tests/test_pedagogical_shell.py
git commit -m "test: define applied tool literacy contract"
```

## Task 2: Criar o guia compartilhado e o contrato do projeto final

**Files:**
- Create: `docs/referencia/guia-de-ferramentas.md`
- Create: `docs/sobre/projeto-final.md`
- Modify: `mkdocs.yml`

**Interfaces:**
- Consumes: política de acesso da especificação e testes de Task 1.
- Produces: páginas canônicas que as seis oficinas referenciam por caminhos relativos `../referencia/guia-de-ferramentas.md` e `../sobre/projeto-final.md`.

- [ ] **Step 1: Pesquisar opções de ferramenta atuais em fontes oficiais**

Pesquisar apenas documentação oficial, registrando URL e data de verificação para cada opção. Selecionar ao menos uma opção verificável para cada categoria: playground/assistente, execução local de modelo, SDK de provedor, orquestração/RAG, automação de agentes, observabilidade/avaliação e gateway. Para cada uma, confirmar explicitamente: necessidade de instalação, conta, chave, cartão e custo potencial.

- [ ] **Step 2: Escrever o guia de ferramentas com a matriz de acesso**

Criar `docs/referencia/guia-de-ferramentas.md` com estas seções e texto operacional:

```markdown
# Guia de ferramentas e plataformas

## Como ler este guia

Uma ferramenta é uma hipótese de implementação, não uma recomendação automática. Antes de adotá-la, registre a decisão, o contrato, o dado enviado, o custo, a forma de saída e o caminho de remoção.

## Regra de acesso justo

Nenhuma atividade obrigatória depende de cartão de crédito. A rota essencial, sem cartão, é suficiente para produzir a evidência e receber a nota máxima. A disponibilidade de planos gratuitos muda: confira a fonte oficial e a data de verificação indicada em cada oficina.

## Categorias e critérios

| Categoria | Decisão que apoia | Critérios | Risco de abstração |
|---|---|---|---|
| AIaaS e SDK | consumo de inferência | dados, região, custo, limite, portabilidade | contrato do provedor vira contrato do produto |
| Framework de RAG/orquestração | contexto e fluxo | rastreabilidade, avaliação, extensibilidade | ocultar recuperação e prompt |
| Executor local | privacidade e autonomia | capacidade, operação, modelo, licença | custo operacional subestimado |
| Gateway | controle compartilhado | identidade, quota, política, failover | gargalo e menor denominador comum |
```

Adicionar uma tabela de opções pesquisadas com as colunas `Categoria`, `Rota essencial sem cartão`, `Institucional`, `Comercial ou avançada`, `Pré-requisitos`, `Fonte e data de verificação`. Concluir com checklist de segurança e uma matriz de seleção.

- [ ] **Step 3: Escrever o enunciado do projeto final em grupo**

Criar `docs/sobre/projeto-final.md` com: propósito; formação de grupos; entregas obrigatórias; evidências mínimas; matriz de comparação de duas opções; regra de rota acessível; rubrica; apresentação e limites éticos. Incluir literalmente:

```markdown
## Equidade de acesso

Uso de ferramenta paga não acrescenta pontos. Quando uma opção comercial for comparada, o grupo deve declarar custo, condição de acesso e uma alternativa essencial sem cartão que permita reproduzir a evidência central.
```

E uma rubrica com os critérios `problema e requisitos`, `arquitetura e ADRs`, `comparação de ferramentas`, `evidências`, `segurança e governança`, `operação e custo`, cada qual com peso explícito totalizando 100 pontos.

- [ ] **Step 4: Incluir as páginas na navegação**

Em `mkdocs.yml`, inserir `Guia de ferramentas: referencia/guia-de-ferramentas.md` após `Catálogo de padrões` e `Projeto final: sobre/projeto-final.md` após `Plano da disciplina`.

- [ ] **Step 5: Executar os testes compartilhados**

Run: `python -m unittest tests.test_applied_literacy.AppliedLiteracyTest.test_shared_guide_and_group_project_preserve_equity -v`  
Expected: PASS.

- [ ] **Step 6: Fazer o commit das referências compartilhadas**

```bash
git add docs/referencia/guia-de-ferramentas.md docs/sobre/projeto-final.md mkdocs.yml
git commit -m "docs: add accessible tool guide and group project"
```

## Task 3: Implementar as oficinas dos módulos 1 e 2

**Files:**
- Create: `docs/modulo-1-fundamentos/oficina-de-ferramentas.md`
- Create: `docs/modulo-2-desenho-conceitual/oficina-de-ferramentas.md`
- Modify: `docs/modulo-1-fundamentos/index.md`
- Modify: `docs/modulo-2-desenho-conceitual/index.md`
- Modify: `mkdocs.yml`

**Interfaces:**
- Consumes: guia de ferramentas e formato testado na Task 1.
- Produces: oficinas de experimentação de modelo e seleção AIaaS/SDK/modelo autogerido, vinculadas ao módulo e à navegação.

- [ ] **Step 1: Escrever a oficina do Módulo 1**

Usar o título `# Oficina de ferramentas — comportamento de modelo e contexto`. Declarar Bloom como `Compreender e aplicar`. A atividade deve comparar, com prompt e corpus sintético fornecidos na página: resposta sem contexto, resposta com contexto e variação controlada de parâmetro. A evidência é tabela de observação de qualidade, fundamentação, latência percebida e limite. As três rotas são: interface gratuita/local sem cartão; ambiente institucional; API/assistente comercial opcional. Proibir dados pessoais e explicitar que resultados não provam qualidade geral.

- [ ] **Step 2: Escrever a oficina do Módulo 2**

Usar o título `# Oficina de ferramentas — escolher a fronteira de consumo`. Declarar Bloom como `Aplicar e analisar`. A atividade deve criar uma matriz para AIaaS/SDK, modelo aberto local/autogerido e camada de orquestração, com critérios de dados, custo, latência, operação, portabilidade e observabilidade. Exigir chamada mínima, configuração simulada ou análise de contrato público; não exigir chave. A evidência é uma mini-ADR com hipótese, escolha, alternativa e gatilho de revisão.

- [ ] **Step 3: Adicionar oficina aos índices e à navegação**

Adicionar a linha abaixo aos roteiros de ambas as páginas `index.md` e a entrada correspondente logo após `Estudo de caso` em cada grupo de módulo de `mkdocs.yml`:

```markdown
| **6. [Oficina de ferramentas](oficina-de-ferramentas.md)** | Como uma ferramenta torna visível a decisão estudada? | Uma evidência breve, comparável e segura. |
```

Renumerar `Exercícios` e `Síntese e referências` para 7 e 8 apenas na tabela, preservando todos os links existentes.

- [ ] **Step 4: Executar o contrato das oficinas e os testes dos dois módulos**

Run: `python -m unittest tests.test_applied_literacy tests.test_module_one tests.test_module_two -v`  
Expected: PASS.

- [ ] **Step 5: Fazer o commit das primeiras oficinas**

```bash
git add docs/modulo-1-fundamentos docs/modulo-2-desenho-conceitual mkdocs.yml
git commit -m "docs: add applied workshops for foundations and design"
```

## Task 4: Implementar as oficinas dos módulos 3 e 4

**Files:**
- Create: `docs/modulo-3-rag/oficina-de-ferramentas.md`
- Create: `docs/modulo-4-agentes/oficina-de-ferramentas.md`
- Modify: `docs/modulo-3-rag/index.md`
- Modify: `docs/modulo-4-agentes/index.md`
- Modify: `mkdocs.yml`

**Interfaces:**
- Consumes: formato das oficinas e guia de ferramentas.
- Produces: oficinas de RAG e fluxo agentivo com fronteiras de acesso e efeito.

- [ ] **Step 1: Escrever a oficina do Módulo 3**

Usar `# Oficina de ferramentas — observar um RAG fundamentado` e Bloom `Aplicar e analisar`. Fornecer corpus sintético pequeno e perguntas de referência; pedir para inspecionar ingestão, recuperação, citação e resposta. A rota essencial deve permitir fazer a atividade com recuperação manual estruturada ou ferramenta local, sem API; rotas institucional/comercial podem usar conectores. A evidência compara uma resposta com e sem evidência, registra proveniência, falha e hipótese de correção.

- [ ] **Step 2: Escrever a oficina do Módulo 4**

Usar `# Oficina de ferramentas — workflow, ferramenta e aprovação` e Bloom `Aplicar e analisar`. A prática usa uma operação de consulta em dados sintéticos, ação simulada e aprovação explícita; não conecta sistemas corporativos reais. A rota essencial pode usar diagrama/arquivo de configuração local e execução simulada; a comercial é opcional. A evidência identifica intenção, autorização, idempotência, aprovação, resultado autoritativo e condição de parada.

- [ ] **Step 3: Adicionar oficinas aos índices e à navegação**

Aplicar a mesma estrutura de oito etapas da Task 3 aos índices dos módulos 3 e 4 e inserir as duas páginas em `mkdocs.yml` após cada estudo de caso.

- [ ] **Step 4: Executar os testes dos módulos e contrato**

Run: `python -m unittest tests.test_applied_literacy tests.test_module_three tests.test_module_four -v`  
Expected: PASS.

- [ ] **Step 5: Fazer o commit das oficinas de conhecimento e agentes**

```bash
git add docs/modulo-3-rag docs/modulo-4-agentes mkdocs.yml
git commit -m "docs: add applied workshops for rag and agents"
```

## Task 5: Implementar as oficinas dos módulos 5 e 6

**Files:**
- Create: `docs/modulo-5-confianca/oficina-de-ferramentas.md`
- Create: `docs/modulo-6-operacao/oficina-de-ferramentas.md`
- Modify: `docs/modulo-5-confianca/index.md`
- Modify: `docs/modulo-6-operacao/index.md`
- Modify: `mkdocs.yml`

**Interfaces:**
- Consumes: formato de oficina, guia e contrato de projeto final.
- Produces: oficinas de avaliação/UX/guardrails e operação/gateway/FinOps que preparam diretamente o projeto em grupo.

- [ ] **Step 1: Escrever a oficina do Módulo 5**

Usar `# Oficina de ferramentas — testar confiança e experiência`. Declarar Bloom `Analisar`. Usar um conjunto sintético de casos: prompt injection, resposta sem evidência, recusa legítima, pedido ambíguo e escalonamento humano. A atividade compara comportamentos e registra se a interface informa limite, oferece recuperação e preserva dignidade do usuário. As rotas devem incluir análise manual ou ferramenta local como essencial; guardrail/eval de plataforma como opção institucional/comercial. A evidência é relatório de cinco casos, com decisão de aceitar, corrigir, escalar ou bloquear.

- [ ] **Step 2: Escrever a oficina do Módulo 6**

Usar `# Oficina de ferramentas — operar uma capacidade compartilhada`. Declarar Bloom `Analisar`. Fornecer traces e métricas sintéticas de qualidade, custo, latência, falha e uso por produto; pedir recomendação de gateway, quota, roteamento, SLO e ação de recuperação. A rota essencial usa os artefatos incluídos; opções institucional/comercial permitem observar dashboard ou gateway existente. A evidência é um parecer operacional com hipótese, métrica, limiar, proprietário e ação.

- [ ] **Step 3: Adicionar oficinas aos índices e à navegação**

Aplicar a mesma estrutura de oito etapas da Task 3 aos índices dos módulos 5 e 6 e inserir as páginas no grupo correto de `mkdocs.yml`.

- [ ] **Step 4: Executar os testes dos módulos e contrato**

Run: `python -m unittest tests.test_applied_literacy tests.test_module_five tests.test_module_six -v`  
Expected: PASS.

- [ ] **Step 5: Fazer o commit das oficinas de confiança e operação**

```bash
git add docs/modulo-5-confianca docs/modulo-6-operacao mkdocs.yml
git commit -m "docs: add applied workshops for trust and operations"
```

## Task 6: Atualizar ementa, percurso, Bloom e projeto pedagógico

**Files:**
- Modify: `docs/sobre/plano-da-disciplina.md`
- Modify: `docs/comecar/sobre-a-disciplina.md`
- Modify: `docs/comecar/mapa-de-aprendizagem.md`
- Modify: `docs/comecar/como-usar.md`
- Modify: `docs/comecar/taxonomia-de-bloom.md`
- Modify: `docs/index.md`
- Modify: `README.md`

**Interfaces:**
- Consumes: seis oficinas, guia e projeto final.
- Produces: promessa pública consistente e aderência explícita à ementa estendida.

- [ ] **Step 1: Atualizar a ementa e a programação de seis encontros**

Em `docs/sobre/plano-da-disciplina.md`, incorporar explicitamente: plataformas e bibliotecas; AI-as-a-Service, IA como commodity e AI Gateway; UX/chatbots; GenAI no desenvolvimento de software; geração e avaliação de alternativas; infraestrutura/FinOps; portfólio/conformidade; tendências. Em cada encontro, substituir `Experimento orientado` por `Oficina aplicada` com link para a página do módulo e identificar o objetivo Bloom. Incluir seção `## Projeto final em grupo` com link para `projeto-final.md`.

- [ ] **Step 2: Tornar a política de acesso visível ao aluno**

Em `docs/comecar/como-usar.md`, adicionar a seção `## Oficinas de ferramentas sem barreira financeira` explicando as três rotas, a suficiência da rota essencial e a proibição de dados sensíveis. Em `docs/comecar/taxonomia-de-bloom.md`, adicionar uma tabela que vincule oficinas a compreender/aplicar/analisar e projeto final a avaliar/criar.

- [ ] **Step 3: Atualizar apresentação, mapa, início e README**

Descrever a combinação de arquitetura e letramento aplicado sem prometer certificação em fornecedor. Linkar o guia e o projeto final em `docs/index.md` e `README.md`; no mapa, acrescentar as seis oficinas como faixas práticas subordinadas a cada decisão do percurso.

- [ ] **Step 4: Executar os testes de conteúdo compartilhado**

Run: `python -m unittest tests.test_shared_content tests.test_pedagogical_shell tests.test_applied_literacy -v`  
Expected: PASS.

- [ ] **Step 5: Fazer o commit do alinhamento curricular**

```bash
git add docs/sobre docs/comecar docs/index.md README.md
git commit -m "docs: align curriculum with applied tool literacy"
```

## Task 7: Validar o site completo e a publicação

**Files:**
- Modify only if a validator, teste ou construção indicar inconsistência: arquivos apontados pelo erro.

**Interfaces:**
- Consumes: todos os conteúdos e testes das Tasks 1–6.
- Produces: site MkDocs navegável e validação editorial íntegra.

- [ ] **Step 1: Executar a suíte completa**

Run: `python -m unittest discover -s tests -v`  
Expected: PASS, incluindo `AppliedLiteracyTest` e regressões dos seis módulos.

- [ ] **Step 2: Executar o validador editorial**

Run: `python scripts/validate_content.py --all`  
Expected: saída sem `ERRO`, com páginas, palavras, imagens e exercícios contados.

- [ ] **Step 3: Construir o site em modo estrito**

Run: `mkdocs build --strict`  
Expected: `Documentation built` sem avisos; todas as novas páginas resolvidas na navegação.

- [ ] **Step 4: Inspecionar a navegação construída**

Abrir a página inicial e um módulo no navegador local; confirmar que cada módulo exibe `Oficina de ferramentas`, que o guia e o projeto final aparecem no menu e que os links internos não levam a página ausente.

- [ ] **Step 5: Fazer o commit de eventuais correções de validação**

```bash
git add docs tests mkdocs.yml README.md scripts
git commit -m "test: verify applied course material"
```

Executar este commit somente se os passos 1–4 exigirem mudanças; não criar commit vazio.

## Revisão do plano

- Cobertura da especificação: Tasks 2–6 implementam as oficinas, guia, projeto, política de acesso e os novos tópicos; Task 7 confirma publicação e integridade.
- Acesso sem cartão: imposto pelo contrato de teste (Task 1), pelo guia (Task 2), pelas seis oficinas (Tasks 3–5) e pela apresentação (Task 6).
- Ferramentas comerciais: pesquisadas em fontes oficiais e tratadas como rota opcional, sem bônus de nota.
- Consistência: as oficinas usam o mesmo nome de arquivo, cabeçalhos, rotas e vínculo de navegação; o projeto usa o guia como referência canônica.
