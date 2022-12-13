r"""2017 - Day 7 Part 1: Recursive Circus.

Wandering further through the circuits of the computer, you come upon a tower
of programs that have gotten themselves into a bit of trouble. A recursive
algorithm has gotten out of hand, and now they're balanced precariously in a
large tower.

One program at the bottom supports the entire tower. It's holding a large
disc, and on the disc are balanced several more sub-towers. At the bottom of
these sub-towers, standing on the bottom disc, are other programs, each
holding their own disc, and so on. At the very tops of these
sub-sub-sub-...-towers, many programs stand simply keeping the disc below
them balanced but with no disc of their own.

You offer to help, but first you need to understand the structure of these
towers. You ask each program to yell out their name, their weight, and (if
they're holding a disc) the names of the programs immediately above them
balancing on that disc. You write this information down (your puzzle input).
Unfortunately, in their panic, they don't do this in an orderly fashion; by
the time you're done, you're not sure which program gave which information.

For example, if your list is the following:

    pbga (66)
    xhth (57)
    ebii (61)
    havc (66)
    ktlj (57)
    fwft (72) -> ktlj, cntj, xhth
    qoyq (66)
    padx (45) -> pbga, havc, qoyq
    tknk (41) -> ugml, padx, fwft
    jptl (61)
    ugml (68) -> gyxo, ebii, jptl
    gyxo (61)
    cntj (57)

...then you would be able to recreate the structure of the towers that looks
like this:

                    gyxo
                  /
             ugml - ebii
           /      \
          |         jptl
          |
          |         pbga
         /        /
    tknk --- padx - havc
         \        \
          |         qoyq
          |
          |         ktlj
           \      /
             fwft - cntj
                  \
                    xhth

In this example, "tknk" is at the bottom of the tower (the bottom program), and
is holding up ugml, padx, and fwft. Those programs are, in turn, holding up
other programs; in this example, none of those programs are holding up any
other programs, and are all the tops of their own towers. (The actual tower
balancing in front of you is much larger.)

Before you're ready to help them, you need to make sure your information is
correct. What is the name of the bottom program?
"""
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
