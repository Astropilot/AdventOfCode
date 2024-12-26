import typing as t
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Coords:
    x: int
    y: int


with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

DIRECTIONS: list[t.Literal["N", "S", "E", "W"]] = ["N", "E", "S", "W"]
ship_position = Coords(0, 0)
ship_direction: t.Literal["N", "S", "E", "W"] = "E"

for line in lines:
    action = t.cast(t.Literal["N", "S", "E", "W", "L", "R", "F"], line[0])
    value = int(line[1:])

    if action == "N":
        ship_position.y -= value
    elif action == "S":
        ship_position.y += value
    elif action == "E":
        ship_position.x += value
    elif action == "W":
        ship_position.x -= value
    elif action == "F":
        if ship_direction == "N":
            ship_position.y -= value
        elif ship_direction == "S":
            ship_position.y += value
        elif ship_direction == "E":
            ship_position.x += value
        elif ship_direction == "W":
            ship_position.x -= value
    else:
        turns = value // 90
        if action == "L":
            turns = -turns
        ship_direction = DIRECTIONS[
            (DIRECTIONS.index(ship_direction) + turns) % len(DIRECTIONS)
        ]

print(f"Result: {abs(ship_position.x) + abs(ship_position.y)}")
