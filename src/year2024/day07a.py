"""2024 - Day 7 Part 1: Bridge Repair"""

from dataclasses import dataclass
from typing import Self


@dataclass
class Equation:
    test_value: int
    numbers: list[int]

    @classmethod
    def from_line(cls, line: str) -> Self:
        left, right = line.split(": ")
        test_value = int(left)
        numbers = [int(x) for x in right.split()]
        return cls(test_value, numbers)

    @property
    def is_good(self) -> bool:
        def dfs(i: int, so_far: int) -> bool:
            if so_far == self.test_value and i == len(self.numbers):
                return True
            elif so_far > self.test_value:
                return False
            elif i < len(self.numbers):
                x = self.numbers[i]
                return dfs(i + 1, so_far + x) or dfs(i + 1, so_far * x)
            else:
                return False

        return dfs(1, self.numbers[0])


def solve(task: str) -> int:
    data = task.split("\n")
    equations = [Equation.from_line(line) for line in data]
    return sum(x.test_value for x in equations if x.is_good)
