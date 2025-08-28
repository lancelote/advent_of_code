"""2024 - Day 16 Part 2: Reindeer Maze"""

from src.year2024.day16a import SHIFTS, TO_LEFT, TO_RIGHT, Direction


def solve(task: str) -> int:
    data = [list(line) for line in task.split("\n")]

    rows = len(data)
    cols = len(data[0])

    start_r, start_c = rows - 2, 1
    end_r, end_c = 1, cols - 2

    start_score = 1

    best_score: dict[tuple[int, int], int] = {}
    result_path_unique_nodes: set[tuple[int, int]] = set()

    best_score[(start_r, start_c)] = start_score
    backtrack: set[tuple[int, int]] = set()

    def dfs(r: int, c: int, score: int, direction: Direction) -> None:
        if not (0 <= r < rows and 0 <= c < cols):
            return

        if r == end_r and c == end_c:
            raise NotImplementedError

        if (r, c) in backtrack:
            return

        if data[r][c] == "#":
            return

        if (r, c) in best_score:
            old_score = best_score[(r, c)]
            if old_score < score:
                return

        if score >= best_score[(end_r, end_c)]:
            return

        best_score[(r, c)] = score
        backtrack.add((r, c))

        dr, dc = SHIFTS[direction]
        dfs(r + dr, c + dc, score + 1, direction)
        dfs(r, c, score + 1000, TO_LEFT[direction])
        dfs(r, c, score + 1000, TO_RIGHT[direction])

        backtrack.remove((r, c))

    dfs(start_r, start_c, start_score, Direction.EAST)
    return len(result_path_unique_nodes)
