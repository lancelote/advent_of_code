"""2021 - Day 18 Part 1: Snailfish."""
from __future__ import annotations

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


class Leaf(Node):
    def __init__(self, value: int) -> None:
        self.value = value

    @property
    def magnitude(self) -> int:
        return self.value


class Branch(Node):
    def __init__(self, left: Node, right: Node) -> None:
        self.left = left
        self.right = right

    @classmethod
    def from_tokens(cls, tokens: Iterator[str]) -> Branch:
        left = Node.from_tokens(tokens)
        right = Node.from_tokens(tokens)
        return cls(left, right)

    @property
    def magnitude(self) -> int:
        return 3 * self.left.magnitude + 2 * self.right.magnitude


def solve(task: str) -> int:
    # ToDo: convert to generator
    # nums = [Branch.from_line(line) for line in task.splitlines()]
    # result = sum(nums)
    # return result.magnitude
    raise NotImplementedError
