from pathlib import Path
from string import ascii_lowercase, ascii_uppercase

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

priority = {
    letter: priority
    for priority, letter in enumerate(ascii_lowercase + ascii_uppercase, 1)
}

total_priority = 0
for i in range(0, len(lines), 3):
    first = set(lines[i])
    second = set(lines[i + 1])
    third = set(lines[i + 2])
    inter = first.intersection(second).intersection(third)

    total_priority += priority[next(iter(inter))]

print(f"Result: {total_priority}")  # Result: 2569
