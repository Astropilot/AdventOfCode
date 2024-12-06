import re
from pathlib import Path

contents = Path(Path(__file__).parent, "input").read_text()
lines = contents.split("\n")

times = list(map(int, re.findall(r"\d+", lines[0])))
distances = list(map(int, re.findall(r"\d+", lines[1])))

assert len(times) == len(distances)

sum_races = 1
for i in range(len(times)):
    time = times[i]
    distance = distances[i]
    ways_to_win = 0

    for t in range(time):
        dist = t * (time - t)

        if dist > distance:
            ways_to_win += 1

    sum_races *= ways_to_win


print(f"Result: {sum_races}")  # Result: 170000
