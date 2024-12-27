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
visited: set[tuple[int, int]] = {(position.x, position.y)}

contents = Path(Path(__file__).parent, "input").read_text()
for command in contents.split(", "):
    action = t.cast(t.Literal["R", "L"], command[0])
    value = int(command[1:])

    direction = DIRECTIONS[direction][action]

    found = False
    for _ in range(value):
        if direction == "N":
            position.y -= 1
        elif direction == "S":
            position.y += 1
        elif direction == "E":
            position.x += 1
        elif direction == "W":
            position.x -= 1
        if (position.x, position.y) in visited:
            found = True
            break
        visited.add((position.x, position.y))

    if found:
        break

print(f"Result: {abs(position.x) + abs(position.y)}")
