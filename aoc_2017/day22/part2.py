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
direction_per_rotation: dict[
    Direction, dict[t.Literal["l", "r", "reverse"], Direction]
] = {
    "u": {"l": "l", "r": "r", "reverse": "d"},
    "d": {"l": "r", "r": "l", "reverse": "u"},
    "l": {"l": "d", "r": "u", "reverse": "r"},
    "r": {"l": "u", "r": "d", "reverse": "l"},
}


@dataclass(frozen=True)
class Coords:
    x: int
    y: int

    def add_direction(self, direction: Direction) -> "Coords":
        vec = direction_to_vec[direction]
        return Coords(self.x + vec[0], self.y + vec[1])


with Path(Path(__file__).parent, "input").open() as f:
    grid = [list(line.rstrip("\n")) for line in f]

HEIGHT = len(grid)
WIDTH = len(grid[0])
MIDDLE_X = WIDTH // 2
MIDDLE_Y = HEIGHT // 2
position = Coords(0, 0)
direction: Direction = "u"
infected_nodes: set[Coords] = set()
weakened_nodes: set[Coords] = set()
flagged_nodes: set[Coords] = set()
burst_infection_count = 0

for y in range(HEIGHT):
    for x in range(WIDTH):
        if grid[y][x] == "#":
            infected_nodes.add(Coords(x - MIDDLE_X, y - MIDDLE_Y))

for _ in range(10000000):
    if position in weakened_nodes:
        weakened_nodes.remove(position)
        infected_nodes.add(position)
        burst_infection_count += 1
    elif position in infected_nodes:
        direction = direction_per_rotation[direction]["r"]
        infected_nodes.remove(position)
        flagged_nodes.add(position)
    elif position in flagged_nodes:
        direction = direction_per_rotation[direction]["reverse"]
        flagged_nodes.remove(position)
    else:
        direction = direction_per_rotation[direction]["l"]
        weakened_nodes.add(position)

    position = position.add_direction(direction)

print(f"Result: {burst_infection_count}")
