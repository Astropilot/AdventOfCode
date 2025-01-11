import sys
import typing as t
from dataclasses import dataclass
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from aoc_2019.day7.intcode2 import ProgramState, execute_intcode

type DirectionLit = t.Literal["N", "S", "E", "W"]


@dataclass(frozen=True)
class Coords:
    x: int
    y: int

    def add_direction(self, direction: DirectionLit) -> "Coords":
        if direction == "N":
            return Coords(self.x, self.y - 1)
        elif direction == "S":
            return Coords(self.x, self.y + 1)
        elif direction == "W":
            return Coords(self.x - 1, self.y)
        elif direction == "E":
            return Coords(self.x + 1, self.y)


DIRECTIONS: dict[DirectionLit, dict[t.Literal[0, 1], DirectionLit]] = {
    "N": {0: "W", 1: "E"},
    "E": {0: "N", 1: "S"},
    "S": {0: "E", 1: "W"},
    "W": {0: "S", 1: "N"},
}
intcode_ori = [
    int(c) for c in Path(Path(__file__).parent, "input").read_text().split(",")
]
program = ProgramState(0, 0, intcode_ori.copy(), False)
position = Coords(0, 0)
visited: set[Coords] = set()
colors: dict[Coords, t.Literal[0, 1]] = {position: 0}
direction: DirectionLit = "N"

while not program.finished:
    color, dir = execute_intcode(program, [colors[position]])
    colors[position] = color  # type: ignore
    visited.add(position)
    direction = DIRECTIONS[direction][dir]  # type: ignore
    position = position.add_direction(direction)

    if position not in colors:
        colors[position] = 0

print(f"Result: {len(visited)}")
