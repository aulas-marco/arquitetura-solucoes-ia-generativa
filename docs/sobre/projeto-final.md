# Projeto final em grupo

## Propósito

Em grupo, desenhem e defendam uma solução de IA generativa para um problema delimitado. O objetivo é demonstrar decisão arquitetural: requisitos, contratos, dados, segurança, avaliação, operação, custo e remoção — não acumular ferramentas ou chamadas a modelos.

## Método de construção

Os grupos usarão SDD como arquitetura do trabalho, e não como documentação adicional no fim da entrega. Cada grupo deve manter uma **constitution** curta com princípios de engenharia, uma **spec** da capacidade principal, um plano técnico e tarefas organizadas em fatias verticais. Requisitos relevantes precisam apontar para critérios de aceite; tarefas precisam apontar para testes ou outra evidência verificável. Questões ainda abertas devem permanecer explícitas, sem serem convertidas silenciosamente em decisões.

O projeto terá três gates: aprovação da spec antes do plano, aprovação do plano antes da execução e aprovação das evidências antes da integração. No último gate, a revisão deve separar duas perguntas: “a solução implementa o comportamento especificado?” e “a implementação respeita segurança, arquitetura, testabilidade e padrões do repositório?”. O grupo pode usar agentes para elaborar e executar partes do fluxo, mas conserva autoria das decisões e responsabilidade pela entrega.

Spec Kit é o fio operacional recomendado para produzir e relacionar esses artefatos. Fluxos equivalentes são aceitáveis quando preservam intenção versionada, clarificação, rastreabilidade e gates. O método não substitui ADRs, threat model, evidências de avaliação ou análise dos atributos de qualidade; ele conecta esses elementos ao processo de construção.

## Formação de grupos

Formem grupos de três a cinco pessoas. Definam papéis de facilitação, arquitetura, evidências e revisão; todos respondem pelo conteúdo final. Grupos com outra composição só podem ser combinados com a docência antes da entrega.

## Entregas obrigatórias

1. Enunciado do problema, usuários, hipóteses, requisitos funcionais e atributos de qualidade.
2. Diagrama arquitetural com fronteiras de dados, componentes, contratos e dependências.
3. Pelo menos dois ADRs: escolha de modelo/execução e escolha de contexto, orquestração, gateway ou controle equivalente.
4. Comparação de duas opções tecnológicas para uma decisão relevante.
5. Evidências reprodutíveis com dados sintéticos: entrada, saída, critério de avaliação, resultado e limites conhecidos.
6. Plano de segurança, operação, custo potencial, observabilidade e remoção.

## Evidências mínimas

A evidência central deve ser reproduzível em uma execução local: entrada sintética, saída, contrato de entrada/saída, avaliação simples e registro de decisão. Não usem nem entreguem credenciais, dados pessoais, dados institucionais, segredos ou dados de produção. Capturas devem ocultar identificadores e chaves.

## Matriz de comparação de duas opções

| Critério | Opção A | Opção B | Decisão e evidência |
|---|---|---|---|
| Dados e privacidade |  |  |  |
| Contrato e portabilidade |  |  |  |
| Instalação, dependências e capacidade local |  |  |  |
| Avaliação e rastreabilidade |  |  |  |
| Operação, custo potencial e remoção |  |  |  |

## Reprodutibilidade do projeto

O grupo deve apresentar uma execução local que outra equipe consiga repetir com os mesmos arquivos sintéticos. Registrem versões, dependências, modelo, parâmetros, limite observado e limpeza do ambiente. A comparação de ferramentas deve discutir efeitos arquiteturais — dados, portabilidade, qualidade, operação e remoção — e não preferência por marca.

## Critérios de avaliação

| Critério | Peso | O que será observado |
|---|---:|---|
| problema e requisitos | 15% | Delimita usuários, hipótese de valor, fora de escopo e atributos de qualidade mensuráveis. Evite descrever solução antes de explicar o problema. |
| arquitetura e ADRs | 20% | Mostra fronteiras, contratos, responsabilidades, alternativas e consequências das decisões. |
| comparação de ferramentas | 15% | Compara duas opções pelos mesmos critérios e registra alternativa local ou open source equivalente. |
| evidências | 20% | Permite repetir a execução com dados sintéticos, mostrando resultado, método de avaliação e limites. |
| segurança e governança | 15% | Explica minimização, segredos, acesso, risco residual, responsabilidade humana e contestação. |
| operação e custo | 15% | Define observabilidade, falhas, capacidade, custo potencial, recuperação e remoção. |

## Apresentação

Cada grupo fará uma apresentação curta com problema, arquitetura, a decisão comparada, demonstração local e riscos. Todas as pessoas devem conseguir explicar as decisões e a evidência atribuída ao grupo.

## Limites éticos

Não automatizem decisões de alto impacto sobre pessoas, nem usem dados reais sensíveis, privados ou sem autorização. Mantenham humano responsável por qualquer ação consequente. Declarem vieses, incertezas, falhas esperadas, limites de uso e o mecanismo de interrupção/remediação.
