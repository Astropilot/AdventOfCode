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
        guard_data = asleep_minute_counter.setdefault(last_guard, {})

        for m in range(last_asleep.minute, timestamp.minute):
            guard_data[m] = guard_data.get(m, 0) + 1

most_asleep_minute_per_guard: list[tuple[int, int, int]] = []

for guard_id in asleep_minute_counter:
    candidate_minute = max(
        asleep_minute_counter[guard_id].items(), key=operator.itemgetter(1)
    )
    most_asleep_minute_per_guard.append((guard_id, *candidate_minute))

candidate = max(most_asleep_minute_per_guard, key=operator.itemgetter(2))

print(candidate[0] * candidate[1])
