"""2021 - Day 4 Part 1: Giant Squid."""
from __future__ import annotations


class Board:
    def __init__(self, nums: list[list[int]]) -> None:
        self.nums = nums
        self.unmarked: set[int] = {x for row in nums for x in row}

    @classmethod
    def from_text(cls, text: str) -> Board:
        nums = []
        for line in text.strip().split("\n"):
            row = []
            for num in line.strip().split():
                row.append(int(num))
            nums.append(row)
        return cls(nums)

    def has_marked_rows(self) -> bool:
        for row in self.nums:
            if not any(num in self.unmarked for num in row):
                return True
        return False

    def has_marked_cols(self) -> bool:
        for i in range(len(self.nums[0])):
            if not any(row[i] in self.unmarked for row in self.nums):
                return True
        return False

    @property
    def won(self) -> bool:
        return self.has_marked_cols() or self.has_marked_rows()


def solve(task: str) -> int:
    first_line, *raw_boards = task.strip().split("\n\n")

    nums = [int(x) for x in first_line.strip().split(",")]
    boards = [Board.from_text(raw_board) for raw_board in raw_boards]

    for num in nums:
        for board in boards:
            board.unmarked.discard(num)
            if board.won:
                return num * sum(board.unmarked)

    raise ValueError("no board won")
