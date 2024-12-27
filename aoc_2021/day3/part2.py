import typing as t
from pathlib import Path

with Path(Path(__file__).parent, "input").open() as f:
    lines = [line.rstrip("\n") for line in f]


def find_bits_criteria(idx: int, lines: list[str], oxygen: bool) -> t.Literal["0", "1"]:
    bit0 = 0
    bit1 = 0
    for line in lines:
        if line[idx] == "0":
            bit0 += 1
        else:
            bit1 += 1
    if bit0 == bit1:
        return "1" if oxygen else "0"
    return ("0" if bit0 > bit1 else "1") if oxygen else ("1" if bit0 > bit1 else "0")


bit_crit_oxy = find_bits_criteria(0, lines, True)
bit_crit_co2 = find_bits_criteria(0, lines, False)
candidates_oxy = list(filter(lambda line: line[0] == bit_crit_oxy, lines))
candidates_co2 = list(filter(lambda line: line[0] == bit_crit_co2, lines))

for bit_idx in range(1, len(lines[0])):
    if len(candidates_oxy) == 1 and len(candidates_co2) == 1:
        break

    bit_crit_oxy = find_bits_criteria(bit_idx, candidates_oxy, True)
    bit_crit_co2 = find_bits_criteria(bit_idx, candidates_co2, False)

    if len(candidates_oxy) > 1:
        candidates_oxy = list(
            filter(lambda line: line[bit_idx] == bit_crit_oxy, candidates_oxy)
        )
    if len(candidates_co2) > 1:
        candidates_co2 = list(
            filter(lambda line: line[bit_idx] == bit_crit_co2, candidates_co2)
        )

result = int(candidates_oxy[0], 2) * int(candidates_co2[0], 2)

print(f"Result: {result}")
