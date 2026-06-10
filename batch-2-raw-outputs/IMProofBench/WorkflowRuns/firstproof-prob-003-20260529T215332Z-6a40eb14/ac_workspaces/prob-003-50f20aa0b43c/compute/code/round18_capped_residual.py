#!/usr/bin/env python3
"""Capped residual checks for the largest-weight induction route.

The non-vacuous induction regime is max_i w_i <= p = 1-q.  This script:
  * computes pivot-plus-dust examples, which approach equality;
  * performs a fast random walk on the capped simplex to look for negative
    residual slack.
"""

from __future__ import annotations

import json
import math
import random
from pathlib import Path

import numpy as np
from scipy.stats import binom

from round18_complement_experiments import phi_and_derivative, residual_gap


def pivot_dust(q: float, eps: float, n_dust: int) -> dict:
    p = 1.0 - q
    a = p - eps
    d = (1.0 - a) / n_dust

    def strict_tail(threshold: float) -> float:
        # P[d Bin(N,q) > threshold].
        k = math.floor(threshold / d) + 1
        if k <= 0:
            return 1.0
        if k > n_dust:
            return 0.0
        return float(binom.sf(k - 1, n_dust, q))

    def leq_prob(threshold: float) -> float:
        # P[d Bin(N,q) <= threshold].
        k = math.floor((threshold + 1e-14) / d)
        if k < 0:
            return 0.0
        if k >= n_dust:
            return 1.0
        return float(binom.cdf(k, n_dust, q))

    phi = q * strict_tail(q - a) + p * strict_tail(q)
    lhs = p * strict_tail(q)
    rhs = q * leq_prob(q - a)
    return {
        "q": q,
        "p": p,
        "epsilon": eps,
        "n": n_dust + 1,
        "a": a,
        "dust_weight": (1.0 - a) / n_dust,
        "phi": phi,
        "phi_minus_q": phi - q,
        "residual_slack": rhs - lhs,
        "residual_lhs": lhs,
        "residual_rhs": rhs,
    }


def capped_walk_sample(n: int, cap: float, rng: random.Random, steps: int = 800) -> np.ndarray:
    """Sample approximately from the capped simplex by random pair transfers."""
    if n * cap < 1.0 - 1e-12:
        raise ValueError("empty capped simplex")
    x = np.ones(n) / n
    # If equal point violates cap due to roundoff/invalid n, use fill.
    if x[0] > cap:
        x[:] = 0.0
        rem = 1.0
        for i in range(n):
            put = min(cap, rem)
            x[i] = put
            rem -= put
    for _ in range(steps):
        i = rng.randrange(n)
        j = rng.randrange(n)
        if i == j or x[j] <= 0 or x[i] >= cap:
            continue
        amount = rng.random() * min(x[j], cap - x[i])
        x[i] += amount
        x[j] -= amount
    return np.sort(x)[::-1]


def random_capped_search(seed: int = 18182) -> list[dict]:
    rng = random.Random(seed)
    q_values = [2 / 3, 0.7, 0.75, 0.8, 0.9]
    records = []
    for q in q_values:
        p = 1.0 - q
        n0 = math.ceil(1.0 / p)
        for n in range(n0, min(n0 + 5, 15)):
            best_slack = None
            best_phi = None
            trials = 600 if n <= 12 else 250
            for _ in range(trials):
                w = capped_walk_sample(n, p, rng)
                rg = residual_gap(w, q)
                if best_slack is None or rg["slack"] < best_slack["slack"]:
                    best_slack = {**rg, "n": n}
                phi, deriv, famsize, gap = phi_and_derivative(w, q)
                rec = {
                    "q": q,
                    "p": p,
                    "n": n,
                    "weights": w.tolist(),
                    "phi": phi,
                    "phi_minus_q": phi - q,
                    "derivative": deriv,
                    "family_size": famsize,
                    "next_gap": gap,
                }
                if best_phi is None or rec["phi_minus_q"] > best_phi["phi_minus_q"]:
                    best_phi = rec
            records.append({"kind": "random_capped_residual", "best": best_slack})
            records.append({"kind": "random_capped_phi", "best": best_phi})
    return records


def main() -> None:
    pivot = []
    for q in [2 / 3, 0.7, 0.75, 0.8, 0.9]:
        for eps in [0.1 * (1 - q), 0.03 * (1 - q), 0.01 * (1 - q)]:
            for n_dust in [20, 100, 500, 10000]:
                pivot.append(pivot_dust(q, eps, n_dust))
    random_records = random_capped_search()
    out = {
        "pivot_dust": pivot,
        "random_records": random_records,
    }
    path = Path("data/round18/capped_residual_fast.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2, sort_keys=True), encoding="utf-8")
    print(f"wrote {path}")
    print("best pivot-dust by phi_minus_q")
    for row in sorted(pivot, key=lambda r: r["phi_minus_q"], reverse=True)[:10]:
        print(
            "q", row["q"],
            "eps", row["epsilon"],
            "N", row["n"] - 1,
            "phi-q", row["phi_minus_q"],
            "resid_slack", row["residual_slack"],
        )
    print("best random capped residual slacks")
    rows = [r["best"] for r in random_records if r["kind"] == "random_capped_residual"]
    for row in sorted(rows, key=lambda r: r["slack"])[:10]:
        print("q", row["q"], "n", row["n"], "slack", row["slack"], "a", row["a"])


if __name__ == "__main__":
    main()
