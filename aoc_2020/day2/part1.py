from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

passwords_valid = 0
for line in lines:
    pwd_policy, password = line.split(": ")
    letter_policy = pwd_policy[-1]
    min_letter, max_letter = map(int, pwd_policy[:-2].split("-"))

    letter_count = password.count(letter_policy)
    if min_letter <= letter_count <= max_letter:
        passwords_valid += 1

print(f"Result: {passwords_valid}")
