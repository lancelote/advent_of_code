"""2019 - Day 3 Part 2: Crossed Wires."""

from collections import defaultdict
from dataclasses import dataclass, field
from typing import DefaultDict

from src.year2019.day03a import Grid as BaseGrid
from src.year2019.day03a import Node, parse_command


@dataclass
class Grid(BaseGrid):
    """Grid counting steps each wire takes."""

    _intersections: list[int] = field(default_factory=list)

    def plot(self, wire: str) -> None:
        """Add wire to the grid."""
        step = 0
        nodes: DefaultDict[Node, int] = defaultdict(int)

        for command in wire.strip().split(","):
            direction, steps = parse_command(command)
            for _ in range(steps):
                step += 1
                self.shift(direction)
                if not nodes[self.current]:
                    nodes[self.current] = step

        self.merge_dict(nodes)
        self.reset()

    def merge_dict(self, nodes: dict[tuple[int, int], int]) -> None:
        """Merge wire nodes into the actual grid."""
        for k, v in nodes.items():
            if self.nodes[k]:
                self._intersections.append(self.nodes[k] + v)
            else:
                self.nodes[k] = v

    @property
    def closest(self) -> int:
        """Closest intersection taking into account wires length."""
        assert self.list_intersections
        return min(self.list_intersections)

    @property
    def list_intersections(self) -> list[int]:
        """Get the list of intersection distances."""
        return self._intersections


def solve(task: str) -> int:
    """Find the closest intersection based on the wires length to it."""
    grid = Grid()

    for wire in task.strip().split("\n"):
        grid.plot(wire)

    return grid.closest
