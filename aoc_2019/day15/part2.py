import sys
import typing as t
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from aoc_2019.day15.intcode2 import ProgramState, execute_intcode

type Direction = t.Literal[1, 2, 3, 4]


class CoordsT(t.NamedTuple):
    x: int
    y: int


REVERSE_DIRECTION: dict[Direction, Direction] = {1: 2, 2: 1, 3: 4, 4: 3}
DIRECTIONS: list[tuple[Direction, CoordsT]] = [
    (1, CoordsT(0, -1)),
    (2, CoordsT(0, 1)),
    (3, CoordsT(-1, 0)),
    (4, CoordsT(1, 0)),
]

intcode = [int(c) for c in Path(Path(__file__).parent, "input").read_text().split(",")]
program = ProgramState(0, 0, intcode, False)
grid: dict[CoordsT, t.Literal["O", " ", "#"]] = {CoordsT(0, 0): " "}


def explore_area(position: CoordsT, old_position: CoordsT | None = None) -> None:
    global program
    global grid

    for command, vec in DIRECTIONS:
        new_position = CoordsT(position.x + vec.x, position.y + vec.y)

        if new_position == old_position:
            continue

        status = execute_intcode(program, [command])[0]

        if status == 0:
            grid[new_position] = "#"
        elif status == 2:
            grid[new_position] = "O"
            execute_intcode(program, [REVERSE_DIRECTION[command]])
        else:
            grid[new_position] = " "
            explore_area(new_position, position)
            execute_intcode(program, [REVERSE_DIRECTION[command]])

    return None


explore_area(CoordsT(0, 0))


minute = 0
while any(v == " " for v in grid.values()):
    for oxygen in [k for k, v in grid.items() if v == "O"]:
        for vec in [CoordsT(0, -1), CoordsT(0, 1), CoordsT(-1, 0), CoordsT(1, 0)]:
            c = CoordsT(oxygen.x + vec.x, oxygen.y + vec.y)
            if c in grid and grid[c] == " ":
                grid[c] = "O"
    minute += 1

print(f"Result: {minute}")
