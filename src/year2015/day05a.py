"""2015 - Day 5 Part 1: Doesn't He Have Intern-Elves For This."""
import re


def process_data(task: str) -> list[str]:
    r"""Process data into list.

    Args:
        task (str): agagasdgsdg \n aasdfasgsdg \n ... (without spaces)

    Returns:
        list: ['agagasdgsdg', 'aasdfasgsdg', ...]

    """
    data = task.strip().split("\n")
    return data


def is_nice(word: str) -> bool:
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


def solve(task: str) -> int:
    r"""Calculate number of nice strings.

    Args:
        task (str): agagasdgsdg \n aasdfasgsdg \n ... (without spaces)

    Returns:
        int: Number of nice strings

    """
    data = process_data(task)
    return sum(is_nice(line) for line in data)
