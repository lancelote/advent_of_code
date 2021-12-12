"""2021 - Day 2 Part 2: Dive!"""


def solve(task: str) -> int:
    x = 0
    y = 0
    aim = 0

    for input_line in task.strip().split("\n"):
        direction, change = input_line.split(" ")
        value = int(change)

        if direction == "forward":
            x += value
            y += value * aim
        elif direction == "down":
            aim += value
        elif direction == "up":
            aim -= value
        else:
            raise ValueError(f"unknown direction {direction}")

    return x * y
