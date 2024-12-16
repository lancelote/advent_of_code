"""2024 - Day 12 Part 2: Garden Groups"""

from textwrap import dedent

from src.year2024.day12b import solve


def test_solve_1():
    task = dedent(
        """
        AAAA
        BBCD
        BBCC
        EEEC
        """
    ).strip()
    assert solve(task) == 80


def test_solve_2():
    task = dedent(
        """
        OOOOO
        OXOXO
        OOOOO
        OXOXO
        OOOOO
        """
    ).strip()
    assert solve(task) == 436


def test_solve_3():
    task = dedent(
        """
        EEEEE
        EXXXX
        EEEEE
        EXXXX
        EEEEE
        """
    ).strip()
    assert solve(task) == 236


def test_solve_4():
    task = dedent(
        """
        AAAAAA
        AAABBA
        AAABBA
        ABBAAA
        ABBAAA
        AAAAAA
        """
    ).strip()
    assert solve(task) == 368


def test_solve_5():
    task = dedent(
        """
        RRRRIICCFF
        RRRRIICCCF
        VVRRRCCFFF
        VVRCCCJFFF
        VVVVCJJCFE
        VVIVCCJJEE
        VVIIICJJEE
        MIIIIIJJEE
        MIIISIJEEE
        MMMISSJEEE
        """
    ).strip()
    assert solve(task) == 1206
