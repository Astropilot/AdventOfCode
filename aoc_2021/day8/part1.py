from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

total_digits = 0
for entry in lines:
    output = entry.split(" | ")[1].split(" ")

    for digit in output:
        if len(digit) in (2, 4, 3, 7):
            total_digits += 1

print(f"Result: {total_digits}")  # Result: 470
