import typing as t
from functools import cache
from itertools import product
from pathlib import Path


class CoordsT(t.NamedTuple):
    x: int
    y: int


with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

DIGIT_POSITIONS: dict[str, CoordsT] = {
    "7": CoordsT(0, 0),
    "8": CoordsT(1, 0),
    "9": CoordsT(2, 0),
    "4": CoordsT(0, 1),
    "5": CoordsT(1, 1),
    "6": CoordsT(2, 1),
    "1": CoordsT(0, 2),
    "2": CoordsT(1, 2),
    "3": CoordsT(2, 2),
    "0": CoordsT(1, 3),
    "A": CoordsT(2, 3),
}
DIRECTION_POSITIONS: dict[str, CoordsT] = {
    "^": CoordsT(1, 0),
    "A": CoordsT(2, 0),
    "<": CoordsT(0, 1),
    "v": CoordsT(1, 1),
    ">": CoordsT(2, 1),
}
NUMERIC_FORBIDDEN = CoordsT(0, 3)
DIRECTIONAL_FORBIDDEN = CoordsT(0, 0)


@cache
def numeric_all_shortest_paths(
    start: CoordsT, goal: CoordsT, forbidden: CoordsT
) -> list[str]:
    if start == goal:
        return [""]
    if start == forbidden:
        return []

    if start.x == goal.x:
        path = ""
        direction = "^" if start.y > goal.y else "v"
        distance = abs(start.y - goal.y)
        for _ in range(distance):
            path += direction
        return [path]
    if start.y == goal.y:
        path = ""
        direction = "<" if start.x > goal.x else ">"
        distance = abs(start.x - goal.x)
        for _ in range(distance):
            path += direction
        return [path]

    direction_x = "<" if start.x > goal.x else ">"
    direction_y = "^" if start.y > goal.y else "v"

    next_x = CoordsT(start.x + (-1 if direction_x == "<" else 1), start.y)
    paths_x = [
        e[0] + e[1]
        for e in product(
            [direction_x], numeric_all_shortest_paths(next_x, goal, forbidden)
        )
    ]

    next_y = CoordsT(start.x, start.y + (-1 if direction_y == "^" else 1))
    paths_y = [
        e[0] + e[1]
        for e in product(
            [direction_y], numeric_all_shortest_paths(next_y, goal, forbidden)
        )
    ]

    return paths_x + paths_y


def resolve_numeric_code(code: str) -> list[str]:
    sequences: list[str] = [""]
    current_digit = "A"

    for digit in code:
        paths = numeric_all_shortest_paths(
            DIGIT_POSITIONS[current_digit],
            DIGIT_POSITIONS[digit],
            NUMERIC_FORBIDDEN,
        )

        sequences = [e[0] + e[1] + "A" for e in product(sequences, paths)]

        current_digit = digit

    return sequences


MAX_ROBOTS = 25


@cache
def smallest_sequence(current: str, next: str, robot: int) -> int:
    if current == next:
        return 1

    sequences = numeric_all_shortest_paths(
        DIRECTION_POSITIONS[current], DIRECTION_POSITIONS[next], DIRECTIONAL_FORBIDDEN
    )
    sequences = [s + "A" for s in sequences]

    if robot == MAX_ROBOTS:
        return min([len(s) for s in sequences])

    seq_lens = []
    for sequence in sequences:
        current_digit = "A"
        min_seq = 0

        for digit in sequence:
            min_seq += smallest_sequence(current_digit, digit, robot + 1)
            current_digit = digit
        seq_lens.append(min_seq)

    return min(seq_lens)


total_complexities = 0
for code in lines:
    sequences = resolve_numeric_code(code)
    seq_lens = []

    for sequence in sequences:
        current_digit = "A"
        min_seq = 0

        for digit in sequence:
            min_seq += smallest_sequence(current_digit, digit, 1)
            current_digit = digit
        seq_lens.append(min_seq)

    total_complexities += min(seq_lens) * int(code.replace("A", ""), 10)

print(f"Result: {total_complexities}")  # Result: 248919739734728
