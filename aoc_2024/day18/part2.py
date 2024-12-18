import typing as t
from pathlib import Path


class CoordsT(t.NamedTuple):
    x: int
    y: int


with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

corrupted: set[CoordsT] = set()
HEIGHT = WIDTH = 71  # 7 for sample


def get_neighbors(coords: CoordsT, corrupted: set[CoordsT]) -> list[CoordsT]:
    neighbors: list[CoordsT] = []

    for dx, dy in ((0, -1), (1, 0), (0, 1), (-1, 0)):
        new_coords = CoordsT(coords.x + dx, coords.y + dy)
        if (
            0 <= new_coords.x < WIDTH
            and 0 <= new_coords.y < HEIGHT
            and new_coords not in corrupted
        ):
            neighbors.append(new_coords)
    return neighbors


# We can skip already the first 1024
for line in lines[:1024]:
    x, y = map(int, line.split(","))
    corrupted.add(CoordsT(x, y))

for line in lines[1024:]:
    x, y = map(int, line.split(","))
    corrupted.add(CoordsT(x, y))

    start = CoordsT(0, 0)
    destination = CoordsT(WIDTH - 1, HEIGHT - 1)
    queue: list[CoordsT] = []
    visited: set[CoordsT] = set()
    previous: dict[CoordsT, CoordsT | None] = {start: None}

    visited.add(start)
    queue.append(start)

    while len(queue) > 0:
        u = queue.pop(0)

        if u == destination:
            break

        for neighbor in get_neighbors(u, corrupted):
            if neighbor not in visited:
                visited.add(neighbor)
                previous[neighbor] = u
                queue.append(neighbor)

    if destination not in previous:
        print(f"Result: {x},{y}")  # Result: 44,64
        break
