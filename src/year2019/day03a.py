"""2019 - Day 3 Part 1: Crossed Wires."""

from collections import defaultdict
from dataclasses import dataclass, field
from typing import DefaultDict

SHIFT = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1),
}

Node = tuple[int, int]
Nodes = DefaultDict[Node, int]


def parse_command(command: str) -> tuple[str, int]:
    """Parse command into direction char and number of steps."""
    direction = command[0]
    steps = int(command[1:])
    return direction, steps


@dataclass
class Grid:
    """Grid with wires on top."""

    nodes: Nodes = field(default_factory=lambda: defaultdict(int))
    current: Node = (0, 0)

    def plot(self, wire: str) -> None:
        """Add wire to the grid."""
        nodes = set()

        for command in wire.strip().split(","):
            direction, steps = parse_command(command)
            for _ in range(steps):
                self.shift(direction)
                nodes.add(self.current)

        self.merge_set(nodes)
        self.reset()

    def merge_set(self, nodes: set[tuple[int, int]]) -> None:
        """Merge wire nodes into the actual grid."""
        for node in nodes:
            self.nodes[node] += 1

    def reset(self) -> None:
        """Reset the grid after the wire plotting."""
        self.current = (0, 0)

    def shift(self, direction: str) -> None:
        """Move current according to new command."""
        assert direction in SHIFT.keys()
        shift_x, shift_y = SHIFT[direction]
        self.current = (self.current[0] + shift_x, self.current[1] + shift_y)

    @property
    def tuple_intersections(self) -> list[tuple[int, int]]:
        """Return all intersection found on the grid."""
        return [k for (k, v) in self.nodes.items() if v > 1]

    @property
    def closest(self) -> int:
        """Return the distance to the closest to (0, 0) intersection."""
        node = min(
            self.tuple_intersections, key=lambda x: abs(x[0]) + abs(x[1])
        )
        return abs(node[0]) + abs(node[1])


def solve(task: str) -> int:
    """Find the closest to (0, 0) intersection Manhattan distance."""
    grid = Grid()

    for wire in task.strip().split("\n"):
        grid.plot(wire)

    return grid.closest
