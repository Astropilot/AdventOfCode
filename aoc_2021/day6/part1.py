from pathlib import Path

contents = Path(Path(__file__).parent, "input").read_text()

fishes = list(map(int, contents.split(",")))

for _ in range(80):
    new_fishes: list[int] = []
    for idx, fish in enumerate(fishes):
        if fish == 0:
            fishes[idx] = 6
            new_fishes.append(8)
            continue
        fishes[idx] = fish - 1
    fishes.extend(new_fishes)

print(f"Result: {len(fishes)}")
