"""Workflow LangGraph com uma chamada real a um LLM: o modelo propoe, o codigo decide."""

from __future__ import annotations

import argparse
import json
from typing import TypedDict

from langchain_ollama import ChatOllama
from langgraph.graph import END, START, StateGraph

CENARIOS = {
    "valido": "Troque o item P10 pelo P20 no pedido 845 e mantenha a data.",
    "invalido": "Troque o item P10 pelo P99 no pedido 845 e mantenha a data.",
}

CATALOGO_VALIDO = {"P10", "P20", "P30"}
PEDIDOS_CONHECIDOS = {"845", "846"}

PROMPT_SISTEMA = (
    "Voce extrai uma proposta de troca de item de pedido a partir de uma "
    "mensagem de cliente. Responda SOMENTE com um objeto JSON, sem texto "
    "antes ou depois, no formato exato: "
    '{"old_sku": "...", "new_sku": "...", "order_id": "..."}. '
    "Nao invente valores que nao estejam na mensagem."
)


class PropostaState(TypedDict, total=False):
    pedido_cliente: str
    proposta_bruta: str
    old_sku: str
    new_sku: str
    order_id: str
    proposta_valida: bool
    motivo: str


def propor(state: PropostaState) -> PropostaState:
    modelo = ChatOllama(model="llama3.2:3b", temperature=0)
    resposta = modelo.invoke(
        [
            ("system", PROMPT_SISTEMA),
            ("human", state["pedido_cliente"]),
        ]
    )
    return {"proposta_bruta": resposta.content}


def interpretar(state: PropostaState) -> PropostaState:
    texto = state["proposta_bruta"].strip()
    try:
        dados = json.loads(texto)
        return {
            "old_sku": dados.get("old_sku", ""),
            "new_sku": dados.get("new_sku", ""),
            "order_id": dados.get("order_id", ""),
        }
    except json.JSONDecodeError:
        return {"old_sku": "", "new_sku": "", "order_id": ""}


def validar(state: PropostaState) -> PropostaState:
    old_sku = state.get("old_sku", "")
    new_sku = state.get("new_sku", "")
    order_id = state.get("order_id", "")

    if not old_sku or not new_sku or not order_id:
        return {"proposta_valida": False, "motivo": "campos ausentes na proposta"}
    if new_sku not in CATALOGO_VALIDO:
        return {"proposta_valida": False, "motivo": f"SKU {new_sku} fora do catalogo"}
    if order_id not in PEDIDOS_CONHECIDOS:
        return {"proposta_valida": False, "motivo": f"pedido {order_id} desconhecido"}
    return {"proposta_valida": True, "motivo": "proposta dentro da politica"}


def build_workflow():
    workflow = StateGraph(PropostaState)
    workflow.add_node("propor", propor)
    workflow.add_node("interpretar", interpretar)
    workflow.add_node("validar", validar)
    workflow.add_edge(START, "propor")
    workflow.add_edge("propor", "interpretar")
    workflow.add_edge("interpretar", "validar")
    workflow.add_edge("validar", END)
    return workflow.compile()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cenario", choices=CENARIOS.keys(), required=True)
    args = parser.parse_args()

    estado = build_workflow().invoke({"pedido_cliente": CENARIOS[args.cenario]})

    print(f"PEDIDO_CLIENTE: {estado['pedido_cliente']}")
    print(f"PROPOSTA_BRUTA_DO_MODELO: {estado['proposta_bruta']}")
    print(f"OLD_SKU: {estado.get('old_sku', '')}")
    print(f"NEW_SKU: {estado.get('new_sku', '')}")
    print(f"ORDER_ID: {estado.get('order_id', '')}")
    print(f"PROPOSTA_VALIDA: {estado.get('proposta_valida', False)}")
    print(f"MOTIVO: {estado.get('motivo', '')}")


if __name__ == "__main__":
    main()
