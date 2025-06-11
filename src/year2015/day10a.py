"""2015 - Day 10 Part 1: Elves Look, Elves Say."""


def iterate(state: list[int]) -> list[int]:
    new_state: list[int] = []

    idx = 0
    count = 1

    while idx < len(state):
        current = state[idx]

        while idx < len(state) - 1 and state[idx + 1] == state[idx]:
            count += 1
            idx += 1

        new_state.append(count)
        new_state.append(current)

        count = 1
        idx += 1

    return new_state


def solve(task: str) -> int:
    state = [int(x) for x in task]
    for _ in range(40):
        state = iterate(state)
    return len(state)
