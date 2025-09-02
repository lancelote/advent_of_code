"""2023 - Day 15 Part 1: Lens Library"""

from textwrap import dedent

import pytest

from src.year2023.day15a import get_hash
from src.year2023.day15a import solve


@pytest.mark.parametrize(
    "sequence,expected",
    (
        ("HASH", 52),
        ("rn=1", 30),
        ("cm-", 253),
    ),
)
def test_calc_hash(sequence, expected):
    assert get_hash(sequence) == expected


def test_solve():
    task = dedent(
        """
        rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
        """
    ).strip()
    assert solve(task) == 1320
