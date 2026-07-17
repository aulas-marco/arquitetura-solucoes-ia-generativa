"""MkDocs hook that attaches explicit visual classes to semantic HTML.

The public source remains ordinary Markdown for GitHub. The hook maps stable,
meaningful structures in MkDocs' generated page fragment to the Academia CSS
components, avoiding broad positional selectors that affect unrelated prose.
"""

from __future__ import annotations

import re


BLOOM_IDS = ("recordar", "compreender", "aplicar", "analisar", "avaliar", "criar")
OBJECTIVE_IDS = ("objetivos-de-aprendizagem", "o-que-voce-aprendera")


def _with_class(opening_tag: str, class_name: str) -> str:
    """Add one class to an opening tag while preserving all existing attributes."""
    class_match = re.search(r'\bclass="([^"]*)"', opening_tag)
    if class_match:
        classes = class_match.group(1).split()
        if class_name not in classes:
            classes.append(class_name)
        return (
            opening_tag[:class_match.start(1)]
            + " ".join(classes)
            + opening_tag[class_match.end(1):]
        )
    return re.sub(r"^(<[a-z0-9]+)", rf'\1 class="{class_name}"', opening_tag, count=1)


def _class_opening_tags(html: str, pattern: str, class_name: str) -> str:
    return re.sub(pattern, lambda match: _with_class(match.group(0), class_name), html)


def _decorate_objective_block(match: re.Match[str]) -> str:
    before, opening, items, closing = match.groups()
    opening = _with_class(opening, "objectives-grid")
    items = re.sub(
        r"<li(?:\s[^>]*)?>",
        lambda item: _with_class(item.group(0), "objective-card"),
        items,
    )
    return before + opening + items + closing


def _decorate_separate_figure(match: re.Match[str]) -> str:
    image_open, image, whitespace, caption_open, caption, caption_close = match.groups()
    return (
        _with_class(image_open, "architecture-figure")
        + image
        + "</p>"
        + whitespace
        + _with_class(caption_open, "figure-caption")
        + caption
        + caption_close
    )


def on_page_content(html: str, **_kwargs) -> str:
    """Decorate semantic page fragments after Markdown conversion."""
    html = _class_opening_tags(html, r"<h1(?:\s[^>]*)?>", "module-opening")
    html = _class_opening_tags(html, r"<table(?:\s[^>]*)?>", "comparison-table")
    html = _class_opening_tags(html, r"<details(?:\s[^>]*)?>", "answer-details")

    bloom_pattern = rf'<h2\b[^>]*\bid="(?:{"|".join(BLOOM_IDS)})"[^>]*>'
    html = _class_opening_tags(html, bloom_pattern, "bloom-label")
    html = _class_opening_tags(
        html,
        r'<h[23]\b[^>]*\bid="adr-[^"]+"[^>]*>',
        "adr-block",
    )

    objective_pattern = re.compile(
        rf'(<h2\b[^>]*\bid="(?:{"|".join(OBJECTIVE_IDS)})"[^>]*>.*?</h2>'
        r"\s*<p>.*?</p>\s*)(<ol(?:\s[^>]*)?>)(.*?)(</ol>)",
        re.DOTALL,
    )
    html = objective_pattern.sub(_decorate_objective_block, html)

    spine_pattern = re.compile(
        r'(<h2\b[^>]*\bid="espinha-de-aprendizagem"[^>]*>.*?</h2>'
        r"\s*<p>.*?</p>\s*)(<ol(?:\s[^>]*)?>)",
        re.DOTALL,
    )
    html = spine_pattern.sub(
        lambda match: match.group(1) + _with_class(match.group(2), "learning-spine"),
        html,
    )

    html = _class_opening_tags(
        html,
        r"<blockquote(?:\s[^>]*)?>(?=\s*<p><strong>Decisão arquitetural:)",
        "decision-callout",
    )
    html = _class_opening_tags(
        html,
        r"<blockquote(?:\s[^>]*)?>(?=\s*<p><strong>Risco arquitetural:)",
        "risk-callout",
    )

    html = _class_opening_tags(
        html,
        r"<p(?:\s[^>]*)?>(?=<img\b[^>]*>\s*<em>Figura\b)",
        "architecture-figure",
    )
    html = re.sub(
        r'(<p\b[^>]*\bclass="[^"]*architecture-figure[^"]*"[^>]*>'
        r"\s*<img\b[^>]*>\s*)<em>",
        r'\1<em class="figure-caption">',
        html,
    )
    html = re.sub(
        r"(<p(?:\s[^>]*)?>)(<img\b[^>]*>)</p>(\s*)"
        r"(<p(?:\s[^>]*)?>)(<em>Figura\b.*?</em>)(</p>)",
        _decorate_separate_figure,
        html,
        flags=re.DOTALL,
    )

    html = _class_opening_tags(
        html,
        r"<p(?:\s[^>]*)?>(?=<strong>Critérios de avaliação\b)",
        "criteria",
    )
    return html
