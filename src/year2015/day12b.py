"""2015 - Day 12 Part 2: JSAbacusFramework.io."""

from typing import Any


class Parser:
    def __init__(self, task: str) -> None:
        self.task = task
        self.i = 0

    def parse_expression(self) -> Any:
        match self.cur_token:
            case "[":
                return self.parse_list()
            case "{":
                return self.parse_dict()
            case '"':
                return self.parse_str()
            case _ if self.cur_token.isdigit():
                return self.parse_int()
            case "-":
                self.consume("-")
                return -self.parse_int()
            case _:
                raise ValueError(f"unknown first token {self.cur_token}")

    def consume(self, token: str) -> None:
        assert self.cur_token == token
        self.i += 1

    def parse_str(self) -> str:
        self.consume('"')
        result: list[str] = []

        while self.cur_token != '"':
            result.append(self.cur_token)
            self.i += 1

        self.consume('"')
        return "".join(result)

    def parse_int(self) -> int:
        result = 0

        while self.cur_token.isdigit():
            result = result * 10 + int(self.cur_token)
            self.i += 1

        return result

    def parse_opt(self) -> tuple[str, Any]:
        key = self.parse_str()
        self.consume(":")
        value = self.parse_expression()
        return key, value

    def parse_list(self) -> list:
        self.consume("[")
        result = []

        while self.cur_token != "]":
            result.append(self.parse_expression())
            if self.cur_token == ",":
                self.i += 1

        self.consume("]")
        return result

    def parse_dict(self) -> dict:
        self.consume("{")
        result = {}

        while self.cur_token != "}":
            key, value = self.parse_opt()
            result[key] = value
            if self.cur_token == ",":
                self.i += 1

        self.consume("}")
        return result

    @property
    def cur_token(self):
        return self.task[self.i]


def sum_dfs(exp) -> int:
    match exp:
        case dict():
            if "red" in exp.values():
                return 0
            return sum(sum_dfs(v) for v in exp.values())
        case list():
            return sum(sum_dfs(x) for x in exp)
        case int():
            return exp
        case str():
            return 0
        case _:
            raise ValueError(f"unexpected type {type(exp)}")


def solve(task: str) -> int:
    exp = Parser(task).parse_expression()
    return sum_dfs(exp)
