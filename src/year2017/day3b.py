"""2017 - Day 3 Part 2: Spiral Memory.

As a stress test on the system, the programs here clear the grid and then
store the value 1 in square 1. Then, in the same allocation order as shown
above, they store the sum of the values in all adjacent squares, including
diagonals.

So, the first few squares' values are chosen as follows:

    - Square 1 starts with the value 1.
    - Square 2 has only one adjacent filled square (with value 1), so it also
      stores 1.
    - Square 3 has both of the above squares as neighbors and stores the sum
      of their values, 2.
    - Square 4 has all three of the aforementioned squares as neighbors and
      stores the sum of their values, 4.
    - Square 5 only has the first and fourth squares as neighbors, so it gets
      the value 5.

Once a square is written, its value does not change. Therefore, the first few
squares would receive the following values:

    147  142  133  122   59
    304    5    4    2   57
    330   10    1    1   54
    351   11   23   25   26
    362  747  806--->   ...


    16  15  14  13  12
    17   4   3   2  11
    18   5   0   1  10
    19   6   7   8   9
    20  21  22  23  24


What is the first value written that is larger than your puzzle input?
"""

import itertools

from collections.abc import Iterable


class Memory(Iterable):
    """Circle memory representation."""

    def __init__(self):
        """Initialize memory with two first cells pre-filled.

        x, y - coordinates of the current cell
        dx, dy - coordinate difference between current and next cell
        circle - current circle number
        data - cell values based on coordinates
        """
        self.x, self.y = 1, 0
        self.dx, self.dy = 0, 0
        self.circle = 1
        self.data = {(0, 0): 1, (1, 0): 1}

    def side_length(self, side: int) -> int:
        """Return number of items to pass on the given side."""
        length = 2 * self.circle + 1
        if side == 0:
            length -= 1  # We need less steps on the right side
        elif side == 3:
            length += 1  # We need one more item to step out of the last side
        return length

    def adjust_direction(self, side: int) -> None:
        """Adjust coordinates difference according to a given side number."""
        shifts = {
            0: (0, 1),  # Right
            1: (-1, 0),  # Top
            2: (0, -1),  # Left
            3: (1, 0),  # Bottom
        }
        self.dx, self.dy = shifts[side]

    @property
    def neighbors(self):
        """Yield coordinates of the current cell neighbors."""
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx or dy:
                    yield (self.x + dx, self.y + dy)

    @property
    def sum_neighbors(self):
        """Get sum of the current cell neighbors values."""
        return sum(self.data.get(neighbor, 0) for neighbor in self.neighbors)

    def __iter__(self):
        """Yield next cell value."""
        yield 1  # First cell
        yield 1  # Second cell

        for _ in itertools.count(start=1):  # Circles
            for side in [0, 1, 2, 3]:
                self.adjust_direction(side)
                for _ in range(self.side_length(side) - 1):  # Items
                    self.x += self.dx
                    self.y += self.dy
                    value = self.sum_neighbors
                    self.data[(self.x, self.y)] = value
                    yield value
            self.circle += 1


def solve(task: str) -> int:
    """Found first cell value that is larger than input."""
    item = 0
    limit = int(task)
    for item in Memory():
        if item > limit:
            break
    return item
