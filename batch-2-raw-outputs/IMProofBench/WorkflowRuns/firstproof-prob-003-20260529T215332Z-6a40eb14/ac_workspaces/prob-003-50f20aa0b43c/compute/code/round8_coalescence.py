#!/usr/bin/env python3
"""Round 8 experiments for the q-complement coalescence assertion.

The main object is

    Phi_q(w) = P_q(sum_i w_i eta_i > q),        q = 1 - p,

and Delta_ij = Phi_q(coalesce i,j) - Phi_q(w).  All exact computations below
use Fraction arithmetic.  The fast floating routines are only used to guide
search; candidates are re-evaluated exactly when rational.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
import json
import math
import random
from pathlib import Path

import numpy as np
from scipy.optimize import differential_evolution


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def subset_distribution(weights: tuple[Fraction, ...], prob: Fraction) -> dict[Fraction, Fraction]:
    """Distribution of sum_{i in R} weights[i], where each i is kept with prob."""

    dist: dict[Fraction, Fraction] = {Fraction(0): Fraction(1)}
    no = 1 - prob
    for w in weights:
        nxt: dict[Fraction, Fraction] = defaultdict(Fraction)
        for s, pr in dist.items():
            nxt[s] += pr * no
            nxt[s + w] += pr * prob
        dist = dict(nxt)
    return dist


def phi_exact(weights: tuple[Fraction, ...], q: Fraction) -> Fraction:
    dist = subset_distribution(weights, q)
    return sum(pr for s, pr in dist.items() if s > q)


def coalesced(weights: tuple[Fraction, ...], i: int, j: int) -> tuple[Fraction, ...]:
    return tuple(weights[k] for k in range(len(weights)) if k not in (i, j)) + (weights[i] + weights[j],)


def delta_exact_by_phi(weights: tuple[Fraction, ...], q: Fraction, i: int, j: int) -> Fraction:
    return phi_exact(coalesced(weights, i, j), q) - phi_exact(weights, q)


def delta_exact_interval(weights: tuple[Fraction, ...], q: Fraction, i: int, j: int) -> Fraction:
    """Exact Delta using the interval formula.

    If x <= y are the two pair weights and F is the p-biased failed weight of
    all other coordinates, then

        Delta/(pq) = P(p-x <= F < p) - P(p-x-y <= F < p-y).

    This endpoint convention is exactly equivalent to Phi_q = P(active > q),
    i.e. P(failed < p).
    """

    p = 1 - q
    x, y = weights[i], weights[j]
    if x > y:
        x, y = y, x
    others = tuple(weights[k] for k in range(len(weights)) if k not in (i, j))
    dist = subset_distribution(others, p)
    upper = sum(pr for s, pr in dist.items() if p - x <= s < p)
    lower = sum(pr for s, pr in dist.items() if p - x - y <= s < p - y)
    return p * q * (upper - lower)


def all_deltas_exact(weights: tuple[Fraction, ...], q: Fraction) -> dict[tuple[int, int], Fraction]:
    return {
        (i, j): delta_exact_interval(weights, q, i, j)
        for i, j in combinations(range(len(weights)), 2)
    }


def aggregate_sums(
    weights: tuple[Fraction, ...], deltas: dict[tuple[int, int], Fraction]
) -> dict[str, Fraction]:
    sums = {
        "unit": Fraction(0),
        "wiwj": Fraction(0),
        "wi_plus_wj": Fraction(0),
        "min": Fraction(0),
        "max": Fraction(0),
        "gap_to_cap": Fraction(0),
    }
    cap = max(weights)  # only a scale-free diagnostic, not necessarily p.
    for (i, j), d in deltas.items():
        wi, wj = weights[i], weights[j]
        sums["unit"] += d
        sums["wiwj"] += wi * wj * d
        sums["wi_plus_wj"] += (wi + wj) * d
        sums["min"] += min(wi, wj) * d
        sums["max"] += max(wi, wj) * d
        sums["gap_to_cap"] += (cap - max(wi, wj)) * d
    return sums


def random_capped_fraction_vector(n: int, p: Fraction, denom: int, rng: random.Random) -> tuple[Fraction, ...] | None:
    """Random integer composition of denom with each part <= p*denom."""

    cap = int(p * denom)
    if cap * n < denom:
        return None
    parts = [0] * n
    remaining = denom
    for i in range(n):
        left = n - i - 1
        lo = max(0, remaining - left * cap)
        hi = min(cap, remaining)
        if lo > hi:
            return None
        # Bias toward non-boundary points, but keep occasional extremes.
        if rng.random() < 0.25:
            v = rng.randint(lo, hi)
        else:
            center = remaining / (left + 1)
            sd = max(1.0, (hi - lo + 1) / 5.0)
            v = int(round(rng.gauss(center, sd)))
            v = max(lo, min(hi, v))
        parts[i] = v
        remaining -= v
    rng.shuffle(parts)
    if any(v > cap for v in parts) or sum(parts) != denom:
        return None
    # Avoid zero-heavy vectors unless forced.
    return tuple(Fraction(v, denom) for v in parts if v)


def exact_random_search(
    q_values: list[Fraction],
    n_values: list[int],
    denoms: list[int],
    trials_per_cell: int,
    seed: int = 20260530,
) -> list[dict[str, object]]:
    rng = random.Random(seed)
    records: list[dict[str, object]] = []
    for q in q_values:
        p = 1 - q
        for n in n_values:
            if n * p < 1:
                continue
            for denom in denoms:
                if (p * denom).denominator != 1:
                    continue
                best_max: Fraction | None = None
                best_min: Fraction | None = None
                best_vec: tuple[Fraction, ...] | None = None
                best_aggs: dict[str, Fraction] | None = None
                counterexample = None
                tested = 0
                neg_agg_counts = defaultdict(int)
                for _ in range(trials_per_cell):
                    w = random_capped_fraction_vector(n, p, denom, rng)
                    if not w or len(w) < 2:
                        continue
                    tested += 1
                    deltas = all_deltas_exact(w, q)
                    max_d = max(deltas.values())
                    min_d = min(deltas.values())
                    aggs = aggregate_sums(w, deltas)
                    for name, val in aggs.items():
                        if val < 0:
                            neg_agg_counts[name] += 1
                    if best_max is None or max_d < best_max:
                        best_max = max_d
                        best_min = min_d
                        best_vec = w
                        best_aggs = aggs
                    if max_d < 0:
                        counterexample = (w, deltas, aggs)
                        break
                records.append(
                    {
                        "q": str(q),
                        "p": str(p),
                        "n": n,
                        "denom": denom,
                        "tested": tested,
                        "best_max_delta": str(best_max) if best_max is not None else None,
                        "best_max_delta_float": float(best_max) if best_max is not None else None,
                        "best_min_delta": str(best_min) if best_min is not None else None,
                        "best_vector": [str(x) for x in best_vec] if best_vec else None,
                        "best_aggregates": {k: str(v) for k, v in (best_aggs or {}).items()},
                        "negative_aggregate_counts": dict(neg_agg_counts),
                        "counterexample": None
                        if counterexample is None
                        else {
                            "vector": [str(x) for x in counterexample[0]],
                            "deltas": {str(k): str(v) for k, v in counterexample[1].items()},
                            "aggregates": {k: str(v) for k, v in counterexample[2].items()},
                        },
                    }
                )
    return records


def normalize_capped_from_logits(z: np.ndarray, p: float) -> np.ndarray:
    """Map unconstrained z to sum-one vector with entries <= p.

    This is not onto with great conditioning, but it is adequate for heuristic
    differential evolution.
    """

    a = np.exp(z - np.max(z))
    a = a / a.sum()
    # Iterative projection onto capped simplex.
    w = a.copy()
    fixed = np.zeros_like(w, dtype=bool)
    remaining_mass = 1.0
    for _ in range(len(w) + 1):
        over = (~fixed) & (w > p)
        if not np.any(over):
            break
        fixed |= over
        w[over] = p
        remaining_mass = 1.0 - w[fixed].sum()
        free = ~fixed
        if np.any(free):
            base = a[free]
            w[free] = remaining_mass * base / base.sum()
    return w


def subset_sums_probs_float(weights: np.ndarray, prob: float) -> tuple[np.ndarray, np.ndarray]:
    sums = np.array([0.0])
    probs = np.array([1.0])
    for w in weights:
        sums = np.concatenate([sums, sums + w])
        probs = np.concatenate([probs * (1 - prob), probs * prob])
    return sums, probs


def all_deltas_float(weights: np.ndarray, q: float, tol: float = 1e-12) -> np.ndarray:
    p = 1 - q
    n = len(weights)
    ds = []
    for i, j in combinations(range(n), 2):
        x, y = sorted((weights[i], weights[j]))
        others = np.array([weights[k] for k in range(n) if k not in (i, j)])
        sums, probs = subset_sums_probs_float(others, p)
        upper = probs[(p - x - tol <= sums) & (sums < p - tol)].sum()
        lower = probs[(p - x - y - tol <= sums) & (sums < p - y - tol)].sum()
        ds.append(p * q * (upper - lower))
    return np.array(ds)


def float_minimax_search(q: float, n: int, restarts: int = 8, seed: int = 20260530) -> dict[str, object]:
    p = 1 - q
    bounds = [(-6, 6)] * n

    def objective(z: np.ndarray) -> float:
        w = normalize_capped_from_logits(z, p)
        ds = all_deltas_float(w, q)
        # Minimize the best available coalescence gain.
        return float(np.max(ds))

    best = None
    for r in range(restarts):
        res = differential_evolution(
            objective,
            bounds,
            seed=seed + 1000 * r + n,
            maxiter=50,
            popsize=7,
            polish=True,
            updating="immediate",
            workers=1,
            tol=1e-8,
        )
        w = normalize_capped_from_logits(res.x, p)
        ds = all_deltas_float(w, q)
        rec = {
            "q": q,
            "p": p,
            "n": n,
            "objective": float(np.max(ds)),
            "min_delta": float(np.min(ds)),
            "vector": w.tolist(),
            "deltas": ds.tolist(),
        }
        if best is None or rec["objective"] < best["objective"]:
            best = rec
    return best


def grid_vectors(n: int, denom: int, cap_num: int):
    parts: list[int] = []

    def rec(pos: int, remaining: int):
        if pos == n:
            if remaining == 0:
                yield tuple(parts)
            return
        left = n - pos - 1
        lo = max(0, remaining - left * cap_num)
        hi = min(cap_num, remaining)
        for v in range(lo, hi + 1):
            parts.append(v)
            yield from rec(pos + 1, remaining - v)
            parts.pop()

    yield from rec(0, denom)


def exhaustive_grid_search(q: Fraction, n: int, denom: int) -> dict[str, object]:
    p = 1 - q
    cap = p * denom
    if cap.denominator != 1:
        raise ValueError("denominator incompatible with p cap")
    cap_num = int(cap)
    tested = 0
    best = None
    counterexample = None
    # Sort vectors to avoid permutations.
    for parts in grid_vectors(n, denom, cap_num):
        if any(parts[i] > parts[i + 1] for i in range(n - 1)):
            continue
        if parts[0] == 0:
            continue
        w = tuple(Fraction(v, denom) for v in parts)
        tested += 1
        deltas = all_deltas_exact(w, q)
        max_d = max(deltas.values())
        rec = (max_d, w, deltas, aggregate_sums(w, deltas))
        if best is None or max_d < best[0]:
            best = rec
        if max_d < 0:
            counterexample = rec
            break
    return {
        "q": str(q),
        "p": str(p),
        "n": n,
        "denom": denom,
        "tested_sorted_positive": tested,
        "best_max_delta": str(best[0]) if best else None,
        "best_max_delta_float": float(best[0]) if best else None,
        "best_vector": [str(x) for x in best[1]] if best else None,
        "best_deltas": {str(k): str(v) for k, v in best[2].items()} if best else None,
        "best_aggregates": {k: str(v) for k, v in best[3].items()} if best else None,
        "counterexample": None
        if counterexample is None
        else {
            "vector": [str(x) for x in counterexample[1]],
            "deltas": {str(k): str(v) for k, v in counterexample[2].items()},
        },
    }


def frac_json_default(obj):
    if isinstance(obj, Fraction):
        return str(obj)
    raise TypeError(type(obj))


def main() -> None:
    DATA.mkdir(exist_ok=True)

    # Sanity check the interval formula against direct Phi evaluation.
    sanity_vectors = [
        (Fraction(1, 3), (Fraction(1, 3), Fraction(1, 3), Fraction(1, 3))),
        (Fraction(3, 4), (Fraction(1, 4), Fraction(1, 4), Fraction(1, 4), Fraction(1, 4))),
        (Fraction(4, 5), (Fraction(1, 5),) * 5),
        (Fraction(7, 10), (Fraction(3, 10), Fraction(3, 10), Fraction(2, 10), Fraction(2, 10))),
    ]
    sanity = []
    for q, w in sanity_vectors:
        for i, j in combinations(range(len(w)), 2):
            a = delta_exact_by_phi(w, q, i, j)
            b = delta_exact_interval(w, q, i, j)
            sanity.append({"q": str(q), "w": [str(x) for x in w], "pair": [i, j], "by_phi": str(a), "by_interval": str(b), "ok": a == b})

    q_values = [Fraction(2, 3), Fraction(7, 10), Fraction(3, 4), Fraction(4, 5), Fraction(5, 6)]
    n_values = list(range(3, 11))
    denoms = [24, 30, 36, 40, 48, 60]
    random_records = exact_random_search(q_values, n_values, denoms, trials_per_cell=60)

    grids = []
    for q, cases in {
        Fraction(2, 3): [(3, 24), (4, 24), (5, 24), (6, 24)],
        Fraction(3, 4): [(4, 24), (5, 24), (6, 24), (7, 24)],
        Fraction(4, 5): [(5, 30), (6, 30), (7, 30)],
        Fraction(5, 6): [(6, 36), (7, 36)],
    }.items():
        for n, denom in cases:
            if n * (1 - q) >= 1:
                grids.append(exhaustive_grid_search(q, n, denom))

    floats = []
    for q in [2 / 3, 0.70, 0.75, 0.80, 5 / 6]:
        p = 1 - q
        for n in range(math.ceil(1 / p), min(math.ceil(1 / p) + 3, 10)):
            floats.append(float_minimax_search(q, n, restarts=1))

    equal_traps = []
    for n in range(4, 10):
        # Choose a rational midpoint p in the interval where 1/n < p < 1/(n-1).
        p = (Fraction(1, n) + Fraction(1, n - 1)) / 2
        q = 1 - p
        w = (Fraction(1, n),) * n
        deltas = all_deltas_exact(w, q)
        equal_traps.append(
            {
                "n": n,
                "p": str(p),
                "q": str(q),
                "vector": [str(x) for x in w],
                "phi": str(phi_exact(w, q)),
                "q_minus_phi": str(q - phi_exact(w, q)),
                "delta_each_pair": str(next(iter(deltas.values()))),
                "formula": "Delta = p*q^(n-2)*(n-2-(n-1)*q), negative for q>(n-2)/(n-1)",
            }
        )

    out = {
        "sanity": sanity,
        "random_exact": random_records,
        "exhaustive_grids": grids,
        "float_minimax": floats,
        "equal_weight_trap_family": equal_traps,
    }
    out_path = DATA / "round8_coalescence_results.json"
    out_path.write_text(json.dumps(out, indent=2, default=frac_json_default), encoding="utf-8")

    # Human-readable summary.
    lines = []
    lines.append("Sanity interval-vs-Phi checks: " + ("OK" if all(r["ok"] for r in sanity) else "FAILED"))
    if random_records:
        best_random = min(
            (r for r in random_records if r["best_max_delta"] is not None),
            key=lambda r: r["best_max_delta_float"],
        )
        lines.append("Best exact random cell:")
        lines.append(json.dumps(best_random, indent=2))
    if grids:
        best_grid = min(grids, key=lambda r: r["best_max_delta_float"])
        lines.append("Best exhaustive grid:")
        lines.append(json.dumps(best_grid, indent=2))
    if floats:
        best_float = min(floats, key=lambda r: r["objective"])
        lines.append("Best float minimax:")
        lines.append(json.dumps(best_float, indent=2))
    lines.append("Equal-weight trap family:")
    lines.append(json.dumps(equal_traps, indent=2))
    counters = [
        r for r in random_records if r.get("counterexample")
    ] + [r for r in grids if r.get("counterexample")]
    lines.append(f"Counterexamples found: {len(counters)}")
    (DATA / "round8_coalescence_summary.txt").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
