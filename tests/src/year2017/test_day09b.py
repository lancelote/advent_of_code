"""2017 - Day 9 Part 2: Stream Processing tests."""
import pytest

from src.year2017.day09b import solve


@pytest.mark.parametrize(
    ("stream", "expected"),
    [
        ("<>", 0),
        ("<random characters>", 17),
        ("<<<<>", 3),
        ("<{!>}>", 2),
        ("<!!>", 0),
        ("<!!!>>", 0),
        ('<{o"i!a,<{i<a>', 10),
    ],
)
def test_solve(stream, expected):
    assert solve(stream) == expected
