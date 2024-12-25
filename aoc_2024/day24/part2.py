import operator
import typing as t
from dataclasses import dataclass
from pathlib import Path

# System reference used: https://www.101computing.net/binary-additions-using-logic-gates/


@dataclass(unsafe_hash=True)
class LogicalGate:
    in_a: str
    in_b: str
    out: str
    op: t.Literal["AND", "XOR", "OR"]


OPERATORS: dict[t.Literal["AND", "XOR", "OR"], t.Callable[[int, int], int]] = {
    "AND": operator.and_,
    "OR": operator.or_,
    "XOR": operator.xor,
}


def find_end_wire(wire: str, gates: list[LogicalGate]) -> str | None:
    gates_to_search: list[LogicalGate] = []

    for gate in gates:
        if gate.in_a == wire or gate.in_b == wire:
            if gate.out[0] == "z":
                z_n = int(gate.out[1:])
                return f"z{z_n-1:>02}"
            else:
                gates_to_search.append(gate)

    for gate in gates_to_search:
        end_wire = find_end_wire(gate.out, gates)
        if end_wire is not None:
            return end_wire
    return None


def run_adder(wires: dict[str, int], gates: list[LogicalGate]) -> None:
    gate_visited: set[LogicalGate] = set()

    while len(gate_visited) < len(gates):
        new_gates: list[LogicalGate] = []
        for gate in gates:
            if gate not in gate_visited and not any(
                (gate.in_a == g.out or gate.in_b == g.out) and g not in gate_visited
                for g in gates
            ):
                new_gates.append(gate)
        for gate in new_gates:
            wires[gate.out] = OPERATORS[gate.op](wires[gate.in_a], wires[gate.in_b])
            gate_visited.add(gate)


with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

separator = lines.index("")
gates: list[LogicalGate] = []
ori_gates: list[LogicalGate] = []
wires: dict[str, int] = {}

for line in lines[:separator]:
    name, value = line.split(": ")
    wires[name] = int(value)

for line in lines[separator + 1 :]:
    gate_raw, output = line.split(" -> ")
    in_a, op, in_b = gate_raw.split(" ")
    gates.append(LogicalGate(in_a, in_b, output, op))  # type: ignore
    ori_gates.append(LogicalGate(in_a, in_b, output, op))  # type: ignore

x = 0
y = 0
ori_wires = wires.copy()

for wire, v in wires.items():
    if wire[0] == "x" and v == 1:
        x += 2 ** int(wire[1:])
    elif wire[0] == "y" and v == 1:
        y += 2 ** int(wire[1:])

wanted_output = x + y

wrong_gates_to_z: list[LogicalGate] = []
wrong_xor_xy_gates: list[LogicalGate] = []
output_to_swap: list[str] = []

for gate in gates:
    if gate.out[0] == "z" and gate.out != "z45":
        if gate.op != "XOR":
            wrong_gates_to_z.append(gate)
            output_to_swap.append(gate.out)
    elif gate.in_a[0] not in ("x", "y") or gate.in_b[0] not in ("x", "y"):
        if gate.op == "XOR":
            wrong_xor_xy_gates.append(gate)
            output_to_swap.append(gate.out)

for gate in wrong_xor_xy_gates:
    wire_end = find_end_wire(gate.out, gates)

    for badgate in wrong_gates_to_z:
        if badgate.out == wire_end:
            badgate.out = gate.out
            gate.out = wire_end
            break

run_adder(wires, gates)

bad_z = 0
for wire, v in [(w, v) for w, v in wires.items() if w[0] == "z"]:
    if v == 1:
        bad_z += 2 ** int(wire[1:])


xor_good_bad = bad_z ^ wanted_output
xor_bin = f"{xor_good_bad:>046b}"[::-1]

bad_carry_idx = 0
for i in range(len(xor_bin) - 1, -1, -1):
    if xor_bin[i] == "1":
        bad_carry_idx = i
        break

bad_or_gate: LogicalGate | None = None

for gate in gates:
    if gate.in_a == f"x{bad_carry_idx:>02}" or gate.in_a == f"y{bad_carry_idx:>02}":
        if bad_or_gate is None:
            bad_or_gate = gate
        else:
            output_to_swap.append(bad_or_gate.out)
            output_to_swap.append(gate.out)
            out = bad_or_gate.out
            bad_or_gate.out = gate.out
            gate.out = out
            break

print(f"Result: {",".join(sorted(output_to_swap))}")
