"""Round 6 exponent LP for the trace-reduction inequalities.

Lengths are encoded as powers of a large parameter L:

    R_i = L**r_i,  S_i = L**s_i,  V = L**v.

For a lower-bound inequality A+B >= c C, the exponent condition is
max(exp(A), exp(B)) >= exp(C).  The four trace inequalities are therefore
checked by enumerating which summand supplies the maximum.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product

import numpy as np
from scipy.optimize import linprog


NAMES = ["r1", "r2", "r3", "r4", "s1", "s2", "s3", "s4", "v"]
N = len(NAMES)


def vec(**kw: float) -> np.ndarray:
    out = np.zeros(N)
    for key, value in kw.items():
        out[NAMES.index(key)] = float(value)
    return out


def add_ge(a_ub: list[np.ndarray], b_ub: list[float], left: np.ndarray, right: np.ndarray) -> None:
    """Append left >= right in scipy's A_ub x <= b_ub convention."""
    a_ub.append(right - left)
    b_ub.append(0.0)


def add_le(a_ub: list[np.ndarray], b_ub: list[float], left: np.ndarray, right: np.ndarray) -> None:
    a_ub.append(left - right)
    b_ub.append(0.0)


def solve_branch(branch: tuple[int, int, int, int]):
    a_ub: list[np.ndarray] = []
    b_ub: list[float] = []
    a_eq: list[np.ndarray] = []
    b_eq: list[float] = []

    for i in range(3):
        add_le(a_ub, b_ub, vec(**{f"r{i+1}": 1}), vec(**{f"r{i+2}": 1}))
        add_le(a_ub, b_ub, vec(**{f"s{i+1}": 1}), vec(**{f"s{i+2}": 1}))

    a_eq.append(vec(v=1, r1=-1, r2=-1, r3=-1, r4=-1))
    b_eq.append(0.0)

    # Normalize the common scale and the size of the target aspect ratio.
    a_eq.append(vec(s1=1))
    b_eq.append(0.0)
    a_eq.append(vec(s4=1))
    b_eq.append(1.0)

    # Hypotheses R1 <= kappa S1 and R3 R4 <= kappa S3 S4 at exponent level.
    add_le(a_ub, b_ub, vec(r1=1), vec(s1=1))
    add_le(a_ub, b_ub, vec(r3=1, r4=1), vec(s3=1, s4=1))

    # Guth Estimate 1, n=4, k=2, with repeated/duplicate cases omitted.
    add_ge(a_ub, b_ub, vec(r1=1, r2=1), vec(s1=1, s2=1))
    add_ge(a_ub, b_ub, vec(r1=1, r2=1, r3=1), vec(s1=1, s2=1, s3=1))
    add_ge(a_ub, b_ub, vec(r1=2, r2=1, r3=1), vec(s1=2, s2=1, s3=1))
    add_ge(a_ub, b_ub, vec(v=1), vec(s1=1, s2=1, s3=1, s4=1))
    add_ge(a_ub, b_ub, vec(r1=3, r2=1, r3=1, r4=1), vec(s1=3, s2=1, s3=1, s4=1))

    trace_target = vec(s1=1, s2=1, s3=2, s4=1)
    for i, choice in enumerate(branch, start=1):
        if choice == 1:
            add_ge(a_ub, b_ub, vec(**{f"r{i}": 1}, v=1), trace_target)
        else:
            add_ge(a_ub, b_ub, vec(v=2, **{f"r{i}": -1}, s3=-1, s4=-1), trace_target)

    objective = vec(v=1, s1=-1, s2=-0.5, s3=-1.5, s4=-1)
    return linprog(
        objective,
        A_ub=np.array(a_ub),
        b_ub=np.array(b_ub),
        A_eq=np.array(a_eq),
        b_eq=np.array(b_eq),
        bounds=[(-20, 20)] * N,
        method="highs",
    )


def ffmt(x: Fraction) -> str:
    if x.denominator == 1:
        return str(x.numerator)
    return f"{x.numerator}/{x.denominator}"


def exact_model() -> None:
    r = [Fraction(-1, 5), Fraction(13, 15), Fraction(13, 15), Fraction(13, 15)]
    s = [Fraction(0), Fraction(0), Fraction(1), Fraction(1)]
    v = sum(r)
    target = s[0] + s[1] / 2 + 3 * s[2] / 2 + s[3]
    trace_target = s[0] + s[1] + 2 * s[2] + s[3]

    print("# Exact exponent model")
    print("S exponents:", [ffmt(x) for x in s])
    print("R exponents:", [ffmt(x) for x in r])
    print("v=sum r_i:", ffmt(v))
    print("desired RHS exponent:", ffmt(target))
    print("volume ratio exponent v-target:", ffmt(v - target))
    print("R1/S1 exponent:", ffmt(r[0] - s[0]))
    print("R3R4/(S3S4) exponent:", ffmt(r[2] + r[3] - s[2] - s[3]))
    print()

    checks = [
        ("G j=0,l=2", r[0] + r[1] - s[0] - s[1]),
        ("G j=0,l=3", sum(r[:3]) - sum(s[:3])),
        ("G j=1,l=3", 2 * r[0] + r[1] + r[2] - (2 * s[0] + s[1] + s[2])),
        ("G j=0,l=4", v - sum(s)),
        ("G j=1,l=4", 3 * r[0] + r[1] + r[2] + r[3] - (3 * s[0] + s[1] + s[2] + s[3])),
    ]
    print("Guth monomial exponents left/right:")
    for label, exp in checks:
        print(f"  {label}: {ffmt(exp)}")
    print()

    print("Trace exponents, max(term1, term2) - target:")
    for i in range(4):
        term1 = r[i] + v
        term2 = 2 * v - r[i] - s[2] - s[3]
        print(
            f"  i={i+1}: term1={ffmt(term1)}, term2={ffmt(term2)}, "
            f"target={ffmt(trace_target)}, slack={ffmt(max(term1, term2) - trace_target)}"
        )


def main() -> None:
    best = None
    for branch in product([1, 2], repeat=4):
        result = solve_branch(branch)
        if result.success and (best is None or result.fun < best[0]):
            best = (result.fun, branch, result.x)

    print("# LP optimum with s1=0, s4=1")
    if best is None:
        print("No feasible branch.")
    else:
        value, branch, x = best
        print("best objective v - target:", value)
        print("branch, 1=R_i V and 2=V^2/(R_i S3S4):", branch)
        for name, coord in zip(NAMES, x):
            print(f"{name} = {coord:.12g}")
        print()

    exact_model()


if __name__ == "__main__":
    main()
