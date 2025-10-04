"""2024 - Day 9 Part 1: Disk Fragmenter"""

from collections import deque
from collections.abc import Generator


def make_generator(files: deque[int]) -> Generator[int]:
    pop_id = len(files) - 1

    def generator() -> Generator[int]:
        nonlocal pop_id

        while True:
            try:
                length = files.pop()
            except IndexError:
                return None

            for _ in range(length):
                yield pop_id

            pop_id -= 1

    return generator()


def solve(task: str) -> int:
    files: deque[int] = deque()
    spaces: deque[int] = deque()

    for i in range(0, len(task), 2):
        files.append(int(task[i]))
        if i + 1 < len(task):
            spaces.append(int(task[i + 1]))

    generator = make_generator(files)
    result: list[int] = []

    i = 0
    while spaces:
        try:
            file = files.popleft()
        except IndexError:
            break

        for _ in range(file):
            result.append(i)

        i += 1

        space = spaces.popleft()
        for _ in range(space):
            try:
                result.append(next(generator))
            except IndexError:
                break

    for x in generator:
        result.append(x)

    return sum(i * x for i, x in enumerate(result))
