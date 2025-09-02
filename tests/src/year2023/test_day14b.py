"""2023 - Day 14 Part 2: Parabolic Reflector Dish"""

from textwrap import dedent

from src.year2023.day14b import Platform
from src.year2023.day14b import cycle
from src.year2023.day14b import solve


def to_str(platform: Platform) -> str:
    return "\n".join("".join(line) for line in platform)


def test_cycle():
    task = dedent(
        """
        O....#....
        O.OO#....#
        .....##...
        OO.#O....O
        .O.....O#.
        O.#..O.#.#
        ..O..#O..O
        .......O..
        #....###..
        #OO..#....
        """
    ).strip()
    platform = [list(line) for line in task.splitlines()]

    cycle(platform)

    assert (
        to_str(platform)
        == dedent(
            """
        .....#....
        ....#...O#
        ...OO##...
        .OO#......
        .....OOO#.
        .O#...O#.#
        ....O#....
        ......OOOO
        #...O###..
        #..OO#....
        """
        ).strip()
    )

    cycle(platform)

    assert (
        to_str(platform)
        == dedent(
            """
        .....#....
        ....#...O#
        .....##...
        ..O#......
        .....OOO#.
        .O#...O#.#
        ....O#...O
        .......OOO
        #..OO###..
        #.OOO#...O
        """
        ).strip()
    )

    cycle(platform)

    assert (
        to_str(platform)
        == dedent(
            """
        .....#....
        ....#...O#
        .....##...
        ..O#......
        .....OOO#.
        .O#...O#.#
        ....O#...O
        .......OOO
        #...O###.O
        #.OOO#...O
        """
        ).strip()
    )


def test_solve():
    task = dedent(
        """
        O....#....
        O.OO#....#
        .....##...
        OO.#O....O
        .O.....O#.
        O.#..O.#.#
        ..O..#O..O
        .......O..
        #....###..
        #OO..#....
        """
    ).strip()
    assert solve(task) == 64
