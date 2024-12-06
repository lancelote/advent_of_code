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

    while True:
        guard = data[gr][gc]

        dr, dc = SHIFTS[guard]

        nr = gr + dr
        nc = gc + dc

        if not (0 <= nr < rows and 0 <= nc < cols):
            break  # out of border

        if data[nr][nc] != "#":
            data[nr][nc] = guard

            gr = nr
            gc = nc
        else:
            new_guard = TURN[guard]
            data[gr][gc] = new_guard

        visited.add((gr, gc))

    return len(visited)
