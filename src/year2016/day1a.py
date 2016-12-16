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


def processed_data(data: str) -> List[namedtuple]:
    """Convert raw sequence of instructions into the list of namedtuples."""
    instruction = namedtuple('Instruction', 'direction distance')
    return [instruction(x[0], int(x[1:])) for x in data.split(', ')]


def update_direction(direction, turn):
    """Return the directions ID after the given turn."""
    if turn == 'R':
        return (direction + 1) % 4
    elif turn == 'L':
        return (direction - 1) % 4


def solve(task: str) -> int:
    """Compute how many blocks away is Easter Bunny HQ."""
    direction = 0  # North
    bunny_hq = [0, 0]
    instructions = processed_data(task)

    for instruction in instructions:
        direction = update_direction(direction, instruction.direction)

        if direction == 0:    # North
            bunny_hq[1] += instruction.distance
        elif direction == 1:  # East
            bunny_hq[0] += instruction.distance
        elif direction == 2:  # South
            bunny_hq[1] -= instruction.distance
        elif direction == 3:  # West
            bunny_hq[0] -= instruction.distance
    return abs(bunny_hq[0]) + abs(bunny_hq[1])
