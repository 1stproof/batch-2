"""Round 3 computations for the cap-vector conjecture.

The conjecture checked here is

    p in [1/4,1/3], sum w_i = 1, 0 <= w_i < p
        => P_p[sum w_i v_i >= p] >= g4(p) = P[Bin(4,p) >= 2].

The script deliberately uses several different formulations:

* direct random/hit-and-run search over the capped simplex;
* chamber enumeration by feasible down-sets for m <= 5;
* a mixed-integer separation model for fixed m that maximizes the failing
  p-biased mass among subsets whose weight is forced below p.

The computations are numerical, but the extremal structures they find are
simple and reproducible.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from math import comb
from pathlib import Path

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, differential_evolution, linprog, milp
from scipy.sparse import lil_matrix


OUT = Path("data/round3_cap_vector_output.txt")


def g4(p: float) -> float:
    return 6 * p * p * (1 - p) ** 2 + 4 * p**3 * (1 - p) + p**4


def subset_data(n: int, p: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    masks = np.arange(1 << n, dtype=np.int64)
    inc = ((masks[:, None] >> np.arange(n)) & 1).astype(float)
    sizes = inc.sum(axis=1).astype(int)
    probs = (p**sizes) * ((1 - p) ** (n - sizes))
    return masks, inc, probs


def tail_prob(weights: np.ndarray, p: float) -> float:
    _, inc, probs = subset_data(len(weights), p)
    sums = inc @ np.asarray(weights, dtype=float)
    return float(probs[sums >= p - 1e-12].sum())


def capped_sample(n: int, p: float, rng: np.random.Generator) -> np.ndarray:
    """Rejection sample from a Dirichlet distribution, biased toward caps."""

    if n * p <= 1:
        raise ValueError("empty strict capped simplex")
    for alpha in (0.25, 0.5, 1.0, 2.0, 5.0):
        for _ in range(2000):
            w = rng.dirichlet(np.full(n, alpha))
            if np.max(w) < p:
                return w
    # Fallback: start from equal weights, which is feasible when n*p > 1.
    return np.full(n, 1.0 / n)


def hit_and_run_min(p: float, n: int, seed: int, steps: int = 50000) -> tuple[float, np.ndarray]:
    rng = np.random.default_rng(seed)
    w = capped_sample(n, p, rng)
    best_w = w.copy()
    best = tail_prob(w, p)
    for _ in range(steps):
        d = rng.normal(size=n)
        d -= d.mean()
        norm = np.linalg.norm(d)
        if norm == 0:
            continue
        d /= norm
        lo = -np.inf
        hi = np.inf
        for wi, di in zip(w, d):
            if abs(di) < 1e-15:
                continue
            if di > 0:
                lo = max(lo, -wi / di)
                hi = min(hi, (p - 1e-10 - wi) / di)
            else:
                lo = max(lo, (p - 1e-10 - wi) / di)
                hi = min(hi, -wi / di)
        if lo <= hi:
            w = w + rng.uniform(lo, hi) * d
            val = tail_prob(w, p)
            if val < best - 1e-14:
                best = val
                best_w = w.copy()
    return best, np.sort(best_w)[::-1]


def softmax(y: np.ndarray) -> np.ndarray:
    z = y - np.max(y)
    e = np.exp(z)
    return e / e.sum()


def de_min(p: float, n: int, seed: int) -> tuple[float, np.ndarray]:
    """Discontinuous differential-evolution search with a cap penalty."""

    def obj(y: np.ndarray) -> float:
        w = softmax(np.asarray(y))
        excess = np.max(w) - (p - 1e-10)
        if excess > 0:
            return 2.0 + 100.0 * excess
        return tail_prob(w, p)

    res = differential_evolution(
        obj,
        [(-12, 12)] * n,
        seed=seed,
        maxiter=350,
        popsize=10,
        tol=1e-8,
        polish=False,
        workers=1,
    )
    w = softmax(np.asarray(res.x))
    if np.max(w) >= p:
        # The optimizer sometimes parks just outside the cap near discontinuities.
        return float("nan"), np.sort(w)[::-1]
    return tail_prob(w, p), np.sort(w)[::-1]


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


def family_measure(fam: int, m: int, p: float) -> float:
    total = 0.0
    for mask in range(1 << m):
        if (fam >> mask) & 1:
            k = mask.bit_count()
            total += p**k * (1 - p) ** (m - k)
    return total


def maximal_members(fam: int, m: int) -> list[tuple[int, ...]]:
    ans = []
    for mask in range(1 << m):
        if not ((fam >> mask) & 1):
            continue
        is_max = True
        for i in range(m):
            if not ((mask >> i) & 1) and ((fam >> (mask | (1 << i))) & 1):
                is_max = False
                break
        if is_max:
            ans.append(tuple(i + 1 for i in range(m) if (mask >> i) & 1))
    return ans


def cap_threshold_margin(fam: int, m: int, p: float) -> float | None:
    """Return the largest strict margin for D={A:w(A)<p}; None if infeasible."""

    rows_ub = []
    rhs_ub = []
    # For each A in D: sum_A w + t <= p.
    for mask in range(1 << m):
        if (fam >> mask) & 1:
            row = np.zeros(m + 1)
            for i in range(m):
                if (mask >> i) & 1:
                    row[i] = 1.0
            row[-1] = 1.0
            rows_ub.append(row)
            rhs_ub.append(p)
        else:
            # For each A not in D: sum_A w >= p.
            row = np.zeros(m + 1)
            for i in range(m):
                if (mask >> i) & 1:
                    row[i] = -1.0
            rows_ub.append(row)
            rhs_ub.append(-p)
    # Cap: w_i + t <= p.
    for i in range(m):
        row = np.zeros(m + 1)
        row[i] = 1.0
        row[-1] = 1.0
        rows_ub.append(row)
        rhs_ub.append(p)

    a_eq = np.zeros((1, m + 1))
    a_eq[0, :m] = 1.0
    bounds = [(0.0, None)] * m + [(0.0, None)]
    res = linprog(
        c=np.array([0.0] * m + [-1.0]),
        A_ub=np.array(rows_ub),
        b_ub=np.array(rhs_ub),
        A_eq=a_eq,
        b_eq=np.array([1.0]),
        bounds=bounds,
        method="highs",
    )
    if not res.success:
        return None
    return float(res.x[-1])


@dataclass
class ChamberResult:
    m: int
    p: float
    tail: float
    fam: int
    margin: float
    count_feasible: int


def chamber_min(m: int, p: float) -> ChamberResult | None:
    best: ChamberResult | None = None
    count = 0
    for fam in all_downsets(m):
        margin = cap_threshold_margin(fam, m, p)
        if margin is None or margin <= 1e-9:
            continue
        count += 1
        fail = family_measure(fam, m, p)
        tail = 1.0 - fail
        if best is None or tail < best.tail - 1e-12:
            best = ChamberResult(m, p, tail, fam, margin, count)
    if best is not None:
        best.count_feasible = count
    return best


def milp_fail_mass(n: int, p: float, eps: float = 1e-7, time_limit: float = 60.0):
    """Maximize p-biased mass forced below p by capped weights.

    Binary x_A may be 1 only if sum_{i in A} w_i <= p-eps.  Maximizing the
    p-biased mass of x_A is a direct separation search for a counterexample.
    """

    masks, inc, probs = subset_data(n, p)
    n_sub = len(masks)
    n_var = n + n_sub
    c = np.zeros(n_var)
    c[n:] = -probs

    rows = 1 + n_sub
    a = lil_matrix((rows, n_var), dtype=float)
    lb = np.full(rows, -np.inf)
    ub = np.full(rows, np.inf)

    # sum_i w_i = 1
    a[0, :n] = 1.0
    lb[0] = 1.0
    ub[0] = 1.0

    big_m = 1.0
    for r, mask in enumerate(masks, start=1):
        for i in range(n):
            if (int(mask) >> i) & 1:
                a[r, i] = 1.0
        a[r, n + r - 1] = big_m
        ub[r] = p - eps + big_m

    bounds = Bounds(
        np.concatenate([np.zeros(n), np.zeros(n_sub)]),
        np.concatenate([np.full(n, p - eps), np.ones(n_sub)]),
    )
    integrality = np.concatenate([np.zeros(n, dtype=int), np.ones(n_sub, dtype=int)])
    constraints = LinearConstraint(a.tocsr(), lb, ub)
    res = milp(
        c=c,
        integrality=integrality,
        bounds=bounds,
        constraints=constraints,
        options={"time_limit": time_limit, "mip_rel_gap": 1e-9, "disp": False},
    )
    if not res.success:
        return res, None, None
    fail = -float(res.fun)
    weights = np.asarray(res.x[:n])
    return res, fail, np.sort(weights)[::-1]


def rank_le_one_tail(m: int, p: float) -> float:
    return 1.0 - ((1 - p) ** m + m * p * (1 - p) ** (m - 1))


def cap_vector_weights(p: float, eps: float = 1e-5) -> np.ndarray:
    return np.array([p - eps, p - eps, p - eps, 1 - 3 * p + 3 * eps])


def main() -> None:
    p_values = [0.25, 0.26, 0.275, 2 / 7, 0.3, 0.32, 1 / 3]
    lines: list[str] = []
    lines.append("Round 3 cap-vector conjecture computations")
    lines.append("")
    lines.append("g4(p)=P[Bin(4,p)>=2]")
    for p in p_values:
        lines.append(f"p={p:.12f} g4={g4(p):.12f} gap_g4_minus_p={g4(p)-p:.12f}")
    lines.append("")

    lines.append("1. Explicit cap-vector family")
    for p in p_values:
        if p > 0.25:
            eps = min(1e-5, (4 * p - 1) / 10)
            w = cap_vector_weights(p, eps)
            lines.append(
                f"p={p:.12f} eps={eps:.3g} weights={np.round(w, 10).tolist()} "
                f"tail={tail_prob(w, p):.12f} g4={g4(p):.12f}"
            )
        else:
            lines.append(
                f"p={p:.12f} four-coordinate cap vector is infeasible under strict w_i<p; "
                f"rank<=1 on five coordinates has tail={rank_le_one_tail(5, p):.12f}"
            )
    lines.append("")

    lines.append("2. Nonlinear searches over capped simplex")
    for p in p_values:
        for n in range(max(2, int(np.floor(1 / p)) + 1), 10):
            hr_val, hr_w = hit_and_run_min(p, n, seed=2000 + n + int(10000 * p), steps=18000)
            de_val, de_w = de_min(p, n, seed=5000 + n + int(10000 * p))
            best_val, best_w, method = (hr_val, hr_w, "hitrun")
            if np.isfinite(de_val) and de_val < best_val:
                best_val, best_w, method = de_val, de_w, "de"
            lines.append(
                f"p={p:.12f} n={n:2d} best_{method}={best_val:.12f} "
                f"minus_g4={best_val-g4(p):.12f} weights={np.round(best_w, 6).tolist()}"
            )
        lines.append("")

    lines.append("3. Chamber/down-set enumeration for m<=5")
    for p in p_values:
        for m in range(1, 6):
            res = chamber_min(m, p)
            if res is None:
                lines.append(f"p={p:.12f} m={m} no strict-cap threshold chambers")
                continue
            lines.append(
                f"p={p:.12f} m={m} feasible={res.count_feasible:4d} "
                f"min_tail={res.tail:.12f} minus_g4={res.tail-g4(p):.12f} "
                f"margin={res.margin:.3g} maxD={maximal_members(res.fam,m)}"
            )
        lines.append("")

    lines.append("4. MILP/separation search")
    for p in p_values:
        for n in range(max(4, int(np.floor(1 / p)) + 1), 11):
            res, fail, w = milp_fail_mass(n, p, eps=1e-7, time_limit=45.0)
            if fail is None:
                lines.append(f"p={p:.12f} n={n:2d} MILP status={res.message}")
                continue
            tail = 1.0 - fail
            lines.append(
                f"p={p:.12f} n={n:2d} milp_tail={tail:.12f} "
                f"minus_g4={tail-g4(p):.12f} weights={np.round(w, 7).tolist()} "
                f"nodes={getattr(res, 'mip_node_count', 'na')} gap={getattr(res, 'mip_gap', 'na')}"
            )
        lines.append("")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines) + "\n")
    print(OUT)


if __name__ == "__main__":
    main()
