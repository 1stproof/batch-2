#!/usr/bin/env python3
"""Finite checks for the flat-coordinate opposition candidate.

The script deliberately checks the subset-indexed tropical Plucker and
incidence relations, not just interval-minimum summaries.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, product
import json
import math
import random
from typing import Callable, Dict, Iterable, List, Sequence, Tuple


INF = 10**9


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


def popcount(mask: int) -> int:
    return mask.bit_count()


def min_twice(values: Sequence[int]) -> bool:
    if not values:
        return True
    m = min(values)
    if m >= INF:
        return True
    return sum(v == m for v in values) >= 2


@dataclass
class Matroid:
    name: str
    n: int
    rank_fn: Callable[[int], int]
    opp_fn: Callable[[int], int]

    def __post_init__(self) -> None:
        self.E = (1 << self.n) - 1
        self.r = self.rank_fn(self.E)
        self.by_size: Dict[int, List[int]] = {
            k: [bits(c) for c in combinations(range(self.n), k)]
            for k in range(self.n + 1)
        }
        self.rank_cache = [self.rank_fn(s) for s in range(1 << self.n)]
        self.independent = [
            self.rank_cache[s] == popcount(s) for s in range(1 << self.n)
        ]
        self.closure_cache = [self._closure_uncached(s) for s in range(1 << self.n)]
        self.flats = [s for s in range(1 << self.n) if self.closure_cache[s] == s]
        self.flats_by_rank: Dict[int, List[int]] = {
            k: [f for f in self.flats if self.rank_cache[f] == k]
            for k in range(self.r + 1)
        }

    def rank(self, s: int) -> int:
        return self.rank_cache[s]

    def closure(self, s: int) -> int:
        return self.closure_cache[s]

    def _closure_uncached(self, s: int) -> int:
        rs = self.rank_fn(s)
        out = s
        for e in range(self.n):
            if not (s >> e) & 1 and self.rank_fn(s | (1 << e)) == rs:
                out |= 1 << e
        return out

    def opp(self, flat: int) -> int:
        out = self.opp_fn(flat)
        if out not in self.flats:
            raise ValueError((self.name, "opposition did not produce a flat", flat, out))
        return out


@dataclass(frozen=True)
class FlatValuation:
    matroid: Matroid
    k: int
    vals: Tuple[int, ...]

    def flat_values(self) -> Dict[int, int]:
        return dict(zip(self.matroid.flats_by_rank[self.k], self.vals))

    def val_subset(self, s: int) -> int:
        if popcount(s) != self.k or not self.matroid.independent[s]:
            return INF
        return self.flat_values()[self.matroid.closure(s)]

    def support_signature(self) -> Tuple[int, ...]:
        return tuple(i for i, v in enumerate(self.vals) if v < INF)

    def normalized_key(self) -> Tuple[int, ...]:
        finite = [v for v in self.vals if v < INF]
        if not finite:
            return self.vals
        m = min(finite)
        return tuple(INF if v >= INF else v - m for v in self.vals)

    def dual(self) -> "FlatValuation":
        M = self.matroid
        dual_k = M.r - self.k
        source = self.flat_values()
        vals = tuple(source[M.opp(f)] for f in M.flats_by_rank[dual_k])
        return FlatValuation(M, dual_k, vals)


def check_plucker(v: FlatValuation) -> Tuple[bool, str]:
    M, k = v.matroid, v.k
    if k < 0 or k > M.n:
        return False, "bad rank"
    if k in (0, M.n):
        return True, ""
    for S in M.by_size[k - 2] if k >= 2 else [0]:
        outside = [e for e in range(M.n) if not (S >> e) & 1]
        for T_tuple in combinations(outside, 4):
            a, b, c, d = T_tuple
            vals = [
                v.val_subset(S | (1 << a) | (1 << b))
                + v.val_subset(S | (1 << c) | (1 << d)),
                v.val_subset(S | (1 << a) | (1 << c))
                + v.val_subset(S | (1 << b) | (1 << d)),
                v.val_subset(S | (1 << a) | (1 << d))
                + v.val_subset(S | (1 << b) | (1 << c)),
            ]
            if not min_twice(vals):
                return False, f"Plucker S={S:b} T={bits(T_tuple):b} vals={vals}"
    return True, ""


def check_incidence(p: FlatValuation, q: FlatValuation) -> Tuple[bool, str]:
    M = p.matroid
    assert M is q.matroid
    a, b = p.k, q.k
    if a > b:
        return False, "incidence ranks reversed"
    if a == b:
        return check_plucker(p)
    if a == 0 or b == M.n:
        return True, ""
    for S in M.by_size.get(a - 1, []):
        for T in M.by_size.get(b + 1, []):
            vals = []
            for i in bit_iter(T & ~S):
                vals.append(p.val_subset(S | (1 << i)) + q.val_subset(T & ~(1 << i)))
            if not min_twice(vals):
                return False, f"Incidence a={a} b={b} S={S:b} T={T:b} vals={vals}"
    return True, ""


def trivial_mu(M: Matroid) -> FlatValuation:
    return FlatValuation(M, M.r, tuple(0 for _ in M.flats_by_rank[M.r]))


def is_quotient_of_M(v: FlatValuation) -> Tuple[bool, str]:
    ok, msg = check_plucker(v)
    if not ok:
        return ok, msg
    ok, msg = check_incidence(v, trivial_mu(v.matroid))
    if not ok:
        return ok, msg
    return True, ""


def enumerate_flat_valuations(
    M: Matroid, k: int, alphabet: Sequence[int], limit: int | None = None
) -> List[FlatValuation]:
    seen = set()
    out: List[FlatValuation] = []
    flats = M.flats_by_rank[k]
    for vals in product(alphabet, repeat=len(flats)):
        v = FlatValuation(M, k, tuple(vals))
        key = v.normalized_key()
        if key in seen:
            continue
        seen.add(key)
        v = FlatValuation(M, k, key)
        ok, _ = is_quotient_of_M(v)
        if ok:
            out.append(v)
            if limit is not None and len(out) >= limit:
                break
    return out


def random_flat_valuations(
    M: Matroid,
    k: int,
    alphabet: Sequence[int],
    count: int,
    seed: int,
    max_attempts: int = 10000,
) -> List[FlatValuation]:
    rng = random.Random(seed)
    found: Dict[Tuple[int, ...], FlatValuation] = {}
    flats = M.flats_by_rank[k]
    attempts = 0
    while len(found) < count and attempts < max_attempts:
        attempts += 1
        vals = tuple(rng.choice(alphabet) for _ in flats)
        v = FlatValuation(M, k, vals)
        key = v.normalized_key()
        if key in found:
            continue
        v = FlatValuation(M, k, key)
        ok, _ = is_quotient_of_M(v)
        if ok:
            found[key] = v
    return list(found.values())


def mask_to_set(mask: int) -> Tuple[int, ...]:
    return tuple(bit_iter(mask))


def uniform_rank_2(n: int, perm: Sequence[int] | None = None) -> Matroid:
    if perm is None:
        perm = list(range(n))
    top = (1 << n) - 1

    def rank_fn(s: int) -> int:
        return min(popcount(s), 2)

    def opp_fn(flat: int) -> int:
        if flat == 0:
            return top
        if flat == top:
            return 0
        if popcount(flat) == 1:
            e = next(bit_iter(flat))
            return 1 << perm[e]
        raise ValueError(("not a flat", flat))

    return Matroid(f"U_2,{n}", n, rank_fn, opp_fn)


def boolean_matroid(r: int) -> Matroid:
    top = (1 << r) - 1

    def rank_fn(s: int) -> int:
        return popcount(s)

    def opp_fn(flat: int) -> int:
        return top ^ flat

    return Matroid(f"Boolean_U_{r},{r}", r, rank_fn, opp_fn)


def direct_sum_u23_u23() -> Matroid:
    n = 6
    comp1 = bits([0, 1, 2])
    comp2 = bits([3, 4, 5])

    def rank_fn(s: int) -> int:
        return min(popcount(s & comp1), 2) + min(popcount(s & comp2), 2)

    def opp_component(s: int, comp: int, offset: int) -> int:
        rel = s & comp
        if rel == 0:
            return comp
        if rel == comp:
            return 0
        if popcount(rel) == 1:
            return rel
        raise ValueError(("not component flat", s, comp))

    def opp_fn(flat: int) -> int:
        return opp_component(flat, comp1, 0) | opp_component(flat, comp2, 3)

    return Matroid("U_2,3_plus_U_2,3", n, rank_fn, opp_fn)


def fano_matroid() -> Matroid:
    # Points are nonzero vectors in F_2^3, encoded as integers 1..7 but indexed 0..6.
    vecs = list(range(1, 8))
    n = len(vecs)
    top = (1 << n) - 1

    def span_dim(s: int) -> int:
        basis: List[int] = []
        for idx in bit_iter(s):
            v = vecs[idx]
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

    def rank_fn(s: int) -> int:
        return span_dim(s)

    def dot(u: int, v: int) -> int:
        return popcount(u & v) % 2

    def opp_fn(flat: int) -> int:
        if flat == 0:
            return top
        if flat == top:
            return 0
        # Orthogonal subspace under the standard dot product.
        out = 0
        for idx, v in enumerate(vecs):
            good = True
            for j in bit_iter(flat):
                if dot(v, vecs[j]):
                    good = False
                    break
            if good:
                out |= 1 << idx
        return out

    return Matroid("Fano_PG_2_2", n, rank_fn, opp_fn)


def pg_2_3_matroid() -> Matroid:
    # Normalized nonzero vectors in F_3^3 modulo scalar.
    reps: List[Tuple[int, int, int]] = []
    seen = set()
    for v in product(range(3), repeat=3):
        if v == (0, 0, 0):
            continue
        orbit = []
        for a in (1, 2):
            orbit.append(tuple((a * x) % 3 for x in v))
        key = min(orbit)
        if key not in seen:
            seen.add(key)
            reps.append(key)
    n = len(reps)
    top = (1 << n) - 1

    def rank_vectors(indices: Iterable[int]) -> int:
        rows = [list(reps[i]) for i in indices]
        rank = 0
        col = 0
        while rank < len(rows) and col < 3:
            pivot = None
            for i in range(rank, len(rows)):
                if rows[i][col] % 3:
                    pivot = i
                    break
            if pivot is None:
                col += 1
                continue
            rows[rank], rows[pivot] = rows[pivot], rows[rank]
            inv = 1 if rows[rank][col] == 1 else 2
            rows[rank] = [(inv * x) % 3 for x in rows[rank]]
            for i in range(len(rows)):
                if i != rank and rows[i][col] % 3:
                    factor = rows[i][col]
                    rows[i] = [(rows[i][j] - factor * rows[rank][j]) % 3 for j in range(3)]
            rank += 1
            col += 1
        return rank

    def rank_fn(s: int) -> int:
        return rank_vectors(bit_iter(s))

    def dot(u: Tuple[int, int, int], v: Tuple[int, int, int]) -> int:
        return sum(a * b for a, b in zip(u, v)) % 3

    def opp_fn(flat: int) -> int:
        if flat == 0:
            return top
        if flat == top:
            return 0
        out = 0
        for idx, v in enumerate(reps):
            if all(dot(v, reps[j]) == 0 for j in bit_iter(flat)):
                out |= 1 << idx
        return out

    return Matroid("PG_2_3", n, rank_fn, opp_fn)


def run_case(
    M: Matroid,
    alphabet: Sequence[int],
    exhaustive_max_flats: int = 7,
    random_count: int = 100,
    pair_sample: int = 2000,
) -> Dict[str, object]:
    case: Dict[str, object] = {
        "name": M.name,
        "n": M.n,
        "rank": M.r,
        "flat_counts": {k: len(M.flats_by_rank[k]) for k in range(M.r + 1)},
        "ranks": {},
        "pair_tests": [],
        "counterexamples": [],
        "alphabet": ["INF" if x >= INF else x for x in alphabet],
    }
    quotients: Dict[int, List[FlatValuation]] = {}
    for k in range(M.r + 1):
        if k in (0, M.r):
            vals = [trivial_mu(M)] if k == M.r else [FlatValuation(M, 0, (0,))]
        elif len(M.flats_by_rank[k]) <= exhaustive_max_flats:
            vals = enumerate_flat_valuations(M, k, alphabet)
        else:
            vals = random_flat_valuations(M, k, alphabet, random_count, seed=1000 + k + M.n)
        quotients[k] = vals
        dual_failures = []
        for v in vals:
            dv = v.dual()
            ok, msg = is_quotient_of_M(dv)
            if not ok:
                dual_failures.append({"valuation": v.vals, "dual": dv.vals, "message": msg})
                break
        case["ranks"][k] = {
            "quotients_found": len(vals),
            "enumeration": "exhaustive" if len(M.flats_by_rank[k]) <= exhaustive_max_flats else "random",
            "dual_failures": dual_failures[:1],
        }
        if dual_failures:
            case["counterexamples"].append({"rank": k, **dual_failures[0]})
    rng = random.Random(20260530 + M.n)
    for a in range(M.r + 1):
        for b in range(a + 1, M.r + 1):
            candidates = []
            all_pairs = len(quotients[a]) * len(quotients[b])
            if all_pairs <= pair_sample:
                pair_iter = ((p, q) for p in quotients[a] for q in quotients[b])
                mode = "exhaustive"
            else:
                pair_iter = (
                    (rng.choice(quotients[a]), rng.choice(quotients[b])) for _ in range(pair_sample)
                )
                mode = f"sampled_{pair_sample}"
            tested_flags = 0
            transformed_failures = []
            for p, q in pair_iter:
                ok, _ = check_incidence(p, q)
                if not ok:
                    continue
                tested_flags += 1
                ok, msg = check_incidence(q.dual(), p.dual())
                if not ok:
                    transformed_failures.append(
                        {
                            "a": a,
                            "b": b,
                            "p": p.vals,
                            "q": q.vals,
                            "p_dual": p.dual().vals,
                            "q_dual": q.dual().vals,
                            "message": msg,
                        }
                    )
                    break
            case["pair_tests"].append(
                {
                    "ranks": [a, b],
                    "mode": mode,
                    "candidate_pairs": all_pairs,
                    "flags_tested": tested_flags,
                    "transformed_failures": transformed_failures[:1],
                }
            )
            if transformed_failures:
                case["counterexamples"].append(transformed_failures[0])
    return case


def main() -> None:
    mats = [
        boolean_matroid(4),
        uniform_rank_2(4, perm=[1, 0, 3, 2]),
        uniform_rank_2(5, perm=[1, 0, 3, 2, 4]),
        fano_matroid(),
        direct_sum_u23_u23(),
        pg_2_3_matroid(),
    ]
    alphabet = [0, 1, INF]
    results = [run_case(M, alphabet) for M in mats]
    print(json.dumps(results, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
