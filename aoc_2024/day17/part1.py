from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

ra = int(lines[0].removeprefix("Register A: "))
rb = int(lines[1].removeprefix("Register B: "))
rc = int(lines[2].removeprefix("Register C: "))
ip = 0
output: list[int] = []

program = list(map(int, lines[4].removeprefix("Program: ").split(",")))
DEBUG = False


def resolve_operand_combo(operand: int, ra: int, rb: int, rc: int) -> int:
    match operand:
        case 0 | 1 | 2 | 3:
            return operand
        case 4:
            return ra
        case 5:
            return rb
        case 6:
            return rc
        case _:
            raise ValueError(f"Unauthorized operand: {operand}")


def operand_combo_tostr(operand: int) -> str:
    match operand:
        case 0 | 1 | 2 | 3:
            return str(operand)
        case 4:
            return "A"
        case 5:
            return "B"
        case 6:
            return "C"
        case _:
            raise ValueError(f"Unauthorized operand: {operand}")


while ip <= len(program) - 2:
    opcode = program[ip]
    operand = program[ip + 1]

    match opcode:
        case 0:
            if DEBUG:
                print(f"A = A // (2 ** {operand_combo_tostr(operand)})")
                print(
                    f"\tA = {ra} // (2 ** {resolve_operand_combo(operand, ra, rb, rc)})"
                )
            ra = ra // (2 ** resolve_operand_combo(operand, ra, rb, rc))
            ip += 2
        case 1:
            if DEBUG:
                print(f"B = B ^ {operand}")
                print(f"\tB = {rb} ^ {operand}")
            rb = rb ^ operand
            ip += 2
        case 2:
            if DEBUG:
                print(f"B = {operand_combo_tostr(operand)} % 8")
                print(f"\tB = {resolve_operand_combo(operand, ra, rb, rc)} % 8")
            rb = resolve_operand_combo(operand, ra, rb, rc) % 8
            ip += 2
        case 3:
            if ra == 0:
                if DEBUG:
                    print("ip += 2")
                ip += 2
            else:
                if DEBUG:
                    print(f"ip = {operand}")
                ip = operand
        case 4:
            if DEBUG:
                print("B = B ^ C")
                print(f"\tB = {rb} ^ {rc}")
            rb = rb ^ rc
            ip += 2
        case 5:
            if DEBUG:
                print(f"out {operand_combo_tostr(operand)} % 8")
                print(f"\tout {resolve_operand_combo(operand, ra, rb, rc)} % 8")
            v = resolve_operand_combo(operand, ra, rb, rc) % 8
            output.append(v)
            ip += 2
        case 6:
            if DEBUG:
                print(f"B = A // (2 ** {operand_combo_tostr(operand)})")
                print(
                    f"\tB = {ra} // (2 ** {resolve_operand_combo(operand, ra, rb, rc)})"
                )
            rb = ra // (2 ** resolve_operand_combo(operand, ra, rb, rc))
            ip += 2
        case 7:
            if DEBUG:
                print(f"C = A // (2 ** {operand_combo_tostr(operand)})")
                print(
                    f"\tC = {ra} // (2 ** {resolve_operand_combo(operand, ra, rb, rc)})"
                )
            rc = ra // (2 ** resolve_operand_combo(operand, ra, rb, rc))
            ip += 2
        case _:
            raise ValueError(f"Illegal opcode: {opcode}")


print(f"Result: {','.join(map(str, output))}")
