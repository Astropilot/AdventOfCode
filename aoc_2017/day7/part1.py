from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    programs = [line.rstrip("\n") for line in f]

children: set[str] = set()

for program in programs:
    if "->" not in program:
        continue

    children_str = program.split(" -> ")[1]
    program_children = children_str.split(", ")

    for child in program_children:
        children.add(child)

for program in programs:
    if "->" not in program:
        continue

    name = program.split(" ")[0]

    if name not in children:
        print(f"Result: {name}")
        break
