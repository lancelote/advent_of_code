r"""2017 - Day 7 Part 1: Recursive Circus."""

import re

PATTERN = r"(?P<parent>\w+) \((?P<weight>\d+)\)( -> (?P<children>[\w, ]+))?"


def process_line(line: str) -> tuple[str, int, list[str]]:
    """Convert raw line to a manageable view.

    Returns a tuple of:
        - Command name itself.
        - Its integer weight.
        - The list of dependent command names.
    """
    match = re.match(PATTERN, line)
    if not match:
        raise ValueError("Wrong command format")
    parent = match.group("parent")
    weight = int(match.group("weight"))
    children = match.group("children")
    return parent, weight, children.split(", ") if children else []


def process_data(data: str) -> list[tuple[str, int, list[str]]]:
    """Convert raw string data into a manageable view.

    Returns a list where each item is a parsed answer from each command. See
    process_line docstring for details per line.
    """
    lines = data.strip().split("\n")
    return [process_line(line.strip()) for line in lines]


def find_root(tree: dict[str, str | None]) -> str | None:
    """Find tree root."""
    root = None
    for child, parent in tree.items():
        if parent is None:
            root = child
            break
    return root


def solve(task: str) -> str:
    """Find base command."""
    tree: dict[str, str | None] = {}
    data = process_data(task)
    for parent, _, children in data:
        if parent not in tree:
            tree[parent] = None
        for child in children:
            tree[child] = parent
    root = find_root(tree)
    if not root:
        raise ValueError("Impossible to find a base command.")
    return root
