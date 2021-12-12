"""2016 - Day 6 Part 1: Signals and Noise.

Something is jamming your communications with Santa. Fortunately, your signal
is only partially jammed, and protocol in situations like this is to switch
to a simple repetition code to get the message through.

In this model, the same message is sent repeatedly. You've recorded the
repeating message signal (your puzzle input), but the data seems quite
corrupted - almost too badly to recover. Almost.

All you need to do is figure out which character is most frequent for each
position. For example, suppose you had recorded the following messages:

    eedadn
    drvtee
    eandsr
    raavrd
    atevrs
    tsrnev
    sdttsa
    rasrtv
    nssdts
    ntnada
    svetve
    tesnvt
    vntsnd
    vrdear
    dvrsen
    enarar

The most common character in the first column is e; in the second, a; in the
third, s, and so on. Combining these characters returns the error-corrected
message, easter.

Given the recording in your puzzle input, what is the error-corrected version
of the message being sent?
"""
from collections import Counter
from typing import List
from typing import Tuple


def process_data(data: str) -> List[Tuple[str, ...]]:
    """Convert raw data into the list of tuples.

    Each tuple corresponds to one character.
    """
    lines = data.strip().split("\n")
    return list(zip(*lines))


def solve(task: str) -> str:
    """Filter errors from the message."""
    message = ""
    for char in process_data(task):
        message += Counter(char).most_common(1)[0][0]
    return message
