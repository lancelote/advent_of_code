"""2015 - Day 19 Part 1: Medicine for Rudolph."""

import pytest

from src.year2015.day19a import solve
from src.year2015.day19a import tokenize


def test_tokenize():
    assert tokenize("CRnSiRnCa") == ["C", "Rn", "Si", "Rn", "Ca"]


@pytest.mark.parametrize(
    "molecule,expected",
    (
        ("HOH", 4),
        ("HOHOHO", 7),
    ),
)
def test_solve(molecule, expected):
    assert (
        solve(f"""H => HO
H => OH
O => HH

{molecule}""")
        == expected
    )
