from itertools import pairwise
from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    depths = [int(line.rstrip("\n")) for line in f]

increase_count = 0
windows: list[int] = []

for i in range(0, len(depths) - 2, 1):
    windows.append(depths[i] + depths[i + 1] + depths[i + 2])

for window1, window2 in pairwise(windows):
    if window2 > window1:
        increase_count += 1

print(f"Result: {increase_count}")  # Result: 1262
