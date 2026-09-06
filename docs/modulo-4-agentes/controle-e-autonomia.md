# Chatbots, copilotos e agentes

Chatbot, copiloto, workflow e agente descrevem quem escolhe a próxima transição. O rótulo da interface não responde a essa pergunta.

## Quatro formas de controle operacional

Um **chatbot** oferece interação conversacional. Pode responder por conhecimento paramétrico, contexto fornecido ou RAG. Conversar em várias rodadas não implica escolher ferramentas nem produzir efeitos externos. A conversa é uma forma de interface.

Um **copiloto** apoia uma pessoa em uma tarefa: resume, sugere, preenche rascunhos ou propõe uma ação. A pessoa mantém o controle decisório e normalmente aciona o efeito em uma interface convencional. Um botão “aplicar sugestão” pode executar código determinístico; isso não transforma automaticamente o copiloto em agente.

Um **workflow determinístico** tem etapas, transições, condições e tratamento de erros definidos pela aplicação. Uma etapa pode usar um modelo para classificar texto ou gerar conteúdo, mas o modelo não decide livremente a próxima etapa. “Consultar pedido → validar regra → pedir aprovação → atualizar CRM” continua sendo workflow mesmo quando duas etapas são generativas.

Um **agente** é um sistema em que o modelo escolhe pelo menos parte do próximo passo — ferramenta, ordem, decomposição ou interrupção — para perseguir um objetivo, dentro de limites. O artigo [ReAct](https://openreview.net/forum?id=WE_vluYUL-X) investiga a combinação de raciocínio e ações intercaladas; arquiteturalmente, o valor está no ciclo observar–escolher–agir, não em expor raciocínio interno como prova. O trace deve registrar decisões observáveis e resultados, não alegar acesso fiel ao processo mental do modelo.

As categorias descrevem **controle**, não qualidade ou maturidade. Um workflow pode ser superior a um agente; um agente pode conversar; um copiloto pode chamar ferramentas somente de leitura para preparar uma sugestão. Pergunte sempre: quem escolhe a transição, quem executa o efeito e quem responde por ele?

## Geração, decisão e ação

Separe três atos numa trajetória:

- **geração:** produzir texto ou dados candidatos;
- **decisão:** selecionar uma opção segundo objetivo, evidência e política;
- **ação:** causar efeito observável fora da geração, como consultar, reservar, cancelar ou enviar.

O modelo pode participar dos três, mas controles determinísticos devem envolver decisões e ações. Uma proposta de reembolso é geração; verificar limite é regra; registrar reembolso é ação. Misturar os atos em “o agente resolveu” oculta fronteiras de autorização, teste e auditoria.

## O critério de entrada

Um agente é candidato quando: a sequência útil varia de modo difícil de enumerar; ferramentas devolvem feedback verificável; erros podem ser contidos; a tarefa tem conclusão observável; e orçamento/autoridade podem ser delimitados. Rejeite ou limite autonomia quando o caminho é estável, o efeito é irreversível, a autorização é ambígua, o feedback chega tarde ou não existe recuperação proporcional.

## Agente único e múltiplos agentes

No **agente único**, um planejador recebe objetivo e catálogo limitado. Há menos mensagens, estados e pontos de coordenação. É a opção inicial quando uma trajetória cabe num contexto controlável e uma equipe pode manter os contratos.

Em **múltiplos agentes**, papéis especializados — atendimento, política, pedido — trocam mensagens ou são coordenados por um supervisor. A divisão pode reduzir contexto por papel e permitir políticas distintas, mas não cria conhecimento nem confiabilidade automaticamente. Multiplica prompts, modelos possíveis, handoffs, latência, custo, estados, permissões e falhas de consenso. “Debate” entre modelos não é aprovação independente se todos compartilham a mesma evidência defeituosa.

Use múltiplos agentes quando houver fronteiras reais: domínios mantidos por equipes diferentes, contextos incompatíveis, competências ou credenciais separadas, ou paralelismo medido. Defina protocolo, proprietário do estado, limite de delegação, formato de entrega e regra de encerramento. Se a motivação for apenas organizar um prompt grande, módulos determinísticos ou ferramentas especializadas costumam ser mais simples.

**n8n** automatiza workflows; **LangGraph** e **AutoGen** organizam estados ou agentes. Nenhum delega autoridade: política e aprovação permanecem externas.

## Agente único versus múltiplos agentes

Comece com agente único e ferramentas estreitas. Adote múltiplos agentes apenas se um experimento demonstrar benefício de especialização, isolamento de contexto/autoridade ou paralelismo. Compare taxa de conclusão, ações indevidas, handoffs, latência, custo e capacidade de reconstruir traces. Um supervisor não elimina falha: precisa de contrato de delegação, orçamento global, regra de consenso e autoridade para interromper. Nunca permita que subagentes ampliem escopo, criem credenciais ou deleguem indefinidamente.

Esses mecanismos aparecem juntos no [Exemplo arquitetural](exemplo-arquitetural.md).
