"""2024 - Day 11 Part 1: Plutonian Pebbles"""


def solve(task: str) -> int:
    stones = [int(x) for x in task.split()]

    for _ in range(25):
        new_stones: list[int] = []

        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif (len_stone := len(str_stone := str(stone))) % 2 == 0:
                middle = len_stone // 2

                left = str_stone[:middle]
                right = str_stone[middle:]

                new_stones.append(int(left))
                new_stones.append(int(right))
            else:
                new_stones.append(stone * 2024)

        stones = new_stones

    return len(stones)
