#!/usr/bin/env python3
"""Round 18 experiments for the complement inequality.

The target is
    Phi_q(w) = P_q[sum_i w_i eta_i > q] <= q,  q >= 2/3.

This script contains exact-enough enumeration utilities for small n and runs:
  * random searches for violations of the largest-weight residual inequality;
  * scans of threshold-flow derivative data near large values of Phi_q(w)-q;
  * simple local optimization from random starts.

Output is JSON, with all floats rounded only at serialization time.
"""

from __future__ import annotations

import argparse
import json
import math
import random
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

import numpy as np
from scipy.optimize import differential_evolution, minimize


def subset_sums(weights: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Return subset sums and cardinalities for all subsets of weights."""
    sums = np.array([0.0])
    cards = np.array([0], dtype=np.int16)
    for w in weights:
        sums = np.concatenate([sums, sums + w])
        cards = np.concatenate([cards, cards + 1])
    return sums, cards


def phi_and_derivative(weights: np.ndarray, q: float) -> tuple[float, float, int, float]:
    """Phi_q(w), derivative between breakpoints, family size, min positive gap."""
    n = len(weights)
    p = 1.0 - q
    sums, cards = subset_sums(weights)
    mask = sums > q + 1e-14
    probs = (q**cards) * (p ** (n - cards))
    phi = float(np.sum(probs[mask]))
    if phi == 0.0:
        deriv = 0.0
    else:
        deriv = float(np.sum(probs[mask] * (cards[mask] / q - (n - cards[mask]) / p)))
    gaps = sums - q
    pos = gaps[gaps > 1e-14]
    gap = float(np.min(pos)) if len(pos) else float("inf")
    return phi, deriv, int(np.sum(mask)), gap


def residual_gap(weights: np.ndarray, q: float, a_index: int | None = None) -> dict:
    """Return largest-weight induction residual inequality slack.

    For maximal a, condition on its coordinate:
      p P[R > q] <= q P[R <= q-a].
    slack = RHS - LHS, so negative is a counterexample to the induction lemma.
    """
    n = len(weights)
    if a_index is None:
        a_index = int(np.argmax(weights))
    a = float(weights[a_index])
    rest = np.delete(weights, a_index)
    sums, cards = subset_sums(rest)
    p = 1.0 - q
    probs = (q**cards) * (p ** ((n - 1) - cards))
    lhs = p * float(np.sum(probs[sums > q + 1e-14]))
    rhs = q * float(np.sum(probs[sums <= q - a + 1e-14]))
    return {
        "q": q,
        "p": p,
        "a": a,
        "weights": weights.tolist(),
        "lhs": lhs,
        "rhs": rhs,
        "slack": rhs - lhs,
    }


def random_simplex(n: int, rng: random.Random) -> np.ndarray:
    x = np.array([rng.expovariate(1.0) for _ in range(n)], dtype=float)
    return x / np.sum(x)


def sorted_simplex_from_unconstrained(x: np.ndarray) -> np.ndarray:
    y = np.exp(np.clip(x, -40, 40))
    w = y / np.sum(y)
    return np.sort(w)[::-1]


@dataclass
class SearchRecord:
    kind: str
    n: int
    q: float
    value: float
    phi: float | None
    deriv: float | None
    residual_slack: float | None
    weights: list[float]
    extra: dict


def scan_random(seed: int, trials: int, ns: Iterable[int], q_grid: Iterable[float]) -> list[SearchRecord]:
    rng = random.Random(seed)
    records: list[SearchRecord] = []
    best_phi_gap: SearchRecord | None = None
    best_deriv_at_near: SearchRecord | None = None
    best_resid: SearchRecord | None = None

    for n in ns:
        for _ in range(trials):
            w = np.sort(random_simplex(n, rng))[::-1]
            for q in q_grid:
                phi, deriv, famsize, gap = phi_and_derivative(w, q)
                rec_gap = phi - q
                if best_phi_gap is None or rec_gap > best_phi_gap.value:
                    best_phi_gap = SearchRecord(
                        "max_phi_minus_q",
                        n,
                        q,
                        rec_gap,
                        phi,
                        deriv,
                        None,
                        w.tolist(),
                        {"family_size": famsize, "next_gap": gap},
                    )
                # derivative is only interesting close to the hypothetical boundary.
                if phi - q > -0.02:
                    score = deriv
                    if best_deriv_at_near is None or score > best_deriv_at_near.value:
                        best_deriv_at_near = SearchRecord(
                            "max_derivative_near_boundary",
                            n,
                            q,
                            score,
                            phi,
                            deriv,
                            None,
                            w.tolist(),
                            {"phi_minus_q": phi - q, "family_size": famsize, "next_gap": gap},
                        )
                rg = residual_gap(w, q)
                if best_resid is None or rg["slack"] < best_resid.value:
                    best_resid = SearchRecord(
                        "min_residual_slack",
                        n,
                        q,
                        rg["slack"],
                        None,
                        None,
                        rg["slack"],
                        w.tolist(),
                        {"lhs": rg["lhs"], "rhs": rg["rhs"], "a": rg["a"]},
                    )
    for rec in (best_phi_gap, best_deriv_at_near, best_resid):
        if rec is not None:
            records.append(rec)
    return records


def optimize_phi_minus_q(n: int, q: float, seed: int) -> SearchRecord:
    """Numerically maximize Phi_q(w)-q over the simplex."""

    def objective(x: np.ndarray) -> float:
        w = sorted_simplex_from_unconstrained(x)
        phi, _, _, _ = phi_and_derivative(w, q)
        return -(phi - q)

    bounds = [(-8, 8)] * n
    de = differential_evolution(objective, bounds, seed=seed, polish=False, maxiter=80, popsize=10, tol=1e-8)
    loc = minimize(objective, de.x, method="Nelder-Mead", options={"maxiter": 5000, "xatol": 1e-12, "fatol": 1e-12})
    x = loc.x if loc.fun < de.fun else de.x
    w = sorted_simplex_from_unconstrained(x)
    phi, deriv, famsize, gap = phi_and_derivative(w, q)
    return SearchRecord(
        "optimized_phi_minus_q",
        n,
        q,
        phi - q,
        phi,
        deriv,
        None,
        w.tolist(),
        {"family_size": famsize, "next_gap": gap},
    )


def optimize_residual_slack(n: int, q: float, seed: int) -> SearchRecord:
    """Numerically minimize residual slack for the largest-weight induction."""

    def objective(x: np.ndarray) -> float:
        w = sorted_simplex_from_unconstrained(x)
        return residual_gap(w, q)["slack"]

    bounds = [(-8, 8)] * n
    de = differential_evolution(objective, bounds, seed=seed, polish=False, maxiter=80, popsize=10, tol=1e-8)
    loc = minimize(objective, de.x, method="Nelder-Mead", options={"maxiter": 5000, "xatol": 1e-12, "fatol": 1e-12})
    x = loc.x if loc.fun < de.fun else de.x
    w = sorted_simplex_from_unconstrained(x)
    rg = residual_gap(w, q)
    return SearchRecord(
        "optimized_residual_slack",
        n,
        q,
        rg["slack"],
        None,
        None,
        rg["slack"],
        w.tolist(),
        {"lhs": rg["lhs"], "rhs": rg["rhs"], "a": rg["a"]},
    )


def exact_named_examples() -> list[dict]:
    out = []
    examples = [
        ("equal_3_q23", np.array([1 / 3] * 3), 2 / 3),
        ("equal_4_q07", np.array([1 / 4] * 4), 0.7),
        ("mse_counterexample_complement", np.array([0.33, 0.335, 0.335]), 0.65),
        ("pivot_dust_8", np.array([0.29] + [0.71 / 7] * 7), 0.7),
    ]
    for name, w, q in examples:
        phi, deriv, famsize, gap = phi_and_derivative(w, q)
        rg = residual_gap(w, q)
        out.append(
            {
                "name": name,
                "q": q,
                "weights": w.tolist(),
                "phi": phi,
                "phi_minus_q": phi - q,
                "derivative_between_breakpoints": deriv,
                "family_size": famsize,
                "next_gap": gap,
                "residual": rg,
            }
        )
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="data/round18/complement_experiments.json")
    ap.add_argument("--trials", type=int, default=3000)
    ap.add_argument("--seed", type=int, default=18018)
    args = ap.parse_args()

    q_grid = [2 / 3, 0.67, 0.68, 0.7, 0.72, 0.75, 0.8, 0.85, 0.9, 0.95]
    records = scan_random(args.seed, args.trials, range(2, 11), q_grid)
    for n in range(2, 9):
        for q in [2 / 3, 0.68, 0.7, 0.75, 0.8, 0.9]:
            records.append(optimize_phi_minus_q(n, q, args.seed + 31 * n + int(1000 * q)))
            records.append(optimize_residual_slack(n, q, args.seed + 131 * n + int(1000 * q)))

    result = {
        "named_examples": exact_named_examples(),
        "records": [asdict(r) for r in records],
    }
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(f"wrote {out}")
    for item in result["named_examples"]:
        print(item["name"], "q", item["q"], "phi-q", item["phi_minus_q"], "resid_slack", item["residual"]["slack"])
    for r in records[:3]:
        print(r.kind, "n", r.n, "q", r.q, "value", r.value)


if __name__ == "__main__":
    main()
