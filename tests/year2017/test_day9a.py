"""2017 - Day 9 Part 1: Stream Processing."""

import pytest

from src.year2017.day9a import solve


@pytest.mark.parametrize(
    ('stream', 'total_score'),
    [
        ('{}', 1),
        ('{{{}}}', 6),
        ('{{},{}}', 5),
        ('{{{},{},{{}}}}', 16),
        ('{<a>,<a>,<a>,<a>}', 1),
        ('{{<ab>},{<ab>},{<ab>},{<ab>}}', 9),
        ('{{<!!>},{<!!>},{<!!>},{<!!>}}', 9),
        ('{{<a!>},{<a!>},{<a!>},{<ab>}}', 3),
    ]
)
def test_solve(stream, total_score):
    assert solve(stream) == total_score
