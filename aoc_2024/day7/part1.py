from itertools import product
from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

total_test = 0


for line in lines:
    test_raw, equation_raw = line.split(": ")
    test = int(test_raw)
    equation_nbs = [int(n) for n in equation_raw.split(" ")]
    count_operators = len(equation_nbs) - 1
    for operators_comb in product(["+", "*"], repeat=count_operators):
        result = equation_nbs[0]
        for i, operator in enumerate(operators_comb):
            if operator == "+":
                result += equation_nbs[i + 1]
            else:
                result *= equation_nbs[i + 1]
        if result == test:
            total_test += test
            break

print(f"Result: {total_test}")  # Result: 4122618559853
