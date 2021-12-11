"""2021 - Day 11 Part 2: Dumbo Octopus."""
from src.year2021.day11a import Data
from src.year2021.day11a import make_step


def solve(task: str) -> int:
    data = Data.from_task(task)

    step = 0
    while True:
        step += 1
        make_step(data)

        if data.all_zeros:
            return step
