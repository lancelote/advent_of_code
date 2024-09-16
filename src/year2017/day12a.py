"""2017 - Day 12 Part 1: Digital Plumber."""

import re
from collections import defaultdict
from typing import DefaultDict


def process_data(data: str) -> list[list[str]]:
    """Convert each line of data into list of ints where first is parent."""
    return [re.findall(r"\d+", line) for line in data.strip().split("\n")]


def process_nodes(connections: list[list[str]]) -> DefaultDict[str, set[str]]:
    """Assign a corresponding component to each node."""
    nodes: DefaultDict[str, set[str]] = defaultdict(set)
    for parent, *children in connections:
        for child in children:
            component = nodes[parent] | nodes[child] | {parent, child}
            for node in component:
                nodes[node] = component
    return nodes


def solve(task: str) -> int:
    """Find the biggest connected component in graph."""
    connections = process_data(task)
    nodes = process_nodes(connections)
    return len(nodes["0"])
