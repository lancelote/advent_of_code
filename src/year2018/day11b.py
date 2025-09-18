"""Day 11 Part 2: Chronal Charge."""

from typing import TypeAlias
from typing import override

from src.year2018.day11a import Cell
from src.year2018.day11a import Grid
from src.year2018.day11a import Power

Size: TypeAlias = int


class CachedGrid(Grid):
    """Grid with a cached square power calculation."""

    def __init__(self, serial: int, side: int) -> None:
        super().__init__(serial, side)
        self.cache: dict[tuple[int, int, int], Power] = {}

    def get_border_power(self, x: int, y: int, size: int) -> Power:
        """Calculate left and bottom area brims power."""
        power = 0
        for dy in range(y, y + size - 1):
            power += self.cells[(x + size - 1, dy)]
        for dx in range(x, x + size):
            power += self.cells[(dx, y + size - 1)]
        return power

    @override
    def get_square_power(self, x: int, y: int, size: int) -> Power:
        """Calculate a cell square sum power by caching previous calls."""
        if (x, y, size) in self.cache:
            return self.cache[(x, y, size)]

        if size == 1:
            result = self.cells[(x, y)]
        else:
            border = self.get_border_power(x, y, size)
            result = self.get_square_power(x, y, size - 1) + border

        self.cache[(x, y, size)] = result
        return result


def solve(task: str) -> tuple[Cell, Size]:
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
