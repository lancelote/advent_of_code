"""2017 - Day 3 Part 2: Spiral Memory."""

import itertools
from collections.abc import Iterable, Iterator


class Memory(Iterable[int]):
    """Circle memory representation."""

    def __init__(self) -> None:
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
            length -= 1  # We need fewer steps on the right side
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
    def neighbors(self) -> Iterator[tuple[int, int]]:
        """Yield coordinates of the current cell neighbors."""
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx or dy:
                    yield self.x + dx, self.y + dy

    @property
    def sum_neighbors(self) -> int:
        """Get sum of the current cell neighbors values."""
        return sum(self.data.get(neighbor, 0) for neighbor in self.neighbors)

    def __iter__(self) -> Iterator[int]:
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
