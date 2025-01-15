import sys
import typing as t
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from aoc_2019.day15.intcode2 import ProgramState, execute_intcode

type Direction = t.Literal[1, 2, 3, 4]
type Status = t.Literal[0, 1, 2]


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


def find_oxygen_system(
    position: CoordsT, old_position: CoordsT | None = None, moves: int = 0
) -> int | None:
    global program

    for command, vec in DIRECTIONS:
        new_position = CoordsT(position.x + vec.x, position.y + vec.y)

        if new_position == old_position:
            continue

        status = execute_intcode(program, [command])[0]

        if status == 0:
            continue
        elif status == 2:
            execute_intcode(program, [REVERSE_DIRECTION[command]])
            return moves + 1
        else:
            steps = find_oxygen_system(new_position, position, moves + 1)
            execute_intcode(program, [REVERSE_DIRECTION[command]])

            if steps:
                return steps

    return None


steps = find_oxygen_system(CoordsT(0, 0))

assert steps is not None

print(f"Result: {steps}")
