import typing as t
from pathlib import Path


class CoordsT(t.NamedTuple):
    x: int
    y: int


with Path(Path(__file__).parent, "input").open() as f:
    rows = [line.rstrip("\n") for line in f]

direction_to_vec: dict[str, CoordsT] = {
    "U": CoordsT(0, -1),
    "D": CoordsT(0, 1),
    "L": CoordsT(-1, 0),
    "R": CoordsT(1, 0),
}
wire1_directions = rows[0].split(",")
wire2_directions = rows[1].split(",")
wire1_segments: set[tuple[CoordsT, CoordsT]] = set()
wire2_segments: set[tuple[CoordsT, CoordsT]] = set()

wire1_pos = CoordsT(0, 0)
for wire1_dir in wire1_directions:
    direction, amount = wire1_dir[0], int(wire1_dir[1:])
    dir_vec = direction_to_vec[direction]
    new_pos = CoordsT(
        wire1_pos.x + (dir_vec.x * amount), wire1_pos.y + (dir_vec.y * amount)
    )
    wire1_segments.add((wire1_pos, new_pos))
    wire1_pos = new_pos

wire2_pos = CoordsT(0, 0)
for wire2_dir in wire2_directions:
    direction, amount = wire2_dir[0], int(wire2_dir[1:])
    dir_vec = direction_to_vec[direction]
    new_pos = CoordsT(
        wire2_pos.x + (dir_vec.x * amount), wire2_pos.y + (dir_vec.y * amount)
    )
    wire2_segments.add((wire2_pos, new_pos))
    wire2_pos = new_pos


def intersection(
    segment1: tuple[CoordsT, CoordsT], segment2: tuple[CoordsT, CoordsT]
) -> CoordsT | None:
    x1, y1 = segment1[0]
    x2, y2 = segment1[1]
    x3, y3 = segment2[0]
    x4, y4 = segment2[1]
    denom = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
    if denom == 0:
        return None
    ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denom
    if ua < 0 or ua > 1:
        return None
    ub = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / denom
    if ub < 0 or ub > 1:
        return None
    x = int(x1 + ua * (x2 - x1))
    y = int(y1 + ua * (y2 - y1))
    return CoordsT(x, y)


intersections: set[CoordsT] = set()
for wire1_segment in wire1_segments:
    for wire2_segment in wire2_segments:
        p = intersection(wire1_segment, wire2_segment)
        if p:
            intersections.add(p)

if CoordsT(0, 0) in intersections:
    intersections.remove(CoordsT(0, 0))
nearest_intersection = sorted(intersections, key=lambda p: abs(p.x) + abs(p.y))[0]

print(f"Result: {abs(nearest_intersection.x) + abs(nearest_intersection.y)}")
