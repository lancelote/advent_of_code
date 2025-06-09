"""2015 - Day 9 Part 1: All in a Single Night."""

from textwrap import dedent

from src.year2015.day09a import solve


def test_original_example():
    task = dedent(
        """
        London to Dublin = 464
        London to Belfast = 518
        Dublin to Belfast = 141
        """
    ).strip()

    assert solve(task) == 605


def test_two_ways():
    task = dedent(
        """
        A to B = 1
        B to C = 5
        A to C = 1
        """
    ).strip()

    assert solve(task) == 2
