"""2021 - Day 12 Part 1: Passage Pathing."""


class Cave:
    def __init__(self, name: str) -> None:
        self.name = name
        self.adjacent: list[Cave] = []

    @property
    def is_small(self) -> bool:
        return self.name.islower()

    def __str__(self) -> str:
        return f"Cave({self.name})"

    __repr__ = __str__


def parse_task(task: str) -> dict[str, Cave]:
    caves: dict[str, Cave] = {}

    for line in task.splitlines():
        from_name, to_name = line.split("-")

        from_cave = caves.get(from_name, Cave(from_name))
        to_cave = caves.get(to_name, Cave(to_name))

        from_cave.adjacent.append(to_cave)
        to_cave.adjacent.append(from_cave)

        caves[from_name] = from_cave
        caves[to_name] = to_cave

    return caves


def solve(task: str) -> int:
    caves = parse_task(task)
    unique_paths = 0

    def visit(cave: Cave, visited: set) -> None:
        nonlocal unique_paths

        if cave.name == "end":
            unique_paths += 1
            return

        visited.add(cave.name)
        for neighbor in cave.adjacent:
            if not (neighbor.is_small and neighbor.name in visited):
                visit(neighbor, visited=visited)

        visited.discard(cave.name)

    visit(caves["start"], visited=set())
    return unique_paths
