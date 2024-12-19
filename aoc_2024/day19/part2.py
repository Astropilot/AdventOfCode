from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

patterns: set[str] = set(lines[0].split(", "))
designs: list[str] = []

for line in lines[2:]:
    designs.append(line)


def count_design_arrangements(
    design: str, i: int, patterns: set[str], memory: dict[int, int]
) -> int:
    if i in memory:
        return memory[i]

    if i >= len(design):
        memory[i] = 1
        return 1

    arrangements = 0
    for pattern in patterns:
        if design[i:].startswith(pattern):
            arrangements += count_design_arrangements(
                design, i + len(pattern), patterns, memory
            )

    memory[i] = arrangements
    return arrangements


total_designs_arrangements = 0
for design in designs:
    memory: dict[int, int] = {}
    total_designs_arrangements += count_design_arrangements(design, 0, patterns, memory)

print(f"Result: {total_designs_arrangements}")  # Result: 712058625427487
