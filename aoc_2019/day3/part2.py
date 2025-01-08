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
wire1_segments: set[tuple[CoordsT, CoordsT, int]] = set()
wire2_segments: set[tuple[CoordsT, CoordsT, int]] = set()

wire1_pos = CoordsT(0, 0)
steps = 0
for wire1_dir in wire1_directions:
    direction, amount = wire1_dir[0], int(wire1_dir[1:])
    dir_vec = direction_to_vec[direction]
    new_pos = CoordsT(
        wire1_pos.x + (dir_vec.x * amount), wire1_pos.y + (dir_vec.y * amount)
    )
    steps += amount
    wire1_segments.add((wire1_pos, new_pos, steps))
    wire1_pos = new_pos

wire2_pos = CoordsT(0, 0)
steps = 0
for wire2_dir in wire2_directions:
    direction, amount = wire2_dir[0], int(wire2_dir[1:])
    dir_vec = direction_to_vec[direction]
    new_pos = CoordsT(
        wire2_pos.x + (dir_vec.x * amount), wire2_pos.y + (dir_vec.y * amount)
    )
    steps += amount
    wire2_segments.add((wire2_pos, new_pos, steps))
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


def manhattan(p1: CoordsT, p2: CoordsT) -> int:
    return abs(p2.x - p1.x) + abs(p2.y - p1.y)


intersections: set[CoordsT] = set()
for wire1_segment in wire1_segments:
    for wire2_segment in wire2_segments:
        p = intersection(wire1_segment[:2], wire2_segment[:2])
        if p and p != CoordsT(0, 0):
            intersections.add(p)

distances: list[int] = []
for p in intersections:
    candidate_wire1 = sorted(
        [
            s
            for s in wire1_segments
            if (
                s[0].y == s[1].y
                and s[0].y == p.y
                and (s[0].x <= p.x <= s[1].x or s[1].x <= p.x <= s[0].x)
            )
            or (
                s[0].x == s[1].x
                and s[0].x == p.x
                and (s[0].y <= p.y <= s[1].y or s[1].y <= p.y <= s[0].y)
            )
        ],
        key=lambda s: s[2],
    )[0]
    candidate_wire2 = sorted(
        [
            s
            for s in wire2_segments
            if (
                s[0].y == s[1].y
                and s[0].y == p.y
                and (s[0].x <= p.x <= s[1].x or s[1].x <= p.x <= s[0].x)
            )
            or (
                s[0].x == s[1].x
                and s[0].x == p.x
                and (s[0].y <= p.y <= s[1].y or s[1].y <= p.y <= s[0].y)
            )
        ],
        key=lambda s: s[2],
    )[0]

    wire1_steps = candidate_wire1[2] - manhattan(p, candidate_wire1[1])
    wire2_steps = candidate_wire2[2] - manhattan(p, candidate_wire2[1])
    distances.append(wire1_steps + wire2_steps)

distances.sort()

print(f"Result: {distances[0]}")
