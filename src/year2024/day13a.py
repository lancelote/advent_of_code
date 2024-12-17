"""2024 - Day 13 Part 1: Claw Contraption"""

import re
from dataclasses import dataclass
from typing import Self

type Point = tuple[int, int]


@dataclass
class Machine:
    a: Point
    b: Point
    prize: Point

    @classmethod
    def from_text(cls, text: str) -> Self:
        first, second, third = text.split("\n")

        ac, ar = re.findall(r"\d+", first)
        a = int(ar), int(ac)

        bc, br = re.findall(r"\d+", second)
        b = int(br), int(bc)

        pc, pr = re.findall(r"\d+", third)
        prize = int(pr), int(pc)

        return cls(a, b, prize)

    @property
    def min_tokens_win(self) -> int:
        x, y = self.prize
        ax, ay = self.a
        bx, by = self.b

        b = (y - x * ay / ax) / (-bx * ay / ax + by)
        a = (x - b * bx) / ax

        an = round(a)
        bn = round(b)

        if an * ax + bn * bx == x and an * ay + bn * by == y:
            return an * 3 + bn
        else:
            return 0


def solve(task: str) -> int:
    machines = [Machine.from_text(block) for block in task.split("\n\n")]
    return sum(x.min_tokens_win for x in machines)
