"""Round 27 weighted f1-level checks.

This script records the algebraic quantities behind the f1-level probe.
It is not a proof engine; it verifies the two scale computations used in
the response:

1. The unrestricted global identity map gives a genuine degree-one
   2-contracting map whose f1-level weighted volume is too small for the
   desired anisotropic 3D estimate when S3 >> S2.
2. Averaging the weighted level integral is exactly the volume of the
   corresponding f1-slab, so the hard-regime averaged statement is the
   desired volume estimate localized to that slab.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class IdentityModel:
    s1: float
    s2: float
    s3: float
    s4: float

    @property
    def level_weighted_volume(self) -> float:
        # M_t = [0,S2] x [0,S3] x [0,S4], w = 1.
        return self.s2 * self.s3 * self.s4

    @property
    def desired_level_bound(self) -> float:
        return (self.s2**0.5) * (self.s3**1.5) * self.s4

    @property
    def central_slab_volume(self) -> float:
        # Ignore harmless central-half constants.
        return self.s1 * self.level_weighted_volume

    @property
    def desired_slab_bound(self) -> float:
        return self.s1 * self.desired_level_bound


def main() -> None:
    print("# Round 27 weighted f1-level probe")
    print()
    print("Identity model: R=S=(1,1,L,L), f=id, central f1-levels.")
    print("For each L, Dil_2(f)=1 and the level map g is degree one.")
    print()
    print("| L | int_M w | desired S2^1/2 S3^3/2 S4 | ratio | slab ratio |")
    print("|---:|---:|---:|---:|---:|")
    for L in [10, 100, 10_000]:
        model = IdentityModel(1.0, 1.0, float(L), float(L))
        ratio = model.level_weighted_volume / model.desired_level_bound
        slab_ratio = model.central_slab_volume / model.desired_slab_bound
        print(
            f"| {L:g} | {model.level_weighted_volume:.6g} | "
            f"{model.desired_level_bound:.6g} | {ratio:.6g} | {slab_ratio:.6g} |"
        )
    print()
    print("The ratio is L^{-1/2}; hence no unrestricted weighted level theorem is possible.")
    print("For any map u=f1, coarea gives")
    print("  int_I int_{<R,u,t>} |grad u|^{-1} dH^3 dt = Vol(u^{-1}(I)).")
    print("Thus the hard-regime averaged strengthening is exactly a central-slab volume lower bound.")


if __name__ == "__main__":
    main()
