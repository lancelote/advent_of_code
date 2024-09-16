"""2015 - Day 2 Part 1: I Was Told There Would Be No Math."""

from __future__ import annotations

from typing import NamedTuple


class Box(NamedTuple):
    length: int
    height: int
    width: int

    @classmethod
    def from_line(cls, line: str) -> Box:
        a, b, c = line.split("x")
        return Box(int(a), int(b), int(c))


def process_data(data: str) -> list[Box]:
    return [Box.from_line(line) for line in data.strip().split("\n")]


def solve(task: str) -> int:
    result = 0
    boxes = process_data(task)

    for box in boxes:
        sides = (
            box.length * box.height,
            box.length * box.width,
            box.height * box.width,
        )
        result += 2 * sum(sides) + min(sides)
    return result
