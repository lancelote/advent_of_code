"""2024 - Day 3 Part 2: Mull It Over"""

from src.year2024.day03b import solve


def test_solve():
    task = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    assert solve(task) == 48
