"""Round 3 down-set partition-function computations.

For lambda=p/(1-p) <= 1/2, the target is

    p*1 notin P(D)  =>  Z_lambda(D) <= (1+lambda)^(m-1).

This script enumerates all down-sets for m <= 5, computes

    T(D) = sup { t : t*1 in P(D) },

and records the extremal partition-function values.  The LP for T(D) uses the
down-closed form: t*1 in P(D) iff there is x in P(D) with all coordinates >= t.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.optimize import linprog


OUT = Path("data/round3_downset_partition_output.txt")
CSV = Path("data/round3_downset_partition_extrema.csv")


_DOWNSET_CACHE: dict[int, list[int]] = {}


def all_downsets(m: int) -> list[int]:
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


def z_value(fam: int, m: int, lam: float) -> float:
    total = 0.0
    for mask in range(1 << m):
        if (fam >> mask) & 1:
            total += lam ** mask.bit_count()
    return total


def t_value(fam: int, m: int) -> float:
    points = [mask for mask in range(1 << m) if (fam >> mask) & 1]
    if not points:
        return 0.0
    n = len(points)
    # Variables are probabilities on points, followed by t.  Maximize t.
    c = np.zeros(n + 1)
    c[-1] = -1.0

    rows_ub = []
    rhs_ub = []
    for coord in range(m):
        row = np.zeros(n + 1)
        for j, mask in enumerate(points):
            row[j] = -float((mask >> coord) & 1)
        row[-1] = 1.0
        rows_ub.append(row)
        rhs_ub.append(0.0)

    a_eq = np.zeros((1, n + 1))
    a_eq[0, :n] = 1.0
    bounds = [(0.0, None)] * n + [(0.0, 1.0)]
    res = linprog(
        c=c,
        A_ub=np.array(rows_ub),
        b_ub=np.array(rhs_ub),
        A_eq=a_eq,
        b_eq=np.array([1.0]),
        bounds=bounds,
        method="highs",
    )
    if not res.success:
        raise RuntimeError(res.message)
    return float(res.x[-1])


def maximal_members(fam: int, m: int) -> list[tuple[int, ...]]:
    out = []
    for mask in range(1 << m):
        if not ((fam >> mask) & 1):
            continue
        maximal = True
        for i in range(m):
            if not ((mask >> i) & 1) and ((fam >> (mask | (1 << i))) & 1):
                maximal = False
                break
        if maximal:
            out.append(tuple(i + 1 for i in range(m) if (mask >> i) & 1))
    return out


def is_dictatorship(fam: int, m: int) -> bool:
    for forbidden in range(m):
        target = 0
        for mask in range(1 << m):
            if not ((mask >> forbidden) & 1):
                target |= 1 << mask
        if fam == target:
            return True
    return False


@dataclass
class Record:
    m: int
    p: float
    lam: float
    fam: int
    t: float
    z: float
    ratio: float
    mu: float
    maximal: list[tuple[int, ...]]
    dictatorship: bool


def analyze(max_m: int, p_values: list[float]) -> tuple[list[str], list[Record]]:
    lines: list[str] = []
    records: list[Record] = []
    lines.append("Round 3 down-set partition-function enumeration")
    lines.append("")
    for m in range(1, max_m + 1):
        ideals = all_downsets(m)
        t_cache = {fam: t_value(fam, m) for fam in ideals}
        lines.append(f"m={m}: enumerated {len(ideals)} down-sets")
        for p in p_values:
            lam = p / (1 - p)
            bound = (1 + lam) ** (m - 1)
            target_mu = 1.0 / (1.0 + lam)
            considered: list[Record] = []
            violations: list[Record] = []
            equalities: list[Record] = []
            best: Record | None = None
            best_nondict: Record | None = None
            best_positive_t: Record | None = None
            best_positive_mu: Record | None = None
            slope_min = float("inf")
            slope_rec: Record | None = None
            for fam in ideals:
                t = t_cache[fam]
                if t >= p - 1e-10:
                    continue
                z = z_value(fam, m, lam)
                ratio = z / bound
                mu = z / ((1 + lam) ** m)
                rec = Record(
                    m=m,
                    p=p,
                    lam=lam,
                    fam=fam,
                    t=t,
                    z=z,
                    ratio=ratio,
                    mu=mu,
                    maximal=maximal_members(fam, m),
                    dictatorship=is_dictatorship(fam, m),
                )
                considered.append(rec)
                records.append(rec)
                if ratio > 1 + 1e-9:
                    violations.append(rec)
                if abs(ratio - 1.0) <= 1e-9:
                    equalities.append(rec)
                if best is None or ratio > best.ratio + 1e-12:
                    best = rec
                if not rec.dictatorship and (best_nondict is None or ratio > best_nondict.ratio + 1e-12):
                    best_nondict = rec
                if t > 1e-10 and (best_positive_t is None or ratio > best_positive_t.ratio + 1e-12):
                    best_positive_t = rec
                if t > 1e-10 and (best_positive_mu is None or mu > best_positive_mu.mu + 1e-12):
                    best_positive_mu = rec
                if t > 1e-10:
                    slope = (target_mu - mu) / t
                    if slope < slope_min:
                        slope_min = slope
                        slope_rec = rec

            lines.append(
                f"  p={p:.12f} lambda={lam:.12f}: considered(T<p)={len(considered)} "
                f"violations={len(violations)} equalities={len(equalities)}"
            )
            if best is not None:
                lines.append(
                    f"    best ratio={best.ratio:.12f} T={best.t:.12f} "
                    f"dict={best.dictatorship} maxD={best.maximal}"
                )
            if best_nondict is not None:
                lines.append(
                    f"    best non-dict ratio={best_nondict.ratio:.12f} "
                    f"T={best_nondict.t:.12f} mu={best_nondict.mu:.12f} "
                    f"maxD={best_nondict.maximal}"
                )
            if best_positive_t is not None:
                lines.append(
                    f"    best T>0 ratio={best_positive_t.ratio:.12f} "
                    f"T={best_positive_t.t:.12f} mu={best_positive_t.mu:.12f} "
                    f"maxD={best_positive_t.maximal}"
                )
            if best_positive_mu is not None:
                g4 = 6 * p * p * (1 - p) ** 2 + 4 * p**3 * (1 - p) + p**4
                lines.append(
                    f"    cap-style positive-T check: max_mu={best_positive_mu.mu:.12f} "
                    f"1-g4={1-g4:.12f} gap={(1-g4)-best_positive_mu.mu:.12f} "
                    f"T={best_positive_mu.t:.12f} maxD={best_positive_mu.maximal}"
                )
            if slope_rec is not None:
                lines.append(
                    f"    weakest linear drop (mu_target-mu)/T={slope_min:.12f} "
                    f"at T={slope_rec.t:.12f}, ratio={slope_rec.ratio:.12f}, "
                    f"maxD={slope_rec.maximal}"
                )
        lines.append("")
    return lines, records


def write_csv(records: list[Record]) -> None:
    rows = [
        "m,p,lambda,fam,T,Z,ratio,mu,dictatorship,maximal",
    ]
    for r in records:
        rows.append(
            f"{r.m},{r.p:.12g},{r.lam:.12g},{r.fam},{r.t:.12g},{r.z:.12g},"
            f"{r.ratio:.12g},{r.mu:.12g},{int(r.dictatorship)},\"{r.maximal}\""
        )
    CSV.write_text("\n".join(rows) + "\n")


def main() -> None:
    p_values = [0.25, 2 / 7, 0.3, 1 / 3]
    lines, records = analyze(5, p_values)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines) + "\n")
    write_csv(records)
    print(OUT)
    print(CSV)


if __name__ == "__main__":
    main()
