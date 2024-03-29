"""2018 - Day 2 Part 2: Inventory Management System."""


def get_similar_id_part(box1: str, box2: str) -> str:
    """Get similar part between box1 and box2."""
    common = ""
    for i, char in enumerate(box1):
        if char == box2[i]:
            common += char
    return common


def solve(task: str) -> str:
    """Find first boxes with id different by 1 character."""
    common = ""
    boxes = task.strip().split("\n")
    limit = len(boxes[0]) - 1

    for i, box1 in enumerate(boxes):
        for j in range(i + 1, len(boxes)):
            common = get_similar_id_part(box1, boxes[j])
            if len(common) == limit:
                return common
    return common
