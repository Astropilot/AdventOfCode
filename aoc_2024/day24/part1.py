import operator
import typing as t
from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

separator = lines.index("")

wires: dict[str, int] = {}
dependencies: dict[str, tuple[str, str, str]] = {}
operators: dict[str, t.Callable[[int, int], int]] = {
    "AND": operator.and_,
    "OR": operator.or_,
    "XOR": operator.xor,
}

for line in lines[:separator]:
    name, value = line.split(": ")
    wires[name] = int(value)

for line in lines[separator + 1 :]:
    gate, wire = line.split(" -> ")
    left_op, op, right_op = gate.split(" ")
    dependencies[wire] = (op, left_op, right_op)


def rec_resolve_wire(name: str) -> None:
    if name in wires:
        return

    gate_info = dependencies[name]

    if gate_info[1] not in wires:
        rec_resolve_wire(gate_info[1])
    if gate_info[2] not in wires:
        rec_resolve_wire(gate_info[2])

    wires[name] = operators[gate_info[0]](wires[gate_info[1]], wires[gate_info[2]])


for z_signal in [w for w in dependencies if w[0] == "z"]:
    if z_signal in wires:
        continue
    gate_info = dependencies[z_signal]
    if gate_info[1] not in wires:
        rec_resolve_wire(gate_info[1])
    if gate_info[2] not in wires:
        rec_resolve_wire(gate_info[2])
    wires[z_signal] = operators[gate_info[0]](wires[gate_info[1]], wires[gate_info[2]])

z_number = ""
for w in sorted([w for w in wires.keys() if w[0] == "z"], reverse=True):
    z_number += str(wires[w])

print(f"Result: {int(z_number, 2)}")
