"""Laboratório RAG Boreal: ingestão local, recuperação visível e resposta citada."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_ollama import ChatOllama, OllamaEmbeddings


ROOT = Path(__file__).resolve().parent
CORPUS = ROOT / "corpus"
DATABASE = ROOT / "chroma-boreal"
REGULAR_REFUND_POLICY = "POL-17-REG:v3"


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


def required_policy(question: str) -> str | None:
    if "compra regular" in question.casefold():
        return REGULAR_REFUND_POLICY
    return None


def build_store(excluded: str | None) -> Chroma:
    if DATABASE.exists():
        shutil.rmtree(DATABASE)
    documents = [read_document(path) for path in sorted(CORPUS.glob("*.txt"))]
    kept = [document for document in documents if f"{document.metadata['id']}:{document.metadata['versao']}" != excluded]
    if not kept:
        raise SystemExit("Nenhum documento restou no corpus após o filtro.")
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return Chroma.from_documents(kept, embeddings, persist_directory=str(DATABASE))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pergunta", required=True)
    parser.add_argument("--excluir", help="ID:versao a excluir, por exemplo POL-17-REG:v3")
    args = parser.parse_args()

    if not CORPUS.exists():
        raise SystemExit("Crie a pasta corpus e copie os três arquivos .txt do laboratório.")
    store = build_store(args.excluir)
    retrieved = store.similarity_search(args.pergunta, k=2)
    print("Trechos recuperados:")
    for document in retrieved:
        print(f"RECUPERADO {document.metadata['id']}:{document.metadata['versao']} — {document.metadata['arquivo']}")
        print(document.page_content)

    required = required_policy(args.pergunta)
    recovered_ids = {
        f"{document.metadata['id']}:{document.metadata['versao']}"
        for document in retrieved
    }
    if required and required not in recovered_ids:
        print(f"\nRESPOSTA: REVISÃO_HUMANA — a evidência obrigatória {required} não foi recuperada.")
        return

    if requires_human_review(args.pergunta):
        print("\nRESPOSTA: REVISÃO_HUMANA — faltam a data e o tipo de compra para aplicar uma regra.")
        return

    context = "\n\n".join(
        f"[{document.metadata['id']}:{document.metadata['versao']} | {document.metadata['arquivo']}] {document.page_content}"
        for document in retrieved
    )
    prompt = (
        "Responda em português somente com base nos trechos abaixo. "
        "Cite o ID, a versão e o arquivo usados. Se não houver evidência suficiente, responda REVISÃO_HUMANA.\n\n"
        f"Trechos:\n{context}\n\nPergunta: {args.pergunta}"
    )
    answer = ChatOllama(model="llama3.2:3b", temperature=0).invoke(prompt)
    print(f"\nRESPOSTA: {answer.content}")


if __name__ == "__main__":
    main()
