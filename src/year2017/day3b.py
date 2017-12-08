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


class Memory:
    def __init__(self):
        self.x, self.y = 0, 0
        self.dx, self.dy = 1, 0
        self.circle = 1
        self.data = {(0, 0): 1}

    @staticmethod
    def neighbors(x, y):
        return [(x + dx, y + dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if dx or dy]

    @property
    def side_length(self):
        """Return given circle length."""
        return 2 * self.circle + 1

    def shift(self, side):
        shifts = {
            0: (0, 1),  # Left
            1: (-1, 0),  # Top
            2: (0, -1),  # Right
            3: (1, 0),  # Left
        }
        self.dx, self.dy = shifts[side]

    def sum_neighbors(self):
        return sum(self.data.get(neighbor, 0) for neighbor in self.neighbors(self.x, self.y))

    def __iter__(self):
        yield 1
        for _ in itertools.count(start=1):
            for side in [0, 1, 2, 3]:
                for _ in range(self.side_length - 1):
                    self.x += self.dx
                    self.y += self.dy
                    value = self.sum_neighbors()
                    self.data[(self.x, self.y)] = value
                    yield value
                self.shift(side)
            self.circle += 1


def solve(task: str) -> int:
    limit = int(task)
    for item in Memory():
        if item < limit:
            return item
