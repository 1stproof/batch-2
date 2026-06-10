"""Small checks for the rational/cyclic interval reformulation.

For q=a/b, representing Bernoulli(q) as a random cyclic interval of
length a in Z/bZ gives the complement formulation

    P(sum w_i eta_i > q) <= q

as an averaged statement about random allocations of weights to b
residue classes.  A tempting deterministic lemma would be:

    for every load vector on Z/bZ, at most a intervals of length a
    have load > a/b, whenever a/b >= 2/3.

This script verifies that this deterministic strengthening is false:
for b=7, a=5 there are load vectors with six good intervals.
The actual desired inequality would need to exploit the averaging over
independent random allocations of the original weights.
"""

from itertools import combinations, product

import numpy as np
from scipy.optimize import linprog


def interval_sum(loads, start, length):
    b = len(loads)
    return sum(loads[(start + k) % b] for k in range(length))


def feasible_many_good_intervals(b, a, count, eps=1e-7):
    """Find a load vector with at least `count` intervals above a/b."""
    threshold = a / b + eps
    for starts in combinations(range(b), count):
        rows = []
        rhs = []
        for j in starts:
            row = np.zeros(b)
            for k in range(a):
                row[(j + k) % b] = -1
            rows.append(row)
            rhs.append(-threshold)
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
            return starts, res.x
    return None, None


def expected_good_intervals(weights, b, c):
    """Exact expectation over independent placements into Z/bZ."""
    threshold = c / b
    total = 0
    for positions in product(range(b), repeat=len(weights)):
        loads = [0.0] * b
        for weight, pos in zip(weights, positions):
            loads[pos] += weight
        total += sum(
            interval_sum(loads, j, c) + 1e-12 >= threshold for j in range(b)
        )
    return total / (b ** len(weights))


if __name__ == "__main__":
    print("Checking deterministic interval strengthening for b<=12...")
    for b in range(3, 13):
        for a in range((2 * b + 2) // 3, b):
            starts, loads = feasible_many_good_intervals(b, a, a + 1)
            print(f"b={b:2d} a={a:2d} has >a deterministic intervals? {starts is not None}")
            if starts is not None:
                sums = [interval_sum(loads, j, a) for j in range(b)]
                print("  starts:", starts)
                print("  loads:", np.round(loads, 9))
                print("  interval sums:", np.round(sums, 9))
                print("  threshold:", a / b)
                break
        else:
            continue
        break

    print("\nExact expected number of good short intervals for sample weights:")
    for b, c in [(7, 2), (10, 3), (9, 3)]:
        print(f"b={b} c={c} threshold={c/b:.6f}")
        for weights in ([1.0], [0.5, 0.5], [0.7, 0.3], [0.25] * 4):
            print(f"  weights={weights}: E count={expected_good_intervals(weights, b, c):.9f}")
