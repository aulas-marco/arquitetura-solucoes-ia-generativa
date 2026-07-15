# Método de referências

Este livro-texto usa um registro único de fontes para manter as atribuições verificáveis e coerentes entre os seis módulos. Cada item recebe um identificador estável em `fontes.yml`; mudanças de título, versão ou endereço devem ser atualizadas nesse registro antes de serem propagadas ao texto.

## Critérios de seleção

A preferência é por fontes primárias: artigos originais, normas e padrões publicados por seus organismos responsáveis, documentação oficial de projetos e publicações institucionais. Fontes secundárias servem apenas para descoberta ou contextualização e não devem sustentar afirmações técnicas quando a fonte original está disponível.

Os capítulos fornecidos pelo professor são fontes locais de apoio. Eles podem orientar sínteses e a organização pedagógica, mas seu conteúdo protegido não deve ser republicado. O texto do curso deve elaborar os conceitos com redação própria e apontar, quando necessário, para a obra ou para o identificador local correspondente.

## Atribuição no texto

Afirmações que dependem de uma fonte usam atribuição próxima ao trecho, com um link descritivo em vez de expressões vagas como “clique aqui”. Exemplo: “o [perfil de riscos para IA generativa do NIST](https://doi.org/10.6028/NIST.AI.600-1) organiza riscos e ações para sistemas generativos”. O texto do link deve revelar qual documento sustenta a afirmação.

O identificador de `fontes.yml` é a chave editorial durável. A URL é a rota de consulta. Para materiais locais, a chave `local://` identifica o exemplar preservado no acervo da disciplina e não deve ser convertida em link público.

## Princípios duráveis e detalhes mutáveis

O texto distingue princípios duráveis — por exemplo, defesa em profundidade, avaliação contextual e observabilidade orientada a objetivos — de detalhes de implementação que mudam com versões de APIs, modelos, bibliotecas e padrões. Um princípio pode ser explicado sem amarrá-lo a um fornecedor; um detalhe mutável deve informar a versão relevante e apontar para a documentação oficial vigente.

Documentos vivos ou instáveis, como especificações em evolução, bases de ameaças e documentação de ferramentas, sempre registram a data de acesso. Neste registro, a data de referência é **2026-07-14**. Ao revisar um módulo, o autor deve conferir se a versão citada continua atual e preservar a URL versionada quando a reprodutibilidade exigir.

## Citações e direitos autorais

O curso privilegia paráfrase analítica e síntese original. É proibida a cópia literal extensa de capítulos, artigos, normas ou páginas web. Citações diretas, quando indispensáveis, devem ser curtas, claramente marcadas e acompanhadas de atribuição e link para a fonte.

Imagens, tabelas e diagramas de terceiros não devem ser reproduzidos apenas por estarem acessíveis na web. O curso deve criar representações próprias ou confirmar uma licença compatível, mantendo a atribuição exigida.

## Manutenção do registro

Antes de adicionar uma nova referência:

1. confirme que a fonte é primária ou oficial;
2. escolha um `id` em kebab-case que não dependa de uma URL temporária;
3. registre título, autoria ou instituição, ano, URL canônica, data de acesso, tópicos, módulos e tipo;
4. use uma URL versionada quando o documento tiver revisões incompatíveis;
5. adicione a fonte à seção temática correspondente da bibliografia consolidada.
