"""2015 - Day 19 Part 1: Medicine for Rudolph."""


def tokenize(data: str) -> list[str]:
    result: list[str] = []
    stack: list[str] = []

    for x in data:
        if x.isupper() and stack:
            result.append("".join(stack))
            stack.clear()
        stack.append(x)

    if stack:
        result.append("".join(stack))

    return result


def process_data(data: str) -> tuple[dict[str, list[str]], list[str]]:
    left, right = data.split("\n\n")
    replacements: dict[str, list[str]] = {}

    for line in left.splitlines():
        from_part, to_part = line.split(" => ")
        if from_part in replacements:
            replacements[from_part].append(to_part)
        else:
            replacements[from_part] = [to_part]

    initial = tokenize(right)
    return replacements, initial


def count_mutations(replacements: dict[str, list[str]], initial: list[str]) -> int:
    options: set[str] = set()

    for i, token in enumerate(initial):
        if token in replacements:
            for replacement in replacements[token]:
                left = "".join(initial[:i])
                right = "".join(initial[i + 1 :])
                mutation = f"{left}{replacement}{right}"
                options.add(mutation)

    return len(options)


def solve(task: str) -> int:
    replacements, initial = process_data(task)
    return count_mutations(replacements, initial)
