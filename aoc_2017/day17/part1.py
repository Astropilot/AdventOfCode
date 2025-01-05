from pathlib import Path

shift = int(Path(Path(__file__).parent, "input").read_text())

buffer = [0]
current_pos = 0

for count in range(1, 2017 + 1):
    i = (current_pos + shift) % len(buffer)
    buffer.insert(i + 1, count)
    current_pos = i + 1

print(f"Result: {buffer[current_pos+1]}")
