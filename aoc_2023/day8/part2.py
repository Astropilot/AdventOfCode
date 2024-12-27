import re
from math import lcm
from pathlib import Path

contents = Path(Path(__file__).parent, "input").read_text()
lines = contents.split("\n")

instructions = [0 if d == "L" else 1 for d in lines[0].strip()]
mapping: dict[str, list[str]] = {}

for line in lines[2:]:
    m = re.match(r"([A-Z0-9]{3}) = \(([A-Z0-9]{3}), ([A-Z0-9]{3})\)", line)
    assert m is not None, "Cannot match mapping line!"

    mapping[m.group(1)] = [m.group(2), m.group(3)]

starting_nodes = list(filter(lambda n: n[2] == "A", mapping.keys()))
steps_list: list[int] = []

print("starting_nodes", starting_nodes)

for node in starting_nodes:
    current_node = node
    steps = 0

    while current_node[2] != "Z":
        instruction = instructions[steps % len(instructions)]

        current_node = mapping[current_node][instruction]
        steps += 1

    print(f"Steps for node {node} to node {current_node}: {steps}")

    steps_list.append(steps)

total_steps = lcm(*steps_list)

print(f"Result: {total_steps}")
