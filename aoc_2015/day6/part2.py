import re
from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    instructions = [line.rstrip("\n") for line in f]

grid = [[0] * 1000 for _ in range(1000)]

for instruction in instructions:
    m = re.match(r"(toggle|turn off|turn on) (\d+,\d+) through (\d+,\d+)", instruction)
    assert m is not None

    command = m.group(1)
    start_x, start_y = map(int, m.group(2).split(","))
    end_x, end_y = map(int, m.group(3).split(","))

    for y in range(start_y, end_y + 1):
        for x in range(start_x, end_x + 1):
            if command == "turn on":
                grid[y][x] += 1
            elif command == "turn off":
                grid[y][x] -= 1
                if grid[y][x] < 0:
                    grid[y][x] = 0
            elif command == "toggle":
                grid[y][x] += 2

total_brightness = 0
for y in range(1000):
    for x in range(1000):
        total_brightness += grid[y][x]

print(f"Result: {total_brightness}")
