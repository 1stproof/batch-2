#!/usr/bin/env python3
"""Round 17 bibliographic/index search for Guth's missing 4D rectangle preprint.

The script intentionally saves raw API responses so later rounds can inspect
exact queries and rerun with different terms.
"""

from __future__ import annotations

import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "round17"
OUT.mkdir(parents=True, exist_ok=True)

UA = "round17-guth-rectangle-search/1.0 (mathematical literature retrieval)"


def fetch(url: str, name: str, *, accept: str | None = None) -> None:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    if accept:
        req.add_header("Accept", accept)
    print(f"FETCH {name}: {url}")
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            data = r.read()
            ctype = r.headers.get("content-type", "")
    except Exception as exc:  # keep going; failures are part of the search log.
        data = f"ERROR fetching {url}\n{type(exc).__name__}: {exc}\n".encode()
        ctype = "text/plain"
    path = OUT / name
    path.write_bytes(data)
    (OUT / f"{name}.meta.json").write_text(
        json.dumps({"url": url, "content_type": ctype, "bytes": len(data)}, indent=2)
        + "\n"
    )
    time.sleep(0.7)


title = "On the 2-dilation of mappings between 4-dimensional rectangles"
terms = [
    title,
    "2-dilation of mappings between 4-dimensional rectangles",
    "D2(R,S) Guth rectangles",
    '"degree 1 map" "4-dimensional rectangles" "2-dilation"',
    '"smallest 2-dilation" "degree 1 map" rectangles Guth',
    '"2-dilation" "4-dimensional rectangles" "recently solved"',
]


def qs(params: dict[str, str | int]) -> str:
    return urllib.parse.urlencode(params, quote_via=urllib.parse.quote)


# arXiv API: exact title and author/title/abstract variants.
for i, term in enumerate(terms):
    q = f'all:"{term}"' if '"' not in term else f"all:{term}"
    fetch(
        "https://export.arxiv.org/api/query?"
        + qs({"search_query": q, "start": 0, "max_results": 20}),
        f"arxiv_query_{i}.xml",
    )

fetch(
    "https://export.arxiv.org/api/query?"
    + qs({"search_query": 'au:"Guth_L" AND all:"2-dilation"', "start": 0, "max_results": 50}),
    "arxiv_guth_2dilation.xml",
)

# Crossref/OpenAlex/DataCite.
fetch(
    "https://api.crossref.org/works?"
    + qs({"query.title": title, "rows": 20}),
    "crossref_exact_title.json",
    accept="application/json",
)
fetch(
    "https://api.openalex.org/works?"
    + qs({"search": title, "per-page": 25}),
    "openalex_exact_title.json",
    accept="application/json",
)
fetch(
    "https://api.datacite.org/dois?"
    + qs({"query": title, "page[size]": 25}),
    "datacite_exact_title.json",
    accept="application/vnd.api+json",
)

# Semantic Scholar can be useful for preprint references even when no DOI exists.
fetch(
    "https://api.semanticscholar.org/graph/v1/paper/search?"
    + qs(
        {
            "query": title,
            "limit": 20,
            "fields": "title,authors,year,venue,externalIds,url,isOpenAccess,openAccessPdf,citationCount",
        }
    ),
    "semanticscholar_exact_title.json",
    accept="application/json",
)
fetch(
    "https://api.semanticscholar.org/graph/v1/paper/search?"
    + qs(
        {
            "query": "Guth 2-dilation 4-dimensional rectangles",
            "limit": 50,
            "fields": "title,authors,year,venue,externalIds,url,isOpenAccess,openAccessPdf,citationCount",
        }
    ),
    "semanticscholar_guth_2dilation_rectangles.json",
    accept="application/json",
)

# Internet Archive metadata search and CDX crawl snapshots.
for i, term in enumerate(terms[:4]):
    fetch(
        "https://archive.org/advancedsearch.php?"
        + qs(
            {
                "q": term,
                "fl[]": "identifier,title,creator,date,description",
                "rows": 50,
                "output": "json",
            }
        ),
        f"archive_advanced_{i}.json",
        accept="application/json",
    )

cdx_patterns = {
    "cdx_math_mit_lguth": "math.mit.edu/~lguth/*",
    "cdx_www_math_mit_lguth": "www-math.mit.edu/~lguth/*",
    "cdx_math_stanford_lguth": "math.stanford.edu/~lguth/*",
    "cdx_www_math_stanford_lguth": "www.math.stanford.edu/~lguth/*",
    "cdx_stanford_lguth": "stanford.edu/~lguth/*",
    "cdx_math_nyu_lguth": "math.nyu.edu/~lguth/*",
    "cdx_cims_nyu_guth": "cims.nyu.edu/~guth/*",
}

for name, urlpat in cdx_patterns.items():
    fetch(
        "https://web.archive.org/cdx?"
        + qs(
            {
                "url": urlpat,
                "output": "json",
                "fl": "timestamp,original,statuscode,mimetype,digest",
                "filter": "statuscode:200",
                "collapse": "digest",
                "limit": 2000,
            }
        ),
        f"{name}.json",
        accept="application/json",
    )

# Current pages likely to contain paper lists.
for name, url in {
    "current_mit_lguth.html": "https://math.mit.edu/~lguth/",
    "current_mit_lguth_papers.html": "https://math.mit.edu/~lguth/papers.html",
    "current_old_mit_lguth.html": "https://www-math.mit.edu/~lguth/",
}.items():
    fetch(url, name)

