"""2017 - Day 3 Part 1: Spiral Memory.

You come across an experimental new kind of memory stored on an infinite
two-dimensional grid.

Each square on the grid is allocated in a spiral pattern starting at a
location marked 1 and then counting up while spiraling outward. For example,
the first few squares are allocated like this:

    17  16  15  14  13
    18   5   4   3  12
    19   6   1   2  11
    20   7   8   9  10
    21  22  23---> ...

While this is very space-efficient (no squares are skipped), requested data
must be carried back to square 1 (the location of the only access port for
this memory system) by programs that can only move up, down, left, or right.
They always take the shortest path: the Manhattan Distance between the
location of the data and square 1.

For example:

    - Data from square 1 is carried 0 steps, since it's at the access port.
    - Data from square 12 is carried 3 steps, such as: down, left, left.
    - Data from square 23 is carried only 2 steps: up twice.
    - Data from square 1024 must be carried 31 steps.

How many steps are required to carry the data from the square identified in
your puzzle input all the way to the access port?
"""

import math


def get_circle_number(number: int) -> int:
    """Return circle number where given number is placed."""
    # Let's consider arithmetic progression with first item 1 and diff 2:
    #
    #    1 3 5 7 9 ...
    #
    # Numbers in circle "n" of memory storage are limited by the square of n'th
    # item from this progression (index base 0), e.g. 3'rd circle items are
    # limited by the square of 3'rd item of progression which is 7*7 = 49

    # Knowing that let's calculate square root of the given number and round
    # it up, this square root is going to either be item from progression by
    # which all items in the current circle are limited or item - 1
    square = int(math.ceil(math.sqrt(number)))

    # item - 1 is an even number so we're going to compensate this
    # by adding 1 to the rounded square root if it's even
    square = square + 1 if square % 2 == 0 else square

    # Now we are going to find which progression index this item has. This
    # index is a circle number in a memory storage. Additional -1 to make it
    # base 0

    # Derived from the formula of n'th child of arithmetic progression:
    #
    #     a_n = a_1 + (n - 1)*d
    #
    # where:
    #
    #     a_n - n'th progression child
    #     a_1 - first progression child
    #     n   - progression child of interest order number
    return (square + 1) // 2 - 1


def get_deviation(number: int, circle: int) -> int:
    """Get distance to horizontal or vertical line from 1."""
    # Special case for memory storage center
    if number == 1:
        return 0

    # Side length derived from progression n'th child formula
    side = circle * 2 + 1

    # Normalize number - bottom left circle number is 0, then +1 clock-wise
    deviation = abs(number - side ** 2)

    # Split by side - number should not exceed side length - 1
    deviation %= side - 1

    # Subtract half of side length to count distance from side center
    deviation = abs(deviation - side // 2)

    return deviation


def solve(task: str) -> int:
    """Count Manhattan Distance to number in memory storage."""
    # To reach given number
    number = int(task)

    # We need firstly to get to the given memory storage circle
    circle = get_circle_number(number)

    # And make some steps from the side center to this number
    deviation = get_deviation(number, circle)
    return circle + deviation
