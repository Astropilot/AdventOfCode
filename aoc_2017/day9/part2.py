from pathlib import Path

stream = Path(Path(__file__).parent, "input").read_text()

total_garbage = 0
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
            total_garbage += 1
    else:
        if c == "<":
            garbage_mode = True

print(f"Result: {total_garbage}")
