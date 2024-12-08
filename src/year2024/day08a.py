"""2024 - Day 8 Part 1: Resonant Collinearity"""

from collections import defaultdict
from itertools import combinations


def solve(task: str) -> int:
    data = task.split("\n")

    rows = len(data)
    cols = len(data[0])

    antennas: dict[str, list[tuple[int, int]]] = defaultdict(list)

    for r, row in enumerate(data):
        for c, item in enumerate(row):
            if item not in {".", "#"}:
                antennas[item].append((r, c))

    ants: set[tuple[int, int]] = set()

    for k, v in antennas.items():
        for a1, a2 in combinations(antennas[k], 2):
            r1, c1 = a1
            r2, c2 = a2

            dr = r1 - r2
            dc = c1 - c2

            for ar, ac in (
                (r1 - dr, c1 - dc),
                (r1 + dr, c1 + dc),
                (r2 - dr, c2 - dc),
                (r2 + dr, c2 + dc),
            ):
                if 0 <= ar < rows and 0 <= ac < cols and data[ar][ac] != k:
                    ants.add((ar, ac))

    return len(ants)
