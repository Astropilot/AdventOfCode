import datetime
import operator
from pathlib import Path

events: list[tuple[datetime.datetime, str]] = []

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

for line in lines:
    timestamp_raw, event = line.split("]")

    timestamp = datetime.datetime.strptime(timestamp_raw[1:], "%Y-%m-%d %H:%M")  # noqa: DTZ007
    event = event[1:]

    events.append((timestamp, event))

events.sort(key=lambda e: e[0])

sleeptime_per_guard: dict[int, int] = {}
asleep_minute_counter: dict[int, dict[int, int]] = {}

last_guard: int = -1
last_asleep: datetime.datetime = datetime.datetime.now()  # noqa: DTZ005

for timestamp, event in events:
    if event.startswith("Guard"):
        guard_id = int(event.split(" ")[1][1:])
        last_guard = guard_id
    elif event == "falls asleep":
        last_asleep = timestamp
    else:  # wakes up
        minutes = timestamp.minute - last_asleep.minute
        sleeptime_per_guard[last_guard] = (
            sleeptime_per_guard.get(last_guard, 0) + minutes
        )
        guard_data = asleep_minute_counter.setdefault(last_guard, {})

        for m in range(last_asleep.minute, timestamp.minute):
            guard_data[m] = guard_data.get(m, 0) + 1

candidate_guard = max(sleeptime_per_guard.items(), key=operator.itemgetter(1))[0]

candidate_minute = max(
    asleep_minute_counter[candidate_guard].items(), key=operator.itemgetter(1)
)[0]

print(candidate_guard * candidate_minute)
