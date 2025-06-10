"""2015 - Day 9 Part 2: All in a Single Night."""

from textwrap import dedent

from src.year2015.day09b import solve


def test_original_example():
    task = dedent(
        """
        London to Dublin = 464
        London to Belfast = 518
        Dublin to Belfast = 141
        """
    ).strip()

    assert solve(task) == 982


def test_two_ways():
    task = dedent(
        """
        A to B = 1
        B to C = 5
        A to C = 1
        """
    ).strip()

    assert solve(task) == 6
