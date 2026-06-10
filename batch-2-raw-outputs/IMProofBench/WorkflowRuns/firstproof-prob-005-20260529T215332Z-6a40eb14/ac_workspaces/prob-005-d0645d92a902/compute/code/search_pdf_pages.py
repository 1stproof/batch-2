#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path


def compact(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("text_file", type=Path)
    parser.add_argument("patterns", nargs="+")
    parser.add_argument("--context", type=int, default=180)
    args = parser.parse_args()

    text = args.text_file.read_text(errors="replace")
    pages = text.split("\f")
    regexes = [re.compile(p, re.IGNORECASE) for p in args.patterns]
    for page_no, page in enumerate(pages, start=1):
        flat = compact(page)
        for regex in regexes:
            for match in regex.finditer(flat):
                start = max(0, match.start() - args.context)
                end = min(len(flat), match.end() + args.context)
                print(f"page {page_no}: /{regex.pattern}/")
                print(flat[start:end])
                print()


if __name__ == "__main__":
    main()
