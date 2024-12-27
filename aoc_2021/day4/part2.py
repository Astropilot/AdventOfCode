from dataclasses import dataclass
from pathlib import Path


@dataclass
class Board:
    grid: list[list[int]]
    marked: list[list[bool]]
    winned: tuple[int, int] | None

    def mark_number(self, n: int) -> None:
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] == n:
                    self.marked[y][x] = True

    def is_winning(self) -> bool:
        for y in range(len(self.grid)):
            if all(m for m in self.marked[y]):
                return True

        for x in range(len(self.grid[0])):
            if all(self.marked[y][x] for y in range(len(self.grid))):
                return True

        return False

    def score(self) -> int:
        score = 0

        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if not self.marked[y][x]:
                    score += self.grid[y][x]

        return score


with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]

numbers_to_draw = list(map(int, lines[0].split(",")))
boards: list[Board] = []
board: Board = None  # type: ignore

for line in lines[1:]:
    if line == "":
        if board is not None:
            boards.append(board)
        board = Board([], [], None)
        continue
    numbers_row = list(map(int, filter(lambda n: n != "", line.split(" "))))

    board.grid.append(numbers_row)
    board.marked.append([False for _ in range(len(numbers_row))])
boards.append(board)

winning_idx = 1
for number in numbers_to_draw:
    boards_left = [b for b in boards if b.winned is None]
    for board in boards_left:
        board.mark_number(number)

        if board.is_winning():
            board.winned = (winning_idx, number)
            winning_idx += 1

    if len(boards_left) == 0:
        break

boards_s = sorted(
    [b for b in boards if b.winned is not None],
    key=lambda b: b.winned[0],  # type: ignore
    reverse=True,
)
last_winner = boards_s[0]
assert last_winner.winned is not None

print(f"Result: {last_winner.winned[1] * last_winner.score()}")
