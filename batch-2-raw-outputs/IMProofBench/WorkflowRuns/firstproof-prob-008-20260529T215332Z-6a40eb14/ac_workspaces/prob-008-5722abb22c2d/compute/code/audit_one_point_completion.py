#!/usr/bin/env python3
"""Audit the truncation/elongation one-point completion formula.

For small examples already used in this workspace, enumerate or sample flat
valuations nu <= mu_M, construct all layers

    h_j(B)=min{nu(C): B subset C, |C|=k}      for j <= k,
    h_j(B)=min{nu(C): C subset B, |C|=k}      for j >= k,

with h_j(B)=INF for dependent B above rank k.  Each layer is normalized by
subtracting its finite minimum.  The audit checks:

  * h_j is flat-constant, so it can be represented by flat coordinates;
  * h_j is a quotient of mu_M;
  * h_j <= h_{j+1} for every adjacent pair;
  * h_r is projectively the trivial top valuation mu_M.
"""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

from flat_duality_tests import (
    INF,
    FlatValuation,
    Matroid,
    bits,
    boolean_matroid,
    check_incidence,
    direct_sum_u23_u23,
    enumerate_flat_valuations,
    fano_matroid,
    is_quotient_of_M,
    pg_2_3_matroid,
    uniform_rank_2,
)


def bit_iter(mask: int) -> Iterable[int]:
    i = 0
    while mask:
        if mask & 1:
            yield i
        mask >>= 1
        i += 1


def normalize(values: Dict[int, int]) -> Dict[int, int]:
    finite = [v for v in values.values() if v < INF]
    if not finite:
        return values
    m = min(finite)
    return {s: (INF if v >= INF else v - m) for s, v in values.items()}


def layer_subset_values(nu: FlatValuation, j: int) -> Dict[int, int]:
    M, k = nu.matroid, nu.k
    out: Dict[int, int] = {}
    for B in M.by_size[j]:
        if j >= k and not M.independent[B]:
            out[B] = INF
            continue
        candidates: List[int] = []
        if j <= k:
            outside = [e for e in range(M.n) if not (B >> e) & 1]
            for extra in combinations(outside, k - j):
                C = B | bits(extra)
                candidates.append(nu.val_subset(C))
        else:
            for C_tuple in combinations(list(bit_iter(B)), k):
                C = bits(C_tuple)
                candidates.append(nu.val_subset(C))
        out[B] = min(candidates) if candidates else INF
    return normalize(out)


def flat_valuation_from_subset_values(
    M: Matroid, j: int, values: Dict[int, int]
) -> Tuple[FlatValuation | None, str]:
    flat_values: Dict[int, int] = {}
    for flat in M.flats_by_rank[j]:
        vals = []
        for B in M.by_size[j]:
            if M.independent[B] and M.closure(B) == flat:
                vals.append(values[B])
        if not vals:
            flat_values[flat] = INF
            continue
        if len(set(vals)) != 1:
            return None, f"not flat-constant at rank {j}, flat {flat:b}, values {sorted(set(vals))}"
        flat_values[flat] = vals[0]
    return FlatValuation(M, j, tuple(flat_values[f] for f in M.flats_by_rank[j])), ""


def audit_nu(nu: FlatValuation) -> Dict[str, object]:
    M = nu.matroid
    layers: List[FlatValuation] = []
    layer_errors = []
    for j in range(M.r + 1):
        values = layer_subset_values(nu, j)
        hv, msg = flat_valuation_from_subset_values(M, j, values)
        if hv is None:
            layer_errors.append(msg)
            continue
        layers.append(hv)
        ok, qmsg = is_quotient_of_M(hv)
        if not ok:
            layer_errors.append(f"rank {j} not quotient of M: {qmsg}")

    adjacent_errors = []
    if len(layers) == M.r + 1:
        for j in range(M.r):
            ok, msg = check_incidence(layers[j], layers[j + 1])
            if not ok:
                adjacent_errors.append(f"rank {j}->{j+1}: {msg}")

    top_values = layers[-1].vals if len(layers) == M.r + 1 else ()
    top_projectively_mu = bool(top_values) and len({v for v in top_values if v < INF}) == 1
    return {
        "rank": nu.k,
        "nu_values": ["INF" if v >= INF else v for v in nu.vals],
        "layer_errors": layer_errors[:3],
        "adjacent_errors": adjacent_errors[:3],
        "top_projectively_mu": top_projectively_mu,
        "top_values": ["INF" if v >= INF else v for v in top_values],
        "ok": not layer_errors and not adjacent_errors and top_projectively_mu,
    }


def run() -> Dict[str, object]:
    cases: List[Matroid] = [
        boolean_matroid(4),
        uniform_rank_2(4, perm=[1, 0, 3, 2]),
        fano_matroid(),
        direct_sum_u23_u23(),
        pg_2_3_matroid(),
    ]
    alphabet = [0, 1, 2, INF]
    results = []
    for M in cases:
        case = {
            "matroid": M.name,
            "rank": M.r,
            "n": M.n,
            "flat_counts": {j: len(M.flats_by_rank[j]) for j in range(M.r + 1)},
            "checks": [],
            "failures": [],
        }
        for k in range(1, M.r):
            exhaustive_max_flats = 7
            if len(M.flats_by_rank[k]) > exhaustive_max_flats:
                continue
            vals = [
                nu
                for nu in enumerate_flat_valuations(M, k, alphabet)
                if any(v < INF for v in nu.vals)
            ]
            for nu in vals[:200]:
                audit = audit_nu(nu)
                case["checks"].append(audit)
                if not audit["ok"]:
                    case["failures"].append(audit)
                    break
            if case["failures"]:
                break
        results.append(case)
    return {
        "description": "Finite audit of the one-point completion formula on small relative Dressians.",
        "alphabet": [0, 1, 2, "INF"],
        "results": results,
    }


def main() -> None:
    result = run()
    out = Path("data/one_point_completion_audit_round3.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
