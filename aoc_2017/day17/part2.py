from pathlib import Path

shift = int(Path(Path(__file__).parent, "input").read_text())

buffer_size = 1
current_pos = 0
last_zero_pos = 0
last_value_written_after = 0

for count in range(1, 50000000 + 1):
    i = (current_pos + shift) % buffer_size

    if i == last_zero_pos:
        last_value_written_after = count
    if i < last_zero_pos:
        last_zero_pos += 1

    buffer_size += 1
    current_pos = i + 1

print(f"Result: {last_value_written_after}")
