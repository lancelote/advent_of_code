"""Part Two.

The next year, to speed up the process, Santa creates a robot version of
himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the
same starting house), then take turns moving based on instructions from the
elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

    ^v delivers presents to 3 houses, because Santa goes north, and then
    Robo-Santa goes south.

    ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up
    back where they started.

    ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one
    direction and Robo-Santa going the other.
"""
from src.year2015.day3a import visit_houses


def solve(task):
    """Solve the puzzle.

    Args:
        task (str): '>^<v...'

    Returns:
        int: Number of houses with at least one present

    """
    santa_task = task[0::2]
    robo_santa_task = task[1::2]
    visited_by_santa = visit_houses(santa_task)
    visited_by_robo = visit_houses(robo_santa_task)
    visited_by_santa.update(visited_by_robo)
    return len(visited_by_santa)
