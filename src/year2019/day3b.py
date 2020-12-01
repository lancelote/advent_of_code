"""2019 - Day 3 Part 2: Crossed Wires.

It turns out that this circuit is very timing-sensitive; you actually need to
minimize the signal delay.

To do this, calculate the number of steps each wire takes to reach each
intersection; choose the intersection where the sum of both wires' steps is
lowest. If a wire visits a position on the grid multiple times, use the steps
value from the first time it visits that position when calculating the total
value of a specific intersection.

The number of steps a wire takes is the total number of grid squares the wire
has entered to get to that location, including the intersection being
considered. Again consider the example from above:

    ...........
    .+-----+...
    .|.....|...
    .|..+--X-+.
    .|..|..|.|.
    .|.-X--+.|.
    .|..|....|.
    .|.......|.
    .o-------+.
    ...........

In the above example, the intersection closest to the central port is reached
after 8+5+5+2 = 20 steps by the first wire and 7+6+4+3 = 20 steps by the
second wire for a total of 20+20 = 40 steps.

However, the top-right intersection is better: the first wire takes only
8+5+2 = 15 and the second wire takes only 7+6+2 = 15,
a total of 15+15 = 30 steps.

Here are the best steps for the extra examples from above:

    R75,D30,R83,U83,L12,D49,R71,U7,L72
    U62,R66,U55,R34,D71,R55,D58,R83 = 610 steps
    R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
    U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = 410 steps

What is the fewest combined steps the wires must take to reach an
intersection?
"""

from collections import defaultdict
from typing import List, DefaultDict
from dataclasses import dataclass, field

from src.year2019.day3a import Grid as BaseGrid, parse_command, Node


@dataclass
class Grid(BaseGrid):
    """Grid counting steps each wire takes."""

    _intersections: List[int] = field(default_factory=list)

    def plot(self, wire: str):
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

        self.merge(nodes)
        self.reset()

    def merge(self, nodes):
        """Merge wire nodes into the actual grid."""
        for k, v in nodes.items():
            if self.nodes[k]:
                self._intersections.append(self.nodes[k] + v)
            else:
                self.nodes[k] = v

    @property
    def closest(self):
        """Closest intersection taking into account wires length."""
        assert self.intersections
        return min(self.intersections)

    @property
    def intersections(self) -> List[int]:
        """Get the list of intersection distances."""
        return self._intersections


def solve(task: str) -> int:
    """Find the closest intersection based on the wires length to it."""
    grid = Grid()

    for wire in task.strip().split("\n"):
        grid.plot(wire)

    return grid.closest
