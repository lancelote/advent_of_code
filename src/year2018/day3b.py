"""2018 - Day 3 Part 2: No Matter How You Slice It.

Amidst the chaos, you notice that exactly one claim doesn't overlap by even a
single square inch of fabric with any other claim. If you can somehow draw
attention to it, maybe the Elves will be able to make Santa's suit after all!

For example, in the claims above, only claim 3 is intact after all claims are
made.

What is the ID of the only claim that doesn't overlap?
"""
from typing import List
from typing import Set

from src.year2018.day3a import Claim
from src.year2018.day3a import process_data


def apply_claim(fabric: List[List[int]], claim: Claim, not_overlap: Set[int]):
    """Claim inches of fabric and update non-overlapping set of claim ids."""
    not_overlap.add(claim.pk)  # Consider claim as non-overlapping by default

    for i in range(claim.from_top, claim.from_top + claim.height):
        for j in range(claim.from_left, claim.from_left + claim.width):

            if fabric[i][j] != 0:  # Overlap detected
                if fabric[i][j] in not_overlap:
                    not_overlap.remove(fabric[i][j])
                if claim.pk in not_overlap:
                    not_overlap.remove(claim.pk)

            fabric[i][j] = claim.pk


def solve(task: str, side=1000) -> int:
    """Find non-overlapping claim."""
    not_overlap: Set[int] = set()
    fabric = [[0 for _ in range(side)] for _ in range(side)]
    for claim in process_data(task):
        apply_claim(fabric, claim, not_overlap)
    return list(not_overlap)[0]
