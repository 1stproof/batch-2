#!/usr/bin/env python3
"""Computational checks for the homogeneous unit-gap inequality.

The scale h is normalized to 1.  For fixed p and n, the events in HUG are
constant on chambers cut out by the affine threshold hyperplanes

    sum_{i in A} b_i - p (sum_i b_i + 1) = 0
    sum_{i in A} b_i - p (sum_i b_i + 1) + 1 = 0.

The MILP below searches globally over these chambers with binary event
indicators.  Its default "closed" mode is a relaxation: the upper closed event
may be undercounted on its boundary, and the lower strict event may be
overcounted on its boundary.  Therefore a nonnegative relaxed optimum proves
HUG for that fixed (p,n).  A negative relaxed optimum is checked by direct
enumeration at the returned coefficient vector.
"""

from __future__ import annotations

import argparse
import itertools
import json
from dataclasses import asdict, dataclass
from fractions import Fraction
from functools import lru_cache
from math import comb
from pathlib import Path
from typing import Iterable

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp


@dataclass
class HugValue:
    p: float
    n: int
    b: list[float]
    upper: float
    lower: float
    rhs_factor: float
    diff: float


@dataclass
class MilpResult:
    p: float
    n: int
    eps: float
    success: bool
    status: int
    message: str
    relaxed_objective: float | None
    true_diff_at_solution: float | None
    true_upper_at_solution: float | None
    true_lower_at_solution: float | None
    b: list[float] | None


def masks(n: int) -> list[int]:
    return list(range(1 << n))


def popcount(x: int) -> int:
    return int(x.bit_count())


def mask_sum(mask: int, b: np.ndarray) -> float:
    s = 0.0
    i = 0
    while mask:
        if mask & 1:
            s += b[i]
        mask >>= 1
        i += 1
    return s


def probabilities_by_mask(n: int, p: float) -> np.ndarray:
    q = 1.0 - p
    return np.array([(p ** popcount(m)) * (q ** (n - popcount(m))) for m in masks(n)])


@lru_cache(maxsize=None)
def incidence_matrix(n: int) -> np.ndarray:
    mat = np.zeros((1 << n, n), dtype=float)
    for m in masks(n):
        for i in range(n):
            if (m >> i) & 1:
                mat[m, i] = 1.0
    return mat


def hug_value(p: float, b: Iterable[float], tol: float = 1e-12) -> HugValue:
    b_arr = np.array(list(b), dtype=float)
    n = len(b_arr)
    probs = probabilities_by_mask(n, p)
    B = float(np.sum(b_arr))
    upper_threshold = p * (B + 1.0)
    lower_threshold = upper_threshold - 1.0
    sums = incidence_matrix(n) @ b_arr
    upper = float(np.sum(probs[sums >= upper_threshold - tol]))
    lower = float(np.sum(probs[sums < lower_threshold - tol]))
    factor = p / (1.0 - p)
    return HugValue(p=p, n=n, b=[float(x) for x in b_arr], upper=upper, lower=lower, rhs_factor=factor, diff=upper - factor * lower)


def hug_value_fraction(p: Fraction, b: list[Fraction]) -> dict[str, str]:
    n = len(b)
    q = 1 - p
    B = sum(b, Fraction(0))
    upper_threshold = p * (B + 1)
    lower_threshold = upper_threshold - 1
    upper = Fraction(0)
    lower = Fraction(0)
    for m in masks(n):
        s = sum((b[i] for i in range(n) if (m >> i) & 1), Fraction(0))
        pr = (p ** popcount(m)) * (q ** (n - popcount(m)))
        if s >= upper_threshold:
            upper += pr
        if s < lower_threshold:
            lower += pr
    diff = upper - (p / q) * lower
    return {
        "p": str(p),
        "n": str(n),
        "b": [str(x) for x in b],
        "upper": str(upper),
        "lower": str(lower),
        "rhs_factor": str(p / q),
        "diff": str(diff),
        "upper_float": f"{float(upper):.17g}",
        "lower_float": f"{float(lower):.17g}",
        "diff_float": f"{float(diff):.17g}",
    }


