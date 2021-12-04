from __future__ import annotations

from itertools import chain
from typing import Iterator


class Board:
    def __init__(self, nums: list[list[int]]) -> None:
        self.last_draw = 0
        self.nums = nums
        self.marked: set[int] = set()

    @classmethod
    def from_text(cls, text: str) -> Board:
        nums = []
        for line in text.strip().split("\n"):
            row = []
            for num in line.strip().split():
                row.append(int(num))
            nums.append(row)
        return cls(nums)

    def draw(self, num: int) -> None:
        self.last_draw = num
        self.marked.add(num)

    def has_marked_rows(self) -> bool:
        for row in self.nums:
            if all(num in self.marked for num in row):
                return True
        return False

    def has_marked_cols(self) -> bool:
        for i in range(len(self.nums[0])):
            if all(row[i] in self.marked for row in self.nums):
                return True
        return False

    @property
    def won(self) -> bool:
        return self.has_marked_cols() or self.has_marked_rows()

    @property
    def unmarked_nums(self) -> Iterator[int]:
        for num in chain.from_iterable(self.nums):
            if num not in self.marked:
                yield num

    @property
    def score(self) -> int:
        return self.last_draw * sum(self.unmarked_nums)


def solve(task: str) -> int:
    first_line, *other_chunks = task.strip().split("\n\n")

    nums = [int(x) for x in first_line.strip().split(",")]
    boards = [Board.from_text(chunk) for chunk in other_chunks]

    for num in nums:
        for board in boards:
            board.draw(num)
            if board.won:
                return board.score

    raise ValueError("no board won")
