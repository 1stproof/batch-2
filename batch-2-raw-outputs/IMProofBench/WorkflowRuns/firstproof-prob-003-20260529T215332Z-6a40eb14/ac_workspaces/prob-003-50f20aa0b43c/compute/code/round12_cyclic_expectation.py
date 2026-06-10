#!/usr/bin/env python3
"""Round 12 checks for the rational cyclic expectation inequality.

The cyclic statement for p=r/b is

    E #{j : L_j < p} <= b-r.

For fixed j this is exactly

    b * P(sum_i w_i X_i < p) <= b-r,  X_i iid Bernoulli(p).

This script therefore concentrates on the weighted Bernoulli lower tail,
but also includes direct cyclic enumeration for small integer-grid weights.
MILP searches are over fixed support size n.  The "strict" search enforces
subset sums <= p-eps for selected light subsets, giving an inner
approximation to the strict event.  The "closed" search uses eps=0 and gives
an upper-bound relaxation for the strict problem.
"""

from __future__ import annotations

import argparse
import itertools
import json
from dataclasses import asdict, dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, linprog, milp


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "round12"
DATA_DIR.mkdir(parents=True, exist_ok=True)


def masks(n: int) -> range:
    return range(1 << n)


def popcount(mask: int) -> int:
    return int(mask.bit_count())


def mask_sum(mask: int, weights: Iterable[Fraction]) -> Fraction:
    return sum((w for i, w in enumerate(weights) if (mask >> i) & 1), Fraction(0))


def prob_mask_fraction(mask: int, n: int, p: Fraction) -> Fraction:
    return (p ** popcount(mask)) * ((1 - p) ** (n - popcount(mask)))


def lower_tail_fraction(p: Fraction, weights: list[Fraction]) -> Fraction:
    n = len(weights)
    return sum(
        prob_mask_fraction(mask, n, p)
        for mask in masks(n)
        if mask_sum(mask, weights) < p
    )


def lower_tail_units(p: Fraction, parts: tuple[int, ...], denom: int) -> Fraction:
    """Exact lower tail for weights parts_i/denom via dynamic programming."""

    dist: dict[int, Fraction] = {0: Fraction(1)}
    q = 1 - p
    for part in parts:
        nxt: dict[int, Fraction] = {}
        for s, pr in dist.items():
            nxt[s] = nxt.get(s, Fraction(0)) + pr * q
            nxt[s + part] = nxt.get(s + part, Fraction(0)) + pr * p
        dist = nxt
    a, b = p.numerator, p.denominator
    return sum(pr for s, pr in dist.items() if b * s < a * denom)


def lower_tail_float(p: float, weights: np.ndarray, tol: float = 1e-12) -> float:
    n = len(weights)
    q = 1.0 - p
    total = 0.0
    for mask in masks(n):
        s = 0.0
        k = popcount(mask)
        for i in range(n):
            if (mask >> i) & 1:
                s += float(weights[i])
        if s < p - tol:
            total += (p**k) * (q ** (n - k))
    return total


def probs_by_mask(n: int, p: float) -> np.ndarray:
    q = 1.0 - p
    return np.array([(p ** popcount(mask)) * (q ** (n - popcount(mask))) for mask in masks(n)])


def incidence(n: int) -> np.ndarray:
    mat = np.zeros((1 << n, n))
    for mask in masks(n):
        for i in range(n):
            if (mask >> i) & 1:
                mat[mask, i] = 1.0
    return mat


@dataclass
class TailMilpResult:
    p: str
    p_float: float
    n: int
    eps: float
    cap: float | None
    force_sum_one: bool
    success: bool
    status: int
    message: str
    objective_light_prob: float | None
    gap_to_target: float | None
    expected_light: float | None
    expected_gap: float | None
    weights: list[float] | None
    true_strict_light_prob_at_solution: float | None
    true_strict_gap_at_solution: float | None


