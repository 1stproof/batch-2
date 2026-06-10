"""Round 22 coordinate second-order linking exponent check.

This script records the n=4, k1=k2=k3=2 specialization of Guth's
directional L2 upper-bound argument, in the relative rectangle form relevant
to maps of pairs.  It then tests the resulting monomial inequalities against
the hard-regime linear constraints from the current draft.

All side lengths are exponents of a large parameter L:
    R_i = L**r_i, S_i = L**s_i.
Constants are ignored.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, permutations, product
from pathlib import Path

import numpy as np
from scipy.optimize import linprog


PAIRS = tuple(combinations((1, 2, 3, 4), 2))
TRIPLES = tuple(combinations((1, 2, 3, 4), 3))
NAMES = ("r1", "r2", "r3", "r4", "s1", "s2", "s3", "s4")


def idx(name: str) -> int:
    return NAMES.index(name)


def vec(**kw: float) -> np.ndarray:
    out = np.zeros(len(NAMES))
    for k, v in kw.items():
        out[idx(k)] = v
    return out


def side_exp(pair: tuple[int, int], prefix: str) -> np.ndarray:
    return vec(**{f"{prefix}{pair[0]}": 1, f"{prefix}{pair[1]}": 1})


def vol_exp(prefix: str) -> np.ndarray:
    return sum((vec(**{f"{prefix}{i}": 1}) for i in range(1, 5)), np.zeros(len(NAMES)))


def pair_to_str(pair: tuple[int, int]) -> str:
    return "".join(map(str, pair))


def remove_one(tup: tuple[int, ...], d: int) -> tuple[int, ...]:
    return tuple(x for x in tup if x != d)


def smallest_not_in(tup: tuple[int, ...]) -> int:
    for i in range(1, 5):
        if i not in tup:
            return i
    raise ValueError(tup)


def relative_fill_2_to_3() -> dict[tuple[int, int, int], list[tuple[int, tuple[int, int]]]]:
    """Directional relative filling of a 2-cycle z by a 3-chain y.

    For a 3-tuple I, Vol_I(y) <= sum_{d<e(I)} R_d Vol_{I-d}(z).
    Since e(I) is the first missing coordinate, all d<e are in I.
    """

    out: dict[tuple[int, int, int], list[tuple[int, tuple[int, int]]]] = {}
    for I in TRIPLES:
        e = smallest_not_in(I)
        terms = []
        for d in range(1, e):
            terms.append((d, remove_one(I, d)))  # R_d * a_{I-d}
        out[I] = terms
    return out


def relative_fill_1_to_2() -> dict[tuple[int, int], list[tuple[int, tuple[int]]]]:
    """Directional relative filling of a 1-cycle c by a 2-chain y."""

    out: dict[tuple[int, int], list[tuple[int, tuple[int]]]] = {}
    for K in PAIRS:
        e = smallest_not_in(K)
        terms = []
        for d in range(1, e):
            terms.append((d, remove_one(K, d)))
        out[K] = terms
    return out


def l2_upper_coefficients() -> dict[tuple[int, int], set[tuple[int, int]]]:
    """Return monomial R-coefficients multiplying each initial z1 2-volume.

    The output maps an initial source 2-direction J to the set of R-index pairs
    (a,b), meaning a term R_a R_b * Vol_J(z1), after the two directional
    fillings and the two generic coarea steps.

    Coarea from a 3-chain to a 1-cycle sums over all 3-directions containing
    the requested line direction.  The final 0-dimensional coarea is bounded
    by total 2-volume of the second filling.
    """

    fill23 = relative_fill_2_to_3()
    fill12 = relative_fill_1_to_2()

    # b_I terms are (R_a, initial J).
    b: dict[tuple[int, int, int], list[tuple[int, tuple[int, int]]]] = fill23

    # c_j terms after slicing y1 by the second S^2 factor.
    c: dict[tuple[int], list[tuple[int, tuple[int, int]]]] = {(j,): [] for j in range(1, 5)}
    for j in range(1, 5):
        for I in TRIPLES:
            if j in I:
                c[(j,)].extend(b[I])

    # y2_K terms after filling c.
    coeffs: dict[tuple[int, int], set[tuple[int, int]]] = {J: set() for J in PAIRS}
    for K, terms in fill12.items():
        for r_index, singleton in terms:
            for prev_r_index, initial_J in c[singleton]:
                coeffs[initial_J].add(tuple(sorted((r_index, prev_r_index))))
    return coeffs


def dominant_coeff_class(coeffs: dict[tuple[int, int], set[tuple[int, int]]]) -> dict[tuple[int, int], tuple[int, int]]:
    """Choose the asymptotically largest coefficient for sorted R exponents."""

    out = {}
    for J, terms in coeffs.items():
        # For r1 <= r2 <= r3 <= r4, compare by sorted lexicographic pair.
        out[J] = max(terms, key=lambda ab: (ab[1], ab[0]))
    return out


@dataclass(frozen=True)
class PathPattern:
    order: tuple[int, int, int, int]

    @property
    def p1(self) -> tuple[int, int]:
        return tuple(sorted((self.order[2], self.order[3])))

    @property
    def p2(self) -> tuple[int, int]:
        return tuple(sorted((self.order[1], self.order[2])))

    @property
    def p3(self) -> tuple[int, int]:
        return tuple(sorted((self.order[0], self.order[1])))

    @property
    def middle_pair(self) -> tuple[int, int]:
        return self.p2

    @property
    def triple(self) -> tuple[tuple[int, int], tuple[int, int], tuple[int, int]]:
        return self.p1, self.p2, self.p3

    def target_exponent_vec(self) -> np.ndarray:
        # Guth lower construction gives Vol(S) times the product of the two
        # middle coordinates in the ordered path.
        return vol_exp("s") + side_exp(self.middle_pair, "s")


def base_constraints(include_hard: bool = True) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    a_ub: list[np.ndarray] = []
    b_ub: list[float] = []
    a_eq: list[np.ndarray] = []
    b_eq: list[float] = []

    # Sorted R and S exponents.
    for prefix in ("r", "s"):
        for i in range(1, 4):
            a_ub.append(vec(**{f"{prefix}{i}": 1, f"{prefix}{i+1}": -1}))
            b_ub.append(0.0)

    # Normalization: s1=0, s4=1.
    a_eq.append(vec(s1=1))
    b_eq.append(0.0)
    a_eq.append(vec(s4=1))
    b_eq.append(1.0)

    # Known degree / dilation consequences listed in the notes.
    # R1 R2 >= S1 S2.
    a_ub.append(-(side_exp((1, 2), "r") - side_exp((1, 2), "s")))
    b_ub.append(0.0)
    # R1 R2 R3 >= S1 S2 S3.
    a_ub.append(-(vec(r1=1, r2=1, r3=1) - vec(s1=1, s2=1, s3=1)))
    b_ub.append(0.0)
    # Vol(R) >= Vol(S).
    a_ub.append(-(vol_exp("r") - vol_exp("s")))
    b_ub.append(0.0)
    # R1^2 R2 R3 >= S1^2 S2 S3.
    a_ub.append(-(vec(r1=2, r2=1, r3=1) - vec(s1=2, s2=1, s3=1)))
    b_ub.append(0.0)
    # R1^2 Vol(R) >= S1^2 Vol(S).
    a_ub.append(-(vec(r1=2) + vol_exp("r") - vec(s1=2) - vol_exp("s")))
    b_ub.append(0.0)
    # (R1 R2)^2 R3 R4 >= (S1 S2)^2 S3 S4.
    a_ub.append(-(vec(r1=2, r2=2, r3=1, r4=1) - vec(s1=2, s2=2, s3=1, s4=1)))
    b_ub.append(0.0)
    # Guth j=1,k=2,l=4: R1^3 R2 R3 R4 >= S1^3 S2 S3 S4.
    a_ub.append(-(vec(r1=3, r2=1, r3=1, r4=1) - vec(s1=3, s2=1, s3=1, s4=1)))
    b_ub.append(0.0)

    # Failure of first alternative gives R1 R2^2 >= S1 S2 S3.
    a_ub.append(-(vec(r1=1, r2=2) - vec(s1=1, s2=1, s3=1)))
    b_ub.append(0.0)

    # Consequence (8) from the current answer:
    # Vol(R) >= (R1/S1)^{1/2} * S1 S2^{1/2} S3^{3/2} S4.
    a_ub.append(-(vol_exp("r") - (vec(r1=0.5, s1=0.5, s2=0.5, s3=1.5, s4=1))))
    b_ub.append(0.0)

    if include_hard:
        # Hard-regime inequalities, non-strict exponent form.
        a_ub.append(vec(r1=1, s1=-1))
        b_ub.append(0.0)
        a_ub.append(vec(r3=1, r4=1, s3=-1, s4=-1))
        b_ub.append(0.0)

    return np.array(a_ub), np.array(b_ub), np.array(a_eq), np.array(b_eq)


def add_linking_inequality(a_ub: list[np.ndarray], b_ub: list[float], target: np.ndarray, coeff: np.ndarray) -> None:
    # Vol(R) + coeff(R) >= target(S)
    a_ub.append(-(vol_exp("r") + coeff - target))
    b_ub.append(0.0)


def solve_min_gap(include_all_formal_path_targets: bool = False) -> tuple[bool, float, np.ndarray]:
    A_ub, b_ub, A_eq, b_eq = base_constraints(include_hard=True)
    a_ub = [row.copy() for row in A_ub]
    b = list(b_ub)

    # Valid Guth coordinate construction for a sorted rectangle:
    # (x3,x4), then (x2,x3), then (x1,x2), giving target Vol(S) S2 S3.
    add_linking_inequality(a_ub, b, vol_exp("s") + side_exp((2, 3), "s"), side_exp((2, 3), "r"))

    if include_all_formal_path_targets:
        # Optimistic formal enumeration: allow every Hamilton path target lower
        # Vol(S) S_i S_j, but keep the only universally valid upper coefficient
        # R2 R3.  Some of these target constructions are not uniformly Lipschitz
        # in Guth's theorem; this option only stress-tests the algebra.
        seen = set()
        for order in permutations((1, 2, 3, 4)):
            pat = PathPattern(order)
            if pat.middle_pair in seen:
                continue
            seen.add(pat.middle_pair)
            add_linking_inequality(a_ub, b, pat.target_exponent_vec(), side_exp((2, 3), "r"))

    desired = vec(s1=1, s2=0.5, s3=1.5, s4=1)
    objective = vol_exp("r") - desired
    res = linprog(
        objective,
        A_ub=np.array(a_ub),
        b_ub=np.array(b),
        A_eq=A_eq,
        b_eq=b_eq,
        bounds=[(-20, 20)] * 8,
        method="highs",
    )
    if not res.success:
        return False, float("nan"), np.full(8, np.nan)
    return True, float(res.fun), res.x


def exponent_of(v: np.ndarray, x: np.ndarray) -> float:
    return float(np.dot(v, x))


def format_solution(x: np.ndarray) -> list[str]:
    v = exponent_of(vol_exp("r"), x)
    t = exponent_of(vec(s1=1, s2=0.5, s3=1.5, s4=1), x)
    lines = []
    lines.append("r = (" + ", ".join(f"{z:.9g}" for z in x[:4]) + ")")
    lines.append("s = (" + ", ".join(f"{z:.9g}" for z in x[4:]) + ")")
    lines.append(f"Vol exponent = {v:.9g}; desired exponent = {t:.9g}; gap Vol-desired = {v-t:.9g}")
    checks = {
        "hard R1/S1": vec(r1=1, s1=-1),
        "hard R3R4/S3S4": vec(r3=1, r4=1, s3=-1, s4=-1),
        "first-alt failure R1R2^2/(S1S2S3)": vec(r1=1, r2=2, s1=-1, s2=-1, s3=-1),
        "Guth degree R1^3R2R3R4/(S1^3S2S3S4)": vec(r1=3, r2=1, r3=1, r4=1, s1=-3, s2=-1, s3=-1, s4=-1),
        "valid L2 R2R3Vol/(VolS S2S3)": vol_exp("r") + side_exp((2, 3), "r") - vol_exp("s") - side_exp((2, 3), "s"),
        "formal strongest R2R3Vol/(VolS S3S4)": vol_exp("r") + side_exp((2, 3), "r") - vol_exp("s") - side_exp((3, 4), "s"),
    }
    for name, row in checks.items():
        lines.append(f"{name}: {exponent_of(row, x):.9g}")
    return lines


def main() -> None:
    coeffs = l2_upper_coefficients()
    dominant = dominant_coeff_class(coeffs)

    out: list[str] = []
    out.append("# Round 22 coordinate L2 LP")
    out.append("")
    out.append("Relative directional L2 upper coefficients, before replacing by R2 R3:")
    for J in PAIRS:
        terms = " + ".join(f"R{a}R{b}" for a, b in sorted(coeffs[J])) or "0"
        out.append(f"  initial source direction {pair_to_str(J)}: {terms}; dominant {pair_to_str(dominant[J])}")

    out.append("")
    out.append("Hamilton-path coordinate triples (Guth lower pattern):")
    seen_triples = set()
    for order in permutations((1, 2, 3, 4)):
        pat = PathPattern(order)
        if pat.triple in seen_triples:
            continue
        seen_triples.add(pat.triple)
        out.append(
            f"  order {order}: P1={pair_to_str(pat.p1)}, P2={pair_to_str(pat.p2)}, "
            f"P3={pair_to_str(pat.p3)}, formal target factor Vol(S)*S{pat.middle_pair[0]}S{pat.middle_pair[1]}"
        )

    out.append("")
    ok, gap, x = solve_min_gap(include_all_formal_path_targets=False)
    out.append("LP with valid sorted Guth L2 inequality Vol(R)R2R3 >= Vol(S)S2S3:")
    out.append(f"  success={ok}, minimum Vol-desired exponent={gap:.12g}")
    if ok:
        out.extend("  " + line for line in format_solution(x))

    out.append("")
    ok, gap, x = solve_min_gap(include_all_formal_path_targets=True)
    out.append("LP with all formal Hamilton-path target factors Vol(S)S_iS_j, still using universal upper R2R3:")
    out.append(f"  success={ok}, minimum Vol-desired exponent={gap:.12g}")
    if ok:
        out.extend("  " + line for line in format_solution(x))

    out.append("")
    out.append("Fixed stress model from round 19, normalized with s=(0,0,1,1):")
    x = np.array([-1 / 5, 13 / 15, 13 / 15, 13 / 15, 0, 0, 1, 1], dtype=float)
    out.extend("  " + line for line in format_solution(x))

    Path("data/round22").mkdir(parents=True, exist_ok=True)
    Path("data/round22/coordinate_l2_lp_report.txt").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
