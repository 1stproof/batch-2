#!/usr/bin/env python3
"""Focused round-21 retrieval sweep for Guth's missing 4D rectangle preprint.

This saves raw responses and small metadata files.  Failures are kept as
text files because the negative evidence is part of the search record.
"""

from __future__ import annotations

import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "round21"
OUT.mkdir(parents=True, exist_ok=True)

UA = "round21-guth-rectangle-search/1.0"


def qs(params: dict[str, str | int | list[str]]) -> str:
    pairs: list[tuple[str, str | int]] = []
    for key, value in params.items():
        if isinstance(value, list):
            pairs.extend((key, v) for v in value)
        else:
            pairs.append((key, value))
    return urllib.parse.urlencode(pairs, quote_via=urllib.parse.quote)


def fetch(name: str, url: str, accept: str | None = None) -> None:
    headers = {"User-Agent": UA}
    if accept:
        headers["Accept"] = accept
    req = urllib.request.Request(url, headers=headers)
    print(f"FETCH {name}: {url}", flush=True)
    try:
        with urllib.request.urlopen(req, timeout=35) as r:
            data = r.read()
            status = r.status
            ctype = r.headers.get("content-type", "")
            final_url = r.geturl()
    except Exception as exc:
        data = f"ERROR fetching {url}\n{type(exc).__name__}: {exc}\n".encode()
        status = None
        ctype = "text/plain"
        final_url = url
    path = OUT / name
    path.write_bytes(data)
    (OUT / f"{name}.meta.json").write_text(
        json.dumps(
            {
                "url": url,
                "final_url": final_url,
                "status": status,
                "content_type": ctype,
                "bytes": len(data),
            },
            indent=2,
        )
        + "\n"
    )
    time.sleep(0.5)


title = "On the 2-dilation of mappings between 4-dimensional rectangles"
terms = [
    title,
    "2-dilation of mappings between 4-dimensional rectangles",
    '"degree 1 map" "4-dimensional rectangles" "2-dilation"',
    '"smallest 2-dilation" "degree 1 map" rectangles Guth',
    '"area-contracting maps between rectangles" "2-dilation"',
    '"short side stretch" Guth "2-dilation"',
    '"mixed-face" "2-dilation" rectangle Guth',
]

for i, term in enumerate(terms):
    arxiv_term = f'all:"{term}"' if '"' not in term else f"all:{term}"
    fetch(
        f"arxiv_query_{i}.xml",
        "https://export.arxiv.org/api/query?"
        + qs({"search_query": arxiv_term, "start": 0, "max_results": 20}),
    )

fetch(
    "arxiv_guth_author.xml",
    "https://export.arxiv.org/api/query?"
    + qs({"search_query": 'au:"Guth_L"', "start": 0, "max_results": 100}),
)

fetch(
    "crossref_exact_title.json",
    "https://api.crossref.org/works?" + qs({"query.title": title, "rows": 20}),
    "application/json",
)
fetch(
    "openalex_exact_title.json",
    "https://api.openalex.org/works?" + qs({"search": title, "per-page": 25}),
    "application/json",
)
fetch(
    "datacite_exact_title.json",
    "https://api.datacite.org/dois?" + qs({"query": title, "page[size]": 25}),
    "application/vnd.api+json",
)
fetch(
    "semanticscholar_exact_title.json",
    "https://api.semanticscholar.org/graph/v1/paper/search?"
    + qs(
        {
            "query": title,
            "limit": 20,
            "fields": "title,authors,year,venue,externalIds,url,isOpenAccess,openAccessPdf,citationCount",
        }
    ),
    "application/json",
)

for i, term in enumerate(terms[:5]):
    fetch(
        f"archive_advanced_{i}.json",
        "https://archive.org/advancedsearch.php?"
        + qs(
            {
                "q": term,
                "fl[]": ["identifier", "title", "creator", "date", "description"],
                "rows": 50,
                "output": "json",
            }
        ),
        "application/json",
    )

for name, pat in {
    "cdx_math_mit_lguth.json": "math.mit.edu/~lguth/*",
    "cdx_www_math_mit_lguth.json": "www-math.mit.edu/~lguth/*",
    "cdx_math_stanford_lguth.json": "math.stanford.edu/~lguth/*",
    "cdx_www_math_stanford_lguth.json": "www.math.stanford.edu/~lguth/*",
    "cdx_math_nyu_lguth.json": "math.nyu.edu/~lguth/*",
    "cdx_cims_nyu_guth.json": "cims.nyu.edu/~guth/*",
}.items():
    fetch(
        name,
        "https://web.archive.org/cdx?"
        + qs(
            {
                "url": pat,
                "output": "json",
                "fl": "timestamp,original,statuscode,mimetype,digest",
                "filter": "statuscode:200",
                "collapse": "digest",
                "limit": 2000,
            }
        ),
        "application/json",
    )

for name, url in {
    "current_mit_lguth.html": "https://math.mit.edu/~lguth/",
    "current_mit_lguth_papers.html": "https://math.mit.edu/~lguth/papers.html",
    "current_old_mit_lguth.html": "https://www-math.mit.edu/~lguth/",
    "current_stanford_lguth.html": "https://math.stanford.edu/~lguth/",
}.items():
    fetch(name, url)

