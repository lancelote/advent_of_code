"""2018 - Day 8 Part 2: Memory Maneuver."""

from src.year2018.day08a import Node
from src.year2018.day08a import parse_tree


def get_node_value(node: Node) -> int:
    """Sum node value.

    If no children:
        sum of metadata
    If children:
        sum value of children with ids from metadata
    """
    if not node.children:
        return sum(node.metadata)
    else:
        current = 0
        for child_id in node.metadata:
            try:
                child = node.children[child_id - 1]  # 1-based
                current += get_node_value(child)
            except IndexError:
                pass  # No such child
        return current


def solve(task: str) -> int:
    """Find root value."""
    data = [int(num) for num in task.strip().split()]
    tree, _ = parse_tree(data)
    return get_node_value(tree)
