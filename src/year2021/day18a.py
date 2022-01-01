"""2021 - Day 18 Part 1: Snailfish."""
from __future__ import annotations

import re
import math
from itertools import chain
from typing import Iterator


def tokenize(line: str) -> Iterator[str]:
    # only care about numbers and the open brackets
    for token in re.findall(r"(\[|\d+)", line):
        yield token


class ListNode:
    def __init__(self, data: str) -> None:
        self.data = data
        self.next: ListNode | None = None
        self.prev: ListNode | None = None

    def replace_with(self, node: ListNode) -> None:
        if self.prev:
            self.prev.next = node
            node.prev = self.prev
        if self.next:
            self.next.prev = node
            node.next = self.next

    def insert_after(self, node: ListNode) -> None:
        self.next = node.next
        node.next.prev = self
        node.next = self
        self.prev = node

    def __str__(self) -> str:
        return self.data


class LinkedList:
    def __init__(self) -> None:
        self.head: ListNode | None = None
        self.tail: ListNode | None = None

    def append(self, node: ListNode) -> None:
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def iter_data(self) -> Iterator[str]:
        for node in self.iter_nodes():
            yield node.data

    def iter_nodes(self) -> Iterator[ListNode]:
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def split(self) -> None:
        for node in self.iter_nodes():
            if node.data.isalnum() and (num := int(node.data)) >= 10:
                new_node0 = ListNode("[")
                new_node1 = ListNode(str(math.floor(num / 2)))
                new_node2 = ListNode(str(math.ceil(num / 2)))

                node.replace_with(new_node0)
                new_node1.insert_after(new_node0)
                new_node2.insert_after(new_node1)
                break

    def __add__(self, other: LinkedList) -> LinkedList:
        tokens = chain("[", self.iter_data(), other.iter_data())
        return LinkedList.from_tokens(tokens)

    @property
    def magnitude(self):
        tree = TreeNode.from_tokens(self.iter_data())
        return tree.magnitude

    @classmethod
    def from_tokens(cls, tokens: Iterator[str]) -> LinkedList:
        linked_list = LinkedList()
        for token in tokens:
            linked_list.append(ListNode(data=token))
        return linked_list

    @classmethod
    def from_line(cls, line: str) -> LinkedList:
        return cls.from_tokens(tokenize(line))

    def __str__(self):
        tree = TreeNode.from_tokens(self.iter_data())
        return str(tree)


class TreeNode:
    @classmethod
    def from_tokens(cls, tokens: Iterator[str]) -> TreeNode:
        for token in tokens:
            if token == "[":
                return Branch.from_tokens(tokens)
            else:
                return Leaf(int(token))
        raise ValueError("no tokens")

    @property
    def magnitude(self) -> int:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


class Leaf(TreeNode):
    def __init__(self, value: int) -> None:
        self.value = value

    @property
    def magnitude(self) -> int:
        return self.value

    def __str__(self) -> str:
        return str(self.value)


class Branch(TreeNode):
    def __init__(self, left: TreeNode, right: TreeNode) -> None:
        self.left = left
        self.right = right

    @classmethod
    def from_tokens(cls, tokens: Iterator[str]) -> Branch:
        left = TreeNode.from_tokens(tokens)
        right = TreeNode.from_tokens(tokens)
        return cls(left, right)

    @property
    def magnitude(self) -> int:
        return 3 * self.left.magnitude + 2 * self.right.magnitude

    def __str__(self) -> str:
        return f"[{self.left},{self.right}]"


def solve(task: str) -> int:
    nums = [LinkedList.from_tokens(line) for line in task.splitlines()]
    total = sum(nums)
    return total.magnitude
