from pathlib import Path

contents = Path(Path(__file__).parent, "input").read_text()

fishes_per_life: dict[int, int] = {}

for fish in map(int, contents.split(",")):
    fishes_per_life[fish] = fishes_per_life.setdefault(fish, 0) + 1

for _ in range(256):
    new_fishes_per_life: dict[int, int] = {}
    for life, fish_count in fishes_per_life.items():
        if life == 0:
            new_fishes_per_life[6] = new_fishes_per_life.setdefault(6, 0) + fish_count
            new_fishes_per_life[8] = new_fishes_per_life.setdefault(8, 0) + fish_count
            continue
        new_fishes_per_life[life - 1] = (
            new_fishes_per_life.setdefault(life - 1, 0) + fish_count
        )

    fishes_per_life = new_fishes_per_life

print(f"Result: {sum(fishes_per_life.values())}")
