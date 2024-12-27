from itertools import pairwise
from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    depths = [int(line.rstrip("\n")) for line in f]

increase_count = 0
for depth1, depth2 in pairwise(depths):
    if depth2 > depth1:
        increase_count += 1

print(f"Result: {increase_count}")
