import re
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Program:
    name: str
    weight: int
    parent: "Program | None"
    children: "list[Program]"


with Path(Path(__file__).parent, "input").open() as f:
    programs = [line.rstrip("\n") for line in f]

program_per_name: dict[str, Program] = {}

for program_str in programs:
    m = re.match(r"([a-z]+) \((\d+)\)(?: -> (.+))?", program_str)
    assert m is not None

    name = m.group(1)
    weight = int(m.group(2))
    children_str = m.group(3)
    if children_str is not None:
        children = children_str.split(", ")
    else:
        children = []

    children_program: list[Program] = []
    for child in children:
        if child in program_per_name:
            children_program.append(program_per_name[child])
        else:
            child_program = Program(child, 0, None, [])
            program_per_name[child] = child_program
            children_program.append(child_program)

    if name in program_per_name:
        program = program_per_name[name]
        program.weight = weight
        program.children = children_program
    else:
        program = Program(name, weight, None, children_program)
        program_per_name[name] = program

    for child in children_program:
        child.parent = program


root = next(p for p in program_per_name.values() if p.parent is None)


def find_wrong_program(program: Program) -> int:
    if len(program.children) == 0:
        return program.weight

    sum_weights = 0
    last_weight: int | None = None

    for child in program.children:
        w = find_wrong_program(child)

        if last_weight is not None and w != last_weight:
            diff = w - last_weight
            print(f"Result: {child.weight - diff}")
            w -= diff

        last_weight = w
        sum_weights += w

    return program.weight + sum_weights


find_wrong_program(root)
