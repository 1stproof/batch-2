"""Round 8 scaling checks for the averaged filling estimate.

The script records three elementary model computations:

1. product foliations, showing the defect term in (AF) is necessary;
2. the Round 7 hard fiber model, showing it violates the pointwise mixed
   2-dilation bound by L^(1/5);
3. a brute-force exponent search over coordinate-permutation linear maps,
   checking that no such diagonal/permutation model both has small normal
   area ratio and violates (AF).

The output is explanatory rather than a proof.
"""

from __future__ import annotations

from itertools import permutations


def fmt(x: float) -> str:
    if abs(x) < 1e-10:
        return "0"
    return f"{x:.6g}"


def product_foliation() -> list[str]:
    # S=(1,1,L,L), R=S.  For central fibers:
    # Fill ~ L, q~L^2, I~q, alpha=1.
    # Thus LHS exponent is 3, the energy terms have exponents 2 and 2,
    # and the defect term has exponent 3.
    return [
        "Product foliation S=R=(1,1,L,L):",
        "  LHS exponent ∫Fill ~ L^3.",
        "  R1 I exponent = 2; I^2/(S1 q) exponent = 2; defect exponent = 3.",
        "  Therefore the defect term is genuinely necessary.",
    ]


def hard_fiber_model() -> list[str]:
    # From round 7:
    # S=(1,1,L,L), R=(L^-1/5,L^3/5,cL,cL)
    # f=(u3/cL,u4/cL,L^6/5 u1,L^2/5 u2).
    # On fibers of F=(f3,f4), lambda~L^-1 and E_y~1, Fill~L^(9/5).
    # The desired fiber energy lower bound would be L^(1/2).
    # But |df(v) wedge df(n)| with v=u3 and n=u1 has exponent -1+6/5=1/5.
    return [
        "Round 7 hard fiber model:",
        "  S=(1,1,L,L), R=(L^(-1/5),L^(3/5),cL,cL).",
        "  E_y exponent = 0, Fill(Z_y) exponent = 9/5.",
        "  It violates the mixed bound |df(v)^df(n)|<=1 by exponent 1/5.",
        "  Hence it is only a counterexample to fiberwise statements, not to (AF).",
    ]


def diagonal_collapse_counterexample() -> list[str]:
    # Let S=(1,1,L,L), R=(1,M,L,L), 1<<M<<L, and
    # f(u1,u2,u3,u4)=(u1, phi(u2), u3, u4), where phi:[0,M]->[0,1]
    # is degree one and 1-Lipschitz.  The simplest smooth monotone choice is
    # phi(u2)=u2/M, but any 1-Lipschitz degree-one collapse has the same
    # operator-norm lambda=1 because f1=u1.
    #
    # For central y=(u3,u4), Z_y=[0,1]x[0,M]x{y}.  Its relative filling
    # volume is ~ M L.  The weighted energy per fiber is ~ M.
    # Hence, over q~L^2:
    #   LHS ~ M L^3,
    #   R1 I ~ M L^2,
    #   I^2/(S1 q) ~ M^2 L^2,
    #   defect ~ L^3.
    # For M=L^a, 0<a<1, the gap is min(a,1-a) in the exponent.
    a = 0.5
    return [
        "Diagonal collapse counterexample to (AF) as written:",
        "  S=(1,1,L,L), R=(1,M,L,L), f=(u1,u2/M,u3,u4), with M=L^a, 0<a<1.",
        "  Dil_2=1, degree=1, and central slices are degree-one over [0,1]^2.",
        "  q exponent = 2, I exponent = a+2, LHS exponent = a+3.",
        "  RHS exponents: R1 I = a+2, quadratic = 2a+2, defect = 3.",
        f"  For a={a}, LHS exponent {a+3:.3g} vs RHS exponent {max(a+2,2*a+2,3):.3g}.",
        "  This violates (AF) by L^min(a,1-a).  It does not violate the final theorem because R1=S1 and R3R4=S3S4.",
    ]


