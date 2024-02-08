"""2023 - Day 19 Part 1: Aplenty"""
import operator
import re
from collections.abc import Callable
from dataclasses import dataclass
from typing import Self


@dataclass
class Part:
    categories: dict[str, int]

    @classmethod
    def from_line(cls, line: str) -> Self:
        line = line.strip("{}")
        categories: dict[str, int] = {}

        for field in line.split(","):
            name, val = field.split("=")
            categories[name] = int(val)

        return cls(categories)

    @property
    def value(self) -> int:
        return sum(self.categories.values())


@dataclass
class Rule:
    target: str
    condition: Callable[[Part], bool]

    @classmethod
    def from_text(cls, text: str) -> Self:
        if ":" not in text:
            target = text
            return cls(target, lambda part: True)
        else:
            match = re.match(r"(\w+)(.)(\d+):(\w+)", text)
            assert match

            field, op, limit, target = match.groups()
            condition = operator.le if op == "<" else operator.gt
            return cls(
                target,
                lambda part: condition(part.categories[field], int(limit)),
            )

    def applies(self, part: Part) -> bool:
        return self.condition(part)


@dataclass
class Workflow:
    name: str
    rules: list[Rule]

    @classmethod
    def from_line(cls, line: str) -> Self:
        name, rules_part = line.strip("}").split("{")
        rules = [Rule.from_text(x) for x in rules_part.split(",")]
        return cls(name, rules)


def process_task(task: str) -> tuple[dict[str, Workflow], list[Part]]:
    workflow_block, parts_block = task.split("\n\n")
    workflows: dict[str, Workflow] = {}

    for line in workflow_block.splitlines():
        workflow = Workflow.from_line(line)
        workflows[workflow.name] = workflow

    parts = [Part.from_line(line) for line in parts_block.splitlines()]
    return workflows, parts


def solve(task: str) -> int:
    result = 0
    workflows, parts = process_task(task)

    for part in parts:
        workflow_name = "in"

        while workflow_name not in {"A", "R"}:
            workflow = workflows[workflow_name]

            for rule in workflow.rules:
                if rule.applies(part):
                    workflow_name = rule.target
                    break

        if workflow_name == "A":
            result += part.value

    return result
