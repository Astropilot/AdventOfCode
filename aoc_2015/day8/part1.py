from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    strings = [line.rstrip("\n") for line in f]

total_code = 0
total_memory = 0

for string in strings:
    total_code += len(string)

    # One way of "cheating", no fun but works:
    # total_memory += eval(f"len({string})")

    string = string[1:-1]
    string_len = 0
    i = 0

    while i < len(string):
        string_len += 1

        if string[i] != "\\":
            i += 1
            continue
        if string[i + 1] in ('"', "\\"):
            i += 2
            continue
        i += 4

    total_memory += string_len

print(f"Result: {total_code - total_memory}")
