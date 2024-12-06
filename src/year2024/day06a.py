"""2024 - Day 6 Part 1: Guard Gallivant"""

SHIFTS = {
    # r c
    "^": (-1, 0),
    ">": (0, +1),
    "v": (+1, 0),
    "<": (0, -1),
}

TURN = {
    "^": ">",
    ">": "v",
    "v": "<",
    "<": "^",
}


def find_guard(data: list[list[str]]) -> tuple[int, int]:
    rows = len(data)
    cols = len(data[0])

    for r in range(rows):
        for c in range(cols):
            if data[r][c] == "^":
                return r, c

    raise ValueError


def solve(task: str) -> int:
    data = [list(line) for line in task.split("\n")]

    gr, gc = find_guard(data)

    rows = len(data)
    cols = len(data[0])

    visited = {(gr, gc)}
    dr, dc = (-1, 0)
    guard = "^"

    while True:
        nr = gr + dr
        nc = gc + dc

        if not (0 <= nr < rows and 0 <= nc < cols):
            break  # out of border

        if data[nr][nc] != "#":
            gr = nr
            gc = nc
        else:
            guard = TURN[guard]
            dr, dc = SHIFTS[guard]

        visited.add((gr, gc))

    return len(visited)
