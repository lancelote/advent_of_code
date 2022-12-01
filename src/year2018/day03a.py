"""2018 - Day 3 Part 1: No Matter How You Slice It.

The Elves managed to locate the chimney-squeeze prototype fabric for Santa's
suit (thanks to someone who helpfully wrote its box IDs on the wall of the
warehouse in the middle of the night). Unfortunately, anomalies are still
affecting them - nobody can even agree on how to cut the fabric.

The whole piece of fabric they're working on is a very large square - at least
1000 inches on each side.

Each Elf has made a claim about which area of fabric would be ideal for Santa's
suit. All claims have an ID and consist of a single rectangle with edges
parallel to the edges of the fabric. Each claim's rectangle is defined as
follows:

    The number of inches between the left edge of the fabric and the left edge
        of the rectangle.
    The number of inches between the top edge of the fabric and the top edge of
        the rectangle.
    The width of the rectangle in inches.
    The height of the rectangle in inches.

A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle 3
inches from the left edge, 2 inches from the top edge, 5 inches wide, and 4
inches tall. Visually, it claims the square inches of fabric represented by #
(and ignores the square inches of fabric represented by .) in the diagram
below:

    ...........
    ...........
    ...#####...
    ...#####...
    ...#####...
    ...#####...
    ...........
    ...........
    ...........

The problem is that many of the claims overlap, causing two or more claims to
cover part of the same areas. For example, consider the following claims:

    #1 @ 1,3: 4x4
    #2 @ 3,1: 4x4
    #3 @ 5,5: 2x2

Visually, these claim the following areas:

    ........
    ...2222.
    ...2222.
    .11XX22.
    .11XX22.
    .111133.
    .111133.
    ........

The four square inches marked with X are claimed by both 1 and 2. (Claim 3,
while adjacent to the others, does not overlap either of them.)

If the Elves all proceed with their own plans, none of them will have enough
fabric. How many square inches of fabric are within two or more claims?
"""
import re
from collections.abc import Generator
from typing import List
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


def process_data(data: str) -> Generator[Claim, None, None]:
    """Yield parsed claims from raw data."""
    for raw_claim in data.strip().split("\n"):
        yield parse_claim(raw_claim)


def apply_claim(fabric: List[List[int]], claim: Claim) -> List[List[int]]:
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
