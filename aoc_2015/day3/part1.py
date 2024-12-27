from pathlib import Path

directions = Path(Path(__file__).parent, "input").read_text()

DIRECTIONS_TO_DXY = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}
current_pos = (0, 0)
visited_pos: set[tuple[int, int]] = {current_pos}

for direction in directions:
    dx, dy = DIRECTIONS_TO_DXY[direction]
    current_pos = (current_pos[0] + dx, current_pos[1] + dy)
    visited_pos.add(current_pos)

print(f"Result: {len(visited_pos)}")
