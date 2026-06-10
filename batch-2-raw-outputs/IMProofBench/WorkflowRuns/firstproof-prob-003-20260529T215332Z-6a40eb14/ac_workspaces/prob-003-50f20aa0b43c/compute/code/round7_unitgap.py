#!/usr/bin/env python3
"""Round 7 computations for the unit-gap formulation.

Target, for 0<p<=1/3 and 0<=b_i<=1:

    P[S >= p(B+1)] >= (p/q) P[S < p(B+1)-1],
    S=sum b_i zeta_i, B=sum b_i, zeta_i iid Bernoulli(p).

This script runs:
  * direct/random and differential-evolution searches for positive violation;
  * exact chamber MILPs for small n and rational p;
  * a finite-grid Bellman LP showing that a one-function subharmonic minorant
    certificate appears too weak/negative.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from math import ceil
from pathlib import Path

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, differential_evolution, linprog, milp
from scipy.sparse import lil_matrix


def subset_probabilities(n: int, p: float) -> np.ndarray:
    probs = np.empty(1 << n, dtype=float)
    q = 1.0 - p
    for mask in range(1 << n):
        k = mask.bit_count()
        probs[mask] = (p**k) * (q ** (n - k))
    return probs


def subset_sums(weights: np.ndarray) -> np.ndarray:
    sums = np.zeros(1 << len(weights), dtype=float)
    for i, w in enumerate(weights):
        bit = 1 << i
        sums[bit : 2 * bit] = sums[:bit] + w
    return sums


def unitgap_stats(weights: np.ndarray, p: float, tol: float = 1e-12) -> tuple[float, float, float]:
    """Return (good, bad, margin=good-(p/q)bad)."""
    weights = np.asarray(weights, dtype=float)
    B = float(weights.sum())
    t = p * (B + 1.0)
    sums = subset_sums(weights)
    probs = subset_probabilities(len(weights), p)
    good = float(probs[sums >= t - tol].sum())
    bad = float(probs[sums < t - 1.0 - tol].sum())
    return good, bad, good - (p / (1.0 - p)) * bad


def softbox(y: np.ndarray) -> np.ndarray:
    """Map unconstrained coordinates to (0,1)."""
    return 1.0 / (1.0 + np.exp(-np.clip(y, -40.0, 40.0)))


@dataclass
class SearchResult:
    p: float
    n: int
    method: str
    violation: float
    good: float
    bad: float
    B: float
    weights: list[float]
    note: str = ""


def de_search(p: float, n: int, seed: int, *, require_bad_possible: bool) -> SearchResult:
    q = 1.0 - p
    min_B = q / p + 1e-5 if require_bad_possible else 0.0

    def objective(y: np.ndarray) -> float:
        b = softbox(y)
        good, bad, margin = unitgap_stats(b, p)
        violation = -margin
        penalty = 0.0
        if b.sum() < min_B:
            penalty += 100.0 * (min_B - b.sum()) + 1000.0 * (min_B - b.sum()) ** 2
        return -violation + penalty

    res = differential_evolution(
        objective,
        [(-12.0, 12.0)] * n,
        seed=seed,
        maxiter=180,
        popsize=8,
        polish=False,
        tol=1e-8,
        workers=1,
        updating="immediate",
    )
    b = softbox(res.x)
    good, bad, margin = unitgap_stats(b, p)
    return SearchResult(
        p,
        n,
        "DE B>q/p" if require_bad_possible else "DE",
        -margin,
        good,
        bad,
        float(b.sum()),
        sorted(map(float, b), reverse=True),
    )


def random_search(p: float, n: int, seed: int, trials: int, *, require_bad_possible: bool) -> SearchResult | None:
    q = 1.0 - p
    min_B = q / p if require_bad_possible else 0.0
    rng = np.random.default_rng(seed)
    best: SearchResult | None = None
    beta_params = [(0.2, 0.2), (0.4, 0.8), (0.8, 0.4), (1.0, 1.0), (2.0, 1.0)]
    for a, bpar in beta_params:
        for _ in range(trials // len(beta_params)):
            w = rng.beta(a, bpar, size=n)
            if require_bad_possible and w.sum() <= min_B:
                # Lift uniformly toward one, preserving the sampled shape.
                if n <= min_B:
                    continue
                theta = (min_B + 1e-4 - w.sum()) / (n - w.sum())
                if theta > 0:
                    w = w + theta * (1.0 - w)
            good, bad, margin = unitgap_stats(w, p)
            cand = SearchResult(
                p,
                n,
                "random B>q/p" if require_bad_possible else "random",
                -margin,
                good,
                bad,
                float(w.sum()),
                sorted(map(float, w), reverse=True),
            )
            if best is None or cand.violation > best.violation:
                best = cand
    return best


@dataclass
class MilpResult:
    p: Fraction
    n: int
    kind: str
    success: bool
    max_violation: float
    direct_violation: float | None
    good: float | None
    bad: float | None
    B: float | None
    weights: list[float] | None
    message: str
    mip_gap: float | None = None


def unitgap_chamber_milp(
    p_frac: Fraction,
    n: int,
    *,
    strict_eps: float = 0.0,
    require_bad_possible: bool = False,
    time_limit: float = 30.0,
) -> MilpResult:
    """Outer/strict chamber MILP for the unit-gap violation."""
    p = float(p_frac)
    q = 1.0 - p
    lam = p / q
    m = 1 << n
    num_vars = n + 2 * m
    y0 = n
    z0 = n + m
    probs = subset_probabilities(n, p)
    M = n + 2.0

    c = np.zeros(num_vars, dtype=float)
    c[y0 : y0 + m] = -lam * probs   # maximize +lambda*bad
    c[z0 : z0 + m] = probs          # maximize -good

    edge_count = n * (m // 2)
    extra_B = 1 if require_bad_possible else 0
    rows = 4 * m + 2 * edge_count + m + max(0, n - 1) + extra_B
    A = lil_matrix((rows, num_vars), dtype=float)
    lb_cons = -np.inf * np.ones(rows, dtype=float)
    ub = np.empty(rows, dtype=float)
    row = 0

    for mask in range(m):
        # L_A = sum_{i in A} b_i - p(B+1)
        coeff = np.full(n, -p, dtype=float)
        for i in range(n):
            if mask & (1 << i):
                coeff[i] += 1.0

        # Here coeff @ b = sum_{i in A} b_i - p B, while
        # L_A = coeff @ b - p = sum_{i in A} b_i - p(B+1).

        # y=1 (lower bad) => L_A <= -1 - eps.
        for i in range(n):
            A[row, i] = coeff[i]
        A[row, y0 + mask] = M
        ub[row] = M + p - 1.0 - strict_eps
        row += 1

        # y=0 => L_A >= -1.
        for i in range(n):
            A[row, i] = -coeff[i]
        A[row, y0 + mask] = -M
        ub[row] = 1.0 - p
        row += 1

        # z=1 (upper good) => L_A >= 0.
        for i in range(n):
            A[row, i] = -coeff[i]
        A[row, z0 + mask] = M
        ub[row] = M - p
        row += 1

        # z=0 => L_A <= -eps.
        for i in range(n):
            A[row, i] = coeff[i]
        A[row, z0 + mask] = -M
        ub[row] = p - strict_eps
        row += 1

    for mask in range(m):
        for i in range(n):
            bit = 1 << i
            if mask & bit:
                continue
            sup = mask | bit
            # Bad labels form a down-set.
            A[row, y0 + sup] = 1.0
            A[row, y0 + mask] = -1.0
            ub[row] = 0.0
            row += 1
            # Good labels form an up-set.
            A[row, z0 + mask] = 1.0
            A[row, z0 + sup] = -1.0
            ub[row] = 0.0
            row += 1

    for mask in range(m):
        # A subset cannot be both lower-bad and upper-good.
        A[row, y0 + mask] = 1.0
        A[row, z0 + mask] = 1.0
        ub[row] = 1.0
        row += 1

    for i in range(n - 1):
        A[row, i] = -1.0
        A[row, i + 1] = 1.0
        ub[row] = 0.0
        row += 1

    if require_bad_possible:
        for i in range(n):
            A[row, i] = -1.0
        ub[row] = -(q / p + strict_eps)
        row += 1

    assert row == rows
    constraints = LinearConstraint(A.tocsr(), lb_cons, ub)
    lb = np.zeros(num_vars, dtype=float)
    ubounds = np.ones(num_vars, dtype=float)
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
    kind = ("strict" if strict_eps else "outer") + (" B>q/p" if require_bad_possible else "")
    if res.x is None:
        return MilpResult(p_frac, n, kind, False, float("nan"), None, None, None, None, None, res.message, getattr(res, "mip_gap", None))
    weights = [float(x) for x in res.x[:n]]
    good, bad, margin = unitgap_stats(np.array(weights), p)
    return MilpResult(
        p_frac,
        n,
        kind,
        True,
        -float(res.fun),
        -margin,
        good,
        bad,
        float(sum(weights)),
        weights,
        res.message,
        getattr(res, "mip_gap", None),
    )


def bellman_minorant_lp(p: float, *, h: float = 0.02, r_min: float = -1.0, r_max: float = 2.0) -> tuple[float, np.ndarray, np.ndarray]:
    """Finite-grid LP for a one-function subharmonic minorant of g.

    Maximize phi(p) subject to phi<=g and
        phi(r) <= q phi(r+pb) + p phi(r-qb)
    on a grid of r and b values.  Linear interpolation is used for off-grid
    successor states.  Boundary values outside the grid are capped by g.
    This is only a diagnostic obstruction, not a proof of nonexistence.
    """
    q = 1.0 - p
    xs = np.arange(r_min, r_max + h / 2, h)
    n = len(xs)

    def g(x: float) -> float:
        if x <= 0:
            return 1.0
        if x > 1:
            return -p / q
        return 0.0

    def interp_coeff(x: float) -> tuple[list[int], list[float], float]:
        """Return grid coefficients and constant cap contribution for phi(x)."""
        if x <= r_min:
            return [], [], g(x)
        if x >= r_max:
            return [], [], g(x)
        j = int(np.floor((x - r_min) / h))
        if j >= n - 1:
            return [n - 1], [1.0], 0.0
        x0 = xs[j]
        a = (x - x0) / h
        return [j, j + 1], [1.0 - a, a], 0.0

    rows = []
    rhs = []

    # phi_i <= g(x_i)
    for i, x in enumerate(xs):
        row = np.zeros(n)
        row[i] = 1.0
        rows.append(row)
        rhs.append(g(float(x)))

    b_grid = np.arange(0.0, 1.0 + 1e-12, h)
    for i, r in enumerate(xs):
        for b in b_grid:
            row = np.zeros(n)
            row[i] = 1.0
            const = 0.0
            idxs, vals, cap = interp_coeff(float(r + p * b))
            const += q * cap
            for j, val in zip(idxs, vals):
                row[j] -= q * val
            idxs, vals, cap = interp_coeff(float(r - q * b))
            const += p * cap
            for j, val in zip(idxs, vals):
                row[j] -= p * val
            rows.append(row)
            rhs.append(const)

    c = np.zeros(n)
    p_index = int(round((p - r_min) / h))
    c[p_index] = -1.0
    res = linprog(c, A_ub=np.vstack(rows), b_ub=np.array(rhs), bounds=[(-10, 10)] * n, method="highs")
    if not res.success:
        raise RuntimeError(res.message)
    return -float(res.fun), xs, res.x


def format_weights(weights: list[float], k: int = 10) -> str:
    return "[" + ", ".join(f"{x:.6g}" for x in weights[:k]) + (", ..." if len(weights) > k else "") + "]"


def main() -> None:
    out = Path("data/round7_unitgap_output.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = []

    def add(s: str = "") -> None:
        lines.append(s)
        out.write_text("\n".join(lines) + "\n")
        print(s, flush=True)

    add("# Round 7 unit-gap computations")
    add("")
    add("## Direct searches for positive violation V=(p/q)bad-good")
    p_grid = [Fraction(1, 6), Fraction(1, 5), Fraction(1, 4), Fraction(2, 7), Fraction(3, 10), Fraction(1, 3)]
    for pf in p_grid:
        p = float(pf)
        min_n = max(1, ceil((1 - p) / p))
        add(f"p={pf} (q/p={(1-p)/p:.6g})")
        for n in sorted(set([min_n, min_n + 1, min_n + 2, 6, 8, 10, 12])):
            if n <= 0:
                continue
            if n <= 14:
                de = de_search(p, n, seed=700000 + 1000 * n + int(100000 * p), require_bad_possible=True)
                add(
                    f"  n={n:2d} DE B>q/p: V={de.violation:+.12e} good={de.good:.12f} "
                    f"bad={de.bad:.12f} B={de.B:.6f} b={format_weights(de.weights, 8)}"
                )
            rnd = random_search(p, n, seed=710000 + 1000 * n + int(100000 * p), trials=4000, require_bad_possible=True)
            if rnd is not None:
                add(
                    f"  n={n:2d} random:   V={rnd.violation:+.12e} good={rnd.good:.12f} "
                    f"bad={rnd.bad:.12f} B={rnd.B:.6f} b={format_weights(rnd.weights, 8)}"
                )
        add("")

    add("## Exact chamber MILP probes")
    for pf in p_grid:
        p = float(pf)
        min_n = ceil((1 - p) / p)
        for n in sorted(set([min_n, min_n + 1, min_n + 2, 6, 7, 8])):
            if n > 8 or n <= 0 or n < min_n:
                continue
            for strict_eps, tlim in [(0.0, 12.0), (1e-5, 12.0)]:
                res = unitgap_chamber_milp(pf, n, strict_eps=strict_eps, require_bad_possible=True, time_limit=tlim)
                if not res.success:
                    add(f"{res.kind} p={pf} n={n}: solver failed: {res.message}")
                    continue
                add(
                    f"{res.kind:15s} p={str(pf):>4} n={n}: maxV={res.max_violation:+.12e} "
                    f"directV={res.direct_violation:+.12e} good={res.good:.12f} bad={res.bad:.12f} "
                    f"B={res.B:.8f} gap={res.mip_gap} b={format_weights(sorted(res.weights, reverse=True), 8)}"
                )
        add("")

    add("## One-function Bellman minorant diagnostic")
    for p in [0.2, 0.25, 0.3, 1 / 3]:
        val, xs, phi = bellman_minorant_lp(p, h=0.025, r_min=-1.0, r_max=2.0)
        add(f"p={p:.12f}: grid max phi(p)={val:+.9f}; phi(0)={phi[np.argmin(abs(xs-0))]:+.9f}, phi(1)={phi[np.argmin(abs(xs-1))]:+.9f}")

    add("")
    add(f"Wrote {out}")


if __name__ == "__main__":
    main()
