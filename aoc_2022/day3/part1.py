from pathlib import Path
from string import ascii_lowercase, ascii_uppercase

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

priority = {
    letter: priority
    for priority, letter in enumerate(ascii_lowercase + ascii_uppercase, 1)
}

total_priority = 0
for line in lines:
    middle_idx = len(line) // 2
    part1, part2 = set(line[:middle_idx]), set(line[middle_idx:])
    inter = next(iter(part1.intersection(part2)))

    total_priority += priority[inter]

print(f"Result: {total_priority}")
