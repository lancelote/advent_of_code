"""2017 - Day 5 Part 2: A Maze of Twisty Trampolines, All Alike.

Now, the jumps are even stranger: after each jump, if the offset was three or
more, instead decrease it by 1. Otherwise, increase it by 1 as before.

Using this rule with the above example, the process now takes 10 steps, and
the offset values after finding the exit are left as 2 3 2 3 -1.

How many steps does it now take to reach the exit?
"""


def solve(task: str) -> int:
    """Find number of steps required to jump out of maze."""
    current_index = 0
    steps = 0
    data = [int(item) for item in task.strip().split('\n')]

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
