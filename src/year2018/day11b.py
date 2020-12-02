"""Day 11 Part 2: Chronal Charge.

You discover a dial on the side of the device; it seems to let you select a
square of any size, not just 3x3. Sizes from 1x1 to 300x300 are supported.

Realizing this, you now must find the square of any size with the largest
total power. Identify this square by including its size as a third parameter
after the top-left coordinate: a 9x9 square with a top-left corner of 3,5
is identified as 3,5,9.

For example:

    For grid serial number 18, the largest total square (with a total power
      of 113) is 16x16 and has a top-left corner of 90,269, so its identifier
      is 90,269,16.
    For grid serial number 42, the largest total square (with a total power
      of 119) is 12x12 and has a top-left corner of 232,251, so its identifier
      is 232,251,12.

What is the X,Y,size identifier of the square with the largest total power?
"""
from functools import lru_cache
from typing import Tuple

from src.year2018.day11a import Cell
from src.year2018.day11a import Grid
from src.year2018.day11a import Power

Size = int


class CachedGrid(Grid):
    """Grid with a cached square power calculation."""

    def get_border_power(self, x: int, y: int, size: int) -> Power:
        """Calculate left and bottom area brims power."""
        power = 0
        for dy in range(y, y + size - 1):
            power += self.cells[(x + size - 1, dy)]
        for dx in range(x, x + size):
            power += self.cells[(dx, y + size - 1)]
        return power

    @lru_cache(10 ** 7)
    def get_square_power(self, x: int, y: int, size: int) -> Power:
        """Calculate a cell square sum power by caching previous calls."""
        if size == 1:
            return self.cells[(x, y)]
        else:
            border = self.get_border_power(x, y, size)
            return self.get_square_power(x, y, size - 1) + border


def solve(task: str) -> Tuple[Cell, Size]:
    """Find the biggest area top left corner and size."""
    grid = CachedGrid(serial=int(task), side=300)
    biggest_size = 0
    biggest_power = 0
    biggest_cell = (0, 0)
    for size in range(1, 50):  # Limit the search
        print("size:", size)
        cell, power = grid.get_biggest_square(size)
        if power > biggest_power:
            biggest_cell = cell
            biggest_size = size
            biggest_power = power
    return biggest_cell, biggest_size
