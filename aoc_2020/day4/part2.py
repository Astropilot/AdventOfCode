import re
from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

i = 0
current_passport: dict[str, str] = {}
valid_passports = 0


def check_valid_passport(passport: dict[str, str]) -> bool:
    if not all(
        m in current_passport for m in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    ):
        return False

    byr = int(passport["byr"])
    if not (1920 <= byr <= 2002):
        return False
    iyr = int(passport["iyr"])
    if not (2010 <= iyr <= 2020):
        return False
    eyr = int(passport["eyr"])
    if not (2020 <= eyr <= 2030):
        return False
    hgt = passport["hgt"]
    if hgt.endswith("cm"):
        if not (150 <= int(hgt[:-2]) <= 193):
            return False
    elif hgt.endswith("in"):
        if not (59 <= int(hgt[:-2]) <= 76):
            return False
    else:
        return False
    hcl = passport["hcl"]
    if re.match(r"#[0-9a-f]{6}", hcl) is None:
        return False
    ecl = passport["ecl"]
    if ecl not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
        return False
    pid = passport["pid"]
    if not (len(pid) == 9 and pid.isdigit()):
        return False

    return True


while i < len(lines):
    if lines[i] == "":
        if check_valid_passport(current_passport):
            valid_passports += 1
        i += 1
        current_passport = {}
        continue

    for keyvalue in lines[i].split(" "):
        key, value = keyvalue.split(":")
        current_passport[key] = value

    i += 1

if check_valid_passport(current_passport):
    valid_passports += 1

print(f"Result: {valid_passports}")  # Result: 140
