"""2024 - Day 2 Part 2:"""


def is_safe(level: list[int]) -> bool:
    n = len(level)
    tolerate = -1

    def is_increasing(level: list[int]) -> bool:
        nonlocal tolerate

        i = 0
        while i < n - 1:
            if level[i] > level[i + 1]:
                if tolerate == -1 or tolerate == i:
                    tolerate = 1
                else:
                    return False
            i += 1
        return True

    def is_decreasing(level: list[int]) -> bool:
        nonlocal tolerate

        i = 0
        while i < n - 1:
            if level[i] < level[i + 1]:
                if tolerate == -1 or tolerate == i:
                    tolerate = i
                else:
                    return False
            i += 1
        return True

    def ok_diff(level: list[int]) -> bool:
        nonlocal tolerate

        i = 0
        while i < n - 1:
            diff = abs(level[i] - level[i + 1])

            if diff < 1 or diff > 3:
                if tolerate == -1 or tolerate == i + 1:
                    if i < (n - 2):
                        diff = abs(level[i] - level[i + 2])
                        if diff < 1 or diff > 3:
                            return False
                        else:
                            tolerate = i
                            i += 1
                    else:
                        return True
                elif tolerate == i:
                    pass
                else:
                    return False
            i += 1
        return True

    if is_increasing(level) and ok_diff(level):
        return True

    tolerate = -1

    if is_decreasing(level) and ok_diff(level):
        return True

    return False


def solve(task: str) -> int:
    lines = task.split("\n")
    levels = [[int(x) for x in line.split()] for line in lines]
    return sum(is_safe(level) for level in levels)
