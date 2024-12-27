from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

MATCHING: dict[str, str] = {"(": ")", "[": "]", "{": "}", "<": ">"}
POINTS: dict[str, int] = {")": 3, "]": 57, "}": 1197, ">": 25137}

total_points = 0
for line in lines:
    stack: list[str] = []

    for c in line:
        if c in MATCHING:
            stack.append(c)
            continue
        opening = stack[-1]
        if c != MATCHING[opening]:
            total_points += POINTS[c]
            break
        stack.pop()

print(f"Result: {total_points}")
