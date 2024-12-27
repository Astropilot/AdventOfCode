from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

MATCHING: dict[str, str] = {"(": ")", "[": "]", "{": "}", "<": ">"}
POINTS: dict[str, int] = {")": 1, "]": 2, "}": 3, ">": 4}

scores: list[int] = []
for line in lines:
    stack: list[str] = []
    is_corrupted = False

    for c in line:
        if c in MATCHING:
            stack.append(c)
            continue
        opening = stack[-1]
        if c != MATCHING[opening]:
            is_corrupted = True
            break
        stack.pop()

    if is_corrupted:
        continue

    score = 0
    while len(stack) != 0:
        c = MATCHING[stack.pop()]
        score *= 5
        score += POINTS[c]

    scores.append(score)

scores.sort()

print(f"Result: {scores[len(scores)//2]}")
