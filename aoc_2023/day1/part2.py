from pathlib import Path

contents = Path(Path(__file__).parent, "input").read_text()


def transform_spelling(line: str) -> list[int]:
    spellings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    numbers: list[int] = []

    for i in range(len(line)):
        for j in range(len(spellings)):
            if line[i:].startswith(spellings[j]):
                numbers.append(j + 1)
                break
        if line[i].isdigit():
            numbers.append(int(line[i]))

    return numbers


sum_calib = 0
for line in contents.split("\n"):
    numbers = transform_spelling(line)
    sum_calib += (numbers[0] * 10) + numbers[-1]

print(f"Result: {sum_calib}")
