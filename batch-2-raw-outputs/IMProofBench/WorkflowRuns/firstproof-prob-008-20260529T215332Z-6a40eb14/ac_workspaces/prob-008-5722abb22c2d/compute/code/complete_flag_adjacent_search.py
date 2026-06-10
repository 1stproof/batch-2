#!/usr/bin/env python3
"""Finite-domain checks for the complete-flag adjacent-relation criterion.

For a rank-r matroid M on E, we fix g_0(empty)=0 and g_r=mu_M
(0 on bases of M, INF otherwise).  For middle ranks, variables range over a
small finite alphabet including INF.  Z3 is asked whether all adjacent
three-term incidence relations can hold while some chosen middle rank slice
violates a tropical Plucker relation.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
import json
from typing import Dict, Iterable, List, Sequence, Tuple

import z3

from flat_duality_tests import (
    INF as OLD_INF,
    Matroid,
    bits,
    boolean_matroid,
    direct_sum_u23_u23,
    fano_matroid,
    uniform_rank_2,
)


def bit_iter(mask: int) -> Iterable[int]:
    i = 0
    while mask:
        if mask & 1:
            yield i
        mask >>= 1
        i += 1


def subsets_of_size(n: int, k: int) -> List[int]:
    if k < 0 or k > n:
        return []
    return [bits(c) for c in combinations(range(n), k)]


def zmin_twice(terms: Sequence[z3.ArithRef]) -> z3.BoolRef:
    if len(terms) <= 1:
        return z3.BoolVal(True)
    witnesses = []
    for i in range(len(terms)):
        for j in range(i + 1, len(terms)):
            witnesses.append(
                z3.And(
                    terms[i] == terms[j],
                    *[terms[i] <= terms[k] for k in range(len(terms))],
                )
            )
    return z3.Or(*witnesses)


@dataclass
class Z3FlagModel:
    M: Matroid
    finite_values: Sequence[int]
    timeout_ms: int = 5_000
    enforce_support_matroids: bool = False

    def __post_init__(self) -> None:
        self.inf = len(self.finite_values)
        self.sum_inf = 10_000
        self.by_size = {k: subsets_of_size(self.M.n, k) for k in range(self.M.n + 1)}
        self.vars: Dict[Tuple[int, int], z3.IntNumRef | z3.Int] = {}

    def const_value(self, k: int, subset: int) -> int:
        if k == 0:
            return 0 if subset == 0 else self.inf
        if k == self.M.r:
            return 0 if self.M.rank(subset) == self.M.r else self.inf
        raise KeyError((k, subset))

    def var(self, k: int, subset: int):
        if k in (0, self.M.r):
            return z3.IntVal(self.const_value(k, subset))
        key = (k, subset)
        if key not in self.vars:
            self.vars[key] = z3.Int(f"g_{k}_{subset}")
        return self.vars[key]

    def add_term(self, a, b):
        return z3.If(z3.Or(a == self.inf, b == self.inf), self.sum_inf, a + b)

    def ordinary_min_twice_or_none(self, finite_flags: Sequence[z3.BoolRef]) -> z3.BoolRef:
        count = z3.Sum([z3.If(flag, 1, 0) for flag in finite_flags])
        return z3.Or(count == 0, count >= 2)

    def base_solver(self) -> z3.Solver:
        solver = z3.Solver()
        solver.set("timeout", self.timeout_ms)

        # Finite alphabet plus INF, and a nonzero slice at every middle rank.
        for k in range(1, self.M.r):
            finite_somewhere = []
            for subset in self.by_size[k]:
                v = self.var(k, subset)
                solver.add(v >= 0, v <= self.inf)
                finite_somewhere.append(v < self.inf)
            solver.add(z3.Or(*finite_somewhere))

        if self.enforce_support_matroids:
            # The finite coordinates in each homogeneous layer must be the
            # bases of an ordinary matroid.  In 0/infinity form this is the
            # no-unique-finite-term version of the 3-term Pluecker relations.
            for k in range(2, self.M.r):
                for S in self.by_size[k - 2]:
                    outside = [e for e in range(self.M.n) if not (S >> e) & 1]
                    for a, b, c, d in combinations(outside, 4):
                        finite_flags = [
                            z3.And(
                                self.var(k, S | (1 << a) | (1 << b)) < self.inf,
                                self.var(k, S | (1 << c) | (1 << d)) < self.inf,
                            ),
                            z3.And(
                                self.var(k, S | (1 << a) | (1 << c)) < self.inf,
                                self.var(k, S | (1 << b) | (1 << d)) < self.inf,
                            ),
                            z3.And(
                                self.var(k, S | (1 << a) | (1 << d)) < self.inf,
                                self.var(k, S | (1 << b) | (1 << c)) < self.inf,
                            ),
                        ]
                        solver.add(self.ordinary_min_twice_or_none(finite_flags))

        # Adjacent three-term incidence for ranks d,d+1, d=1,...,r-1.
        for d in range(1, self.M.r):
            for S in self.by_size[d - 1]:
                outside = [e for e in range(self.M.n) if not (S >> e) & 1]
                for x, y, z in combinations(outside, 3):
                    terms = [
                        self.add_term(
                            self.var(d, S | (1 << x)),
                            self.var(d + 1, S | (1 << y) | (1 << z)),
                        ),
                        self.add_term(
                            self.var(d, S | (1 << y)),
                            self.var(d + 1, S | (1 << x) | (1 << z)),
                        ),
                        self.add_term(
                            self.var(d, S | (1 << z)),
                            self.var(d + 1, S | (1 << x) | (1 << y)),
                        ),
                    ]
                    solver.add(zmin_twice(terms))
        return solver

    def plucker_failure_formula(self, k: int):
        failures = []
        if k < 2 or k >= self.M.r:
            return z3.BoolVal(False)
        for S in self.by_size[k - 2]:
            outside = [e for e in range(self.M.n) if not (S >> e) & 1]
            for a, b, c, d in combinations(outside, 4):
                terms = [
                    self.add_term(
                        self.var(k, S | (1 << a) | (1 << b)),
                        self.var(k, S | (1 << c) | (1 << d)),
                    ),
                    self.add_term(
                        self.var(k, S | (1 << a) | (1 << c)),
                        self.var(k, S | (1 << b) | (1 << d)),
                    ),
                    self.add_term(
                        self.var(k, S | (1 << a) | (1 << d)),
                        self.var(k, S | (1 << b) | (1 << c)),
                    ),
                ]
                failures.append(z3.Not(zmin_twice(terms)))
        return z3.Or(*failures) if failures else z3.BoolVal(False)

    def find_plucker_counterexample(self, k: int) -> Dict[str, object]:
        solver = self.base_solver()
        solver.add(self.plucker_failure_formula(k))
        status = solver.check()
        out: Dict[str, object] = {
            "rank": k,
            "status": str(status),
            "plucker_relations_exist": k >= 2 and k < self.M.r,
        }
        if status == z3.sat:
            model = solver.model()
            vals = []
            for subset in self.by_size[k]:
                raw = model.eval(self.var(k, subset), model_completion=True).as_long()
                vals.append("INF" if raw == self.inf else raw)
            out["valuation"] = {
                "subsets": [tuple(bit_iter(s)) for s in self.by_size[k]],
                "values": vals,
            }
        return out


def run() -> Dict[str, object]:
    cases: List[Matroid] = [
        boolean_matroid(4),
        boolean_matroid(5),
        uniform_rank_2(4, perm=[1, 0, 3, 2]),
        uniform_rank_2(5, perm=[1, 0, 3, 2, 4]),
        fano_matroid(),
        direct_sum_u23_u23(),
    ]
    alphabets = [[0, 1], [0, 1, 2]]
    results = []
    for M in cases:
        for finite_values in alphabets:
            model = Z3FlagModel(M, finite_values)
            checks = [
                model.find_plucker_counterexample(k)
                for k in range(1, M.r)
            ]
            results.append(
                {
                    "matroid": M.name,
                    "n": M.n,
                    "rank": M.r,
                    "alphabet": finite_values + ["INF"],
                    "checks": checks,
                }
            )
    return {
        "description": (
            "Z3 search for adjacent complete flags with trivial endpoints and a "
            "middle rank slice violating tropical Plucker."
        ),
        "inf_encoding_note": "INF is encoded as a distinguished alphabet value; sums involving INF are treated as INF.",
        "results": results,
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
