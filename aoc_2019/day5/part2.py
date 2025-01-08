import typing as t
from enum import Enum
from pathlib import Path

type OpCode = t.Literal[99, 1, 2, 3, 4, 5, 6, 7, 8]


class ParameterMode(Enum):
    POSITION = 0
    IMMEDIATE = 1


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


def read_value(intcode: list[int], idx: int, mode: ParameterMode) -> int:
    address = intcode[idx]

    if mode == ParameterMode.IMMEDIATE:
        return address
    elif mode == ParameterMode.POSITION:
        return intcode[address]


def write_value(intcode: list[int], idx: int, value: int) -> None:
    intcode[idx] = value


def execute_intcode(intcode: list[int], input_cb: t.Callable[[], int]) -> list[int]:
    ip = 0
    output: list[int] = []

    while True:
        instruction = parse_instruction(intcode[ip])
        match instruction:
            case (99, []):  # Halt
                break
            case (1, [mode1, mode2, _]):  # Add
                write_value(
                    intcode,
                    read_value(intcode, ip + 3, ParameterMode.IMMEDIATE),
                    read_value(intcode, ip + 1, mode1)
                    + read_value(intcode, ip + 2, mode2),
                )
                ip += 4
            case (2, [mode1, mode2, _]):  # Mul
                write_value(
                    intcode,
                    read_value(intcode, ip + 3, ParameterMode.IMMEDIATE),
                    read_value(intcode, ip + 1, mode1)
                    * read_value(intcode, ip + 2, mode2),
                )
                ip += 4
            case (3, [_]):  # Input
                write_value(
                    intcode,
                    read_value(intcode, ip + 1, ParameterMode.IMMEDIATE),
                    input_cb(),
                )
                ip += 2
            case (4, [mode1]):  # Output
                output.append(read_value(intcode, ip + 1, mode1))
                ip += 2
            case (5, [mode1, mode2]):  # Jump-if-true
                if read_value(intcode, ip + 1, mode1) != 0:
                    ip = read_value(intcode, ip + 2, mode2)
                else:
                    ip += 3
            case (6, [mode1, mode2]):  # Jump-if-false
                if read_value(intcode, ip + 1, mode1) == 0:
                    ip = read_value(intcode, ip + 2, mode2)
                else:
                    ip += 3
            case (7, [mode1, mode2, _]):  # Less than
                if read_value(intcode, ip + 1, mode1) < read_value(
                    intcode, ip + 2, mode2
                ):
                    write_value(
                        intcode, read_value(intcode, ip + 3, ParameterMode.IMMEDIATE), 1
                    )
                else:
                    write_value(
                        intcode, read_value(intcode, ip + 3, ParameterMode.IMMEDIATE), 0
                    )
                ip += 4
            case (8, [mode1, mode2, _]):  # Equals
                if read_value(intcode, ip + 1, mode1) == read_value(
                    intcode, ip + 2, mode2
                ):
                    write_value(
                        intcode, read_value(intcode, ip + 3, ParameterMode.IMMEDIATE), 1
                    )
                else:
                    write_value(
                        intcode, read_value(intcode, ip + 3, ParameterMode.IMMEDIATE), 0
                    )
                ip += 4
            case _:
                raise ValueError(f"Unknown instruction: {instruction}")

    return output


intcode_ori = [
    int(c) for c in Path(Path(__file__).parent, "input").read_text().split(",")
]
intcode = intcode_ori.copy()
output = execute_intcode(intcode, lambda: 5)

print(f"Result: {output}")
