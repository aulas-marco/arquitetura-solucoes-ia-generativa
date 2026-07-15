#!/usr/bin/env python3
"""Validate the structure and editorial quality gates of the course content."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
IMAGES = DOCS / "assets" / "images"
COVER = "capa-cartografia-solucao-generativa.png"

MODULES = {
    "modulo-1-fundamentos": ("Fundamentos", ("m01-deterministico-probabilistico.png", "m01-anatomia-solucao-generativa.png")),
    "modulo-2-desenho-conceitual": ("Desenho conceitual", ("m02-oportunidade-arquitetura.png", "m02-paisagem-decisoes.png")),
    "modulo-3-rag": ("RAG", ("m03-dois-fluxos-rag.png", "m03-pergunta-evidencia.png")),
    "modulo-4-agentes": ("Agentes", ("m04-agente-ferramentas.png", "m04-fronteiras-autonomia.png")),
    "modulo-5-confianca": ("Confiança", ("m05-defesas-profundidade.png", "m05-prisma-avaliacao.png")),
    "modulo-6-operacao": ("Operação", ("m06-ciclo-llmops.png", "m06-plataforma-corporativa.png")),
}
PAGES = (
    "index.md", "conceitos.md", "padroes-e-decisoes.md",
    "exemplo-arquitetural.md", "estudo-de-caso.md",
    "exercicios.md", "sintese-e-referencias.md",
)
BLOOM = ("Recordar", "Compreender", "Aplicar", "Analisar", "Avaliar", "Criar")

EDITORIAL_MARKERS = ("TODO", "TBD", "PLACEHOLDER", "PREENCHER")
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
REFERENCE_IMAGE_RE = re.compile(r"!\[([^\]]*)\]\[([^\]]+)\]")
REFERENCE_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\[([^\]]+)\]")
REFERENCE_DEFINITION_RE = re.compile(
    r"(?m)^[ \t]{0,3}\[([^\]]+)\]:[ \t]*(.+?)[ \t]*$"
)
MARKDOWN_HEADING_RE = re.compile(r"(?m)^(#{1,6})[ \t]+.*?[ \t]*$")
WORD_RE = re.compile(r"\b[^\W\d_]+(?:[-’'][^\W\d_]+)*\b", re.UNICODE)


@dataclass
class Counts:
    pages: int = 0
    words: int = 0
    images: int = 0
    exercises: int = 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Valida páginas, exercícios, links e imagens do site-livro."
    )
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument("--module", choices=tuple(MODULES), metavar="SLUG")
    selection.add_argument("--all", action="store_true", help="valida todos os módulos")
    return parser.parse_args()


def markdown_target(raw_target: str) -> str:
    """Return the URL/path portion of an inline Markdown destination."""
    target = raw_target.strip()
    if target.startswith("<") and ">" in target:
        return target[1:target.index(">")]
    return target.split(maxsplit=1)[0]


def local_path(source: Path, raw_target: str) -> Path | None:
    target = markdown_target(raw_target)
    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc or not parsed.path:
        return None
    path_text = unquote(parsed.path)
    if path_text.startswith("/"):
        return DOCS / path_text.lstrip("/")
    return source.parent / path_text


def normalize_reference_id(reference_id: str) -> str:
    return re.sub(r"\s+", " ", reference_id.strip()).casefold()


def validate_references(path: Path, text: str, errors: list[str], counts: Counts) -> None:
    definitions = {
        normalize_reference_id(reference_id): target
        for reference_id, target in REFERENCE_DEFINITION_RE.findall(text)
    }

    for alt, target in IMAGE_RE.findall(text):
        counts.images += 1
        if not alt.strip():
            errors.append(f"{path.relative_to(ROOT)}: imagem com texto alternativo vazio")
        destination = local_path(path, target)
        if destination is not None and not destination.resolve().is_file():
            errors.append(
                f"{path.relative_to(ROOT)}: imagem local inexistente: {markdown_target(target)}"
            )

    for target in LINK_RE.findall(text):
        destination = local_path(path, target)
        if destination is None:
            continue
        resolved = destination.resolve()
        if resolved.is_dir():
            resolved = resolved / "index.md"
        if not resolved.is_file():
            errors.append(
                f"{path.relative_to(ROOT)}: link relativo inexistente: {markdown_target(target)}"
            )

    for alt, reference_id in REFERENCE_IMAGE_RE.findall(text):
        counts.images += 1
        if not alt.strip():
            errors.append(f"{path.relative_to(ROOT)}: imagem com texto alternativo vazio")
        target = definitions.get(normalize_reference_id(reference_id))
        if target is None:
            errors.append(
                f"{path.relative_to(ROOT)}: referência de imagem sem definição: {reference_id}"
            )
            continue
        destination = local_path(path, target)
        if destination is not None and not destination.resolve().is_file():
            errors.append(
                f"{path.relative_to(ROOT)}: imagem local inexistente: {markdown_target(target)}"
            )

    for reference_id in REFERENCE_LINK_RE.findall(text):
        target = definitions.get(normalize_reference_id(reference_id))
        if target is None:
            errors.append(
                f"{path.relative_to(ROOT)}: referência de link sem definição: {reference_id}"
            )
            continue
        destination = local_path(path, target)
        if destination is None:
            continue
        resolved = destination.resolve()
        if resolved.is_dir():
            resolved = resolved / "index.md"
        if not resolved.is_file():
            errors.append(
                f"{path.relative_to(ROOT)}: link relativo inexistente: {markdown_target(target)}"
            )


def bloom_sections(text: str) -> dict[str, str]:
    headings = list(MARKDOWN_HEADING_RE.finditer(text))
    bloom_heading = re.compile(
        rf"^(#{{1,6}})[ \t]+({'|'.join(map(re.escape, BLOOM))})(?:[ \t]+.*?)?[ \t]*$"
    )
    sections: dict[str, str] = {}
    for index, heading in enumerate(headings):
        match = bloom_heading.fullmatch(heading.group(0))
        if match is None:
            continue
        level = len(match.group(1))
        end = next(
            (
                following.start()
                for following in headings[index + 1:]
                if len(following.group(1)) <= level
            ),
            len(text),
        )
        sections[match.group(2)] = text[heading.end():end]
    return sections


def validate_exercises(path: Path, text: str, errors: list[str], counts: Counts) -> None:
    sections = bloom_sections(text)
    counts.exercises += len(sections)
    for level in BLOOM:
        if level not in sections:
            errors.append(f"{path.relative_to(ROOT)}: seção de Bloom ausente: {level}")

    for level in ("Recordar", "Compreender"):
        section = sections.get(level, "")
        if not re.search(r"<details(?:\s|>)", section, re.IGNORECASE) or not re.search(
            r"</details\s*>", section, re.IGNORECASE
        ):
            errors.append(f"{path.relative_to(ROOT)}: {level} requer bloco <details>")

    for level in ("Aplicar", "Analisar", "Avaliar", "Criar"):
        if not re.search(r"\bRubrica\b", sections.get(level, "")):
            errors.append(f"{path.relative_to(ROOT)}: {level} requer Rubrica")


def validate_module(slug: str, errors: list[str], counts: Counts) -> None:
    module_dir = DOCS / slug
    for page_name in PAGES:
        path = module_dir / page_name
        if not path.is_file():
            errors.append(f"página ausente: docs/{slug}/{page_name}")
            continue

        text = path.read_text(encoding="utf-8")
        counts.pages += 1
        counts.words += len(WORD_RE.findall(text))

        for marker in EDITORIAL_MARKERS:
            if re.search(rf"\b{marker}\b", text):
                errors.append(f"{path.relative_to(ROOT)}: marcador editorial proibido: {marker}")

        validate_references(path, text, errors, counts)
        if page_name == "exercicios.md":
            validate_exercises(path, text, errors, counts)


def validate_required_images(slugs: tuple[str, ...], include_cover: bool, errors: list[str]) -> None:
    required = [image for slug in slugs for image in MODULES[slug][1]]
    if include_cover:
        required.insert(0, COVER)
    for filename in required:
        if not (IMAGES / filename).is_file():
            errors.append(f"imagem obrigatória ausente: docs/assets/images/{filename}")


def main() -> int:
    args = parse_args()
    slugs = tuple(MODULES) if args.all else (args.module,)
    errors: list[str] = []
    counts = Counts()

    for slug in slugs:
        validate_module(slug, errors, counts)
    validate_required_images(slugs, include_cover=args.all, errors=errors)

    print(
        f"Páginas: {counts.pages} | Palavras: {counts.words} | "
        f"Imagens: {counts.images} | Exercícios: {counts.exercises}"
    )
    if errors:
        print(f"Validação falhou com {len(errors)} erro(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Validação concluída sem erros.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
