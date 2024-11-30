"""2018 - Day 3 Part 1: No Matter How You Slice It."""

import re
from collections.abc import Generator
from typing import NamedTuple

PATTERN = r"^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$"


class Claim(NamedTuple):
    """Claim tuple representation."""

    pk: int
    from_left: int
    from_top: int
    width: int
    height: int


def parse_claim(raw_claim: str) -> Claim:
    """Convert raw claim string to tuple."""
    match = re.match(PATTERN, raw_claim)
    if match is not None:
        groups = match.groups()
    else:
        raise ValueError('Unknown claim format: "%s"' % raw_claim)
    return Claim(*map(int, groups))


def process_data(data: str) -> Generator[Claim]:
    """Yield parsed claims from raw data."""
    for raw_claim in data.strip().split("\n"):
        yield parse_claim(raw_claim)


def apply_claim(fabric: list[list[int]], claim: Claim) -> list[list[int]]:
    """Add +1 on each inch of the given claim."""
    for i in range(claim.from_top, claim.from_top + claim.height):
        for j in range(claim.from_left, claim.from_left + claim.width):
            fabric[i][j] += 1
    return fabric


def solve(task: str, side: int = 1000) -> int:
    """Get the number of inches with 2 or more claims."""
    total_claimed = 0
    fabric = [[0 for _ in range(side)] for _ in range(side)]
    for claim in process_data(task):
        apply_claim(fabric, claim)
    for i in range(side):
        for j in range(side):
            total_claimed += fabric[i][j] > 1
    return total_claimed