def tail_milp(
    p_frac: Fraction,
    n: int,
    eps: float,
    cap: float | None,
    time_limit: float,
    force_sum_one: bool = True,
) -> TailMilpResult:
    """Maximize p-biased mass of subsets forced to have weight <= p-eps.

    Variables are w_i and binary y_A.  y_A=1 implies w(A) <= p-eps.
    The objective maximizes sum_A Pr_p(A)y_A.  If eps=0, this is the closed
    lower tail relaxation.  If eps>0, it searches strict chambers with slack.
    """

    p = float(p_frac)
    k = 1 << n
    total = n + k
    probs = probs_by_mask(n, p)

    c = np.zeros(total)
    c[n:] = -probs

    lb = np.zeros(total)
    ub = np.ones(total)
    if cap is not None:
        ub[:n] = cap
    bounds = Bounds(lb, ub)

    integrality = np.zeros(total, dtype=int)
    integrality[n:] = 1

    rows = []
    lows = []
    ups = []

    mat = incidence(n)
    big_m = n + 1.0
    for mask in masks(n):
        row = np.zeros(total)
        row[:n] = mat[mask]
        row[n + mask] = big_m
        # y=1 => w(A) <= p-eps, i.e. w(A)+M*y <= p-eps+M.
        rows.append(row)
        lows.append(-np.inf)
        ups.append(p - eps + big_m)

    if force_sum_one:
        row = np.zeros(total)
        row[:n] = 1.0
        rows.append(row)
        lows.append(1.0)
        ups.append(1.0)

    constraints = LinearConstraint(np.vstack(rows), np.array(lows), np.array(ups))
    res = milp(
        c=c,
        integrality=integrality,
        bounds=bounds,
        constraints=constraints,
        options={"time_limit": time_limit, "mip_rel_gap": 0.0},
    )

    objective = None
    weights = None
    true_strict = None
    if res.fun is not None:
        objective = -float(res.fun)
    if res.x is not None:
        weights = [float(x) for x in res.x[:n]]
        true_strict = lower_tail_float(p, np.array(weights))

    target = 1.0 - p
    return TailMilpResult(
        p=str(p_frac),
        p_float=p,
        n=n,
        eps=eps,
        cap=cap,
        force_sum_one=force_sum_one,
        success=bool(res.success),
        status=int(res.status),
        message=str(res.message),
        objective_light_prob=objective,
        gap_to_target=None if objective is None else target - objective,
        expected_light=None if objective is None else (float(p_frac.denominator) * objective),
        expected_gap=None if objective is None else (float(p_frac.denominator - p_frac.numerator) - float(p_frac.denominator) * objective),
        weights=weights,
        true_strict_light_prob_at_solution=true_strict,
        true_strict_gap_at_solution=None if true_strict is None else target - true_strict,
    )


def integer_partitions(total: int, max_part: int | None = None) -> Iterable[tuple[int, ...]]:
    if total == 0:
        yield ()
        return
    if max_part is None or max_part > total:
        max_part = total
    for first in range(max_part, 0, -1):
        for rest in integer_partitions(total - first, first):
            yield (first,) + rest


def grid_tail_extrema(p_frac: Fraction, denom: int, cap_strict: bool) -> dict[str, object]:
    """Enumerate sorted positive grid weights summing to one."""

    best: tuple[Fraction, tuple[int, ...]] | None = None
    count = 0
    for parts_desc in integer_partitions(denom):
        parts = tuple(sorted(parts_desc))
        if cap_strict and max(parts) * p_frac.denominator >= p_frac.numerator * denom:
            continue
        count += 1
        val = lower_tail_units(p_frac, parts, denom)
        if best is None or val > best[0]:
            best = (val, parts)
    if best is None:
        return {"p": str(p_frac), "denom": denom, "cap_strict": cap_strict, "count": 0}
    val, parts = best
    b = p_frac.denominator
    r = p_frac.numerator
    return {
        "p": str(p_frac),
        "denom": denom,
        "cap_strict": cap_strict,
        "count": count,
        "max_light_prob": str(val),
        "max_light_prob_float": float(val),
        "target": str(1 - p_frac),
        "gap_to_target": str((1 - p_frac) - val),
        "expected_light": str(b * val),
        "expected_gap": str((b - r) - b * val),
        "parts": list(parts),
        "weights": [str(Fraction(x, denom)) for x in parts],
    }


def cyclic_light_count(b: int, r: int, bin_loads: list[Fraction]) -> int:
    p = Fraction(r, b)
    light = 0
    for j in range(b):
        s = sum((bin_loads[(j + k) % b] for k in range(r)), Fraction(0))
        if s < p:
            light += 1
    return light


def cyclic_expected_light_fraction(b: int, r: int, weights: list[Fraction]) -> Fraction:
    """Directly enumerate all b^n cyclic allocations for small n."""

    total = Fraction(0)
    n = len(weights)
    for positions in itertools.product(range(b), repeat=n):
        loads = [Fraction(0) for _ in range(b)]
        for w, pos in zip(weights, positions):
            loads[pos] += w
        total += cyclic_light_count(b, r, loads)
    return total / (b**n)


def cyclic_grid_examples() -> list[dict[str, object]]:
    examples: list[dict[str, object]] = []
    hand = [
        (7, 2, [Fraction(1, 7)] * 7),
        (7, 2, [Fraction(2, 7), Fraction(5, 7)]),
        (10, 3, [Fraction(1, 4)] * 4),
        (10, 3, [Fraction(3, 10), Fraction(7, 10)]),
        (13, 4, [Fraction(1, 4)] * 4),
        (13, 4, [Fraction(4, 13), Fraction(9, 13)]),
    ]
    for b, r, weights in hand:
        exp = cyclic_expected_light_fraction(b, r, weights)
        tail = lower_tail_fraction(Fraction(r, b), weights)
        examples.append(
            {
                "b": b,
                "r": r,
                "p": f"{r}/{b}",
                "weights": [str(w) for w in weights],
                "direct_expected_light": str(exp),
                "direct_expected_light_float": float(exp),
                "b_times_tail": str(b * tail),
                "target": b - r,
                "gap": str(Fraction(b - r) - exp),
            }
        )
    return examples


