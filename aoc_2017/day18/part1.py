from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    instructions = [line.rstrip("\n") for line in f]

registers: dict[str, int] = {}
last_frequency: int | None = None
ip = 0


def resolve_arg(arg: str) -> int:
    global registers

    if arg.removeprefix("-").isdigit():
        return int(arg)

    return registers.setdefault(arg, 0)


while ip < len(instructions):
    instruction = instructions[ip]

    match instruction.split(" "):
        case ["snd", X]:
            last_frequency = resolve_arg(X)
        case ["set", X, Y]:
            registers[X] = resolve_arg(Y)
        case ["add", X, Y]:
            registers[X] = resolve_arg(X) + resolve_arg(Y)
        case ["mul", X, Y]:
            registers[X] = resolve_arg(X) * resolve_arg(Y)
        case ["mod", X, Y]:
            registers[X] = resolve_arg(X) % resolve_arg(Y)
        case ["rcv", X]:
            if resolve_arg(X) != 0:
                print(f"Result: {last_frequency}")
                break
        case ["jgz", X, Y]:
            if resolve_arg(X) > 0:
                ip += resolve_arg(Y)
                continue
        case _:
            raise ValueError(f"Unknown instruction: {instruction}")

    ip += 1