from itertools import pairwise
from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    reports = [list(map(int, line.split())) for line in f]

report_counter = 0

for report in reports:
    canditates = [list(report) for _ in report]
    for i in range(len(canditates)):
        canditates[i].pop(i)

    is_report_safe = False

    for candidate in canditates:
        last_direction = None
        is_candidate_safe = True
        for a, b in pairwise(candidate):
            diff_direction = "dec" if a - b > 0 else "inc"
            if not (1 <= abs(a - b) <= 3):
                is_candidate_safe = False
                break
            if last_direction is not None and diff_direction != last_direction:
                is_candidate_safe = False
                break
            last_direction = diff_direction
        if is_candidate_safe:
            is_report_safe = True

    if is_report_safe:
        report_counter += 1

print(f"Result: {report_counter}")
