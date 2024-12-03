"""2024 - Day 3 Part 1: Mull It Over"""

from src.year2024.day03a import solve


def test_solve():
    task = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    assert solve(task) == 161
