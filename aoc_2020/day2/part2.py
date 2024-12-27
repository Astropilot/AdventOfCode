from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

passwords_valid = 0
for line in lines:
    pwd_policy, password = line.split(": ")
    letter_policy = pwd_policy[-1]
    pos_1, pos_2 = map(int, pwd_policy[:-2].split("-"))

    if (
        password[pos_1 - 1] == letter_policy or password[pos_2 - 1] == letter_policy
    ) and password[pos_1 - 1] != password[pos_2 - 1]:
        passwords_valid += 1

print(f"Result: {passwords_valid}")
