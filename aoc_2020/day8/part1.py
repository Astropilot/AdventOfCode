from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

visited: set[int] = set()
accumulator = 0
ip = 0

while ip < len(lines):
    if ip in visited:
        break
    visited.add(ip)

    opcode, arg = lines[ip].split(" ")
    arg_num = int(arg)

    if opcode == "acc":
        accumulator += arg_num
        ip += 1
    elif opcode == "jmp":
        ip += arg_num
    else:
        ip += 1

print(f"Result: {accumulator}")