def linear_permutation_search() -> list[str]:
    # Fix S exponents (0,0,1,1). Search source exponents on a coarse grid.
    # Coordinate maps assign target coordinate j to source coordinate p[j].
    # For the central slicing by target coordinates 3,4 to be degree-one on
    # fibers for G=(target 1,2), target 1,2 must use the complementary source
    # coordinates. This is automatic for a permutation map.
    #
    # For each model:
    #   sigma_j exponent = s_j - r_{p[j]}.
    # Dil_2<=1 means the sum of the two largest sigma exponents <=0.
    # alpha exponent = r_{p[2]}+r_{p[3]} - (s_2+s_3).
    # LHS exponent = q + area(fiber) + min(normal source side exponents).
    # Energy per fiber exponent = area(fiber)+2 max(s0-r_p0, s1-r_p1).
    # I exponent = q + E_y.
    # RHS is max of R1I, I^2/(S1q), defect.
    s = (0.0, 0.0, 1.0, 1.0)
    q_exp = s[2] + s[3]
    grid = [i / 5 for i in range(-5, 11)]
    violations = []
    feasible = 0
    small_alpha = 0

    for r in permutations(grid, 4):
        if tuple(sorted(r)) != r:
            continue
        # source side ordering and volume enough for degree-one.
        if sum(r) + 1e-10 < sum(s):
            continue
        for p in permutations(range(4)):
            sig = [s[j] - r[p[j]] for j in range(4)]
            if sum(sorted(sig, reverse=True)[:2]) > 1e-10:
                continue
            feasible += 1
            normal = (p[2], p[3])
            tangent = (p[0], p[1])
            alpha_exp = r[normal[0]] + r[normal[1]] - q_exp
            if alpha_exp < -1e-10:
                small_alpha += 1
            fill_exp = r[tangent[0]] + r[tangent[1]] + min(r[normal[0]], r[normal[1]])
            lhs_exp = q_exp + fill_exp
            lam_exp = max(s[0] - r[p[0]], s[1] - r[p[1]])
            e_y_exp = r[tangent[0]] + r[tangent[1]] + 2 * lam_exp
            i_exp = q_exp + e_y_exp
            r1i_exp = r[0] + i_exp
            quad_exp = 2 * i_exp - s[0] - q_exp
            defect_exp = alpha_exp + (s[0] + s[1] + s[2]) + q_exp
            rhs_exp = max(r1i_exp, quad_exp, defect_exp)
            if alpha_exp < -1e-10 and lhs_exp > rhs_exp + 1e-10:
                violations.append((lhs_exp - rhs_exp, r, p, sig, alpha_exp, lhs_exp, rhs_exp))

    lines = [
        "Coordinate-permutation linear exponent search for S=(1,1,L,L):",
        f"  feasible Dil_2<=1 permutation models checked: {feasible}",
        f"  with small normal area ratio exponent alpha<0: {small_alpha}",
        f"  AF exponent violations found: {len(violations)}",
    ]
    if violations:
        violations.sort(reverse=True, key=lambda x: x[0])
        gap, r, p, sig, alpha, lhs, rhs = violations[0]
        lines.extend(
            [
                "  worst violation:",
                f"    gap={fmt(gap)}, r={tuple(fmt(x) for x in r)}, p={p}",
                f"    sigma={tuple(fmt(x) for x in sig)}, alpha={fmt(alpha)}",
                f"    lhs={fmt(lhs)}, rhs={fmt(rhs)}",
            ]
        )
    else:
        lines.append("  No diagonal/permutation linear counterexample appears on this grid.")
    return lines


def main() -> None:
    sections = [
        product_foliation(),
        hard_fiber_model(),
        diagonal_collapse_counterexample(),
        linear_permutation_search(),
    ]
    print("\n\n".join("\n".join(section) for section in sections))


if __name__ == "__main__":
    main()
