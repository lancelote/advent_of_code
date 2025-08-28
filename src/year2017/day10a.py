r"""2017 - Day 10 Part 1: Knot Hash."""

from itertools import cycle, islice


class Rope:
    """Rope representation."""

    def __init__(self, nodes: list[int] | None = None) -> None:
        """By default rope consists of 256 segments."""
        self.nodes = nodes or list(range(256))
        self.shift = 0
        self.pos = 0

    def reverse(self, length: int) -> None:
        """Reverse selection of the rope."""
        rope_view = cycle(self.nodes[self.pos :] + self.nodes[: self.pos])
        selection = list(islice(rope_view, length))
        index = self.pos
        for node in reversed(selection):
            self.nodes[index] = node
            index = (index + 1) % len(self.nodes)

    def move(self, length: int) -> None:
        """Advance current position and increment shift."""
        self.pos = (self.pos + length + self.shift) % len(self.nodes)
        self.shift += 1

    def first_two_multiply(self) -> int:
        """Return multiplication of first two nodes."""
        return self.nodes[0] * self.nodes[1]


def process_data(data: str) -> list[int]:
    """Convert raw data into list of int lengths."""
    return [int(length) for length in data.split(",")]


def solve(task: str) -> int:
    """Find first two nodes multiplication result."""
    lengths = process_data(task)
    rope = Rope()
    for length in lengths:
        rope.reverse(length)
        rope.move(length)
    return rope.first_two_multiply()
