from pathlib import Path

stream = Path(Path(__file__).parent, "input").read_text()

total_score = 0
depth = 1
garbage_mode = False
ignore_next_c = False

for c in stream:
    if ignore_next_c:
        ignore_next_c = False
        continue

    if garbage_mode:
        if c == "!":
            ignore_next_c = True
        elif c == ">":
            garbage_mode = False
        else:
            # We recognize every other characters but don't do anything
            pass
    else:
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            total_score += depth
        elif c == "<":
            garbage_mode = True
        elif c == ",":
            # No special treatment, we just recognize this character
            pass
        else:
            raise ValueError(f"Unknown character in group mode: {c}")

print(f"Result: {total_score}")
