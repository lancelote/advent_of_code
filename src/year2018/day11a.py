"""Day 11 Part 1: Chronal Charge.

You watch the Elves and their sleigh fade into the distance as they head toward
the North Pole.

Actually, you're the one fading. The falling sensation returns.

The low fuel warning light is illuminated on your wrist-mounted device. Tapping
it once causes it to project a hologram of the situation: a 300x300 grid of
fuel cells and their current power levels, some negative. You're not sure what
negative power means in the context of time travel, but it can't be good.

Each fuel cell has a coordinate ranging from 1 to 300 in both the X
(horizontal) and Y (vertical) direction. In X,Y notation, the top-left cell is
1,1, and the top-right cell is 300,1.

The interface lets you select any 3x3 square of fuel cells. To increase your
chances of getting to your destination, you decide to choose the 3x3 square
with the largest total power.

The power level in a given fuel cell can be found through the following
process:

    - Find the fuel cell's rack ID, which is its X coordinate plus 10.
    - Begin with a power level of the rack ID times the Y coordinate.
    - Increase the power level by the value of the grid serial number
      (your puzzle input).
    - Set the power level to itself multiplied by the rack ID.
    - Keep only the hundreds digit of the power level (so 12345 becomes 3;
      numbers with no hundreds digit become 0).
    - Subtract 5 from the power level.

For example, to find the power level of the fuel cell at 3,5 in a grid with
serial number 8:

    - The rack ID is 3 + 10 = 13.
    - The power level starts at 13 * 5 = 65.
    - Adding the serial number produces 65 + 8 = 73.
    - Multiplying by the rack ID produces 73 * 13 = 949.
    - The hundreds digit of 949 is 9.
    - Subtracting 5 produces 9 - 5 = 4.

So, the power level of this fuel cell is 4.

Here are some more example power levels:

    - Fuel cell at  122,79, grid serial number 57: power level -5.
    - Fuel cell at 217,196, grid serial number 39: power level  0.
    - Fuel cell at 101,153, grid serial number 71: power level  4.

Your goal is to find the 3x3 square which has the largest total power.
The square must be entirely within the 300x300 grid. Identify this square using
the X,Y coordinate of its top-left fuel cell. For example:

For grid serial number 18, the largest total 3x3 square has a top-left corner
of 33,45 (with a total power of 29); these fuel cells appear in the middle of
this 5x5 region:

    -2  -4   4   4   4
    -4   4   4   4  -5
     4   3   3   4  -4
     1   1   2   4  -3
    -1   0   2  -5  -2

For grid serial number 42, the largest 3x3 square's top-left is 21,61 (with a
total power of 30); they are in the middle of this region:

    -3   4   2   2   2
    -4   4   3   3   4
    -5   3   3   4  -4
     4   3   3   4  -3
     3   3   3  -5  -1

What is the X,Y coordinate of the top-left fuel cell of the 3x3 square with the
largest total power?
"""

from collections import defaultdict
from functools import lru_cache
from itertools import product
from typing import DefaultDict, Tuple

Power = int
Cell = Tuple[int, int]


class Grid:
    """Power grid."""

    def __init__(self, serial: int, side: int):
        """Where serial is grid serial number and side is a side length."""
        self.side = side
        self.cells: DefaultDict[Cell, Power] = defaultdict(int)
        for x, y in product(range(side), range(side)):
            self.cells[(x, y)] = self.get_power_level(x, y, serial)

    def show(self):
        """Plot a human readable grid image."""
        grid = [["." for _ in range(self.side)] for _ in range(self.side)]
        for cell, value in self.cells.items():
            x, y = cell
            grid[y][x] = f"{value}".rjust(2)
        print("\n")
        print("\n".join(" ".join(line) for line in grid))

    @staticmethod
    def get_power_level(x: int, y: int, serial: int) -> Power:
        """Get cell power level."""
        rack_id = x + 10
        power_level = rack_id * y
        power_level += serial
        power_level *= rack_id
        try:
            power_level = int(str(power_level)[-3])
        except IndexError:
            power_level = 0
        power_level -= 5
        return power_level

    @lru_cache(0)  # Compatibility with a derived class
    def get_square_power(self, x: int, y: int, size: int) -> Power:
        """Calculate a cell square sum power."""
        square_power = 0
        for dx in range(x, x + size):
            for dy in range(y, y + size):
                square_power += self.cells[(dx, dy)]
        return square_power

    def get_biggest_square(self, size) -> Tuple[Cell, Power]:
        """Get left cell coordinates of a most powerful grid square."""
        biggest_power = -99
        top_left_corner = (0, 0)
        side_range = range(self.side - size - 1)

        for x, y in product(side_range, side_range):
            square_power = self.get_square_power(x, y, size)
            if square_power > biggest_power:
                biggest_power = square_power
                top_left_corner = (x, y)
        return top_left_corner, biggest_power


def solve(task: str) -> Cell:
    """Find the biggest area top left corner by a given grid serial."""
    grid = Grid(serial=int(task), side=300)
    cell, _ = grid.get_biggest_square(size=3)
    return cell
