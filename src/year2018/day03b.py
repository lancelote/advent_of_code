"""2018 - Day 3 Part 2: No Matter How You Slice It."""
from src.year2018.day03a import Claim
from src.year2018.day03a import process_data


def apply_claim(
    fabric: list[list[int]], claim: Claim, not_overlap: set[int]
) -> None:
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


def solve(task: str, side: int = 1000) -> int:
    """Find non-overlapping claim."""
    not_overlap: set[int] = set()
    fabric = [[0 for _ in range(side)] for _ in range(side)]
    for claim in process_data(task):
        apply_claim(fabric, claim, not_overlap)
    return list(not_overlap)[0]
