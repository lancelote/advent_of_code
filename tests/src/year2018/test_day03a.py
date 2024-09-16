"""2018 - Day 3 Part 1: No Matter How You Slice It tests."""

from textwrap import dedent

import pytest

from src.year2018.day03a import Claim
from src.year2018.day03a import apply_claim
from src.year2018.day03a import parse_claim
from src.year2018.day03a import process_data
from src.year2018.day03a import solve


@pytest.mark.parametrize(
    ("raw_claim", "expected"),
    [
        ("#1 @ 12,548: 19x10", Claim(1, 12, 548, 19, 10)),
        ("#39 @ 325,166: 23x18", Claim(39, 325, 166, 23, 18)),
        ("#77 @ 2,920: 26x25", Claim(77, 2, 920, 26, 25)),
        ("#264 @ 127,1: 21x25", Claim(264, 127, 1, 21, 25)),
        ("#293 @ 78,198: 5x8", Claim(293, 78, 198, 5, 8)),
    ],
)
def test_parse_claim(raw_claim, expected):
    assert parse_claim(raw_claim) == expected


def test_process_data():
    test_data = dedent(
        """
        #181 @ 875,9: 14x28
        #182 @ 580,669: 24x24
        #183 @ 295,256: 17x27
    """
    )
    expected = [
        Claim(181, 875, 9, 14, 28),
        Claim(182, 580, 669, 24, 24),
        Claim(183, 295, 256, 17, 27),
    ]
    assert list(process_data(test_data)) == expected


def test_apply_claim():
    fabric = [[0 for _ in range(11)] for _ in range(9)]
    expected = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    assert apply_claim(fabric, Claim(123, 3, 2, 5, 4)) == expected


def test_solve():
    test_task = dedent(
        """
        #1 @ 1,3: 4x4
        #2 @ 3,1: 4x4
        #3 @ 5,5: 2x2
    """
    )
    assert solve(test_task, side=8) == 4
