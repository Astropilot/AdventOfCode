import typing as t
from dataclasses import dataclass
from pathlib import Path

type Direction = t.Literal["u", "d", "l", "r"]
direction_to_vec: dict[Direction, tuple[int, int]] = {
    "u": (0, -1),
    "d": (0, 1),
    "l": (-1, 0),
    "r": (1, 0),
}
reverse_direction: dict[Direction, Direction] = {"u": "d", "d": "u", "l": "r", "r": "l"}


@dataclass(frozen=True)
class Coords:
    x: int
    y: int

    def add_direction(self, direction: Direction) -> "Coords":
        vec = direction_to_vec[direction]
        return Coords(self.x + vec[0], self.y + vec[1])


with Path(Path(__file__).parent, "input").open() as f:
    grid = [list(line.rstrip("\n")) for line in f]

position = Coords(grid[0].index("|"), 0)
direction: Direction = "d"
letters = ""

while True:
    if grid[position.y][position.x] not in (" ", "|", "-", "+"):
        letters += grid[position.y][position.x]
        position = position.add_direction(direction)
        continue

    if grid[position.y][position.x] == "+":
        for dir in direction_to_vec.keys():
            if dir != reverse_direction[direction]:
                neighbor = position.add_direction(dir)
                if (
                    0 <= neighbor.y < len(grid)
                    and 0 <= neighbor.x < len(grid[neighbor.y])
                    and grid[neighbor.y][neighbor.x] != " "
                ):
                    position = neighbor
                    direction = dir
        continue

    if grid[position.y][position.x] == " ":
        break

    position = position.add_direction(direction)

print(f"Result: {letters}")
