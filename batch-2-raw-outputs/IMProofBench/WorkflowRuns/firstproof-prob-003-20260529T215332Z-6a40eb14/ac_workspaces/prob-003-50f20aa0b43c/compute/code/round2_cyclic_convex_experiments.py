"""Round 2 experiments for the small-p Bernoulli problem.

The script keeps the computations intentionally small and reproducible:

* deterministic cyclic-interval strengthening checks by linear programming;
* exact weighted Bernoulli tail values for selected rational p and small supports;
* heuristic minimization over the simplex for small n;
* brute force verification of the finite downset/convex-hull formulation for
  m <= 5.

All inequalities here are numerical experiments, not proof certificates.
"""

from __future__ import annotations

from itertools import combinations, product
from math import comb
from pathlib import Path

import numpy as np
from scipy.optimize import differential_evolution, linprog, minimize


OUT = Path("data/round2_cyclic_convex_experiments.txt")


def interval_indices(b: int, a: int, start: int) -> list[int]:
    return [(start + k) % b for k in range(a)]


def cyclic_interval_sums(loads: np.ndarray, a: int) -> np.ndarray:
    b = len(loads)
    return np.array([sum(loads[(j + k) % b] for k in range(a)) for j in range(b)])


def deterministic_cyclic_failure(b: int, a: int, eps: float = 1e-6):
    """Find loads with fewer than a good cyclic a-intervals, if possible.

    Good means interval load >= a/b.  To avoid floating-point ambiguity, the
    LP enforces at least b-a+1 named intervals to have load <= a/b - eps.
    """

    threshold = a / b
    needed_bad = b - a + 1
    for bad in combinations(range(b), needed_bad):
        rows = []
        rhs = []
        for j in bad:
            row = np.zeros(b)
            for i in interval_indices(b, a, j):
                row[i] = 1.0
            rows.append(row)
            rhs.append(threshold - eps)
        res = linprog(
            c=np.zeros(b),
            A_ub=np.array(rows),
            b_ub=np.array(rhs),
            A_eq=np.ones((1, b)),
            b_eq=[1],
            bounds=[(0, None)] * b,
            method="highs",
        )
        if res.success:
            sums = cyclic_interval_sums(res.x, a)
            good = int(np.sum(sums >= threshold - 1e-9))
            return bad, res.x, sums, good
    return None


def uniform_subset_count(loads: list[float], a: int) -> int:
    threshold = a / len(loads)
    count = 0
    for subset in combinations(range(len(loads)), a):
        if sum(loads[i] for i in subset) >= threshold - 1e-12:
            count += 1
    return count


def bernoulli_tail_exact(weights: np.ndarray, p: float) -> float:
    n = len(weights)
    ans = 0.0
    for mask in range(1 << n):
        s = 0.0
        k = 0
        for i, w in enumerate(weights):
            if (mask >> i) & 1:
                s += w
                k += 1
        if s >= p - 1e-12:
            ans += (p**k) * ((1 - p) ** (n - k))
    return ans


def softmax(y: np.ndarray) -> np.ndarray:
    z = y - np.max(y)
    e = np.exp(z)
    return e / e.sum()


def minimize_tail(p: float, n: int, seed: int) -> tuple[float, np.ndarray]:
    """Heuristic global search on n-point simplex."""

    def obj(y):
        return bernoulli_tail_exact(softmax(np.asarray(y)), p)

    res = differential_evolution(
        obj,
        [(-10, 10)] * n,
        seed=seed,
        maxiter=250,
        popsize=8,
        tol=1e-8,
        polish=False,
        workers=1,
    )
    loc = minimize(obj, res.x, method="Nelder-Mead", options={"maxiter": 3000})
    y = loc.x if loc.success and loc.fun <= res.fun else res.x
    w = softmax(np.asarray(y))
    return bernoulli_tail_exact(w, p), np.sort(w)[::-1]


_DOWNSET_CACHE: dict[int, list[int]] = {}


def all_downsets(m: int) -> list[int]:
    """Enumerate downsets of 2^[m] as bitmasks over subset masks.

    A family mask has bit A set iff A belongs to the downset.  The recursion
    uses sections at the last coordinate: a downset is a pair D1 subset D0 of
    downsets in dimension m-1.
    """

    if m in _DOWNSET_CACHE:
        return _DOWNSET_CACHE[m]
    if m == 0:
        _DOWNSET_CACHE[m] = [0, 1]
        return _DOWNSET_CACHE[m]

    prev = all_downsets(m - 1)
    half = 1 << (m - 1)
    ideals = []
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
            ideals.append(fam)
    _DOWNSET_CACHE[m] = ideals
    return ideals


