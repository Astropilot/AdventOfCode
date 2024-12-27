import typing as t
from pathlib import Path


class CoordsT(t.NamedTuple):
    x: int
    y: int


with Path(Path(__file__).parent, "input").open() as f:
    grid = [list(line.rstrip("\n")) for line in f]

HEIGHT = len(grid)
WIDTH = len(grid[0])
walls: set[CoordsT] = set()
start = CoordsT(0, 0)
destination = CoordsT(0, 0)

for y in range(HEIGHT):
    for x in range(WIDTH):
        if grid[y][x] == "#":
            walls.add(CoordsT(x, y))
        elif grid[y][x] == "S":
            start = CoordsT(x, y)
        elif grid[y][x] == "E":
            destination = CoordsT(x, y)


def get_neighbors(coords: CoordsT, walls: set[CoordsT]) -> list[CoordsT]:
    neighbors: list[CoordsT] = []

    for dx, dy in ((0, -1), (1, 0), (0, 1), (-1, 0)):
        new_coords = CoordsT(coords.x + dx, coords.y + dy)
        if (
            0 <= new_coords.x < WIDTH
            and 0 <= new_coords.y < HEIGHT
            and new_coords not in walls
        ):
            neighbors.append(new_coords)
    return neighbors


def shortest_path_len(
    start: CoordsT, destination: CoordsT, walls: set[CoordsT]
) -> list[CoordsT]:
    queue: list[CoordsT] = []
    visited: set[CoordsT] = set()
    previous: dict[CoordsT, CoordsT | None] = {start: None}

    visited.add(start)
    queue.append(start)

    while len(queue) > 0:
        u = queue.pop(0)

        if u == destination:
            break

        for neighbor in get_neighbors(u, walls):
            if neighbor not in visited:
                visited.add(neighbor)
                previous[neighbor] = u
                queue.append(neighbor)

    if destination not in previous:
        raise ValueError("Did not found any correct path!")

    current: CoordsT | None = destination
    path: list[CoordsT] = []
    while current is not None:
        path.insert(0, current)
        current = previous[current]

    return path


path = shortest_path_len(start, destination, walls)
len_path = len(path) - 1
path_set = set(path)
count_highest_cheats = 0
tile_to_idx: dict[CoordsT, int] = {t: i for i, t in enumerate(path)}

for tile in path:
    if tile == destination:
        continue

    for dx, dy in ((0, -1), (1, 0), (0, 1), (-1, 0)):
        neighbor = CoordsT(tile.x + dx, tile.y + dy)
        neighbor_after = CoordsT(tile.x + dx + dx, tile.y + dy + dy)

        if (
            neighbor in walls
            and neighbor_after in path_set
            and tile_to_idx[neighbor_after] > tile_to_idx[tile]
        ):
            saved = abs(tile_to_idx[neighbor_after] - tile_to_idx[tile]) - 2
            if saved >= 100:
                count_highest_cheats += 1

print(f"Result: {count_highest_cheats}")
