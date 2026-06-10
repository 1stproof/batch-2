#!/usr/bin/env python3
"""Z3 search for the first arbitrary-rank flat-opposition gap in PG(3,2).

The searched configuration is:

    p rank 1, q rank 3, p <= q <= mu_M,  M = PG(3,2), rank(M)=4.

Variables are flat-constant:
    p_X for rank-1 flats X (points),
    q_Y for rank-3 flats Y (planes).

For a subset coordinate the value is INF if the subset is dependent or has
the wrong closure rank; otherwise it is the variable of its closure.  The
script imposes full tropical Plucker and incidence relations, then asserts a
unique-min violation of q^perp <= p^perp.
"""

from __future__ import annotations

import argparse
import json
import time
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

import z3


def bit_iter(mask: int) -> Iterable[int]:
    i = 0
    while mask:
        if mask & 1:
            yield i
        mask >>= 1
        i += 1


def bits(items: Iterable[int]) -> int:
    out = 0
    for i in items:
        out |= 1 << i
    return out


def popcount(mask: int) -> int:
    return mask.bit_count()


def gf2_rank(vectors: Iterable[int]) -> int:
    basis: List[int] = []
    for v in vectors:
        x = v
        for b in basis:
            x = min(x, x ^ b)
        if x:
            pivot = x.bit_length() - 1
            for j, b in enumerate(basis):
                if (b >> pivot) & 1:
                    basis[j] = b ^ x
            basis.append(x)
            basis.sort(reverse=True)
    return len(basis)


@dataclass
class PG32:
    """The simple matroid of nonzero vectors in F_2^4."""

    def __post_init__(self) -> None:
        self.vecs = list(range(1, 16))
        self.n = len(self.vecs)
        self.rank = 4
        self.top = (1 << self.n) - 1
        self.by_size = {
            k: [bits(c) for c in combinations(range(self.n), k)]
            for k in range(self.n + 1)
        }
        self.rank_cache = [self._rank_uncached(s) for s in range(1 << self.n)]
        self.closure_cache = [self._closure_uncached(s) for s in range(1 << self.n)]
        self.flats = [s for s in range(1 << self.n) if self.closure_cache[s] == s]
        self.flats_by_rank = {
            k: [f for f in self.flats if self.rank_cache[f] == k]
            for k in range(self.rank + 1)
        }
        self.flat_index = {
            k: {f: i for i, f in enumerate(self.flats_by_rank[k])}
            for k in range(self.rank + 1)
        }
        self.orth_cache = {f: self._orthogonal_flat(f) for f in self.flats}

    def _rank_uncached(self, subset: int) -> int:
        return gf2_rank(self.vecs[i] for i in bit_iter(subset))

    def _span_mask(self, subset: int) -> int:
        basis = [self.vecs[i] for i in bit_iter(subset)]
        out_vecs = {0}
        for v in basis:
            out_vecs |= {x ^ v for x in list(out_vecs)}
        out = 0
        for idx, v in enumerate(self.vecs):
            if v in out_vecs:
                out |= 1 << idx
        return out

    def _closure_uncached(self, subset: int) -> int:
        return self._span_mask(subset)

    @staticmethod
    def dot(u: int, v: int) -> int:
        return popcount(u & v) & 1

    def _orthogonal_flat(self, flat: int) -> int:
        out = 0
        for idx, v in enumerate(self.vecs):
            if all(self.dot(v, self.vecs[j]) == 0 for j in bit_iter(flat)):
                out |= 1 << idx
        return out

    def rank_of(self, subset: int) -> int:
        return self.rank_cache[subset]

    def closure(self, subset: int) -> int:
        return self.closure_cache[subset]

    def independent(self, subset: int) -> bool:
        return self.rank_of(subset) == popcount(subset)

    def orth(self, flat: int) -> int:
        return self.orth_cache[flat]

    def name_subset(self, subset: int) -> Tuple[int, ...]:
        return tuple(self.vecs[i] for i in bit_iter(subset))


