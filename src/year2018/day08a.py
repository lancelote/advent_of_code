"""2018 - Day 8 Part 1: Memory Maneuver."""
from dataclasses import dataclass


@dataclass
class Node:
    """Has a list of child-nodes and a metadata as a list of ints."""

    children: list["Node"]
    metadata: list[int]


def parse_tree(data: list[int], start: int = 0) -> tuple[Node, int]:
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
