from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

i = 0
current_passport: dict[str, str] = {}
valid_passports = 0

while i < len(lines):
    if lines[i] == "":
        if all(
            m in current_passport
            for m in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
        ):
            valid_passports += 1
        i += 1
        current_passport = {}
        continue

    for keyvalue in lines[i].split(" "):
        key, value = keyvalue.split(":")
        current_passport[key] = value

    i += 1

if all(
    m in current_passport for m in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
):
    valid_passports += 1

print(f"Result: {valid_passports}")  # Result: 222
