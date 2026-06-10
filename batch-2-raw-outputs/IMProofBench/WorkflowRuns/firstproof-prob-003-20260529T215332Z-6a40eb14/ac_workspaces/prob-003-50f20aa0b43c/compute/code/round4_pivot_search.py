#!/usr/bin/env python3
"""Round 4 computations for the pivot two-tail inequality.

The main finite-dimensional search is a MILP over threshold chambers.  For
fixed p,a,n and weights w_i of total 1-a, the pivot violation is

    V(w) = lambda * P[w(R) < p-a] - P[w(R) >= p].

A counterexample is V(w)>0.  The binary variables label, for every subset A,
which side of the lower threshold p-a and upper threshold p it lies on.
The "outer" MILP treats equality at either threshold in the direction most
favorable to a violation; hence an outer optimum <=0 rules out counterexamples
for that (p,a,n).  The "strict" MILP enforces a small gap from the thresholds
and any positive strict solution is checked by direct evaluation.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from math import comb
from pathlib import Path
from typing import Iterable

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import lil_matrix
from scipy.stats import binom


@dataclass
class MilpResult:
    p: Fraction
    a: Fraction
    n: int
    kind: str
    success: bool
    max_violation: float
    direct_violation: float | None
    tail: float | None
    bad: float | None
    weights: list[float] | None
    message: str
    mip_gap: float | None = None
    mip_dual_bound: float | None = None


def subset_probabilities(n: int, p: float) -> np.ndarray:
    probs = np.empty(1 << n, dtype=float)
    q = 1.0 - p
    for mask in range(1 << n):
        k = mask.bit_count()
        probs[mask] = (p**k) * (q ** (n - k))
    return probs


def subset_sums(weights: Iterable[float]) -> np.ndarray:
    weights = list(weights)
    sums = np.zeros(1 << len(weights), dtype=float)
    for i, w in enumerate(weights):
        bit = 1 << i
        for mask in range(bit):
            sums[mask | bit] = sums[mask] + w
    return sums


def pivot_stats(weights: Iterable[float], p: float, a: float) -> tuple[float, float, float]:
    """Return (tail, bad, pivot_margin=tail-lambda*bad)."""
    weights = list(weights)
    sums = subset_sums(weights)
    probs = subset_probabilities(len(weights), p)
    tail = float(probs[sums >= p - 1e-12].sum())
    bad = float(probs[sums < p - a - 1e-12].sum())
    lam = p / (1.0 - p)
    return tail, bad, tail - lam * bad


def exact_pivot_stats(weights: list[Fraction], p: Fraction, a: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    n = len(weights)
    tail = Fraction(0)
    bad = Fraction(0)
    q = 1 - p
    for mask in range(1 << n):
        s = sum(weights[i] for i in range(n) if mask & (1 << i))
        k = mask.bit_count()
        prob = (p**k) * (q ** (n - k))
        if s >= p:
            tail += prob
        if s < p - a:
            bad += prob
    lam = p / (1 - p)
    return tail, bad, tail - lam * bad


def chamber_milp(p_frac: Fraction, a_frac: Fraction, n: int, *, strict_eps: float = 0.0, time_limit: float = 30.0) -> MilpResult:
    """Maximize the chamber violation over n weights.

    strict_eps=0 gives the equality-ambiguous outer relaxation.
    strict_eps>0 requires bad subsets to be <=L-eps and non-success subsets to
    be <=U-eps; this searches only chambers separated from thresholds.
    """
    p = float(p_frac)
    a = float(a_frac)
    lam = p / (1.0 - p)
    total = 1.0 - a
    lower = p - a
    upper = p
    m = 1 << n
    num_vars = n + 2 * m
    y0 = n
    z0 = n + m
    probs = subset_probabilities(n, p)
    M = 1.0

    # Objective for scipy.milp is minimization.  We minimize -V.
    c = np.zeros(num_vars, dtype=float)
    c[y0 : y0 + m] = -lam * probs
    c[z0 : z0 + m] = probs

    edge_count = n * (m // 2)
    rows = 4 * m + 2 * edge_count + m + max(0, n - 1) + 1
    A = lil_matrix((rows, num_vars), dtype=float)
    lb_cons = -np.inf * np.ones(rows, dtype=float)
    ub = np.empty(rows, dtype=float)
    row = 0
    for mask in range(m):
        bits = [i for i in range(n) if mask & (1 << i)]

        # y_mask=1 => sum_A w_i <= lower - strict_eps.
        for i in bits:
            A[row, i] = 1.0
        A[row, y0 + mask] = M
        ub[row] = lower - strict_eps + M
        row += 1

        # y_mask=0 => sum_A w_i >= lower.
        for i in bits:
            A[row, i] = -1.0
        A[row, y0 + mask] = -M
        ub[row] = -lower
        row += 1

        # z_mask=1 => sum_A w_i >= upper.
        for i in bits:
            A[row, i] = -1.0
        A[row, z0 + mask] = M
        ub[row] = M - upper
        row += 1

        # z_mask=0 => sum_A w_i <= upper - strict_eps.
        for i in bits:
            A[row, i] = 1.0
        A[row, z0 + mask] = -M
        ub[row] = upper - strict_eps
        row += 1

    for mask in range(m):
        # Bad labels form a down-set and success labels form an up-set.
        for i in range(n):
            bit = 1 << i
            if mask & bit:
                continue
            sup = mask | bit
            A[row, y0 + sup] = 1.0
            A[row, y0 + mask] = -1.0
            ub[row] = 0.0
            row += 1

            A[row, z0 + mask] = 1.0
            A[row, z0 + sup] = -1.0
            ub[row] = 0.0
            row += 1

    for mask in range(m):
        # Since p-a <= p, a subset cannot be simultaneously lower-bad and
        # upper-success.  This is redundant for the weight constraints and
        # useful for branch-and-bound.
        A[row, y0 + mask] = 1.0
        A[row, z0 + mask] = 1.0
        ub[row] = 1.0
        row += 1

    for i in range(n - 1):
        # Symmetry break: sort weights nonincreasingly.  Since the objective and
        # thresholds are invariant under coordinate permutations, some optimum
        # has this order.
        A[row, i] = -1.0
        A[row, i + 1] = 1.0
        ub[row] = 0.0
        row += 1

    for i in range(n):
        A[row, i] = 1.0
    lb_cons[row] = total
    ub[row] = total
    row += 1

    assert row == rows

    constraints = LinearConstraint(A.tocsr(), lb_cons, ub)

    lb = np.zeros(num_vars, dtype=float)
    ubounds = np.ones(num_vars, dtype=float)
    ubounds[:n] = total
    integrality = np.zeros(num_vars, dtype=int)
    integrality[n:] = 1

    res = milp(
        c,
        integrality=integrality,
        bounds=Bounds(lb, ubounds),
        constraints=constraints,
        options={
            "time_limit": time_limit,
            "mip_rel_gap": 0.0,
            "disp": False,
            "primal_feasibility_tolerance": 1e-9,
            "dual_feasibility_tolerance": 1e-9,
        },
    )
    if res.x is None:
        return MilpResult(
            p_frac,
            a_frac,
            n,
            "strict" if strict_eps else "outer",
            False,
            float("nan"),
            None,
            None,
            None,
            None,
            res.message,
            getattr(res, "mip_gap", None),
            getattr(res, "mip_dual_bound", None),
        )

    max_violation = -float(res.fun)
    weights = [float(x) for x in res.x[:n]]
    tail, bad, margin = pivot_stats(weights, p, a)
    direct_violation = -margin
    return MilpResult(
        p_frac,
        a_frac,
        n,
        "strict" if strict_eps else "outer",
        True,
        max_violation,
        direct_violation,
        tail,
        bad,
        weights,
        res.message,
        getattr(res, "mip_gap", None),
        getattr(res, "mip_dual_bound", None),
    )


def random_dirichlet_search(p_frac: Fraction, a_frac: Fraction, n: int, trials: int, seed: int) -> tuple[float, list[float], float, float]:
    rng = np.random.default_rng(seed)
    p = float(p_frac)
    a = float(a_frac)
    total = 1.0 - a
    best_margin = float("inf")
    best_weights: list[float] = []
    best_tail = best_bad = float("nan")
    alphas = [0.05, 0.1, 0.25, 0.5, 1.0, 2.0]
    for alpha in alphas:
        for _ in range(trials // len(alphas)):
            w = total * rng.dirichlet(np.full(n, alpha))
            tail, bad, margin = pivot_stats(w, p, a)
            if margin < best_margin:
                best_margin = margin
                best_weights = [float(x) for x in w]
                best_tail = tail
                best_bad = bad
    return best_margin, best_weights, best_tail, best_bad


def pivot_plus_dust(p_frac: Fraction, eps_frac: Fraction, Ns: list[int]) -> list[tuple[int, float, float, float]]:
    p = float(p_frac)
    eps = float(eps_frac)
    a = p - eps
    rows = []
    for N in Ns:
        dust = (1.0 - a) / N
        # Original a=0 inequality with one pivot of size p-eps and N equal
        # dust weights.  Conditional on the pivot variable, the dust is a
        # scaled Bin(N,p), so no subset enumeration is needed.
        k_tail_with_pivot = int(np.ceil((p - a) / dust - 1e-12))
        k_tail_without_pivot = int(np.ceil(p / dust - 1e-12))
        k_bad_with_pivot = int(np.ceil((p - a) / dust - 1e-12)) - 1
        k_bad_without_pivot = int(np.ceil(p / dust - 1e-12)) - 1
        tail = p * binom.sf(k_tail_with_pivot - 1, N, p) + (1.0 - p) * binom.sf(k_tail_without_pivot - 1, N, p)
        bad = p * binom.cdf(k_bad_with_pivot, N, p) + (1.0 - p) * binom.cdf(k_bad_without_pivot, N, p)
        margin = tail - (p / (1.0 - p)) * bad
        rows.append((N, tail, bad, margin))
    return rows


def exact_small_examples() -> list[str]:
    lines: list[str] = []
    p = Fraction(3, 10)
    alpha = Fraction(1, 10)
    beta = Fraction(1, 10)
    w = [1 - alpha - beta]
    # False coefficient-1 two-threshold comparison:
    # P[Y >= p-beta] >= P[Y < p-alpha].
    tail = p
    low = 1 - p
    lines.append(
        "Coefficient-1 two-threshold invariant fails exactly: "
        f"p={p}, alpha=beta={alpha}, one remaining weight={w[0]}, "
        f"P[Y >= p-beta]={tail}, P[Y < p-alpha]={low}."
    )
    for a in [Fraction(0), Fraction(1, 10), Fraction(1, 5), Fraction(3, 10)]:
        total = 1 - a
        tail, bad, margin = exact_pivot_stats([total], p, a)
        lines.append(
            f"One-weight pivot check p={p}, a={a}, weight={total}: "
            f"tail={tail}, bad={bad}, margin={margin}."
        )
    return lines


def run() -> None:
    out = Path("data/round4_pivot_search_output.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = []
    def add(line: str = "") -> None:
        lines.append(line)
        out.write_text("\n".join(lines) + "\n")
        print(line, flush=True)

    add("# Round 4 pivot search output")
    add("")
    add("## Exact induction obstruction examples")
    for line in exact_small_examples():
        add(line)

    add("")
    add("## Pivot plus dust approaching equality for original a=0 inequality")
    for p_frac, eps_frac in [(Fraction(3, 10), Fraction(1, 100)), (Fraction(1, 3), Fraction(1, 100))]:
        add(f"p={p_frac}, pivot weight p-eps={p_frac - eps_frac}, eps={eps_frac}")
        for N, tail, bad, margin in pivot_plus_dust(p_frac, eps_frac, [20, 50, 100, 200, 500, 1000]):
            add(f"  N={N:4d} tail={tail:.12f} tail-p={tail-float(p_frac):+.6e} margin={margin:.12f}")

    add("")
    add("## Random Dirichlet search for pivot functional")
    for p_frac in [Fraction(1, 6), Fraction(1, 5), Fraction(1, 4), Fraction(3, 10), Fraction(1, 3)]:
        for mult in [Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)]:
            a_frac = p_frac * mult
            margin, weights, tail, bad = random_dirichlet_search(p_frac, a_frac, 8, trials=2000, seed=1000 + p_frac.numerator * 97 + p_frac.denominator * 13 + mult.numerator * 7)
            add(
                f"p={str(p_frac):>5}, a={str(a_frac):>5}, n=8 random: "
                f"best_margin={margin:.12e}, tail={tail:.12f}, bad={bad:.12f}, "
                f"weights={np.round(weights, 6).tolist()}"
            )

    add("")
    add("## MILP chamber/separation search, n=7 (contains supports <=7 by zero weights)")
    grid: list[tuple[Fraction, Fraction]] = []
    for p_frac in [Fraction(1, 6), Fraction(1, 5), Fraction(1, 4), Fraction(2, 7), Fraction(3, 10), Fraction(1, 3)]:
        for mult in [Fraction(0), Fraction(1, 2), Fraction(3, 4)]:
            grid.append((p_frac, p_frac * mult))

    for p_frac, a_frac in grid:
        outer = chamber_milp(p_frac, a_frac, 7, strict_eps=0.0, time_limit=15.0)
        strict = chamber_milp(p_frac, a_frac, 7, strict_eps=1e-5, time_limit=15.0)
        for res in [outer, strict]:
            if res.weights is not None:
                add(
                    f"{res.kind:6s} p={res.p}, a={res.a}, n={res.n}: "
                    f"maxV={res.max_violation:.12e}, directV={res.direct_violation:.12e}, "
                    f"tail={res.tail:.12f}, bad={res.bad:.12f}, "
                    f"gap={res.mip_gap}, status={'optimal' if res.success and 'Optimal' in res.message else 'incumbent'}, "
                    f"weights={np.round(res.weights, 8).tolist()}"
                )
            else:
                add(f"{res.kind:6s} p={res.p}, a={res.a}, n={res.n}: solver failed: {res.message}")

    add("")
    add("## Selected n=8 strict MILP incumbent/optimal checks")
    grid8 = [
        (Fraction(1, 6), Fraction(1, 12)),
        (Fraction(1, 4), Fraction(1, 8)),
        (Fraction(2, 7), Fraction(1, 7)),
        (Fraction(3, 10), Fraction(0)),
        (Fraction(3, 10), Fraction(3, 20)),
        (Fraction(1, 3), Fraction(0)),
        (Fraction(1, 3), Fraction(1, 6)),
    ]
    for p_frac, a_frac in grid8:
        res = chamber_milp(p_frac, a_frac, 8, strict_eps=1e-5, time_limit=20.0)
        if res.weights is not None:
            add(
                f"{res.kind:6s} p={res.p}, a={res.a}, n={res.n}: "
                f"maxV={res.max_violation:.12e}, directV={res.direct_violation:.12e}, "
                f"tail={res.tail:.12f}, bad={res.bad:.12f}, "
                f"gap={res.mip_gap}, status={'optimal' if res.success and 'Optimal' in res.message else 'incumbent'}, "
                f"weights={np.round(res.weights, 8).tolist()}"
            )
        else:
            add(f"{res.kind:6s} p={res.p}, a={res.a}, n={res.n}: solver failed: {res.message}")

    print(f"wrote {out}")


if __name__ == "__main__":
    run()
