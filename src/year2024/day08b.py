"""2024 - Day 8 Part 2: Resonant Collinearity"""

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

            ar1 = r1 - dr
            ac1 = c1 - dc

            ar2 = r1 + dr
            ac2 = c1 + dc

            ar3 = r2 - dr
            ac3 = c2 - dc

            ar4 = r2 + dr
            ac4 = c2 + dc

            while 0 <= ar1 < rows and 0 <= ac1 < cols:
                ants.add((ar1, ac1))
                ar1 -= dr
                ac1 -= dc

            while 0 <= ar2 < rows and 0 <= ac2 < cols:
                ants.add((ar2, ac2))
                ar2 += dr
                ac2 += dc

            while 0 <= ar3 < rows and 0 <= ac3 < cols:
                ants.add((ar3, ac3))
                ar3 -= dr
                ac3 -= dc

            while 0 <= ar4 < rows and 0 <= ac4 < cols:
                ants.add((ar4, ac4))
                ar4 += dr
                ac4 += dc

    return len(ants)
