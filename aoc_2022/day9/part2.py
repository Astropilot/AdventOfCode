import typing as t
from dataclasses import dataclass
from pathlib import Path


class CoordsT(t.NamedTuple):
    x: int
    y: int


@dataclass
class Tail:
    x: int
    y: int


with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

head = Tail(0, 0)
tails: list[Tail] = [Tail(0, 0) for _ in range(9)]
tail_visited: set[CoordsT] = {CoordsT(0, 0)}
DIRECTIONS_TO_VELOCITY: dict[str, CoordsT] = {
    "U": CoordsT(0, -1),
    "D": CoordsT(0, 1),
    "L": CoordsT(-1, 0),
    "R": CoordsT(1, 0),
}


for line in lines:
    direction, count_str = line.split(" ")
    count = int(count_str)

    for _ in range(count):
        dx, dy = DIRECTIONS_TO_VELOCITY[direction]
        head = Tail(head.x + dx, head.y + dy)
        current_head = head

        for i, tail in enumerate(tails, 1):
            if tail.x == current_head.x:
                if abs(tail.y - current_head.y) == 2:
                    tail.y += -1 if tail.y - current_head.y > 0 else 1
                    if i == 9:
                        tail_visited.add(CoordsT(tail.x, tail.y))
            elif tail.y == current_head.y:
                if abs(tail.x - current_head.x) == 2:
                    tail.x += -1 if tail.x - current_head.x > 0 else 1
                    if i == 9:
                        tail_visited.add(CoordsT(tail.x, tail.y))
            else:
                candidates = [
                    Tail(tail.x + 1, tail.y - 1),
                    Tail(tail.x + 1, tail.y + 1),
                    Tail(tail.x - 1, tail.y - 1),
                    Tail(tail.x - 1, tail.y + 1),
                ]
                if current_head not in candidates:
                    head_dx = 1 if current_head.x - tail.x > 0 else -1
                    head_dy = 1 if current_head.y - tail.y > 0 else -1
                    tail.x += head_dx
                    tail.y += head_dy
                    if i == 9:
                        tail_visited.add(CoordsT(tail.x, tail.y))
            current_head = tail


print(f"Result: {len(tail_visited)}")
