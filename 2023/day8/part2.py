import re
from pathlib import Path

contents = Path(Path(__file__).parent, "input").read_text()
lines = contents.split("\n")

instructions = [0 if d == "L" else 1 for d in lines[0].strip()]
mapping: dict[str, list[str]] = {}

for line in lines[2:]:
    m = re.match(r"([A-Z0-9]{3}) = \(([A-Z0-9]{3}), ([A-Z0-9]{3})\)", line)
    assert m is not None, "Cannot match mapping line!"

    mapping[m.group(1)] = [m.group(2), m.group(3)]

current_nodes = list(filter(lambda n: n[2] == "A", mapping.keys()))
steps = 0

print("initial nodes", current_nodes)

while not all(n[2] == "Z" for n in current_nodes):
    instruction = instructions[steps % len(instructions)]

    current_nodes = [mapping[n][instruction] for n in current_nodes]
    steps += 1

    # print("current_nodes", current_nodes)

print(f"Result: {steps}")  # Result:
