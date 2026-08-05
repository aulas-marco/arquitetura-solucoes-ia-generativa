"""Contraste de autonomia: Lume fica em workflow, Aurora vira agente de leitura."""

from __future__ import annotations

import argparse
from typing import TypedDict

from langgraph.graph import END, START, StateGraph

CONTRATO = {"numero": "CTR-771", "versao": "v3", "situacao": "ativo"}
PAGAMENTO = {"atraso_dias": 12, "saldo": 4300.00}
POLITICA = {"campanha": "CAMP-09", "versao": "v2", "vigente": True}


class LumeState(TypedDict, total=False):
    contexto: dict
    rascunho: str
    trace: list[str]


def lume_montar_contexto(state: LumeState) -> LumeState:
    return {"contexto": {"politica": POLITICA}, "trace": ["contexto montado: sequência fixa"]}


def lume_gerar_rascunho(state: LumeState) -> LumeState:
    return {
        "rascunho": "Rascunho de contestação com política POL-vigente citada",
        "trace": state["trace"] + ["rascunho gerado sem escolha de ferramenta"],
    }


def build_lume_workflow():
    workflow = StateGraph(LumeState)
    workflow.add_node("montar_contexto", lume_montar_contexto)
    workflow.add_node("gerar_rascunho", lume_gerar_rascunho)
    workflow.add_edge(START, "montar_contexto")
    workflow.add_edge("montar_contexto", "gerar_rascunho")
    workflow.add_edge("gerar_rascunho", END)
    return workflow.compile()


class AuroraState(TypedDict, total=False):
    chamadas: int
    orcamento: int
    trajetoria: list[str]
    dossie: dict


def consultar_contrato(state: AuroraState) -> AuroraState:
    return {
        "chamadas": state["chamadas"] + 1,
        "trajetoria": state["trajetoria"] + ["consultar_contrato"],
        "dossie": {**state.get("dossie", {}), "contrato": CONTRATO},
    }


def consultar_pagamento(state: AuroraState) -> AuroraState:
    return {
        "chamadas": state["chamadas"] + 1,
        "trajetoria": state["trajetoria"] + ["consultar_pagamento"],
        "dossie": {**state.get("dossie", {}), "pagamento": PAGAMENTO},
    }


def consultar_politica_campanha(state: AuroraState) -> AuroraState:
    return {
        "chamadas": state["chamadas"] + 1,
        "trajetoria": state["trajetoria"] + ["consultar_politica_campanha"],
        "dossie": {**state.get("dossie", {}), "politica": POLITICA},
    }


def decide_next(state: AuroraState) -> str:
    if state["chamadas"] >= state["orcamento"]:
        return "concluir"
    faltantes = {"contrato", "pagamento", "politica"} - set(state.get("dossie", {}))
    if "contrato" in faltantes:
        return "contrato"
    if "pagamento" in faltantes:
        return "pagamento"
    if "politica" in faltantes:
        return "politica"
    return "concluir"


def concluir(state: AuroraState) -> AuroraState:
    return {"trajetoria": state["trajetoria"] + ["dossiê proposto para revisão do especialista"]}


def build_aurora_agent():
    workflow = StateGraph(AuroraState)
    workflow.add_node("contrato", consultar_contrato)
    workflow.add_node("pagamento", consultar_pagamento)
    workflow.add_node("politica", consultar_politica_campanha)
    workflow.add_node("concluir", concluir)
    workflow.add_conditional_edges(
        START, decide_next,
        {"contrato": "contrato", "pagamento": "pagamento", "politica": "politica", "concluir": "concluir"},
    )
    for node in ("contrato", "pagamento", "politica"):
        workflow.add_conditional_edges(
            node, decide_next,
            {"contrato": "contrato", "pagamento": "pagamento", "politica": "politica", "concluir": "concluir"},
        )
    workflow.add_edge("concluir", END)
    return workflow.compile()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--caso", choices=("lume", "aurora"), required=True)
    parser.add_argument("--orcamento", type=int, default=6)
    args = parser.parse_args()

    if args.caso == "lume":
        state = build_lume_workflow().invoke({"trace": []})
        print("CASO: lume (workflow assistivo, sem ferramenta de efeito)")
        print(f"RASCUNHO: {state['rascunho']}")
        for event in state["trace"]:
            print(f"TRACE: {event}")
    else:
        state = build_aurora_agent().invoke(
            {"chamadas": 0, "orcamento": args.orcamento, "trajetoria": [], "dossie": {}}
        )
        print("CASO: aurora (agente com ferramentas somente leitura)")
        print(f"CHAMADAS: {state['chamadas']}/{args.orcamento}")
        print(f"DOSSIE: {list(state['dossie'].keys())}")
        for event in state["trajetoria"]:
            print(f"TRACE: {event}")


if __name__ == "__main__":
    main()
