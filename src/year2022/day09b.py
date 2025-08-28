"""2022 - Day 9 Part 2: Rope Bridge."""

from src.year2022.day09a import SHIFT, Step, process_data, update_tail


def count_tail_positions(steps: list[Step]) -> int:
    rope = [(0, 0)] * 10
    visited = {rope[-1]}

    for step in steps:
        dr, dc = SHIFT[step.direction]

        for _ in range(step.length):
            r, c = rope[0]
            rope[0] = (r + dr, c + dc)

            for i in range(1, 10):
                rope[i] = update_tail(rope[i - 1], rope[i])
            visited.add(rope[-1])

    return len(visited)


def solve(task: str) -> int:
    steps = process_data(task)
    return count_tail_positions(steps)
