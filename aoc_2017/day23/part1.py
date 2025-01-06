from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    instructions = [line.rstrip("\n") for line in f]

registers: dict[str, int] = {}
ip = 0
mul_count = 0


def resolve_arg(arg: str) -> int:
    global registers

    if arg.removeprefix("-").isdigit():
        return int(arg)

    return registers.setdefault(arg, 0)


while ip < len(instructions):
    instruction = instructions[ip]

    match instruction.split(" "):
        case ["set", X, Y]:
            registers[X] = resolve_arg(Y)
        case ["sub", X, Y]:
            registers[X] = resolve_arg(X) - resolve_arg(Y)
        case ["mul", X, Y]:
            registers[X] = resolve_arg(X) * resolve_arg(Y)
            mul_count += 1
        case ["jnz", X, Y]:
            if resolve_arg(X) != 0:
                ip += resolve_arg(Y)
                continue
        case _:
            raise ValueError(f"Unknown instruction: {instruction}")

    ip += 1

print(f"Result: {mul_count}")
