from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

register_x = 1
last_count: int | None = None
i_program = 0
sum_signal_strength = 0

for cycle in range(1, 220 + 1, 1):
    if cycle in [20, 60, 100, 140, 180, 220]:
        sum_signal_strength += cycle * register_x

    if last_count is None and i_program == len(lines):
        print(f"[{cycle}] Early termination: program buffer empty")
        break
    if last_count is not None:
        register_x += last_count
        last_count = None
        continue

    if lines[i_program] == "noop":
        i_program += 1
        continue

    last_count = int(lines[i_program].split(" ")[1])
    i_program += 1

print(f"Result: {sum_signal_strength}")
