"""2022 - Day 7 Part 1: No Space Left On Device."""
from textwrap import dedent

from src.year2022.day07a import solve


def test_solve():
    task = dedent(
        """
        $ cd /
        $ ls
        dir a
        14848514 b.txt
        8504156 c.dat
        dir d
        $ cd a
        $ ls
        dir e
        29116 f
        2557 g
        62596 h.lst
        $ cd e
        $ ls
        584 i
        $ cd ..
        $ cd ..
        $ cd d
        $ ls
        4060174 j
        8033020 d.log
        5626152 d.ext
        7214296 k
        """
    ).strip()
    assert solve(task) == 95437


def test_same_name():
    task = dedent(
        """
        $ cd /
        $ ls
        dir foo
        1 bar.txt
        $ cd foo
        $ ls
        dir foo
        2 baz.txt
        $ cd foo
        $ ls
        3 bak.txt
        """
    ).strip()
    assert solve(task) == 6 + 5 + 3
