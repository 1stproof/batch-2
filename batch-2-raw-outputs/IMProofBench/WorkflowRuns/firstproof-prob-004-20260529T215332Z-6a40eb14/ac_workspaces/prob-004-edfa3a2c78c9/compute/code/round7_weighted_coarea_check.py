"""Round 7 checks for the weighted coarea replacement.

The script has two independent parts.

1. Random linear-algebra stress tests for the pointwise estimate

       lambda(A,B)^2 * J_2(B) <= ||Lambda^2(A,B)||^2,

   where B is the last two rows of a 4 x 4 differential, T=ker B,
   lambda is the operator norm of the first two rows restricted to T,
   and J_2(B) is the 2-Jacobian of B.

2. Exponent bookkeeping for the simple fiber model showing that the
   proposed fiber-energy lower bound is false without the full ambient
   two-Jacobian hypotheses.
"""

from __future__ import annotations

from fractions import Fraction

import numpy as np


def exterior_2_norm(m: np.ndarray) -> float:
    """Operator norm of Lambda^2 m, i.e. product of top two singular values."""
    s = np.linalg.svd(m, compute_uv=False)
    if len(s) < 2:
        return 0.0
    return float(s[0] * s[1])


def kernel_basis(b: np.ndarray, tol: float = 1e-10) -> np.ndarray:
    """Return an orthonormal basis for ker(b) as columns."""
    _, s, vh = np.linalg.svd(b)
    rank = int((s > tol).sum())
    return vh[rank:].T


def lambda_on_kernel(m: np.ndarray) -> float:
    a = m[:2, :]
    b = m[2:, :]
    k = kernel_basis(b)
    if k.shape[1] == 0:
        return 0.0
    return float(np.linalg.svd(a @ k, compute_uv=False)[0])


def j2_of_f(m: np.ndarray) -> float:
    b = m[2:, :]
    s = np.linalg.svd(b, compute_uv=False)
    return float(s[0] * s[1])


def random_stress(seed: int = 7, n: int = 20_000) -> list[str]:
    rng = np.random.default_rng(seed)
    worst = 0.0
    worst_tuple: tuple[float, float, float, float] | None = None
    failures = 0
    for _ in range(n):
        # Use anisotropic random matrices to stress near-rank-deficient and
        # highly stretched cases.
        u, _ = np.linalg.qr(rng.normal(size=(4, 4)))
        v, _ = np.linalg.qr(rng.normal(size=(4, 4)))
        exponents = rng.uniform(-3.0, 3.0, size=4)
        s = np.diag(np.exp(exponents))
        m = u @ s @ v.T

        dil2 = exterior_2_norm(m)
        lam = lambda_on_kernel(m)
        jf = j2_of_f(m)
        ratio = 0.0 if dil2 == 0 else (lam * lam * jf) / (dil2 * dil2)
        if ratio > worst:
            worst = ratio
            worst_tuple = (lam, jf, dil2, ratio)
        if ratio > 1 + 1e-8:
            failures += 1

    lines = ["# weighted coarea linear-algebra stress test"]
    lines.append(f"samples: {n}")
    lines.append(f"failures above 1+1e-8: {failures}")
    if worst_tuple is not None:
        lam, jf, dil2, ratio = worst_tuple
        lines.append(f"worst ratio lambda^2 J_F / Dil_2^2: {ratio:.12g}")
        lines.append(f"  lambda={lam:.12g}, J_F={jf:.12g}, Dil_2={dil2:.12g}")
    return lines


def ffmt(x: Fraction) -> str:
    if x.denominator == 1:
        return str(x.numerator)
    return f"{x.numerator}/{x.denominator}"


def model_exponents() -> list[str]:
    """Bookkeeping for S=(1,1,L,L), R=(L^-1/5,L^3/5,cL,cL)."""
    r1, r2, r3, r4 = Fraction(-1, 5), Fraction(3, 5), Fraction(1), Fraction(1)
    s1, s2, s3, s4 = Fraction(0), Fraction(0), Fraction(1), Fraction(1)
    v = r1 + r2 + r3 + r4
    desired = s1 + s2 / 2 + 3 * s3 / 2 + s4
    energy_needed = s1 + s2 / 2 + s3 / 2

    # Model fibers are long (u3,u4)-rectangles.  The model map is
    # (u3/(cL), u4/(cL), L u1/R1, L u2/R2).
    fiber_area = r3 + r4
    lam = Fraction(-1)  # constants in c ignored
    energy = 2 * lam + fiber_area
    fill = r1 + fiber_area  # calibration in the short normal direction
    normal_op = s3 - r1
    mixed = lam + normal_op
    normal_j = (s3 - r1) + (s4 - r2)

    lines = ["# hard exponent fiber model"]
    lines.append("S exponents: (0, 0, 1, 1)")
    lines.append("R exponents: (-1/5, 3/5, 1, 1), constants c on R3,R4 ignored")
    lines.append(f"volume exponent: {ffmt(v)}")
    lines.append(f"desired theorem RHS exponent: {ffmt(desired)}")
    lines.append(f"volume gap exponent V/RHS: {ffmt(v - desired)}")
    lines.append(f"per-fiber energy needed for weighted coarea closure: {ffmt(energy_needed)}")
    lines.append("Guth/first-alternative exponent margins for the hard model:")
    checks = [
        ("R1 R2 >= S1 S2", r1 + r2 - s1 - s2),
        ("R1 R2 R3 >= S1 S2 S3", r1 + r2 + r3 - s1 - s2 - s3),
        ("R1^2 R2 R3 >= S1^2 S2 S3", 2 * r1 + r2 + r3 - 2 * s1 - s2 - s3),
        ("Vol >= Vol(S)", v - (s1 + s2 + s3 + s4)),
        ("R1^3 R2 R3 R4 >= S1^3 S2 S3 S4", 3 * r1 + r2 + r3 + r4 - (3 * s1 + s2 + s3 + s4)),
        ("R1 R2^2 >= S1 S2 S3", r1 + 2 * r2 - (s1 + s2 + s3)),
    ]
    for label, margin in checks:
        lines.append(f"  {label}: {ffmt(margin)}")
    lines.append("")
    lines.append("Long-fiber model Z_y = {u1,u2 fixed} x [0,cL]^2:")
    lines.append(f"  fiber area exponent: {ffmt(fiber_area)}")
    lines.append(f"  lambda exponent for g=(u3/(cL),u4/(cL)): {ffmt(lam)}")
    lines.append(f"  energy exponent int_Z lambda^2: {ffmt(energy)}")
    lines.append(f"  source filling lower exponent from short-normal calibration: {ffmt(fill)}")
    lines.append(f"  mixed one-tangent/one-normal exponent lambda * ||dF||: {ffmt(mixed)}")
    lines.append(f"  pure normal J_F exponent: {ffmt(normal_j)}")
    return lines


def main() -> None:
    for line in random_stress():
        print(line)
    print()
    for line in model_exponents():
        print(line)


if __name__ == "__main__":
    main()
