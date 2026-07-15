# Infográficos de síntese para as páginas de conceitos

## Objetivo

Adicionar um infográfico didático de síntese a cada uma das seis páginas `conceitos.md` da disciplina **Arquitetura de Soluções com IA Generativa**. Cada imagem deve ajudar estudantes de pós-graduação a transformar o vocabulário do módulo em um modelo mental utilizável em decisões de arquitetura.

Os infográficos não repetem o texto da página nem substituem os diagramas dos estudos de caso. Eles funcionam como uma *visão de orientação*: mostram a pergunta arquitetural do módulo, as relações entre seus conceitos e as evidências que permitem defender uma decisão.

## Decisão de design

Será usada a abordagem **mapa de decisão arquitetural**, uma imagem por módulo. A composição padrão terá:

1. uma pergunta arquitetural explícita no topo;
2. três a cinco zonas visuais com os conceitos que precisam ser conectados;
3. fluxos direcionais, fronteiras ou ciclos que expressem causalidade e responsabilidade;
4. uma faixa final de evidências, decisões ou critérios de saída;
5. uma legenda editorial no Markdown e um texto alternativo completo.

O visual será editorial-técnico e compatível com a linguagem Academia do site: fundo claro quente, azul profundo e cobalto como cores estruturais, acentos em âmbar para decisão e coral para risco. Ícones e rótulos são auxiliares; a compreensão não dependerá somente de cor. O gerador não deve produzir parágrafos, tabelas densas, marcas, marcas-d’água ou texto pequeno. Rótulos essenciais permanecem curtos e legíveis em português.

## Escopo por módulo

| Módulo | Arquivo e ativo | Pergunta orientadora | Conteúdo do mapa |
| --- | --- | --- | --- |
| 1 — Fundamentos | `modulo-1-fundamentos/conceitos.md` e `m01-mapa-comportamento-generativo.png` | O que muda quando a arquitetura passa a depender de comportamento probabilístico? | Entrada e contexto → modelo → saída variável; tokens, prompt e parâmetros; conhecimento paramétrico; camadas de avaliação, segurança e observabilidade. |
| 2 — Desenho conceitual | `modulo-2-desenho-conceitual/conceitos.md` e `m02-mapa-da-oportunidade-ao-conops.png` | Como converter uma oportunidade em uma solução operável e justificável? | Oportunidade, hipótese de valor e capacidade, adequação/rejeição de IA, CONOPS, stakeholders, modos, responsabilidade humano–IA e requisitos significativos. |
| 3 — RAG | `modulo-3-rag/conceitos.md` e `m03-mapa-rag-dos-dois-pipelines.png` | Como fazer conhecimento externo chegar a uma resposta com evidência? | Fluxo offline de ingestão e fluxo online de consulta, fronteiras de autorização, fontes, índices, recuperação, citações, atualização e abstenção. |
| 4 — Agentes | `modulo-4-agentes/conceitos.md` e `m04-mapa-autonomia-controlada.png` | Onde termina a conversa e começa uma ação que precisa de controle? | Diálogo, workflow, agente e múltiplos agentes; planejamento; estado; ferramentas tipadas; políticas; aprovação humana e fronteiras de autonomia. |
| 5 — Confiança | `modulo-5-confianca/conceitos.md` e `m05-mapa-confianca-sistemica.png` | Como projetar confiança como propriedade verificável do sistema? | Perigo, risco inerente e residual; famílias de risco; controles em camadas; rastreabilidade proporcional; papéis; dimensões de avaliação. |
| 6 — Operação | `modulo-6-operacao/conceitos.md` e `m06-mapa-operacao-evidencia-continua.png` | Como operar comportamento de IA como um ativo evolutivo e auditável? | Pacote comportamental versionado, ambientes e promoção, avaliação contínua, entrega controlada, traces, métricas, privacidade, SLO e aprendizado. |

## Inserção e acessibilidade

Cada imagem será inserida imediatamente após o título de nível 1 da página `conceitos.md`, antes da primeira seção conceitual. A inserção seguirá o padrão Markdown já empregado pelo projeto:

```md
![Texto alternativo completo e específico](../assets/images/<arquivo>.png "Título curto da figura")

*Figura — legenda editorial que explica como ler o mapa e qual decisão ele apoia.*
```

O texto alternativo descreverá o fluxo, as fronteiras e a mensagem arquitetural sem depender de leitura óptica. A legenda acrescentará a interpretação pedagógica, não duplicará o `alt` e não dependerá de cor.

## Produção das imagens

As seis imagens serão geradas individualmente como infográficos arquiteturais em formato horizontal, com alto contraste e margem de segurança para a renderização responsiva. Cada prompt incluirá: objetivo didático, destinatário (pós-graduação), estrutura do mapa, paleta, rótulos mínimos em português, restrições de legibilidade e proibição de texto denso.

Depois de cada geração, a imagem será inspecionada para verificar:

- relações corretas entre os conceitos;
- ausência de rótulos ilegíveis ou texto inventado;
- contraste, composição e consistência com os ativos existentes;
- presença de todos os fluxos e fronteiras prometidos;
- adequação do conteúdo ao texto da página.

Os arquivos finais serão copiados para `docs/assets/images/`, sem sobrescrever imagens existentes.

## Integração e validação

Serão atualizados os seis arquivos `conceitos.md` e, quando necessário, os testes/validador de conteúdo para reconhecer os novos ativos. A entrega será validada por:

1. verificação de links e imagens locais;
2. testes automatizados do repositório;
3. `python scripts/validate_content.py --all`;
4. `mkdocs build --strict`;
5. inspeção visual do site gerado em uma página de conceitos de cada padrão relevante.

## Fora de escopo

- alterar a estrutura curricular, exercícios ou estudos de caso;
- substituir os diagramas de arquitetura já existentes;
- criar infográficos por seção individual;
- mudar a identidade visual global do site.
