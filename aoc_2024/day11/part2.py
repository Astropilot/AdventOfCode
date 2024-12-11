from functools import cache
from pathlib import Path

contents = Path(Path(__file__).parent, "input").read_text()

stones: list[int] = list(map(int, contents.split()))


@cache
def count_stones(stone: int, blink: int, max_blink: int) -> int:
    if stone == 0:
        if blink == max_blink:
            return 1
        return count_stones(1, blink + 1, max_blink)

    stone_str = str(stone)

    if len(stone_str) % 2 == 0:
        if blink == max_blink:
            return 2

        return count_stones(
            int(stone_str[: len(stone_str) // 2]), blink + 1, max_blink
        ) + count_stones(int(stone_str[len(stone_str) // 2 :]), blink + 1, max_blink)

    if blink == max_blink:
        return 1

    return count_stones(stone * 2024, blink + 1, max_blink)


count = 0

for stone in stones:
    count += count_stones(stone, 1, 75)

print(f"Result: {count}")  # Result: 221280540398419
