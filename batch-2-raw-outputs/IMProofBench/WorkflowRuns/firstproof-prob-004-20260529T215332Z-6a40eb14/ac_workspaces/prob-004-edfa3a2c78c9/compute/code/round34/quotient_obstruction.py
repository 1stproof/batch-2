#!/usr/bin/env python3
"""Finite cubical obstruction to a source-local quotient plaque homotopy.

The model is the smallest algebraic shadow of two cubical sheets with the
same f-image but different exact-plaque badness.

Source relative 2-cells:
    A  = large-transverse-plaque sheet, bad for the chosen z
    A' = small-transverse-plaque sheet, not bad for the chosen z

Target relative 2-cell:
    P

The cellular push-forward is f_# A = P and f_# A' = P, so A-A' is f-null
and quotient 2-cochains are exactly row vectors (x,x).  The source-local
operator that keeps the bad sheet and kills the nonbad sheet has matrix
diag(1,0).  It does not preserve ker f_#, and its dual does not send quotient
cochains to quotient cochains.
"""

from __future__ import annotations

from itertools import product

import sympy as sp


def preserves_kernel(f: sp.Matrix, op: sp.Matrix) -> bool:
    """Return whether op maps ker(f) into ker(f)."""
    for v in f.nullspace():
        if f * op * v != sp.zeros(f.rows, 1):
            return False
    return True


def row(v: sp.Matrix) -> str:
    return "[" + ", ".join(str(v[i]) for i in range(v.rows)) + "]"


def main() -> None:
    f2 = sp.Matrix([[1, 1]])  # f_#: C_2(source)->C_2(target)
    null = f2.nullspace()[0]  # A - A'

    keep_bad = sp.diag(1, 0)
    keep_good = sp.diag(0, 1)
    keep_both = sp.diag(1, 1)
    keep_none = sp.diag(0, 0)
    transfer_to_bad = sp.Matrix([[1, 1], [0, 0]])

    phi = sp.Matrix([[1, 1]])  # a quotient 2-cochain: phi(A)=phi(A')=1
    dual_keep_bad_phi = phi * keep_bad

    print("# Round 34 quotient obstruction")
    print()
    print("Basis C_2(source) = (A, A'), C_2(target) = (P).")
    print("Push-forward matrix f_# =", list(f2))
    print("Kernel generator N=A-A' =", row(null))
    print()

    print("## The bad-sheet projection")
    print("P_bad = diag(1,0) keeps A and kills A'.")
    print("f_# P_bad (A-A') =", row(f2 * keep_bad * null))
    print("Preserves ker f_#?", preserves_kernel(f2, keep_bad))
    print()
    print("Dual test with quotient cochain phi=(1,1):")
    print("P_bad^* phi = phi P_bad =", list(dual_keep_bad_phi))
    print("(P_bad^* phi)(A-A') =", list(dual_keep_bad_phi * null)[0])
    print("So P_bad^* phi is not a quotient cochain.")
    print()

    print("## Which diagonal exact-plaque masks descend?")
    print("| mask on (A,A') | preserves ker f_#? |")
    print("|---|---|")
    for a, b in product([0, 1], repeat=2):
        op = sp.diag(a, b)
        print(f"| ({a},{b}) | {'yes' if preserves_kernel(f2, op) else 'no'} |")
    print()
    print(
        "Only masks that are constant on the f-equivalence class {A,A'} descend."
    )
    print()

    print("## The quotient/localization tradeoff")
    print(
        "A nonlocal transfer T_bad with T_bad(A)=A and T_bad(A')=A does "
        "preserve ker f_#:"
    )
    print("T_bad matrix =", transfer_to_bad.tolist())
    print("f_# T_bad (A-A') =", row(f2 * transfer_to_bad * null))
    print("Preserves ker f_#?", preserves_kernel(f2, transfer_to_bad))
    print(
        "But it violates exact bad localization: the nonbad cell A' has "
        "zero mass in B_z={A}, while T_bad(A')=A has mass one."
    )
    print(
        "Equivalently, any operator T supported in {A} and inducing the "
        "identity on the quotient must have f_#T(A')=f_#A'=P, so it cannot "
        "also satisfy a bound by the exact bad mass of A'."
    )
    print()

    print("## Bad-supported quotient cochains")
    x = sp.symbols("x")
    # Bad support {A} means a quotient cochain (x,x) must vanish on A'.
    sol_bad_A = sp.solve([sp.Eq(x, 0)], [x], dict=True)
    print("If bad support is {A}, a quotient cochain (x,x) supported there")
    print("must satisfy x=0 on A', hence x=0. Solution:", sol_bad_A)
    print(
        "Thus a nonzero quotient residual cannot be supported on a nonsaturated "
        "exact-plaque bad set."
    )
    print()

    print("## Consequence for the strong cochain identity")
    print(
        "In the relative 2-complex with no 1-cells or 3-cells, delta phi=0 "
        "and delta L phi=0.  The proposed identity "
        "phi=K delta phi + Pi phi + delta L phi therefore reduces to "
        "phi=Pi phi for closed quotient 2-cochains."
    )
    print(
        "For phi=(1,1), this would require a nonzero quotient cochain "
        "supported in {A}, which the previous line shows does not exist."
    )
    print()

    print("## PL realization")
    print(
        "Take two small disjoint 4-cubes U_A,U_A' in R and central horizontal "
        "2-squares A,A'.  On both squares set G=(u,v), F=0, so f_#A=f_#A'=P.  "
        "Extend over transverse (s,t)-plaques by F=(s,t) on U_A and "
        "F=epsilon(s,t) on U_A'.  For z with epsilon << |z| < 1, A is in "
        "the exact-plaque bad set and A' is not, although A-A' is f-null."
    )


if __name__ == "__main__":
    main()
