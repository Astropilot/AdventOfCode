from pathlib import Path

contents = Path(Path(__file__).parent, "input").read_text()
lines = contents.split("\n")

sum_loads = 0
for col in range(len(lines[0])):
    next_available_i = 0
    for i in range(len(lines)):
        if lines[i][col] == "O":
            sum_loads += len(lines) - next_available_i
            next_available_i += 1
        elif lines[i][col] == "#":
            next_available_i = i + 1

print(f"Result {sum_loads}")
