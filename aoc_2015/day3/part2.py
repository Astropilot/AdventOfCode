from pathlib import Path

directions = Path(Path(__file__).parent, "input").read_text()

DIRECTIONS_TO_DXY = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}
santa_pos = (0, 0)
robot_pos = (0, 0)
visited_pos: set[tuple[int, int]] = {santa_pos}

for i, direction in enumerate(directions):
    dx, dy = DIRECTIONS_TO_DXY[direction]

    if i % 2 == 0:
        santa_pos = (santa_pos[0] + dx, santa_pos[1] + dy)
        visited_pos.add(santa_pos)
    else:
        robot_pos = (robot_pos[0] + dx, robot_pos[1] + dy)
        visited_pos.add(robot_pos)

print(f"Result: {len(visited_pos)}")
