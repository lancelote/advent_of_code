"""2021 - Day 18 Part 1: Snailfish."""
from __future__ import annotations

import functools
import math
import re
from collections.abc import Iterator


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

    def __add__(self, other: Node) -> Node:
        return reduce(Branch(left=self, right=other))

    def __str__(self) -> str:
        return f"[{self.left},{self.right}]"


def reduce(num: Node) -> Node:
    while True:
        num_after_explode = explode(num)
        if str(num_after_explode) == str(num):
            num_after_split = split(num)
            if str(num_after_split) == str(num):
                break
            else:
                num = num_after_split
        else:
            num = num_after_explode
    return num


def duplicate(node: Node) -> Node:
    if isinstance(node, Leaf):
        return Leaf(node.value)
    elif isinstance(node, Branch):
        return Branch(duplicate(node.left), duplicate(node.right))
    raise ValueError(f"unknown node type: {node}")


def explode(num: Node) -> Node:
    add_to_left = 0
    add_to_right = 0
    left_added = False
    right_added = False
    exploded_node: Node | None = None
    path_to_exploded_node = []

    num = duplicate(num)

    def traverse(node: Node, depth: int, path: list[Node]) -> Node:
        """Find the exploding node and replace it with a zero leaf."""
        nonlocal add_to_left
        nonlocal add_to_right
        nonlocal exploded_node
        nonlocal path_to_exploded_node

        if isinstance(node, Leaf):
            return Leaf(node.value)
        elif isinstance(node, Branch):
            if depth == 4 and exploded_node is None:
                assert isinstance(node.left, Leaf)
                assert isinstance(node.right, Leaf)

                add_to_left = node.left.value
                add_to_right = node.right.value
                path_to_exploded_node = path
                exploded_node = Leaf(0)

                return exploded_node
            else:
                dummy_node = Node()
                branch = Branch(dummy_node, dummy_node)
                branch.left = traverse(node.left, depth + 1, path + [branch])
                branch.right = traverse(node.right, depth + 1, path + [branch])
            return branch

        raise ValueError(f"unknown node type: {node}")

    num = traverse(num, depth=0, path=[])

    def add_exploded_parts(last: Node) -> None:
        """Go the tree up searching for nodes to add exploded parts to."""
        nonlocal left_added
        nonlocal right_added

        if not path_to_exploded_node:
            return

        current = path_to_exploded_node.pop()
        assert isinstance(current, Branch)

        if current.left != last and not left_added:
            add_to_most_right(current.left, add_to_left)
            left_added = True
        elif current.right != last and not right_added:
            add_to_most_left(current.right, add_to_right)
            right_added = True

        if not (left_added and right_added):
            add_exploded_parts(last=current)

    def add_to_most_right(node: Node, value: int) -> None:
        """Add the value to the rightest leaf."""
        if isinstance(node, Leaf):
            node.value += value
        elif isinstance(node, Branch):
            add_to_most_right(node.right, value)
        else:
            ValueError(f"the hell is {node}?")

    def add_to_most_left(node: Node, value: int) -> None:
        """Add the value to the leftest leaf."""
        if isinstance(node, Leaf):
            node.value += value
        elif isinstance(node, Branch):
            add_to_most_left(node.left, value)
        else:
            ValueError(f"the hell is {node}?")

    if exploded_node is not None:
        add_exploded_parts(last=exploded_node)

    return num


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

        raise ValueError(f"unknown node type: {node}")

    return traverse(num)


def solve(task: str) -> int:
    nums = [Node.from_line(line) for line in task.splitlines()]
    result = functools.reduce(lambda x, y: x + y, nums)
    return result.magnitude
