import typing as t
from pathlib import Path

type ParameterMode = t.Literal["position", "immediate"]


def read_value(intcode: list[int], idx: int, mode: ParameterMode) -> int:
    address = intcode[idx]

    if mode == "immediate":
        return address
    elif mode == "position":
        return intcode[address]


def write_value(intcode: list[int], idx: int, value: int) -> None:
    intcode[idx] = value


def extract_instruction(
    n: int,
) -> tuple[int, ParameterMode, ParameterMode, ParameterMode]:
    int_to_param: list[ParameterMode] = ["position", "immediate"]
    opcode = n % 100
    n = n // 100
    first_mode = n % 10
    n = n // 10
    second_mode = n % 10
    n = n // 10
    third_mode = n % 10

    return (
        opcode,
        int_to_param[first_mode],
        int_to_param[second_mode],
        int_to_param[third_mode],
    )


def execute_intcode(intcode: list[int], input_cb: t.Callable[[], int]) -> list[int]:
    ip = 0
    output: list[int] = []

    while True:
        instruction = extract_instruction(intcode[ip])
        match instruction:
            case (99, _, _, _):
                break
            case (1, mode1, mode2, mode3):
                if mode3 == "immediate":
                    raise ValueError(
                        "Cannot accept output argument to be in immediate mode!"
                    )

                write_value(
                    intcode,
                    read_value(intcode, ip + 3, "immediate"),
                    read_value(intcode, ip + 1, mode1)
                    + read_value(intcode, ip + 2, mode2),
                )
                ip += 4
            case (2, mode1, mode2, mode3):
                if mode3 == "immediate":
                    raise ValueError(
                        "Cannot accept output argument to be in immediate mode!"
                    )

                write_value(
                    intcode,
                    read_value(intcode, ip + 3, "immediate"),
                    read_value(intcode, ip + 1, mode1)
                    * read_value(intcode, ip + 2, mode2),
                )
                ip += 4
            case (3, mode1, _, _):
                if mode1 == "immediate":
                    raise ValueError(
                        "Cannot accept output argument to be in immediate mode!"
                    )

                write_value(
                    intcode, read_value(intcode, ip + 1, "immediate"), input_cb()
                )
                ip += 2
            case (4, mode1, _, _):
                output.append(read_value(intcode, ip + 1, mode1))
                ip += 2
            case _:
                raise ValueError(f"Unknown opcode: {intcode[ip]}")

    return output


intcode_ori = [
    int(c) for c in Path(Path(__file__).parent, "input").read_text().split(",")
]
intcode = intcode_ori.copy()
output = execute_intcode(intcode, lambda: 1)

print(f"Result: {output}")
