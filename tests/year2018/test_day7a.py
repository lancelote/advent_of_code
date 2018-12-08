"""2018 - Day 7 Part 1: The Sum of Its Parts tests."""

from textwrap import dedent

from src.year2018.day7a import solve


def test_solve():
    test_task = dedent("""
        Step C must be finished before step A can begin.
        Step C must be finished before step F can begin.
        Step A must be finished before step B can begin.
        Step A must be finished before step D can begin.
        Step B must be finished before step E can begin.
        Step D must be finished before step E can begin.
        Step F must be finished before step E can begin.
    """)
    assert solve(test_task, steps='ABCDEF') == 'CABDFE'
