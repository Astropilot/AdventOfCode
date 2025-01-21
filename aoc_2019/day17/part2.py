import sys
import typing as t
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from aoc_2019.day17.intcode2 import ProgramState, execute_intcode

type Direction = t.Literal["^", "v", "<", ">"]


class CoordsT(t.NamedTuple):
    x: int
    y: int


DIRECTIONS: dict[Direction, CoordsT] = {
    "^": CoordsT(0, -1),
    "v": CoordsT(0, 1),
    "<": CoordsT(-1, 0),
    ">": CoordsT(1, 0),
}
NEIGHBORS: dict[Direction, tuple[Direction, Direction]] = {
    "^": ("<", ">"),
    "v": ("<", ">"),
    "<": ("^", "v"),
    ">": ("^", "v"),
}
ASCII_DIRECTIONS = [ord("^"), ord("v"), ord("<"), ord(">")]

intcode = [int(c) for c in Path(Path(__file__).parent, "input").read_text().split(",")]
program = ProgramState(0, 0, intcode.copy(), False)
output = execute_intcode(program, [])

scaffolds: set[CoordsT] = set()
robot_pos = CoordsT(0, 0)
direction: Direction = "^"

x = 0
y = 0
for code in output:
    if code == 35:
        scaffolds.add(CoordsT(x, y))
    elif code == 10:
        y += 1
        x = 0
        continue
    elif code in ASCII_DIRECTIONS:
        robot_pos = CoordsT(x, y)
        scaffolds.add(robot_pos)
        direction = chr(code)  # type: ignore
    x += 1

ROTATIONS: dict[Direction, dict[Direction, t.Literal["R", "L"]]] = {
    "^": {"<": "L", ">": "R"},
    "v": {"<": "R", ">": "L"},
    "<": {"^": "R", "v": "L"},
    ">": {"^": "L", "v": "R"},
}
steps = 0
path: list[str] = []
while True:
    vec = DIRECTIONS[direction]
    coords = CoordsT(robot_pos.x + vec.x, robot_pos.y + vec.y)

    if coords in scaffolds:
        robot_pos = coords
        steps += 1
    else:
        if steps > 0:
            path.append(str(steps))
        steps = 0

        dir1, dir2 = NEIGHBORS[direction]
        nvec1, nvec2 = DIRECTIONS[dir1], DIRECTIONS[dir2]
        c1 = CoordsT(robot_pos.x + nvec1.x, robot_pos.y + nvec1.y)
        c2 = CoordsT(robot_pos.x + nvec2.x, robot_pos.y + nvec2.y)

        if c1 in scaffolds:
            path.append(ROTATIONS[direction][dir1])
            direction = dir1
        elif c2 in scaffolds:
            path.append(ROTATIONS[direction][dir2])
            direction = dir2
        else:
            break

MAX_MEMORY = 20


def split_path(
    path: list[str], candidates: list[list[str]]
) -> tuple[list[str], list[list[str]]] | None:
    if len(path) == 0:
        return ([], candidates)
    if len(candidates) > 3:
        return None

    for i, candidate in enumerate(candidates):
        if path[: len(candidate)] == candidate:
            r = split_path(path[len(candidate) :], candidates)
            if r is not None:
                return ([str(i)] + r[0], r[1])

    if len(candidates) == 3:
        return None

    for size in range(MAX_MEMORY, 0, -1):
        candidate = path[:size]
        if len(",".join(candidate)) > MAX_MEMORY:
            continue
        r = split_path(path[size:], [*candidates, candidate])
        if r is not None:
            return ([str(len(candidates))] + r[0], r[1])

    return None


def ascii_input_convert(input: str) -> list[int]:
    return [ord(c) for c in input] + [10]


result = split_path(path, [])

assert result is not None

new_intcode = intcode.copy()
new_intcode[0] = 2
program = ProgramState(0, 0, new_intcode, False)

main = ascii_input_convert(
    ",".join(result[0]).replace("0", "A").replace("1", "B").replace("2", "C")
)
a = ascii_input_convert(",".join(result[1][0]))
b = ascii_input_convert(",".join(result[1][1]))
c = ascii_input_convert(",".join(result[1][2]))
video_feed = ascii_input_convert("n")
output = execute_intcode(program, main + a + b + c + video_feed)

print(f"Result: {output[-1]}")
