from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]


def check_equation(numbers: tuple[int, ...], test: int, i: int, count: int) -> bool:
    if count > test:
        return False
    if i == len(numbers):
        return test == count

    count_plus = count + numbers[i]
    if check_equation(numbers, test, i + 1, count_plus):
        return True

    count_mul = count * numbers[i]
    if check_equation(numbers, test, i + 1, count_mul):
        return True

    count_conc = int(str(count) + str(numbers[i]))
    if check_equation(numbers, test, i + 1, count_conc):
        return True

    return False


total_test = 0
for line in lines:
    test_raw, equation_raw = line.split(": ")
    test = int(test_raw)
    equation_nbs = tuple(int(n) for n in equation_raw.split(" "))

    if check_equation(equation_nbs, test, 1, equation_nbs[0]):
        total_test += test

print(f"Result: {total_test}")
