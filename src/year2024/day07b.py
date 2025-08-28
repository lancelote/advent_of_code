"""2024 - Day 7 Part 2: Bridge Repair"""

from dataclasses import dataclass

from src.year2024.day07a import Equation as BaseEquation


def join(x1: int, x2: int) -> int:
    return int(str(x1) + str(x2))


@dataclass
class Equation(BaseEquation):
    @property
    def is_good(self) -> bool:
        def dfs(i: int, so_far: int) -> bool:
            if so_far == self.test_value and i == len(self.numbers):
                return True
            elif so_far > self.test_value:
                return False
            elif i < len(self.numbers):
                x = self.numbers[i]
                return (
                    dfs(i + 1, so_far + x) or dfs(i + 1, so_far * x) or dfs(i + 1, join(so_far, x))
                )
            else:
                return False

        return dfs(1, self.numbers[0])


def solve(task: str) -> int:
    data = task.split("\n")
    equations = [Equation.from_line(line) for line in data]
    return sum(x.test_value for x in equations if x.is_good)
