"""Lean runner for the round 3 cap-vector computations.

This imports the routines in round3_cap_vector.py but avoids the slower large
differential-evolution grid.  It writes incrementally so partial evidence is not
lost if a later MILP case is slow.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np

from round3_cap_vector import (
    cap_vector_weights,
    chamber_min,
    g4,
    hit_and_run_min,
    maximal_members,
    milp_fail_mass,
    rank_le_one_tail,
    tail_prob,
)


OUT = Path("data/round3_cap_vector_fast_output.txt")


def append(lines: list[str], text: str = "") -> None:
    lines.append(text)
    OUT.write_text("\n".join(lines) + "\n")


def min_support(p: float) -> int:
    return int(np.floor(1 / p)) + 1


def main() -> None:
    p_values = [0.25, 0.26, 2 / 7, 0.3, 1 / 3]
    lines: list[str] = []
    OUT.parent.mkdir(parents=True, exist_ok=True)

    append(lines, "Round 3 cap-vector conjecture computations (lean run)")
    append(lines)
    append(lines, "g4(p)=P[Bin(4,p)>=2]")
    for p in p_values:
        append(lines, f"p={p:.12f} g4={g4(p):.12f} gap_g4_minus_p={g4(p)-p:.12f}")
    append(lines)

    append(lines, "1. Explicit extremal families")
    for p in p_values:
        if p > 0.25:
            eps = min(1e-6, (4 * p - 1) / 10)
            w = cap_vector_weights(p, eps)
            append(
                lines,
                f"p={p:.12f} cap-vector weights={np.round(w, 10).tolist()} "
                f"tail={tail_prob(w, p):.12f} g4={g4(p):.12f}",
            )
        else:
            append(
                lines,
                f"p={p:.12f} strict four-cap vector infeasible; "
                f"rank<=1 on five coordinates tail={rank_le_one_tail(5, p):.12f}",
            )
    append(lines)

    append(lines, "2. Hit-and-run nonlinear search on capped simplex")
    for p in p_values:
        n0 = min_support(p)
        test_ns = sorted(set([n0, n0 + 1, max(n0 + 2, 8)]))
        for n in test_ns:
            val, w = hit_and_run_min(p, n, seed=7300 + n + int(10000 * p), steps=6000)
            append(
                lines,
                f"p={p:.12f} n={n:2d} hitrun_min={val:.12f} "
                f"minus_g4={val-g4(p):.12f} weights={np.round(w, 7).tolist()}",
            )
        append(lines)

    append(lines, "3. Exact chamber/down-set enumeration for m<=5")
    for p in p_values:
        chamber_ms = range(1, 6) if p == 0.25 else range(1, 5)
        for m in chamber_ms:
            res = chamber_min(m, p)
            if res is None:
                append(lines, f"p={p:.12f} m={m} no strict-cap threshold chambers")
            else:
                append(
                    lines,
                    f"p={p:.12f} m={m} feasible={res.count_feasible:4d} "
                    f"min_tail={res.tail:.12f} minus_g4={res.tail-g4(p):.12f} "
                    f"margin={res.margin:.3g} maxD={maximal_members(res.fam,m)}",
                )
        append(lines)

    append(lines, "4. MILP/separation search")
    for p in p_values:
        n0 = max(4, min_support(p))
        max_n = 7
        for n in range(n0, max_n + 1):
            res, fail, w = milp_fail_mass(n, p, eps=1e-4, time_limit=20.0)
            if fail is None:
                append(lines, f"p={p:.12f} n={n:2d} MILP status={res.message}")
                continue
            tail = 1.0 - fail
            append(
                lines,
                f"p={p:.12f} n={n:2d} milp_tail={tail:.12f} "
                f"minus_g4={tail-g4(p):.12f} weights={np.round(w, 7).tolist()} "
                f"nodes={getattr(res, 'mip_node_count', 'na')} gap={getattr(res, 'mip_gap', 'na')}",
            )
        append(lines)

    print(OUT)


if __name__ == "__main__":
    main()
