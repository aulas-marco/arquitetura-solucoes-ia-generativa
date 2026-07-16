# Mapa de aprendizagem

O percurso acompanha a ampliação gradual da responsabilidade arquitetural: primeiro ler o sistema, depois escolher, conectar conhecimento, permitir ações, criar confiança e, por fim, sustentar a solução em escala.

```mermaid
flowchart LR
    A["1. Compreender<br/>Fundamentos"] --> B["2. Decidir<br/>Desenho conceitual"]
    B --> C["3. Fundamentar<br/>RAG e conhecimento"]
    C --> D["4. Agir<br/>Agentes e integração"]
    D --> E["5. Proteger e avaliar<br/>Confiança e governança"]
    E --> F["6. Operar e escalar<br/>LLMOps e plataforma"]
    A -. faixa prática .-> OA["Oficina 1"]
    B -. faixa prática .-> OB["Oficina 2"]
    C -. faixa prática .-> OC["Oficina 3"]
    D -. faixa prática .-> OD["Oficina 4"]
    E -. faixa prática .-> OE["Oficina 5"]
    F -. faixa prática .-> OF["Oficina 6"]
```

## 1. Compreender

Você reconhece modelos, componentes determinísticos e probabilísticos, contexto, conhecimento e capacidades transversais. O resultado é uma leitura arquitetural comum para discutir o restante do curso.

**Faixa prática:** a [oficina de comportamento de modelo e contexto](../modulo-1-fundamentos/oficina-de-ferramentas.md) torna visível o efeito de contexto e parâmetros em dados sintéticos.

## 2. Decidir

Você converte uma oportunidade em cenários, requisitos, atributos de qualidade e alternativas. O foco muda de “qual tecnologia usar?” para “qual decisão atende este contexto e como será validada?”.

**Faixa prática:** a [oficina de fronteira de consumo](../modulo-2-desenho-conceitual/oficina-de-ferramentas.md) compara AIaaS/SDK, execução local e orquestração por critérios arquiteturais.

## 3. Fundamentar

Você separa conhecimento, recuperação e geração; projeta os fluxos offline e online; e define como evidências, autorização e proveniência chegam à resposta.

**Faixa prática:** a [oficina de RAG fundamentado](../modulo-3-rag/oficina-de-ferramentas.md) contrasta resposta sem evidência, recuperação, citação e hipótese de correção.

## 4. Agir

Você conecta modelos a ferramentas e sistemas corporativos, modela estado e memória e define limites de autonomia, aprovação e recuperação de falhas.

**Faixa prática:** a [oficina de workflow, ferramenta e aprovação](../modulo-4-agentes/oficina-de-ferramentas.md) simula intenção, autorização, idempotência e efeito controlado.

## 5. Proteger e avaliar

Você trata confiança como propriedade do sistema. Ameaças, guardrails, privacidade, governança e avaliação passam a produzir evidências proporcionais ao risco.

**Faixa prática:** a [oficina de confiança e experiência](../modulo-5-confianca/oficina-de-ferramentas.md) avalia limites, recuperação e encaminhamento humano em casos sintéticos.

## 6. Operar e escalar

Você integra versionamento, observabilidade, SLOs, entrega controlada e recuperação. Por fim, decide o que padronizar em uma plataforma corporativa e o que manter sob autonomia dos times de produto.

**Faixa prática:** a [oficina de capacidade compartilhada](../modulo-6-operacao/oficina-de-ferramentas.md) relaciona gateway, quota, roteamento, SLO e recuperação a sinais operacionais sintéticos.

As etapas são cumulativas, mas não formam uma linha rígida. Evidências de avaliação podem obrigar a rever requisitos; incidentes podem revelar um limite de autonomia inadequado; mudanças no conhecimento podem alterar custo e latência. Arquitetar é percorrer esse mapa de forma iterativa e explícita.
