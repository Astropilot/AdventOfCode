import typing as t
from pathlib import Path


class CoordsT(t.NamedTuple):
    x: int
    y: int


with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

coords_count: dict[CoordsT, int] = {}

for line in lines:
    start, end = line.split(" -> ")
    startx, starty = map(int, start.split(","))
    endx, endy = map(int, end.split(","))

    if startx == endx:
        direction = -1 if starty - endy > 0 else 1
        for y in range(starty, endy + direction, direction):
            c = CoordsT(startx, y)
            coords_count[c] = coords_count.setdefault(c, 0) + 1
    elif starty == endy:
        direction = -1 if startx - endx > 0 else 1
        for x in range(startx, endx + direction, direction):
            c = CoordsT(x, starty)
            coords_count[c] = coords_count.setdefault(c, 0) + 1
    else:
        directionx = -1 if startx - endx > 0 else 1
        directiony = -1 if starty - endy > 0 else 1
        c = CoordsT(startx, starty)
        while c != CoordsT(endx, endy):
            coords_count[c] = coords_count.setdefault(c, 0) + 1
            c = CoordsT(c.x + directionx, c.y + directiony)
        coords_count[c] = coords_count.setdefault(c, 0) + 1

r = len([m for m, c in coords_count.items() if c >= 2])

print(f"Result: {r}")
