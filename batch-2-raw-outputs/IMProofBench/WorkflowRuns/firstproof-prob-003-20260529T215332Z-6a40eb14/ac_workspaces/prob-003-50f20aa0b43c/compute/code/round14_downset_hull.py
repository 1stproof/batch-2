#!/usr/bin/env python3
"""Round 14 down-set convex-hull checks.

For a down-set D on [m], write

    r(D) = max { t : t*1 lies in conv(1_A : A in D) }.

Since D is a down-set, its convex hull is already coordinatewise down-closed.
Thus the proposed statement for a fixed p is:

    mu_p(D) > 1-p  =>  r(D) >= p.

This script exhaustively enumerates all down-sets for m <= 5 and computes r(D)
by a small LP.  It also records empirical slice-recursion diagnostics for the
state r(D), and runs a separate MILP search over separated threshold down-sets
for m=6.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from fractions import Fraction
from pathlib import Path
import json
import math

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, linprog, milp


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "round14"
DATA.mkdir(parents=True, exist_ok=True)


P_VALUES = [Fraction(1, 3), Fraction(3, 10), Fraction(1, 4), Fraction(1, 5)]


def fstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


_DOWNSET_CACHE: dict[int, list[int]] = {}


def all_downsets(m: int) -> list[int]:
    """Return down-sets as bitsets indexed by subset masks."""

    if m in _DOWNSET_CACHE:
        return _DOWNSET_CACHE[m]
    if m == 0:
        _DOWNSET_CACHE[m] = [0, 1]
        return _DOWNSET_CACHE[m]

    prev = all_downsets(m - 1)
    half = 1 << (m - 1)
    out: list[int] = []
    for d0 in prev:
        for d1 in prev:
            if d1 & ~d0:
                continue
            fam = 0
            for base in range(half):
                if (d0 >> base) & 1:
                    fam |= 1 << base
                if (d1 >> base) & 1:
                    fam |= 1 << (base | half)
            out.append(fam)
    _DOWNSET_CACHE[m] = out
    return out


def slices(fam: int, m: int) -> tuple[int, int]:
    """Return (D0,D1) on [m-1] for the last coordinate."""

    half = 1 << (m - 1)
    d0 = 0
    d1 = 0
    for base in range(half):
        if (fam >> base) & 1:
            d0 |= 1 << base
        if (fam >> (base | half)) & 1:
            d1 |= 1 << base
    return d0, d1


def mu_value(fam: int, m: int, p: Fraction) -> Fraction:
    q = 1 - p
    total = Fraction(0)
    for mask in range(1 << m):
        if (fam >> mask) & 1:
            k = mask.bit_count()
            total += (p**k) * (q ** (m - k))
    return total


def maximal_members(fam: int, m: int) -> list[tuple[int, ...]]:
    out: list[tuple[int, ...]] = []
    for mask in range(1 << m):
        if not ((fam >> mask) & 1):
            continue
        is_max = True
        for i in range(m):
            if not ((mask >> i) & 1) and ((fam >> (mask | (1 << i))) & 1):
                is_max = False
                break
        if is_max:
            out.append(tuple(i + 1 for i in range(m) if (mask >> i) & 1))
    return out


def r_value(fam: int, m: int) -> float:
    """Primal LP for r(D)."""

    points = [mask for mask in range(1 << m) if (fam >> mask) & 1]
    if not points or m == 0:
        return 0.0
    n = len(points)
    c = np.zeros(n + 1)
    c[-1] = -1.0

    rows = []
    rhs = []
    for coord in range(m):
        row = np.zeros(n + 1)
        for j, mask in enumerate(points):
            row[j] = -float((mask >> coord) & 1)
        row[-1] = 1.0
        rows.append(row)
        rhs.append(0.0)

    eq = np.zeros((1, n + 1))
    eq[0, :n] = 1.0
    res = linprog(
        c,
        A_ub=np.array(rows),
        b_ub=np.array(rhs),
        A_eq=eq,
        b_eq=np.array([1.0]),
        bounds=[(0.0, None)] * n + [(0.0, 1.0)],
        method="highs",
    )
    if not res.success:
        raise RuntimeError(res.message)
    return float(res.x[-1])


def dual_separator(fam: int, m: int) -> tuple[float, list[float]]:
    """Return min_y max_{A in D} y(A), sum y_i=1, y>=0.

    This is the LP dual value r(D).  The y vector is a separating weight vector
    when the value is < p.
    """

    if m == 0:
        return 0.0, []
    points = [mask for mask in range(1 << m) if (fam >> mask) & 1]
    c = np.zeros(m + 1)
    c[-1] = 1.0
    rows = []
    rhs = []
    for mask in points:
        row = np.zeros(m + 1)
        for i in range(m):
            if (mask >> i) & 1:
                row[i] = 1.0
        row[-1] = -1.0
        rows.append(row)
        rhs.append(0.0)
    eq = np.zeros((1, m + 1))
    eq[0, :m] = 1.0
    res = linprog(
        c,
        A_ub=np.array(rows) if rows else None,
        b_ub=np.array(rhs) if rows else None,
        A_eq=eq,
        b_eq=np.array([1.0]),
        bounds=[(0.0, 1.0)] * m + [(0.0, 1.0)],
        method="highs",
    )
    if not res.success:
        raise RuntimeError(res.message)
    return float(res.x[-1]), [float(x) for x in res.x[:m]]


@dataclass
class BestRecord:
    m: int
    p: str
    mu: str
    mu_float: float
    r: float
    gap_to_target: str
    max_sets: list[tuple[int, ...]]
    separator_value: float | None = None
    separator_weights: list[float] | None = None


@dataclass
class ExhaustiveSummary:
    m: int
    downsets: int
    p: str
    premise_count: int
    violation_count: int
    max_mu_with_r_lt_p: BestRecord | None
    max_mu_with_0_lt_r_lt_p: BestRecord | None
    min_r_among_premise: BestRecord | None


def exhaustive(max_m: int = 5) -> tuple[list[ExhaustiveSummary], dict[int, dict[int, float]]]:
    summaries: list[ExhaustiveSummary] = []
    r_cache_by_m: dict[int, dict[int, float]] = {}
    for m in range(1, max_m + 1):
        ideals = all_downsets(m)
        r_cache = {fam: r_value(fam, m) for fam in ideals}
        r_cache_by_m[m] = r_cache
        for p in P_VALUES:
            target = 1 - p
            premise_count = 0
            violation_count = 0
            max_bad: BestRecord | None = None
            max_active_bad: BestRecord | None = None
            min_prem: BestRecord | None = None
            for fam in ideals:
                r = r_cache[fam]
                mu = mu_value(fam, m, p)
                if mu > target:
                    premise_count += 1
                    rec = BestRecord(
                        m=m,
                        p=fstr(p),
                        mu=fstr(mu),
                        mu_float=float(mu),
                        r=r,
                        gap_to_target=fstr(mu - target),
                        max_sets=maximal_members(fam, m),
                    )
                    if min_prem is None or r < min_prem.r - 1e-12:
                        min_prem = rec
                    if r < float(p) - 1e-10:
                        violation_count += 1
                if r < float(p) - 1e-10:
                    if max_bad is None or float(mu) > max_bad.mu_float + 1e-12:
                        val, sep = dual_separator(fam, m)
                        max_bad = BestRecord(
                            m=m,
                            p=fstr(p),
                            mu=fstr(mu),
                            mu_float=float(mu),
                            r=r,
                            gap_to_target=fstr(target - mu),
                            max_sets=maximal_members(fam, m),
                            separator_value=val,
                            separator_weights=sep,
                        )
                    if r > 1e-10 and (max_active_bad is None or float(mu) > max_active_bad.mu_float + 1e-12):
                        val, sep = dual_separator(fam, m)
                        max_active_bad = BestRecord(
                            m=m,
                            p=fstr(p),
                            mu=fstr(mu),
                            mu_float=float(mu),
                            r=r,
                            gap_to_target=fstr(target - mu),
                            max_sets=maximal_members(fam, m),
                            separator_value=val,
                            separator_weights=sep,
                        )
            summaries.append(
                ExhaustiveSummary(
                    m=m,
                    downsets=len(ideals),
                    p=fstr(p),
                    premise_count=premise_count,
                    violation_count=violation_count,
                    max_mu_with_r_lt_p=max_bad,
                    max_mu_with_0_lt_r_lt_p=max_active_bad,
                    min_r_among_premise=min_prem,
                )
            )
    return summaries, r_cache_by_m


def r_lower_from_slices(r0: float, r1: float) -> float:
    """Scalar lower bound from mixing the two slices."""

    if r0 <= 0.0:
        return 0.0
    return r0 / (1.0 + r0 - r1)


@dataclass
class SliceDiagnostic:
    m: int
    exact_failures_of_scalar_formula: int
    max_exact_minus_scalar: float
    example: dict[str, object] | None
    worst_needed_boost: dict[str, object] | None


def slice_diagnostics(r_cache_by_m: dict[int, dict[int, float]]) -> list[SliceDiagnostic]:
    out: list[SliceDiagnostic] = []
    for m in range(2, 6):
        count = 0
        max_diff = 0.0
        example = None
        worst_boost = None
        for fam in all_downsets(m):
            d0, d1 = slices(fam, m)
            r0 = r_cache_by_m[m - 1][d0]
            r1 = r_cache_by_m[m - 1][d1]
            scalar = r_lower_from_slices(r0, r1)
            exact = r_cache_by_m[m][fam]
            diff = exact - scalar
            if diff > 1e-9:
                count += 1
            if diff > max_diff + 1e-12:
                max_diff = diff
                example = {
                    "max_sets_D": maximal_members(fam, m),
                    "max_sets_D0": maximal_members(d0, m - 1),
                    "max_sets_D1": maximal_members(d1, m - 1),
                    "r_D": exact,
                    "r_D0": r0,
                    "r_D1": r1,
                    "scalar_lower": scalar,
                }
            # This records examples where D0 alone reaches 1/3 but D1 does not,
            # and the scalar lower bound remains below 1/3.
            if r0 >= 1 / 3 - 1e-10 and r1 < 1 / 3 - 1e-10 and scalar < 1 / 3 - 1e-10:
                boost = exact - scalar
                if worst_boost is None or boost > worst_boost["exact_minus_scalar"]:
                    worst_boost = {
                        "max_sets_D": maximal_members(fam, m),
                        "max_sets_D0": maximal_members(d0, m - 1),
                        "max_sets_D1": maximal_members(d1, m - 1),
                        "r_D": exact,
                        "r_D0": r0,
                        "r_D1": r1,
                        "scalar_lower": scalar,
                        "exact_minus_scalar": boost,
                    }
        out.append(
            SliceDiagnostic(
                m=m,
                exact_failures_of_scalar_formula=count,
                max_exact_minus_scalar=max_diff,
                example=example,
                worst_needed_boost=worst_boost,
            )
        )
    return out


@dataclass
class HalfspaceMilpResult:
    p: str
    m: int
    eps: float
    success: bool
    objective_light_mass: float | None
    target: float
    gap_target_minus_objective: float | None
    weights: list[float] | None
    light_sets: list[tuple[int, ...]] | None
    message: str


def separated_halfspace_milp(p_frac: Fraction, m: int, eps: float, time_limit: float = 60.0) -> HalfspaceMilpResult:
    """Maximize mu_p({A: y_A=1}) with y_A=1 => w(A) <= p-eps.

    This is a direct search for separated threshold down-sets on m coordinates.
    If a down-set counterexample exists with separator w and margin eps, this
    MILP finds at least as much measure by taking all subsets below the same
    halfspace threshold.
    """

    p = float(p_frac)
    q = 1.0 - p
    k = 1 << m
    nvars = m + k
    probs = np.array([(p ** mask.bit_count()) * (q ** (m - mask.bit_count())) for mask in range(k)])

    c = np.zeros(nvars)
    c[m:] = -probs

    lb = np.zeros(nvars)
    ub = np.ones(nvars)
    bounds = Bounds(lb, ub)
    integrality = np.zeros(nvars, dtype=int)
    integrality[m:] = 1

    rows = []
    lows = []
    ups = []
    big_m = m + 1.0
    for mask in range(k):
        row = np.zeros(nvars)
        for i in range(m):
            if (mask >> i) & 1:
                row[i] = 1.0
        row[m + mask] = big_m
        rows.append(row)
        lows.append(-np.inf)
        ups.append(p - eps + big_m)

    row = np.zeros(nvars)
    row[:m] = 1.0
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
    light_sets = None
    if res.fun is not None:
        obj = -float(res.fun)
    if res.x is not None:
        weights = [float(x) for x in res.x[:m]]
        light_sets = [
            tuple(i + 1 for i in range(m) if (mask >> i) & 1)
            for mask in range(k)
            if res.x[m + mask] > 0.5
        ]
    return HalfspaceMilpResult(
        p=fstr(p_frac),
        m=m,
        eps=eps,
        success=bool(res.success),
        objective_light_mass=obj,
        target=float(1 - p_frac),
        gap_target_minus_objective=None if obj is None else float(1 - p_frac) - obj,
        weights=weights,
        light_sets=light_sets,
        message=str(res.message),
    )


def main() -> None:
    summaries, r_cache_by_m = exhaustive(5)
    diagnostics = slice_diagnostics(r_cache_by_m)

    milp_results = []
    for p in P_VALUES:
        for eps in (1e-6,):
            milp_results.append(asdict(separated_halfspace_milp(p, 6, eps=eps, time_limit=60.0)))

    payload = {
        "p_values": [fstr(p) for p in P_VALUES],
        "exhaustive_summaries": [asdict(s) for s in summaries],
        "slice_diagnostics": [asdict(d) for d in diagnostics],
        "m6_separated_halfspace_milp": milp_results,
    }
    (DATA / "downset_hull_results.json").write_text(json.dumps(payload, indent=2) + "\n")

    lines: list[str] = []
    lines.append("# Round 14 down-set convex-hull enumeration")
    lines.append("")
    lines.append("Exhaustive LP enumeration was run for all down-sets on m<=5.")
    lines.append("")
    lines.append("| m | p | #downsets | # with mu_p(D)>1-p | violations | max mu_p(D) among r(D)<p | target gap | maximals |")
    lines.append("|---:|---:|---:|---:|---:|---:|---:|---|")
    for s in summaries:
        b = s.max_mu_with_r_lt_p
        lines.append(
            f"| {s.m} | {s.p} | {s.downsets} | {s.premise_count} | {s.violation_count} | "
            f"{b.mu_float:.12f} | {b.gap_to_target} | {b.max_sets} |"
        )

    lines.append("")
    lines.append("## Best separated examples with positive diagonal")
    lines.append("")
    lines.append("| m | p | max mu_p(D) with 0<r(D)<p | r(D) | target gap | maximals |")
    lines.append("|---:|---:|---:|---:|---:|---|")
    for s in summaries:
        b = s.max_mu_with_0_lt_r_lt_p
        if b is None:
            continue
        lines.append(f"| {s.m} | {s.p} | {b.mu_float:.12f} | {b.r:.12f} | {b.gap_to_target} | {b.max_sets} |")

    lines.append("")
    lines.append("## Minimum r(D) among premise families")
    lines.append("")
    lines.append("| m | p | min r with mu_p(D)>1-p | mu | maximals |")
    lines.append("|---:|---:|---:|---:|---|")
    for s in summaries:
        b = s.min_r_among_premise
        if b is None:
            continue
        lines.append(f"| {s.m} | {s.p} | {b.r:.12f} | {b.mu_float:.12f} | {b.max_sets} |")

    lines.append("")
    lines.append("## Slice r-state diagnostics")
    lines.append("")
    lines.append("The scalar slice lower bound used here is")
    lines.append("r(D) >= r(D0)/(1+r(D0)-r(D1)).")
    lines.append("")
    for d in diagnostics:
        lines.append(
            f"- m={d.m}: scalar formula not exact for {d.exact_failures_of_scalar_formula} down-sets; "
            f"largest exact-minus-scalar = {d.max_exact_minus_scalar:.12f}."
        )
        if d.worst_needed_boost is not None:
            w = d.worst_needed_boost
            lines.append(
                "  Example with r(D0)>=1/3, r(D1)<1/3, scalar<1/3: "
                f"rD={w['r_D']:.12f}, r0={w['r_D0']:.12f}, r1={w['r_D1']:.12f}, "
                f"scalar={w['scalar_lower']:.12f}, maxD={w['max_sets_D']}."
            )

    lines.append("")
    lines.append("## m=6 separated-halfspace MILP")
    lines.append("")
    lines.append("| p | eps | solver | max strict light mass | target 1-p | gap | weights |")
    lines.append("|---:|---:|---|---:|---:|---:|---|")
    for r in milp_results:
        obj = r["objective_light_mass"]
        gap = r["gap_target_minus_objective"]
        weights_s = None if r["weights"] is None else [round(x, 8) for x in r["weights"]]
        lines.append(
            f"| {r['p']} | {r['eps']:.0e} | {r['success']} | "
            f"{obj if obj is not None else math.nan:.12f} | {r['target']:.12f} | "
            f"{gap if gap is not None else math.nan:.12f} | {weights_s} |"
        )

    (DATA / "downset_hull_summary.md").write_text("\n".join(lines) + "\n")
    print(DATA / "downset_hull_summary.md")
    print(DATA / "downset_hull_results.json")


if __name__ == "__main__":
    main()
