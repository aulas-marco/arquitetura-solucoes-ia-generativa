"""Avalia recuperação lexical, vetorial e híbrida do caso Lume/Aurora com MRR e nDCG@k."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

from rag_lume_aurora import MODOS, load_corpus


ROOT = Path(__file__).resolve().parent
CASOS_PATH = ROOT / "casos_recuperacao_lume_aurora.json"


def reciprocal_rank(ranked_ids: list[str], relevante: str) -> float:
    for posicao, doc_id in enumerate(ranked_ids, start=1):
        if doc_id == relevante:
            return 1 / posicao
    return 0.0


def ndcg_at_k(ranked_ids: list[str], relevante: str, k: int) -> float:
    dcg = 0.0
    for posicao, doc_id in enumerate(ranked_ids[:k], start=1):
        if doc_id == relevante:
            dcg = 1 / math.log2(posicao + 1)
            break
    idcg = 1 / math.log2(2)  # um único documento relevante por pergunta; a posição ideal é 1
    return dcg / idcg


def avaliar(caso: str, k: int) -> dict[str, dict[str, float]]:
    perguntas = json.loads(CASOS_PATH.read_text(encoding="utf-8"))[caso]
    documents = load_corpus(caso)
    resultado: dict[str, dict[str, float]] = {}
    for modo, ranquear in MODOS.items():
        soma_mrr = 0.0
        soma_ndcg = 0.0
        for item in perguntas:
            ranked_ids = [document.metadata["id"] for document in ranquear(documents, item["pergunta"])]
            soma_mrr += reciprocal_rank(ranked_ids, item["id_relevante"])
            soma_ndcg += ndcg_at_k(ranked_ids, item["id_relevante"], k)
        resultado[modo] = {
            "MRR": round(soma_mrr / len(perguntas), 3),
            f"nDCG@{k}": round(soma_ndcg / len(perguntas), 3),
        }
    return resultado


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--caso", required=True, choices=["lume", "aurora"])
    parser.add_argument("--k", type=int, default=3)
    args = parser.parse_args()

    resultado = avaliar(args.caso, args.k)
    print(f"Caso: {args.caso} | {len(json.loads(CASOS_PATH.read_text(encoding='utf-8'))[args.caso])} perguntas rotuladas")
    for modo, metricas in resultado.items():
        linha = " | ".join(f"{nome}: {valor}" for nome, valor in metricas.items())
        print(f"{modo:9s} — {linha}")


if __name__ == "__main__":
    main()
