import typing as t
from pathlib import Path


class CoordsT(t.NamedTuple):
    x: int
    y: int


with Path(Path(__file__).parent, "input").open() as f:
    grid = [list(map(int, line.rstrip("\n"))) for line in f]

HEIGHT = len(grid)
WIDTH = len(grid[0])

total_flash = 0
for _ in range(100):
    total_flashed: set[CoordsT] = set()
    flashed: set[CoordsT] = set()
    for y in range(HEIGHT):
        for x in range(WIDTH):
            grid[y][x] += 1
            if grid[y][x] > 9:
                total_flashed.add(CoordsT(x, y))
                flashed.add(CoordsT(x, y))

    while len(flashed) > 0:
        new_flashed: set[CoordsT] = set()
        for flash in flashed:
            for dx, dy in (
                (0, -1),
                (1, -1),
                (1, 0),
                (1, 1),
                (0, 1),
                (-1, 1),
                (-1, 0),
                (-1, -1),
            ):
                if 0 <= flash.x + dx < WIDTH and 0 <= flash.y + dy < HEIGHT:
                    neighbor = CoordsT(flash.x + dx, flash.y + dy)
                    grid[flash.y + dy][flash.x + dx] += 1

                    if (
                        grid[flash.y + dy][flash.x + dx] > 9
                        and neighbor not in total_flashed
                    ):
                        new_flashed.add(neighbor)
        flashed = new_flashed
        total_flashed.update(new_flashed)

    total_flash += len(total_flashed)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            if grid[y][x] > 9:
                grid[y][x] = 0

print(f"Result: {total_flash}")
