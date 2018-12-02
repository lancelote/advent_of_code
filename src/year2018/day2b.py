"""2018 - Day 2 Part 2: Inventory Management System.

Confident that your list of box IDs is complete, you're ready to find the boxes
full of prototype fabric.

The boxes will have IDs which differ by exactly one character at the same
position in both strings. For example, given the following box IDs:

    abcde
    fghij
    klmno
    pqrst
    fguij
    axcye
    wvxyz

The IDs abcde and axcye are close, but they differ by two characters
(the second and fourth). However, the IDs fghij and fguij differ by exactly
one character, the third (h and u). Those must be the correct boxes.

What letters are common between the two correct box IDs? (In the example above,
this is found by removing the differing character from either ID, producing
fgij.)
"""


def get_similar_id_part(box1: str, box2: str) -> str:
    """Get similar part between box1 and box2."""
    common = ''
    for i, char in enumerate(box1):
        if char == box2[i]:
            common += char
    return common


def solve(task: str) -> str:
    """Find first boxes with id different by 1 character."""
    common = ''
    boxes = task.strip().split('\n')
    limit = len(boxes[0]) - 1

    for i, box1 in enumerate(boxes):
        for j in range(i + 1, len(boxes)):
            common = get_similar_id_part(box1, boxes[j])
            if len(common) == limit:
                return common
    return common
