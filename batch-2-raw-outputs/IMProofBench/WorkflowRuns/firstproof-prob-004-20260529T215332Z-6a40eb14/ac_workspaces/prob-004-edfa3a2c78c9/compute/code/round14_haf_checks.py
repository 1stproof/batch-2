"""Round 14 checks for the hard-regime averaged filling estimate.

The script records three kinds of evidence:

1. Exact exponent bookkeeping for the two stress scalings discussed in the
   notes/prompt.
2. A linear-programming check that affine/coordinate-permutation maps cannot
   give a positive-margin hard-regime counterexample.
3. A bounded-depth search through the corrected Guth thesis Chapter 8.2
   exponent moves, ending with an allowed linear 2-contraction if possible.

All side lengths are encoded as powers of a large parameter L.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations
from pathlib import Path
import sys

import numpy as np
from scipy.optimize import linprog

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from code.guth_ch8_exponent_search import (  # noqa: E402
    F,
    Vec,
    fmt,
    fmt_vec,
    lin2_exponent,
    shortest_route_to_target,
    target_badness,
)


def margin(expr_r: Fraction, expr_s: Fraction) -> Fraction:
    return expr_r - expr_s


def side_report(name: str, r: Vec, s: Vec) -> list[str]:
    out: list[str] = []
    out.append(f"## {name}")
    out.append(f"R exponents = {fmt_vec(r)}")
    out.append(f"S exponents = {fmt_vec(s)}")
    out.append(f"badness exponents (R1/S1, R3R4/S3S4, Vol/T) = {tuple(fmt(x) for x in target_badness(r, s))}")
    out.append(f"Vol(R) exponent = {fmt(sum(r))}")
    target = s[0] + Fraction(1, 2) * s[1] + Fraction(3, 2) * s[2] + s[3]
    out.append(f"T=S1*S2^(1/2)*S3^(3/2)*S4 exponent = {fmt(target)}")
    out.append(f"first-alt threshold margin R1*R2^2 / (S1*S2*S3) = {fmt(r[0] + 2*r[1] - s[0] - s[1] - s[2])}")
    alpha = r[0] - s[0]
    out.append(f"alpha=R1/S1 exponent = {fmt(alpha)}")
    out.append(f"current lower bound alpha^(1/2)*T exponent = {fmt(target + alpha/2)}")
    out.append(f"best affine/coordinate-permutation 2-dilation exponent R->S = {fmt(lin2_exponent(r, s))}")

    # Guth Estimate 1 monomials for k=2, plus the k=3,j=2,l=4 consequence.
    checks = [
        ("k=2 j=0 l=2: R1R2 >= S1S2", r[0] + r[1], s[0] + s[1]),
        ("k=2 j=0 l=3: R1R2R3 >= S1S2S3", r[0] + r[1] + r[2], s[0] + s[1] + s[2]),
        ("k=2 j=0 l=4: Vol(R) >= Vol(S)", sum(r), sum(s)),
        ("k=2 j=1 l=3: R1^2 R2 R3 >= S1^2 S2 S3", 2*r[0] + r[1] + r[2], 2*s[0] + s[1] + s[2]),
        ("k=2 j=1 l=4: R1^3 Vol(R)/R1 >= S1^3 Vol(S)/S1", 3*r[0] + r[1] + r[2] + r[3], 3*s[0] + s[1] + s[2] + s[3]),
        ("k=3 j=2 l=4: (R1R2)^2 R3R4 >= (S1S2)^2 S3S4", 2*r[0] + 2*r[1] + r[2] + r[3], 2*s[0] + 2*s[1] + s[2] + s[3]),
    ]
    out.append("Guth monomial margins (left exponent minus right exponent):")
    for label, lhs, rhs in checks:
        out.append(f"  {label}: {fmt(margin(lhs, rhs))}")
    return out


NAMES = ["r1", "r2", "r3", "r4", "s1", "s2", "s3", "s4", "m"]


def coeff(**kw: float) -> np.ndarray:
    row = np.zeros(len(NAMES))
    for key, value in kw.items():
        row[NAMES.index(key)] = value
    return row


def affine_lp_report() -> list[str]:
    """Maximize a common hard-regime failure margin among diagonal/permuted maps."""
    best: list[tuple[float, tuple[int, ...], np.ndarray]] = []
    for perm in permutations(range(4)):
        a_ub: list[np.ndarray] = []
        b_ub: list[float] = []
        a_eq: list[np.ndarray] = []
        b_eq: list[float] = []

        for i in range(3):
            a_ub.append(coeff(**{f"r{i+1}": 1, f"r{i+2}": -1}))
            b_ub.append(0.0)
            a_ub.append(coeff(**{f"s{i+1}": 1, f"s{i+2}": -1}))
            b_ub.append(0.0)

        # Normalize the target by homogeneity.
        a_eq.append(coeff(s1=1))
        b_eq.append(0.0)
        a_eq.append(coeff(s4=1))
        b_eq.append(1.0)

        # The three desired alternatives fail by margin m.
        a_ub.append(coeff(r1=1, s1=-1, m=1))
        b_ub.append(0.0)
        a_ub.append(coeff(r3=1, r4=1, s3=-1, s4=-1, m=1))
        b_ub.append(0.0)
        a_ub.append(coeff(r1=1, r2=1, r3=1, r4=1, s1=-1, s2=-0.5, s3=-1.5, s4=-1, m=1))
        b_ub.append(0.0)
        a_ub.append(coeff(m=-1))
        b_ub.append(0.0)
        a_ub.append(coeff(m=1))
        b_ub.append(10.0)

        # Diagonal/permuted affine map: all pair expansion exponents <= 0.
        for a, b in combinations(range(4), 2):
            row = np.zeros(len(NAMES))
            row[4 + a] += 1
            row[perm[a]] -= 1
            row[4 + b] += 1
            row[perm[b]] -= 1
            a_ub.append(row)
            b_ub.append(0.0)

        result = linprog(
            coeff(m=-1),
            A_ub=np.array(a_ub),
            b_ub=np.array(b_ub),
            A_eq=np.array(a_eq),
            b_eq=np.array(b_eq),
            bounds=[(-20, 20)] * 8 + [(0, 10)],
            method="highs",
        )
        if result.success:
            best.append((-float(result.fun), perm, result.x))

    best.sort(reverse=True, key=lambda item: item[0])
    out = ["## affine/coordinate-permutation LP"]
    if not best:
        out.append("No feasible LP solutions.")
        return out
    out.append(f"best common failure margin = {best[0][0]:.12g}")
    if best[0][0] <= 1e-9:
        out.append("Conclusion: no positive-margin hard-regime affine/permutation counterexample.")
    for value, perm, x in best[:4]:
        q = [x[4 + i] - x[perm[i]] for i in range(4)]
        rvals = tuple(round(float(z), 9) for z in x[:4])
        svals = tuple(round(float(z), 9) for z in x[4:8])
        out.append(f"  perm={perm}, margin={value:.12g}, r={rvals}, s={svals}, top2={sum(sorted(q)[-2:]):.9g}")
    return out


def route_report(name: str, r: Vec, s: Vec, specs: list[tuple[Fraction, int, int]]) -> list[str]:
    out = [f"## Guth Chapter 8.2 route search: {name}"]
    for step, depth, beam in specs:
        ok, path = shortest_route_to_target(r, s, depth=depth, step=step, beam=beam)
        out.append(f"step={fmt(step)} depth={depth} beam={beam}: {'FOUND' if ok else 'not found'}")
        out.append("  " + " -> ".join(path))
    return out


def main() -> None:
    haf_r: Vec = (F(Fraction(-1, 5)), F(Fraction(13, 15)), F(Fraction(13, 15)), F(Fraction(13, 15)))
    haf_s: Vec = (F(0), F(0), F(1), F(1))
    old_r: Vec = (F(-1), F(4), F(5), F(6))
    old_s: Vec = (F(0), F(0), F(6), F(6))

    out: list[str] = ["# Round 14 HAF/exponent checks", ""]
    out.extend(side_report("prompt hard model S=(1,1,L,L), R=(L^-1/5,L^13/15,L^13/15,L^13/15)", haf_r, haf_s))
    out.append("")
    out.extend(side_report("older stress model S=(1,1,L^6,L^6), R=(L^-1,L^4,L^5,L^6)", old_r, old_s))
    out.append("")
    out.extend(affine_lp_report())
    out.append("")
    # This is a bounded search, not a proof of non-existence.  The exact 1/15
    # grid is too large for deep searches in this worker call, so the route
    # search is deliberately short/coarse and is paired with the prior deeper
    # half/quarter-grid stress-family searches in data/round11_*.
    out.extend(route_report("prompt hard model", haf_r, haf_s, [(Fraction(1, 5), 2, 1000)]))
    out.append("")
    out.extend(route_report("older stress model", old_r, old_s, [(Fraction(1, 1), 3, 1000)]))

    text = "\n".join(out) + "\n"
    Path("data/round14").mkdir(parents=True, exist_ok=True)
    Path("data/round14/haf_checks.txt").write_text(text)
    print(text)


if __name__ == "__main__":
    main()
