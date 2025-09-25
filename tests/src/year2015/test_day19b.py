"""2015 - Day 19 Part 1: Medicine for Rudolph."""

import pytest

from src.year2015.day19b import solve


@pytest.mark.parametrize(
    "molecule,expected",
    (
        ("HOH", 3),
        ("HOHOHO", 6),
    ),
)
def test_solve(molecule, expected):
    assert (
        solve(f"""e => H
e => O
H => HO
H => OH
O => HH

{molecule}""")
        == expected
    )
