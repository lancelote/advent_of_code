"""2021 - Day 17 Part 1: Trick Shot."""
from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass
class Target:
    left_x: int
    right_x: int
    bottom_y: int
    top_y: int

    @classmethod
    def from_line(cls, line: str) -> Target:
        return cls(*[int(x) for x in re.findall(r"-?\d+", line)])


def solve(task: str) -> int:
    ...
