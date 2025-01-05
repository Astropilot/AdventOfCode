import typing as t
from dataclasses import dataclass
from math import sqrt
from pathlib import Path

type PixelState = t.Literal["#", "."]


@dataclass(frozen=True)
class SquareMatrix:
    grid: tuple[tuple[PixelState, ...], ...]
    size: int

    @staticmethod
    def construct(input: str) -> "SquareMatrix":
        rows = input.split("/")
        return SquareMatrix(tuple(tuple(row) for row in rows), len(rows))  # type: ignore

    @staticmethod
    def join(squares: "list[SquareMatrix]") -> "SquareMatrix":
        split = sqrt(len(squares))
        size = split * squares[0].size
        i_row = -(squares[0].size)
        grid: list[tuple[PixelState, ...]] = []

        for i, square in enumerate(squares):
            if i % split == 0:
                grid += square.grid
                i_row += square.size
            else:
                for j in range(square.size):
                    grid[i_row + j] += square.grid[j]

        return SquareMatrix(tuple(grid), int(size))

    def flip(self, direction: t.Literal["v", "h"]) -> "SquareMatrix":
        if direction == "h":
            return SquareMatrix(self.grid[::-1], self.size)
        elif direction == "v":
            return SquareMatrix(tuple(row[::-1] for row in self.grid), self.size)

    def rotate(self, direction: t.Literal["l", "r"]) -> "SquareMatrix":
        if direction == "r":
            return SquareMatrix(tuple(zip(*self.grid[::-1], strict=True)), self.size)
        elif direction == "l":
            return SquareMatrix(tuple(zip(*self.grid, strict=True))[::-1], self.size)

    def divide(self) -> "list[SquareMatrix]":
        if self.size % 2 == 0:
            subsize = 2
        elif self.size % 3 == 0:
            subsize = 3
        else:
            raise ValueError(f"Invalid square size {self.size}!")

        sub_squares: list[SquareMatrix] = []

        for row_i in range(0, len(self.grid), subsize):
            for col_i in range(0, len(self.grid), subsize):
                square: tuple[tuple[PixelState, ...], ...] = ()
                for cc_i in range(0, subsize):
                    row = self.grid[row_i + cc_i][col_i : col_i + subsize]
                    square += (row,)
                sub_squares.append(SquareMatrix(square, subsize))

        return sub_squares

    def print(self) -> None:
        for row in self.grid:
            for c in row:
                print(c, end="")
            print()
        print()


with Path(Path(__file__).parent, "input").open() as f:
    rules = [line.rstrip("\n") for line in f]

rules_2x: dict[SquareMatrix, SquareMatrix] = {}
rules_3x: dict[SquareMatrix, SquareMatrix] = {}
image = SquareMatrix.construct(".#./..#/###")

for rule in rules:
    r_in, r_out = rule.split(" => ")

    m_in = SquareMatrix.construct(r_in)
    m_out = SquareMatrix.construct(r_out)

    if m_in.size == 2:
        rules_2x[m_in] = m_out
        rules_2x[m_in.flip("v")] = m_out
        rules_2x[m_in.flip("h")] = m_out
        rules_2x[m_in.flip("v").flip("h")] = m_out
        rules_2x[m_in.flip("h").flip("v")] = m_out
        rules_2x[m_in.rotate("l")] = m_out
        rules_2x[m_in.rotate("r")] = m_out
        rules_2x[m_in.rotate("l").flip("v")] = m_out
        rules_2x[m_in.rotate("l").flip("h")] = m_out
        rules_2x[m_in.rotate("r").flip("v")] = m_out
        rules_2x[m_in.rotate("r").flip("h")] = m_out
    else:
        rules_3x[m_in] = m_out
        rules_3x[m_in.flip("v")] = m_out
        rules_3x[m_in.flip("h")] = m_out
        rules_3x[m_in.flip("v").flip("h")] = m_out
        rules_3x[m_in.flip("h").flip("v")] = m_out
        rules_3x[m_in.rotate("l")] = m_out
        rules_3x[m_in.rotate("r")] = m_out
        rules_3x[m_in.rotate("l").flip("v")] = m_out
        rules_3x[m_in.rotate("l").flip("h")] = m_out
        rules_3x[m_in.rotate("r").flip("v")] = m_out
        rules_3x[m_in.rotate("r").flip("h")] = m_out

for _ in range(5):
    subs = image.divide()
    new_subs: list[SquareMatrix] = []

    for sub in subs:
        if sub.size == 2:
            new_subs.append(rules_2x[sub])
        else:
            new_subs.append(rules_3x[sub])

    image = SquareMatrix.join(new_subs)

r = sum(sum(1 if c == "#" else 0 for c in row) for row in image.grid)

print(f"Result: {r}")
