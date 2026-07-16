# Arquitetura de Soluções com IA Generativa

Livro-texto digital da disciplina de pós-graduação **Arquitetura de Soluções com IA Generativa**, organizada em seis encontros de quatro horas. O material foi pensado para arquitetos, engenheiros e líderes técnicos que já dominam fundamentos de arquitetura de software e desejam projetar soluções generativas com critérios explícitos de qualidade, risco e operação.

O site combina conceitos, exemplos arquiteturais, estudos de caso, seis oficinas aplicadas e exercícios nos seis níveis da Taxonomia de Bloom. As oficinas desenvolvem letramento aplicado com dados sintéticos e rotas de acesso equivalentes; não são treinamento nem certificação de fornecedor. A leitura começa ampla, para criar um vocabulário comum, e avança até RAG, agentes, confiança, governança e LLMOps.

## Comece por aqui

Mesmo sem publicar o site, todo o conteúdo pode ser lido diretamente no GitHub:

- [Página inicial do livro-texto](docs/index.md)
- [Sobre a disciplina e seus objetivos](docs/comecar/sobre-a-disciplina.md)
- [Mapa de aprendizagem dos seis encontros](docs/comecar/mapa-de-aprendizagem.md)
- [Como estudar com este material](docs/comecar/como-usar.md)
- [Taxonomia de Bloom nos exercícios](docs/comecar/taxonomia-de-bloom.md)
- [Plano completo da disciplina](docs/sobre/plano-da-disciplina.md)
- [Guia de ferramentas e plataformas](docs/referencia/guia-de-ferramentas.md)
- [Projeto final em grupo](docs/sobre/projeto-final.md)

### Percurso em seis módulos

1. [Fundamentos de sistemas generativos](docs/modulo-1-fundamentos/index.md)
2. [Desenho conceitual e decisões](docs/modulo-2-desenho-conceitual/index.md)
3. [RAG e conhecimento verificável](docs/modulo-3-rag/index.md)
4. [Agentes, ferramentas e autonomia](docs/modulo-4-agentes/index.md)
5. [Confiança, avaliação e governança](docs/modulo-5-confianca/index.md)
6. [Operação, LLMOps e plataforma](docs/modulo-6-operacao/index.md)

Para consultas durante as aulas, use também o [glossário](docs/referencia/glossario.md), o [catálogo de padrões](docs/referencia/catalogo-de-padroes.md), os [cenários de atributos de qualidade](docs/referencia/atributos-de-qualidade.md) e o [template de ADR](docs/referencia/template-adr.md). Em qualquer oficina, a rota essencial sem cartão é suficiente para a entrega; rotas institucional e comercial são opcionais, não acrescentam pontos e nunca devem receber dados sensíveis.

## Organização do repositório

```text
.
├── docs/                  conteúdo público do site-livro
│   ├── comecar/           orientação para a jornada
│   ├── modulo-1-.../      um diretório para cada encontro
│   ├── referencia/        glossário, padrões e bibliografia
│   ├── sobre/             plano da disciplina
│   └── assets/            imagens, estilos e comportamento visual
├── tests/                 verificações automáticas do material
├── scripts/               validação editorial do conteúdo
├── mkdocs.yml             navegação e configuração do site
└── requirements.txt       dependências necessárias para publicar
```

O diretório `site/` é gerado automaticamente e não deve ser editado. As fontes do livro permanecem em `docs/`.

## Visualizar o site no computador

Não é necessário conhecer programação. Os comandos abaixo preparam um ambiente isolado, instalam o MkDocs e abrem uma prévia local.

### 1. Preparar uma única vez

No Terminal, dentro deste repositório, execute:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

No Windows PowerShell, substitua o segundo comando por:

```powershell
.venv\Scripts\Activate.ps1
```

### 2. Abrir a prévia

Com o ambiente ativado, execute:

```bash
mkdocs serve
```

Abra o endereço exibido no Terminal — normalmente `http://127.0.0.1:8000`. Alterações salvas nos arquivos Markdown aparecem automaticamente. Para encerrar, pressione `Ctrl+C`.

### 3. Conferir antes de publicar

```bash
python -m unittest discover -s tests -v
python scripts/validate_content.py --all
mkdocs build --strict
```

O último comando recria `site/` e interrompe a publicação se encontrar um problema de configuração ou navegação.

## Publicar gratuitamente no GitHub Pages

O repositório já inclui uma automação em [`.github/workflows/publicar-site.yml`](.github/workflows/publicar-site.yml). Ela instala as dependências, valida o site e publica o resultado sem chaves, senhas ou serviços externos.

1. Crie um repositório no GitHub e envie estes arquivos para a branch `main`.
2. No GitHub, abra **Settings → Pages**.
3. Em **Build and deployment → Source**, selecione **GitHub Actions**.
4. Abra a aba **Actions** para acompanhar a execução chamada “Publicar site no GitHub Pages”.
5. Quando a execução terminar, o endereço público aparecerá no ambiente `github-pages` e em **Settings → Pages**.

A automação roda a cada atualização da branch `main` e também pode ser iniciada manualmente pela aba **Actions**. Ela usa apenas as permissões mínimas fornecidas pelo próprio GitHub.

### Endereço definitivo do site

O arquivo `mkdocs.yml` não fixa nome de usuário nem endereço de repositório. Assim, o projeto continua portátil e os links e recursos relativos funcionam tanto na prévia local quanto no GitHub Pages.

Depois de criar o repositório, é opcional acrescentar ao início de `mkdocs.yml`:

```yaml
site_url: https://SEU-USUARIO.github.io/NOME-DO-REPOSITORIO/
```

Se o repositório se chamar `SEU-USUARIO.github.io`, use `https://SEU-USUARIO.github.io/`. Essa informação melhora metadados e links canônicos, mas não é necessária para construir ou publicar o site.

## Material exclusivo do professor

`material-professor/` contém orientações e gabaritos para uso docente. Ele é **intencionalmente local**, está protegido pelo `.gitignore` e não deve ser adicionado, forçado ou enviado ao repositório público. O site do aluno funciona sem esse diretório.

Antes do primeiro envio ao GitHub, confirme que `material-professor/` não aparece na lista de arquivos preparados para publicação.

## Status e licença

Material didático em desenvolvimento, preparado para a disciplina indicada acima. **Nenhuma licença de uso ou redistribuição foi definida neste repositório.** A pessoa responsável pelo material deve escolher e adicionar uma licença antes de autorizar reutilização pública por terceiros.
