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

    def __add__(self, other: Node) -> Branch:
        return Branch(left=self, right=other)

    def __str__(self) -> str:
        return f"[{self.left},{self.right}]"


def explode(num: Node) -> Node:
    ...


def split(num: Node) -> Node:
    was_split = False

    def traverse(node: Node) -> Node:
        nonlocal was_split

        if isinstance(node, Leaf):
            if node.value >= 10 and not was_split:
                was_split = True
                return Branch.from_int(node.value)
            else:
                return Leaf(node.value)
        elif isinstance(node, Branch):
            return Branch(traverse(node.left), traverse(node.right))

    return traverse(num)


def solve(task: str) -> int:
    # ToDo: convert to generator
    # nums = [Branch.from_line(line) for line in task.splitlines()]
    # result = sum(nums)
    # return result.magnitude
    raise NotImplementedError
