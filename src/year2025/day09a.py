"""2025 - Day 9 Part 1: Movie Theater"""

type Tile = tuple[int, int]


def to_tile(line: str) -> Tile:
    a, b = line.split(",")
    return int(a), int(b)


def process_data(data: str) -> list[Tile]:
    return [to_tile(line) for line in data.splitlines()]


def get_area(a: Tile, b: Tile) -> int:
    x1, y1 = a
    x2, y2 = b

    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


def largest_rectangle_area(tiles: list[Tile]) -> int:
    max_area = 0

    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            a = tiles[i]
            b = tiles[j]
            area = get_area(a, b)
            max_area = max(max_area, area)

    return max_area


def solve(task: str) -> int:
    tiles = process_data(task)
    return largest_rectangle_area(tiles)
