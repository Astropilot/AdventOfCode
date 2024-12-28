from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    triangles = [line.rstrip("\n") for line in f]

valid_triangles = 0
for triangle in triangles:
    l1, l2, l3 = [int(l) for l in triangle.split(" ") if len(l) > 0]

    if l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2:
        valid_triangles += 1

print(f"Result: {valid_triangles}")
