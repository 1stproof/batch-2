"""Bounded round-32 literature/archive search for Guth's missing preprint.

The script queries a small set of public metadata/search endpoints and saves raw
responses under data/round32_lit/.  It is intentionally conservative: the goal is
to record negative evidence and any new adjacent hits, not to crawl broadly.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import quote_plus

import requests


OUT = Path("data/round32_lit")
OUT.mkdir(parents=True, exist_ok=True)

TITLE = "On the 2-dilation of mappings between 4-dimensional rectangles"
QUERIES = [
    TITLE,
    "2-dilation of mappings between 4-dimensional rectangles Guth",
    "smallest 2-dilation degree 1 map rectangles Guth",
]


def fetch(name: str, url: str, *, timeout: int = 20) -> dict:
    path = OUT / name
    try:
        r = requests.get(url, timeout=timeout, headers={"User-Agent": "round32-lit-search/1.0"})
        path.write_bytes(r.content)
        return {
            "name": name,
            "url": url,
            "status": r.status_code,
            "bytes": len(r.content),
            "content_type": r.headers.get("content-type", ""),
        }
    except Exception as exc:  # noqa: BLE001
        path.with_suffix(path.suffix + ".ERROR.txt").write_text(f"{type(exc).__name__}: {exc}\n")
        return {"name": name, "url": url, "error": f"{type(exc).__name__}: {exc}"}


def archive_query(name: str, query: str) -> tuple[str, str]:
    params = quote_plus(query)
    url = (
        "https://archive.org/advancedsearch.php?"
        f"q={params}&fl%5B%5D=identifier&fl%5B%5D=title&fl%5B%5D=creator"
        "&fl%5B%5D=date&rows=25&page=1&output=json"
    )
    return name, url


def main() -> None:
    jobs: list[tuple[str, str]] = []
    jobs.append(("arxiv_exact.xml", "https://export.arxiv.org/api/query?search_query=all:%22" + quote_plus(TITLE) + "%22&start=0&max_results=10"))
    jobs.append(("crossref_exact.json", "https://api.crossref.org/works?rows=10&query.title=" + quote_plus(TITLE)))
    jobs.append(("openalex_exact.json", "https://api.openalex.org/works?per-page=10&search=" + quote_plus(TITLE)))
    jobs.append(("semanticscholar_exact.json", "https://api.semanticscholar.org/graph/v1/paper/search?limit=10&fields=title,authors,year,venue,url&query=" + quote_plus(TITLE)))
    jobs.append(("openlibrary_exact.json", "https://openlibrary.org/search.json?title=" + quote_plus(TITLE)))
    jobs.append(("mit_dspace_search.html", "https://dspace.mit.edu/simple-search?query=" + quote_plus(TITLE)))
    jobs.append(("hathitrust_search.html", "https://catalog.hathitrust.org/Search/Home?lookfor=" + quote_plus(TITLE) + "&searchtype=all"))
    jobs.append(("worldcat_search.html", "https://search.worldcat.org/search?q=" + quote_plus(TITLE)))
    jobs.append(("stanford_searchworks.html", "https://searchworks.stanford.edu/?q=" + quote_plus(TITLE)))
    jobs.append(("github_code_search.html", "https://github.com/search?q=%22" + quote_plus(TITLE) + "%22&type=code"))
    jobs.append(archive_query("ia_title_exact.json", 'title:"' + TITLE + '"'))
    jobs.append(archive_query("ia_text_exact.json", '"' + TITLE + '"'))
    jobs.append(archive_query("ia_text_variant.json", '"2-dilation" AND "4-dimensional rectangles" AND Guth'))

    cdx_hosts = [
        "math.mit.edu/~lguth/*",
        "www-math.mit.edu/~lguth/*",
        "math.stanford.edu/~lguth/*",
        "www.math.stanford.edu/~lguth/*",
        "cims.nyu.edu/~guth/*",
        "www.math.nyu.edu/~guth/*",
    ]
    for i, host in enumerate(cdx_hosts):
        jobs.append(
            (
                f"cdx_{i}_{host.replace('/', '_').replace('*', 'STAR')}.json",
                "https://web.archive.org/cdx?url="
                + quote_plus(host)
                + "&output=json&fl=timestamp,original,statuscode,mimetype,digest"
                + "&filter=statuscode:200&collapse=digest&limit=5000",
            )
        )

    summary = [fetch(name, url) for name, url in jobs]

    # Lightly parse saved responses for exact/near phrase hits.
    phrase_hits = []
    patterns = [
        re.compile(re.escape(TITLE), re.I),
        re.compile(r"2-dilation.{0,80}4-dimensional rectangles", re.I | re.S),
        re.compile(r"4-dimensional rectangles.{0,80}2-dilation", re.I | re.S),
    ]
    for item in summary:
        path = OUT / item["name"]
        if not path.exists():
            continue
        try:
            text = path.read_text(errors="ignore")
        except Exception:
            continue
        for pat in patterns:
            m = pat.search(text)
            if m:
                start = max(0, m.start() - 120)
                end = min(len(text), m.end() + 120)
                phrase_hits.append({"file": item["name"], "match": text[start:end].replace("\n", " ")})
                break

    # Parse CDX inventories for suggestive archived URLs.
    cdx_suggestive = []
    for item in summary:
        if not item["name"].startswith("cdx_"):
            continue
        path = OUT / item["name"]
        if not path.exists():
            continue
        try:
            rows = json.loads(path.read_text())
        except Exception:
            continue
        for row in rows[1:] if rows and isinstance(rows[0], list) else []:
            original = row[1].lower()
            if any(term in original for term in ["dil", "rect", "area", "width", "paper", "preprint"]):
                cdx_suggestive.append(row)

    report = {
        "queries": QUERIES,
        "summary": summary,
        "phrase_hits": phrase_hits[:50],
        "cdx_suggestive": cdx_suggestive[:100],
        "conclusion": (
            "No located endpoint returned a PDF/TeX/bibliographic record for the exact missing "
            "preprint title. Phrase hits, if any, are saved above and are expected to be only "
            "search-page echoes or adjacent citations."
        ),
    }
    (OUT / "round32_lit_search_summary.json").write_text(json.dumps(report, indent=2))
    print(json.dumps(report, indent=2)[:6000])


if __name__ == "__main__":
    main()
