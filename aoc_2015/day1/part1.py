from pathlib import Path

contents = Path(Path(__file__).parent, "input").read_text()

floor = 0
for c in contents:
    if c == "(":
        floor += 1
    elif c == ")":
        floor -= 1

print(f"Result: {floor}")
