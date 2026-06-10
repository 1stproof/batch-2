#!/usr/bin/env python3
"""Z3 search for failures of the two-rank local quotient criterion.

The model uses min-plus conventions.  A distinguished alphabet value encodes
infinity; sums involving infinity are represented by a large sentinel.

Constraints:
  * p and q have at least one finite coordinate;
  * p and q satisfy 3-term tropical Pluecker relations;
  * the ordinary finite supports are in quotient order, encoded as the
    0/infinity version of all incidence relations;
  * all nested endpoint incidence relations hold for the actual values.

The asserted bad event is a unique finite minimum in an arbitrary incidence
relation with I not contained in J.
"""

from __future__ import annotations

import argparse
import json
import time
from itertools import combinations
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

import z3


def bits(items: Iterable[int]) -> int:
    out = 0
    for i in items:
        out |= 1 << i
    return out


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


def set_tuple(mask: int) -> Tuple[int, ...]:
    return tuple(bit_iter(mask))


class TwoRankSearch:
    def __init__(
        self,
        n: int,
        a: int,
        b: int,
        K: int,
        allow_inf: bool,
        timeout_ms: int,
        fixed_bad_I: int | None = None,
        fixed_bad_J: int | None = None,
    ) -> None:
        self.n = n
        self.a = a
        self.b = b
        self.K = K
        self.allow_inf = allow_inf
        self.inf = K + 1
        self.big = 10_000
        self.timeout_ms = timeout_ms
        self.fixed_bad_I = fixed_bad_I
        self.fixed_bad_J = fixed_bad_J
        self.by_size = {k: subsets_of_size(n, k) for k in range(n + 1)}
        self.p_subsets = self.by_size[a]
        self.q_subsets = self.by_size[b]
        self.p_index = {s: i for i, s in enumerate(self.p_subsets)}
        self.q_index = {s: i for i, s in enumerate(self.q_subsets)}
        self.p_vars = [z3.Int(f"p_{s}") for s in self.p_subsets]
        self.q_vars = [z3.Int(f"q_{s}") for s in self.q_subsets]
        self.counts: Dict[str, int] = {
            "domain": 0,
            "normalization": 0,
            "p_pluecker": 0,
            "q_pluecker": 0,
            "support_quotient": 0,
            "nested_value_incidence": 0,
            "bad_non_nested_disjuncts": 0,
        }

    def p(self, subset: int):
        return self.p_vars[self.p_index[subset]]

    def q(self, subset: int):
        return self.q_vars[self.q_index[subset]]

    def add_term(self, x, y):
        return z3.If(z3.Or(x == self.inf, y == self.inf), self.big, x + y)

    def min_twice(self, terms: Sequence[z3.ArithRef]):
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

    def ordinary_min_twice_or_none(self, finite_flags: Sequence[z3.BoolRef]):
        count = z3.Sum([z3.If(flag, 1, 0) for flag in finite_flags])
        return z3.Or(count == 0, count >= 2)

    def unique_finite_min(self, terms: Sequence[z3.ArithRef]):
        return z3.Or(
            *[
                z3.And(term < self.big, *[term < other for j, other in enumerate(terms) if j != i])
                for i, term in enumerate(terms)
            ]
        )

    def add_pluecker(self, solver: z3.Solver, rank: int, getter, counter_key: str) -> None:
        if rank < 2:
            return
        for S in self.by_size[rank - 2]:
            outside = [e for e in range(self.n) if not (S >> e) & 1]
            for i, j, k, l in combinations(outside, 4):
                terms = [
                    self.add_term(getter(S | (1 << i) | (1 << j)), getter(S | (1 << k) | (1 << l))),
                    self.add_term(getter(S | (1 << i) | (1 << k)), getter(S | (1 << j) | (1 << l))),
                    self.add_term(getter(S | (1 << i) | (1 << l)), getter(S | (1 << j) | (1 << k))),
                ]
                solver.add(self.min_twice(terms))
                self.counts[counter_key] += 1

    def incidence_terms(self, I: int, J: int) -> List[z3.ArithRef]:
        return [
            self.add_term(self.p(I | (1 << i)), self.q(J & ~(1 << i)))
            for i in bit_iter(J & ~I)
        ]

    def incidence_support_flags(self, I: int, J: int) -> List[z3.BoolRef]:
        return [
            z3.And(self.p(I | (1 << i)) < self.inf, self.q(J & ~(1 << i)) < self.inf)
            for i in bit_iter(J & ~I)
        ]

    def build_solver(self) -> Tuple[z3.Solver, List[Tuple[int, int, List[z3.ArithRef]]]]:
        solver = z3.Solver()
        solver.set("timeout", self.timeout_ms)
        domain = list(range(self.K + 1))
        if self.allow_inf:
            domain.append(self.inf)

        for v in self.p_vars + self.q_vars:
            solver.add(z3.Or(*[v == d for d in domain]))
            self.counts["domain"] += 1
        solver.add(z3.Or(*[v < self.inf for v in self.p_vars]))
        solver.add(z3.Or(*[v < self.inf for v in self.q_vars]))
        solver.add(z3.Or(*[v == 0 for v in self.p_vars]))
        solver.add(z3.Or(*[v == 0 for v in self.q_vars]))
        self.counts["normalization"] += 4

        self.add_pluecker(solver, self.a, self.p, "p_pluecker")
        self.add_pluecker(solver, self.b, self.q, "q_pluecker")

        # Ordinary support quotient: all arbitrary incidence relations for
        # the 0/infinity supports have no unique finite term.
        for I in self.by_size[self.a - 1]:
            for J in self.by_size[self.b + 1]:
                flags = self.incidence_support_flags(I, J)
                solver.add(self.ordinary_min_twice_or_none(flags))
                self.counts["support_quotient"] += 1

        # Actual-value nested endpoint incidence.
        for S in self.by_size[self.a - 1]:
            for T in self.by_size[self.b + 1]:
                if S & ~T:
                    continue
                solver.add(self.min_twice(self.incidence_terms(S, T)))
                self.counts["nested_value_incidence"] += 1

        bad_relations = []
        for I in self.by_size[self.a - 1]:
            for J in self.by_size[self.b + 1]:
                if not (I & ~J):
                    continue
                if self.fixed_bad_I is not None and I != self.fixed_bad_I:
                    continue
                if self.fixed_bad_J is not None and J != self.fixed_bad_J:
                    continue
                terms = self.incidence_terms(I, J)
                bad_relations.append((I, J, terms))
        self.counts["bad_non_nested_disjuncts"] = sum(len(t) for _, _, t in bad_relations)
        if not bad_relations:
            raise ValueError("fixed bad relation is not a non-nested incidence relation")
        solver.add(z3.Or(*[self.unique_finite_min(terms) for _, _, terms in bad_relations]))
        return solver, bad_relations

    def solve(self) -> Dict[str, object]:
        start = time.time()
        solver, bad_relations = self.build_solver()
        status = solver.check()
        out: Dict[str, object] = {
            "n": self.n,
            "ranks": [self.a, self.b],
            "K": self.K,
            "allow_inf": self.allow_inf,
            "alphabet": list(range(self.K + 1)) + (["INF"] if self.allow_inf else []),
            "inf_code": self.inf if self.allow_inf else None,
            "status": str(status),
            "elapsed_seconds": time.time() - start,
            "timeout_ms": self.timeout_ms,
            "fixed_bad_relation": (
                None
                if self.fixed_bad_I is None
                else {"I": set_tuple(self.fixed_bad_I), "J": set_tuple(self.fixed_bad_J or 0)}
            ),
            "constraint_counts": self.counts,
        }
        if status == z3.unknown:
            out["reason_unknown"] = solver.reason_unknown()
            return out
        if status != z3.sat:
            return out

        model = solver.model()

        def eval_value(v):
            raw = model.eval(v, model_completion=True).as_long()
            return "INF" if raw == self.inf else raw

        out["p"] = {
            "rank": self.a,
            "coordinates": [
                {"set": set_tuple(s), "value": eval_value(self.p(s))}
                for s in self.p_subsets
            ],
        }
        out["q"] = {
            "rank": self.b,
            "coordinates": [
                {"set": set_tuple(s), "value": eval_value(self.q(s))}
                for s in self.q_subsets
            ],
        }
        for I, J, terms in bad_relations:
            vals = [model.eval(t, model_completion=True).as_long() for t in terms]
            finite_vals = [v for v in vals if v < self.big]
            if finite_vals and vals.count(min(finite_vals)) == 1:
                out["failed_relation"] = {
                    "I": set_tuple(I),
                    "J": set_tuple(J),
                    "indices": list(set_tuple(J & ~I)),
                    "term_values": ["INF" if v >= self.big else v for v in vals],
                }
                break
        return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--a", type=int, required=True)
    parser.add_argument("--b", type=int, required=True)
    parser.add_argument("--K", type=int, required=True)
    parser.add_argument("--allow-inf", action="store_true")
    parser.add_argument("--timeout-ms", type=int, default=120_000)
    parser.add_argument(
        "--fixed-bad",
        nargs=2,
        metavar=("I", "J"),
        help="Fix the bad relation to comma-separated element lists, e.g. 0 1,2,3,4,5",
    )
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    result = TwoRankSearch(
        n=args.n,
        a=args.a,
        b=args.b,
        K=args.K,
        allow_inf=args.allow_inf,
        timeout_ms=args.timeout_ms,
        fixed_bad_I=bits(int(x) for x in args.fixed_bad[0].split(",") if x != "")
        if args.fixed_bad
        else None,
        fixed_bad_J=bits(int(x) for x in args.fixed_bad[1].split(",") if x != "")
        if args.fixed_bad
        else None,
    ).solve()
    text = json.dumps(result, indent=2, sort_keys=True)
    if args.out:
        args.out.write_text(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
