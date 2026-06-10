#!/usr/bin/env python3
"""LP enumeration of small threshold up-families for round 18.

For fixed n and q, enumerate all downsets D on [n].  Its complement U is an
up-family.  We test whether U is representable as

    U = {A : w(A) > q}

for some probability vector w by maximizing a strict margin delta:

    w(A) >= q + delta  for A in U,
    w(A) <= q          for A not in U,
    w_i >= 0, sum w_i = 1.

Then we record max mu_q(U)-q among representable up-families.  This is not a
proof for all n, but it gives exact finite-dimensional diagnostics for n <= 5.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from code.round14_downset_hull import all_downsets
from compute_utils import safe_json_dump


def mu_up(fam: int, n: int, q: float) -> float:
    p = 1.0 - q
    total = 0.0
    for mask in range(1 << n):
        if (fam >> mask) & 1:
            k = mask.bit_count()
            total += (q**k) * (p ** (n - k))
    return total


def mask_str(mask: int, n: int) -> str:
    if mask == 0:
        return "{}"
    return "".join(str(i + 1) for i in range(n) if (mask >> i) & 1)


def minimal_members(fam: int, n: int) -> list[str]:
    out = []
    for mask in range(1 << n):
        if not ((fam >> mask) & 1):
            continue
        ok = True
        s = mask
        while s:
            b = s & -s
            if (fam >> (mask ^ b)) & 1:
                ok = False
                break
            s -= b
        if ok:
            out.append(mask_str(mask, n))
    return out


def threshold_margin(upfam: int, n: int, q: float) -> tuple[float, list[float] | None]:
    """Maximize strict margin for upfam = {A: w(A)>q}."""
    # variables w_0,...,w_{n-1}, delta. Max delta == min -delta.
    c = np.zeros(n + 1)
    c[-1] = -1.0
    rows = []
    rhs = []
    for mask in range(1 << n):
        row = np.zeros(n + 1)
        for i in range(n):
            if (mask >> i) & 1:
                row[i] = 1.0
        if (upfam >> mask) & 1:
            # -w(A) + delta <= -q
            rows.append(-row + np.r_[np.zeros(n), 1.0])
            rhs.append(-q)
        else:
            # w(A) <= q
            rows.append(row)
            rhs.append(q)
    eq = np.zeros((1, n + 1))
    eq[0, :n] = 1.0
    res = linprog(
        c,
        A_ub=np.array(rows),
        b_ub=np.array(rhs),
        A_eq=eq,
        b_eq=np.array([1.0]),
        bounds=[(0.0, 1.0)] * n + [(0.0, 1.0)],
        method="highs",
    )
    if not res.success:
        return -1.0, None
    return float(res.x[-1]), [float(x) for x in res.x[:n]]


def run() -> list[dict]:
    q_values = [2 / 3, 0.67, 0.68, 0.7, 0.72, 0.75, 0.8, 0.85, 0.9]
    out = []
    for n in range(1, 6):
        full = (1 << (1 << n)) - 1
        downsets = all_downsets(n)
        for q in q_values:
            best = None
            feasible = 0
            for down in downsets:
                up = full ^ down
                margin, weights = threshold_margin(up, n, q)
                if margin <= 1e-9:
                    continue
                feasible += 1
                mu = mu_up(up, n, q)
                rec = {
                    "n": n,
                    "q": q,
                    "mu": mu,
                    "mu_minus_q": mu - q,
                    "margin": margin,
                    "weights": weights,
                    "minimal_members": minimal_members(up, n),
                }
                if best is None or rec["mu_minus_q"] > best["mu_minus_q"]:
                    best = rec
            out.append(
                {
                    "n": n,
                    "q": q,
                    "downsets": len(downsets),
                    "threshold_upfamilies": feasible,
                    "best": best,
                }
            )
    return out


def main() -> None:
    data = run()
    out = ROOT / "data" / "round18" / "threshold_lp_n5.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    safe_json_dump(data, out)
    print(f"wrote {out}")
    for rec in data:
        b = rec["best"]
        print(
            "n", rec["n"],
            "q", rec["q"],
            "feasible", rec["threshold_upfamilies"],
            "best_mu-q", None if b is None else b["mu_minus_q"],
            "mins", None if b is None else b["minimal_members"],
        )


if __name__ == "__main__":
    main()
