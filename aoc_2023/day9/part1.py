from pathlib import Path

contents = Path(Path(__file__).parent, "input").read_text()
lines = contents.split("\n")

sum_vals = 0
for line in lines:
    history = list(map(int, line.split(" ")))
    sequences: list[list[int]] = []

    s: list[int] = []
    for i in range(len(history) - 1):
        s.append(history[i + 1] - history[i])
    sequences.append(s)

    while not all(s == 0 for s in sequences[-1]):
        s = []
        current_seq = sequences[-1]
        for i in range(len(current_seq) - 1):
            s.append(current_seq[i + 1] - current_seq[i])
        sequences.append(s)

    val = sum(s[-1] for s in sequences) + history[-1]
    sum_vals += val

print(f"Result: {sum_vals}")
