# Projeto final em grupo

## Propósito

Em grupo, desenhem e defendam uma solução de IA generativa para um problema delimitado. O objetivo é demonstrar decisão arquitetural: requisitos, contratos, dados, segurança, avaliação, operação, custo e remoção — não acumular ferramentas ou chamadas a modelos.

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

A evidência central deve ser reproduzível na rota essencial, sem cartão: uma fixture ou execução local, um contrato de entrada/saída, uma avaliação simples e um registro de decisão. Não usem nem entreguem credenciais, dados pessoais, dados institucionais, segredos ou dados de produção. Capturas devem ocultar identificadores e chaves.

## Matriz de comparação de duas opções

| Critério | Opção A | Opção B | Decisão e evidência |
|---|---|---|---|
| Dados e privacidade |  |  |  |
| Contrato e portabilidade |  |  |  |
| Instalação, conta, chave e cartão |  |  |  |
| Avaliação e rastreabilidade |  |  |  |
| Operação, custo potencial e remoção |  |  |  |

## Equidade de acesso

Uso de ferramenta paga não acrescenta pontos. Quando uma opção comercial for comparada, o grupo deve declarar custo, condição de acesso e uma alternativa essencial sem cartão que permita reproduzir a evidência central.

A rota essencial sem cartão é obrigatória; uma rota institucional ou comercial pode ser apresentada apenas como comparação e não confere vantagem. Planos, limites e preços podem mudar: registrem a fonte oficial e a data de verificação.

## Rubrica

| Critério | Peso | O que será observado |
|---|---:|---|
| problema e requisitos | 15 pontos | escopo, usuários, hipóteses e atributos de qualidade verificáveis |
| arquitetura e ADRs | 20 pontos | fronteiras, contratos, justificativas e consequências das decisões |
| comparação de ferramentas | 15 pontos | duas opções, critérios explícitos e alternativa acessível equivalente |
| evidências | 20 pontos | reprodução com dados sintéticos, resultado, avaliação e limites |
| segurança e governança | 15 pontos | minimização de dados, segredos, riscos, acesso e responsabilidade humana |
| operação e custo | 15 pontos | observabilidade, falhas, custo potencial, capacidade e caminho de remoção |
| **Total** | **100 pontos** |  |

## Apresentação

Cada grupo fará uma apresentação curta com problema, arquitetura, a decisão comparada, demonstração ou fixture da rota essencial e riscos. Todas as pessoas devem conseguir explicar as decisões e a evidência atribuída ao grupo.

## Limites éticos

Não automatizem decisões de alto impacto sobre pessoas, nem usem dados reais sensíveis, privados ou sem autorização. Mantenham humano responsável por qualquer ação consequente. Declarem vieses, incertezas, falhas esperadas, limites de uso e o mecanismo de interrupção/remediação.
