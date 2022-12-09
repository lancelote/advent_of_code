"""2022 - Day 7 Part 1: No Space Left On Device."""
from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field


@dataclass
class File:
    name: str
    size: int


@dataclass
class Directory:
    name: str
    parent: Directory | None = None
    content: dict[str, Directory | File] = field(default_factory=dict)

    @property
    def absolute_path(self) -> str:
        path: list[str] = []
        cwd: Directory | None = self

        while cwd:
            path.append(cwd.name)
            cwd = cwd.parent

        return ":".join(path)


def process_data(data: str) -> Directory:
    lines = data.splitlines()
    n = len(lines)
    i = 1
    root = cwd = Directory(name="/")

    while i != n:
        if lines[i].startswith("$ cd"):
            _, _, dir_name = lines[i].split()
            if dir_name == "..":
                if not cwd.parent:
                    raise ValueError(f"{cwd} doesn't have a parent")
                cwd = cwd.parent
            else:
                if dir_name in cwd.content:
                    obj = cwd.content[dir_name]
                    assert isinstance(obj, Directory)
                    cwd = obj
                else:
                    cwd = Directory(dir_name, cwd)
            i += 1
        elif lines[i].startswith("$ ls"):
            i += 1
            while i < n and not lines[i].startswith("$"):
                if lines[i].startswith("dir"):
                    _, dir_name = lines[i].split()
                    if dir_name not in cwd.content:
                        cwd.content[dir_name] = Directory(dir_name, cwd)
                else:
                    size_str, file_name = lines[i].split()
                    if file_name not in cwd.content:
                        file = File(file_name, int(size_str))
                        cwd.content[file_name] = file
                i += 1

    return root


def count_size(directory: Directory, cache: dict[str, int]) -> int:
    size = 0

    for _, obj in directory.content.items():
        if isinstance(obj, File):
            size += obj.size
        elif isinstance(obj, Directory):
            size += count_size(obj, cache)

    path = directory.absolute_path
    if path in cache:
        raise ValueError(f"{path} was already counted")
    cache[path] = size
    return size


def solve(task: str) -> int:
    root = process_data(task)
    cache: dict[str, int] = {}
    count_size(root, cache)
    return sum(x for x in cache.values() if x <= 100_000)
