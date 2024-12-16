from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    contents = f.read()

i_marker = -1
for i in range(4, len(contents), 1):
    if len(set(contents[i - 4 : i])) == len(contents[i - 4 : i]):
        i_marker = i
        break

print(f"Result: {i_marker}")  # Result: 1275
