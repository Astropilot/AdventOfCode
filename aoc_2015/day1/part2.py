from pathlib import Path

contents = Path(Path(__file__).parent, "input").read_text()

floor = 0
i_basement = 0
for i, c in enumerate(contents, 1):
    if c == "(":
        floor += 1
    elif c == ")":
        floor -= 1

    if floor == -1:
        i_basement = i
        break

print(f"Result: {i_basement}")
