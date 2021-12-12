"""2021 - Day 2 Part 1: Dive!"""


def solve(task: str) -> int:
    x = 0
    y = 0

    for input_line in task.strip().split("\n"):
        direction, change = input_line.split(" ")
        value = int(change)

        if direction == "forward":
            x += value
        elif direction == "down":
            y += value
        elif direction == "up":
            y -= value
        else:
            raise ValueError(f"unknown direction {direction}")

    return x * y
