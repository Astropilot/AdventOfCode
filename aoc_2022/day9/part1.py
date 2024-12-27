import typing as t
from pathlib import Path


class CoordsT(t.NamedTuple):
    x: int
    y: int


with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

head = CoordsT(0, 0)
tail = CoordsT(0, 0)
tail_visited: set[CoordsT] = {tail}
DIRECTIONS_TO_VELOCITY: dict[str, CoordsT] = {
    "U": CoordsT(0, -1),
    "D": CoordsT(0, 1),
    "L": CoordsT(-1, 0),
    "R": CoordsT(1, 0),
}

for line in lines:
    direction, count_str = line.split(" ")
    count = int(count_str)
    dx, dy = DIRECTIONS_TO_VELOCITY[direction]

    for _ in range(count):
        head = CoordsT(head.x + dx, head.y + dy)

        if tail.x == head.x:
            if abs(tail.y - head.y) == 2:
                tail = CoordsT(tail.x, tail.y + dy)
                tail_visited.add(tail)
        elif tail.y == head.y:
            if abs(tail.x - head.x) == 2:
                tail = CoordsT(tail.x + dx, tail.y)
                tail_visited.add(tail)
        else:
            candidates = [
                CoordsT(tail.x + 1, tail.y - 2),
                CoordsT(tail.x + 1, tail.y + 2),
                CoordsT(tail.x - 1, tail.y - 2),
                CoordsT(tail.x - 1, tail.y + 2),
                CoordsT(tail.x + 2, tail.y - 1),
                CoordsT(tail.x + 2, tail.y + 1),
                CoordsT(tail.x - 2, tail.y - 1),
                CoordsT(tail.x - 2, tail.y + 1),
            ]
            if head in candidates:
                tail = CoordsT(head.x - dx, head.y - dy)
                tail_visited.add(tail)


print(f"Result: {len(tail_visited)}")
