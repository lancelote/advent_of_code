"""2023 - Day 11 Part 1: Cosmic Expansion"""

from itertools import combinations
from typing import Self
from typing import TypeAlias

C: TypeAlias = tuple[int, int]


class StarMap:
    def __init__(self, data: list[list[str]], age: int = 2) -> None:
        self.data = data
        self.age = age

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
                extra_r += self.age - 1

        for c in range(min(g1[1], g2[1]), max(g1[1], g2[1])):
            if c in self.empty_cols:
                extra_c += self.age - 1

        return abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]) + extra_c + extra_r

    @classmethod
    def from_text(cls, text: str, age: int = 2) -> Self:
        return cls([list(line) for line in text.splitlines()], age)

    @property
    def total_path(self) -> int:
        total = 0

        for g1, g2 in combinations(self.galaxies, 2):
            path = self.get_path(g1, g2)
            total += path

        return total


def solve(task: str) -> int:
    sm = StarMap.from_text(task)
    return sm.total_path
