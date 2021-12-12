"""2021 - Day 4 Part 2: Giant Squid."""
from src.year2021.day04a import Board


def solve(task: str) -> int:
    first_line, *raw_boards = task.strip().split("\n\n")

    nums = [int(x) for x in first_line.strip().split(",")]
    boards = [Board.from_text(raw_board) for raw_board in raw_boards]

    for num in nums:
        next_round_boards = []

        for board in boards:
            board.unmarked.discard(num)

            did_win = board.won
            is_last_board = len(boards) == 1

            if is_last_board and did_win:
                return num * sum(board.unmarked)
            elif not did_win:
                next_round_boards.append(board)

        boards = next_round_boards

    raise ValueError("cannot find the single last winning board")
