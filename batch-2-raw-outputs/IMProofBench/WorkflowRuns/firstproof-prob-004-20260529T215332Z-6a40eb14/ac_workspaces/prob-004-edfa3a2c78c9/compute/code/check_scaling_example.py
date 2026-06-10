"""Check the high-aspect 4D rectangle scaling against known estimates.

All side lengths are encoded as powers of eps: length = eps**exponent,
for eps -> 0+.  An inequality A >= c B is asymptotically satisfied iff
exponent(A/B) <= 0.
"""

from fractions import Fraction


S = {
    "S1": Fraction(0),
    "S2": Fraction(0),
    "S3": Fraction(-6),
    "S4": Fraction(-6),
}
R = {
    "R1": Fraction(1),
    "R2": Fraction(-4),
    "R3": Fraction(-5),
    "R4": Fraction(-6),
}


def eprod(names):
    total = Fraction(0)
    for name in names:
        total += (R if name.startswith("R") else S)[name]
    return total


def ratio_exp(left, right):
    return left - right


checks = [
    ("assumption R1/S1", R["R1"] - S["S1"]),
    ("first alternative ratio R3R4/(S3S4)", eprod(["R3", "R4"]) - eprod(["S3", "S4"])),
    (
        "volume target ratio Vol(R)/(S1 S2^(1/2) S3^(3/2) S4)",
        eprod(["R1", "R2", "R3", "R4"])
        - (S["S1"] + S["S2"] / 2 + 3 * S["S3"] / 2 + S["S4"]),
    ),
    ("G j=0,l=2: R1R2/(S1S2)", eprod(["R1", "R2"]) - eprod(["S1", "S2"])),
    ("G j=0,l=3: R1R2R3/(S1S2S3)", eprod(["R1", "R2", "R3"]) - eprod(["S1", "S2", "S3"])),
    ("G j=1,l=3: R1^2 R2R3/(S1^2 S2S3)", 2 * R["R1"] + R["R2"] + R["R3"] - (2 * S["S1"] + S["S2"] + S["S3"])),
    ("G j=0,l=4: Vol(R)/Vol(S)", eprod(["R1", "R2", "R3", "R4"]) - eprod(["S1", "S2", "S3", "S4"])),
    ("G j=1,l=4: R1^2 Vol(R)/(S1^2 Vol(S))", 2 * R["R1"] + eprod(["R1", "R2", "R3", "R4"]) - (2 * S["S1"] + eprod(["S1", "S2", "S3", "S4"]))),
    ("Dil3 j=1,l=4", Fraction(3, 2) * R["R1"] + R["R2"] + R["R3"] + R["R4"] - (Fraction(3, 2) * S["S1"] + S["S2"] + S["S3"] + S["S4"])),
    ("Dil3 j=2,l=4", 2 * (R["R1"] + R["R2"]) + R["R3"] + R["R4"] - (2 * (S["S1"] + S["S2"]) + S["S3"] + S["S4"])),
    ("Thesis Prop 8.1.3 antecedent ratio R1R2^2/(S1S2S3)", R["R1"] + 2 * R["R2"] - (S["S1"] + S["S2"] + S["S3"])),
    ("Thesis p130 boundary rational-homotopy ratio", R["R2"] + 2 * R["R3"] + R["R4"] - (S["S2"] + 2 * S["S3"] + S["S4"])),
    ("Thesis p130 double ratio 1", R["R1"] + R["R2"] + 2 * R["R3"] + R["R4"] - (S["S1"] + S["S2"] + 2 * S["S3"] + S["S4"])),
    ("Thesis p130 double ratio 2", R["R1"] + 2 * R["R2"] + 2 * R["R3"] + R["R4"] - (S["S1"] + 2 * S["S2"] + 2 * S["S3"] + S["S4"])),
]


print("Scaling: S=(1,1,eps^-6,eps^-6), R=(eps,eps^-4,eps^-5,eps^-6)")
print("A ratio exponent <= 0 means the corresponding lower-bound inequality is satisfied.")
for name, exp in checks:
    verdict = "small" if exp > 0 else "large/satisfied"
    print(f"{name:72s} eps^{exp!s:>5s}  {verdict}")
