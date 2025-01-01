"""2024 - Day 12 Part 1: Garden Groups"""

from textwrap import dedent

from src.year2024.day12a import solve


def test_solve_1():
    task = dedent(
        """
        AAAA
        BBCD
        BBCC
        EEEC
        """
    ).strip()
    assert solve(task) == 140


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
    assert solve(task) == 772


def test_solve_3():
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
    assert solve(task) == 1930