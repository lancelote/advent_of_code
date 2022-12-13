"""2021 - Day 14 Part 2: Extended Polymerization."""
from collections import defaultdict
from itertools import pairwise
from typing import TypeAlias

Pair: TypeAlias = tuple[str, ...]
Pairs: TypeAlias = dict[Pair, int]
Insertions: TypeAlias = dict[Pair, str]
Counts: TypeAlias = dict[str, int]


def parse_task(task: str) -> tuple[Pairs, Insertions, Counts]:
    raw_polymer, raw_insertions = task.split("\n\n")

    counts: Counts = defaultdict(int)

    for element in raw_polymer:
        counts[element] += 1

    pairs: Pairs = defaultdict(int)

    for a, b in pairwise(raw_polymer):
        pairs[(a, b)] += 1

    insertions: Insertions = {}

    for insertion in raw_insertions.splitlines():
        base, output = insertion.split(" -> ")
        insertions[tuple(base)] = output

    return pairs, insertions, counts


def step(pairs: Pairs, insertions: Insertions, counts: Counts) -> Pairs:
    new_pairs: dict[Pair, int] = defaultdict(int)

    for (a, b), count in pairs.items():
        c = insertions[(a, b)]
        new_pairs[(a, c)] += count
        new_pairs[(c, b)] += count
        counts[c] += count

    return new_pairs


def solve(task: str) -> int:
    pairs, insertions, counts = parse_task(task)

    for _ in range(40):
        pairs = step(pairs, insertions, counts)

    return max(counts.values()) - min(counts.values())
