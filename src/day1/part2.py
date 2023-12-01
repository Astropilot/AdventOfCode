from pathlib import Path

contents = Path(Path(__file__).parent, "input").read_text()


def transform_spelling(line: str) -> list[int]:
    spellings = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    numbers: list[int] = []

    for i in range(len(line)):
        for spell in spellings.keys():
            if line[i:].startswith(spell):
                numbers.append(spellings[spell])
                break
        if line[i].isdigit():
            numbers.append(int(line[i]))

    return numbers


sum_calib = 0
for line in contents.split("\n"):
    numbers = transform_spelling(line)
    sum_calib += (numbers[0] * 10) + numbers[-1]

print(f"Result: {sum_calib}")  # Result: 54265

# One liner (code golf for fun)
# fmt: off
spellings = {"one": 1,"two": 2,"three": 3,"four": 4,"five": 5,"six": 6,"seven": 7,"eight": 8,"nine": 9}
print(sum([(n[0]*10)+n[-1]for n in[[int(L[i])if L[i].isdigit()else spellings[[s for s in spellings if L[i:].startswith(s)][0]]for i in range(len(L))if L[i].isdigit() or any(L[i:].startswith(s) for s in spellings)] for L in open("input")]]))
# fmt: on
