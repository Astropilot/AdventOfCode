from pathlib import Path


def read_value(intcode: list[int], idx: int) -> int:
    return intcode[idx]


def write_value(intcode: list[int], idx: int, value: int) -> None:
    intcode[idx] = value


intcode_ori = [
    int(c) for c in Path(Path(__file__).parent, "input").read_text().split(",")
]


def execute_intcode(intcode: list[int]) -> None:
    ip = 0

    while True:
        match intcode[ip]:
            case 99:
                break
            case 1:
                write_value(
                    intcode,
                    read_value(intcode, ip + 3),
                    read_value(intcode, read_value(intcode, ip + 1))
                    + read_value(intcode, read_value(intcode, ip + 2)),
                )
            case 2:
                write_value(
                    intcode,
                    read_value(intcode, ip + 3),
                    read_value(intcode, read_value(intcode, ip + 1))
                    * read_value(intcode, read_value(intcode, ip + 2)),
                )
            case _:
                raise ValueError(f"Unknown opcode: {intcode[ip]}")

        ip += 4


for noun in range(0, 100):
    f = False
    for verb in range(0, 100):
        intcode = intcode_ori.copy()
        intcode[1] = noun
        intcode[2] = verb
        execute_intcode(intcode)

        if intcode[0] == 19690720:
            print(f"Result: {100 * noun + verb}")
            f = True
            break
    if f:
        break
