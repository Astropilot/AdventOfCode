import operator
import typing as t
from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    instructions = [line.rstrip("\n") for line in f]

registers: dict[str, int] = {}
CMP_FUNCS: dict[str, t.Callable[[int, int], bool]] = {
    "<": operator.lt,
    "<=": operator.le,
    ">": operator.gt,
    ">=": operator.ge,
    "==": operator.eq,
    "!=": operator.ne,
}
max_register_value = 0

for instruction in instructions:
    reg_out, operation, n, _, cmp_reg, cmp_op, cmp_n = instruction.split(" ")

    reg_out_value = registers.setdefault(reg_out, 0)
    cmp_reg_value = registers.setdefault(cmp_reg, 0)

    if CMP_FUNCS[cmp_op](cmp_reg_value, int(cmp_n)):
        if operation == "inc":
            registers[reg_out] = reg_out_value + int(n)
        elif operation == "dec":
            registers[reg_out] = reg_out_value - int(n)

    max_register_value = max(max_register_value, *registers.values())

print(f"Result: {max_register_value}")
