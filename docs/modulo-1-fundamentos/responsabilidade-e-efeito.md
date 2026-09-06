# Quem gera, decide, autoriza e executa

Separar geração de decisão, autorização e efeito é o que permite dizer quem responde por cada passo, e é a base de todas as decisões dos módulos seguintes.

## Como distribuir responsabilidade

A distribuição começa pelas condições que tornam o sistema aceitável. **Atributos de qualidade** descrevem como ele deve responder em situações relevantes: segurança, disponibilidade, desempenho, modificabilidade, observabilidade e outras características. Cada atributo precisa de cenário, medida e prioridade para orientar o desenho.

### Atributos de qualidade, trade-offs e significância

Mais contexto pode ampliar cobertura e piorar latência, custo e exposição. Trace detalhado pode ajudar diagnóstico e ferir minimização. Fallback pode melhorar disponibilidade e reduzir a qualidade da resposta. A primeira lei de Richards e Ford — “tudo é trade-off” — aplica-se à composição inteira ([*Fundamentals of Software Architecture*](https://www.oreilly.com/library/view/fundamentals-of-software-architecture/9781492043454/)).

Uma escolha é **arquiteturalmente significativa** quando influencia estruturas fundamentais, características prioritárias, dependências, responsabilidades ou custo de mudança. Reformular uma frase descartável pode permanecer uma decisão local. Enviar dados pessoais a um provedor, permitir ferramentas ou criar uma plataforma comum tende a exigir análise arquitetural.

### Geração, decisão, autorização e efeito

Quatro responsabilidades ajudam a traçar essas fronteiras:

| Responsabilidade | Pergunta |
|---|---|
| Geração | Que proposta o modelo produz? |
| Decisão | Que opção será seguida e por qual critério? |
| Autorização | Quem permite a ação sobre este recurso e finalidade? |
| Efeito | Que componente executa, confirma e recupera a mudança? |

O modelo **gera** uma proposta ou sugere um próximo passo. Uma regra, workflow ou pessoa **decide** conforme o caso. Uma política externa **autoriza** identidade, escopo e finalidade. Um componente transacional **executa** e registra o efeito. A separação permite testar contratos, restringir credenciais e atribuir responsabilidade sem exigir que toda solução tenha a mesma estrutura.

### Multimodalidade

Um sistema **multimodal** processa ou produz mais de um tipo de dado. Imagem, áudio e documentos digitalizados acrescentam etapas de extração, ameaças, acessibilidade e métricas próprias. Um modelo pode ler uma nota fiscal; regras ainda validam valores, e uma autoridade ainda aprova o efeito. Mudar a modalidade amplia a superfície, mas não transfere essas responsabilidades ao modelo.

O [Módulo 4](../modulo-4-agentes/index.md) aprofundará autonomia e ferramentas; o [Módulo 5](../modulo-5-confianca/index.md) tratará ameaças, controles e risco residual. Antes dessas decisões, porém, é necessário definir que evidência sustenta a aceitação do sistema.

## Mapa de responsabilidades

O mapa abaixo organiza perguntas recorrentes; não prescreve um estilo arquitetural nem exige todos os elementos em toda solução.

![Anatomia de uma solução generativa organizada em responsabilidades, do canal do usuário às capacidades transversais de segurança, governança, avaliação e observabilidade](../assets/images/m01-anatomia-solucao-generativa.png)
*Figura — Anatomia de referência: responsabilidades transversais atravessam o fluxo e não constituem uma etapa final.*

| Grupo | Responsabilidade |
|---|---|
| Canais e experiência | capturar intenção, consentimento, anexos e feedback; comunicar limites |
| Aplicação e APIs | autenticar, aplicar regras e transformar interação em solicitação estruturada |
| Orquestração | selecionar fluxo, coordenar componentes, preservar estado e recuperar falhas |
| Contexto e evidência | selecionar informação autorizada, registrar origem e montar contexto |
| Modelos e inferência | produzir geração ou representações por interfaces controladas |
| Ferramentas e efeitos | consultar ou agir por contratos, políticas e identidades delimitadas |
| Infraestrutura e operação | sustentar execução, redes, segredos, implantação e dependências |
| Capacidades transversais | aplicar segurança, governança, avaliação e observabilidade |

Conhecimento, contexto, estado, memória, evidência e trace atravessam esses grupos com finalidades e retenções próprias. Eles não formam uma única camada.

### Componentes e dependências

![Componentes de uma solução generativa: canal, aplicação, orquestrador, conhecimento autorizado, gateway de modelos e ferramentas corporativas sob segurança, governança, avaliação, observabilidade e operação](../assets/images/m01-componentes-dependencias.png)
*Figura — Um arranjo possível para discutir dependências; cada componente precisa de um direcionador.*

**Equivalente textual — componentes.** O canal envia uma solicitação à aplicação, que autentica a sessão e entrega um pedido estruturado ao orquestrador. O orquestrador pode solicitar evidência autorizada, montar contexto e pedir inferência. Se houver proposta de ferramenta, política e aplicação validam identidade, escopo e contrato antes de um executor determinístico produzir efeito. O resultado tipado retorna ao orquestrador — na notação da figura, `T -. "resultado tipado" .-> O`. Segurança, avaliação, observabilidade e operação atravessam o percurso.

### Três trajetórias

| Trajetória | Encadeamento | Responsabilidade dominante |
|---|---|---|
| Resposta | entrada → inferência → validação → rascunho | avaliar geração sob escopo |
| Evidência | identidade → política → recuperação → contexto → geração → validação | preservar fonte, autorização e suficiência |
| Ação | intenção → proposta → política → aprovação → executor → confirmação | separar geração, decisão, autorização e efeito |

Na trajetória de ação, o modelo gera proposta estruturada; política e responsável decidem e autorizam; executor idempotente produz o efeito. Na trajetória de evidência, recuperar um trecho não prova que ele sustenta a afirmação. Cada composição exige teste de software, avaliação comportamental e verificação arquitetural proporcionais.
