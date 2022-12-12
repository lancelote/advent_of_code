"""2020 - Day 5 Part 1: Binary Boarding."""
from __future__ import annotations

from dataclasses import dataclass
from functools import cached_property
from typing import Any


LEFT = "FL"
RIGHT = "BR"


def binary_search(start: int, stop: int, steps: str, step_id: int = 0) -> int:
    if not step_id < len(steps):
        return stop
    else:
        step = steps[step_id]
        start = start if step in LEFT else (stop + start) // 2 + 1
        stop = stop if step in RIGHT else (stop + start) // 2
        return binary_search(start, stop, steps, step_id + 1)


@dataclass
class Seat:
    code: str

    @cached_property
    def row(self) -> int:
        return binary_search(0, 127, self.code[0:7])

    @cached_property
    def column(self) -> int:
        return binary_search(0, 7, self.code[7:10])

    @cached_property
    def pk(self) -> int:
        return self.row * 8 + self.column

    def __lt__(self, other: Any) -> bool:
        assert isinstance(other, Seat)
        return self.pk < other.pk


def process_data(task: str) -> list[Seat]:
    return [Seat(code) for code in task.strip().split("\n")]


def solve(task: str) -> int:
    seats = process_data(task)
    return max(seats).pk
