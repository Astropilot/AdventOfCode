from pathlib import Path

contents = Path(Path(__file__).parent, "input").read_text()
lines = contents.split("\n")

time = int(lines[0].split(":")[1].replace(" ", ""))
distance = int(lines[1].split(":")[1].replace(" ", ""))

ways_to_win = 0
for t in range(time):
    dist = t * (time - t)

    if dist > distance:
        ways_to_win += 1


print(f"Result: {ways_to_win}")  # Result: 20537782
