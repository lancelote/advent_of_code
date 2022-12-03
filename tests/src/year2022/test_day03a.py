"""2022 - Day 3 Part 1: Rucksack Reorganization."""
from textwrap import dedent

from src.year2022.day03a import solve


def test_solve():
    task = dedent(
        """
        vJrwpWtwJgWrhcsFMMfFFhFp
        jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
        PmmdzqPrVvPwwTWBwg
        wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
        ttgJtRGJQctTZtZT
        CrZsJsPPZsGzwwsLwLmpwMDw
        """
    ).strip()
    assert solve(task) == 157
