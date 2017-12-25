"""2017 - Day 7 Part 2: Recursive Circus.

The programs explain the situation: they can't get down. Rather, they could
get down, if they weren't expending all of their energy trying to keep the
tower balanced. Apparently, one program has the wrong weight, and until it's
fixed, they're stuck here.

For any program holding a disc, each program standing on that disc forms a
sub-tower. Each of those sub-towers are supposed to be the same weight,
or the disc itself isn't balanced. The weight of a tower is the sum of the
weights of the programs in that tower.

In the example above, this means that for ugml's disc to be balanced, gyxo,
ebii, and jptl must all have the same weight, and they do: 61.

However, for tknk to be balanced, each of the programs standing on its disc
and all programs above it must each match. This means that the following sums
must all be the same:

    ugml + (gyxo + ebii + jptl) = 68 + (61 + 61 + 61) = 251
    padx + (pbga + havc + qoyq) = 45 + (66 + 66 + 66) = 243
    fwft + (ktlj + cntj + xhth) = 72 + (57 + 57 + 57) = 243

As you can see, tknk's disc is unbalanced: ugml's stack is heavier than the
other two. Even though the nodes above ugml are balanced, ugml itself is too
heavy: it needs to be 8 units lighter for its stack to weigh 243 and keep the 
towers balanced. If this change were made, its weight would be 60.

Given that exactly one program is the wrong weight, what would its weight
need to be to balance the entire tower?
"""

from typing import Dict, List, Tuple

from src.year2017.day7a import process_data
from src.year2017.day7a import solve as find_root


def weight_difference(children: List[int]) -> Tuple[int, int]:
    first, second = set(children)
    if children.count(first) == 1:
        base, unique = second, first
    else:
        base, unique = first, second
    return base, unique


def unbalanced(command: str,
               tree: Dict[str, List[str]],
               weights: Dict[str, int]) -> Tuple[bool, int]:
    children = []
    for child in tree[command]:
        balance, weight = unbalanced(child, tree, weights)
        if balance:
            children.append(weight)
        else:
            return False, weight
    if len(set(children)) == 2:
        base, unique = weight_difference(children)
        unique_command = tree[command][children.index(unique)]
        return False, weights[unique_command] + base - unique
    return True, sum(children) + weights[command]


def solve(task: str) -> int:
    """Find correct weight of the wrong-weighted command."""
    data = process_data(task)
    tree: Dict[str, List[str]] = {}
    weights: Dict[str, int] = {}
    root = find_root(task)

    for parent, weight, children in data:
        weights[parent] = weight
        tree[parent] = children

    _, weight = unbalanced(root, tree, weights)
    return weight
