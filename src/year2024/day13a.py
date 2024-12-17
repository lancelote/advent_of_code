"""2024 - Day 13 Part 1: Claw Contraption"""

import re
import sys
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
        min_cost = {(0, 0): 0}

        ar, ac = self.a
        br, bc = self.b

        for ai in range(100):
            for bi in range(1, 100):
                nr = ar * ai + br * bi
                nc = ac * ai + bc * bi

                min_cost[(nr, nc)] = min(
                    min_cost.get((nr - br, nc - bc), sys.maxsize) + 1,
                    min_cost.get((nr - ar, nc - ac), sys.maxsize) + 3,
                )

        return min_cost.get(self.prize, 0)


def solve(task: str) -> int:
    machines = [Machine.from_text(block) for block in task.split("\n\n")]
    return sum(x.min_tokens_win for x in machines)
