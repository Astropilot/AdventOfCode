from pathlib import Path
from typing import NamedTuple

with Path(Path(__file__).parent, "input").open() as f:
    grid = [list(map(int, line.rstrip("\n"))) for line in f]


class Coords(NamedTuple):
    x: int
    y: int


height = len(grid)
width = len(grid[0])


def find_hiking_trails(x: int, y: int, nb: int) -> int:
    nb_paths = 0

    for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        if (
            (0 <= x + dx < width)
            and (0 <= y + dy < height)
            and grid[y + dy][x + dx] == nb
        ):
            if nb == 9:
                nb_paths += 1
            else:
                nb_paths += find_hiking_trails(x + dx, y + dy, nb + 1)

    return nb_paths


score = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == 0:
            score += find_hiking_trails(x, y, 1)

print(f"Result: {score}")
