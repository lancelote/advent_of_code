"""2018 - Day 3 Part 2: No Matter How You Slice It tests."""

from src.year2018.day03b import Claim, apply_claim


def test_apply_claim():
    not_overlap = set()
    fabric = [[0 for _ in range(8)] for _ in range(8)]
    expected = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 2, 2, 2, 0],
        [0, 0, 0, 2, 2, 2, 2, 0],
        [0, 1, 1, 2, 2, 2, 2, 0],
        [0, 1, 1, 2, 2, 2, 2, 0],
        [0, 1, 1, 1, 1, 3, 3, 0],
        [0, 1, 1, 1, 1, 3, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]
    claims = [
        Claim(1, 1, 3, 4, 4),
        Claim(2, 3, 1, 4, 4),
        Claim(3, 5, 5, 2, 2),
    ]

    for claim in claims:
        apply_claim(fabric, claim, not_overlap)

    assert fabric == expected
    assert not_overlap == {3}


def test_apply_claim_multiple_overlaps_on_one_inch():
    not_overlap = set()
    fabric = [[0]]
    claims = [
        Claim(1, 0, 0, 1, 1),
        Claim(2, 0, 0, 1, 1),
        Claim(3, 0, 0, 1, 1),
    ]

    for claim in claims:
        apply_claim(fabric, claim, not_overlap)

    assert fabric == [[3]]
    assert not_overlap == set()