def pointwise_excess_examples() -> list[dict[str, object]]:
    """Find deterministic bin-load vectors with more than b-r light intervals."""

    out = []
    for b, r in [(7, 2), (10, 3), (13, 4)]:
        threshold = r / b
        desired = b - r + 1
        found = None
        for light_starts in itertools.combinations(range(b), desired):
            rows = []
            rhs = []
            for j in light_starts:
                row = np.zeros(b)
                for k in range(r):
                    row[(j + k) % b] = 1.0
                rows.append(row)
                rhs.append(threshold - 1e-5)
            res = linprog(
                c=np.zeros(b),
                A_ub=np.array(rows),
                b_ub=np.array(rhs),
                A_eq=np.ones((1, b)),
                b_eq=np.array([1.0]),
                bounds=[(0.0, None)] * b,
                method="highs",
            )
            if res.success:
                loads = [Fraction(float(x)).limit_denominator(10**6) for x in res.x]
                cnt = cyclic_light_count(b, r, loads)
                found = {
                    "b": b,
                    "r": r,
                    "target": b - r,
                    "light_count": cnt,
                    "forced_light_starts": list(light_starts),
                    "bin_loads_float": [float(x) for x in res.x],
                    "bin_loads_rationalized": [str(x) for x in loads],
                }
                break
        if found is not None:
            out.append(found)
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--time-limit", type=float, default=45.0)
    parser.add_argument("--n-max", type=int, default=8)
    parser.add_argument("--out", default=str(DATA_DIR / "round12_results.json"))
    args = parser.parse_args()

    p_values = [Fraction(2, 7), Fraction(3, 10), Fraction(4, 13)]

    milp_results = []
    for p in p_values:
        for n in range(1, args.n_max + 1):
            milp_results.append(tail_milp(p, n, eps=0.0, cap=None, time_limit=args.time_limit))
            # Strict capped chamber: all weights are below p, with a small slack.
            cap = float(p) - 1e-5
            if cap > 0:
                milp_results.append(tail_milp(p, n, eps=1e-6, cap=cap, time_limit=args.time_limit))

    grids = []
    for p in p_values:
        for denom in [p.denominator, 2 * p.denominator]:
            grids.append(grid_tail_extrema(p, denom, cap_strict=False))
            grids.append(grid_tail_extrema(p, denom, cap_strict=True))

    exact_named = []
    for p, weights in [
        (Fraction(2, 7), [Fraction(2, 7), Fraction(5, 7)]),
        (Fraction(2, 7), [Fraction(1, 4)] * 4),
        (Fraction(3, 10), [Fraction(3, 10), Fraction(7, 10)]),
        (Fraction(3, 10), [Fraction(1, 4)] * 4),
        (Fraction(4, 13), [Fraction(4, 13), Fraction(9, 13)]),
        (Fraction(4, 13), [Fraction(1, 4)] * 4),
    ]:
        val = lower_tail_fraction(p, weights)
        exact_named.append(
            {
                "p": str(p),
                "weights": [str(w) for w in weights],
                "light_prob": str(val),
                "light_prob_float": float(val),
                "target": str(1 - p),
                "gap_to_target": str((1 - p) - val),
            }
        )

    payload = {
        "milp_results": [asdict(x) for x in milp_results],
        "grid_tail_extrema": grids,
        "exact_named_examples": exact_named,
        "cyclic_direct_examples": cyclic_grid_examples(),
        "pointwise_excess_examples": pointwise_excess_examples(),
    }
    Path(args.out).write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")

    # Compact markdown summary for quick inspection.
    lines = ["# Round 12 cyclic expectation computations", ""]
    lines.append("## MILP strict capped minima by p,n")
    for p in p_values:
        lines.append("")
        lines.append(f"p={p}")
        rows = [
            r
            for r in milp_results
            if r.p == str(p) and r.eps > 0 and r.objective_light_prob is not None
        ]
        for r in rows:
            lines.append(
                f"- n={r.n}: max light <= {r.objective_light_prob:.12f}, "
                f"gap {r.gap_to_target:.12g}, w={np.round(r.weights, 6).tolist() if r.weights else None}"
            )
    lines.append("")
    lines.append("## Grid extrema")
    for g in grids:
        if g.get("count", 0):
            lines.append(
                f"- p={g['p']} d={g['denom']} cap={g['cap_strict']}: "
                f"max={g['max_light_prob']} gap={g['gap_to_target']} weights={g['weights']}"
            )
    lines.append("")
    lines.append("## Direct cyclic examples")
    for ex in payload["cyclic_direct_examples"]:
        lines.append(
            f"- b={ex['b']} r={ex['r']} weights={ex['weights']}: "
            f"E light={ex['direct_expected_light']} target={ex['target']} gap={ex['gap']}"
        )
    lines.append("")
    lines.append("## Pointwise deterministic excess examples found")
    for ex in payload["pointwise_excess_examples"]:
        lines.append(
            f"- b={ex['b']} r={ex['r']}: light={ex['light_count']} "
            f"target={ex['target']} loads={ex['bin_loads_rationalized']}"
        )
    (DATA_DIR / "round12_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(args.out)
    print(DATA_DIR / "round12_summary.md")


if __name__ == "__main__":
    main()
