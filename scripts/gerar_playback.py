"""Gera a pagina de playback do laco a partir das transcricoes gravadas.

As transcricoes vem de `loop_objetivado.py --gravar`. Este script inlina os
dados na pagina para que o playback funcione sem rede e sem fetch relativo.

Uso: python scripts/gerar_playback.py
"""

from __future__ import annotations

import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
GRAVACOES = RAIZ / "docs" / "assets" / "labs" / "modulo-6" / "gravacoes"
DESTINO = RAIZ / "docs" / "modulo-7-operacao" / "playback-do-laco.md"

# Ordem deliberada: do pior desfecho ao aceitavel. O aluno ve primeiro
# o que da errado, e so entao o que uma execucao bem-sucedida custa.
SESSOES = [
    ("autodeclarada", "1. Sem verificador",
     "o modelo declara que terminou, e o laco acredita"),
    ("modelo-fraco", "2. Modelo sem capacidade",
     "o verificador funciona, o modelo nao da conta"),
    ("orcamento", "3. Orcamento curto",
     "tudo certo, menos o teto de iteracoes"),
    ("objetiva", "4. Convergencia",
     "o verificador aprova, no limite do orcamento"),
]


def carregar() -> list[dict]:
    dados = []
    for chave, titulo, resumo in SESSOES:
        d = json.loads((GRAVACOES / f"sessao-{chave}.json").read_text(encoding="utf-8"))
        d["chave"] = chave
        d["titulo"] = titulo
        d["resumo"] = resumo
        dados.append(d)
    return dados


def gerar() -> str:
    dados = carregar()
    payload = json.dumps(dados, ensure_ascii=False)
    cab = (CABECALHO
           .replace("__ESPEC__", dados[0]["especificacao"].strip())
           .replace("__SUITE__", dados[0]["suite"].strip()))
    return cab + PLAYER.replace("__DADOS__", payload) + RODAPE


