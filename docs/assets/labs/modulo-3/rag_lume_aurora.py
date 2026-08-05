"""Laboratório RAG do caso contínuo: Banco Lume (contestação) e Cooperativa Aurora (renegociação)."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_ollama import ChatOllama, OllamaEmbeddings


ROOT = Path(__file__).resolve().parent
DATABASE = ROOT / "chroma-lume-aurora"
CORPUS_POR_CASO = {
    "lume": ("lume-politica-contestacao.txt", "lume-politica-estorno-parcial.txt"),
    "aurora": ("aurora-politica-campanha.txt", "aurora-politica-carencia.txt"),
}


def read_document(path: Path) -> Document:
    lines = path.read_text(encoding="utf-8").splitlines()
    metadata = dict(line.split(": ", 1) for line in lines[:2])
    content = "\n".join(lines[3:]).strip()
    return Document(
        page_content=content,
        metadata={"id": metadata["ID"], "versao": metadata["VERSAO"], "arquivo": path.name},
    )


def requires_human_review(question: str) -> bool:
    normalized = question.casefold()
    return "não sei a data" in normalized or "nao sei a data" in normalized


def build_store(caso: str) -> Chroma:
    if DATABASE.exists():
        shutil.rmtree(DATABASE)
    documents = [read_document(ROOT / name) for name in CORPUS_POR_CASO[caso]]
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return Chroma.from_documents(documents, embeddings, persist_directory=str(DATABASE))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--caso", required=True, choices=sorted(CORPUS_POR_CASO))
    parser.add_argument("--pergunta", required=True)
    args = parser.parse_args()

    store = build_store(args.caso)
    retrieved = store.similarity_search(args.pergunta, k=2)
    print(f"Caso: {args.caso}")
    print("Trechos recuperados:")
    for document in retrieved:
        print(f"RECUPERADO {document.metadata['id']}:{document.metadata['versao']} — {document.metadata['arquivo']}")
        print(document.page_content)

    if requires_human_review(args.pergunta):
        print("\nRESPOSTA: REVISÃO_HUMANA — faltam dados suficientes para aplicar uma regra.")
        return

    context = "\n\n".join(
        f"[{document.metadata['id']}:{document.metadata['versao']}] {document.page_content}"
        for document in retrieved
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
