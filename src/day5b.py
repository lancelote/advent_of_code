# coding=utf-8

"""
--- Part Two ---

Realizing the error of his ways, Santa has switched to a better model of
determining whether a string is naughty or nice. None of the old rules apply,
as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

    It contains a pair of any two letters that appears at least twice in the
    string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not
    like aaa (aa, but it overlaps).

    It contains at least one letter which repeats with exactly one letter
    between them, like xyx, abcdefeghi (efe), or even aaa.

For example:

    qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and
    a letter that repeats with exactly one letter between them (zxz).

    xxyxx is nice because it has a pair that appears twice and a letter that
    repeats with one between, even though the letters used by each rule
    overlap.

    uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with
    a single letter between them.

    ieodomkazucvgmuy is naughty because it has a repeating letter with one
    between (odo), but no pair that appears twice.

How many strings are nice under these new rules?
"""

import re

from src.day5a import process_data


def is_nice(word):
    """
    Check if string is nice

    Args:
        word: String to check

    Returns:
        bool: True if nice, False if naughty
    """
    pairs = len(re.findall(r'(..).*\1', word))
    guarded_letter = len(re.findall(r'(.).\1', word))
    return pairs >= 1 and guarded_letter >= 1


def solve(task):
    """
    Calculate number of nice strings

    Args:
        task (str): agagasdgsdg \n aasdfasgsdg \n ... (without spaces)

    Returns:
        int: Number of nice strings
    """
    data = process_data(task)
    return sum(is_nice(line) for line in data)
