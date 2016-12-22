# pylint: disable=invalid-name

"""Day 1: No Time for a Taxicab.

Santa's sleigh uses a very high-precision clock to guide its movements, and
the clock's oscillator is regulated by stars. Unfortunately, the stars have
been stolen... by the Easter Bunny. To save Christmas, Santa needs you to
retrieve all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each
day in the advent calendar; the second puzzle is unlocked when you complete
the first. Each puzzle grants one star. Good luck!

You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near",
unfortunately, is as close as you can get - the instructions on the Easter
Bunny Recruiting Document the Elves intercepted start here, and nobody had time
to work them out further.

The Document indicates that you should start at the given coordinates (where
you just landed) and face North. Then, follow the provided sequence: either
turn left (L) or right (R) 90 degrees, then walk forward the given number of
blocks, ending at a new intersection.

There's no time to follow such ridiculous instructions on foot, though, so you
take a moment and work out the destination. Given that you can only walk on the
street grid of the city, how far is the shortest path to the destination?

For example:

    - Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks
      away.
    - R2, R2, R2 leaves you 2 blocks due South of your starting position, which
      is 2 blocks away.
    - R5, L5, R5, R3 leaves you 12 blocks away.
"""

from collections import namedtuple
from typing import List

Instruction = namedtuple('Instruction', 'direction distance')


class Point(object):
    """Point coordinates representation."""

    def __init__(self, x=0, y=0):
        """2D point representation.

        Args:
            x (int): x coordinates
            y (int): y coordinates
        """
        self.x = x
        self.y = y

    def move(self, direction: int, distance: int):
        """Move the point to given direction by given distance."""
        if direction == 0:    # North
            self.y += distance
        elif direction == 1:  # East
            self.x += distance
        elif direction == 2:  # South
            self.y -= distance
        elif direction == 3:  # West
            self.x -= distance

    def distance_from_zero(self) -> int:
        """Compute squared city distance from (0, 0) to the point."""
        return abs(self.x) + abs(self.y)

    def __repr__(self):
        """Point(1, 2) -> (1, 2)."""
        return '(%s, %s)' % (self.x, self.y)

    def __eq__(self, other):
        """Check if the two Point equal (have the same coordinates)."""
        return self.x == other.x and self.y == other.y


def processed_data(data: str) -> List[Instruction]:
    """Convert raw sequence of instructions into the list of named tuples."""
    return [Instruction(x[0], int(x[1:])) for x in data.split(', ')]


def update_direction(direction, turn):
    """Return the directions ID after the given turn."""
    if turn == 'R':
        return (direction + 1) % 4
    elif turn == 'L':
        return (direction - 1) % 4


def solve(task: str) -> int:
    """Compute how many blocks away is Easter Bunny HQ."""
    direction = 0  # North
    current = Point()
    instructions = processed_data(task)  # type: List[Instruction]

    for instruction in instructions:
        direction = update_direction(direction, instruction.direction)
        current.move(direction, instruction.distance)
    return current.distance_from_zero()
