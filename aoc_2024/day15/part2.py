import typing as t
from pathlib import Path


class Coords(t.NamedTuple):
    x: int
    y: int


with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

separator_idx = lines.index("")
grid: list[list[t.Literal["[", "]", "#", "."]]] = []
robot: Coords = None  # type: ignore

for y in range(separator_idx):
    grid.append([])
    for x in range(len(lines[y])):
        if lines[y][x] in ["#", "."]:
            grid[y].append(lines[y][x])  # type: ignore
            grid[y].append(lines[y][x])  # type: ignore
        if lines[y][x] == "O":
            grid[y].append("[")
            grid[y].append("]")
        elif lines[y][x] == "@":
            robot = Coords(len(grid[y]), y)
            grid[y].append(".")
            grid[y].append(".")


def resolve_x_move(dir_i: int, x: int, y: int) -> bool:
    if grid[y][x] == "#":
        return False
    if grid[y][x] == ".":
        return True

    res_box = resolve_x_move(dir_i, x + (dir_i * 2), y)

    if res_box:
        grid[y][x + (dir_i * 2)] = grid[y][x + dir_i]
        grid[y][x + dir_i] = grid[y][x]

    return res_box


def resolve_y_move(dir_i: int, x: int, y: int, check_only: bool = False) -> bool:
    if grid[y][x] == "#":
        return False
    if grid[y][x] == ".":
        return True

    res_box_first = resolve_y_move(dir_i, x, y + dir_i, check_only)
    if res_box_first:
        idx = 1 if grid[y][x] == "[" else -1
        res_box_other = resolve_y_move(dir_i, x + idx, y + dir_i, check_only)

        if not res_box_other:
            return False

        if not check_only:
            grid[y + dir_i][x] = grid[y][x]
            grid[y + dir_i][x + idx] = grid[y][x + idx]
            grid[y][x] = "."
            grid[y][x + idx] = "."

        return True

    return False


for line in lines[separator_idx + 1 :]:
    for direction in line:
        if direction in ["<", ">"]:
            dir_i = 1 if direction == ">" else -1
            if resolve_x_move(dir_i, robot.x + dir_i, robot.y):
                grid[robot.y][robot.x + dir_i] = grid[robot.y][robot.x]
                robot = Coords(robot.x + dir_i, robot.y)
        if direction in ["^", "v"]:
            dir_i = 1 if direction == "v" else -1
            if resolve_y_move(dir_i, robot.x, robot.y + dir_i, True):
                resolve_y_move(dir_i, robot.x, robot.y + dir_i, False)
                grid[robot.y + dir_i][robot.x] = grid[robot.y][robot.x]
                robot = Coords(robot.x, robot.y + dir_i)

total_distance = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "[":
            total_distance += (y * 100) + x

print(f"Result: {total_distance}")
