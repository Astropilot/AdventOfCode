from pathlib import Path

contents = Path(Path(__file__).parent, "input").read_text()

stones: list[int] = list(map(int, contents.split()))

for _ in range(25):
    new_stones: list[int] = []

    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            new_stones.append(int(stone_str[: len(stone_str) // 2]))
            new_stones.append(int(stone_str[len(stone_str) // 2 :]))
        else:
            new_stones.append(stone * 2024)

    stones = new_stones

print(f"Result: {len(stones)}")  # Result: 185205
