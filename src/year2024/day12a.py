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
    def __init__(self, key: str, perimeter: int = 0) -> None:
        self.key = key
        self.perimeter = perimeter
        self.points: set[tuple[int, int]] = set()

    @classmethod
    def from_point(
        cls, sr: int, sc: int, data: list[str], seen: set[tuple[int, int]]
    ) -> Region:
        rows = len(data)
        cols = len(data[0])

        region = Region(key=data[sr][sc])
        to_process = [(sr, sc)]
        region.points.add((sr, sc))

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
                    region.points.add((nr, nc))
                    to_process.append((nr, nc))
                    seen.add((nr, nc))

        return region

    @property
    def price(self) -> int:
        return self.area * self.perimeter

    @property
    def price_with_discount(self) -> int:
        return self.area * self.sides

    @property
    def area(self) -> int:
        return len(self.points)

    @property
    def sides(self) -> int:
        # we count region points which are corners
        count = 0

        for r, c in self.points:
            for x, y, z in (
                ((r, c - 1), (r - 1, c - 1), (r - 1, c)),
                ((r - 1, c), (r - 1, c + 1), (r, c + 1)),
                ((r, c + 1), (r + 1, c + 1), (r + 1, c)),
                ((r, c - 1), (r + 1, c - 1), (r + 1, c)),
            ):
                if x in self.points and y not in self.points and z in self.points:
                    count += 1
                if (
                    x not in self.points
                    and y not in self.points
                    and z not in self.points
                ):
                    count += 1
                if x not in self.points and y in self.points and z not in self.points:
                    count += 1
        return count

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
