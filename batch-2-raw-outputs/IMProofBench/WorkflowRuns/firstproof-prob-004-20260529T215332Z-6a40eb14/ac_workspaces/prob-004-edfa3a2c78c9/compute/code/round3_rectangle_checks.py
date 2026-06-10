"""Round 3 exponent checks for the 4D rectangle problem.

All side lengths are represented by powers of L.  The script checks the
specific scaling R=(L^-1,L^4,L^5,L^6), S=(1,1,L^6,L^6), and the residual
map after the short-side stretch, R=(1,L,L^5,L^6).
"""

from fractions import Fraction
from itertools import combinations


def fmt(x: Fraction) -> str:
    if x == 0:
        return "1"
    if x.denominator == 1:
        return f"L^{x.numerator}"
    return f"L^({x.numerator}/{x.denominator})"


def q_exponents(R, S):
    return [s - r for r, s in zip(R, S)]


def estimate1_exponents(R, S, k):
    """Return exponents of Guth Estimate 1 lower-bound monomials."""
    q = q_exponents(R, S)
    out = []
    n = len(R)
    for j in range(0, k):
        for ell in range(k, n + 1):
            exponent = sum(q[:j]) + Fraction(k - j, ell - j) * sum(q[j:ell])
            out.append((j, ell, exponent))
    return out


def boundary_checks(R, S):
    """Guth thesis p.130 n=4,k=2 boundary/double rational-homotopy checks."""
    checks = [
        (
            "boundary RH: R2 R3^2 R4 >= S2 S3^2 S4",
            R[1] + 2 * R[2] + R[3],
            S[1] + 2 * S[2] + S[3],
        ),
        (
            "double RH 1: R1 R2 R3^2 R4 >= S1 S2 S3^2 S4",
            R[0] + R[1] + 2 * R[2] + R[3],
            S[0] + S[1] + 2 * S[2] + S[3],
        ),
        (
            "double RH 2: R1 R2^2 R3^2 R4 >= S1 S2^2 S3^2 S4",
            R[0] + 2 * R[1] + 2 * R[2] + R[3],
            S[0] + 2 * S[1] + 2 * S[2] + S[3],
        ),
        (
            "ellipsoid B1: R2 R3 >= S2 S3",
            R[1] + R[2],
            S[1] + S[2],
        ),
        (
            "ellipsoid B2: R2 R3 R4 >= S2^2 S3 S4",
            R[1] + R[2] + R[3],
            2 * S[1] + S[2] + S[3],
        ),
        (
            "ellipsoid B3a: R2 R3 R4 >= S2^(1/2) S3^(3/2) S4",
            R[1] + R[2] + R[3],
            Fraction(1, 2) * S[1] + Fraction(3, 2) * S[2] + S[3],
        ),
        (
            "ellipsoid B3b: R3 R4 >= S3 S4",
            R[2] + R[3],
            S[2] + S[3],
        ),
    ]
    return checks


def target_ratios(R, S):
    desired = S[0] + Fraction(1, 2) * S[1] + Fraction(3, 2) * S[2] + S[3]
    return [
        ("R1/S1", R[0] - S[0]),
        ("R3 R4 / (S3 S4)", R[2] + R[3] - S[2] - S[3]),
        ("Vol(R)/(S1 S2^(1/2) S3^(3/2) S4)", sum(R) - desired),
        ("R1 R2^2 / (S1 S2 S3)", R[0] + 2 * R[1] - S[0] - S[1] - S[2]),
    ]


def linear_2_dilation_exponent(R, S):
    q = q_exponents(R, S)
    return max(q[i] + q[j] for i, j in combinations(range(len(q)), 2))


def report_case(name, R, S):
    lines = [f"## {name}", f"R exponents = {R}", f"S exponents = {S}", ""]
    lines.append("Target/complement ratios:")
    for label, exponent in target_ratios(R, S):
        lines.append(f"  {label}: {fmt(exponent)}")
    lines.append("")
    lines.append(f"Axis-linear 2-dilation exponent: {fmt(linear_2_dilation_exponent(R, S))}")
    lines.append("")
    for k in (2, 3, 4):
        lines.append(f"Guth Estimate 1 lower-bound exponents for k={k}:")
        for j, ell, exponent in estimate1_exponents(R, S, k):
            flag = "OK for bounded maps" if exponent <= 0 else "rules out bounded maps"
            lines.append(f"  j={j}, l={ell}: {fmt(exponent)}  [{flag}]")
        lines.append("")
    lines.append("Boundary / rational-homotopy / ellipsoid checks:")
    for label, left, right in boundary_checks(R, S):
        diff = left - right
        status = "passes up to constants" if diff >= 0 else "fails by " + fmt(-diff)
        lines.append(f"  {label}: left {fmt(left)}, right {fmt(right)}, ratio {fmt(diff)} [{status}]")
    lines.append("")
    return "\n".join(lines)


def main():
    S = [Fraction(0), Fraction(0), Fraction(6), Fraction(6)]
    full = [Fraction(-1), Fraction(4), Fraction(5), Fraction(6)]
    residual = [Fraction(0), Fraction(1), Fraction(5), Fraction(6)]
    print(report_case("full scaling test", full, S))
    print(report_case("residual after short-side stretch", residual, S))


if __name__ == "__main__":
    main()
