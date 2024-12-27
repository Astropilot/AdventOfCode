import re
from pathlib import Path

contents = Path(Path(__file__).parent, "input").read_text()
lines = contents.split("\n")

instructions = [0 if d == "L" else 1 for d in lines[0].strip()]
mapping: dict[str, list[str]] = {}

for line in lines[2:]:
    m = re.match(r"([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)", line)
    assert m is not None, "Cannot match mapping line!"

    mapping[m.group(1)] = [m.group(2), m.group(3)]

current_node = "AAA"
steps = 0

while current_node != "ZZZ":
    instruction = instructions[steps % len(instructions)]

    current_node = mapping[current_node][instruction]
    steps += 1

print(f"Result: {steps}")
