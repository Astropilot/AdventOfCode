from pathlib import Path

banks = [int(c) for c in Path(Path(__file__).parent, "input").read_text().split("\t")]

visited_configs: set[str] = {"".join(map(str, banks))}

cycle = 0

while True:
    cycle += 1
    max_bank = max(banks)
    idx_max_bank = banks.index(max_bank)

    banks[idx_max_bank] = 0

    i_bank = (idx_max_bank + 1) % len(banks)
    for _ in range(max_bank):
        banks[i_bank] += 1
        i_bank = (i_bank + 1) % len(banks)

    config = "".join(map(str, banks))

    if config in visited_configs:
        break
    visited_configs.add(config)

print(f"Result: {cycle}")
