"""2021 - Day 8 Part 2: ."""
from __future__ import annotations

from collections import defaultdict

from src.year2021.day8a import process_data

fz = frozenset
union = set.union
intersect = set.intersection


class Screen:
    def __init__(
        self, a: str, b: str, c: str, d: str, e: str, f: str, g: str
    ) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g

        self.mapping = {
            fz({self.a, self.b, self.c, self.e, self.f, self.g}): "0",
            fz({self.c, self.f}): "1",
            fz({self.a, self.c, self.d, self.e, self.g}): "2",
            fz({self.a, self.c, self.d, self.f, self.g}): "3",
            fz({self.b, self.c, self.d, self.f}): "4",
            fz({self.a, self.b, self.d, self.f, self.g}): "5",
            fz({self.a, self.b, self.d, self.e, self.f, self.g}): "6",
            fz({self.a, self.c, self.f}): "7",
            fz({self.a, self.b, self.c, self.d, self.e, self.f, self.g}): "8",
            fz({self.a, self.b, self.c, self.d, self.f, self.g}): "9",
        }

    def parse_output(self, output: list[str]) -> int:
        """Convert raw string output to the corresponding integer."""
        return int("".join(self.mapping[fz(x)] for x in output))

    @classmethod
    def from_signal(cls, nums: list[str]) -> Screen:
        """Given a signal deduce its meaning and create a screen for it."""
        lengths = defaultdict(list)
        for num in nums:
            lengths[len(num)].append(set(num))

        one = lengths[2][0]
        four = lengths[4][0]
        seven = lengths[3][0]
        eight = lengths[7][0]
        zero_six_nine = lengths[6]

        # magic
        a = seven - four
        e = (eight - intersect(*zero_six_nine)) - four  # type: ignore
        d = (eight - intersect(*zero_six_nine)) - e - one  # type: ignore
        c = (eight - intersect(*zero_six_nine)) - e - d  # type: ignore
        b = four - one - d
        f = four - b - c - d
        g = eight - a - b - c - d - e - f

        return cls(
            a.pop(),
            b.pop(),
            c.pop(),
            d.pop(),
            e.pop(),
            f.pop(),
            g.pop(),
        )


def solve(task: str) -> int:
    entries = process_data(task)
    return sum(
        Screen.from_signal(entry.signal).parse_output(entry.output)
        for entry in entries
    )
