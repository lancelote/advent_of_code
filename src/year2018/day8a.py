"""2018 - Day 8 Part 1: Memory Maneuver.

The sleigh is much easier to pull than you'd expect for something its weight.
Unfortunately, neither you nor the Elves know which way the North Pole is from
here.

You check your wrist device for anything that might help. It seems to have some
kind of navigation system! Activating the navigation system produces more bad
news: "Failed to start navigation system. Could not read software license
file."

The navigation system's license file consists of a list of numbers (your puzzle
input). The numbers define a data structure which, when processed, produces
some kind of tree that can be used to calculate the license number.

The tree is made up of nodes; a single, outermost node forms the tree's root,
and it contains all other nodes in the tree (or contains nodes that contain
nodes, and so on).

Specifically, a node consists of:

    A header, which is always exactly two numbers:
        The quantity of child nodes.
        The quantity of metadata entries.
    Zero or more child nodes (as specified in the header).
    One or more metadata entries (as specified in the header).

Each child node is itself a node that has its own header, child nodes, and
metadata. For example:

2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
A----------------------------------
    B----------- C-----------
                     D-----

In this example, each node of the tree is also marked with an underline
starting with a letter for easier identification. In it, there are four nodes:

    A, which has 2 child nodes (B, C) and 3 metadata entries (1, 1, 2).
    B, which has 0 child nodes and 3 metadata entries (10, 11, 12).
    C, which has 1 child node (D) and 1 metadata entry (2).
    D, which has 0 child nodes and 1 metadata entry (99).

The first check done on the license file is to simply add up all of the
metadata entries. In this example, that sum is 1+1+2+10+11+12+2+99=138.

What is the sum of all metadata entries?
"""

from typing import List, Tuple
from dataclasses import dataclass


@dataclass
class Node:
    """Has a list of child-nodes and a metadata as a list of ints."""

    children: List["Node"]
    metadata: List[int]


def parse_tree(data: List[int], start=0) -> Tuple[Node, int]:
    """Parse a data into a tree of nodes."""
    children_num = data[start]
    metadata_len = data[start + 1]

    if children_num == 0:
        end = start + 2 + metadata_len
        metadata = data[start + 2 : end]
        return Node(children=[], metadata=metadata), end

    else:
        start += 2
        end = start
        children = []
        for _ in range(children_num):
            child, end = parse_tree(data, end)
            children.append(child)
        return (
            Node(children, data[end : end + metadata_len]),
            end + metadata_len,
        )


def sum_metadata(node: Node) -> int:
    """Sum metadata of all nodes in tree."""
    current_sum = sum(node.metadata)
    if not node.children:
        return current_sum
    else:
        children_sum = sum(sum_metadata(child) for child in node.children)
        return children_sum + current_sum


def solve(task: str) -> int:
    """Sum all nodes metadata."""
    data = [int(num) for num in task.strip().split()]
    tree, _ = parse_tree(data)
    return sum_metadata(tree)
