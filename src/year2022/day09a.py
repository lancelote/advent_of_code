"""2022 - Day 9 Part 1: Rope Bridge."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TypeAlias

Position: TypeAlias = tuple[int, int]

SHIFT = {
    "L": (0, -1),
    "U": (+1, 0),
    "R": (0, +1),
    "D": (-1, 0),
}


@dataclass
class Step:
    direction: str
    length: int

    @classmethod
    def from_line(cls, line: str) -> Step:
        direction, length_str = line.split()
        return Step(direction, int(length_str))


def process_data(data: str) -> list[Step]:
    return [Step.from_line(line) for line in data.splitlines()]


def update_tail(head: Position, tail: Position) -> Position:
    hr, hc = head
    tr, tc = tail
    nr, nc = tail

    dr = abs(hr - tr)
    dc = abs(hc - tc)

    if dr > 1 or (hr != tr and dc > 1):
        nr = tr + (1 if hr > tr else -1)
    if dc > 1 or (hc != tc and dr > 1):
        nc = tc + (1 if hc > tc else -1)

    return nr, nc


def count_tail_positions(steps: list[Step]) -> int:
    tail = (0, 0)
    head = (0, 0)

    visited = {tail}

    for step in steps:
        dr, dc = SHIFT[step.direction]

        for _ in range(step.length):
            r, c = head
            head = (r + dr, c + dc)
            tail = update_tail(head, tail)
            visited.add(tail)

    return len(visited)


def solve(task: str) -> int:
    steps = process_data(task)
    return count_tail_positions(steps)
