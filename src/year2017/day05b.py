"""2017 - Day 5 Part 2: A Maze of Twisty Trampolines, All Alike."""


def solve(task: str) -> int:
    """Find number of steps required to jump out of maze."""
    current_index = 0
    steps = 0
    data = [int(item) for item in task.strip().split("\n")]

    while 0 <= current_index < len(data):
        offset = data[current_index]
        next_index = current_index + offset
        if offset >= 3:
            data[current_index] -= 1
        else:
            data[current_index] += 1
        current_index = next_index
        steps += 1
    return steps
