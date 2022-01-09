"""2021 - Day 19 Part 1: Beacon Scanner."""
from __future__ import annotations

from dataclasses import dataclass
from typing import NamedTuple

DETECTION_RANGE = 1_000
BEACONS_TO_MATCH = 12


class Position(NamedTuple):
    x: int
    y: int
    z: int

    @classmethod
    def from_line(cls, line: str) -> Position:
        a, b, c = line.split(",")
        return Position(int(a), int(b), int(c))


@dataclass
class Scanner:
    pk: int
    beacons: list[Position]


def solve(task: str) -> int:
    ...
