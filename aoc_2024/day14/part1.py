import re
import typing as t
from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]


class Coords(t.NamedTuple):
    x: int
    y: int


width = 101  # 11 for sample
height = 103  # 7 for sample
final_coords: list[Coords] = []

for line in lines:
    m = re.match(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", line)

    assert m is not None

    r_x, r_y, v_x, v_y = list(map(int, m.groups()))

    for _ in range(100):
        r_x = (r_x + v_x) % width
        r_y = (r_y + v_y) % height

    final_coords.append(Coords(r_x, r_y))

x_before = width // 2 - 1
x_after = x_before + 2
y_before = height // 2 - 1
y_after = y_before + 2

#                      x    y    w    h
quadrants: list[tuple[int, int, int, int]] = [
    (0, 0, x_before, y_before),
    (x_after, 0, width - 1, y_before),
    (0, y_after, x_before, height - 1),
    (x_after, y_after, width - 1, height - 1),
]

safety_factor = 1
for q in quadrants:
    safety_factor *= len(
        list(
            filter(lambda c: q[0] <= c.x <= q[2] and q[1] <= c.y <= q[3], final_coords)
        )
    )

print(f"Result: {safety_factor}")
