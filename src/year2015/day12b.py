"""2015 - Day 12 Part 2: JSAbacusFramework.io."""

from dataclasses import dataclass
from enum import Enum
from collections.abc import Iterator


class Symbol(Enum):
    OPEN = "("
    CLOSE = ")"
    RED = "red"


@dataclass(frozen=True, slots=True)
class Number:
    value: int


type Token = Number | Symbol


@dataclass
class Lexer:
    task: str
    i: int = 0

    @property
    def current(self) -> str:
        return self.task[self.i]

    def read_int(self) -> int:
        result = 0

        while self.current.isdigit():
            result = result * 10 + int(self.current)
            self.i += 1

        return result

    def consume_char(self, char: str) -> bool:
        if self.current == char:
            self.i += 1
            return True
        return False

    def consume_quote(self) -> bool:
        return self.consume_char('"')

    def consume_red(self) -> bool:
        if not self.consume_quote():
            return False

        for char in "red":
            if not self.consume_char(char):
                return False

        return self.consume_quote()

    def __iter__(self) -> Iterator[Token]:
        while self.i < len(self.task):
            match self.current:
                case "[" | "{":
                    self.i += 1
                    yield Symbol.OPEN
                case "]" | "}":
                    self.i += 1
                    yield Symbol.CLOSE
                case "-":
                    self.i += 1  # skip `-`
                    yield Number(-self.read_int())
                case _ if self.current.isdigit():
                    yield Number(self.read_int())
                case ":":
                    self.i += 1  # skip `:`
                    if self.consume_red():
                        yield Symbol.RED
                case _:
                    self.i += 1


def solve(task: str) -> int:
    stack = [0]
    skip_to_close = 0

    for token in Lexer(task):
        if skip_to_close != 0:
            if token is Symbol.OPEN:
                skip_to_close += 1
            elif token is Symbol.CLOSE:
                skip_to_close -= 1
            continue

        match token:
            case Symbol.OPEN:
                stack.append(0)
            case Symbol.CLOSE:
                last = stack.pop()
                stack[-1] += last
                skip_to_close = 1
            case Symbol.RED:
                stack.pop()
                skip_to_close = 1
            case Number(value=x):
                stack[-1] += x

    return stack[0]