class PG32Search:
    def __init__(self, K: int, allow_inf: bool, timeout_ms: int) -> None:
        self.M = PG32()
        self.K = K
        self.allow_inf = allow_inf
        self.inf = K + 1
        self.big = 10_000
        self.timeout_ms = timeout_ms
        self.p_vars = [z3.Int(f"p_{i}") for i in range(len(self.M.flats_by_rank[1]))]
        self.q_vars = [z3.Int(f"q_{i}") for i in range(len(self.M.flats_by_rank[3]))]
        self.constraint_counts: Dict[str, int] = {
            "domain": 0,
            "normalization": 0,
            "q_plucker": 0,
            "q_mu_incidence": 0,
            "p_q_incidence": 0,
            "violation_disjuncts": 0,
        }

    def finite_domain_values(self) -> List[int]:
        vals = list(range(self.K + 1))
        if self.allow_inf:
            vals.append(self.inf)
        return vals

    def value_from_vars(self, vars_: Sequence[z3.ArithRef], rank: int, subset: int):
        if popcount(subset) != rank or not self.M.independent(subset):
            return z3.IntVal(self.inf)
        flat = self.M.closure(subset)
        if self.M.rank_of(flat) != rank:
            return z3.IntVal(self.inf)
        return vars_[self.M.flat_index[rank][flat]]

    def p(self, subset: int):
        return self.value_from_vars(self.p_vars, 1, subset)

    def q(self, subset: int):
        return self.value_from_vars(self.q_vars, 3, subset)

    def mu(self, subset: int):
        if popcount(subset) == 4 and self.M.independent(subset):
            return z3.IntVal(0)
        return z3.IntVal(self.inf)

    def add_term(self, a, b):
        return z3.If(z3.Or(a == self.inf, b == self.inf), self.big, a + b)

    def min_twice(self, terms: Sequence[z3.ArithRef]):
        witnesses = []
        for i in range(len(terms)):
            for j in range(i + 1, len(terms)):
                witnesses.append(
                    z3.And(
                        terms[i] == terms[j],
                        *[terms[i] <= terms[k] for k in range(len(terms))],
                    )
                )
        return z3.Or(*witnesses) if witnesses else z3.BoolVal(True)

    def unique_min_somewhere(self, terms_by_label: Sequence[Tuple[int, List[z3.ArithRef]]]):
        disjuncts = []
        for T, terms in terms_by_label:
            for i, term in enumerate(terms):
                disjuncts.append(
                    z3.And(
                        term < self.big,
                        *[term < other for j, other in enumerate(terms) if j != i],
                    )
                )
        self.constraint_counts["violation_disjuncts"] = len(disjuncts)
        return z3.Or(*disjuncts)

    def q_perp(self, subset: int):
        if popcount(subset) != 1 or not self.M.independent(subset):
            return z3.IntVal(self.inf)
        point = self.M.closure(subset)
        plane = self.M.orth(point)
        return self.q_vars[self.M.flat_index[3][plane]]

    def p_perp(self, subset: int):
        if popcount(subset) != 3 or not self.M.independent(subset):
            return z3.IntVal(self.inf)
        plane = self.M.closure(subset)
        point = self.M.orth(plane)
        return self.p_vars[self.M.flat_index[1][point]]

    def build_solver(self) -> Tuple[z3.Solver, List[Tuple[int, List[z3.ArithRef]]]]:
        solver = z3.Solver()
        solver.set("timeout", self.timeout_ms)
        domain = self.finite_domain_values()
        for v in self.p_vars + self.q_vars:
            solver.add(z3.Or(*[v == d for d in domain]))
            self.constraint_counts["domain"] += 1

        solver.add(z3.Or(*[v == 0 for v in self.p_vars]))
        solver.add(z3.Or(*[v == 0 for v in self.q_vars]))
        self.constraint_counts["normalization"] += 2

        # Full tropical Plucker for q, rank 3.
        for S in self.M.by_size[1]:
            outside = [e for e in range(self.M.n) if not (S >> e) & 1]
            for a, b, c, d in combinations(outside, 4):
                terms = [
                    self.add_term(
                        self.q(S | (1 << a) | (1 << b)),
                        self.q(S | (1 << c) | (1 << d)),
                    ),
                    self.add_term(
                        self.q(S | (1 << a) | (1 << c)),
                        self.q(S | (1 << b) | (1 << d)),
                    ),
                    self.add_term(
                        self.q(S | (1 << a) | (1 << d)),
                        self.q(S | (1 << b) | (1 << c)),
                    ),
                ]
                solver.add(self.min_twice(terms))
                self.constraint_counts["q_plucker"] += 1

        # Full incidence q <= mu_M, ranks 3 <= 4.
        for S in self.M.by_size[2]:
            rest = [e for e in range(self.M.n) if not (S >> e) & 1]
            for extra in combinations(rest, 3):
                T = S | bits(extra)
                terms = [
                    self.add_term(self.q(S | (1 << i)), self.mu(T & ~(1 << i)))
                    for i in bit_iter(T & ~S)
                ]
                solver.add(self.min_twice(terms))
                self.constraint_counts["q_mu_incidence"] += 1

        # Full incidence p <= q, ranks 1 <= 3.
        for T in self.M.by_size[4]:
            terms = [
                self.add_term(self.p(1 << i), self.q(T & ~(1 << i)))
                for i in bit_iter(T)
            ]
            solver.add(self.min_twice(terms))
            self.constraint_counts["p_q_incidence"] += 1

        # Transformed incidence q^perp <= p^perp, ranks 1 <= 3.
        transformed_terms = []
        for T in self.M.by_size[4]:
            terms = [
                self.add_term(self.q_perp(1 << i), self.p_perp(T & ~(1 << i)))
                for i in bit_iter(T)
            ]
            transformed_terms.append((T, terms))
        solver.add(self.unique_min_somewhere(transformed_terms))
        return solver, transformed_terms

    def decode_vars(self, model: z3.ModelRef, vars_: Sequence[z3.ArithRef]) -> List[int | str]:
        out: List[int | str] = []
        for v in vars_:
            raw = model.eval(v, model_completion=True).as_long()
            out.append("INF" if self.allow_inf and raw == self.inf else raw)
        return out

    def find_witness(self, model: z3.ModelRef) -> Dict[str, object] | None:
        for T in self.M.by_size[4]:
            raw_terms = []
            for i in bit_iter(T):
                term = self.add_term(self.q_perp(1 << i), self.p_perp(T & ~(1 << i)))
                raw_terms.append((i, model.eval(term, model_completion=True).as_long()))
            finite = [(i, v) for i, v in raw_terms if v < self.big]
            if finite:
                m = min(v for _, v in finite)
                winners = [i for i, v in finite if v == m]
                if len(winners) == 1:
                    return {
                        "T_point_vectors": self.M.name_subset(T),
                        "terms": [
                            {
                                "deleted_point_vector": self.M.vecs[i],
                                "value": "INF" if v >= self.big else v,
                            }
                            for i, v in raw_terms
                        ],
                        "unique_winner_deleted_point_vector": self.M.vecs[winners[0]],
                    }
        return None

    def run(self) -> Dict[str, object]:
        start = time.time()
        solver, _ = self.build_solver()
        status = solver.check()
        elapsed = time.time() - start
        result: Dict[str, object] = {
            "matroid": "PG(3,2)",
            "rank": 4,
            "points": len(self.M.flats_by_rank[1]),
            "planes": len(self.M.flats_by_rank[3]),
            "K": self.K,
            "allow_inf": self.allow_inf,
            "status": str(status),
            "elapsed_seconds": elapsed,
            "timeout_ms": self.timeout_ms,
            "constraint_counts": self.constraint_counts,
            "encoding": {
                "point_vectors": self.M.vecs,
                "finite_values": list(range(self.K + 1)),
                "inf_code": self.inf if self.allow_inf else None,
                "normalization": "min p = 0 and min q = 0, encoded by some flat variable equal to 0 in each rank",
            },
        }
        if status == z3.sat:
            model = solver.model()
            result["p_values_by_point_vector"] = dict(
                zip(map(str, self.M.vecs), self.decode_vars(model, self.p_vars))
            )
            result["q_values_by_plane_point_vectors"] = {
                str(self.M.name_subset(flat)): value
                for flat, value in zip(
                    self.M.flats_by_rank[3], self.decode_vars(model, self.q_vars)
                )
            }
            result["witness"] = self.find_witness(model)
        elif status == z3.unknown:
            result["reason_unknown"] = solver.reason_unknown()
        return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--K", type=int, required=True)
    parser.add_argument("--allow-inf", action="store_true")
    parser.add_argument("--timeout-ms", type=int, default=120_000)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    result = PG32Search(args.K, args.allow_inf, args.timeout_ms).run()
    text = json.dumps(result, indent=2, sort_keys=True)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
