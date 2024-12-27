import typing as t
from pathlib import Path


class Coords(t.NamedTuple):
    x: int
    y: int


with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

separator_idx = lines.index("")
grid: list[list[t.Literal["#", "O", "."]]] = []
robot: Coords = None  # type: ignore

for y in range(separator_idx):
    grid.append([])
    for x in range(len(lines[y])):
        if lines[y][x] in ["#", "O", "."]:
            grid[y].append(lines[y][x])  # type: ignore
        elif lines[y][x] == "@":
            robot = Coords(x, y)
            grid[y].append(".")

for line in lines[separator_idx + 1 :]:
    for direction in line:
        if direction == ">" or direction == "<":
            dir_i = 1 if direction == ">" else -1
            x = robot.x + dir_i
            while grid[robot.y][x] not in ["#", "."]:
                x += dir_i
            if grid[robot.y][x] == "#":
                continue
            for xx in range(x, robot.x, -dir_i):
                grid[robot.y][xx] = grid[robot.y][xx - dir_i]
            robot = Coords(robot.x + dir_i, robot.y)
        elif direction == "^" or direction == "v":
            dir_i = 1 if direction == "v" else -1
            y = robot.y + dir_i
            while grid[y][robot.x] not in ["#", "."]:
                y += dir_i
            if grid[y][robot.x] == "#":
                continue
            for yy in range(y, robot.y, -dir_i):
                grid[yy][robot.x] = grid[yy - dir_i][robot.x]
            robot = Coords(robot.x, robot.y + dir_i)

total_distance = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "O":
            total_distance += (y * 100) + x

print(f"Result: {total_distance}")
