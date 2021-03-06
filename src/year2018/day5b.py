"""2018 - Day 5 Part 2: Alchemical Reduction.

Time to improve the polymer.

One of the unit types is causing problems; it's preventing the polymer from
collapsing as much as it should. Your goal is to figure out which unit type is
causing the most problems, remove all instances of it (regardless of polarity),
fully react the remaining polymer, and measure its length.

For example, again using the polymer dabAcCaCBAcCcaDA from above:

    Removing all A/a units produces dbcCCBcCcD. Fully reacting this polymer
      produces dbCBcD, which has length 6.
    Removing all B/b units produces daAcCaCAcCcaDA. Fully reacting this polymer
      produces daCAcaDA, which has length 8.
    Removing all C/c units produces dabAaBAaDA. Fully reacting this polymer
      produces daDA, which has length 4.
    Removing all D/d units produces abAcCaCBAcCcaA. Fully reacting this polymer
      produces abCBAc, which has length 6.

In this example, removing all C/c units was best, producing the answer 4.

What is the length of the shortest polymer you can produce by removing all
units of exactly one type and fully reacting the result?
"""
import re
import string

from src.year2018.day5a import solve as length


def solve(task: str) -> int:
    """Find the shortest polymer for each possible reduction."""
    results = []
    polymer = task.strip()

    for char in string.ascii_lowercase:
        pattern = f"{char}|{char.upper()}"
        results.append(length(re.sub(pattern, "", polymer)))

    return min(results)
