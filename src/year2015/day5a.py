# coding=utf-8

"""Day 5: Doesn't He Have Intern-Elves For This.

Santa needs help figuring out which strings in his text file are naughty or
nice.

A nice string is one with all of the following properties:

    It contains at least three vowels (aeiou only), like aei, xazegov, or
    aeiouaeiouaeiou.

    It contains at least one letter that appears twice in a row, like xx,
    abcdde (dd), or aabbccdd (aa, bb, cc, or dd).

    It does not contain the strings ab, cd, pq, or xy, even if they are part
    of one of the other requirements.

For example:

    ugknbfddgicrmopn is nice because it has at least three vowels
    (u...i...o...), a double letter (...dd...), and none of the disallowed
    substrings.

    aaa is nice because it has at least three vowels and a double letter,
    even though the letters used by different rules overlap.

    jchzalrnumimnmhp is naughty because it has no double letter.

    haegwjzuvuyypxyu is naughty because it contains the string xy.

    dvszwmarrgswjxmb is naughty because it contains only one vowel.

How many strings are nice?
"""

import re


def process_data(task):
    r"""Process data into list.

    Args:
        task (str): agagasdgsdg \n aasdfasgsdg \n ... (without spaces)

    Returns:
        list: ['agagasdgsdg', 'aasdfasgsdg', ...]

    """
    data = task.strip().split("\n")
    return data


def is_nice(word):
    """Check if string is nice.

    Args:
        word: String to check

    Returns:
        bool: True if nice, False if naughty

    """
    vowels = len(re.findall(r"[aeiou]", word))
    pairs = len(re.findall(r"(.)\1", word))
    banned = len(re.findall(r"ab|cd|pq|xy", word))
    return vowels > 2 and pairs > 0 and banned == 0


def solve(task):
    r"""Calculate number of nice strings.

    Args:
        task (str): agagasdgsdg \n aasdfasgsdg \n ... (without spaces)

    Returns:
        int: Number of nice strings

    """
    data = process_data(task)
    return sum(is_nice(line) for line in data)