def biased_measure(fam: int, m: int, p: float) -> float:
    total = 0.0
    for a in range(1 << m):
        if (fam >> a) & 1:
            k = a.bit_count()
            total += (p**k) * ((1 - p) ** (m - k))
    return total


def contains_diagonal(fam: int, m: int, p: float) -> bool:
    points = [a for a in range(1 << m) if (fam >> a) & 1]
    n = len(points)
    if n == 0:
        return False
    a_eq = [np.ones(n)]
    b_eq = [1.0]
    for coord in range(m):
        a_eq.append(np.array([(mask >> coord) & 1 for mask in points], dtype=float))
        b_eq.append(p)
    res = linprog(
        c=np.zeros(n),
        A_eq=np.array(a_eq),
        b_eq=np.array(b_eq),
        bounds=[(0, None)] * n,
        method="highs",
    )
    return bool(res.success)


def check_downsets(max_m: int, p_values: list[float]) -> list[str]:
    lines = []
    for m in range(1, max_m + 1):
        ideals = all_downsets(m)
        for p in p_values:
            active = 0
            bad = []
            margin = 0.0
            for fam in ideals:
                mu = biased_measure(fam, m, p)
                if mu > 1 - p + 1e-10:
                    active += 1
                    margin = max(margin, mu - (1 - p))
                    if not contains_diagonal(fam, m, p):
                        bad.append((fam, mu))
                        break
            status = "ok" if not bad else f"COUNTEREXAMPLE fam={bad[0][0]} mu={bad[0][1]:.12f}"
            lines.append(
                f"m={m} p={p:.9f} downsets={len(ideals)} active={active} "
                f"max_margin={margin:.6g} {status}"
            )
    return lines


def main() -> None:
    lines = []

    lines.append("CAS availability was checked outside this script; scipy linprog was used here.")
    lines.append("")
    lines.append("1. Deterministic cyclic interval strengthening")
    first_fail = None
    for b in range(3, 19):
        for a in range(1, b // 3 + 1):
            fail = deterministic_cyclic_failure(b, a)
            if fail and first_fail is None:
                first_fail = (b, a, fail)
            flag = "fail" if fail else "ok"
            detail = ""
            if fail:
                _, loads, sums, good = fail
                detail = f" good={good} loads={np.round(loads, 6).tolist()} sums={np.round(sums, 6).tolist()}"
            lines.append(f"b={b:2d} a={a:2d} p={a/b:.6f}: {flag}{detail}")
    lines.append("")

    lines.append("2. Uniform subset deterministic strengthening at p=3/10")
    loads = [1 / 7] * 7 + [0.0] * 3
    count = uniform_subset_count(loads, 3)
    lines.append(
        f"loads seven 1/7 and three 0: good 3-subsets={count}/{comb(10, 3)} "
        f"= {count/comb(10, 3):.9f}, target=0.3"
    )
    lines.append("")

    lines.append("3. Exact tail values for selected weights")
    examples = [
        (2 / 7, [2 / 7, 2 / 7, 2 / 7, 1 / 7]),
        (3 / 10, [1 / 7] * 7),
        (3 / 10, [0.4, 0.3, 0.3]),
        (3 / 10, [0.25] * 4),
        (4 / 13, [0.25] * 4),
        (3 / 11, [1 / 8] * 8),
        (0.34, [1 / 3, 1 / 3, 1 / 3]),
    ]
    for p, weights in examples:
        val = bernoulli_tail_exact(np.array(weights, dtype=float), p)
        lines.append(
            f"p={p:.9f} n={len(weights):2d} tail={val:.12f} gap={val-p:.12f} "
            f"weights={np.round(weights, 6).tolist()}"
        )
    lines.append("")

    lines.append("4. Heuristic minimization over small supports")
    for p in [1 / 4, 2 / 7, 3 / 10, 1 / 3, 0.34]:
        for n in range(2, 9):
            val, w = minimize_tail(p, n, seed=1000 + 97 * n + int(round(10000 * p)))
            lines.append(
                f"p={p:.9f} n={n} min~={val:.12f} gap={val-p:.12f} "
                f"w={np.round(w, 5).tolist()}"
            )
        lines.append("")

    lines.append("5. Brute force downset convex-hull check")
    lines.extend(check_downsets(5, [1 / 4, 2 / 7, 3 / 10, 1 / 3, 0.34]))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines) + "\n")
    print(OUT)


if __name__ == "__main__":
    main()
