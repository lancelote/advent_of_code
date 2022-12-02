"""2015 - Day 4 Part 1: The Ideal Stocking Stuffer."""
from hashlib import md5


def solve(task: str, zeros: int = 5) -> int:
    """Solve the puzzle.

    Args:
        zeros (int): number of zeros to find
        task (str): key to encode

    Returns:
        int: Biggest number
    """
    i = 0
    message_hash = ""
    while not message_hash.startswith("0" * zeros):
        message = task + str(i)
        message_hash = md5(message.encode()).hexdigest()
        i += 1
    return i - 1
