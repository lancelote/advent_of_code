"""2023 - Day 10 Part 2: Pipe Maze"""

from textwrap import dedent

from src.year2023.day10b import solve


def test_solve_0():
    task = dedent(
        """
        .....
        .S-7.
        .|.|.
        .L-J.
        .....
        """
    ).strip()
    assert solve(task) == 1


def test_solve_1():
    task = dedent(
        """
        ..F7.
        .FJ|.
        SJ.L7
        |F--J
        LJ...
        """
    ).strip()
    assert solve(task) == 1


def test_solve_2():
    task = dedent(
        """
        ...........
        .S-------7.
        .|F-----7|.
        .||.....||.
        .||.....||.
        .|L-7.F-J|.
        .|..|.|..|.
        .L--J.L--J.
        ...........
        """
    ).strip()
    assert solve(task) == 4


def test_solve_3():
    task = dedent(
        """
        ..........
        .S------7.
        .|F----7|.
        .||....||.
        .||....||.
        .|L-7F-J|.
        .|..||..|.
        .L--JL--J.
        ..........
        """
    ).strip()
    assert solve(task) == 4


def test_solve_4():
    task = dedent(
        """
        .F----7F7F7F7F-7....
        .|F--7||||||||FJ....
        .||.FJ||||||||L7....
        FJL7L7LJLJ||LJ.L-7..
        L--J.L7...LJS7F-7L7.
        ....F-J..F7FJ|L7L7L7
        ....L7.F7||L7|.L7L7|
        .....|FJLJ|FJ|F7|.LJ
        ....FJL-7.||.||||...
        ....L---J.LJ.LJLJ...
        """
    ).strip()
    assert solve(task) == 8


def test_solve_5():
    task = dedent(
        """
        FF7FSF7F7F7F7F7F---7
        L|LJ||||||||||||F--J
        FL-7LJLJ||||||LJL-77
        F--JF--7||LJLJ7F7FJ-
        L---JF-JLJ.||-FJLJJ7
        |F|F-JF---7F7-L7L|7|
        |FFJF7L7F-JF7|JL---7
        7-L-JL7||F7|L7F-7F7|
        L.L7LFJ|||||FJL7||LJ
        L7JLJL-JLJLJL--JLJ.L
        """
    ).strip()
    assert solve(task) == 10
