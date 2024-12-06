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
        if grid[y][x] != "A":
            continue

        topleft_downright = (
            get_letter(grid, x - 1, y - 1) == "M"
            and get_letter(grid, x + 1, y + 1) == "S"
        ) or (
            get_letter(grid, x - 1, y - 1) == "S"
            and get_letter(grid, x + 1, y + 1) == "M"
        )

        topright_downleft = (
            get_letter(grid, x + 1, y - 1) == "M"
            and get_letter(grid, x - 1, y + 1) == "S"
        ) or (
            get_letter(grid, x + 1, y - 1) == "S"
            and get_letter(grid, x - 1, y + 1) == "M"
        )

        if topleft_downright and topright_downleft:
            xmas_counter += 1


print(f"Result {xmas_counter}")  # Result: 1950
