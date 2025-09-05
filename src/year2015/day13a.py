"""2015 - Day 13 Part 1: Knights of the Dinner Table."""

import re

type Preference = dict[tuple[str, str], int]


def process_data(task: str) -> Preference:
    result: Preference = {}
    pattern = (
        r"^(\w+) would (lose|gain) (\d+) happiness units"
        r" by sitting next to (\w+)\.$"
    )

    for line in task.splitlines():
        match = re.match(pattern, line)
        assert match is not None

        name1, sign, num_str, name2 = match.groups()
        result[(name1, name2)] = -int(num_str) if sign == "lose" else int(num_str)

    return result


def count_happiness(seating: list[str], preference: Preference) -> int:
    n = len(seating)
    happiness = 0

    for i, name in enumerate(seating):
        happiness += preference.get((name, seating[i - 1]), 0)
        happiness += preference.get((name, seating[(i + 1) % n]), 0)

    return happiness


def solve(task: str) -> int:
    preference = process_data(task)
    names = {x[0] for x in preference.keys()}

    seating: list[str] = []
    happiness = 0

    def dfs(name: str) -> None:
        nonlocal happiness

        seating.append(name)

        if len(names) == 0:
            happiness = max(happiness, count_happiness(seating, preference))
        else:
            for next_name in names:
                names.remove(next_name)
                dfs(next_name)
                names.add(next_name)

        _ = seating.pop()

    dfs(names.pop())
    return happiness
