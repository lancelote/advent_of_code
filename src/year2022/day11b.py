"""2022 - Day 11 Part 2: Monkey in the Middle."""

from src.year2022.day11a import Game, Monkey


def solve(task: str) -> int:
    monkeys: dict[int, Monkey] = {}

    for text in task.split("\n\n"):
        monkey = Monkey.from_text(text)
        monkeys[monkey.id] = monkey

    game = Game(monkeys, reducer=1)
    for _ in range(10_000):
        game.round()

    inspect = [x.inspect for x in game.monkeys.values()]
    inspect.sort()
    return inspect[-1] * inspect[-2]
