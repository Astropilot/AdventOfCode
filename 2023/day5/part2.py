import math
from pathlib import Path

contents = Path(Path(__file__).parent, "input").read_text()
lines_blocks = [b.split("\n") for b in contents.split("\n\n")]
seeds = tuple(map(int, lines_blocks[0][0].split(": ")[1].split(" ")))

ranges = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds) - 1, 2)]

for block in lines_blocks[1:]:
    next_start = 0
    mapping: list[tuple[int, int, int]] = [
        tuple(map(int, line.split(" "))) for line in block[1:]
    ]
    full_mapping: list[tuple[int, int, int]] = []

    mapping.sort(key=lambda m: m[1])

    for dst_start, src_start, length in mapping:
        if next_start != src_start:
            full_mapping.append((next_start, next_start, src_start - next_start + 1))
        full_mapping.append((dst_start, src_start, length))
        next_start = src_start + length
    full_mapping.append((next_start, next_start, math.inf))

    next_ranges: list[tuple[int, int]] = []
    for range_start, range_end in ranges:
        for dst_start, src_start, length in full_mapping:
            if src_start <= range_end and range_start <= (src_start + length - 1):
                next_ranges.append(
                    (
                        dst_start + max(range_start, src_start) - src_start,
                        dst_start
                        + min(range_end, (src_start + length - 1))
                        - src_start,
                    )
                )

    ranges = next_ranges

print(f"Result {min(low for low, _ in ranges)}")  # Result: 27992443
