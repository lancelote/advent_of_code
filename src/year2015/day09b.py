"""2015 - Day 9 Part 2: All in a Single Night."""

from src.year2015.day09a import Data
from src.year2015.day09a import process_data


def find_longest(data: Data) -> int:
    unique_cities = len(set(data.keys()))
    longest = 0
    path: set[str] = set()

    def dfs(city: str, so_far: int = 0) -> None:
        nonlocal longest

        if city in path:
            return

        if city not in data:
            return

        if len(path) == unique_cities - 1:
            longest = max(longest, so_far)
            return

        path.add(city)
        for next_city, distance in data[city]:
            dfs(next_city, so_far + distance)
        path.remove(city)

    for k in data.keys():
        dfs(k)

    return longest


def solve(task: str) -> int:
    data = process_data(task)
    return find_longest(data)
