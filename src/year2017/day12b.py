"""2017 - Day 12 Part 2: Digital Plumber.

There are more programs than just the ones in the group containing program
ID 0. The rest of them have no way of reaching that group, and still might
have no way of reaching each other.

A group is a collection of programs that can all communicate via pipes either
directly or indirectly. The programs you identified just a moment ago are all
part of the same group. Now, they would like you to determine the total number
of groups.

In the example above, there were 2 groups: one consisting of programs
0, 2, 3, 4, 5, 6, and the other consisting solely of program 1.

How many groups are there in total?
"""

from src.year2017.day12a import process_data, process_nodes


def solve(task: str) -> int:
    """Count number of connected components in graph."""
    connections = process_data(task)
    nodes = process_nodes(connections)
    return len(set(id(component) for component in nodes.values()))
