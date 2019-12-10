"""2019 - Day 3 Part 1: Crossed Wires.

The gravity assist was successful, and you're well on your way to the Venus
refuelling station. During the rush back on Earth, the fuel management system
wasn't completely installed, so that's next on the priority list.

Opening the front panel reveals a jumble of wires. Specifically, two wires are
connected to a central port and extend outward on a grid. You trace the path
each wire takes as it leaves the central port, one wire per line of text (your
puzzle input).

The wires twist and turn, but the two wires occasionally cross paths. To fix
the circuit, you need to find the intersection point closest to the central
port. Because the wires are on a grid, use the Manhattan distance for this
measurement. While the wires do technically cross right at the central port
where they both start, this point does not count, nor does a wire count as
crossing with itself.

For example, if the first wire's path is R8,U5,L5,D3, then starting from the
central port (o), it goes right 8, up 5, left 5, and finally down 3:

    ...........
    ...........
    ...........
    ....+----+.
    ....|....|.
    ....|....|.
    ....|....|.
    .........|.
    .o-------+.
    ...........

Then, if the second wire's path is U7,R6,D4,L4, it goes up 7, right 6, down 4,
and left 4:

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

These wires cross at two locations (marked X), but the lower-left one is
closer to the central port: its distance is 3 + 3 = 6.

Here are a few more examples:

    R75,D30,R83,U83,L12,D49,R71,U7,L72
    U62,R66,U55,R34,D71,R55,D58,R83 = distance 159

    R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
    U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = distance 135

What is the Manhattan distance from the central port to the closest
intersection?
"""

from collections import defaultdict
from dataclasses import dataclass, field
from typing import DefaultDict, Tuple

SHIFT = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1),
}

Node = Tuple[int, int]
Nodes = DefaultDict[Node, int]


def parse_command(command: str) -> Tuple[str, int]:
    """Parse command into direction char and number of steps."""
    direction = command[0]
    steps = int(command[1:])
    return direction, steps


@dataclass
class Grid:
    """Grid with wires on top."""

    nodes: Nodes = field(default_factory=lambda: defaultdict(int))
    current: Node = (0, 0)

    def plot(self, wire: str):
        """Add wire to the grid."""
        nodes = set()

        for command in wire.strip().split(','):
            direction, steps = parse_command(command)
            for _ in range(steps):
                self.shift(direction)
                nodes.add(self.current)

        self.merge(nodes)
        self.reset()

    def merge(self, nodes):
        """Merge wire nodes into the actual grid."""
        for node in nodes:
            self.nodes[node] += 1

    def reset(self):
        """Reset the grid after the wire plotting."""
        self.current = (0, 0)

    def shift(self, direction: str):
        """Move current according to new command."""
        assert direction in SHIFT.keys()
        shift_x, shift_y = SHIFT[direction]
        self.current = (self.current[0] + shift_x, self.current[1] + shift_y)

    @property
    def intersections(self):
        """Return all intersection found on the grid."""
        return [k for (k, v) in self.nodes.items() if v > 1]

    @property
    def closest(self):
        """Return Manhattan distance to the closest to (0, 0) intersection."""
        node = min(self.intersections, key=lambda x: abs(x[0]) + abs(x[1]))
        return abs(node[0]) + abs(node[1])


def solve(task: str) -> int:
    """Find the closest to (0, 0) intersection Manhattan distance."""
    grid = Grid()

    for wire in task.strip().split('\n'):
        grid.plot(wire)

    return grid.closest
