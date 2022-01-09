"""2021 - Day 19 Part 1: Beacon Scanner."""
from __future__ import annotations

import re
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

    @classmethod
    def from_text(cls, text: str) -> Scanner:
        [header, *body] = text.splitlines()
        [pk_str] = re.findall(r"\d+", header)
        pk = int(pk_str)
        beacons = [Position.from_line(line) for line in body]
        return Scanner(pk, beacons)


def solve(task: str) -> int:
    scanners = [Scanner.from_text(text) for text in task.split("\n\n")]
