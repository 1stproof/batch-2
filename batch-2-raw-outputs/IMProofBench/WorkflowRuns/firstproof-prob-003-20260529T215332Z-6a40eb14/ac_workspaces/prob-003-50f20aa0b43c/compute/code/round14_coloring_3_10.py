#!/usr/bin/env python3
"""Round 14 averaged-coloring computations for p=3/10.

For p=a/b and a random coloring of original weight atoms into b colors,

    E #{J in C([b],a): load(J) >= a/b}
      = C(b,a) * P_p(sum_i w_i v_i >= p).

The p=3/10 target is therefore E heavy triples >= 36.
This script records exact values for representative vectors and grid searches.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import asdict, dataclass
from fractions import Fraction
from pathlib import Path
import json
import math

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "round14"
DATA.mkdir(parents=True, exist_ok=True)


P = Fraction(3, 10)
Q = 1 - P
B = 10
A = 3
NTRIPLES = math.comb(B, A)
TARGET_HEAVY = math.comb(B - 1, A - 1)


def fstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def lower_tail(weights: list[Fraction], p: Fraction = P) -> Fraction:
    dist: dict[Fraction, Fraction] = {Fraction(0): Fraction(1)}
    q = 1 - p
    for w in weights:
        nxt: dict[Fraction, Fraction] = defaultdict(Fraction)
        for s, pr in dist.items():
            nxt[s] += pr * q
            nxt[s + w] += pr * p
        dist = dict(nxt)
    return sum(pr for s, pr in dist.items() if s < p)


def success_tail(weights: list[Fraction], p: Fraction = P) -> Fraction:
    return 1 - lower_tail(weights, p)


def heavy_expectation(weights: list[Fraction]) -> Fraction:
    return NTRIPLES * success_tail(weights)


def fixed_color_heavy(loads: list[Fraction]) -> int:
    total = 0
    n = len(loads)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if loads[i] + loads[j] + loads[k] >= P:
                    total += 1
    return total


@dataclass
class Example:
    name: str
    weights: list[str] | None
    success: str | None
    success_float: float | None
    expected_heavy: str | None
    expected_heavy_float: float | None
    gap_to_36: str | None
    fixed_loads: list[str] | None = None
    fixed_heavy_triples: int | None = None


def examples() -> list[Example]:
    out: list[Example] = []

    loads = [Fraction(1, 7)] * 7 + [Fraction(0)] * 3
    out.append(
        Example(
            name="deterministic seven 1/7 and three 0 color-load vector",
            weights=None,
            success=None,
            success_float=None,
            expected_heavy=None,
            expected_heavy_float=None,
            gap_to_36=None,
            fixed_loads=[fstr(x) for x in loads],
            fixed_heavy_triples=fixed_color_heavy(loads),
        )
    )

    weight_examples: dict[str, list[Fraction]] = {
        "seven original atoms of weight 1/7": [Fraction(1, 7)] * 7,
        "four original atoms of weight 1/4": [Fraction(1, 4)] * 4,
        "one atom 29/100 plus 60 dust atoms": [Fraction(29, 100)] + [Fraction(71, 6000)] * 60,
        "one atom 1": [Fraction(1)],
    }
    for name, weights in weight_examples.items():
        succ = success_tail(weights)
        exp = NTRIPLES * succ
        out.append(
            Example(
                name=name,
                weights=[fstr(w) for w in weights[:12]] + (["..."] if len(weights) > 12 else []),
                success=fstr(succ),
                success_float=float(succ),
                expected_heavy=fstr(exp),
                expected_heavy_float=float(exp),
                gap_to_36=fstr(exp - TARGET_HEAVY),
            )
        )
    return out


def lower_tail_units(parts: tuple[int, ...], denom: int, p: Fraction = P) -> Fraction:
    dist: dict[int, Fraction] = {0: Fraction(1)}
    q = 1 - p
    for part in parts:
        nxt: dict[int, Fraction] = defaultdict(Fraction)
        for s, pr in dist.items():
            nxt[s] += pr * q
            nxt[s + part] += pr * p
        dist = dict(nxt)
    return sum(pr for s, pr in dist.items() if p.denominator * s < p.numerator * denom)


def integer_partitions(total: int, max_part: int | None = None):
    if total == 0:
        yield ()
        return
    if max_part is None or max_part > total:
        max_part = total
    for first in range(max_part, 0, -1):
        for rest in integer_partitions(total - first, first):
            yield (first,) + rest


@dataclass
class GridResult:
    denom: int
    cap_strict: bool
    count: int
    max_lower_tail: str
    max_lower_tail_float: float
    success: str
    expected_heavy: str
    expected_heavy_float: float
    gap_to_36: str
    parts: list[int]
    weights: list[str]


def grid_search(denom: int, cap_strict: bool) -> GridResult:
    best_val: Fraction | None = None
    best_parts: tuple[int, ...] | None = None
    count = 0
    for parts_desc in integer_partitions(denom):
        parts = tuple(sorted(parts_desc))
        if cap_strict and max(parts) * P.denominator >= P.numerator * denom:
            continue
        count += 1
        val = lower_tail_units(parts, denom)
        if best_val is None or val > best_val:
            best_val = val
            best_parts = parts
    assert best_val is not None and best_parts is not None
    succ = 1 - best_val
    exp = NTRIPLES * succ
    return GridResult(
        denom=denom,
        cap_strict=cap_strict,
        count=count,
        max_lower_tail=fstr(best_val),
        max_lower_tail_float=float(best_val),
        success=fstr(succ),
        expected_heavy=fstr(exp),
        expected_heavy_float=float(exp),
        gap_to_36=fstr(exp - TARGET_HEAVY),
        parts=list(best_parts),
        weights=[fstr(Fraction(x, denom)) for x in best_parts],
    )


@dataclass
class MilpResult:
    n: int
    eps: float
    cap: float | None
    success: bool
    max_light_prob_relaxation: float | None
    heavy_expectation_lower_bound: float | None
    gap_to_36: float | None
    weights: list[float] | None
    message: str


def probs_by_mask(n: int, p: float) -> np.ndarray:
    q = 1.0 - p
    return np.array([(p ** mask.bit_count()) * (q ** (n - mask.bit_count())) for mask in range(1 << n)])


def lower_tail_float(weights: list[float], p: float = 0.3) -> float:
    q = 1.0 - p
    total = 0.0
    n = len(weights)
    for mask in range(1 << n):
        s = sum(weights[i] for i in range(n) if (mask >> i) & 1)
        if s < p - 1e-10:
            total += (p ** mask.bit_count()) * (q ** (n - mask.bit_count()))
    return total


def tail_milp(n: int, eps: float, cap: float | None, time_limit: float) -> MilpResult:
    """Maximize p-biased light mass with y_A=1 => w(A) <= p-eps."""

    p = float(P)
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
    big_m = n + 1.0
    for mask in range(k):
        row = np.zeros(total)
        for i in range(n):
            if (mask >> i) & 1:
                row[i] = 1.0
        row[n + mask] = big_m
        rows.append(row)
        lows.append(-np.inf)
        ups.append(p - eps + big_m)

    row = np.zeros(total)
    row[:n] = 1.0
    rows.append(row)
    lows.append(1.0)
    ups.append(1.0)

    res = milp(
        c,
        integrality=integrality,
        bounds=bounds,
        constraints=LinearConstraint(np.vstack(rows), np.array(lows), np.array(ups)),
        options={"time_limit": time_limit, "mip_rel_gap": 0.0},
    )

    obj = None
    weights = None
    if res.fun is not None:
        obj = -float(res.fun)
    if res.x is not None:
        weights = [float(x) for x in res.x[:n]]
        # Report the true strict light mass at the returned weights, since the
        # binary relaxation may be slightly stale when the solver times out.
        obj = lower_tail_float(weights)
    exp_lower = None if obj is None else NTRIPLES * (1.0 - obj)
    return MilpResult(
        n=n,
        eps=eps,
        cap=cap,
        success=bool(res.success),
        max_light_prob_relaxation=obj,
        heavy_expectation_lower_bound=exp_lower,
        gap_to_36=None if exp_lower is None else exp_lower - TARGET_HEAVY,
        weights=weights,
        message=str(res.message),
    )


def main() -> None:
    ex = examples()
    grids = []
    for denom in (10, 20, 30, 40):
        grids.append(grid_search(denom, cap_strict=False))
        grids.append(grid_search(denom, cap_strict=True))

    milps = []
    for n in (6, 7):
        milps.append(tail_milp(n=n, eps=1e-6, cap=float(P) - 1e-6, time_limit=45.0))

    payload = {
        "p": fstr(P),
        "a": A,
        "b": B,
        "num_triples": NTRIPLES,
        "target_heavy": TARGET_HEAVY,
        "examples": [asdict(x) for x in ex],
        "grid_search": [asdict(x) for x in grids],
        "milp": [asdict(x) for x in milps],
    }
    (DATA / "coloring_3_10_results.json").write_text(json.dumps(payload, indent=2) + "\n")

    lines: list[str] = []
    lines.append("# Round 14 averaged coloring checks for p=3/10")
    lines.append("")
    lines.append("For p=a/b, linearity and symmetry give")
    lines.append("E #heavy a-subsets = binom(b,a) P_p(sum_i w_i v_i >= a/b).")
    lines.append("For a/b=3/10 this is 120 P(S>=0.3), and the target is 36.")
    lines.append("")
    lines.append("## Examples")
    lines.append("")
    lines.append("| example | success probability | expected heavy triples | gap to 36 | fixed heavy triples |")
    lines.append("|---|---:|---:|---:|---:|")
    for e in ex:
        lines.append(
            f"| {e.name} | {e.success or ''} | {e.expected_heavy or ''} | "
            f"{e.gap_to_36 or ''} | {'' if e.fixed_heavy_triples is None else e.fixed_heavy_triples} |"
        )

    lines.append("")
    lines.append("## Exact grid maximization of the light probability")
    lines.append("")
    lines.append("| denom | cap w_i<0.3 | vectors | max light | E heavy | gap to 36 | weights |")
    lines.append("|---:|---|---:|---:|---:|---:|---|")
    for g in grids:
        lines.append(
            f"| {g.denom} | {g.cap_strict} | {g.count} | {g.max_lower_tail} | "
            f"{g.expected_heavy} | {g.gap_to_36} | {g.weights[:12]}{' ...' if len(g.weights) > 12 else ''} |"
        )

    lines.append("")
    lines.append("## Capped MILP chamber search")
    lines.append("")
    lines.append("| n | solver optimal | returned strict light | E heavy | gap to 36 | weights |")
    lines.append("|---:|---|---:|---:|---:|---|")
    for r in milps:
        weights_s = None if r.weights is None else [round(x, 8) for x in r.weights]
        lines.append(
            f"| {r.n} | {r.success} | "
            f"{r.max_light_prob_relaxation if r.max_light_prob_relaxation is not None else math.nan:.12f} | "
            f"{r.heavy_expectation_lower_bound if r.heavy_expectation_lower_bound is not None else math.nan:.12f} | "
            f"{r.gap_to_36 if r.gap_to_36 is not None else math.nan:.12f} | {weights_s} |"
        )

    (DATA / "coloring_3_10_summary.md").write_text("\n".join(lines) + "\n")
    print(DATA / "coloring_3_10_summary.md")
    print(DATA / "coloring_3_10_results.json")


if __name__ == "__main__":
    main()
