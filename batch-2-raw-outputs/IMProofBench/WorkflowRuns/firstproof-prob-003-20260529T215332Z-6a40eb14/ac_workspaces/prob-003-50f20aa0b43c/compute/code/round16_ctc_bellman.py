#!/usr/bin/env python3
"""Round 16 finite-grid Bellman checks for the centered tail comparison.

For rational p=a/d and coefficients c in {1/M,2/M,...,1}, the centered
increments are -p c and q c.  In units 1/(dM), these shifts are -a k and
(d-a) k.  This script computes the exact adaptive dynamic-programming value

    V_r(x) = inf E g(x + sum c_i(zeta_i-p))

over choices of remaining coefficients with total r/M, where the next
coefficient may depend on the current state x.  This adaptivity is stronger
than the original problem, whose coefficients are fixed in advance.

    g(y)=q 1_{y>=p} - p 1_{y<-q}.

It is a finite-grid diagnostic for possible Bellman barriers, not a proof for
arbitrary real coefficients.  Negative values show that a Bellman proof with
only (x, remaining total mass) as state is too weak for the non-adaptive CTC.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, asdict
from fractions import Fraction
from pathlib import Path


@dataclass
class BellmanRecord:
    p: str
    mesh: int
    total: str
    value_at_zero: str
    first_coeff: str | None
    approx_value: float


def fstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def terminal_value(idx: int, a: int, d: int, mesh: int) -> float:
    """Payoff at x=idx/(d*mesh)."""

    # x >= p=a/d iff idx >= a*mesh.
    if idx >= a * mesh:
        return (d - a) / d
    # x < -q=-(d-a)/d iff idx < -(d-a)*mesh.
    if idx < -(d - a) * mesh:
        return -a / d
    return 0.0


def solve(p: Fraction, mesh: int, r_max: int) -> tuple[list[BellmanRecord], dict[str, object]]:
    a = p.numerator
    d = p.denominator
    qnum = d - a

    # V[r] is a dict indexed by x-units idx.  For total r/mesh, the attainable
    # support lies in [-a*r, qnum*r].
    values: list[dict[int, float]] = []
    choices: list[dict[int, int | None]] = []

    global_lo = -a * r_max
    global_hi = qnum * r_max
    v0 = {idx: terminal_value(idx, a, d, mesh) for idx in range(global_lo, global_hi + 1)}
    # Work on one fixed x-window for every r.  The window contains all states
    # queried from x=0 with total mass at most r_max/mesh.
    values.append(v0)
    choices.append({idx: None for idx in v0})

    for r in range(1, r_max + 1):
        cur: dict[int, float] = {}
        arg: dict[int, int | None] = {}
        lo = -a * (r_max - r)
        hi = qnum * (r_max - r)
        for idx in range(lo, hi + 1):
            best: float | None = None
            best_k: int | None = None
            for k in range(1, min(mesh, r) + 1):
                prev = values[r - k]
                # T_c f(x)=q f(x-pc)+p f(x+qc).
                left = idx - a * k
                right = idx + qnum * k
                if left not in prev or right not in prev:
                    continue
                val = (qnum / d) * prev[left] + (a / d) * prev[right]
                if best is None or val < best:
                    best = val
                    best_k = k
            if best is None:
                raise RuntimeError(f"no transition for r={r}, idx={idx}")
            cur[idx] = best
            arg[idx] = best_k
        values.append(cur)
        choices.append(arg)

    records: list[BellmanRecord] = []
    for r in range(0, r_max + 1):
        val = values[r][0]
        k = choices[r].get(0)
        records.append(
            BellmanRecord(
                p=fstr(p),
                mesh=mesh,
                total=fstr(Fraction(r, mesh)),
                value_at_zero=f"{val:.17g}",
                first_coeff=None if k is None else fstr(Fraction(k, mesh)),
                approx_value=float(val),
            )
        )

    best = min(records, key=lambda z: z.approx_value)
    meta = {
        "p": fstr(p),
        "mesh": mesh,
        "r_max": r_max,
        "best": asdict(best),
        "unit": f"1/{d * mesh}",
    }
    return records, meta


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="data/round16/bellman_grid.json")
    parser.add_argument("--mesh", type=int, default=20)
    parser.add_argument("--r-max", type=int, default=240)
    args = parser.parse_args()

    payload: dict[str, object] = {"runs": []}
    for p in [Fraction(1, 6), Fraction(1, 5), Fraction(1, 4), Fraction(3, 10), Fraction(1, 3)]:
        records, meta = solve(p, args.mesh, args.r_max)
        payload["runs"].append({"meta": meta, "records": [asdict(x) for x in records]})

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

    for run in payload["runs"]:
        meta = run["meta"]
        print(
            f"p={meta['p']} mesh={meta['mesh']} r_max={meta['r_max']} "
            f"best_total={meta['best']['total']} best_value={meta['best']['value_at_zero']} "
            f"first_coeff={meta['best']['first_coeff']}"
        )


if __name__ == "__main__":
    main()