def milp_relaxed(
    p: float,
    n: int,
    eps: float = 0.0,
    time_limit: float = 60.0,
    force_first_one: bool = False,
) -> MilpResult:
    """Minimize the relaxed chamber objective for fixed p,n.

    Variables are b_i, z_A, y_A.  z_A marks the upper event and y_A marks the
    lower event.  With eps=0 this is a closed-boundary relaxation.  With eps>0,
    it searches only chambers with at least eps slack on the forced side.
    """

    ms = masks(n)
    k = len(ms)
    nb = n
    nz0 = nb
    ny0 = nb + k
    total = nb + 2 * k
    probs = probabilities_by_mask(n, p)
    factor = p / (1.0 - p)

    c = np.zeros(total)
    c[nz0 : nz0 + k] = probs
    c[ny0 : ny0 + k] = -factor * probs

    lb = np.zeros(total)
    ub = np.ones(total)
    bounds = Bounds(lb, ub)
    integrality = np.zeros(total, dtype=int)
    integrality[nz0:] = 1

    rows = []
    lows = []
    ups = []
    big_m = n + 2.0
    for j, m in enumerate(ms):
        coeff = np.zeros(total)
        for i in range(n):
            coeff[i] = (1.0 if ((m >> i) & 1) else 0.0) - p
        # u = coeff*b - p.  Constraint u <= -eps + M z.
        # coeff*b - M z <= p - eps.
        coeff[nz0 + j] = -big_m
        rows.append(coeff)
        lows.append(-np.inf)
        ups.append(p - eps)

        coeff2 = np.zeros(total)
        for i in range(n):
            coeff2[i] = (1.0 if ((m >> i) & 1) else 0.0) - p
        # v = u + 1 = coeff*b + (1-p).  Constraint y=1 => v <= -eps:
        # v <= -eps + M(1-y), so coeff*b + M y <= M - (1-p) - eps.
        coeff2[ny0 + j] = big_m
        rows.append(coeff2)
        lows.append(-np.inf)
        ups.append(big_m - (1.0 - p) - eps)

    if force_first_one:
        coeff = np.zeros(total)
        coeff[0] = 1.0
        rows.append(coeff)
        lows.append(1.0)
        ups.append(1.0)

    constraints = LinearConstraint(np.vstack(rows), np.array(lows), np.array(ups))
    res = milp(c=c, integrality=integrality, bounds=bounds, constraints=constraints, options={"time_limit": time_limit})

    b = None
    true = None
    if res.x is not None:
        b = [float(x) for x in res.x[:n]]
        true = hug_value(p, b)
    return MilpResult(
        p=p,
        n=n,
        eps=eps,
        success=bool(res.success),
        status=int(res.status),
        message=str(res.message),
        relaxed_objective=None if res.fun is None else float(res.fun),
        true_diff_at_solution=None if true is None else true.diff,
        true_upper_at_solution=None if true is None else true.upper,
        true_lower_at_solution=None if true is None else true.lower,
        b=b,
    )


def random_search(p_values: list[float], n_max: int, trials: int, seed: int) -> list[HugValue]:
    rng = np.random.default_rng(seed)
    best: dict[tuple[float, int], HugValue] = {}
    for p in p_values:
        for n in range(1, n_max + 1):
            candidates = []
            candidates.append(np.ones(n))
            candidates.append(np.zeros(n))
            for k in range(1, n + 1):
                v = np.zeros(n)
                v[:k] = 1.0
                candidates.append(v)
            for _ in range(trials):
                r = rng.random(n)
                candidates.append(r)
                # Edge-biased beta draws probe near coefficient caps.
                candidates.append(rng.beta(0.25, 0.25, size=n))
            vals = [hug_value(p, b) for b in candidates]
            best[(p, n)] = min(vals, key=lambda x: x.diff)
    return [best[key] for key in sorted(best)]


def binomial_equal_coeff_summary(p_values: list[float], n_max: int) -> list[dict[str, float]]:
    out = []
    for p in p_values:
        factor = p / (1.0 - p)
        for n in range(1, n_max + 1):
            b = np.ones(n)
            val = hug_value(p, b)
            out.append({"p": p, "n": n, "diff": val.diff, "upper": val.upper, "lower": val.lower, "factor": factor})
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="data/hug_results.json")
    parser.add_argument("--trials", type=int, default=20000)
    parser.add_argument("--n-random", type=int, default=9)
    parser.add_argument("--n-milp", type=int, default=6)
    parser.add_argument("--time-limit", type=float, default=60.0)
    args = parser.parse_args()

    p_values = [1 / 6, 0.2, 0.25, 0.3, 1 / 3, 0.34, 0.36, 0.4, 0.45]
    random_best = random_search(p_values, args.n_random, args.trials, seed=20260530)

    milp_ps = [1 / 6, 0.2, 0.25, 0.3, 1 / 3, 0.34, 0.36, 0.4]
    milp_results = []
    for p, n in itertools.product(milp_ps, range(1, args.n_milp + 1)):
        milp_results.append(milp_relaxed(p, n, eps=0.0, time_limit=args.time_limit))

    exact_examples = {
        "p_2_5_b_1_1_counterexample": hug_value_fraction(Fraction(2, 5), [Fraction(1), Fraction(1)]),
        "p_1_3_b_1_1_endpoint": hug_value_fraction(Fraction(1, 3), [Fraction(1), Fraction(1)]),
        "p_3_10_b_1_1_safe": hug_value_fraction(Fraction(3, 10), [Fraction(1), Fraction(1)]),
    }

    payload = {
        "random_trials_per_n_p": args.trials,
        "random_best": [asdict(x) for x in random_best],
        "milp_relaxed": [asdict(x) for x in milp_results],
        "equal_coefficients": binomial_equal_coeff_summary(p_values, args.n_random),
        "exact_examples": exact_examples,
    }
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


if __name__ == "__main__":
    main()
