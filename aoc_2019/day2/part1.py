from pathlib import Path


def read_value(intcode: list[int], idx: int) -> int:
    return intcode[idx]


def write_value(intcode: list[int], idx: int, value: int) -> None:
    intcode[idx] = value


intcode = [int(c) for c in Path(Path(__file__).parent, "input").read_text().split(",")]
ip = 0

intcode[1] = 12
intcode[2] = 2

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

print(f"Result: {intcode[0]}")
