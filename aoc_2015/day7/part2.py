import typing as t
from dataclasses import dataclass
from functools import cache
from pathlib import Path


@dataclass(frozen=True)
class Instruction:
    operator: t.Literal["ASSIGN", "AND", "LSHIFT", "NOT", "OR", "RSHIFT"]
    in_a: int | str
    in_b: int | str
    output: str


INSTRUCTION_PER_OUTPUT: dict[str, Instruction] = {}

with Path(Path(__file__).parent, "input").open() as f:
    instructions = [line.rstrip("\n") for line in f]

for instruction in instructions:
    inst, output = instruction.split(" -> ")

    if inst.startswith("NOT"):
        INSTRUCTION_PER_OUTPUT[output] = Instruction(
            "NOT", inst.removeprefix("NOT "), "", output
        )
    elif inst.count(" ") == 0:
        INSTRUCTION_PER_OUTPUT[output] = Instruction(
            "ASSIGN", int(inst) if inst.isdigit() else inst, "", output
        )
    else:
        in_a_raw, operator, in_b_raw = inst.split(" ")
        if in_a_raw.isdigit():
            in_a: int | str = int(in_a_raw)
        else:
            in_a = in_a_raw
        if in_b_raw.isdigit():
            in_b: int | str = int(in_b_raw)
        else:
            in_b = in_b_raw
        if operator == "AND":
            INSTRUCTION_PER_OUTPUT[output] = Instruction("AND", in_a, in_b, output)
        elif operator == "OR":
            INSTRUCTION_PER_OUTPUT[output] = Instruction("OR", in_a, in_b, output)
        elif operator == "LSHIFT":
            INSTRUCTION_PER_OUTPUT[output] = Instruction("LSHIFT", in_a, in_b, output)
        elif operator == "RSHIFT":
            INSTRUCTION_PER_OUTPUT[output] = Instruction("RSHIFT", in_a, in_b, output)


@cache
def get_wire_value(wire: str) -> int:
    instruction = INSTRUCTION_PER_OUTPUT[wire]

    if instruction.operator == "ASSIGN":
        return (
            get_wire_value(instruction.in_a)
            if isinstance(instruction.in_a, str)
            else instruction.in_a
        )

    in_a = 0
    in_b = 0

    if instruction.in_a != "":
        in_a = (
            get_wire_value(instruction.in_a)
            if isinstance(instruction.in_a, str)
            else instruction.in_a
        )
    if instruction.in_b != "":
        in_b = (
            get_wire_value(instruction.in_b)
            if isinstance(instruction.in_b, str)
            else instruction.in_b
        )

    match instruction.operator:
        case "NOT":
            return (1 << 16) - 1 - in_a
        case "AND":
            return in_a & in_b
        case "OR":
            return in_a | in_b
        case "LSHIFT":
            return in_a << in_b
        case "RSHIFT":
            return in_a >> in_b
        case _:
            raise ValueError("unknown operator")


# Overriding wire b with result from part 1
# This is the only change from part 1 code
INSTRUCTION_PER_OUTPUT["b"] = Instruction("ASSIGN", 3176, "", "b")

print(f"Result: {get_wire_value('a')}")
