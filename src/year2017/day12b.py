"""2017 - Day 12 Part 2: Digital Plumber."""

from src.year2017.day12a import process_data, process_nodes


def solve(task: str) -> int:
    """Count number of connected components in graph."""
    connections = process_data(task)
    nodes = process_nodes(connections)
    return len({id(component) for component in nodes.values()})