CABECALHO = """# Playback: um laço objetivado, iteração por iteração

Esta página é autossuficiente: dá para lê-la sem ter feito a oficina e sem outra página aberta. Ela reproduz **quatro execuções reais** de um agente que escreve código sozinho, gravadas com `loop_objetivado.py --gravar`. Nada roda aqui. O que você vê são as entradas e as saídas registradas na máquina onde o laço executou.

A gravação existe por dois motivos. Executar ao vivo custa minutos de espera por um resultado já conhecido, e o objeto de estudo não é a velocidade do modelo. E, sobretudo, algumas dessas execuções levam oito iterações para chegar a lugar nenhum — poder pular, voltar e comparar vale mais do que assistir.

## Antes do player: o que é um laço agêntico

Um agente é um modelo cercado de código, configuração e lógica de execução. Esse conjunto tem nome: **arnês**. A pergunta seguinte é **quem aciona o arnês, e quantas vezes** — e a resposta se organiza numa escada de quatro degraus, em que **a cada degrau você entrega uma coisa a mais para a máquina**:

| Nível | O que dispara | O que você entrega | Como o laço para |
|---|---|---|---|
| 1 — por rodada | seu *prompt* | a verificação | o agente julga que terminou |
| 2 — por objetivo | seu *prompt*, uma vez | a condição de parada | um critério objetivo é satisfeito, ou o teto é atingido |
| 3 — por tempo | um agendamento | o gatilho | você cancela ou o trabalho termina |
| 4 — proativo | um evento, sem pessoa presente | o próprio *prompt* | a rotina roda até ser desligada |

**As quatro gravações desta página são do nível 2**, e a fronteira entre o nível 1 e o nível 2 é a coisa mais importante a entender aqui. No nível 1, o agente para quando **acha** que terminou. No nível 2, ele para quando um critério objetivo é satisfeito. Trocar julgamento por critério é o que permite tirar a pessoa da frente sem trocar supervisão por esperança.

Enquanto uma pessoa acompanha, ela é o verificador implícito de última instância: lê a saída, percebe o disparate e interrompe. Ao remover a pessoa, essa função precisa existir em outro lugar, **escrita e executável**. Se não existir, o pior desfecho não é a fatura — é o **falso positivo**, quando o sistema declara conclusão, encerra, e ninguém confere. A primeira aba do player é exatamente isso.

## A tarefa que o laço tenta resolver

Produzir uma função `normalizar_pedido(texto)` que converta uma linha de pedido num dicionário. A especificação que o modelo recebe é esta:

```text
__ESPEC__
```

E o **verificador** é esta suíte de cinco testes. Ela não é sugestão nem documentação: é a condição de parada. O laço só encerra por mérito quando `pytest` devolve 5/5.

```python
__SUITE__
```

## O arnês deste laço

Cada peça abaixo foi necessária para o laço funcionar. Vale ler antes de abrir o player, porque a coluna da direita é o que você vai ver acontecendo na tela.

| Componente | Como aparece aqui |
|---|---|
| *Prompt* de sistema | instrui a devolver só o bloco de código; muda conforme a condição de parada escolhida |
| Contexto | a especificação, a suíte e **a versão anterior do próprio código** entram no pedido de cada iteração |
| *Sandbox* | tudo é escrito numa pasta `loop-sandbox`; o `pytest` roda como subprocesso ali dentro |
| Guarda estática | a árvore sintática do código gerado é analisada, e `import` fora de uma lista curta, `exec`, `open` e atributos com prefixo duplo são recusados antes de qualquer execução |
| Verificador | `pytest` com cinco casos; o relatório de falha volta ao modelo na iteração seguinte |
| Orçamento | teto de iterações, com comportamento definido no esgotamento |
| Detecção de estagnação | duas iterações com o mesmo relatório de falha elevam a temperatura, em vez de repetir a mesma chamada |

Essa última linha existe por um motivo empírico que vale antecipar: **com temperatura zero e contexto idêntico, o modelo devolve exatamente a mesma resposta**. Um laço determinístico sobre entrada constante é um laço que não itera. Por isso o arnês sobe a temperatura de 0,0 para 0,4 e depois 0,8 quando percebe que o verificador devolveu a mesma falha — é a única forma de escapar do ponto fixo.

## Como ler o player

As quatro abas estão em ordem deliberada, **do pior desfecho ao aceitável**. Comece pela primeira.

Cada iteração mostra três colunas:

- **Entrada** — o que o arnês enviou ao modelo naquela rodada: o relatório de falha da iteração anterior e a versão anterior do código. Na primeira iteração não há relatório, só a especificação.
- **Saída** — o código que o modelo devolveu. A partir da segunda iteração, as linhas que **não existiam antes** aparecem destacadas em verde. É onde se vê o que de fato mudou entre uma tentativa e a seguinte, que costuma ser bem menos do que parece.
- **Verificador** — o veredito da guarda estática e o resultado do `pytest`, com a primeira falha.

Abaixo, a barra de estado traz temperatura, tokens acumulados e o aviso de estagnação. A linha do tempo no topo é clicável: a cor da borda superior indica quantos testes passaram naquela iteração.

"""

