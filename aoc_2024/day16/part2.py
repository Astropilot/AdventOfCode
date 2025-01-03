import math
import typing as t
from pathlib import Path
from queue import PriorityQueue, Queue


class Coords(t.NamedTuple):
    x: int
    y: int
    dir: t.Literal["N", "E", "S", "W"] | None


with Path(Path(__file__).parent, "input").open() as f:
    grid = [list(line.rstrip("\n")) for line in f]

start: Coords = None  # type: ignore
end: Coords = None  # type: ignore
vertices: list[Coords] = []
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "S":
            start = Coords(x, y, "E")
        elif grid[y][x] == "E":
            end = Coords(x, y, None)
            vertices.append(Coords(x, y, None))
        elif grid[y][x] == ".":
            vertices.append(Coords(x, y, None))


def get_neighbors(coords: Coords) -> list[Coords]:
    neighbors: list[Coords] = []

    for dx, dy, direction in [(0, -1, "N"), (1, 0, "E"), (0, 1, "S"), (-1, 0, "W")]:
        x = coords.x + dx
        y = coords.y + dy
        if (
            0 <= x < len(grid[0])
            and 0 <= y <= len(grid)
            and (grid[y][x] == "." or grid[y][x] == "E")
        ):
            neighbors.append(Coords(x, y, direction))  # type: ignore

    return neighbors


distance: dict[Coords, float] = {}
previouses: dict[Coords, list[Coords]] = {}
Q: PriorityQueue[tuple[float, Coords]] = PriorityQueue()

distance[start] = 0
Q.put((0, start))

while not Q.empty():
    u_dis, u = Q.get()

    if u.x == end.x and u.y == end.y:
        break

    for v in get_neighbors(u):
        alt = u_dis + 1 + (1000 if u.dir != v.dir else 0)
        if alt <= distance.get(v, math.inf):
            distance[v] = alt
            Q.put((alt, v))
            if alt == distance.get(v, math.inf):
                if v not in previouses:
                    previouses[v] = []
                previouses[v].append(u)

tiles: set[tuple[int, int]] = set()
queue: Queue[Coords] = Queue()
visited: set[Coords] = set()

for direction in ("N", "E", "S", "W"):
    e = Coords(end.x, end.y, direction)
    if e in distance:
        queue.put(e)

while not queue.empty():
    u = queue.get()

    if u in visited:
        continue
    visited.add(u)
    tiles.add((u.x, u.y))

    if u in previouses:
        for v in previouses[u]:
            queue.put(v)

print(f"Result: {len(tiles)}")
