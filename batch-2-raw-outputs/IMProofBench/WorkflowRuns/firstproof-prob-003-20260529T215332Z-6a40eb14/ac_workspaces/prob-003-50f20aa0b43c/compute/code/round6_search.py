#!/usr/bin/env python3
"""Round 6 direct searches for the small-p Bernoulli weighted-tail lemma.

The target is

    P[sum_i w_i X_i >= p] >= p,  X_i iid Bernoulli(p),  sum_i w_i=1.

Any counterexample must have max_i w_i < p, so this script combines:

* unconstrained differential-evolution minimization over the simplex;
* hit-and-run sampling in the capped simplex max_i w_i <= p-eps;
* a structured "pivot plus dust" family approaching equality from above;
* strict chamber MILP checks for a=0 using the round-4 pivot MILP, where the
  pivot inequality is algebraically equivalent to the original inequality.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import ceil
from pathlib import Path

import numpy as np
from scipy.optimize import differential_evolution
from scipy.stats import binom

from round4_pivot_search import chamber_milp


@dataclass
class SearchRow:
    p: float
    n: int
    method: str
    best_tail: float
    gap: float
    weights: list[float]
    samples: int | None = None


def subset_sums(weights: np.ndarray) -> np.ndarray:
    sums = np.zeros(1 << len(weights), dtype=float)
    for i, w in enumerate(weights):
        bit = 1 << i
        sums[bit : 2 * bit] = sums[:bit] + w
    return sums


def subset_probabilities(n: int, p: float) -> np.ndarray:
    probs = np.empty(1 << n, dtype=float)
    q = 1.0 - p
    for mask in range(1 << n):
        k = mask.bit_count()
        probs[mask] = (p**k) * (q ** (n - k))
    return probs


def tail_prob(weights: np.ndarray, p: float) -> float:
    sums = subset_sums(np.asarray(weights, dtype=float))
    probs = subset_probabilities(len(weights), p)
    return float(probs[sums >= p - 1e-12].sum())


def softmax(y: np.ndarray) -> np.ndarray:
    y = np.asarray(y, dtype=float)
    y = y - y.max()
    e = np.exp(y)
    return e / e.sum()


def de_search(p: float, n: int, seed: int, *, hard_cap: bool) -> SearchRow:
    cap_slack = min(1e-4, p / 1000.0)
    cap = p - cap_slack

    def objective(y: np.ndarray) -> float:
        w = softmax(y)
        val = tail_prob(w, p)
        if hard_cap:
            over = max(0.0, float(w.max()) - cap)
            # Large enough to push the optimizer into the nontrivial capped
            # region, without dwarfing differences once feasible.
            val += 100.0 * over + 1000.0 * over * over
        return val

    res = differential_evolution(
        objective,
        [(-10.0, 10.0)] * n,
        seed=seed,
        maxiter=180,
        popsize=7,
        polish=False,
        tol=1e-7,
        workers=1,
        updating="immediate",
    )
    w = softmax(res.x)
    tail = tail_prob(w, p)
    return SearchRow(p, n, "DE capped" if hard_cap else "DE", tail, tail - p, sorted(map(float, w), reverse=True))


def capped_hit_and_run(
    p: float,
    n: int,
    seed: int,
    *,
    steps: int = 6000,
    restarts: int = 8,
) -> SearchRow | None:
    """Search in {w>=0, sum w=1, w_i <= p-eps} by hit-and-run.

    This is not intended to sample perfectly.  It is a cheap way to probe the
    actual possible counterexample region, especially near the cap boundary.
    """

    eps = min(1e-4, p / 1000.0)
    cap = p - eps
    if n * cap <= 1.0:
        return None
    rng = np.random.default_rng(seed)
    best_tail = float("inf")
    best_w: np.ndarray | None = None
    samples = 0

    for _ in range(restarts):
        # Equal weights are feasible whenever n*cap>1 and are a stable start.
        w = np.full(n, 1.0 / n)
        # Add a short randomized warmup.
        for step in range(steps):
            d = rng.normal(size=n)
            d -= d.mean()
            if np.linalg.norm(d) < 1e-14:
                continue

            lo = -float("inf")
            hi = float("inf")
            pos = d > 1e-14
            neg = d < -1e-14
            if np.any(pos):
                lo = max(lo, float(np.max(-w[pos] / d[pos])))
                hi = min(hi, float(np.min((cap - w[pos]) / d[pos])))
            if np.any(neg):
                lo = max(lo, float(np.max((cap - w[neg]) / d[neg])))
                hi = min(hi, float(np.min(-w[neg] / d[neg])))
            if not np.isfinite(lo) or not np.isfinite(hi) or lo > hi:
                continue
            t = rng.uniform(lo, hi)
            w = w + t * d
            w = np.clip(w, 0.0, cap)
            w = w / w.sum()

            if step % 5 == 0:
                tail = tail_prob(w, p)
                samples += 1
                if tail < best_tail:
                    best_tail = tail
                    best_w = w.copy()

    if best_w is None:
        return None
    return SearchRow(p, n, "capped hit-run", best_tail, best_tail - p, sorted(map(float, best_w), reverse=True), samples)


def pivot_plus_dust_tail(p: float, eps: float, n_dust: int) -> float:
    """One weight p-eps plus n equal dust weights summing 1-p+eps."""

    pivot = p - eps
    dust_total = 1.0 - pivot
    dust = dust_total / n_dust
    # With pivot selected, need at least eps dust; otherwise need at least p.
    k_with = ceil((p - pivot - 1e-13) / dust)
    k_without = ceil((p - 1e-13) / dust)
    return float(
        p * binom.sf(k_with - 1, n_dust, p)
        + (1.0 - p) * binom.sf(k_without - 1, n_dust, p)
    )


def run() -> None:
    out = Path("data/round6_search_output.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    csv = Path("data/round6_random_search.csv")
    rows: list[SearchRow] = []
    lines: list[str] = []

    def add(line: str = "") -> None:
        lines.append(line)
        out.write_text("\n".join(lines) + "\n")
        print(line, flush=True)

    add("# Round 6 search for small-p weighted Bernoulli lemma")
    add("")

    p_grid = [1 / 6, 0.20, 0.25, 2 / 7, 0.30, 1 / 3]
    add("## Differential-evolution searches")
    for p in p_grid:
        add(f"p={p:.12f}")
        for n in [3, 4, 5, 6, 7, 8, 10, 12]:
            row = de_search(p, n, seed=20260530 + 1000 * n + int(round(100000 * p)), hard_cap=False)
            rows.append(row)
            add(f"  n={n:2d} DE        tail={row.best_tail:.12f} gap={row.gap:+.6e} w={np.round(row.weights[:8], 7).tolist()}")
            if n * (p - min(1e-4, p / 1000.0)) > 1.0:
                row = de_search(p, n, seed=20261530 + 1000 * n + int(round(100000 * p)), hard_cap=True)
                rows.append(row)
                add(f"  n={n:2d} DE capped tail={row.best_tail:.12f} gap={row.gap:+.6e} w={np.round(row.weights[:8], 7).tolist()}")

    add("")
    add("## Capped-simplex hit-and-run searches (max w_i < p)")
    for p in p_grid:
        for n in [ceil(1 / p) + 1, ceil(1 / p) + 2, 10, 12, 14]:
            if n < 2:
                continue
            row = capped_hit_and_run(p, n, seed=30360530 + 1000 * n + int(round(100000 * p)))
            if row is None:
                continue
            rows.append(row)
            add(
                f"p={p:.12f} n={n:2d} samples={row.samples:5d} "
                f"tail={row.best_tail:.12f} gap={row.gap:+.6e} "
                f"maxw={max(row.weights):.8f} w={np.round(row.weights[:10], 7).tolist()}"
            )

    add("")
    add("## Structured pivot-plus-dust family")
    for p in [0.20, 0.25, 0.30, 1 / 3]:
        eps = min(1e-3, p / 100.0)
        add(f"p={p:.12f}, pivot=p-eps={p - eps:.12f}, eps={eps:.3e}")
        for n_dust in [20, 50, 100, 200, 500, 1000, 2000]:
            tail = pivot_plus_dust_tail(p, eps, n_dust)
            add(f"  dust={n_dust:4d} tail={tail:.12f} gap={tail-p:+.6e}")

    add("")
    add("## Strict chamber MILP checks for original inequality (a=0)")
    for p_frac in [Fraction(1, 6), Fraction(1, 5), Fraction(1, 4), Fraction(2, 7), Fraction(3, 10), Fraction(1, 3)]:
        for n, tlim in [(8, 10.0), (9, 12.0)]:
            res = chamber_milp(p_frac, Fraction(0), n, strict_eps=1e-5, time_limit=tlim)
            if res.weights is None:
                add(f"strict p={p_frac} n={n}: solver failed: {res.message}")
                continue
            add(
                f"strict p={p_frac} n={n}: maxV={res.max_violation:.12e} "
                f"directV={res.direct_violation:.12e} tail={res.tail:.12f} "
                f"gap_tail={res.tail-float(p_frac):+.6e} mip_gap={res.mip_gap} "
                f"weights={np.round(res.weights, 8).tolist()}"
            )

    with csv.open("w") as f:
        f.write("p,n,method,best_tail,gap,samples,weights_desc\n")
        for row in rows:
            weights = " ".join(f"{x:.12g}" for x in row.weights)
            f.write(f"{row.p:.12g},{row.n},{row.method},{row.best_tail:.15g},{row.gap:.15g},{row.samples or ''},\"{weights}\"\n")
    add("")
    add(f"Wrote CSV summary to {csv}")


if __name__ == "__main__":
    run()
