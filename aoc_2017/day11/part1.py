import typing as t
from pathlib import Path

# Reference: https://www.redblobgames.com/grids/hexagons/


class Cube(t.NamedTuple):
    q: int
    r: int
    s: int


directions = Path(Path(__file__).parent, "input").read_text().split(",")


def get_neighbor(
    hex: Cube, direction: t.Literal["n", "s", "ne", "se", "nw", "sw"]
) -> Cube:
    match direction:
        case "n":
            return Cube(hex.q, hex.r - 1, hex.s + 1)
        case "s":
            return Cube(hex.q, hex.r + 1, hex.s - 1)
        case "ne":
            return Cube(hex.q + 1, hex.r - 1, hex.s)
        case "se":
            return Cube(hex.q + 1, hex.r, hex.s - 1)
        case "nw":
            return Cube(hex.q - 1, hex.r, hex.s + 1)
        case "sw":
            return Cube(hex.q - 1, hex.r + 1, hex.s)
        case _:
            raise ValueError("Unknown direction")


def hex_distance(hex1: Cube, hex2: Cube) -> int:
    vec = Cube(hex1.q - hex2.q, hex1.r - hex2.r, hex1.s - hex2.s)

    return (abs(vec.q) + abs(vec.r) + abs(vec.s)) // 2


position = Cube(0, 0, 0)
for direction in directions:
    position = get_neighbor(position, direction)  # type: ignore

print(hex_distance(Cube(0, 0, 0), position))
