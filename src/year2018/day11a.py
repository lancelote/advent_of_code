"""Day 11 Part 1: Chronal Charge."""

from collections import defaultdict
from itertools import product
from typing import DefaultDict
from typing import TypeAlias

Power: TypeAlias = int
Cell: TypeAlias = tuple[int, int]


class Grid:
    """Power grid."""

    def __init__(self, serial: int, side: int) -> None:
        """Where serial is grid serial number and side is a side length."""
        self.side = side
        self.cells: DefaultDict[Cell, Power] = defaultdict(int)
        for x, y in product(range(side), range(side)):
            self.cells[(x, y)] = self.get_power_level(x, y, serial)

    def show(self) -> None:
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

    def get_square_power(self, x: int, y: int, size: int) -> Power:
        """Calculate a cell square sum power."""
        square_power = 0
        for dx in range(x, x + size):
            for dy in range(y, y + size):
                square_power += self.cells[(dx, dy)]
        return square_power

    def get_biggest_square(self, size: int) -> tuple[Cell, Power]:
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
