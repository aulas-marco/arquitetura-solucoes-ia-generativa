"""Workflow LangGraph local para observar aprovação e idempotência."""

from __future__ import annotations

import argparse
from typing import TypedDict

from langgraph.graph import END, START, StateGraph


class ExchangeState(TypedDict, total=False):
    approved: bool
    repeated: bool
    idempotency_key: str
    status: str
    result: str
    trace: list[str]


def register_intent(state: ExchangeState) -> ExchangeState:
    return {"status": "reserva_pendente", "trace": ["intenção registrada"]}


def decide_approval(state: ExchangeState) -> str:
    return "reserve" if state["approved"] else "wait"


def wait_for_approval(state: ExchangeState) -> ExchangeState:
    return {"status": "aguardando_aprovacao", "trace": state["trace"] + ["aprovação ausente"]}


def reserve(state: ExchangeState) -> ExchangeState:
    if state["repeated"]:
        return {"status": "reservado", "result": "RES-501", "trace": state["trace"] + ["repetição reconhecida: nenhuma nova reserva"]}
    return {"status": "reservado", "result": "RES-501", "trace": state["trace"] + ["reserva simulada criada"]}


def build_workflow():
    workflow = StateGraph(ExchangeState)
    workflow.add_node("intencao", register_intent)
    workflow.add_node("aguardar", wait_for_approval)
    workflow.add_node("reservar", reserve)
    workflow.add_edge(START, "intencao")
    workflow.add_conditional_edges("intencao", decide_approval, {"wait": "aguardar", "reserve": "reservar"})
    workflow.add_edge("aguardar", END)
    workflow.add_edge("reservar", END)
    return workflow.compile()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--aprovado", choices=("true", "false"), required=True)
    parser.add_argument("--repetir", action="store_true")
    args = parser.parse_args()
    state = build_workflow().invoke({
        "approved": args.aprovado == "true",
        "repeated": args.repetir,
        "idempotency_key": "TROCA-PED-104-1",
        "trace": [],
    })
    print(f"ESTADO: {state['status']}")
    print(f"CHAVE: {state['idempotency_key']}")
    print(f"RESULTADO: {state.get('result', 'nenhum efeito')}")
    for event in state["trace"]:
        print(f"TRACE: {event}")


if __name__ == "__main__":
    main()
