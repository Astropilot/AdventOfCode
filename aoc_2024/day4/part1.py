from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    grid = [list(line.rstrip("\n")) for line in f]

xmas_counter = 0


def get_letter(grid: list[list[str]], x: int, y: int) -> str:
    if y < 0 or y == len(grid):
        return ""
    if x < 0 or x == len(grid[y]):
        return ""
    return grid[y][x]


for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] != "X":
            continue

        deltas = [
            [(0, -1), (0, -2), (0, -3)],  # Up
            [(1, -1), (2, -2), (3, -3)],  # Up Right
            [(1, 0), (2, 0), (3, 0)],  # Right
            [(1, 1), (2, 2), (3, 3)],  # Down Right
            [(0, 1), (0, 2), (0, 3)],  # Down
            [(-1, 1), (-2, 2), (-3, 3)],  # Down Left
            [(-1, 0), (-2, 0), (-3, 0)],  # Left
            [(-1, -1), (-2, -2), (-3, -3)],  # Up Left
        ]

        for delta in deltas:
            if (
                get_letter(grid, x + delta[0][0], y + delta[0][1]) == "M"
                and get_letter(grid, x + delta[1][0], y + delta[1][1]) == "A"
                and get_letter(grid, x + delta[2][0], y + delta[2][1]) == "S"
            ):
                xmas_counter += 1


print(f"Result {xmas_counter}")
