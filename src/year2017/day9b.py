"""2017 - Day 9 Part 2: Stream Processing.

Now, you're ready to remove the garbage.

To prove you've removed it, you need to count all of the characters within the
garbage. The leading and trailing < and > don't count, nor do any canceled
characters or the ! doing the canceling.

    <>, 0 characters.
    <random characters>, 17 characters.
    <<<<>, 3 characters.
    <{!>}>, 2 characters.
    <!!>, 0 characters.
    <!!!>>, 0 characters.
    <{o"i!a,<{i<a>, 10 characters.

How many non-canceled characters are within the garbage in your puzzle input?
"""


def solve(task: str) -> int:
    """Count total group score."""
    garbage_chars = 0
    garbage = False
    escape = False

    for token in task.strip():
        if escape:
            escape = False
        elif token == ">":
            garbage = False
        elif token == "!":
            escape = True
        elif garbage:
            garbage_chars += 1
        elif token == "{":
            pass
        elif token == "}":
            pass
        elif token == "<":
            garbage = True
    return garbage_chars
