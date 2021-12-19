"""2021 - Day 17 Part 1: Trick Shot."""
from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass
class Target:
    x_min: int
    x_max: int
    y_min: int
    y_max: int

    @classmethod
    def from_line(cls, line: str) -> Target:
        return cls(*[int(x) for x in re.findall(r"-?\d+", line)])


def solve(task: str) -> int:
    ...
