from pathlib import Path
from typing import Literal, NamedTuple

with Path(Path(__file__).parent, "input").open() as f:
    grid = [list(line.rstrip("\n")) for line in f]


class CoordsDirection(NamedTuple):
    x: int
    y: int
    direction: Literal["^", ">", "v", "<"]


height = len(grid)
width = len(grid[0])
guard = None

for y in range(height):
    for x in range(width):
        if grid[y][x] in ["^", ">", "v", "<"]:
            guard = CoordsDirection(x, y, grid[y][x])  # type: ignore
            break
    if guard is not None:
        break

assert guard is not None


def compute_usual_guard_path(
    grid: list[list[str]], guard: CoordsDirection
) -> set[tuple[int, int]]:
    positions: set[tuple[int, int]] = set()

    while (0 <= guard[0] < width) and (0 <= guard[1] < height):
        x, y, direction = guard
        if direction == "^":
            if y - 1 >= 0 and grid[y - 1][x] == "#":
                guard = CoordsDirection(guard.x, guard.y, ">")
            else:
                guard = CoordsDirection(x, y - 1, direction)
        if direction == ">":
            if x + 1 < width and grid[y][x + 1] == "#":
                guard = CoordsDirection(guard.x, guard.y, "v")
            else:
                guard = CoordsDirection(x + 1, y, direction)
        if direction == "v":
            if y + 1 < height and grid[y + 1][x] == "#":
                guard = CoordsDirection(guard.x, guard.y, "<")
            else:
                guard = CoordsDirection(x, y + 1, direction)
        if direction == "<":
            if x - 1 >= 0 and grid[y][x - 1] == "#":
                guard = CoordsDirection(guard.x, guard.y, "^")
            else:
                guard = CoordsDirection(x - 1, y, direction)
        positions.add((guard.x, guard.y))

    positions.remove((guard.x, guard.y))

    return positions


def is_guard_looping(grid: list[list[str]], guard: CoordsDirection) -> bool:
    paths: set[CoordsDirection] = {guard}

    while (0 <= guard[0] < width) and (0 <= guard[1] < height):
        x, y, direction = guard
        if direction == "^":
            if y - 1 >= 0 and grid[y - 1][x] == "#":
                guard = CoordsDirection(guard.x, guard.y, ">")
            else:
                guard = CoordsDirection(x, y - 1, direction)
        if direction == ">":
            if x + 1 < width and grid[y][x + 1] == "#":
                guard = CoordsDirection(guard.x, guard.y, "v")
            else:
                guard = CoordsDirection(x + 1, y, direction)
        if direction == "v":
            if y + 1 < height and grid[y + 1][x] == "#":
                guard = CoordsDirection(guard.x, guard.y, "<")
            else:
                guard = CoordsDirection(x, y + 1, direction)
        if direction == "<":
            if x - 1 >= 0 and grid[y][x - 1] == "#":
                guard = CoordsDirection(guard.x, guard.y, "^")
            else:
                guard = CoordsDirection(x - 1, y, direction)

        if guard in paths:
            return True
        paths.add(guard)

    return False


positions = compute_usual_guard_path(grid, guard)
count_possible_positions = 0

for position in positions:
    tmp = grid[position[1]][position[0]]
    grid[position[1]][position[0]] = "#"

    if is_guard_looping(grid, guard):
        count_possible_positions += 1

    grid[position[1]][position[0]] = tmp

print(f"Result: {count_possible_positions}")
