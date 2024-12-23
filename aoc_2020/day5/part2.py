from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]


def compute_seat(boarding_pass: str) -> tuple[int, int]:
    min_row = 0
    max_row = 127
    min_col = 0
    max_col = 7

    for c in boarding_pass[:7]:
        mid = (max_row - min_row) // 2
        if c == "F":
            max_row = min_row + mid
        elif c == "B":
            min_row = min_row + mid + 1

    for c in boarding_pass[7:]:
        mid = (max_col - min_col) // 2
        if c == "L":
            max_col = min_col + mid
        elif c == "R":
            min_col = min_col + mid + 1

    return min_row, min_col


seat_ids = []
for boarding_pass in lines:
    row, column = compute_seat(boarding_pass)
    seat_id = (row * 8) + column
    seat_ids.append(seat_id)

seat_ids.sort()

for i in range(len(seat_ids) - 1):
    if seat_ids[i] + 2 == seat_ids[i + 1]:
        print(f"Result: {seat_ids[i]+1}")
        break
