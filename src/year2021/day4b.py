from src.year2021.day4a import Board


def solve(task: str) -> int:
    first_line, *other_chunks = task.strip().split("\n\n")

    nums = [int(x) for x in first_line.strip().split(",")]
    boards = [Board.from_text(chunk) for chunk in other_chunks]

    i = 0

    for i in range(len(nums)):
        new_boards = []

        for board in boards:
            board.draw(nums[i])
            if not board.won:
                new_boards.append(board)

        boards = new_boards
        if len(boards) == 1:
            break

    the_board = boards[0]
    for j in range(i + 1, len(nums)):
        the_board.draw(nums[j])
        if the_board.won:
            return the_board.score

    raise ValueError("cannot find the last winning board")
