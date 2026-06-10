from fractions import Fraction


def fp(x):
    return Fraction(x)


def fmt_power(q):
    if q == 0:
        return "1"
    return f"L^{q}"


def add(*xs):
    s = Fraction(0)
    for x in xs:
        s += x
    return s


def original_sequence():
    D0 = [fp(-7), fp(0), fp(1), fp(1)]
    D1 = [fp(-6), fp(-3), fp(1), fp(1)]
    P = [fp(Fraction(-13, 2)), fp(Fraction(-13, 2)), fp(Fraction(-13, 2)), fp(12)]
    S = [fp(Fraction(-13, 2)), fp(Fraction(-13, 2)), fp(0), fp(Fraction(11, 2))]

    print("Original exponent vectors for powers of L")
    for name, v in [("D0", D0), ("D1", D1), ("P", P), ("S", S)]:
        print(f"  {name}: {v}")

    print("\nGuth hypotheses, original non-strict form")
    print(f"  Step 1 short-side stretch: A^4 exponent = 4, R2/R1 exponent = {D0[1] - D0[0]}")
    a = Fraction(-13, 2)
    b = Fraction(12)
    print(f"  Step 2 pinching: a exponent = {a}, R1 exponent = {D1[0]}")
    print(f"  Step 2 pinching: a^2 b exponent = {2*a+b}, R2 R3 R4 exponent = {D1[1]+D1[2]+D1[3]}")
    print(f"  Step 3 interpolated stretch: A^4 exponent = 0, R2/R1 exponent = {P[1]-P[0]}")
    print(f"  Step 3 interpolated stretch: R3 exponent = {P[2]}, A exponent = 0")
    print(f"  Step 3 interpolated stretch: sqrt(R3 R4) exponent = {(P[2]+P[3])/2}")

    print("\nBad-ratio exponents before fixed lambda scaling")
    print(f"  R1/S1: {D0[0]-S[0]}")
    print(f"  R3 R4 / (S3 S4): {D0[2]+D0[3]-S[2]-S[3]}")
    weighted_S = S[0] + S[1] / 2 + 3 * S[2] / 2 + S[3]
    print(f"  Vol(D0)/(S1 S2^1/2 S3^3/2 S4): {sum(D0)-weighted_S}")


def strict_perturbation():
    print("\nOne strict-inequality perturbation")
    print("  Fix constants 0 < alpha < 1 and mu > 1.")
    print("  Step 2 use a = alpha L^(-13/2), b = L^12.")
    print("  Then a^2 b = alpha^2 L^-1 < L^-1 = R2 R3 R4.")
    print("  Insert the bounded linear map")
    print("      (a,a,a,L^12) -> (a, mu a, a, L^12/mu).")
    print("  Step 3 uses A = 1, now with R2/R1 = mu > 1.")
    print("  The final target is")
    print("      S' = (alpha L^(-13/2), mu alpha L^(-13/2), 1, alpha mu^-1 L^(11/2)).")
    print("  After scaling D0 by lambda = C0^(1/2), the three ratios are")
    print("      (lambda/alpha) L^(-1/2),")
    print("      (lambda^2 mu/alpha) L^(-7/2),")
    print("      lambda^4 alpha^(-5/2) mu^(1/2) L^(-3/4).")
    print("  Hence all still tend to zero as L -> infinity.")


if __name__ == "__main__":
    original_sequence()
    strict_perturbation()
