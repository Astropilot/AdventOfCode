from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    triangles = [line.rstrip("\n") for line in f]

valid_triangles = 0
i = 0
while i < len(triangles):
    l11, l12, l13 = [int(l) for l in triangles[i].split(" ") if len(l) > 0]
    l21, l22, l23 = [int(l) for l in triangles[i + 1].split(" ") if len(l) > 0]
    l31, l32, l33 = [int(l) for l in triangles[i + 2].split(" ") if len(l) > 0]

    if l11 + l21 > l31 and l21 + l31 > l11 and l31 + l11 > l21:
        valid_triangles += 1
    if l12 + l22 > l32 and l22 + l32 > l12 and l32 + l12 > l22:
        valid_triangles += 1
    if l13 + l23 > l33 and l23 + l33 > l13 and l33 + l13 > l23:
        valid_triangles += 1

    i += 3

print(f"Result: {valid_triangles}")
