"""2021 - Day 8 Part 2: ."""
from __future__ import annotations

from collections import defaultdict

from src.year2021.day8a import process_data

fz = frozenset


class Screen:
    def __init__(self, a, b, c, d, e, f, g) -> None:
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

    def parse_num(self):
        return {
            0: {self.a, self.b, self.c, self.e, self.f, self.g},
            1: {self.c, self.f},
            2: {self.a, self.c, self.d, self.e, self.g},
            3: {self.a, self.c, self.d, self.f, self.g},
            4: {self.b, self.c, self.d, self.f},
            5: {self.a, self.b, self.d, self.f, self.g},
            6: {self.a, self.b, self.d, self.e, self.f, self.g},
            7: {self.a, self.c, self.f},
            8: {self.a, self.b, self.c, self.d, self.e, self.f, self.g},
            9: {self.a, self.b, self.c, self.d, self.f, self.g},
        }

    def parse_output(self, output: list[str]) -> int:
        digits = []

        for num in output:
            digits.append(self.mapping[frozenset(num)])

        return int("".join(digits))

    @classmethod
    def from_signal(cls, nums: list[str]) -> Screen:
        lengths = defaultdict(list)
        for num in nums:
            lengths[len(num)].append(set(num))

        one = lengths[2][0]
        four = lengths[4][0]
        seven = lengths[3][0]
        eight = lengths[7][0]
        zero_six_nine = lengths[6]
        two_three_five = lengths[5]

        # magic
        a = seven - four
        e = (set.union(*zero_six_nine) - set.intersection(*zero_six_nine)) - four
        d = (set.union(*zero_six_nine) - set.intersection(*zero_six_nine)) - e - one
        c = (set.union(*zero_six_nine) - set.intersection(*zero_six_nine)) - e - d
        b = four - one - d
        f = four - b - c - d
        g = eight - a - b - c - d - e - f

        a = a.pop()
        b = b.pop()
        c = c.pop()
        d = d.pop()
        e = e.pop()
        f = f.pop()
        g = g.pop()

        return cls(a, b, c, d, e, f, g)


def solve(task: str) -> int:
    entries = process_data(task)
    return sum(
        Screen.from_signal(entry.signal).parse_output(entry.output)
        for entry in entries
    )
