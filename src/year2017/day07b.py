"""2017 - Day 7 Part 2: Recursive Circus."""
from src.year2017.day07a import process_data
from src.year2017.day07a import solve as find_root


def find_unique(children: list[int]) -> tuple[int, int]:
    """Find unique item and return difference from other items and index."""
    first, second = set(children)
    if children.count(first) == 1:
        common, unique = second, first
    else:
        common, unique = first, second
    return common - unique, children.index(unique)


def unbalanced(
    command: str, tree: dict[str, list[str]], weights: dict[str, int]
) -> tuple[bool, int]:
    """Recursively search for unbalanced node."""
    children_weights = []
    children = tree[command]

    for child in children:
        balance, weight = unbalanced(child, tree, weights)
        if balance:
            children_weights.append(weight)
        else:
            return False, weight

    if len(set(children_weights)) == 2:
        difference, unique_index = find_unique(children_weights)
        unbalanced_command = children[unique_index]
        return False, weights[unbalanced_command] + difference

    return True, sum(children_weights) + weights[command]


def solve(task: str) -> int:
    """Find correct weight of the wrong-weighted command."""
    data = process_data(task)
    tree: dict[str, list[str]] = {}
    weights: dict[str, int] = {}
    root = find_root(task)

    for parent, weight, children in data:
        weights[parent] = weight
        tree[parent] = children

    _, new_weight = unbalanced(root, tree, weights)
    return new_weight
