"""Round 9 hard-regime counterexample searches.

All lengths are encoded as powers of a large parameter L.  The script has
two independent checks.

1. Diagonal/permutation maps.  For each permutation we solve a linear program
   maximizing a common positive margin by which the three desired lower-bound
   alternatives fail, subject to sorted side lengths and linear Dil_2 <= 1.

2. Guth thesis Chapter 8.2 constructions.  We reuse the exponent move model
   in code/guth_ch8_exponent_search.py and run a larger random scan for
   all-three-failing examples among bounded-2-dilation snake/pinch/double-pinch
   compositions.
"""

from __future__ import annotations

from itertools import combinations, permutations
from pathlib import Path
import sys

import numpy as np
from scipy.optimize import linprog

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from code.guth_ch8_exponent_search import random_counterexample_scan


NAMES = ["r1", "r2", "r3", "r4", "s1", "s2", "s3", "s4", "m"]


def vec(**kw: float) -> np.ndarray:
    out = np.zeros(len(NAMES))
    for key, value in kw.items():
        out[NAMES.index(key)] = value
    return out


def diagonal_lp_report() -> list[str]:
    best: list[tuple[float, tuple[int, ...], np.ndarray]] = []
    for perm in permutations(range(4)):
        a_ub: list[np.ndarray] = []
        b_ub: list[float] = []
        a_eq: list[np.ndarray] = []
        b_eq: list[float] = []

        for i in range(3):
            row = np.zeros(len(NAMES))
            row[i] = 1
            row[i + 1] = -1
            a_ub.append(row)
            b_ub.append(0.0)

            row = np.zeros(len(NAMES))
            row[4 + i] = 1
            row[4 + i + 1] = -1
            a_ub.append(row)
            b_ub.append(0.0)

        # Normalize target scale/aspect to remove homogeneity.
        a_eq.append(vec(s1=1))
        b_eq.append(0.0)
        a_eq.append(vec(s4=1))
        b_eq.append(1.0)

        # Hard regime and desired-volume failure, each by margin m:
        # R1/S1 <= L^-m, R3R4/(S3S4) <= L^-m, V_R/target <= L^-m.
        a_ub.append(vec(r1=1, s1=-1, m=1))
        b_ub.append(0.0)
        a_ub.append(vec(r3=1, r4=1, s3=-1, s4=-1, m=1))
        b_ub.append(0.0)
        a_ub.append(vec(r1=1, r2=1, r3=1, r4=1, s1=-1, s2=-0.5, s3=-1.5, s4=-1, m=1))
        b_ub.append(0.0)

        # m >= 0 and a harmless upper bound to keep the LP bounded.
        a_ub.append(vec(m=-1))
        b_ub.append(0.0)
        a_ub.append(vec(m=1))
        b_ub.append(10.0)

        # Linear Dil_2 <= 1.  If q_i = s_i - r_perm[i], this is
        # equivalent to q_a + q_b <= 0 for every pair.
        for a, b in combinations(range(4), 2):
            row = np.zeros(len(NAMES))
            row[4 + a] += 1
            row[perm[a]] -= 1
            row[4 + b] += 1
            row[perm[b]] -= 1
            a_ub.append(row)
            b_ub.append(0.0)

        result = linprog(
            vec(m=-1),
            A_ub=np.array(a_ub),
            b_ub=np.array(b_ub),
            A_eq=np.array(a_eq),
            b_eq=np.array(b_eq),
            bounds=[(-20, 20)] * 8 + [(0, 10)],
            method="highs",
        )
        if result.success:
            best.append((-float(result.fun), perm, result.x))

    best.sort(reverse=True, key=lambda item: item[0])
    lines = ["# diagonal/permutation LP"]
    if not best:
        lines.append("No feasible solution.")
        return lines
    margin, _, _ = best[0]
    lines.append(f"best common failure margin: {margin:.12g}")
    if margin <= 1e-9:
        lines.append("Conclusion: no positive-margin hard-regime diagonal/permutation counterexample.")
    for margin, perm, x in best[:8]:
        q = [x[4 + i] - x[perm[i]] for i in range(4)]
        lines.append(f"perm={perm}, margin={margin:.12g}")
        lines.append("  r=" + " ".join(f"{z:.9g}" for z in x[:4]))
        lines.append("  s=" + " ".join(f"{z:.9g}" for z in x[4:8]))
        lines.append("  q=" + " ".join(f"{z:.9g}" for z in q) + f", top2={sum(sorted(q)[-2:]):.9g}")
    return lines


def guth_random_report(seeds: int = 3, trials: int = 1_000, depth: int = 4) -> list[str]:
    lines = ["# Guth Chapter 8.2 random composition scan"]
    lines.append(f"seeds={seeds}, trials_per_seed={trials}, depth={depth}")
    for seed in range(1, seeds + 1):
        lines.append(f"## seed {seed}")
        lines.extend(random_counterexample_scan(seed=seed, trials=trials, depth=depth))
    return lines


def main() -> None:
    out = []
    out.extend(diagonal_lp_report())
    out.append("")
    out.extend(guth_random_report())
    text = "\n".join(out) + "\n"
    Path("data").mkdir(exist_ok=True)
    Path("data/round9_hard_regime_search.txt").write_text(text)
    print(text)


if __name__ == "__main__":
    main()
