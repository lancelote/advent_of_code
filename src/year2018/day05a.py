"""2018 - Day 5 Part 1: Alchemical Reduction."""


def react(char1: str, char2: str) -> bool:
    """Check if pair reacts."""
    return char1 != char2 and char1.lower() == char2.lower()


def solve(task: str) -> int:
    """Reduce polymer and count left unites."""
    left: list[str] = []
    for char in task.strip():
        if not left:
            left.append(char)
        else:
            if react(left[-1], char):
                left.pop()
            else:
                left.append(char)
    return len(left)
