# Oficina de ferramentas — escolher a fronteira de consumo

**Objetivo Bloom:** Aplicar e Analisar.

Esta oficina exercita uma escolha conceitual: onde a aplicação consome capacidade generativa e quais responsabilidades continuam visíveis. Não é uma recomendação de fornecedor nem requer uma chamada remota.

## Decisão arquitetural em foco

Consumir inferência por AIaaS/SDK, operar um modelo aberto localmente ou introduzir uma camada de orquestração altera as fronteiras de dados, operação e observação. A **atividade guiada** transforma essa escolha em hipótese verificável, em vez de escolher por familiaridade com uma ferramenta.

Use as categorias, critérios e avisos do [Guia de ferramentas e plataformas](../referencia/guia-de-ferramentas.md). Nenhuma opção descrita aqui promete disponibilidade, gratuidade ou adequação ao seu caso.

## Roteiros equivalentes de acesso

### Essencial, sem cartão

Preencha a matriz com base no contrato público de um SDK/AIaaS, na decisão de capacidade de um executor local e em uma configuração simulada de orquestração com entradas e saídas sintéticas. Uma fixture local pode representar a resposta de um SDK; não faça chamada remota. Esta rota não depende de cartão, conta, chave ou crédito e produz toda a evidência obrigatória.

### Institucional

Se houver ambiente institucional autorizado, examine um contrato, adaptador ou configuração já disponibilizados, sem enviar dados da instituição nem executar ação fora do escopo permitido. Registre apenas observações seguras e sintéticas. A rota institucional não acrescenta pontos: a matriz e a mini-ADR são as mesmas da rota essencial.

### Comercial ou avançada

Opcionalmente, faça uma chamada mínima autorizada ou inspecione uma camada comercial de orquestração, sempre com dados sintéticos e sem expor chaves. Declare custo potencial, condições de acesso e o dado que sairia da fronteira. A rota comercial ou avançada não acrescenta pontos e nunca é pré-requisito da atividade.

## Atividade guiada

A atividade obrigatória é realizável pela rota **Essencial, sem cartão**; ela não depende de cartão e não exige chave de API. Considere o cenário sintético: uma equipe quer redigir um resumo de solicitações fictícias de suporte e precisa manter o contrato de entrada e saída explícito.

1. Faça uma **chamada mínima simulada**, uma configuração de exemplo ou uma análise de contrato público para cada alternativa. Para AIaaS/SDK, descreva uma entrada `texto` e uma saída `resumo`, usando uma fixture local. Para modelo aberto local/autogerido, descreva a mesma entrada/saída e a capacidade operacional necessária. Para orquestração, descreva um fluxo que valida entrada, chama um adaptador simulado e registra a saída.
2. Preencha a matriz abaixo sem atribuir nota de “melhor” antes de declarar a hipótese. Compare dados, custo, latência, operação, portabilidade e observabilidade.
3. Escreva uma mini-ADR: hipótese, escolha provisória, alternativa preterida e gatilho que faria a equipe revisar a decisão. Essa mini-ADR é a evidência da atividade.

| Alternativa | Dados e fronteira de envio | Custo e limite | Latência | Operação | Portabilidade | Observabilidade |
|---|---|---|---|---|---|---|
| AIaaS/SDK |  |  |  |  |  |  |
| Modelo aberto local/autogerido |  |  |  |  |  |  |
| Camada de orquestração |  |  |  |  |  |  |

Não use dados pessoais, solicitações reais, documentos corporativos, credenciais, chaves ou URLs privadas. A decisão arquitetural em discussão é: **qual fronteira de consumo preserva o contrato e permite revisar a escolha quando os requisitos mudarem?**

## Evidência a entregar

Entregue a matriz preenchida e uma mini-ADR da atividade, de até 250 palavras. Inclua segurança e custo: declare que os dados são sintéticos, identifique custo potencial e explique quem teria acesso à entrada, à saída e aos registros.

```markdown
### Mini-ADR — fronteira de consumo

- **Hipótese:**
- **Escolha provisória:**
- **Alternativa considerada:**
- **Evidência da atividade:**
- **Gatilho de revisão:**
```

O gatilho pode ser uma nova restrição de dados, um limite de latência, aumento de custo, necessidade de auditoria ou mudança de portabilidade. A mini-ADR registra uma hipótese; não prova que uma alternativa é universalmente superior.

## Segurança e custo

A decisão arquitetural deve registrar o que atravessa cada fronteira, quem opera a capacidade e como observar falhas. Na atividade, a análise de contrato ou configuração simulada evita a necessidade de chave; se for feita uma chamada autorizada, remova credenciais e não armazene dados reais.

Mesmo uma rota local pode demandar instalação, hardware, energia e operação; AIaaS/SDK e orquestração podem trazer cobrança, retenção, limites ou dependência contratual. Documente esses riscos na evidência da atividade e mantenha a rota essencial como alternativa reproduzível sem cartão.
