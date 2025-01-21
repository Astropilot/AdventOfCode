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
program = ProgramState(0, 0, intcode, False)
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

visited: set[CoordsT] = {robot_pos}
intersections: set[CoordsT] = set()

while True:
    vec = DIRECTIONS[direction]
    c = CoordsT(robot_pos.x + vec.x, robot_pos.y + vec.y)

    if c in scaffolds:
        if c in visited:
            intersections.add(c)
        visited.add(c)
        robot_pos = c
    else:
        dir1, dir2 = NEIGHBORS[direction]
        nvec1, nvec2 = DIRECTIONS[dir1], DIRECTIONS[dir2]
        c1 = CoordsT(robot_pos.x + nvec1.x, robot_pos.y + nvec1.y)
        c2 = CoordsT(robot_pos.x + nvec2.x, robot_pos.y + nvec2.y)

        if c1 in scaffolds:
            direction = dir1
        elif c2 in scaffolds:
            direction = dir2
        else:
            break

r = sum(i.x * i.y for i in intersections)

print(f"Result: {r}")
