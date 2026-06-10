#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data" / "round28_lit"

PDF_TEXTS = {
    "Guth thesis PDF text": OUT / "Guth_thesis_pdftotext_layout.txt",
    "Guth thesis DSpace OCR": OUT / "Guth_thesis_DSpace_extracted_text.txt",
    "arXiv 0710.0403 PDF text": OUT / "arxiv_0710.0403.txt",
    "arXiv 0802.3549 PDF text": OUT / "arxiv_0802.3549.txt",
    "arXiv 0802.3550 PDF text": OUT / "arxiv_0802.3550.txt",
}

TEX_SOURCES = {
    "arXiv 0710.0403 source": ROOT / "papers" / "arxiv_0710.0403_source_dir" / "EXEMB2.TEX",
    "arXiv 0802.3549 source": ROOT / "papers" / "arxiv_0802.3549_source_dir" / "LINKDIL2.TEX",
    "arXiv 0802.3550 source": ROOT / "papers" / "arxiv_0802.3550_source_dir" / "LINKDIL1.TEX",
}

TERMS = {
    "2-dilation": [r"2[- ]dilation", r"2[- ]contracting"],
    "4-dimensional rectangles": [r"4[- ]dimensional rectangles", r"four[- ]dimensional rectangles"],
    "R_3 R_4": [r"R_3\s*R_4", r"R3\s*R4", r"R\s*3\s*R\s*4"],
    "S_3 S_4": [r"S_3\s*S_4", r"S3\s*S4", r"S\s*3\s*S\s*4"],
    "S_2^{1/2}": [r"S_2\^\{?1/2\}?", r"S2\s*(\^|\*\*)?\s*1/2"],
    "S_3^{3/2}": [r"S_3\^\{?3/2\}?", r"S3\s*(\^|\*\*)?\s*3/2"],
    "degree": [r"\bdegree\b"],
    "rectangle": [r"\brectangles?\b"],
    "tightening": [r"\btightening\b"],
    "sweepout": [r"\bsweepout\b"],
    "fiber": [r"\bfibers?\b"],
    "preprint title": [r"On the 2-dilation of mappings between 4-dimensional rectangles"],
}


def clean(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def page_marker_for_lines(lines: list[str]) -> list[str | None]:
    current = None
    pages = []
    for line in lines:
        stripped = line.strip()
        if stripped.isdigit():
            n = int(stripped)
            # The MIT OCR often puts variable subscripts on their own lines
            # ("1", "2", ...).  Treat only two- or three-digit standalone
            # numbers as printed page markers.
            if 10 <= n <= 250:
                current = stripped
        pages.append(current)
    return pages


def search_plain_text(name: str, path: Path, max_hits_per_term: int = 25) -> list[str]:
    text = path.read_text(errors="replace")
    lines = text.splitlines()
    if "\f" in text:
        pages = text.split("\f")
        lines_with_pages: list[tuple[str, int | str, int]] = []
        for pageno, page in enumerate(pages, start=1):
            for lineno, line in enumerate(page.splitlines(), start=1):
                lines_with_pages.append((line, pageno, lineno))
    else:
        markers = page_marker_for_lines(lines)
        lines_with_pages = [(line, markers[i] or "?", i + 1) for i, line in enumerate(lines)]

    report = [f"## {name}", f"Path: `{path}`", ""]
    for term, patterns in TERMS.items():
        hits = []
        regs = [re.compile(p, re.I) for p in patterns]
        for idx, (line, page, lineno) in enumerate(lines_with_pages):
            if any(r.search(line) for r in regs):
                context = clean(line)
                if not context:
                    before = clean(lines_with_pages[idx - 1][0]) if idx else ""
                    after = clean(lines_with_pages[idx + 1][0]) if idx + 1 < len(lines_with_pages) else ""
                    context = clean(before + " " + after)
                hits.append((page, lineno, context))
                if len(hits) >= max_hits_per_term:
                    break
        report.append(f"### {term}: {len(hits)} shown")
        if hits:
            for page, lineno, context in hits:
                report.append(f"- page {page}, line {lineno}: {context[:260]}")
        else:
            report.append("- no hits")
        report.append("")
    return report


def search_tex(name: str, path: Path, max_hits_per_term: int = 25) -> list[str]:
    lines = path.read_text(errors="replace").splitlines()
    report = [f"## {name}", f"Path: `{path}`", ""]
    for term, patterns in TERMS.items():
        hits = []
        regs = [re.compile(p, re.I) for p in patterns]
        for lineno, line in enumerate(lines, start=1):
            if any(r.search(line) for r in regs):
                hits.append((lineno, clean(line)))
                if len(hits) >= max_hits_per_term:
                    break
        report.append(f"### {term}: {len(hits)} shown")
        if hits:
            for lineno, context in hits:
                report.append(f"- line {lineno}: {context[:260]}")
        else:
            report.append("- no hits")
        report.append("")
    return report


def main() -> None:
    chunks = ["# Round 28 Literature Search Hits", ""]
    for name, path in PDF_TEXTS.items():
        chunks.extend(search_plain_text(name, path))
        chunks.append("")
    chunks.extend(["# TeX Source Hits", ""])
    for name, path in TEX_SOURCES.items():
        chunks.extend(search_tex(name, path))
        chunks.append("")
    (OUT / "search_hits.md").write_text("\n".join(chunks))


if __name__ == "__main__":
    main()
