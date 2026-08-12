"""Laboratório RAG do caso contínuo: Banco Lume (contestação) e Cooperativa Aurora (renegociação) — recuperação lexical, vetorial e híbrida."""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_ollama import ChatOllama, OllamaEmbeddings
from rank_bm25 import BM25Okapi


ROOT = Path(__file__).resolve().parent
DATABASE = ROOT / "chroma-lume-aurora"
CORPUS_POR_CASO = {
    "lume": (
        "lume-politica-contestacao.txt",
        "lume-politica-estorno-parcial.txt",
        "lume-politica-compra-internacional.txt",
        "lume-politica-cobranca-duplicada.txt",
        "lume-politica-produto-nao-entregue.txt",
    ),
    "aurora": (
        "aurora-politica-campanha.txt",
        "aurora-politica-carencia.txt",
        "aurora-politica-atraso-prolongado.txt",
        "aurora-politica-parcelamento.txt",
        "aurora-politica-restricao-judicial.txt",
    ),
}


def read_document(path: Path) -> Document:
    lines = path.read_text(encoding="utf-8").splitlines()
    metadata = dict(line.split(": ", 1) for line in lines[:2])
    content = "\n".join(lines[3:]).strip()
    return Document(
        page_content=content,
        metadata={"id": metadata["ID"], "versao": metadata["VERSAO"], "arquivo": path.name},
    )


def load_corpus(caso: str) -> list[Document]:
    return [read_document(ROOT / name) for name in CORPUS_POR_CASO[caso]]


def tokenize(text: str) -> list[str]:
    return re.findall(r"\w+", text.casefold())


def rank_lexical(documents: list[Document], pergunta: str) -> list[Document]:
    """Ordena por BM25 sobre o texto bruto — forte quando a pergunta repete os termos do documento."""
    bm25 = BM25Okapi([tokenize(document.page_content) for document in documents])
    scores = bm25.get_scores(tokenize(pergunta))
    order = sorted(range(len(documents)), key=lambda i: scores[i], reverse=True)
    return [documents[i] for i in order]


def rank_vetorial(documents: list[Document], pergunta: str) -> list[Document]:
    """Ordena por similaridade de embeddings — forte quando a pergunta parafraseia o documento."""
    if DATABASE.exists():
        shutil.rmtree(DATABASE)
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    store = Chroma.from_documents(documents, embeddings, persist_directory=str(DATABASE))
    return store.similarity_search(pergunta, k=len(documents))


def rank_hibrido(documents: list[Document], pergunta: str, k_rrf: int = 60) -> list[Document]:
    """Combina as duas ordens por Reciprocal Rank Fusion — soma 1/(k_rrf + posição) de cada lista."""
    lexical = rank_lexical(documents, pergunta)
    vetorial = rank_vetorial(documents, pergunta)
    posicao_lexical = {document.metadata["id"]: i for i, document in enumerate(lexical)}
    posicao_vetorial = {document.metadata["id"]: i for i, document in enumerate(vetorial)}

    def rrf_score(document: Document) -> float:
        doc_id = document.metadata["id"]
        return 1 / (k_rrf + posicao_lexical[doc_id] + 1) + 1 / (k_rrf + posicao_vetorial[doc_id] + 1)

    return sorted(documents, key=rrf_score, reverse=True)


MODOS = {"lexical": rank_lexical, "vetorial": rank_vetorial, "hibrido": rank_hibrido}


def requires_human_review(question: str) -> bool:
    normalized = question.casefold()
    return "não sei a data" in normalized or "nao sei a data" in normalized


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--caso", required=True, choices=sorted(CORPUS_POR_CASO))
    parser.add_argument("--modo", default="hibrido", choices=sorted(MODOS))
    parser.add_argument("--pergunta", required=True)
    args = parser.parse_args()

    documents = load_corpus(args.caso)
    ranked = MODOS[args.modo](documents, args.pergunta)
    top = ranked[:2]
    top_ids = {document.metadata["id"] for document in top}

    print(f"Caso: {args.caso} | Modo: {args.modo}")
    print("Trechos recuperados (ordem de relevância; → = usado na resposta):")
    for posicao, document in enumerate(ranked, start=1):
        marca = "→" if document.metadata["id"] in top_ids else " "
        print(f"{marca} {posicao}. {document.metadata['id']}:{document.metadata['versao']} — {document.metadata['arquivo']}")

    if requires_human_review(args.pergunta):
        print("\nRESPOSTA: REVISÃO_HUMANA — faltam dados suficientes para aplicar uma regra.")
        return

    context = "\n\n".join(
        f"[{document.metadata['id']}:{document.metadata['versao']}] {document.page_content}"
        for document in top
    )
    prompt = (
        "Responda em português somente com base nos trechos abaixo. "
        "Cite o ID e a versão usados. Se não houver evidência suficiente, responda REVISÃO_HUMANA.\n\n"
        f"Trechos:\n{context}\n\nPergunta: {args.pergunta}"
    )
    answer = ChatOllama(model="llama3.2:3b", temperature=0).invoke(prompt)
    print(f"\nRESPOSTA: {answer.content}")


if __name__ == "__main__":
    main()
