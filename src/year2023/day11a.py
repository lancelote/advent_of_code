"""2023 - Day 11 Part 1: Cosmic Expansion"""
from itertools import combinations
from typing import Self
from typing import TypeAlias

C: TypeAlias = tuple[int, int]


class StarMap:
    def __init__(self, data: list[list[str]]) -> None:
        self.data = data

        rows = len(self.data)
        cols = len(self.data[0])

        self.empty_rows = {r for r in range(rows)}
        self.empty_cols = {c for c in range(cols)}

        self.galaxies: set[C] = set()

        for r in range(rows):
            for c in range(cols):
                if self.data[r][c] == "#":
                    self.empty_rows.discard(r)
                    self.empty_cols.discard(c)
                    self.galaxies.add((r, c))

    def get_path(self, g1: C, g2: C) -> int:
        extra_r = 0
        extra_c = 0

        for r in range(min(g1[0], g2[0]), max(g1[0], g2[0])):
            if r in self.empty_rows:
                extra_r += 1

        for c in range(min(g1[1], g2[1]), max(g1[1], g2[1])):
            if c in self.empty_cols:
                extra_c += 1

        return abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]) + extra_c + extra_r

    @classmethod
    def from_text(cls, text: str) -> Self:
        return cls([list(line) for line in text.splitlines()])


def solve(task: str) -> int:
    total = 0
    sm = StarMap.from_text(task)

    for g1, g2 in combinations(sm.galaxies, 2):
        path = sm.get_path(g1, g2)
        total += path

    return total
