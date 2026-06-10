"""Symbolic exponent check for the tempting double-pinching route.

This records a useful correction: the thesis OCR can read the target as
R1/A x A x A x B, but the construction and the final linear map force
R1^2/A x A x A x B.  With the corrected exponent, the tempting
counterexample disappears.
"""

from fractions import Fraction
from itertools import combinations


def fmt(x: Fraction) -> str:
    if x == 0:
        return "L^0"
    if x.denominator == 1:
        return f"L^{x.numerator}"
    return f"L^({x.numerator}/{x.denominator})"


def q_exponents(R, S):
    return [s - r for r, s in zip(R, S)]


def estimate1_exponents(R, S, k):
    q = q_exponents(R, S)
    out = []
    n = len(R)
    for j in range(0, k):
        for ell in range(k, n + 1):
            exponent = sum(q[:j]) + Fraction(k - j, ell - j) * sum(q[j:ell])
            out.append((j, ell, exponent))
    return out


def linear_2_dilation_exponent(R, S):
    q = q_exponents(R, S)
    return max(q[i] + q[j] for i, j in combinations(range(len(q)), 2))


def main():
    # Domain of Guth's double pinching map.
    R = [Fraction(-4), Fraction(1, 2), Fraction(1), Fraction(4)]
    # Parameter A=L^a, B=L^b.  Strict A^3 B < Vol(R) can be enforced by
    # multiplying B by a small fixed constant; exponents are unchanged.
    a = Fraction(-5, 2)
    b = Fraction(9)
    S_unsorted = [2 * R[0] - a, a, a, b]
    S = sorted(S_unsorted)

    print("# Round 4 corrected double-pinching check")
    print("R exponents:", R)
    print("A exponent:", a)
    print("B exponent:", b, "(take B=eta*L^9 with fixed eta<1 for strictness)")
    print("unsorted target R1^2/A x A x A x B:", S_unsorted)
    print("sorted S exponents:", S)
    print()

    print("Guth double pinching hypotheses (exponent comparison):")
    print("  R1 < A:", R[0], "<", a, "difference A/R1 =", fmt(a - R[0]))
    print("  A^2 < R2 R3:", 2 * a, "<", R[1] + R[2], "ratio =", fmt(R[1] + R[2] - 2 * a))
    print("  A^3 B < Vol(R):", 3 * a + b, "<=", sum(R), "same exponent; fixed eta<1 makes it strict")
    print()

    denom = S[0] + Fraction(1, 2) * S[1] + Fraction(3, 2) * S[2] + S[3]
    checks = [
        ("R1/S1", R[0] - S[0]),
        ("R3R4/(S3S4)", R[2] + R[3] - S[2] - S[3]),
        ("Vol(R)/(S1 S2^1/2 S3^3/2 S4)", sum(R) - denom),
    ]
    print("Target theorem ratios before fixed domain scaling:")
    for label, exp in checks:
        print(f"  {label}: {fmt(exp)}")
    print()

    print("Guth Estimate 1 lower-bound monomial exponents for this R->S:")
    for k in (2, 3, 4):
        print(f"  k={k}:")
        for j, ell, exp in estimate1_exponents(R, S, k):
            status = "passes" if exp <= 0 else "would obstruct"
            print(f"    j={j}, l={ell}: {fmt(exp)} [{status}]")
    print()
    print("Axis-linear 2-dilation exponent R->S:", fmt(linear_2_dilation_exponent(R, S)))
    print("The linear map is very expanding, so the nonlinear pinch is essential.")
    print()
    print("After scaling the domain by lambda=sqrt(C0), where C0 bounds Guth's 2-dilation:")
    print("  R1/S1 gains lambda and has exponent +3/2, so the hypothesis R1 << S1 fails.")
    print("  R3R4/(S3S4) gains lambda^2 and has exponent -3/2.")
    print("  volume ratio gains lambda^4 and has exponent +3.")


if __name__ == "__main__":
    main()
