"""2024 - Day 12 Part 1: Garden Groups"""

from __future__ import annotations

SHIFTS = (
    # r c
    (-1, 0),  # up
    (0, +1),  # right
    (+1, 0),  # down
    (0, -1),  # left
)


class Region:
    def __init__(self, key: str, area: int = 1, perimeter: int = 0) -> None:
        self.key = key
        self.area = area
        self.perimeter = perimeter

    @classmethod
    def from_point(
        cls, sr: int, sc: int, data: list[str], seen: set[tuple[int, int]]
    ) -> Region:
        rows = len(data)
        cols = len(data[0])

        region = Region(key=data[sr][sc])
        to_process = [(sr, sc)]

        while to_process:
            r, c = to_process.pop()

            for dr, dc in SHIFTS:
                nr = r + dr
                nc = c + dc

                if not (0 <= nr < rows and 0 <= nc < cols):
                    region.perimeter += 1
                elif data[nr][nc] != region.key:
                    region.perimeter += 1
                elif (nr, nc) not in seen:
                    region.area += 1
                    to_process.append((nr, nc))
                    seen.add((nr, nc))

        return region

    @property
    def price(self) -> int:
        return self.area * self.perimeter

    def __str__(self) -> str:
        return f"Region(key='{self.key}')"


def parse_regions(data: list[str]) -> list[Region]:
    rows = len(data)
    cols = len(data[0])

    seen: set[tuple[int, int]] = set()
    regions: list[Region] = []

    for r in range(rows):
        for c in range(cols):
            if (r, c) not in seen:
                seen.add((r, c))
                region = Region.from_point(r, c, data, seen)
                regions.append(region)

    return regions


def solve(task: str) -> int:
    data = task.split("\n")
    regions = parse_regions(data)
    return sum(x.price for x in regions)
