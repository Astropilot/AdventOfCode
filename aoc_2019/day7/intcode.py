import typing as t
from enum import Enum

type OpCode = t.Literal[99, 1, 2, 3, 4, 5, 6, 7, 8, 9]


class ParameterMode(Enum):
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2


INSTRUCTIONS_ARITY: dict[OpCode, int] = {
    99: 0,  # Halt
    1: 3,  # Add
    2: 3,  # Mul
    3: 1,  # Input
    4: 1,  # Output
    5: 2,  # Jump-if-true
    6: 2,  # Jump-if-false
    7: 3,  # Less than
    8: 3,  # Equals
    9: 1,  # Relative base
}


def parse_instruction(
    n: int,
) -> tuple[OpCode, list[ParameterMode]]:
    opcode = n % 100
    n = n // 100

    if opcode not in INSTRUCTIONS_ARITY:
        raise ValueError(f"[ERROR] Unknown opcode: {opcode}")

    args: list[ParameterMode] = []

    for _ in range(INSTRUCTIONS_ARITY[opcode]):  # type: ignore
        args.append(ParameterMode(n % 10))
        n = n // 10

    return (opcode, args)  # type: ignore


def allocate_memory(intcode: list[int], idx: int) -> None:
    if 0 <= idx < len(intcode):
        return
    size = (idx + 1) - len(intcode)

    intcode.extend([0] * size)


def read_value(
    intcode: list[int], idx: int, mode: ParameterMode, relative_base: int
) -> int:
    allocate_memory(intcode, idx)
    address = intcode[idx]

    if mode == ParameterMode.IMMEDIATE:
        return address
    elif mode == ParameterMode.POSITION:
        allocate_memory(intcode, address)
        return intcode[address]
    elif mode == ParameterMode.RELATIVE:
        allocate_memory(intcode, relative_base + address)
        return intcode[relative_base + address]


def write_value(
    intcode: list[int], idx: int, value: int, mode: ParameterMode, relative_base: int
) -> None:
    if mode == ParameterMode.IMMEDIATE:
        raise ValueError("Mode cannot be immediate for writing in memory")

    allocate_memory(intcode, idx)
    address = intcode[idx]

    if mode == ParameterMode.POSITION:
        allocate_memory(intcode, address)
        intcode[address] = value
    elif mode == ParameterMode.RELATIVE:
        allocate_memory(intcode, relative_base + address)
        intcode[relative_base + address] = value


def execute_intcode(intcode: list[int], inputs: list[int]) -> list[int]:
    ip = 0
    relative_base = 0
    output: list[int] = []

    while True:
        instruction = parse_instruction(intcode[ip])
        match instruction:
            case (99, []):  # Halt
                break
            case (1, [mode1, mode2, mode3]):  # Add
                write_value(
                    intcode,
                    ip + 3,
                    read_value(intcode, ip + 1, mode1, relative_base)
                    + read_value(intcode, ip + 2, mode2, relative_base),
                    mode3,
                    relative_base,
                )
                ip += 4
            case (2, [mode1, mode2, mode3]):  # Mul
                write_value(
                    intcode,
                    ip + 3,
                    read_value(intcode, ip + 1, mode1, relative_base)
                    * read_value(intcode, ip + 2, mode2, relative_base),
                    mode3,
                    relative_base,
                )
                ip += 4
            case (3, [mode1]):  # Input
                write_value(intcode, ip + 1, inputs.pop(0), mode1, relative_base)
                ip += 2
            case (4, [mode1]):  # Output
                output.append(read_value(intcode, ip + 1, mode1, relative_base))
                ip += 2
            case (5, [mode1, mode2]):  # Jump-if-true
                if read_value(intcode, ip + 1, mode1, relative_base) != 0:
                    ip = read_value(intcode, ip + 2, mode2, relative_base)
                else:
                    ip += 3
            case (6, [mode1, mode2]):  # Jump-if-false
                if read_value(intcode, ip + 1, mode1, relative_base) == 0:
                    ip = read_value(intcode, ip + 2, mode2, relative_base)
                else:
                    ip += 3
            case (7, [mode1, mode2, mode3]):  # Less than
                if read_value(intcode, ip + 1, mode1, relative_base) < read_value(
                    intcode, ip + 2, mode2, relative_base
                ):
                    write_value(intcode, ip + 3, 1, mode3, relative_base)
                else:
                    write_value(intcode, ip + 3, 0, mode3, relative_base)
                ip += 4
            case (8, [mode1, mode2, mode3]):  # Equals
                if read_value(intcode, ip + 1, mode1, relative_base) == read_value(
                    intcode, ip + 2, mode2, relative_base
                ):
                    write_value(intcode, ip + 3, 1, mode3, relative_base)
                else:
                    write_value(intcode, ip + 3, 0, mode3, relative_base)
                ip += 4
            case (9, [mode1]):  # Relative
                relative_base += read_value(intcode, ip + 1, mode1, relative_base)
                ip += 2
            case _:
                raise ValueError(f"Unknown instruction: {instruction}")

    return output
