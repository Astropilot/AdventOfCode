from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

register_x = 1
last_count: int | None = None
i_program = 0
crt_idx = 0

for cycle in range(1, 240 + 1, 1):
    if last_count is None and i_program == len(lines):
        print(f"[{cycle}] Early termination: program buffer empty")
        break

    if crt_idx + 1 >= register_x and crt_idx + 1 <= register_x + 2:
        print("#", end="")
    else:
        print(".", end="")
    crt_idx = (crt_idx + 1) % 40
    if crt_idx == 0:
        print()

    if last_count is not None:
        register_x += last_count
        last_count = None
        continue

    if lines[i_program] == "noop":
        i_program += 1
        continue

    last_count = int(lines[i_program].split(" ")[1])
    i_program += 1
