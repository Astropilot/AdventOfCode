import typing as t
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Coords:
    x: int
    y: int


type DirectionLit = t.Literal["N", "S", "E", "W"]


DIRECTIONS: dict[DirectionLit, dict[t.Literal["R", "L"], DirectionLit]] = {
    "N": {"L": "W", "R": "E"},
    "E": {"L": "N", "R": "S"},
    "S": {"L": "E", "R": "W"},
    "W": {"L": "S", "R": "N"},
}
position = Coords(0, 0)
direction: DirectionLit = "N"

contents = Path(Path(__file__).parent, "input").read_text()
for command in contents.split(", "):
    action = t.cast(t.Literal["R", "L"], command[0])
    value = int(command[1:])

    direction = DIRECTIONS[direction][action]

    if direction == "N":
        position.y -= value
    elif direction == "S":
        position.y += value
    elif direction == "E":
        position.x += value
    elif direction == "W":
        position.x -= value

print(f"Result: {abs(position.x) + abs(position.y)}")
