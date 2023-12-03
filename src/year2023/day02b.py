"""2023 - Day 2 Part 2: Cube Conundrum"""
from src.year2023.day02a import process_data


def solve(task: str) -> int:
    count = 0
    games = process_data(task)

    for game in games:
        red = green = blue = 0

        for r in game.rounds:
            red = max(red, r.red)
            green = max(green, r.green)
            blue = max(blue, r.blue)

        power = red * green * blue
        count += power

    return count
