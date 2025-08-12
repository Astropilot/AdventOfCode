from pathlib import Path

contents = Path(Path(__file__).parent, "input").read_text()

for _ in range(40):
    output = ""

    counter = 1
    last_digit = contents[0]
    for c in contents[1:]:
        if c == last_digit:
            counter += 1
        elif counter > 0:
            output += str(counter) + last_digit
            counter = 1
        last_digit = c

    output += str(counter) + last_digit
    contents = output

print(f"Result: {len(contents)}")