PLAYER = r"""
<div class="pb" id="pb">
  <div class="pb-sessoes" role="tablist" aria-label="Sessões gravadas"></div>

  <div class="pb-ficha">
    <div><span class="pb-rot">Modelo</span><b class="pb-modelo"></b></div>
    <div><span class="pb-rot">Condição de parada</span><b class="pb-cond"></b></div>
    <div><span class="pb-rot">Orçamento</span><b class="pb-orc"></b></div>
    <div><span class="pb-rot">Verificador</span><b class="pb-verif"></b></div>
  </div>

  <div class="pb-controles">
    <button class="pb-btn" data-acao="inicio" title="Primeira iteração" aria-label="Primeira iteração">⏮</button>
    <button class="pb-btn" data-acao="anterior" title="Iteração anterior" aria-label="Iteração anterior">◀</button>
    <button class="pb-btn pb-play" data-acao="play" aria-label="Reproduzir">▶ Reproduzir</button>
    <button class="pb-btn" data-acao="proxima" title="Próxima iteração" aria-label="Próxima iteração">▶</button>
    <button class="pb-btn" data-acao="fim" title="Última iteração" aria-label="Última iteração">⏭</button>
    <label class="pb-vel">Ritmo
      <select class="pb-select">
        <option value="3200">lento</option>
        <option value="2000" selected>normal</option>
        <option value="1100">rápido</option>
      </select>
    </label>
  </div>

  <ol class="pb-linha" aria-label="Linha do tempo das iterações"></ol>

  <div class="pb-palco">
    <section class="pb-col pb-entrada">
      <h4>Entrada <span class="pb-tag">o que o arnês enviou ao modelo</span></h4>
      <div class="pb-corpo"></div>
    </section>
    <section class="pb-col pb-saida">
      <h4>Saída <span class="pb-tag">o código que o modelo devolveu</span></h4>
      <div class="pb-corpo"></div>
    </section>
    <section class="pb-col pb-verificador">
      <h4>Verificador <span class="pb-tag">guarda estática e pytest</span></h4>
      <div class="pb-corpo"></div>
    </section>
  </div>

  <div class="pb-estado"></div>
  <div class="pb-final" hidden></div>
</div>

<style>
.pb{border:1px solid var(--color-border,#CED9E9);border-radius:.45rem;background:var(--color-surface,#fff);padding:1rem;margin:1.5rem 0;font-family:var(--course-body-font,system-ui)}
.pb *{box-sizing:border-box}
.pb-sessoes{display:flex;flex-wrap:wrap;gap:.4rem;margin-bottom:.85rem}
.pb-sessoes button{flex:1 1 12rem;text-align:left;padding:.5rem .7rem;border:1px solid var(--color-border,#CED9E9);border-radius:.3rem;background:var(--course-paper,#F2F6FB);color:var(--color-text,#16243A);cursor:pointer;font:inherit;line-height:1.3}
.pb-sessoes button b{display:block;font-size:.92rem}
.pb-sessoes button span{font-size:.76rem;color:var(--color-text-muted,#56677F)}
.pb-sessoes button[aria-selected=true]{background:var(--course-ink,#16243A);border-color:var(--course-ink,#16243A);color:#fff}
.pb-sessoes button[aria-selected=true] span{color:#C5D3E8}
.pb-ficha{display:flex;flex-wrap:wrap;gap:.35rem 1.6rem;padding:.6rem .75rem;background:var(--course-paper,#F2F6FB);border-radius:.3rem;margin-bottom:.85rem;font-size:.82rem}
.pb-rot{display:block;color:var(--color-text-muted,#56677F);font-size:.7rem;text-transform:uppercase;letter-spacing:.05em}
.pb-ficha b{font-family:var(--course-meta-font,monospace);font-weight:600;font-size:.85rem}
.pb-controles{display:flex;flex-wrap:wrap;align-items:center;gap:.4rem;margin-bottom:.75rem}
.pb-btn{padding:.4rem .7rem;border:1px solid var(--course-cobalt,#254DB8);border-radius:.3rem;background:#fff;color:var(--course-cobalt,#254DB8);cursor:pointer;font:inherit;font-size:.85rem}
.pb-btn:hover:not(:disabled){background:var(--course-cobalt,#254DB8);color:#fff}
.pb-btn:disabled{opacity:.35;cursor:default}
.pb-play{font-weight:600;min-width:8.5rem}
.pb-vel{margin-left:auto;font-size:.78rem;color:var(--color-text-muted,#56677F)}
.pb-vel select{margin-left:.35rem;font:inherit;padding:.2rem .3rem;border:1px solid var(--color-border,#CED9E9);border-radius:.25rem;background:#fff;color:var(--color-text,#16243A)}
.pb-linha{display:flex;flex-wrap:wrap;gap:.3rem;list-style:none;margin:0 0 .9rem;padding:0}
.pb-linha li{flex:1 1 2.6rem}
.pb-linha button{width:100%;padding:.3rem .2rem;border:1px solid var(--color-border,#CED9E9);border-top-width:3px;border-radius:.25rem;background:#fff;cursor:pointer;font-family:var(--course-meta-font,monospace);font-size:.72rem;color:var(--color-text,#16243A);line-height:1.25}
.pb-linha button small{display:block;font-size:.66rem;color:var(--color-text-muted,#56677F)}
.pb-linha button[data-nivel=parcial]{border-top-color:var(--course-amber,#F2B84B)}
.pb-linha button[data-nivel=completo]{border-top-color:#2E7D5B}
.pb-linha button[data-nivel=recusado]{border-top-color:#B3402F}
.pb-linha button[aria-current=true]{background:var(--course-ink,#16243A);color:#fff;border-color:var(--course-ink,#16243A)}
.pb-linha button[aria-current=true] small{color:#C5D3E8}
.pb-palco{display:grid;grid-template-columns:repeat(auto-fit,minmax(15rem,1fr));gap:.7rem}
.pb-col{border:1px solid var(--color-border,#CED9E9);border-radius:.3rem;overflow:hidden;min-width:0}
.pb-col h4{margin:0;padding:.4rem .6rem;background:var(--course-paper,#F2F6FB);border-bottom:1px solid var(--color-border,#CED9E9);font-size:.8rem;font-family:var(--course-body-font,system-ui);font-weight:600}
.pb-tag{display:block;font-weight:400;font-size:.7rem;color:var(--color-text-muted,#56677F)}
.pb-corpo{padding:.55rem .6rem;max-height:21rem;overflow:auto}
.pb-corpo pre{margin:0;font-family:var(--course-meta-font,monospace);font-size:.74rem;line-height:1.5;white-space:pre-wrap;overflow-wrap:anywhere}
.pb-corpo .pb-nova{background:#E4F2EA;border-left:3px solid #2E7D5B;padding-left:.3rem;margin-left:-.3rem;display:block}
.pb-vazio{color:var(--color-text-muted,#56677F);font-size:.78rem;font-style:italic}
.pb-selo{display:inline-block;padding:.1rem .45rem;border-radius:.2rem;font-family:var(--course-meta-font,monospace);font-size:.72rem;font-weight:600;margin-bottom:.4rem}
.pb-selo.ok{background:#E4F2EA;color:#1E5C41}
.pb-selo.parcial{background:#FCF0D8;color:#5D4514}
.pb-selo.ruim{background:#F8E3DF;color:#8A2E20}
.pb-estado{display:flex;flex-wrap:wrap;gap:.3rem .9rem;margin-top:.7rem;padding:.5rem .65rem;background:var(--course-paper,#F2F6FB);border-radius:.3rem;font-family:var(--course-meta-font,monospace);font-size:.76rem}
.pb-estado span b{color:var(--course-cobalt,#254DB8)}
.pb-alerta{width:100%;color:#8A2E20;font-weight:600}
.pb-final{margin-top:.7rem;padding:.65rem .75rem;border-radius:.3rem;border-left:4px solid var(--course-ink,#16243A);background:var(--course-paper,#F2F6FB);font-size:.85rem}
.pb-final b{font-family:var(--course-meta-font,monospace)}
@media (max-width:44rem){.pb-palco{grid-template-columns:1fr}.pb-corpo{max-height:15rem}}
</style>

<script>
(function(){
  var DADOS = __DADOS__;
  var raiz = document.getElementById('pb');
  if(!raiz || !DADOS.length) return;
  var iSes = 0, iIter = 0, timer = null, ritmo = 2000;

  var elSes = raiz.querySelector('.pb-sessoes'),
      elLinha = raiz.querySelector('.pb-linha'),
      elEstado = raiz.querySelector('.pb-estado'),
      elFinal = raiz.querySelector('.pb-final'),
      elPlay = raiz.querySelector('.pb-play'),
      corpo = {
        entrada: raiz.querySelector('.pb-entrada .pb-corpo'),
        saida: raiz.querySelector('.pb-saida .pb-corpo'),
        verificador: raiz.querySelector('.pb-verificador .pb-corpo')
      };

  function esc(s){ return String(s == null ? '' : s).replace(/[&<>]/g, function(c){ return {'&':'&amp;','<':'&lt;','>':'&gt;'}[c]; }); }
  function ses(){ return DADOS[iSes]; }
  function iter(){ return ses().iteracoes[iIter]; }

  DADOS.forEach(function(d, i){
    var b = document.createElement('button');
    b.type = 'button'; b.setAttribute('role','tab');
    b.innerHTML = '<b>' + esc(d.titulo) + '</b><span>' + esc(d.resumo) + '</span>';
    b.addEventListener('click', function(){ parar(); iSes = i; iIter = 0; montar(); });
    elSes.appendChild(b);
  });

  function montar(){
    var d = ses();
    Array.prototype.forEach.call(elSes.children, function(b, i){ b.setAttribute('aria-selected', i === iSes); });
    raiz.querySelector('.pb-modelo').textContent = d.modelo;
    raiz.querySelector('.pb-cond').textContent = d.condicao_de_parada === 'testes' ? 'pytest aprova' : 'o modelo declara';
    raiz.querySelector('.pb-orc').textContent = d.orcamento + ' iterações';
    raiz.querySelector('.pb-verif').textContent = 'pytest, ' + d.total_testes + ' casos';
    elLinha.innerHTML = '';
    d.iteracoes.forEach(function(it, i){
      var li = document.createElement('li'), b = document.createElement('button');
      b.type = 'button';
      var nivel = it.guarda === 'recusado' ? 'recusado' : (it.testes_passaram === d.total_testes ? 'completo' : 'parcial');
      b.dataset.nivel = nivel;
      var marca = it.guarda === 'recusado' ? '—' : it.testes_passaram + '/' + d.total_testes;
      b.innerHTML = esc(it.n) + '<small>' + esc(marca) + '</small>';
      b.addEventListener('click', function(){ parar(); iIter = i; pintar(); });
      li.appendChild(b); elLinha.appendChild(li);
    });
    pintar();
  }

  function linhasNovas(atual, anterior){
    var antes = {}; (anterior || '').split('\n').forEach(function(l){ antes[l.trim()] = 1; });
    return atual.split('\n').map(function(l){
      var nova = l.trim() && !antes[l.trim()];
      return nova ? '<span class="pb-nova">' + esc(l) + '</span>' : esc(l);
    }).join('\n');
  }

  function pintar(){
    var d = ses(), it = iter(), n = d.iteracoes.length;
    Array.prototype.forEach.call(elLinha.querySelectorAll('button'), function(b, i){ b.setAttribute('aria-current', i === iIter); });

    if(iIter === 0){
      corpo.entrada.innerHTML = '<p class="pb-vazio">Primeira iteração: o modelo recebe só a especificação e a suíte de testes. Não há relatório de falha nem código anterior.</p>'
        + '<pre>' + esc(d.especificacao.trim()) + '</pre>';
    } else {
      corpo.entrada.innerHTML = '<span class="pb-selo parcial">relatório da iteração ' + (it.n - 1) + '</span>'
        + '<pre>' + esc(it.realimentacao_recebida.trim() || '(vazio)') + '</pre>'
        + (it.codigo_anterior_enviado ? '<p class="pb-vazio">Mais a versão anterior do próprio código, devolvida ao modelo pelo arnês.</p>' : '');
    }

    var anterior = iIter > 0 ? d.iteracoes[iIter - 1].codigo : '';
    corpo.saida.innerHTML = '<pre>' + linhasNovas(it.codigo, anterior) + '</pre>'
      + (iIter > 0 ? '<p class="pb-vazio">Destacado: linha que não existia na iteração anterior.</p>' : '');

    if(it.guarda === 'recusado'){
      corpo.verificador.innerHTML = '<span class="pb-selo ruim">guarda estática recusou</span><pre>' + esc(it.motivo_recusa) + '</pre>'
        + '<p class="pb-vazio">O pytest não chegou a rodar. Isolamento e verificação são portões distintos.</p>';
    } else {
      var completo = it.testes_passaram === d.total_testes;
      corpo.verificador.innerHTML = '<span class="pb-selo ' + (completo ? 'ok' : 'parcial') + '">'
        + it.testes_passaram + '/' + d.total_testes + ' testes passando</span>'
        + '<pre>' + esc(it.relatorio.trim() || 'sem falhas') + '</pre>';
    }

    var partes = ['<span>iteração <b>' + it.n + '</b> de ' + n + '</span>',
      '<span>temperatura <b>' + it.temperatura.toFixed(1) + '</b></span>',
      '<span>tokens acumulados <b>' + it.tokens_acumulados + '</b></span>',
      '<span>autodeclarou pronto <b>' + (it.autodeclarou ? 'sim' : 'não') + '</b></span>'];
    if(it.estagnado) partes.push('<span class="pb-alerta">Estagnação: o verificador devolveu exatamente a mesma falha da iteração anterior, e o arnês elevou a temperatura para ' + it.temperatura.toFixed(1) + ' em vez de repetir a mesma chamada.</span>');
    elEstado.innerHTML = partes.join('');

    if(iIter === n - 1){
      var honesto = (d.parada === 'autodeclarada_pelo_modelo' && d.verdade_final < d.total_testes);
      elFinal.hidden = false;
      elFinal.innerHTML = 'Parada: <b>' + esc(d.parada) + '</b> · iterações: <b>' + d.iteracoes_totais
        + '</b> · tokens: <b>' + d.tokens_totais + '</b> · verdade final: <b>' + d.verdade_final + '/' + d.total_testes + '</b>'
        + (honesto ? '<br><strong>O laço afirmou conclusão com ' + d.verdade_final + '/' + d.total_testes + '.</strong> A linha de verdade final só existe porque o script roda os testes de qualquer forma no fim. Num sistema real ela não existiria.'
                   : (d.parada === 'orcamento_esgotado' ? '<br>O laço não terminou o trabalho e informou que não terminou. É um desfecho aceitável.'
                                                        : '<br>O verificador aprovou. O laço parou porque um critério objetivo foi satisfeito, não porque o modelo achou que tinha acabado.'));
    } else {
      elFinal.hidden = true;
    }

    raiz.querySelector('[data-acao=inicio]').disabled = iIter === 0;
    raiz.querySelector('[data-acao=anterior]').disabled = iIter === 0;
    raiz.querySelector('[data-acao=proxima]').disabled = iIter === n - 1;
    raiz.querySelector('[data-acao=fim]').disabled = iIter === n - 1;
  }

  function parar(){ if(timer){ clearInterval(timer); timer = null; } elPlay.textContent = '▶ Reproduzir'; elPlay.setAttribute('aria-label','Reproduzir'); }
  function tocar(){
    if(timer){ parar(); return; }
    if(iIter === ses().iteracoes.length - 1) iIter = 0;
    pintar();
    elPlay.textContent = '❙❙ Pausar'; elPlay.setAttribute('aria-label','Pausar');
    timer = setInterval(function(){
      if(iIter >= ses().iteracoes.length - 1){ parar(); return; }
      iIter++; pintar();
    }, ritmo);
  }

  raiz.querySelectorAll('.pb-btn').forEach(function(b){
    b.addEventListener('click', function(){
      var a = b.dataset.acao, n = ses().iteracoes.length;
      if(a === 'play'){ tocar(); return; }
      parar();
      if(a === 'inicio') iIter = 0;
      if(a === 'fim') iIter = n - 1;
      if(a === 'anterior' && iIter > 0) iIter--;
      if(a === 'proxima' && iIter < n - 1) iIter++;
      pintar();
    });
  });
  raiz.querySelector('.pb-select').addEventListener('change', function(e){
    ritmo = Number(e.target.value);
    if(timer){ parar(); tocar(); }
  });

  montar();
})();
</script>
"""

