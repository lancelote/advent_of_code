"""Puzzle Solver Runner."""

import importlib
import sys
from collections.abc import Sequence
from typing import Protocol
from typing import cast

from aocd import get_data

from utils.cli import convert_argv


class SolverModule(Protocol):
    def solve(self, task: str) -> int: ...


def solve(args: Sequence[str]) -> str:
    year, day, part = convert_argv(args)
    task = get_data(day=day, year=year)
    module = importlib.import_module(f"src.year{year}.day{day:02}{part}")
    solver = cast("SolverModule", cast("object", module))
    solution = str(solver.solve(task))
    return solution


def main(*args: str) -> None:
    if not args:
        args = tuple(sys.argv[1:])

    solution = solve(args)
    print(f"answer: {solution}")


if __name__ == "__main__":
    main()
