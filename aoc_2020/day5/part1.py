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


highest_seatid = 0
for boarding_pass in lines:
    row, column = compute_seat(boarding_pass)
    seat_id = (row * 8) + column
    if seat_id > highest_seatid:
        highest_seatid = seat_id

print(f"Result: {highest_seatid}")