RODAPE = """
## O que cada gravação mostra

### 1. Sem verificador: a falha que ninguém vê

A condição de parada foi trocada: em vez de `pytest`, o modelo escreve `PRONTO` quando se considera pronto, e o laço acredita. Ele encerra na **primeira** iteração, gasta **719 tokens** e entrega uma função com **4/5** testes passando.

Repare onde a diferença **não** está. É o mesmo modelo, os mesmos pesos, a mesma especificação. Na primeira iteração, esta sessão e a sessão 4 produzem exatamente o mesmo código e o mesmo 4/5. A diferença inteira está em quem tem autoridade para dizer que o trabalho terminou.

A linha `verdade final` do painel só existe porque o script roda os testes de qualquer forma no fim, para efeito de laboratório. **Num sistema real essa linha não existiria.** O laço teria encerrado, declarado sucesso, e o artefato defeituoso seguiria adiante. Este é o falso positivo, e ele é o desfecho mais barato dos quatro.

### 2. Modelo sem capacidade: o arnês não faz milagre

Aqui o verificador está no lugar e o orçamento é o mesmo de oito iterações. O que muda é o modelo: `llama3.2:3b`, de 2 GB, no lugar do `qwen2.5-coder:7b`. O laço esgota o orçamento com **1/5**, consumindo **7.235 tokens**.

Compare com a sessão 4, que convergiu gastando **7.413 tokens**. Praticamente o mesmo custo, e uma das duas não entregou nada. Um laço barato que nunca converge é pior que um caro que converge, e é por isso que **custo total isolado engana** como métrica: o sinal útil é custo por objetivo concluído.

A leitura arquitetural é que duas afirmações convivem sem contradição. Reconstruir o arnês costuma render mais do que trocar de modelo, **e** existe um piso de capacidade abaixo do qual nenhum arnês fecha o laço. Descobrir de que lado desse piso está o seu caso é trabalho de arquitetura, e a forma de descobrir é medir — não projetar.

### 3. Orçamento curto: o desfecho honesto

Modelo capaz, verificador funcionando, e o teto em três iterações. O laço para em **4/5** e informa `orcamento_esgotado`.

**Este é um desfecho aceitável.** O laço não terminou o trabalho e disse que não terminou. Comparado com a sessão 1, que encerrou em um sexto do tempo afirmando o contrário, ele é o mais barato dos dois em consequência, mesmo custando mais em tokens.

O que um laço em operação precisa fazer ao esgotar o orçamento é registrar o que tentou, o que bloqueou o progresso e qual é o estado do artefato, e encaminhar a uma pessoa. O que não pode acontecer é encerrar em silêncio deixando algo parcial que parece pronto.

### 4. Convergência: o que custa acertar

Modelo capaz, verificador funcionando, teto de oito iterações. O laço fecha em **5/5** com **7.413 tokens** — na oitava iteração.

Percorra devagar. Da primeira à sétima iteração o resultado **não sai de 4/5**, e a estagnação é sinalizada seis vezes: o arnês sobe a temperatura para 0,4, depois 0,8, e o modelo continua devolvendo praticamente o mesmo código. O que finalmente fecha o laço é um `.strip()` acrescentado ao argumento da expressão regular. Sete rodadas e 6.443 tokens para chegar a uma correção de nove caracteres.

E o detalhe que mais importa para quem vai dimensionar um laço em produção: **a convergência veio na última iteração do orçamento**. Se o teto fosse sete, esta execução teria terminado em `orcamento_esgotado`, como a sessão 3. Uma execução anterior desta mesma oficina, com o mesmo modelo e a mesma tarefa, convergiu em quatro iterações. Duas execuções do mesmo laço com a mesma entrada não produzem o mesmo número de iterações nem o mesmo custo — a partir do momento em que o arnês diversifica a temperatura, a trajetória deixa de ser determinística.

A consequência de planejamento é direta: **orçamento de laço se dimensiona por distribuição observada, com percentil, e não por média**. Quem tivesse visto só a execução de quatro iterações teria fixado o teto em quatro ou cinco, e teria cortado esta.

## Três leituras que atravessam as quatro gravações

**O gargalo é a qualidade da realimentação, não a do modelo.** Repare no que volta ao modelo em qualquer aba: a linha `FAILED test_solucao.py::test_espacos_extras_e_caixa_baixa - ValueError: Linha...`, truncada. O modelo não recebe a entrada que falhou nem o valor esperado. Sete iterações para descobrir um `.strip()` é o que se paga por um relatório fino. Melhorar o que o verificador devolve é decisão de arquitetura, e neste laço ela vale mais do que trocar o modelo.

**Isolamento e verificação são portões distintos.** A guarda estática impede que o código gerado importe módulos fora da lista ou chame `exec`, e é por isso que o laço pode rodar sem supervisão numa máquina de estudo. Ela não diz nada sobre a correção do resultado. Cumprir um portão não dispensa o outro.

**O laço não escreve o verificador.** Nas quatro gravações, o agente não tem permissão de escrita sobre `test_solucao.py`. Se tivesse, a condição de parada viraria variável de folga, e o desfecho fácil seria alterar o teste em vez de corrigir o código. Quando o mesmo processo produz o artefato e o critério que o aprova, não existe verificação: existe autoavaliação.

## Se você for operar um laço desses

Quatro portões, cumulativos, que nenhum modelo dispensa:

- **Critério** — a condição de parada existe, é executável por comando determinístico, está versionada junto ao pacote, e existe pelo menos um caso conhecido em que ela **reprova**. Condição que nunca reprova é decoração.
- **Orçamento** — dois tetos independentes, iterações e custo, cada um com dono e com comportamento definido no esgotamento. Encerrar em silêncio não é comportamento aceitável.
- **Isolamento** — identidade própria, escopo menor que o de qualquer pessoa, credenciais de prazo curto, e nenhum alcance a produção ou dado real enquanto a natureza do efeito não estiver classificada.
- **Interrupção** — desligamento acessível fora do processo do laço, documentado, testado, e conhecido por quem está de plantão.

Três coisas nunca descem para o laço, mesmo no quarto degrau da escada: a definição do critério de sucesso, porque é ela que codifica a intenção; a aceitação do risco residual de rodar sem supervisão, que é decisão de governança com dono nomeado; e o desligamento.

## Gravar a sua própria execução

O playback não substitui rodar. Quem tiver Ollama e o modelo baixado pode gravar a própria sessão e comparar a trajetória com estas quatro:

```bash
python loop_objetivado.py --gravar minha-sessao.json
python loop_objetivado.py --max-iteracoes 3 --gravar orcamento-curto.json
python loop_objetivado.py --parada modelo --gravar autodeclarada.json
python loop_objetivado.py --modelo llama3.2:3b --gravar modelo-fraco.json
```

O roteiro completo, com instalação e questões de discussão, está na [oficina do módulo](oficina-de-ferramentas.md#extensao-loop-objetivado-com-orcamento). As quatro transcrições desta página vivem em `docs/assets/labs/modulo-6/gravacoes/`, no mesmo formato que o `--gravar` produz, e `python scripts/gerar_playback.py` reconstrói esta página a partir delas.

Para o tratamento operacional — portões, modos de falha, métricas e verificação independente —, siga para [Operação de loops](lacos-desassistidos.md). Para a escada de níveis e o critério de subida, [Loops agênticos](../modulo-4-agentes/loops.md#quatro-niveis-de-loop).
"""

if __name__ == "__main__":
    DESTINO.write_text(gerar(), encoding="utf-8")
    print(f"gerado: {DESTINO.relative_to(RAIZ)}")
