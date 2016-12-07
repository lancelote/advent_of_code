# coding=utf-8

"""
--- Day 1 Part Two ---

Now, given the same instructions, find the position of the first character that
causes him to enter the basement (floor -1). The first character in the
instructions has position 1, the second character has position 2, and so on.

For example:

    ) causes him to enter the basement at character position 1.
    ()()) causes him to enter the basement at character position 5.

What is the position of the character that causes Santa to first enter the
basement?
"""


def solve(task):
    """
    Solve puzzle

    Args:
        task (str): Puzzle input

    Returns:
        int: Puzzle solution
    """
    level = 0
    i = 0
    for char in task:
        i += 1
        if char == '(':
            level += 1
        elif char == ')':
            level -= 1
        if level == -1:
            return i
