from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]


def program_output(modified_opcode: str, i_modified: int) -> int | None:
    visited: set[int] = set()
    accumulator = 0
    ip = 0

    while ip < len(lines):
        if ip in visited:
            return None
        visited.add(ip)

        opcode, arg = lines[ip].split(" ")
        arg_num = int(arg)

        if ip == i_modified:
            opcode = modified_opcode

        if opcode == "acc":
            accumulator += arg_num
            ip += 1
        elif opcode == "jmp":
            ip += arg_num
        else:
            ip += 1

    return accumulator


all_jmps = [i for i in range(len(lines)) if lines[i].startswith("jmp")]

for jmp_i in all_jmps:
    r = program_output("nop", jmp_i)
    if r is not None:
        print(f"Result: {r}")

all_nops = [i for i in range(len(lines)) if lines[i].startswith("jmp")]

for nop_i in all_nops:
    r = program_output("jmp", nop_i)
    if r is not None:
        print(f"Result: {r}")
