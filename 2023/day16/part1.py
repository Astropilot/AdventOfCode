from pathlib import Path
from typing import Literal, TypeAlias

contents = Path(Path(__file__).parent, "input").read_text()
lines = contents.split("\n")

Direction: TypeAlias = Literal["up", "down", "left", "right"]

map_count: list[list[tuple[str, list[Direction]]]] = []
mapping: dict[Direction, tuple[int, int]] = {
    "up": (0, -1),
    "down": (0, 1),
    "left": (-1, 0),
    "right": (1, 0),
}

for line in lines:
    map_count.append([])

    for c in line:
        map_count[-1].append((c, []))


def rec_fill_energy(
    map_count: list[list[tuple[str, list[Direction]]]],
    x: int,
    y: int,
    dir: Direction,
) -> None:
    while True:
        if x < 0 or x == len(map_count[0]):
            return
        if y < 0 or y == len(map_count):
            return
        if dir in map_count[y][x][1]:
            return

        map_count[y][x][1].append(dir)

        if map_count[y][x][0] == "/":
            match dir:
                case "up":
                    dir = "right"
                case "down":
                    dir = "left"
                case "left":
                    dir = "down"
                case "right":
                    dir = "up"
        elif map_count[y][x][0] == "\\":
            match dir:
                case "up":
                    dir = "left"
                case "down":
                    dir = "right"
                case "left":
                    dir = "up"
                case "right":
                    dir = "down"
        elif map_count[y][x][0] == "|" and dir in ["left", "right"]:
            rec_fill_energy(map_count, x, y - 1, "up")
            rec_fill_energy(map_count, x, y + 1, "down")
            return
        elif map_count[y][x][0] == "-" and dir in ["up", "down"]:
            rec_fill_energy(map_count, x - 1, y, "left")
            rec_fill_energy(map_count, x + 1, y, "right")
            return

        x, y = x + mapping[dir][0], y + mapping[dir][1]


rec_fill_energy(map_count, 0, 0, "right")

tiles_energized = 0
for y in range(len(map_count)):
    for x in range(len(map_count[y])):
        if len(map_count[y][x][1]) > 0:
            tiles_energized += 1

print(f"Result: {tiles_energized}")  # Result: 7951
