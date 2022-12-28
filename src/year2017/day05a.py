"""2017 - Day 5 Part 1: A Maze of Twisty Trampolines, All Alike."""


def solve(task: str) -> int:
    """Find number of steps required to jump out of maze."""
    current_index = 0
    steps = 0
    data = [int(item) for item in task.strip().split("\n")]

    while 0 <= current_index < len(data):
        next_index = current_index + data[current_index]
        data[current_index] += 1
        current_index = next_index
        steps += 1
    return steps
