"""2022 - Day 11 Part 1: Monkey in the Middle."""
from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from dataclasses import field


def add(a: int, b: int) -> int:
    return a + b


def mul(a: int, b: int) -> int:
    return a * b


OPS = {
    "+": add,
    "*": mul,
}

# if left == right == "old":
#     op = lambda x: OPS[op_str](x, x)
# else:
#     op = lambda x: OPS[op_str](x, int(right))


@dataclass
class Game:
    monkeys: dict[int, Monkey] = field(default_factory=dict)

    def round(self) -> None:
        for monkey in self.monkeys.values():
            monkey.round(self)


@dataclass
class Monkey:
    id: int
    op: Callable[[int], int]
    test_value: int
    true_monkey: int
    false_monkey: int
    items: list[int] = field(default_factory=list)
    inspect: int = 0

    @classmethod
    def from_text(cls, text: str) -> Monkey:
        lines = text.splitlines()

        monkey_id_str = lines[0][7]
        monkey_id = int(monkey_id_str)

        _, items_raw = lines[1].split(": ")
        items_str = items_raw.split(", ")
        items = [int(x) for x in items_str]

        _, operation_raw = lines[2].split(" = ")
        left, op_str, right = operation_raw.split(" ")
        if left == right == "old":

            def op(x: int) -> int:
                return OPS[op_str](x, x)

        else:

            def op(x: int) -> int:
                return OPS[op_str](x, int(right))

        *_, test_value_str = lines[3].strip().split(" ")
        test_value = int(test_value_str)

        *_, true_monkey_str = lines[4].strip().split(" ")
        true_money = int(true_monkey_str)

        *_, false_monkey_str = lines[5].strip().split(" ")
        false_monkey = int(false_monkey_str)

        return Monkey(
            monkey_id, op, test_value, true_money, false_monkey, items
        )

    def test(self, value: int) -> bool:
        return value % self.test_value == 0

    def toss(self, value: int, game: Game) -> None:
        if self.test(value):
            game.monkeys[self.true_monkey].append(value)
        else:
            game.monkeys[self.false_monkey].append(value)

    def append(self, value: int) -> None:
        self.items.append(value)

    def worry(self, value: int) -> int:
        return self.op(value)

    def round(self, game: Game) -> None:
        while self.items:
            self.inspect += 1
            value = self.items.pop()
            value = self.worry(value)
            value //= 3
            self.toss(value, game)


def solve(task: str) -> int:
    monkeys: dict[int, Monkey] = {}

    for text in task.split("\n\n"):
        monkey = Monkey.from_text(text)
        monkeys[monkey.id] = monkey

    game = Game(monkeys)
    for _ in range(20):
        game.round()

    inspect = [x.inspect for x in game.monkeys.values()]
    inspect.sort()
    return inspect[-1] * inspect[-2]
