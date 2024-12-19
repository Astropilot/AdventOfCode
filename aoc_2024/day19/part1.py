from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

patterns: set[str] = set(lines[0].split(", "))
designs: list[str] = []

for line in lines[2:]:
    designs.append(line)


def check_design(
    design: str, i: int, patterns: set[str], memory: dict[int, bool]
) -> bool:
    if i in memory:
        return memory[i]

    if i >= len(design):
        memory[i] = True
        return True

    for pattern in patterns:
        if design[i:].startswith(pattern) and check_design(
            design, i + len(pattern), patterns, memory
        ):
            memory[i] = True
            return True

    memory[i] = False
    return False


design_possibles = 0
for design in designs:
    memory: dict[int, bool] = {}
    if check_design(design, 0, patterns, memory):
        design_possibles += 1

print(f"Result: {design_possibles}")  # Result: 290
