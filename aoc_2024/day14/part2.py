import re
from dataclasses import dataclass
from itertools import pairwise
from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]


@dataclass
class Robot:
    x: int
    y: int
    v_x: int
    v_y: int


width = 101  # 11 for sample
height = 103  # 7 for sample
robots: list[Robot] = []


def manhattan(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x2 - x1) + abs(y2 - y1)


for line in lines:
    m = re.match(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", line)

    assert m is not None

    r_x, r_y, v_x, v_y = list(map(int, m.groups()))

    robots.append(Robot(r_x, r_y, v_x, v_y))

min_i = -1
min_dis = 9999999999

for i in range(1, width * height + 1):
    for robot in robots:
        robot.x = (robot.x + robot.v_x) % width
        robot.y = (robot.y + robot.v_y) % height

    d = 0
    for r1, r2 in pairwise(robots):
        d += manhattan(r1.x, r1.y, r2.x, r2.y)

    if d < min_dis:
        min_dis = d
        min_i = i

print(f"Result: {min_i}")  # Result: 8087
