from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    strings = [line.rstrip("\n") for line in f]

total_code = 0
total_encode = 0

for string in strings:
    total_code += len(string)

    string_encode = '"'
    i = 0

    for c in string:
        if c == '"':
            string_encode += '\\"'
        elif c == "\\":
            string_encode += "\\\\"
        else:
            string_encode += c

    string_encode += '"'

    total_encode += len(string_encode)

print(f"Result: {total_encode - total_code}")
