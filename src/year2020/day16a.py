"""2020 - Day 16 Part 1: Ticket Translation."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Range:
    start: int
    stop: int

    @staticmethod
    def from_text(text: str) -> Range:
        start, stop = text.split("-")
        return Range(int(start), int(stop))

    def __contains__(self, item: int) -> bool:
        return self.start <= item <= self.stop


@dataclass
class Rule:
    field: str
    range1: Range
    range2: Range

    @staticmethod
    def from_text(text: str) -> Rule:
        field, ranges = text.split(": ")
        range1, range2 = ranges.split(" or ")
        return Rule(field, Range.from_text(range1), Range.from_text(range2))

    def __contains__(self, item: int) -> bool:
        return item in self.range1 or item in self.range2


@dataclass
class Ticket:
    fields: list[int]

    @staticmethod
    def from_text(text: str) -> Ticket:
        return Ticket([int(x) for x in text.split(",")])

    def error_rate(self, rules: list[Rule]) -> int:
        errors = 0

        for field in self.fields:
            for rule in rules:
                if field in rule:
                    break
            else:
                errors += field

        return errors


@dataclass
class Puzzle:
    rules: list[Rule]
    my_ticket: Ticket
    tickets: list[Ticket]

    @staticmethod
    def from_text(text: str) -> Puzzle:
        raw_rules, raw_ticket, raw_tickets = text.split("\n\n")

        rules = [Rule.from_text(line) for line in raw_rules.split("\n")]

        ticket = Ticket.from_text(raw_ticket.split("\n")[1])

        tickets = [
            Ticket.from_text(line) for line in raw_tickets.split("\n")[1:]
        ]

        return Puzzle(rules, ticket, tickets)

    @property
    def ticket_scanning_error_rate(self) -> int:
        return sum(ticket.error_rate(self.rules) for ticket in self.tickets)


def solve(task: str) -> int:
    puzzle = Puzzle.from_text(task)
    return puzzle.ticket_scanning_error_rate
