from pathlib import Path


def resolve_arg(arg: str, registers: dict[str, int]) -> int:
    if arg.removeprefix("-").isdigit():
        return int(arg)

    return registers.setdefault(arg, 0)


with Path(Path(__file__).parent, "input").open() as f:
    instructions = [line.rstrip("\n") for line in f]

registers_0: dict[str, int] = {"p": 0}
registers_1: dict[str, int] = {"p": 1}
queue_0_1: list[int] = []
queue_1_0: list[int] = []
ip_0 = 0
ip_1 = 0
send_1_counter = 0


def execute_program_till_endorwait(
    registers: dict[str, int], q_recv: list[int], q_send: list[int], ip: int, id: int
) -> tuple[bool, int]:
    global send_1_counter

    while ip < len(instructions):
        instruction = instructions[ip]

        match instruction.split(" "):
            case ["snd", X]:
                q_send.append(resolve_arg(X, registers))
                if id == 1:
                    send_1_counter += 1
            case ["set", X, Y]:
                registers[X] = resolve_arg(Y, registers)
            case ["add", X, Y]:
                registers[X] = resolve_arg(X, registers) + resolve_arg(Y, registers)
            case ["mul", X, Y]:
                registers[X] = resolve_arg(X, registers) * resolve_arg(Y, registers)
            case ["mod", X, Y]:
                registers[X] = resolve_arg(X, registers) % resolve_arg(Y, registers)
            case ["rcv", X]:
                if len(q_recv) == 0:
                    return (True, ip)
                registers[X] = q_recv.pop(0)
            case ["jgz", X, Y]:
                if resolve_arg(X, registers) > 0:
                    ip += resolve_arg(Y, registers)
                    continue
            case _:
                raise ValueError(f"Unknown instruction: {instruction}")

        ip += 1

    return (False, ip)


waiting = 0
while True:
    waiting_0, ip_0 = execute_program_till_endorwait(
        registers_0, queue_1_0, queue_0_1, ip_0, 0
    )
    waiting_1, ip_1 = execute_program_till_endorwait(
        registers_1, queue_0_1, queue_1_0, ip_1, 1
    )

    if not waiting_0 and waiting_1:
        break
    if len(queue_0_1) == 0 and len(queue_1_0) == 0:
        break

print(f"Result: {send_1_counter}")
