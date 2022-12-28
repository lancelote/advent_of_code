"""2016 - Day 3 Part 1: Squares With Three Sides."""


def process_data(data: str) -> list[tuple[int, int, int]]:
    """Parse the raw data.

    Convert raw triangle data:

        1 2 3
        4 5 6

    Into list of tuples, where each item is a triangle with a, b, c sides
    """
    triangles = []
    for triangle in data.strip().split("\n"):
        a, b, c = triangle.split()
        triangles.append((int(a), int(b), int(c)))
    return triangles


def is_bad(triangle: tuple[int, int, int]) -> bool:
    """Check if there can exist such triangle."""
    longest = max(triangle)
    return sum(triangle) - longest <= longest


def count_possible(triangles: list[tuple[int, int, int]]) -> int:
    """Calculate the number of possible triangles."""
    possible = 0
    for triangle in triangles:
        if not is_bad(triangle):
            possible += 1
    return possible


def solve(task: str) -> int:
    """Solve the puzzle."""
    triangles = process_data(task)
    return count_possible(triangles)
