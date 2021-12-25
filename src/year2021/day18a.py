"""2021 - Day 18 Part 1: Snailfish."""
from __future__ import annotations

import math
import re
from typing import Iterator


def tokenize(line: str) -> Iterator[str]:
    for token in re.findall(r"(\[|\d+)", line):
        yield token


class Node:
    @classmethod
    def from_line(cls, line: str) -> Node:
        return cls.from_tokens(tokenize(line))

    @classmethod
    def from_tokens(cls, tokens: Iterator[str]) -> Node:
        for token in tokens:
            if token == "[":
                return Branch.from_tokens(tokens)
            else:
                return Leaf(int(token))
        raise ValueError("no tokens")

    @property
    def magnitude(self) -> int:
        raise NotImplementedError

    def reduce(self) -> bool:
        return self.explode() or self.split()

    def explode(self) -> bool:
        raise NotImplementedError

    def split(self) -> bool:
        raise NotImplementedError

    def __add__(self, other: Node) -> Node:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


class Leaf(Node):
    def __init__(self, value: int) -> None:
        self.value = value

    @property
    def magnitude(self) -> int:
        return self.value

    def explode(self) -> bool:
        raise ValueError("cannot explode leaf")

    def split(self) -> bool:
        return False  # Cannot self split

    def __add__(self, other: Node) -> Leaf:
        raise ValueError("cannot sum leafs")

    def __str__(self) -> str:
        return str(self.value)


class Branch(Node):
    def __init__(self, left: Node, right: Node) -> None:
        self.left = left
        self.right = right

    @classmethod
    def from_tokens(cls, tokens: Iterator[str]) -> Branch:
        left = Node.from_tokens(tokens)
        right = Node.from_tokens(tokens)
        return cls(left, right)

    @classmethod
    def from_int(cls, value: int) -> Branch:
        left = Leaf(math.floor(value / 2))
        right = Leaf(math.ceil(value / 2))
        return cls(left, right)

    @property
    def magnitude(self) -> int:
        return 3 * self.left.magnitude + 2 * self.right.magnitude

    def explode(self) -> bool:
        return False

    def split(self) -> bool:
        if isinstance(self.left, Leaf) and self.left.value >= 10:
            self.left = Branch.from_int(self.left.value)
            return True
        elif isinstance(self.right, Leaf) and self.right.value >= 10:
            self.right = Branch.from_int(self.right.value)
            return True
        else:
            return self.left.split() or self.right.split()

    def __add__(self, other: Node) -> Branch:
        return Branch(left=self, right=other)

    def __str__(self) -> str:
        return f"[{self.left},{self.right}]"


def solve(task: str) -> int:
    # ToDo: convert to generator
    # nums = [Branch.from_line(line) for line in task.splitlines()]
    # result = sum(nums)
    # return result.magnitude
    raise NotImplementedError
